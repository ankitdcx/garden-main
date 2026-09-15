from __future__ import annotations

import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from garden_kernel.process_engine import CycleBinding, ProcessFactory, ProcessRoute, ProcessState
from garden_kernel.section_units import build_inventory


ROOT = Path(__file__).resolve().parents[2]
SOURCE_DIR = ROOT / "canonical" / "current"
MANIFEST = json.loads((SOURCE_DIR / "SOURCE_MANIFEST.json").read_text(encoding="utf-8"))
PROFILE = json.loads((ROOT / "gsl" / "EVOLUTION_ALGEBRA_PROFILE.json").read_text(encoding="utf-8"))


class SectionUnitInventoryTests(unittest.TestCase):
    def test_synthetic_anchor_segmentation_is_contiguous_and_conservative(self):
        with tempfile.TemporaryDirectory() as tmp:
            source_dir = Path(tmp)
            body = (
                "release header\n"
                "SemanticAnchor: [S-ONE]\n"
                "MUST preserve evidence.\n"
                "  [S-TWO] table-of-contents reference only\n"
                "[S-TWO] Explanatory mechanism\n"
                "Example only.\n"
                "SemanticAnchor: [S-HISTORY]\n"
                "Historical retrospective archive.\n"
            )
            raw = body.encode("utf-8")
            import hashlib
            digest = hashlib.sha256(raw).hexdigest()
            path = source_dir / "one.txt"
            path.write_bytes(raw)
            manifest = {
                "schema": "GardenCanonicalSourceManifest/v1",
                "release": "Garden vX",
                "source_root_sha256": "f" * 64,
                "files": {
                    "User": {"name": "one.txt", "bytes": len(raw), "sha256": digest},
                    "System": {"name": "one.txt", "bytes": len(raw), "sha256": digest},
                    "Technical": {"name": "one.txt", "bytes": len(raw), "sha256": digest},
                    "Annexure": {"name": "one.txt", "bytes": len(raw), "sha256": digest},
                    "Theories": {"name": "one.txt", "bytes": len(raw), "sha256": digest},
                },
            }
            inventory = build_inventory(source_dir=source_dir, manifest=manifest, process_version="1.4")
            self.assertTrue(inventory.coverage_complete)
            self.assertEqual(inventory.counts()["TOTAL"], 20)
            self.assertGreater(inventory.counts()["TIER_A"], 0)
            self.assertGreater(inventory.counts()["TIER_B"], 0)
            self.assertGreater(inventory.counts()["TIER_C"], 0)

    def test_current_five_file_inventory_has_exact_denominator(self):
        inventory = build_inventory(source_dir=SOURCE_DIR, manifest=MANIFEST, process_version="1.4")
        counts = inventory.counts()
        self.assertTrue(inventory.coverage_complete)
        self.assertEqual(counts["TOTAL"], counts["TIER_A"] + counts["TIER_B"] + counts["TIER_C"])
        self.assertGreater(counts["TOTAL"], 5)
        self.assertEqual(len(inventory.source_hashes), 5)
        expected_hashes = {entry["name"]: entry["sha256"] for entry in MANIFEST["files"].values()}
        self.assertEqual(dict(inventory.source_hashes), expected_hashes)
        receipt = inventory.count_receipt(qualified=0, stale=0, unreviewed=counts["TOTAL"])
        self.assertEqual(receipt["UNREVIEWED"], receipt["TOTAL"])
        self.assertFalse(receipt["sweep_completion_valid"])
        print("CANONICAL_SECTION_COUNT_RECEIPT_TEST=" + json.dumps(receipt, sort_keys=True))

    def test_every_current_unit_can_be_routed_through_process_factory(self):
        inventory = build_inventory(source_dir=SOURCE_DIR, manifest=MANIFEST, process_version="1.4")
        for unit in inventory.units:
            binding = CycleBinding(
                cycle_id=f"TEST-{unit.unit_id}",
                process_version="1.4",
                design_epoch="v15.5",
                source_root_sha256=inventory.source_root_sha256,
                repo_heads={"garden-main": "TEST_HEAD"},
            )
            process = ProcessFactory.create(ProcessRoute.SECTION_UNIT_REVIEW, binding=binding, work_id=unit.unit_id)
            receipt = process.advance(
                ProcessState.ROUTED,
                satisfied_gates=["ROUTE_CLASSIFIED"],
                algebra_profile=PROFILE,
                source_obligation_refs=[
                    "governance/PROCESS_CURRENT.json",
                    f"canonical/current/{unit.source_file}:{unit.start_line}-{unit.end_line}",
                ],
            )
            self.assertEqual(receipt["route"], "SECTION_UNIT_REVIEW")
            self.assertEqual(receipt["to_state"], "ROUTED")
            self.assertEqual(receipt["process_operator"], "BRANCH")
            self.assertEqual(receipt["algebra_validation"]["authorization_result"], "NOT_EVALUATED_HERE")

    @unittest.skipUnless(os.environ.get("GITHUB_ACTIONS") == "true", "CI artifact emission")
    def test_ci_emits_canonical_section_inventory_artifacts(self):
        out = Path("/tmp/wp009-conformance")
        out.mkdir(parents=True, exist_ok=True)
        subprocess.run(
            [
                sys.executable,
                str(ROOT / "scripts" / "build_canonical_section_units.py"),
                "--repo-head",
                os.environ["GITHUB_SHA"],
                "--inventory-output",
                str(out / "canonical-section-inventory.json"),
                "--count-output",
                str(out / "canonical-section-count.json"),
                "--process-output",
                str(out / "canonical-section-routing.json"),
            ],
            cwd=ROOT,
            check=True,
            env={**os.environ, "PYTHONPATH": str(ROOT / "implementation")},
        )
        receipt = json.loads((out / "canonical-section-count.json").read_text(encoding="utf-8"))
        self.assertTrue(receipt["coverage_complete"])
        self.assertEqual(receipt["UNREVIEWED"], receipt["TOTAL"])


if __name__ == "__main__":
    unittest.main()
