import unittest

from implementation.garden_kernel.integration_provenance import (
    AgentWorkIntent,
    assess_intents,
    compare_intents,
    validate_current_binding,
)

BASE = "1" * 40
ROOT = "2" * 64
EPOCH = f"Garden-v15.5@{ROOT}"


def intent(intent_id="a", **overrides):
    data = {
        "schema": "AgentWorkIntent/v1",
        "intent_id": intent_id,
        "agent_id": "agent:a",
        "work_package_id": "WP-X",
        "base_sha": BASE,
        "source_root_sha256": ROOT,
        "design_epoch_ref": EPOCH,
        "target_paths": ["implementation/a.py"],
        "target_symbols": ["Thing"],
        "semantic_domains": ["authority-resolution"],
        "affected_invariants": ["INV-1"],
        "affected_contracts": ["FC-1"],
        "intended_effect": "bounded change",
        "parallel_mode": "INDEPENDENT_COMPARISON",
    }
    data.update(overrides)
    return AgentWorkIntent.from_mapping(data)


class IntegrationProvenanceTests(unittest.TestCase):
    def test_different_files_same_semantic_domain_collide(self):
        a = intent("a", target_paths=["implementation/a.py"], target_symbols=[])
        b = intent("b", target_paths=["implementation/b.py"], target_symbols=[], affected_invariants=[], affected_contracts=[])
        result = compare_intents(a, b)
        self.assertEqual(result["classification"], "POTENTIAL_COLLISION")
        self.assertIn("SEMANTIC_DOMAIN_OVERLAP", result["reasons"])

    def test_parent_directory_overlap_collides(self):
        a = intent("a", target_paths=["implementation"])
        b = intent("b", target_paths=["implementation/garden_kernel/core.py"], semantic_domains=["other"], target_symbols=[], affected_invariants=[], affected_contracts=[])
        self.assertIn("PATH_OVERLAP", compare_intents(a, b)["reasons"])

    def test_shared_contract_collides_without_path_overlap(self):
        a = intent("a", target_paths=["a.py"], semantic_domains=["one"], target_symbols=[], affected_invariants=[])
        b = intent("b", target_paths=["b.py"], semantic_domains=["two"], target_symbols=[], affected_invariants=[])
        self.assertIn("CONTRACT_OVERLAP", compare_intents(a, b)["reasons"])

    def test_no_overlap_passes_without_receipt(self):
        a = intent("a", target_paths=["a.py"], semantic_domains=["one"], target_symbols=[], affected_invariants=[], affected_contracts=[])
        b = intent("b", target_paths=["b.py"], semantic_domains=["two"], target_symbols=[], affected_invariants=[], affected_contracts=[])
        self.assertEqual(assess_intents(a, [b])["disposition"], "PASS")

    def test_collision_requires_receipt(self):
        self.assertEqual(assess_intents(intent("a"), [intent("b")])["disposition"], "REQUIRES_INTEGRATION_RECEIPT")

    def test_compatible_receipt_requires_post_integration_tests(self):
        a, b = intent("a"), intent("b")
        receipt = {
            "schema": "IntegrationReceipt/v1", "current_intent_id": "a", "work_package_id": "WP-X",
            "base_sha": BASE, "source_root_sha256": ROOT, "design_epoch_ref": EPOCH,
            "concurrent_intent_ids": ["b"], "semantic_compare": "COMPATIBLE",
            "composition_evidence": ["manual semantic diff"],
        }
        self.assertEqual(assess_intents(a, [b], receipt)["disposition"], "BLOCKED")

    def test_complete_receipt_passes(self):
        a, b = intent("a"), intent("b")
        receipt = {
            "schema": "IntegrationReceipt/v1", "current_intent_id": "a", "work_package_id": "WP-X",
            "base_sha": BASE, "source_root_sha256": ROOT, "design_epoch_ref": EPOCH,
            "concurrent_intent_ids": ["b"], "semantic_compare": "COMPATIBLE",
            "composition_evidence": ["semantic delta composition checked"],
            "tests_after_integration": ["python -m unittest"],
        }
        self.assertEqual(assess_intents(a, [b], receipt)["disposition"], "PASS")

    def test_receipt_omitting_colliding_intent_blocks(self):
        a, b = intent("a"), intent("b")
        receipt = {
            "schema": "IntegrationReceipt/v1", "current_intent_id": "a", "work_package_id": "WP-X",
            "base_sha": BASE, "source_root_sha256": ROOT, "design_epoch_ref": EPOCH,
            "concurrent_intent_ids": [], "semantic_compare": "COMPATIBLE",
            "composition_evidence": ["x"], "tests_after_integration": ["y"],
        }
        self.assertEqual(assess_intents(a, [b], receipt)["disposition"], "BLOCKED")

    def test_binding_rejects_stale_source_root(self):
        errors = validate_current_binding(intent("a"), base_sha=BASE, source_root_sha256="3" * 64, design_epoch_ref=EPOCH)
        self.assertIn("STALE_OR_MISMATCHED_SOURCE_ROOT", errors)

    def test_binding_rejects_stale_base_sha(self):
        errors = validate_current_binding(intent("a"), base_sha="4" * 40, source_root_sha256=ROOT, design_epoch_ref=EPOCH)
        self.assertIn("STALE_OR_MISMATCHED_BASE_SHA", errors)


if __name__ == "__main__":
    unittest.main()
