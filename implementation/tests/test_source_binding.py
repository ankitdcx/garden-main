import unittest

from garden_kernel.core import Obligation
from garden_kernel.source_binding import build_source_bindings, diff_source_bindings


class SourceBindingTests(unittest.TestCase):
    def test_definition_identity_survives_nonsemantic_location_change(self):
        a = Obligation(
            obligation_id="DEF:INV-1", text="System MUST reject ambiguity.",
            source_file="A.txt", source_anchor="[A-X]", owner="Engine.Proof",
            status="EXTRACTED_DEFINITION",
        )
        b = Obligation(
            obligation_id="DEF:INV-1", text="System MUST reject ambiguity.",
            source_file="A.txt", source_anchor="[A-X]", owner="Engine.Proof",
            status="EXTRACTED_DEFINITION",
        )
        first = build_source_bindings([a])
        second = build_source_bindings([b])
        diff = diff_source_bindings(first, second)
        self.assertEqual(diff["unchanged_count"], 1)
        self.assertEqual(diff["stale_binding_keys"], [])

    def test_semantic_change_marks_binding_stale(self):
        before = Obligation(
            obligation_id="DEF:INV-1", text="System MUST reject ambiguity.",
            source_file="A.txt", source_anchor="[A-X]", owner="Engine.Proof",
            status="EXTRACTED_DEFINITION",
        )
        after = Obligation(
            obligation_id="DEF:INV-1", text="System MAY accept ambiguity.",
            source_file="A.txt", source_anchor="[A-X]", owner="Engine.Proof",
            status="EXTRACTED_DEFINITION",
        )
        diff = diff_source_bindings(build_source_bindings([before]), build_source_bindings([after]))
        self.assertEqual(diff["stale_binding_keys"], ["DEF:INV-1"])
        self.assertEqual(len(diff["changed"]), 1)

    def test_free_text_identity_ignores_whitespace(self):
        before = Obligation(
            obligation_id="TEXT:old", text="Action  MUST   remain bounded.",
            source_file="T.txt", source_anchor="[T-X]", status="EXTRACTED_NORMATIVE_TEXT",
        )
        after = Obligation(
            obligation_id="TEXT:new", text="Action MUST remain bounded.",
            source_file="T.txt", source_anchor="[T-X]", status="EXTRACTED_NORMATIVE_TEXT",
        )
        diff = diff_source_bindings(build_source_bindings([before]), build_source_bindings([after]))
        self.assertEqual(diff["unchanged_count"], 1)
        self.assertEqual(diff["stale_binding_keys"], [])


if __name__ == "__main__":
    unittest.main()
