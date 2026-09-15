from __future__ import annotations

import importlib.util
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "scripts" / "build_evolution_audit_chain.py"

spec = importlib.util.spec_from_file_location("build_evolution_audit_chain", SCRIPT)
module = importlib.util.module_from_spec(spec)
assert spec and spec.loader
spec.loader.exec_module(module)


class RecordPathResolutionTests(unittest.TestCase):
    def test_missing_absolute_optional_path_is_ignored(self):
        missing = Path(tempfile.gettempdir()) / "garden-missing-audit-records-never-created"
        self.assertEqual(module._record_paths([str(missing)]), [])

    def test_absolute_directory_and_glob_are_supported(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            record = root / "receipt.json"
            record.write_text("{}\n", encoding="utf-8")
            self.assertEqual(module._record_paths([str(root)]), [record])
            self.assertEqual(module._record_paths([str(root / "*.json")]), [record])


if __name__ == "__main__":
    unittest.main()
