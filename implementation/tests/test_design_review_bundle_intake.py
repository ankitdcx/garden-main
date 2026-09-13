from __future__ import annotations
import unittest
from scripts.validate_design_review_bundle import digest, validate

EPOCH = "v15.5"
ROOT = "63561ce9fcd4a72f44af333662b342fd18c4e99930209c30c5f801bcc5c74598"


def valid_bundle():
    families = ("deepseek", "qwen", "mistral")
    independent = [
        {"reviewer_family": f, "reviewer_model": f"example/{f}:free"}
        for f in families
    ]
    finals = [dict(row) for row in independent]
    attempts = [
        {"status": "CALLED", "family": f, "model": f"example/{f}:free", "usage": {"cost": 0}, "phase": phase}
        for phase in ("INDEPENDENT", "PEER_CROSS_EXAMINATION")
        for f in families
    ]
    bundle = {
        "schema": "GardenDesignReviewBundle/v1",
        "design_epoch": EPOCH,
        "canonical_source_root_sha256": ROOT,
        "target": {"target_id": "DRM-TEST", "public_only": True},
        "minimum_independent_reviewer_families": 3,
        "independent_reviewer_family_count": 3,
        "final_disposition_family_count": 3,
        "zero_cost_verified": True,
        "provider_attempts": attempts,
        "independent_findings": independent,
        "final_dispositions": finals,
        "status": "REVIEW_COMPLETE_NEEDS_GSL_INTEGRATOR",
        "semantic_delta_admitted": False,
    }
    bundle["bundle_sha256"] = digest(bundle)
    return bundle


def rehash(bundle):
    bundle["bundle_sha256"] = digest({k:v for k,v in bundle.items() if k != "bundle_sha256"})
    return bundle


class DesignReviewBundleIntakeTests(unittest.TestCase):
    def test_valid_bundle_is_candidate_evidence_only(self):
        receipt = validate(valid_bundle(), EPOCH, ROOT)
        self.assertTrue(receipt["candidate_evidence_eligible"])
        self.assertFalse(receipt["automatic_semantic_admission"])
        self.assertEqual(receipt["authorization_result"], "NOT_EVALUATED_HERE")
        self.assertEqual(receipt["next_required_stage"], "WHOLE_FIVE_FILE_CROSS_REFERENCE_AND_GSL_ADMISSION")

    def test_insufficient_review_fails_closed(self):
        bundle = valid_bundle()
        bundle["independent_findings"] = bundle["independent_findings"][:2]
        bundle["final_dispositions"] = bundle["final_dispositions"][:2]
        receipt = validate(rehash(bundle), EPOCH, ROOT)
        self.assertFalse(receipt["candidate_evidence_eligible"])
        self.assertIn("INSUFFICIENT_INDEPENDENT_REVIEW", receipt["failures"])
        self.assertIn("INDEPENDENT_COUNT_MISMATCH", receipt["failures"])

    def test_public_bundle_cannot_self_admit(self):
        bundle = valid_bundle(); bundle["semantic_delta_admitted"] = True
        receipt = validate(rehash(bundle), EPOCH, ROOT)
        self.assertFalse(receipt["candidate_evidence_eligible"])
        self.assertIn("SELF_ADMISSION_REFUSED", receipt["failures"])

    def test_missing_or_nonzero_cost_fails_closed(self):
        for bad_cost in (None, 0.01):
            bundle = valid_bundle(); bundle["provider_attempts"][0]["usage"]["cost"] = bad_cost
            receipt = validate(rehash(bundle), EPOCH, ROOT)
            self.assertFalse(receipt["candidate_evidence_eligible"])
            self.assertIn("ZERO_COST_NOT_EXPLICIT", receipt["failures"])

    def test_finding_without_matching_provider_call_fails_closed(self):
        bundle = valid_bundle()
        bundle["provider_attempts"] = [row for row in bundle["provider_attempts"] if not (row["phase"] == "INDEPENDENT" and row["family"] == "qwen")]
        receipt = validate(rehash(bundle), EPOCH, ROOT)
        self.assertFalse(receipt["candidate_evidence_eligible"])
        self.assertIn("INDEPENDENT_FINDING_WITHOUT_MATCHING_CALL", receipt["failures"])

    def test_stale_epoch_or_source_root_fails_closed(self):
        bundle = valid_bundle()
        receipt = validate(bundle, "v15.6", ROOT)
        self.assertFalse(receipt["candidate_evidence_eligible"])
        self.assertIn("STALE_EPOCH", receipt["failures"])
        receipt = validate(bundle, EPOCH, "1" * 64)
        self.assertFalse(receipt["candidate_evidence_eligible"])
        self.assertIn("STALE_SOURCE_ROOT", receipt["failures"])


if __name__ == "__main__":
    unittest.main()
