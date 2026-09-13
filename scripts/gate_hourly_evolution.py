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
    load_authority_registry,
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
    parser.add_argument(
        "--authority-registry",
        default=str(ROOT / "governance" / "evolution_authority_registry.json"),
    )
    args = parser.parse_args()

    request = json.loads(Path(args.input).read_text(encoding="utf-8"))
    identity = load_source_identity(args.manifest)
    trusted_authorities = load_authority_registry(args.authority_registry, identity)

    # Human approval and independent-review status are intentionally not command-line
    # booleans. They will be enabled only by a later trusted receipt verifier.
    receipt = evaluate_production_request(
        request,
        identity,
        trusted_authorities,
        trusted_human_signoff=False,
        trusted_independent_review=False,
    )

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(receipt, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(
        json.dumps(
            {
                "action_id": receipt["action_id"],
                "verb": receipt["verb"],
                "decision": receipt["decision"],
                "reasons": receipt["reasons"],
            },
            ensure_ascii=False,
        )
    )

    if receipt["decision"] == "ALLOW":
        return 0
    if receipt["decision"] == "ESCALATE":
        return 3
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
