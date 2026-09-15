#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import sys
import subprocess

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "implementation"))

from garden_kernel.process_engine import CycleBinding, ProcessFactory, ProcessRoute, ProcessState  # noqa: E402
from garden_kernel.section_units import build_inventory  # noqa: E402


def _write(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-dir", default=str(ROOT / "canonical" / "current"))
    parser.add_argument("--manifest", default=str(ROOT / "canonical" / "current" / "SOURCE_MANIFEST.json"))
    parser.add_argument("--algebra-profile", default=str(ROOT / "gsl" / "EVOLUTION_ALGEBRA_PROFILE.json"))
    parser.add_argument("--process-version", default="1.4")
    parser.add_argument("--repo-head", default=os.environ.get("GITHUB_SHA"))
    parser.add_argument("--inventory-output", required=True)
    parser.add_argument("--count-output", required=True)
    parser.add_argument("--process-output", required=True)
    args = parser.parse_args()

    manifest = json.loads(Path(args.manifest).read_text(encoding="utf-8"))
    profile = json.loads(Path(args.algebra_profile).read_text(encoding="utf-8"))
    inventory = build_inventory(source_dir=Path(args.source_dir), manifest=manifest, process_version=args.process_version)
    repo_head = args.repo_head
    if repo_head is None:
        try:
            repo_head = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()
        except (OSError, subprocess.CalledProcessError):
            parser.error("provide --repo-head with the full observed commit SHA")
    repo_head = str(repo_head).strip()
    if not repo_head:
        raise SystemExit("repo head is required")

    routed: list[dict[str, object]] = []
    for unit in inventory.units:
        cycle_digest = hashlib.sha256((inventory.source_root_sha256 + "\0" + args.process_version + "\0" + repo_head + "\0" + unit.unit_id).encode("utf-8")).hexdigest()[:24]
        binding = CycleBinding(
            cycle_id=f"GARDEN-SECTION-{cycle_digest.upper()}",
            process_version=args.process_version,
            design_epoch="v15.5",
            source_root_sha256=inventory.source_root_sha256,
            repo_heads={"garden-main": repo_head},
        )
        process = ProcessFactory.create(ProcessRoute.SECTION_UNIT_REVIEW, binding=binding, work_id=unit.unit_id)
        route_receipt = process.route_receipt()
        transition = process.advance(
            ProcessState.ROUTED,
            satisfied_gates=["ROUTE_CLASSIFIED"],
            algebra_profile=profile,
            source_obligation_refs=[
                "governance/PROCESS_CURRENT.json",
                "governance/GardenCanonicalUpdateProcess_v1.4.json",
                f"canonical/current/{unit.source_file}:{unit.start_line}-{unit.end_line}",
            ],
        )
        routed.append({
            "section_unit_id": unit.unit_id,
            "coverage_state": "UNREVIEWED",
            "cycle_binding": {
                "schema": "CycleBinding/v1",
                "CycleID": binding.cycle_id,
                "ProcessVersion": binding.process_version,
                "DesignEpoch": inventory.design_epoch,
                "source_root_sha256": binding.source_root_sha256,
                "repo_heads": dict(binding.repo_heads),
            },
            "route_receipt": route_receipt,
            "transition_receipt": transition,
        })

    count_receipt = inventory.count_receipt(qualified=0, stale=0, unreviewed=len(inventory.units))
    process_receipt = {
        "schema": "CanonicalSectionProcessRoutingReceipt/v1",
        "source_root_sha256": inventory.source_root_sha256,
        "DesignEpoch": inventory.design_epoch,
        "ProcessVersion": args.process_version,
        "repo_head": repo_head,
        "route": "SECTION_UNIT_REVIEW",
        "unit_count": len(routed),
        "all_instances_advanced_to": "ROUTED",
        "coverage_state": "UNREVIEWED",
        "instances": routed,
        "authorization_result": "NOT_MINTED_BY_SWEEP_ROUTING",
        "semantic_compliance_proved": False,
    }

    _write(Path(args.inventory_output), inventory.to_dict())
    _write(Path(args.count_output), count_receipt)
    _write(Path(args.process_output), process_receipt)
    print("CANONICAL_SECTION_COUNT_RECEIPT=" + json.dumps(count_receipt, sort_keys=True, separators=(",", ":")))
    unresolved_units = sum(1 for unit in inventory.units if unit.unresolved_references)
    print("CANONICAL_SECTION_REFERENCE_SUMMARY=" + json.dumps({"units_with_unresolved_references": unresolved_units, "total_units": len(inventory.units)}, sort_keys=True, separators=(",", ":")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
