#!/usr/bin/env python3
"""Fail if a candidate canonical successor differs from the admitted expected diff.

The manifest names predecessor/candidate files, the admitted delta IDs affecting
that file, and the SHA-256 of the exact normalized unified diff expected for the
file. Any unexplained difference is a materialization defect.
"""
from __future__ import annotations

import argparse
import difflib
import hashlib
import json
from pathlib import Path


def digest_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def normalized_diff(old_path: Path, new_path: Path) -> str:
    old = old_path.read_text(encoding="utf-8").splitlines()
    new = new_path.read_text(encoding="utf-8").splitlines()
    lines = difflib.unified_diff(
        old,
        new,
        fromfile=old_path.name,
        tofile=new_path.name,
        lineterm="",
    )
    return "\n".join(lines) + ("\n" if old != new else "")


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("manifest", help="GardenSuccessorDeltaManifest/v1 JSON")
    p.add_argument("--write-observed-diffs", help="optional directory for observed .diff files")
    args = p.parse_args()

    manifest_path = Path(args.manifest)
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if manifest.get("schema") != "GardenSuccessorDeltaManifest/v1":
        raise SystemExit("unsupported manifest schema")
    entries = manifest.get("files") or []
    if len(entries) != 5:
        raise SystemExit(f"successor manifest must bind exactly five canonical files, found {len(entries)}")

    failures = []
    observed = []
    outdir = Path(args.write_observed_diffs) if args.write_observed_diffs else None
    if outdir:
        outdir.mkdir(parents=True, exist_ok=True)

    for entry in entries:
        old_path = Path(entry["predecessor"])
        new_path = Path(entry["candidate"])
        if not old_path.is_file() or not new_path.is_file():
            failures.append({"file": entry, "reason": "missing predecessor or candidate file"})
            continue
        diff = normalized_diff(old_path, new_path)
        actual = digest_text(diff)
        expected = entry.get("expected_diff_sha256")
        delta_ids = entry.get("delta_ids") or []
        changed = bool(diff)
        if changed and not delta_ids:
            failures.append({"candidate": str(new_path), "reason": "changed file has no admitted delta_ids"})
        if actual != expected:
            failures.append({
                "candidate": str(new_path),
                "reason": "observed diff hash does not match admitted expected diff",
                "expected_diff_sha256": expected,
                "observed_diff_sha256": actual,
            })
        observed.append({
            "predecessor": str(old_path),
            "candidate": str(new_path),
            "delta_ids": delta_ids,
            "changed": changed,
            "observed_diff_sha256": actual,
        })
        if outdir:
            (outdir / f"{new_path.name}.diff").write_text(diff, encoding="utf-8")

    receipt = {
        "schema": "GardenSuccessorDriftReceipt/v1",
        "predecessor_release": manifest.get("predecessor_release"),
        "candidate_release": manifest.get("candidate_release"),
        "observed": observed,
        "status": "PASS" if not failures else "FAIL",
        "failures": failures,
        "rule": "candidate == predecessor + exactly the admitted expected per-file diffs",
    }
    print(json.dumps(receipt, indent=2, ensure_ascii=False))
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
