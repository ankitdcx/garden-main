#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "implementation"))

from garden_kernel.repo_conformance import (  # noqa: E402
    audit_repo,
    load_repo_profile,
    validate_profile_against_manifest,
)


def main() -> int:
    p = argparse.ArgumentParser(
        description=(
            "Load every repository file into the bounded GardenRepoConformanceProfile. "
            "This proves classification coverage only, not full semantic GSL compliance."
        )
    )
    p.add_argument("--repo-root", default=str(ROOT))
    p.add_argument("--profile", default=str(ROOT / "gsl" / "GSL_REPO_PROFILE.json"))
    p.add_argument(
        "--canonical-manifest",
        default=str(ROOT / "canonical" / "current" / "SOURCE_MANIFEST.json"),
    )
    p.add_argument("--output", default="gsl-repo-audit.json")
    p.add_argument(
        "--strict-frontier",
        action="store_true",
        help="fail if any artifact remains in the explicit FRONTIER class",
    )
    args = p.parse_args()

    profile = load_repo_profile(args.profile)
    manifest = json.loads(Path(args.canonical_manifest).read_text(encoding="utf-8"))
    validate_profile_against_manifest(profile, manifest)
    report = audit_repo(args.repo_root, profile)
    payload = report.as_dict()
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    summary = {
        "schema": payload["schema"],
        "profile_id": payload["profile_id"],
        "design_epoch": payload["design_epoch"],
        "artifact_count": payload["artifact_count"],
        "explicit_artifact_count": payload["explicit_artifact_count"],
        "frontier_artifact_count": payload["frontier_artifact_count"],
        "semantic_compliance_proved": payload["semantic_compliance_proved"],
        "output": str(output),
    }
    print(json.dumps(summary, sort_keys=True))
    if args.strict_frontier and report.frontier_artifact_count:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
