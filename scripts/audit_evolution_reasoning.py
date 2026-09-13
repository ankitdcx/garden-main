#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import subprocess
import sys
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "implementation"))

from garden_kernel.evolution_reasoning import validate_reasoning_bundle  # noqa: E402
from garden_kernel.evolution_transport import load_source_identity  # noqa: E402


REPORT_SCHEMA = "GardenEvolutionReasoningConformanceReport/v1"
MATERIAL_PREFIXES = (
    "implementation/",
    "scripts/",
    "governance/",
    "gsl/",
    "work_packages/",
    ".github/workflows/",
    "reviews/evolution/production/",
)


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
            f"cannot derive changed paths from {base_ref}..{head_ref}: {proc.stderr.strip()}"
        )
    return tuple(sorted({line.strip() for line in proc.stdout.splitlines() if line.strip()}))


def _material(paths: tuple[str, ...]) -> tuple[str, ...]:
    return tuple(path for path in paths if path.startswith(MATERIAL_PREFIXES))


def _changed_actions(paths: tuple[str, ...]) -> tuple[str, ...]:
    prefix = "reviews/evolution/production/"
    return tuple(
        path
        for path in paths
        if path.startswith(prefix) and path.endswith(".json")
    )


def _reasoning_refs(request: dict[str, Any]) -> tuple[str, ...]:
    action = dict(request.get("action") or {})
    refs = [
        str(ref).strip()
        for ref in action.get("input_refs", ())
        if str(ref).strip().startswith("reviews/evolution/reasoning/")
        and str(ref).strip().endswith(".json")
    ]
    return tuple(refs)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    parser.add_argument(
        "--manifest",
        default=str(ROOT / "canonical" / "current" / "SOURCE_MANIFEST.json"),
    )
    parser.add_argument("--base-ref")
    parser.add_argument("--head-ref", default="HEAD")
    args = parser.parse_args()

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    identity = load_source_identity(args.manifest)
    base_ref = _resolve_base_ref(args.base_ref)
    failures: list[str] = []
    checked: list[dict[str, Any]] = []

    try:
        changed = _changed_paths(base_ref, args.head_ref)
        material = _material(changed)
        actions = _changed_actions(changed)
        if material and not actions:
            failures.append(
                "material change has no changed GardenEvolutionProductionAction/v1 transport"
            )

        for rel in actions:
            path = ROOT / rel
            request = json.loads(path.read_text(encoding="utf-8"))
            if request.get("schema") != "GardenEvolutionProductionAction/v1":
                failures.append(f"{rel}: production action schema is not recognized")
                continue
            action = dict(request.get("action") or {})
            action_id = str(action.get("action_id", "")).strip()
            refs = _reasoning_refs(request)
            if len(refs) != 1:
                failures.append(
                    f"{rel}: changed production action requires exactly one reasoning bundle input ref"
                )
                continue
            reasoning_rel = refs[0]
            reasoning_path = ROOT / reasoning_rel
            if not reasoning_path.is_file():
                failures.append(f"{rel}: reasoning bundle does not exist: {reasoning_rel}")
                continue
            try:
                receipt = validate_reasoning_bundle(
                    json.loads(reasoning_path.read_text(encoding="utf-8")),
                    expected_action_id=action_id,
                    expected_design_epoch=identity.design_epoch,
                    expected_source_root_sha256=identity.source_root_sha256,
                )
            except Exception as exc:  # report receipt must survive validation failure
                failures.append(f"{rel}: reasoning validation failed: {type(exc).__name__}:{exc}")
                continue
            checked.append(
                {
                    "production_action": rel,
                    "action_id": action_id,
                    "reasoning_bundle": reasoning_rel,
                    "validation": receipt,
                }
            )
    except Exception as exc:
        changed = ()
        material = ()
        actions = ()
        failures.append(f"audit execution failed: {type(exc).__name__}:{exc}")

    report = {
        "schema": REPORT_SCHEMA,
        "design_epoch": identity.design_epoch,
        "canonical_source_root_sha256": identity.source_root_sha256,
        "base_ref": base_ref,
        "head_ref": args.head_ref,
        "changed_paths": list(changed),
        "material_changed_paths": list(material),
        "changed_production_actions": list(actions),
        "checked_actions": checked,
        "failures": failures,
        "status": "FAIL" if failures else "PASS",
        "semantic_compliance_proved": False,
        "boundary": "Reasoning validation is conformance evidence only. It does not authorize actions; trusted authority and ActionGate remain the admission owners.",
    }
    output.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False))
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
