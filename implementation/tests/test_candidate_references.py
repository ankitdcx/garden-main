from __future__ import annotations

import importlib.util
from pathlib import Path
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location("check_candidate_references", ROOT / "scripts/check_candidate_references.py")
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class CandidateReferenceAuditTests(unittest.TestCase):
    def test_exact_semantic_and_human_definitions_resolve(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "candidate.txt"
            source.write_text("@N|SemanticAnchor: [A-ONE]\n1. HUMAN SECTION  [H-01]\n", encoding="utf-8")
            result = MODULE.check_reported_references([source], ["[A-ONE]", "[H-01]"])
        self.assertEqual([item["anchor"] for item in result["resolved_explicit_definitions"]], ["[A-ONE]", "[H-01]"])
        self.assertEqual(result["still_unresolved"], [])

    def test_exact_negated_anchor_is_not_treated_as_definition(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "candidate.txt"
            source.write_text("no [T-REGULATION-COUPLING] anchor is created\n", encoding="utf-8")
            result = MODULE.check_reported_references([source], ["[T-REGULATION-COUPLING]"])
        self.assertEqual(result["resolved_explicit_definitions"], [])
        self.assertEqual(result["intentionally_not_defined"][0]["anchor"], "[T-REGULATION-COUPLING]")

    def test_unknown_reference_remains_unresolved(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "candidate.txt"
            source.write_text("Reference: [A-MISSING]\n", encoding="utf-8")
            result = MODULE.check_reported_references([source], ["[A-MISSING]"])
        self.assertEqual(result["still_unresolved"], ["[A-MISSING]"])

    def test_mentions_and_prefixes_do_not_define_references(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "candidate.txt"
            source.write_text("See [A-MENTION].\nSemanticAnchor: [A-OTHER]-suffix\n", encoding="utf-8")
            result = MODULE.check_reported_references([source], ["[A-MENTION]", "[A-OTHER]"])
        self.assertEqual(result["resolved_explicit_definitions"], [])
        self.assertEqual(result["still_unresolved"], ["[A-MENTION]", "[A-OTHER]"])


if __name__ == "__main__":
    unittest.main()
