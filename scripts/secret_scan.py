#!/usr/bin/env python3
"""High-confidence changed-file secret scanner for Garden CI."""
from __future__ import annotations
import argparse, hashlib, json, re, subprocess
from pathlib import Path
RULES={"PRIVATE_KEY_PEM":re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----"),"GITHUB_TOKEN":re.compile(r"\b(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,})\b"),"OPENAI_OR_OPENROUTER_KEY":re.compile(r"\bsk-(?:proj-|or-v1-)?[A-Za-z0-9_-]{20,}\b"),"AWS_ACCESS_KEY_ID":re.compile(r"\bAKIA[0-9A-Z]{16}\b"),"GOOGLE_API_KEY":re.compile(r"\bAIza[0-9A-Za-z_-]{30,}\b"),"HIGH_CONFIDENCE_ASSIGNMENT":re.compile(r"(?ix)\b(?:api[_-]?key|secret|password|access[_-]?token)\b\s*[:=]\s*[\"']([A-Za-z0-9_./+=-]{32,})[\"']")}
PLACEHOLDER_WORDS=("example","placeholder","redacted","changeme","dummy","fake","test-only","<","${")
def _git(*args): return subprocess.check_output(["git",*args],text=True).strip()
def changed_files(base,head):
    out=_git("diff","--name-only","--diff-filter=ACMR",base,head); return [x for x in out.splitlines() if x]
def load_allowlist(path):
    if not path.exists(): return []
    data=json.loads(path.read_text(encoding="utf-8"))
    if data.get("schema")!="GardenSecretScanAllowlist/v1": raise ValueError("unsupported secret-scan allowlist")
    return data.get("entries") or []
def _allowed(path,rule,line,rows):
    h=hashlib.sha256(line.encode()).hexdigest(); return any(r.get("path")==path and r.get("rule")==rule and r.get("line_sha256")==h and str(r.get("reason") or "").strip() for r in rows)
def scan_paths(paths,root=Path("."),allowlist=None):
    allowlist=allowlist or []; findings=[]; scanned=0
    for rel in paths:
        p=root/rel
        if not p.is_file(): continue
        raw=p.read_bytes()
        if b"\x00" in raw: continue
        try: text=raw.decode("utf-8")
        except UnicodeDecodeError: continue
        scanned+=1
        for lineno,line in enumerate(text.splitlines(),1):
            for rule,pattern in RULES.items():
                m=pattern.search(line)
                if not m: continue
                candidate=m.group(1) if rule=="HIGH_CONFIDENCE_ASSIGNMENT" and m.groups() else m.group(0)
                if rule=="HIGH_CONFIDENCE_ASSIGNMENT" and any(w in candidate.lower() for w in PLACEHOLDER_WORDS): continue
                if _allowed(rel,rule,line,allowlist): continue
                findings.append({"path":rel,"line":lineno,"rule":rule,"match_sha256":hashlib.sha256(candidate.encode()).hexdigest()})
    return {"schema":"GardenSecretScanReceipt/v1","scanned_text_files":scanned,"finding_count":len(findings),"findings":findings,"status":"BLOCKED" if findings else "PASS","boundary":"Hashes identify suspected matches without printing credential material."}
def main():
    p=argparse.ArgumentParser(); p.add_argument("--base",required=True); p.add_argument("--head",default="HEAD"); p.add_argument("--allowlist",default="security/secret-scan-allowlist.json"); p.add_argument("--output"); a=p.parse_args()
    receipt=scan_paths(changed_files(a.base,a.head),allowlist=load_allowlist(Path(a.allowlist))); rendered=json.dumps(receipt,indent=2,sort_keys=True)+"\n"
    if a.output: Path(a.output).write_text(rendered,encoding="utf-8")
    print(rendered,end=""); return 0 if receipt["status"]=="PASS" else 2
if __name__=="__main__": raise SystemExit(main())
