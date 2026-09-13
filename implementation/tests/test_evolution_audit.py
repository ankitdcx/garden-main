from __future__ import annotations

import copy
import unittest

from garden_kernel.core import SemanticError
from garden_kernel.evolution_audit import GENESIS_HASH, build_audit_chain, validate_audit_chain


EPOCH = "v15.5"
ROOT = "6" * 64


def records():
    return [
        {
            "record_ref": "/tmp/conformance/reasoning.json",
            "record_sha256": "1" * 64,
            "record_schema": "GardenEvolutionReasoningConformanceReport/v1",
            "action_id": "A-1",
            "disposition": "PASS",
        },
        {
            "record_ref": "/tmp/gates/a-1.receipt.json",
            "record_sha256": "2" * 64,
            "record_schema": "GardenEvolutionProductionGateReceipt/v1",
            "action_id": "A-1",
            "disposition": "REJECT",
        },
    ]


class EvolutionAuditTests(unittest.TestCase):
    def test_build_and_validate_chain(self):
        chain = build_audit_chain(records(), chain_id="RUN-1", design_epoch=EPOCH, canonical_source_root_sha256=ROOT)
        self.assertEqual(chain["entries"][0]["previous_entry_hash"], GENESIS_HASH)
        self.assertEqual(chain["entries"][1]["previous_entry_hash"], chain["entries"][0]["entry_hash"])
        receipt = validate_audit_chain(chain, expected_design_epoch=EPOCH, expected_source_root_sha256=ROOT)
        self.assertTrue(receipt["tamper_evident"])
        self.assertEqual(receipt["authorization_result"], "NOT_EVALUATED_HERE")

    def test_content_tamper_fails(self):
        chain = build_audit_chain(records(), chain_id="RUN-1", design_epoch=EPOCH, canonical_source_root_sha256=ROOT)
        bad = copy.deepcopy(chain)
        bad["entries"][0]["disposition"] = "ALLOW"
        with self.assertRaisesRegex(SemanticError, "content hash mismatch"):
            validate_audit_chain(bad)

    def test_reordering_fails(self):
        chain = build_audit_chain(records(), chain_id="RUN-1", design_epoch=EPOCH, canonical_source_root_sha256=ROOT)
        bad = copy.deepcopy(chain)
        bad["entries"] = [bad["entries"][1], bad["entries"][0]]
        with self.assertRaisesRegex(SemanticError, "sequence is not contiguous"):
            validate_audit_chain(bad)

    def test_deletion_without_count_update_fails(self):
        chain = build_audit_chain(records(), chain_id="RUN-1", design_epoch=EPOCH, canonical_source_root_sha256=ROOT)
        bad = copy.deepcopy(chain)
        bad["entries"].pop()
        with self.assertRaisesRegex(SemanticError, "entry_count mismatch"):
            validate_audit_chain(bad)

    def test_stale_identity_fails(self):
        chain = build_audit_chain(records(), chain_id="RUN-1", design_epoch=EPOCH, canonical_source_root_sha256=ROOT)
        with self.assertRaisesRegex(SemanticError, "stale for current DesignEpoch"):
            validate_audit_chain(chain, expected_design_epoch="v15.6")

    def test_audit_descriptor_cannot_mint_authority(self):
        bad = records()
        bad[0]["human_signoff"] = True
        with self.assertRaisesRegex(SemanticError, "may not mint trust fields"):
            build_audit_chain(bad, chain_id="RUN-1", design_epoch=EPOCH, canonical_source_root_sha256=ROOT)


if __name__ == "__main__":
    unittest.main()
