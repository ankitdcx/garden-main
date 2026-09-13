#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from dataclasses import asdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "implementation"))

from garden_kernel.extractor import ObligationExtractor  # noqa: E402

DEFAULT_FILES = [
    "Garden_User_v15.5_FULL_2026-09-12.txt",
    "Garden_System_v15.5_FULL_2026-09-12.txt",
    "Garden_Technical_v15.5_FULL_2026-09-12.txt",
    "Garden_Annexure_v15.5_FULL_2026-09-12.txt",
    "Garden_Theories_v15.5_FULL_2026-09-12.txt",
]


def serialize_manifest(manifest) -> dict:
    return {
        "schema": "GardenObligationExtraction/v0.1",
        "source_hashes": manifest.source_hashes,
        "coverage_complete": manifest.coverage_complete,
        "coverage_note": manifest.coverage_note,
        "total_nonempty_lines": manifest.total_nonempty_lines,
        "classified_lines": manifest.classified_lines,
        "unclassified_lines": manifest.unclassified_lines,
        "anchors_seen": sorted(manifest.anchors_seen),
        "parsed_definition_ids": sorted(manifest.parsed_definition_ids),
        "parsed_schema_names": sorted(manifest.parsed_schema_names),
        "obligation_count": len(manifest.obligations),
        "gap_count": len(manifest.gaps),
        "obligations": [asdict(x) for x in manifest.obligations],
        "gaps": [asdict(x) for x in manifest.gaps],
    }


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--source-dir", default=str(ROOT / "canonical" / "current"))
    p.add_argument("--output", default="obligation-extraction.json")
    args = p.parse_args()

    source_dir = Path(args.source_dir).resolve()
    paths = [source_dir / name for name in DEFAULT_FILES]
    missing = [str(path) for path in paths if not path.is_file()]
    if missing:
        raise SystemExit("Missing canonical source files: " + ", ".join(missing))

    manifest = ObligationExtractor().extract_paths(paths)
    payload = serialize_manifest(manifest)
    Path(args.output).write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(
        json.dumps(
            {
                "source_files": len(payload["source_hashes"]),
                "obligation_count": payload["obligation_count"],
                "gap_count": payload["gap_count"],
                "classified_lines": payload["classified_lines"],
                "unclassified_lines": payload["unclassified_lines"],
                "coverage_complete": payload["coverage_complete"],
            },
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
