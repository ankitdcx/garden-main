from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from scripts.build_evolution_audit_chain import _record_paths


class EvolutionAuditScriptTests(unittest.TestCase):
    def test_absent_absolute_optional_receipt_path_is_ignored(self):
        with tempfile.TemporaryDirectory() as tmp:
            absent = Path(tmp) / "not-created-gate-receipts"
            self.assertTrue(absent.is_absolute())
            self.assertFalse(absent.exists())
            self.assertEqual(_record_paths([str(absent)]), [])

    def test_existing_absolute_receipt_directory_is_collected(self):
        with tempfile.TemporaryDirectory() as tmp:
            directory = Path(tmp) / "receipts"
            directory.mkdir()
            receipt = directory / "a.json"
            receipt.write_text("{}\n", encoding="utf-8")
            self.assertEqual(_record_paths([str(directory)]), [receipt])

    def test_absolute_receipt_glob_collects_only_matching_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            directory = Path(tmp) / "receipts"
            directory.mkdir()
            first = directory / "a.json"
            second = directory / "b.json"
            ignored = directory / "notes.txt"
            first.write_text("{}\n", encoding="utf-8")
            second.write_text("{}\n", encoding="utf-8")
            ignored.write_text("not a receipt\n", encoding="utf-8")

            found = _record_paths([str(directory / "*.json")])

            self.assertEqual(found, [first, second])

    def test_unmatched_absolute_receipt_glob_is_empty(self):
        with tempfile.TemporaryDirectory() as tmp:
            pattern = str(Path(tmp) / "not-created" / "*.json")
            self.assertEqual(_record_paths([pattern]), [])


if __name__ == "__main__":
    unittest.main()
