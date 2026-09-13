from __future__ import annotations

import json
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[2]
ANNEXURE = ROOT / "canonical" / "current" / "Garden_Annexure_v15.5_FULL_2026-09-12.txt"
CATALOG_DELTA = ROOT / "design_deltas" / "v15.6" / "CATALOG_ADDITIONS.json"
RIGHT_RE = re.compile(r"^@D\|RIGHT-(\d{3})\|", re.MULTILINE)


class DesignDeltaArtifactTests(unittest.TestCase):
    def test_catalogue_candidate_ids_are_unique_and_close_grammar_gap(self) -> None:
        payload = json.loads(CATALOG_DELTA.read_text(encoding="utf-8"))
        entries = payload["entries"]
        ids = [entry["schema_id"] for entry in entries]
        self.assertEqual(len(ids), len(set(ids)))
        by_name = {entry["name"]: entry for entry in entries}
        self.assertEqual(by_name["AuthorityDecl"]["schema_id"], "SCHEMA-A8447C581A")
        self.assertEqual(by_name["EffectDecl"]["schema_id"], "SCHEMA-D1DD528992")
        self.assertEqual(payload["status"], "CANDIDATE_NOT_CANONICAL")

    def test_rights_generated_view_order_is_active_then_nonactive(self) -> None:
        source = ANNEXURE.read_text(encoding="utf-8")
        found = {int(value) for value in RIGHT_RE.findall(source)}
        for number in range(1, 28):
            self.assertIn(number, found)
        view_order = [n for n in range(1, 26) if n in found] + [26, 27]
        self.assertEqual(view_order, list(range(1, 28)))
        # The immutable predecessor may remain physically interleaved; the v15.6
        # reader-view rule is explicitly non-semantic and must not renumber IDs.
        self.assertEqual(len(view_order), 27)


if __name__ == "__main__":
    unittest.main()
