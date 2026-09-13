#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "implementation"))

from garden_kernel.evolution_transport import (  # noqa: E402
    evaluate_production_request,
    load_source_identity,
)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument(
        "--manifest",
        default=str(ROOT / "canonical" / "current" / "SOURCE_MANIFEST.json"),
    )
    args = parser.parse_args()

    request = json.loads(Path(args.input).read_text(encoding="utf-8"))
    identity = load_source_identity(args.manifest)
    receipt = evaluate_production_request(request, identity)

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(receipt, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({
        "action_id": receipt["action_id"],
        "verb": receipt["verb"],
        "decision": receipt["decision"],
        "reasons": receipt["reasons"],
    }, ensure_ascii=False))

    if receipt["decision"] == "ALLOW":
        return 0
    if receipt["decision"] == "ESCALATE":
        return 3
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
