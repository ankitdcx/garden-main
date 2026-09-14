#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

SECRET_PATTERNS = [
    ("PEM_PRIVATE_KEY", re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----")),
    ("GITHUB_TOKEN", re.compile(r"\b(?:ghp|gho|ghu|ghs|ghr)_[A-Za-z0-9]{20,}\b|\bgithub_pat_[A-Za-z0-9_]{20,}\b")),
    ("OPENAI_KEY", re.compile(r"\bsk-(?:proj-)?[A-Za-z0-9_-]{20,}\b")),
    ("GOOGLE_API_KEY", re.compile(r"\bAIza[0-9A-Za-z_-]{30,}\b")),
    ("AWS_ACCESS_KEY", re.compile(r"\bAKIA[0-9A-Z]{16}\b")),
    ("ASSIGNED_SECRET", re.compile(r"(?i)\b(?:OPENROUTER_API_KEY|GEMINI_API_KEY|DEEPSEEK_API_KEY|ANTHROPIC_API_KEY|OPENAI_API_KEY|AWS_SECRET_ACCESS_KEY)\s*[:=]\s*['\"]?[A-Za-z0-9_./+=-]{12,}")),
]
EMAIL_RE = re.compile(r"(?i)\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b")
SUSPICIOUS_NAMES = (".env", "credentials", "secret", "private_key", "id_rsa", "id_ed25519", ".pem", ".p12", ".pfx")
MAX_BLOB = 2_000_000


def run(*args: str, check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(args, cwd=ROOT, text=True, capture_output=True, check=check)


def blob_bytes(sha: str) -> bytes:
    proc = subprocess.run(["git", "cat-file", "blob", sha], cwd=ROOT, capture_output=True, check=True)
    return proc.stdout


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="/tmp/garden-main-publication-readiness.json")
    args = parser.parse_args()

    # The workflow fetches all branches/tags before invoking this script.
    objects = run("git", "rev-list", "--objects", "--all").stdout.splitlines()
    seen: set[str] = set()
    secret_findings = []
    privacy_findings = []
    filename_findings = []
    skipped_large = []
    blob_count = 0

    for line in objects:
        if not line.strip():
            continue
        parts = line.split(" ", 1)
        sha = parts[0]
        path = parts[1] if len(parts) > 1 else "<unnamed>"
        if sha in seen:
            continue
        seen.add(sha)
        kind = run("git", "cat-file", "-t", sha, check=False)
        if kind.returncode != 0 or kind.stdout.strip() != "blob":
            continue
        blob_count += 1
        size_proc = run("git", "cat-file", "-s", sha, check=False)
        try:
            size = int(size_proc.stdout.strip())
        except Exception:
            continue
        lower_path = path.lower()
        if any(token in lower_path for token in SUSPICIOUS_NAMES):
            filename_findings.append({"path": path, "object": sha, "reason": "SUSPICIOUS_FILENAME"})
        if size > MAX_BLOB:
            skipped_large.append({"path": path, "object": sha, "size": size})
            continue
        data = blob_bytes(sha)
        if b"\x00" in data[:4096]:
            continue
        text = data.decode("utf-8", errors="replace")
        for name, pattern in SECRET_PATTERNS:
            if pattern.search(text):
                secret_findings.append({"path": path, "object": sha, "pattern": name})
        emails = sorted(set(EMAIL_RE.findall(text)))
        for email in emails:
            low = email.lower()
            if low.endswith("@users.noreply.github.com") or low.endswith("@github.com"):
                continue
            privacy_findings.append({
                "path": path,
                "object": sha,
                "kind": "EMAIL_ADDRESS",
                "value_sha256": hashlib.sha256(low.encode()).hexdigest(),
                "value_redacted": low[:2] + "***@" + low.split("@", 1)[1],
            })

    refs = run("git", "for-each-ref", "--format=%(refname):%(objectname)", "refs/heads", "refs/remotes/origin", "refs/tags").stdout.splitlines()
    receipt = {
        "schema": "GardenRepositoryPublicationReadinessReceipt/v1",
        "repository": "ankitdcx/garden-main",
        "scope": "ALL_REACHABLE_LOCAL_AND_FETCHED_REMOTE_BRANCH_TAG_HISTORY",
        "refs": sorted(refs),
        "unique_object_count": len(seen),
        "blob_count": blob_count,
        "secret_findings": secret_findings,
        "privacy_findings": privacy_findings,
        "suspicious_filename_findings": filename_findings,
        "skipped_large_blobs": skipped_large,
        "result": "FAIL_SECRET" if secret_findings else ("REVIEW_PRIVACY" if privacy_findings or filename_findings or skipped_large else "PASS"),
        "publication_authorized": False,
        "boundary": "This audit detects selected credential/privacy patterns in reachable Git history. PASS is publication-readiness evidence, not a guarantee that no sensitive information exists and not authority to change repository visibility.",
    }
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(receipt, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({"result": receipt["result"], "secret_findings": len(secret_findings), "privacy_findings": len(privacy_findings), "suspicious_filenames": len(filename_findings), "skipped_large": len(skipped_large)}, sort_keys=True))
    return 1 if secret_findings else 0


if __name__ == "__main__":
    raise SystemExit(main())
