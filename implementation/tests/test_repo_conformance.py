from __future__ import annotations

import json
from pathlib import Path
import unittest

from garden_kernel.repo_conformance import (
    RepoArtifactClass,
    audit_repo,
    load_repo_profile,
    validate_profile_against_manifest,
)


ROOT = Path(__file__).resolve().parents[2]
PROFILE = ROOT / "gsl" / "GSL_REPO_PROFILE.json"
MANIFEST = ROOT / "canonical" / "current" / "SOURCE_MANIFEST.json"


class RepoConformanceTests(unittest.TestCase):
    def setUp(self) -> None:
        self.profile = load_repo_profile(PROFILE)
        self.manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))

    def test_profile_is_bound_to_current_canonical_identity(self) -> None:
        validate_profile_against_manifest(self.profile, self.manifest)
        self.assertFalse(self.profile.semantic_compliance_proved)

    def test_audit_loads_entire_repo_without_silent_omission(self) -> None:
        report = audit_repo(ROOT, self.profile)
        records = {record.path: record for record in report.artifacts}
        self.assertGreater(report.artifact_count, 0)
        self.assertEqual(report.artifact_count, len(records))
        self.assertFalse(report.semantic_compliance_proved)

        self.assertEqual(
            records["canonical/current/Garden_System_v15.5_FULL_2026-09-12.txt"].artifact_class,
            RepoArtifactClass.CANONICAL_SOURCE,
        )
        self.assertEqual(
            records["implementation/garden_kernel/evolution_gate.py"].artifact_class,
            RepoArtifactClass.IMPLEMENTATION,
        )
        self.assertEqual(
            records["implementation/tests/test_repo_conformance.py"].artifact_class,
            RepoArtifactClass.TEST,
        )
        self.assertEqual(
            records[".github/workflows/kernel-ci.yml"].artifact_class,
            RepoArtifactClass.WORKFLOW,
        )
        self.assertEqual(
            records["work_packages/WP-009.md"].artifact_class,
            RepoArtifactClass.WORK_PACKAGE,
        )
        self.assertEqual(
            records["gsl/GSL_REPO_PROFILE.json"].artifact_class,
            RepoArtifactClass.CONFIGURATION,
        )

    def test_frontier_is_explicit_not_false_compliance(self) -> None:
        report = audit_repo(ROOT, self.profile)
        frontier = [r for r in report.artifacts if r.coverage_state == "FRONTIER"]
        self.assertEqual(len(frontier), report.frontier_artifact_count)
        for record in frontier:
            self.assertEqual(record.artifact_class, RepoArtifactClass.FRONTIER)
            self.assertEqual(record.rule_id, "UNCLASSIFIED-FRONTIER")


if __name__ == "__main__":
    unittest.main()
