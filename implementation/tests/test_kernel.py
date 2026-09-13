import tempfile
import unittest
from pathlib import Path

from garden_kernel.core import Claim, EpistemicStatus, EvidenceRef, ReceiptStatus, SemanticError, TypedValue, parse_claim
from garden_kernel.extractor import ObligationExtractor
from garden_kernel.store import KnowledgeStore
from garden_kernel.verifier import VerifierClass, VerifierRegistry


class CoreTests(unittest.TestCase):
    def test_parser_rejects_silent_semantics(self):
        with self.assertRaises(SemanticError):
            parse_claim({
                "claim_id": "c1", "subject": "s", "predicate": "p",
                "object": {"type_name": "String", "value": "x"},
                "confidence_magic": 0.9,
            })

    def test_status_is_explicit(self):
        c = parse_claim({
            "claim_id": "c1", "subject": "s", "predicate": "p",
            "object": {"type_name": "String", "value": "x"},
        })
        self.assertEqual(c.epistemic_status, EpistemicStatus.UNKNOWN)


class ExtractorTests(unittest.TestCase):
    def test_extracts_and_preserves_frontier(self):
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / "x.txt"
            p.write_text("[T-X]\n@D|INV-1|System MUST reject ambiguity.\n@ZZ|future|record\n", encoding="utf-8")
            m = ObligationExtractor().extract_paths([p])
            self.assertTrue(any(o.obligation_id == "DEF:INV-1" for o in m.obligations))
            self.assertEqual(len(m.gaps), 1)
            self.assertFalse(m.coverage_complete)


class StoreTests(unittest.TestCase):
    def setUp(self):
        self.store = KnowledgeStore()
        self.store.put_claim(Claim(
            claim_id="c1", subject="s", predicate="p",
            object=TypedValue("String", "x"), epistemic_status=EpistemicStatus.ASSERTED,
        ))

    def test_repetition_cannot_promote(self):
        with self.assertRaises(SemanticError):
            self.store.transition_status("c1", EpistemicStatus.SUPPORTED, reason="repeated")

    def test_admitted_evidence_can_support_explicit_transition(self):
        e = EvidenceRef("e1", "test", "fixture://e1", "abc")
        self.store.put_evidence(e)
        self.store.attach_evidence("c1", "e1", admitted=True)
        self.store.transition_status("c1", EpistemicStatus.SUPPORTED, reason="admitted fixture", evidence_ids=["e1"])
        self.assertEqual(self.store.get_claim("c1").epistemic_status, EpistemicStatus.SUPPORTED)

    def test_dependency_impact_traversal(self):
        self.store.add_dependency("claim:a", "artifact:x", "semantic")
        self.store.add_dependency("claim:b", "claim:a", "semantic")
        self.assertEqual(self.store.affected_by("artifact:x"), {"claim:a", "claim:b"})


class VerifierTests(unittest.TestCase):
    def test_class_separation_and_staleness(self):
        reg = VerifierRegistry()
        reg.register(
            verifier_id="compile-fixture", verifier_class=VerifierClass.COMPILE,
            version="1", implementation_bytes=b"compile-v1",
            protected_owner="Garden.ProtectedVerifier",
            fn=lambda b: (ReceiptStatus.PASS, ("syntactic validity",), ("python fixture",)),
        )
        receipt = reg.verify_bytes("compile-fixture", "a.py", b"print(1)", design_epoch="E1")
        self.assertEqual(receipt.result, ReceiptStatus.PASS)
        with self.assertRaises(SemanticError):
            reg.require_class(receipt, VerifierClass.FORMAL_PROOF)
        stale = reg.invalidate_if_changed(receipt, artifact=b"print(2)")
        self.assertEqual(stale.result, ReceiptStatus.STALE)

    def test_unprotected_verifier_cannot_register(self):
        reg = VerifierRegistry()
        with self.assertRaises(SemanticError):
            reg.register(
                verifier_id="self", verifier_class=VerifierClass.CONFORMANCE,
                version="1", implementation_bytes=b"candidate",
                protected_owner="Candidate.Agent", fn=lambda b: (ReceiptStatus.PASS, (), ()),
            )


if __name__ == "__main__":
    unittest.main()
