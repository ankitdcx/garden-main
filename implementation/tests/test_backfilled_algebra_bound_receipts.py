from __future__ import annotations

import json
from pathlib import Path
import unittest

from garden_kernel.algebra_bound_update import validate_algebra_bound_update


ROOT = Path(__file__).resolve().parents[2]
PROFILE_REF = "gsl/EVOLUTION_ALGEBRA_PROFILE.json"
PROFILE_BLOB_SHA = "ef1775f9890a4066969ca576cb25e40a9b217102"
PROFILE = json.loads((ROOT / PROFILE_REF).read_text(encoding="utf-8"))
EPOCH = "v15.5"
SOURCE_ROOT = "63561ce9fcd4a72f44af333662b342fd18c4e99930209c30c5f801bcc5c74598"
PROCESS_VERSION = "GardenCanonicalUpdateProcess@1.3-candidate"


CASES = [
    {
        "name": "garden_main_v1_3_merge",
        "repo": "ankitdcx/garden-main",
        "sha": "aab395031871c35611188d0b95d6aab61555d618",
        "target_kind": "CANONICAL_DESIGN",
        "bound": "reviews/evolution/algebra_bound/2026-09-15-garden-main-aab3950-bound-update.json",
        "usage": "reviews/evolution/algebra/2026-09-15-backfill-garden-main-aab3950-usage.json",
        "validation": "reviews/evolution/algebra/2026-09-15-backfill-garden-main-aab3950-validation.json",
    },
    {
        "name": "garden_swarm_ip_review_merge",
        "repo": "ankitdcx/garden-swarm",
        "sha": "05948d6ae45e75429f95286c1d4e60d73ea7652b",
        "target_kind": "PUBLIC_REPO",
        "bound": "reviews/evolution/algebra_bound/2026-09-15-garden-swarm-05948d6-bound-update.json",
        "usage": "reviews/evolution/algebra/2026-09-15-backfill-garden-swarm-05948d6-usage.json",
        "validation": "reviews/evolution/algebra/2026-09-15-backfill-garden-swarm-05948d6-validation.json",
    },
]


def load(path: str) -> dict:
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


class BackfilledAlgebraBoundReceiptTests(unittest.TestCase):
    def test_backfilled_receipts_validate_at_exact_bound_shas(self):
        for case in CASES:
            with self.subTest(case=case["name"]):
                result = validate_algebra_bound_update(
                    load(case["bound"]),
                    load(case["usage"]),
                    load(case["validation"]),
                    PROFILE,
                    expected_repo=case["repo"],
                    expected_repo_sha=case["sha"],
                    expected_target_kind=case["target_kind"],
                    expected_process_version=PROCESS_VERSION,
                    expected_design_epoch=EPOCH,
                    expected_source_root_sha256=SOURCE_ROOT,
                    expected_profile_ref=PROFILE_REF,
                    expected_profile_blob_sha=PROFILE_BLOB_SHA,
                )
                self.assertEqual(result["repo"], case["repo"])
                self.assertEqual(result["repo_sha"], case["sha"])
                self.assertEqual(result["target_kind"], case["target_kind"])
                self.assertFalse(result["semantic_compliance_proved"])
                self.assertEqual(result["authorization_result"], "NOT_EVALUATED_HERE")


if __name__ == "__main__":
    unittest.main()
