#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CANON = ROOT / "canonical" / "current"
MANIFEST = CANON / "SOURCE_MANIFEST.json"
FILES = {
    "User": "Garden_User_v15.5_FULL_2026-09-12.txt",
    "System": "Garden_System_v15.5_FULL_2026-09-12.txt",
    "Technical": "Garden_Technical_v15.5_FULL_2026-09-12.txt",
    "Annexure": "Garden_Annexure_v15.5_FULL_2026-09-12.txt",
    "Theories": "Garden_Theories_v15.5_FULL_2026-09-12.txt",
}


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def expected_manifest() -> dict:
    file_rows: dict[str, dict] = {}
    root_items: list[dict] = []
    for role, name in FILES.items():
        path = CANON / name
        raw = path.read_bytes()
        digest = sha256(raw)
        row = {"name": name, "bytes": len(raw), "sha256": digest}
        file_rows[role] = row
        root_items.append({"role": role, **row})
    root_payload = json.dumps(
        sorted(root_items, key=lambda x: x["role"]),
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    ).encode("utf-8")
    return {
        "schema": "GardenCanonicalSourceManifest/v1",
        "release": "Garden v15.5",
        "gsl": "v45.1",
        "date": "2026-09-12",
        "files": file_rows,
        "source_root_algorithm": "sha256(canonical-json(sorted role/name/bytes/sha256 rows))",
        "source_root_sha256": sha256(root_payload),
        "immutability": "published predecessor files are not rewritten in place",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--write", action="store_true")
    mode.add_argument("--print", dest="print_only", action="store_true")
    args = parser.parse_args()

    expected = expected_manifest()
    rendered = json.dumps(expected, indent=2, ensure_ascii=False) + "\n"
    if args.print_only:
        print(rendered, end="")
        return 0
    if args.write:
        MANIFEST.write_text(rendered, encoding="utf-8")
        return 0

    current = json.loads(MANIFEST.read_text(encoding="utf-8"))
    if current != expected:
        print("SOURCE_MANIFEST_MISMATCH")
        print("EXPECTED_MANIFEST_BEGIN")
        print(rendered, end="")
        print("EXPECTED_MANIFEST_END")
        return 1
    print("SOURCE_MANIFEST_OK", expected["source_root_sha256"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
