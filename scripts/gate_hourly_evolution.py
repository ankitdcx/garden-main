#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "implementation"))

from garden_kernel.evolution_transport import (  # noqa: E402
    evaluate_production_request,
    load_authority_registry,
    load_source_identity,
)
from garden_kernel.evolution_trust import governance_receipt_from_changed_paths  # noqa: E402


def _resolve_base_ref(explicit: str | None) -> str:
    if explicit:
        return explicit
    base_branch = os.environ.get("GITHUB_BASE_REF", "").strip()
    if base_branch:
        return f"origin/{base_branch}"
    return "HEAD^"


def _changed_paths(base_ref: str, head_ref: str) -> tuple[str, ...]:
    proc = subprocess.run(
        ["git", "diff", "--name-only", "--diff-filter=ACMRTUXB", base_ref, head_ref],
        cwd=ROOT,
        text=True,
        capture_output=True,
    )
    if proc.returncode != 0:
        raise RuntimeError(
            f"cannot derive trusted governance change set from {base_ref}..{head_ref}: "
            f"{proc.stderr.strip()}"
        )
    return tuple(sorted({line.strip() for line in proc.stdout.splitlines() if line.strip()}))


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
    parser.add_argument("--base-ref")
    parser.add_argument("--head-ref", default="HEAD")
    args = parser.parse_args()

    request = json.loads(Path(args.input).read_text(encoding="utf-8"))
    identity = load_source_identity(args.manifest)
    trusted_authorities = load_authority_registry(args.authority_registry, identity)

    action_id = str(dict(request.get("action") or {}).get("action_id", "UNKNOWN"))
    base_ref = _resolve_base_ref(args.base_ref)
    changed_paths = _changed_paths(base_ref, args.head_ref)
    governance_receipt = governance_receipt_from_changed_paths(
        action_id=action_id,
        design_epoch=identity.design_epoch,
        source_root_sha256=identity.source_root_sha256,
        changed_paths=changed_paths,
        base_ref=base_ref,
        head_ref=args.head_ref,
    )

    # No boolean approval/review switches exist. Until a protected attestor
    # registry is explicitly human-approved, trusted attestation state is empty.
    # Constitutional changes and MATERIALIZE therefore fail closed rather than
    # letting an action self-assert approval or independent review.
    receipt = evaluate_production_request(
        request,
        identity,
        trusted_authorities,
        trusted_governance_receipt=governance_receipt,
        trusted_attestation_receipts=(),
        trusted_attestors={},
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
                "governance": receipt["governance"],
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
