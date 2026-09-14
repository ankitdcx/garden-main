#!/usr/bin/env python3
"""Fail-closed validator and typed readiness receipt for Garden DeltaRecord/v1.

The legacy ``admission_eligible`` field is retained only as a process-candidacy
marker for migration compatibility. It is never sufficient evidence of current
successor-admission readiness. Readiness is derived from the governed review,
semantic-impact, Challenger, conflict, and lifecycle state below.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "design_deltas" / "v15.6" / "DELTA_LEDGER.json"

RULE_ID = "RULE-DELTA-ADMISSION-FAIL-CLOSED"
CHECK_ID = "CHECK-DELTA-ADMISSION-READINESS"
RECEIPT_SCHEMA = "DeltaAdmissionReadinessReceipt/v1"

REQUIRED_RECORD_KEYS = {
    "schema", "delta_id", "record_kind", "title", "predecessor_release",
    "candidate_release", "design_epoch_ref", "source", "source_status",
    "lifecycle_state", "semantic_impact", "review", "challenger",
    "provenance", "admission_eligible", "canonical_effect",
}
LIFECYCLE = {
    "PROPOSED", "REVIEWED", "DISPUTED", "ACCEPTED", "ADMITTED_FOR_SUCCESSOR",
    "REJECTED", "DEFERRED", "UNRESOLVED", "IMPLEMENTED", "VERIFIED",
    "AUDITED", "CLOSED", "REOPENED", "REVERTED",
}
SEMANTIC = {"NOT_ASSESSED", "YES", "NO", "UNCLEAR"}
QUORUM = {"NOT_ASSESSED", "INSUFFICIENT", "SATISFIED"}
CHALLENGER = {"NOT_ASSESSED", "NOT_REQUIRED", "PENDING", "PASS", "CHALLENGE", "ESCALATE", "AUDIT_PENDING"}
READY_LIFECYCLE = {"ACCEPTED", "ADMITTED_FOR_SUCCESSOR"}
COMMIT_RE = re.compile(r"^[0-9a-f]{40}$")


def fail(msg: str) -> None:
    raise AssertionError(msg)


def load_json(path: Path):
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_item_exists(source_doc: dict, item_id: str) -> bool:
    if source_doc.get("delta_set_id") == item_id:
        return True
    for collection, id_key in (("deltas", "delta_id"), ("candidates", "candidate_id")):
        rows = source_doc.get(collection)
        if isinstance(rows, list) and any(isinstance(r, dict) and r.get(id_key) == item_id for r in rows):
            return True
    return not isinstance(source_doc.get("deltas"), list) and not isinstance(source_doc.get("candidates"), list)


def admission_readiness(rec: dict) -> tuple[bool, list[str]]:
    """Return current successor-admission readiness and fail-closed reasons.

    This is deliberately stricter than process candidacy. Unknown or unresolved
    state is never treated as ready.
    """
    reasons: list[str] = []
    review = rec.get("review", {})
    semantic = rec.get("semantic_impact", {})
    challenger = rec.get("challenger", {})

    if rec.get("lifecycle_state") not in READY_LIFECYCLE:
        reasons.append("LIFECYCLE_NOT_ACCEPTED")
    if semantic.get("status") not in {"YES", "NO"}:
        reasons.append("SEMANTIC_IMPACT_UNRESOLVED")
    if not semantic.get("assessment_ref"):
        reasons.append("SEMANTIC_IMPACT_RECEIPT_MISSING")
    if review.get("quorum_status") != "SATISFIED":
        reasons.append("INDEPENDENT_REVIEW_QUORUM_NOT_SATISFIED")
    if len(set(review.get("reviewer_families", []))) < 3:
        reasons.append("FEWER_THAN_THREE_REVIEWER_FAMILIES")
    if len(set(review.get("blind_review_refs", []))) < 3:
        reasons.append("BLIND_REVIEW_RECEIPTS_INSUFFICIENT")
    if len(set(review.get("cross_exam_refs", []))) < 3:
        reasons.append("CROSS_EXAM_RECEIPTS_INSUFFICIENT")
    if review.get("evidence_conflict_status") == "UNRESOLVED":
        reasons.append("EVIDENCE_CONFLICT_UNRESOLVED")
    if challenger.get("status") != "PASS":
        reasons.append("CHALLENGER_NOT_PASS")
    if not challenger.get("decision_ref"):
        reasons.append("CHALLENGER_RECEIPT_MISSING")
    if rec.get("canonical_effect") is not False:
        reasons.append("CANONICAL_EFFECT_NOT_FALSE")

    return (not reasons, reasons)


def validate(repository_commit: str) -> dict:
    if not COMMIT_RE.fullmatch(repository_commit):
        fail("exact 40-hex repository commit binding is required")

    ledger = load_json(LEDGER)
    if ledger.get("schema") != "GardenDeltaLedger/v1":
        fail("ledger schema must be GardenDeltaLedger/v1")
    records = ledger.get("records")
    if not isinstance(records, list) or not records:
        fail("ledger records must be a non-empty list")

    ids: set[str] = set()
    source_cache: dict[Path, dict] = {}
    legacy_candidate_count = 0
    readiness: list[dict] = []

    for i, rec in enumerate(records):
        if not isinstance(rec, dict):
            fail(f"record[{i}] must be an object")
        missing = REQUIRED_RECORD_KEYS - rec.keys()
        if missing:
            fail(f"{rec.get('delta_id', i)} missing keys: {sorted(missing)}")
        if rec["schema"] != "DeltaRecord/v1":
            fail(f"{rec['delta_id']} has wrong schema")
        did = rec["delta_id"]
        if did in ids:
            fail(f"duplicate delta_id: {did}")
        ids.add(did)
        if rec["lifecycle_state"] not in LIFECYCLE:
            fail(f"{did} invalid lifecycle_state")
        if rec["semantic_impact"].get("status") not in SEMANTIC:
            fail(f"{did} invalid semantic impact")
        if rec["review"].get("quorum_status") not in QUORUM:
            fail(f"{did} invalid quorum status")
        if rec["challenger"].get("status") not in CHALLENGER:
            fail(f"{did} invalid challenger status")
        if rec["canonical_effect"] is not False:
            fail(f"{did} ledger tracking cannot itself have canonical effect")
        if not isinstance(rec["admission_eligible"], bool):
            fail(f"{did} legacy admission_eligible marker must be boolean")
        if rec["admission_eligible"]:
            legacy_candidate_count += 1

        src = rec["source"]
        for key in ("path", "parent_set_id", "source_item_id"):
            if not src.get(key):
                fail(f"{did} source missing {key}")
        src_path = ROOT / src["path"]
        if not src_path.is_file():
            fail(f"{did} source file missing: {src['path']}")
        if src_path not in source_cache:
            source_cache[src_path] = load_json(src_path)
        source_doc = source_cache[src_path]
        if source_doc.get("delta_set_id") != src["parent_set_id"]:
            fail(f"{did} parent_set_id does not match source file")
        if not source_item_exists(source_doc, src["source_item_id"]):
            fail(f"{did} source_item_id not found in source set")

        review = rec["review"]
        if review["quorum_status"] == "SATISFIED" and len(set(review.get("reviewer_families", []))) < 3:
            fail(f"{did} cannot claim SATISFIED quorum with fewer than 3 families")

        ready, reasons = admission_readiness(rec)
        readiness.append({"delta_id": did, "ready": ready, "blocking_reasons": reasons})
        if rec["lifecycle_state"] == "ADMITTED_FOR_SUCCESSOR" and not ready:
            fail(f"{did} admitted while fail-closed readiness check is false: {reasons}")

    ready_ids = [row["delta_id"] for row in readiness if row["ready"]]
    return {
        "schema": RECEIPT_SCHEMA,
        "status": "PASS",
        "rule_trace": {
            "rule_id": RULE_ID,
            "check_id": CHECK_ID,
            "result": "PASS"
        },
        "repository_commit": repository_commit,
        "canonical_version": ledger.get("predecessor_release", "Garden v15.5"),
        "design_epoch_ref": ledger.get("design_epoch_ref"),
        "evidence": {
            "ledger_path": str(LEDGER.relative_to(ROOT)),
            "ledger_sha256": sha256_file(LEDGER)
        },
        "record_count": len(records),
        "unique_delta_ids": len(ids),
        "legacy_process_candidate_marker_count": legacy_candidate_count,
        "admission_ready_count": len(ready_ids),
        "admission_ready_delta_ids": ready_ids,
        "readiness_by_delta": readiness
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repository-commit", required=True)
    args = parser.parse_args()
    try:
        result = validate(args.repository_commit)
    except Exception as exc:
        print(json.dumps({
            "schema": RECEIPT_SCHEMA,
            "status": "FAIL",
            "rule_trace": {"rule_id": RULE_ID, "check_id": CHECK_ID, "result": "FAIL"},
            "repository_commit": args.repository_commit,
            "error": str(exc)
        }, sort_keys=True))
        return 1
    print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
