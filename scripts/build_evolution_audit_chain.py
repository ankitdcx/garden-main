#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "implementation"))

from garden_kernel.evolution_audit import build_audit_chain, validate_audit_chain  # noqa: E402
from garden_kernel.evolution_transport import load_source_identity  # noqa: E402


def _record_paths(values: list[str]) -> list[Path]:
    paths: set[Path] = set()
    for value in values:
        path = Path(value)
        if path.is_dir():
            paths.update(p for p in path.rglob("*.json") if p.is_file())
        elif path.is_file():
            paths.add(path)
        elif path.is_absolute():
            # Optional CI receipt directories may legitimately be absent when an
            # earlier gated stage was skipped. An absent absolute path contributes
            # no records; it must never be reinterpreted as a repository glob.
            continue
        else:
            paths.update(p for p in ROOT.glob(value) if p.is_file())
    return sorted(paths, key=lambda p: p.as_posix())


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(65536), b""):
            digest.update(block)
    return digest.hexdigest()


def _descriptor(path: Path) -> dict[str, str]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    try:
        record_ref = path.resolve().relative_to(ROOT.resolve()).as_posix()
    except ValueError:
        record_ref = path.resolve().as_posix()
    action_id = str(payload.get("action_id") or (payload.get("action") or {}).get("action_id") or "CI-CONFORMANCE")
    disposition = str(payload.get("decision") or payload.get("status") or payload.get("admission_status") or "RECORDED")
    return {
        "record_ref": record_ref,
        "record_sha256": _sha256(path),
        "record_schema": str(payload.get("schema", "UNKNOWN")),
        "action_id": action_id,
        "disposition": disposition,
    }


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

    descriptors = [_descriptor(path) for path in paths]
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
