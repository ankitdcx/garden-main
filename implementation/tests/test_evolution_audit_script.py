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


if __name__ == "__main__":
    unittest.main()
