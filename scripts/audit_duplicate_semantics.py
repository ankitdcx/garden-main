#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "implementation"))

from garden_kernel.evolution_epoch import (  # noqa: E402
    EvolutionArtifactBinding,
    EvolutionArtifactKind,
    validate_evolution_binding,
)
from garden_kernel.evolution_transport import load_source_identity  # noqa: E402


def _canonical_hash(value: Any) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    ).hexdigest()


def _load_public(public_root: Path):
    path = public_root / "prototype" / "design_epoch.py"
    if not path.is_file():
        raise SystemExit(f"public DesignEpoch reference missing: {path}")
    spec = importlib.util.spec_from_file_location("garden_public_design_epoch", path)
    if spec is None or spec.loader is None:
        raise SystemExit("could not load public DesignEpoch reference")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def _git_head(path: Path) -> str:
    return subprocess.check_output(
        ["git", "-C", str(path), "rev-parse", "HEAD"], text=True
    ).strip()


def _prefixes_ok(reasons: list[str], prefixes: list[str]) -> bool:
    return all(any(reason.startswith(prefix) for reason in reasons) for prefix in prefixes)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--public-root", required=True)
    parser.add_argument("--vectors", default=str(ROOT / "gsl/SHARED_CONFORMANCE_VECTORS.json"))
    parser.add_argument("--manifest", default=str(ROOT / "canonical/current/SOURCE_MANIFEST.json"))
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    payload = json.loads(Path(args.vectors).read_text(encoding="utf-8"))
    if payload.get("schema") != "GardenSharedConformanceVectors/v1":
        raise SystemExit("shared conformance vector schema is not recognized")
    if payload.get("semantic_compliance_proved") is not False:
        raise SystemExit("shared vector profile may not claim semantic compliance")
    vectors = payload.get("vectors")
    if not isinstance(vectors, list) or not vectors:
        raise SystemExit("shared conformance vectors must be non-empty")
    observed_hash = _canonical_hash(vectors)
    if observed_hash != payload.get("vector_set_sha256"):
        raise SystemExit("shared conformance vector_set_sha256 mismatch")

    identity = load_source_identity(args.manifest)
    expected_ref = f"Garden-{identity.design_epoch}@{identity.source_root_sha256}"
    if payload.get("design_epoch_ref") != expected_ref:
        raise SystemExit("shared vectors are stale for current DesignEpoch/source root")

    public_root = Path(args.public_root).resolve()
    public = _load_public(public_root)
    results: list[dict[str, Any]] = []
    failed = False

    for row in vectors:
        vector_id = str(row["vector_id"])
        i = row["input"]
        expected = row["expected"]
        required = i.get("required_dependencies")
        required_set = None if required is None else frozenset(required)

        public_result = public.validate_binding(
            public.ArtifactBinding(
                artifact_id=f"public:{vector_id}",
                design_epoch=i["binding_epoch"],
                dependencies=i["bound_dependencies"],
                required_dependencies=required_set,
            ),
            current_design_epoch=i["current_epoch"],
            current_dependencies=i["current_dependencies"],
        )
        private_result = validate_evolution_binding(
            EvolutionArtifactBinding(
                artifact_id=f"private:{vector_id}",
                kind=EvolutionArtifactKind.FINDING,
                design_epoch=i["binding_epoch"],
                dependencies=i["bound_dependencies"],
                required_dependencies=required_set,
            ),
            current_design_epoch=i["current_epoch"],
            current_dependencies=i["current_dependencies"],
        )

        public_reasons = list(public_result.reasons)
        private_reasons = list(private_result.reasons)
        expected_prefixes = list(expected["reason_prefixes"])
        vector_pass = (
            public_result.status.value == expected["status"]
            and private_result.status.value == expected["status"]
            and public_result.status.value == private_result.status.value
            and _prefixes_ok(public_reasons, expected_prefixes)
            and _prefixes_ok(private_reasons, expected_prefixes)
        )
        failed = failed or not vector_pass
        results.append(
            {
                "vector_id": vector_id,
                "expected_status": expected["status"],
                "public": {"status": public_result.status.value, "reasons": public_reasons},
                "private": {"status": private_result.status.value, "reasons": private_reasons},
                "compatible": vector_pass,
            }
        )

    receipt = {
        "schema": "GardenDuplicateSemanticsConformanceReport/v1",
        "design_epoch": identity.design_epoch,
        "canonical_source_root_sha256": identity.source_root_sha256,
        "source_obligation_refs": ["work_packages/WP-009.md#WP-009H"],
        "scope": "DESIGN_EPOCH_FRESHNESS",
        "vector_set_id": payload["vector_set_id"],
        "vector_set_sha256": observed_hash,
        "public_repository_ref": f"git:ankitdcx/garden-swarm@{_git_head(public_root)}",
        "private_repository_ref": f"git:ankitdcx/garden-main@{_git_head(ROOT)}",
        "implementations": {
            "public_prototype": "CHECKED",
            "private_kernel": "CHECKED",
            "scep_seed": "FRONTIER"
        },
        "vectors": results,
        "checked_count": len(results),
        "compatible_count": sum(1 for row in results if row["compatible"]),
        "frontier": [
            "SCEP/bootstrap does not yet consume these shared DesignEpoch vectors.",
            "Other duplicate semantics outside DesignEpoch freshness remain FRONTIER."
        ],
        "status": "FAIL" if failed else "PASS_SCOPED",
        "authorization_result": "NOT_EVALUATED_HERE",
        "semantic_compliance_proved": False,
        "boundary": "Scoped compatibility evidence cannot authorize actions, promote canon, or establish repo-wide Garden/GSL certification."
    }
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(receipt, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({"schema": receipt["schema"], "status": receipt["status"], "checked_count": len(results), "scep": "FRONTIER"}))
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
