#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "implementation"))

from garden_kernel.function_contracts import (  # noqa: E402
    audit_function_contract_coverage,
    load_function_contract_registry,
    validate_registry_against_manifest,
)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--registry",
        default=str(ROOT / "gsl" / "FUNCTION_CONTRACTS.json"),
    )
    parser.add_argument(
        "--manifest",
        default=str(ROOT / "canonical" / "current" / "SOURCE_MANIFEST.json"),
    )
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    registry = load_function_contract_registry(args.registry)
    manifest = json.loads(Path(args.manifest).read_text(encoding="utf-8"))
    validate_registry_against_manifest(registry, manifest)
    report = audit_function_contract_coverage(ROOT, registry)

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(report.as_dict(), indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(json.dumps({
        "registry_id": report.registry_id,
        "scoped_function_count": report.scoped_function_count,
        "declared_contract_count": report.declared_contract_count,
        "frontier_function_count": report.frontier_function_count,
        "declaration_coverage_ratio": report.declaration_coverage_ratio,
        "semantic_compliance_proved": report.semantic_compliance_proved,
    }))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
