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
from garden_kernel.base_admission import base_pinned_attestation  # noqa: E402
from garden_kernel.core import SemanticError  # noqa: E402


def _resolve_base_ref(explicit: str | None) -> str:
    if explicit:
        return explicit
    base_branch = os.environ.get("GITHUB_BASE_REF", "").strip()
    if base_branch:
        return f"origin/{base_branch}"
    return "HEAD^"


def _changed_paths(base_ref: str, head_ref: str) -> tuple[str, ...]:
    proc = subprocess.run(
        ["git", "diff", "--name-only", "--no-renames", base_ref, head_ref],
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

    admission_error = None
    try:
        attestations, attestors = base_pinned_attestation(
            root=ROOT, base_ref=base_ref, head_ref=args.head_ref,
            repository=os.environ.get("GITHUB_REPOSITORY", ""), request=request,
            design_epoch=identity.design_epoch,
            source_root_sha256=identity.source_root_sha256,
        )
    except SemanticError as exc:
        attestations, attestors = (), {}
        admission_error = str(exc)
    receipt = evaluate_production_request(
        request,
        identity,
        trusted_authorities,
        trusted_governance_receipt=governance_receipt,
        trusted_attestation_receipts=attestations,
        trusted_attestors=attestors,
    )

    if admission_error:
        receipt["base_admission_error"] = admission_error

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
