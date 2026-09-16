#!/usr/bin/env python3
"""Recheck explicitly reported candidate anchors without claiming semantic closure."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path


ANCHOR_RE = re.compile(r"\[[A-Z][A-Z0-9*_-]*\]")
SEMANTIC_DEFINITION_RE = re.compile(r"^\s*(?:@N\|)?SemanticAnchor:\s*(\[[A-Z][A-Z0-9_-]*\])\s*$")
HUMAN_HEADING_RE = re.compile(r"^\s*(?:\d+[A-Z0-9-]*\..*\s{2,})?(\[H-[A-Z0-9_-]+\])(?:\s+.*)?$")
NEGATED_NONDEFINITION_RE = re.compile(r"\bno\s+(\[T-[A-Z0-9_-]+\])\s+anchor\s+is\s+created\b", re.IGNORECASE)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def scan_definitions(paths: list[Path], reference_root: Path | None = None) -> tuple[dict[str, list[str]], dict[str, list[str]]]:
    definitions: dict[str, list[str]] = {}
    intentional_nondefinitions: dict[str, list[str]] = {}
    for path in paths:
        display_path = path.relative_to(reference_root) if reference_root is not None else path
        for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            semantic = SEMANTIC_DEFINITION_RE.match(line)
            human = HUMAN_HEADING_RE.match(line)
            if semantic or human:
                anchor = (semantic or human).group(1)
                definitions.setdefault(anchor, []).append(f"{display_path.as_posix()}:{line_number}")
            for match in NEGATED_NONDEFINITION_RE.finditer(line):
                intentional_nondefinitions.setdefault(match.group(1), []).append(f"{display_path.as_posix()}:{line_number}")
    return definitions, intentional_nondefinitions


def check_reported_references(paths: list[Path], reported: list[str], reference_root: Path | None = None) -> dict[str, object]:
    definitions, intentional_nondefinitions = scan_definitions(paths, reference_root=reference_root)
    resolved: list[dict[str, object]] = []
    intentionally_not_defined: list[dict[str, object]] = []
    unresolved: list[str] = []
    for anchor in sorted(set(reported)):
        if not ANCHOR_RE.fullmatch(anchor):
            unresolved.append(anchor)
        elif anchor in definitions:
            resolved.append({"anchor": anchor, "definition_refs": definitions[anchor]})
        elif anchor in intentional_nondefinitions:
            intentionally_not_defined.append({"anchor": anchor, "evidence_refs": intentional_nondefinitions[anchor]})
        else:
            unresolved.append(anchor)
    return {
        "resolved_explicit_definitions": resolved,
        "intentionally_not_defined": intentionally_not_defined,
        "still_unresolved": unresolved,
    }


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-dir", type=Path, default=root / "canonical/candidates/v15.7")
    parser.add_argument("--input-receipt", type=Path, default=root / "reviews/v15.7/REFERENCE-CLOSURE-RECEIPT.json")
    parser.add_argument("--manifest", type=Path, default=root / "canonical/candidates/v15.7/SOURCE_MANIFEST.json")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    source_paths = sorted(args.source_dir.glob("Garden_*_FULL_CANDIDATE_*.txt"))
    if len(source_paths) != 5:
        raise SystemExit(f"expected exactly five candidate source texts, found {len(source_paths)}")
    input_receipt = json.loads(args.input_receipt.read_text(encoding="utf-8"))
    manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
    result = check_reported_references(source_paths, input_receipt["unresolved"], reference_root=root)
    payload = {
        "schema": "GardenCandidateExplicitReferenceAudit/v1",
        "status": "INCONCLUSIVE",
        "candidate_source_root_sha256": manifest["source_root_sha256"],
        "scope": "Exact syntactic recheck of references previously reported unresolved; not a full type, owner, GSL, or semantic closure validator.",
        "input_receipt": args.input_receipt.relative_to(root).as_posix(),
        "input_receipt_sha256": sha256(args.input_receipt),
        "manifest": args.manifest.relative_to(root).as_posix(),
        "manifest_sha256": sha256(args.manifest),
        "checked_source_sha256": {path.relative_to(root).as_posix(): sha256(path) for path in source_paths},
        **result,
        "counts": {
            "reported": len(set(input_receipt["unresolved"])),
            "resolved_explicit_definitions": len(result["resolved_explicit_definitions"]),
            "intentionally_not_defined": len(result["intentionally_not_defined"]),
            "still_unresolved": len(result["still_unresolved"]),
        },
        "semantic_closure_complete": False,
        "full_type_owner_gsl_validation_complete": False,
        "qualification_effect": "NONE",
        "authorization_effect": "NONE",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(payload["counts"], sort_keys=True))
    return 0 if not result["still_unresolved"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
