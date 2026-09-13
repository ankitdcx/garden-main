#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "implementation"))

from garden_kernel.evolution_audit import build_audit_chain, record_descriptor, validate_audit_chain  # noqa: E402
from garden_kernel.evolution_transport import load_source_identity  # noqa: E402


def _record_paths(values: list[str]) -> list[Path]:
    paths: set[Path] = set()
    for value in values:
        path = Path(value)
        if path.is_dir():
            paths.update(p for p in path.rglob("*.json") if p.is_file())
        elif path.is_file():
            paths.add(path)
        else:
            paths.update(p for p in ROOT.glob(value) if p.is_file())
    return sorted(paths, key=lambda p: p.as_posix())


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    parser.add_argument("--manifest", default=str(ROOT / "canonical/current/SOURCE_MANIFEST.json"))
    parser.add_argument("--chain-id", required=True)
    parser.add_argument("--record", action="append", default=[], help="File, directory, or repository-root glob. Repeatable.")
    args = parser.parse_args()

    identity = load_source_identity(args.manifest)
    paths = _record_paths(args.record)
    if not paths:
        raise SystemExit("durable audit chain requires at least one receipt record")

    descriptors = [record_descriptor(path, root=ROOT) for path in paths]
    chain = build_audit_chain(
        descriptors,
        chain_id=args.chain_id,
        design_epoch=identity.design_epoch,
        canonical_source_root_sha256=identity.source_root_sha256,
    )
    validation = validate_audit_chain(
        chain,
        expected_design_epoch=identity.design_epoch,
        expected_source_root_sha256=identity.source_root_sha256,
    )
    chain["validation"] = validation
    chain["record_refs"] = [item["record_ref"] for item in descriptors]
    chain["persistence_boundary"] = "GitHub Actions immutable artifact for configured retention; protected permanent archival remains FRONTIER."

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(chain, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({"schema": chain["schema"], "chain_id": chain["chain_id"], "entry_count": chain["entry_count"], "head_hash": chain["head_hash"]}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
