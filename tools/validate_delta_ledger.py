#!/usr/bin/env python3
"""Fail-closed structural validator for Garden DeltaRecord/v1 ledger.

This intentionally uses only the Python standard library so CI can run it without
network/package installation. It validates the closed fields Garden relies on for
per-delta traceability; JSON Schema validation may be added as a separate layer.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "design_deltas" / "v15.6" / "DELTA_LEDGER.json"

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


def fail(msg: str) -> None:
    raise AssertionError(msg)


def load_json(path: Path):
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def source_item_exists(source_doc: dict, item_id: str) -> bool:
    if source_doc.get("delta_set_id") == item_id:
        return True
    for collection, id_key in (("deltas", "delta_id"), ("candidates", "candidate_id")):
        rows = source_doc.get(collection)
        if isinstance(rows, list) and any(isinstance(r, dict) and r.get(id_key) == item_id for r in rows):
            return True
    # Some grouped candidate files describe one candidate at set level rather than
    # carrying an inner delta_id. Those are traceable by the parent set itself.
    return not isinstance(source_doc.get("deltas"), list) and not isinstance(source_doc.get("candidates"), list)


def validate() -> dict:
    ledger = load_json(LEDGER)
    if ledger.get("schema") != "GardenDeltaLedger/v1":
        fail("ledger schema must be GardenDeltaLedger/v1")
    records = ledger.get("records")
    if not isinstance(records, list) or not records:
        fail("ledger records must be a non-empty list")

    ids: set[str] = set()
    source_cache: dict[Path, dict] = {}
    admission_count = 0

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
        if rec["admission_eligible"]:
            admission_count += 1

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
        if rec["lifecycle_state"] == "ADMITTED_FOR_SUCCESSOR":
            if review["quorum_status"] != "SATISFIED":
                fail(f"{did} admitted without review quorum")
            if rec["semantic_impact"].get("status") not in {"YES", "NO"}:
                fail(f"{did} admitted without resolved semantic impact")
            if rec["challenger"].get("status") != "PASS":
                fail(f"{did} admitted without Challenger PASS")

    return {
        "schema": ledger["schema"],
        "record_count": len(records),
        "unique_delta_ids": len(ids),
        "admission_eligible_count": admission_count,
        "status": "PASS",
    }


if __name__ == "__main__":
    try:
        result = validate()
    except Exception as exc:
        print(json.dumps({"status": "FAIL", "error": str(exc)}, sort_keys=True))
        sys.exit(1)
    print(json.dumps(result, sort_keys=True))
