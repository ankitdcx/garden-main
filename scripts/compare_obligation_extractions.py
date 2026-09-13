#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "implementation"))

from garden_kernel.source_binding import SourceBinding, diff_source_bindings  # noqa: E402


def load_bindings(path: Path) -> list[SourceBinding]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    raw = payload.get("source_bindings")
    if not isinstance(raw, list):
        raise SystemExit(f"{path} does not contain source_bindings; regenerate with extraction schema v0.2+")
    return [SourceBinding(**item) for item in raw]


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("previous")
    p.add_argument("current")
    p.add_argument("--output", default="obligation-binding-diff.json")
    args = p.parse_args()

    previous = load_bindings(Path(args.previous))
    current = load_bindings(Path(args.current))
    diff = diff_source_bindings(previous, current)
    Path(args.output).write_text(
        json.dumps(diff, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(
        json.dumps(
            {
                "added": len(diff["added"]),
                "removed": len(diff["removed"]),
                "changed": len(diff["changed"]),
                "unchanged": diff["unchanged_count"],
                "stale_candidates": len(diff["stale_binding_keys"]),
            },
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
