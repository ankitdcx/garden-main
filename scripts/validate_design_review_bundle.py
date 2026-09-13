#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def validate(bundle, epoch, source_root):
    failures = []
    if not isinstance(bundle, dict):
        bundle = {}
        failures.append("BUNDLE_NOT_OBJECT")
    if bundle.get("schema") != "GardenDesignReviewBundle/v1": failures.append("BAD_SCHEMA")
    if bundle.get("bundle_sha256") != digest({k:v for k,v in bundle.items() if k != "bundle_sha256"}): failures.append("BAD_HASH")
    if bundle.get("design_epoch") != epoch: failures.append("STALE_EPOCH")
    if bundle.get("canonical_source_root_sha256") != source_root: failures.append("STALE_SOURCE_ROOT")
    if bundle.get("semantic_delta_admitted") is not False: failures.append("SELF_ADMISSION_REFUSED")

    target = bundle.get("target") if isinstance(bundle.get("target"), dict) else {}
    if target.get("public_only") is not True: failures.append("NON_PUBLIC_TARGET")
    if not str(target.get("target_id", "")).strip(): failures.append("TARGET_ID_MISSING")

    try:
        minimum = int(bundle.get("minimum_independent_reviewer_families", 0))
    except (TypeError, ValueError):
        minimum = 0
    if minimum < 3: failures.append("MINIMUM_BELOW_THREE")

    independent = bundle.get("independent_findings") if isinstance(bundle.get("independent_findings"), list) else []
    finals = bundle.get("final_dispositions") if isinstance(bundle.get("final_dispositions"), list) else []
    if not isinstance(bundle.get("independent_findings"), list): failures.append("INDEPENDENT_FINDINGS_MALFORMED")
    if not isinstance(bundle.get("final_dispositions"), list): failures.append("FINAL_DISPOSITIONS_MALFORMED")

    def identity_rows(rows, label):
        identities = []
        for row in rows:
            if not isinstance(row, dict):
                failures.append(f"{label}_ENTRY_MALFORMED")
                continue
            family = str(row.get("reviewer_family", "")).strip()
            model = str(row.get("reviewer_model", "")).strip()
            if not family or not model:
                failures.append(f"{label}_IDENTITY_MISSING")
                continue
            if not model.endswith(":free"):
                failures.append(f"{label}_NON_FREE_REVIEWER")
            identities.append((family, model))
        if len({family for family, _ in identities}) != len(identities):
            failures.append(f"{label}_DUPLICATE_FAMILY")
        return identities

    independent_ids = identity_rows(independent, "INDEPENDENT")
    final_ids = identity_rows(finals, "FINAL")
    independent_families = {family for family, _ in independent_ids}
    final_families = {family for family, _ in final_ids}

    if len(independent_families) < minimum: failures.append("INSUFFICIENT_INDEPENDENT_REVIEW")
    if len(final_families) < minimum: failures.append("INSUFFICIENT_FINAL_REVIEW")
    if not final_families.issubset(independent_families): failures.append("FINAL_REVIEWER_SET_INVALID")
    try:
        if int(bundle.get("independent_reviewer_family_count", -1)) != len(independent_families): failures.append("INDEPENDENT_COUNT_MISMATCH")
        if int(bundle.get("final_disposition_family_count", -1)) != len(final_families): failures.append("FINAL_COUNT_MISMATCH")
    except (TypeError, ValueError):
        failures.append("DECLARED_COUNT_MALFORMED")

    attempts = bundle.get("provider_attempts") if isinstance(bundle.get("provider_attempts"), list) else []
    if not isinstance(bundle.get("provider_attempts"), list): failures.append("PROVIDER_ATTEMPTS_MALFORMED")
    called = [x for x in attempts if isinstance(x, dict) and x.get("status") == "CALLED"]
    if not called: failures.append("NO_SUCCESSFUL_CALLS")
    for row in called:
        if not str(row.get("model", "")).endswith(":free"): failures.append("NON_FREE_CALL")
        if (row.get("usage") or {}).get("cost") not in (0, 0.0): failures.append("ZERO_COST_NOT_EXPLICIT")

    independent_calls = {(str(row.get("family", "")), str(row.get("model", ""))) for row in called if row.get("phase") == "INDEPENDENT"}
    peer_calls = {(str(row.get("family", "")), str(row.get("model", ""))) for row in called if row.get("phase") == "PEER_CROSS_EXAMINATION"}
    for identity in independent_ids:
        if identity not in independent_calls: failures.append("INDEPENDENT_FINDING_WITHOUT_MATCHING_CALL")
    for identity in final_ids:
        if identity not in peer_calls: failures.append("FINAL_DISPOSITION_WITHOUT_MATCHING_PEER_CALL")

    if bundle.get("status") != "REVIEW_COMPLETE_NEEDS_GSL_INTEGRATOR": failures.append("REVIEW_NOT_COMPLETE")
    if bundle.get("zero_cost_verified") is not True: failures.append("ZERO_COST_FLAG_NOT_TRUE")

    failures = sorted(set(failures))
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
        "canonical_promotion_result":"NOT_EVALUATED_HERE",
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
