#!/usr/bin/env python3
"""Deterministically search the complete current Garden canonical source."""
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path
DEFAULT_ROOT = Path("canonical/current")
def sha256(path: Path) -> str: return hashlib.sha256(path.read_bytes()).hexdigest()
def canonical_files(root: Path) -> list[Path]:
    files=sorted(root.glob("Garden_*_v*_FULL_*.txt"))
    if len(files)!=5: raise SystemExit(f"expected exactly five canonical source files in {root}, found {len(files)}")
    return files
def main() -> int:
    p=argparse.ArgumentParser(); p.add_argument("--root",default=str(DEFAULT_ROOT)); p.add_argument("--term",action="append",required=True); p.add_argument("--output"); p.add_argument("--context",type=int,default=0); args=p.parse_args()
    root=Path(args.root); terms=[t for t in args.term if t.strip()]
    if not terms: raise SystemExit("at least one non-empty --term is required")
    sources=[]; hits=[]
    for path in canonical_files(root):
        digest=sha256(path); lines=path.read_text(encoding="utf-8").splitlines(); sources.append({"file":str(path),"sha256":digest,"line_count":len(lines)}); lowered=[line.casefold() for line in lines]
        for term in terms:
            needle=term.casefold()
            for idx,line in enumerate(lowered):
                if needle not in line: continue
                lo=max(0,idx-args.context); hi=min(len(lines),idx+args.context+1)
                hits.append({"term":term,"file":str(path),"source_sha256":digest,"line":idx+1,"excerpt":"\n".join(lines[lo:hi])})
    receipt={"schema":"GardenCanonicalSearchTrace/v1","coverage":"ALL_FIVE_CURRENT_CANONICAL_FILES_LEXICAL","terms":terms,"sources":sources,"hits":hits,"hit_count_by_term":{term:sum(1 for h in hits if h["term"]==term) for term in terms},"semantic_absence_proved":False,"note":"Zero lexical hits do not prove semantic absence; integrate with obligation/reference evidence."}
    text=json.dumps(receipt,indent=2,ensure_ascii=False)+"\n"
    if args.output:
        out=Path(args.output); out.parent.mkdir(parents=True,exist_ok=True); out.write_text(text,encoding="utf-8")
    else: print(text,end="")
    return 0
if __name__=="__main__": raise SystemExit(main())
