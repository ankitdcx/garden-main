#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

RIGHT_RE = re.compile(r"^@D\|RIGHT-(\d{3})\|(.*)$")


def extract_rights(text: str) -> dict[int, str]:
    rights: dict[int, str] = {}
    for line in text.splitlines():
        match = RIGHT_RE.match(line.strip())
        if not match:
            continue
        number = int(match.group(1))
        if number in rights:
            raise ValueError(f"duplicate RIGHT-{number:03d}")
        rights[number] = match.group(2).strip()
    return rights


def ordered_right_ids(rights: dict[int, str]) -> list[int]:
    active = [n for n in range(1, 26) if n in rights]
    non_active = [n for n in (26, 27) if n in rights]
    remainder = sorted(set(rights) - set(active) - set(non_active))
    return active + non_active + remainder


def build_view(rights: dict[int, str]) -> dict:
    order = ordered_right_ids(rights)
    return {
        "schema": "GardenRightsReaderView/v1",
        "semantic_identity_changed": False,
        "note": (
            "Display ordering is non-semantic. Active RIGHT-001..025 are shown first, "
            "then explicit non-active RIGHT-026 RESERVED and RIGHT-027 ON_HOLD."
        ),
        "rights": [
            {"id": f"RIGHT-{number:03d}", "text": rights[number]}
            for number in order
        ],
    }


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("source")
    p.add_argument("--output")
    args = p.parse_args()
    rights = extract_rights(Path(args.source).read_text(encoding="utf-8"))
    view = build_view(rights)
    rendered = json.dumps(view, indent=2, ensure_ascii=False) + "\n"
    if args.output:
        Path(args.output).write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
