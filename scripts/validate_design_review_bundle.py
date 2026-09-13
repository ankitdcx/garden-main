#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()

def validate(bundle, epoch, source_root):
    failures = []
    if bundle.get("schema") != "GardenDesignReviewBundle/v1": failures.append("BAD_SCHEMA")
    if bundle.get("bundle_sha256") != digest({k:v for k,v in bundle.items() if k != "bundle_sha256"}): failures.append("BAD_HASH")
    if bundle.get("design_epoch") != epoch: failures.append("STALE_EPOCH")
    if bundle.get("canonical_source_root_sha256") != source_root: failures.append("STALE_SOURCE_ROOT")
    if bundle.get("semantic_delta_admitted") is not False: failures.append("SELF_ADMISSION_REFUSED")
    target = bundle.get("target") or {}
    if target.get("public_only") is not True: failures.append("NON_PUBLIC_TARGET")
    minimum = int(bundle.get("minimum_independent_reviewer_families", 0))
    if minimum < 3: failures.append("MINIMUM_BELOW_THREE")
    independent = bundle.get("independent_findings") or []
    finals = bundle.get("final_dispositions") or []
    independent_families = {str(x.get("reviewer_family", "")) for x in independent if isinstance(x, dict)}
    final_families = {str(x.get("reviewer_family", "")) for x in finals if isinstance(x, dict)}
    if "" in independent_families or len(independent_families) < minimum: failures.append("INSUFFICIENT_INDEPENDENT_REVIEW")
    if "" in final_families or len(final_families) < minimum: failures.append("INSUFFICIENT_FINAL_REVIEW")
    if not final_families.issubset(independent_families): failures.append("FINAL_REVIEWER_SET_INVALID")
    for row in independent + finals:
        if not str(row.get("reviewer_model", "")).endswith(":free"): failures.append("NON_FREE_REVIEWER")
    called = [x for x in (bundle.get("provider_attempts") or []) if isinstance(x, dict) and x.get("status") == "CALLED"]
    if not called: failures.append("NO_SUCCESSFUL_CALLS")
    for row in called:
        if not str(row.get("model", "")).endswith(":free"): failures.append("NON_FREE_CALL")
        if (row.get("usage") or {}).get("cost") not in (0, 0.0): failures.append("ZERO_COST_NOT_EXPLICIT")
    if bundle.get("status") != "REVIEW_COMPLETE_NEEDS_GSL_INTEGRATOR": failures.append("REVIEW_NOT_COMPLETE")
    if bundle.get("zero_cost_verified") is not True: failures.append("ZERO_COST_FLAG_NOT_TRUE")
    receipt = {
        "schema":"GardenDesignReviewIntakeReceipt/v1",
        "design_epoch":epoch,
        "canonical_source_root_sha256":source_root,
        "source_obligation_refs":["work_packages/WP-005.md#Required process"],
        "target_id":target.get("target_id"),
        "candidate_evidence_eligible":not failures,
        "failures":failures,
        "next_required_stage":"WHOLE_FIVE_FILE_CROSS_REFERENCE_AND_GSL_ADMISSION" if not failures else "REJECT_OR_REVIEW_AGAIN",
        "automatic_semantic_admission":False,
        "authorization_result":"NOT_EVALUATED_HERE",
        "boundary":"Passing intake preserves candidate evidence only; it does not establish proof, authorization, canonical promotion, or certification."
    }
    receipt["receipt_sha256"] = digest(receipt)
    return receipt

def main():
    p=argparse.ArgumentParser(); p.add_argument("--input", required=True); p.add_argument("--output", required=True); p.add_argument("--manifest", default=str(ROOT/"canonical/current/SOURCE_MANIFEST.json")); a=p.parse_args()
    bundle=json.loads(Path(a.input).read_text()); manifest=json.loads(Path(a.manifest).read_text())
    epoch=str(manifest["release"]).removeprefix("Garden "); root=str(manifest["source_root_sha256"])
    receipt=validate(bundle, epoch, root); out=Path(a.output); out.parent.mkdir(parents=True, exist_ok=True); out.write_text(json.dumps(receipt, indent=2)+"\n")
    print(json.dumps({"target_id":receipt["target_id"],"candidate_evidence_eligible":receipt["candidate_evidence_eligible"],"failures":len(receipt["failures"])}))
    return 0 if receipt["candidate_evidence_eligible"] else 1
if __name__ == "__main__": raise SystemExit(main())
