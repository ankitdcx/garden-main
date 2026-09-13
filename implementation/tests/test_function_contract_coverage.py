from __future__ import annotations

from dataclasses import replace
import json
from pathlib import Path
import unittest

from garden_kernel.core import SemanticError
from garden_kernel.function_contracts import (
    FunctionContractRegistry,
    FunctionContractBinding,
    audit_function_contract_coverage,
    enumerate_scoped_public_functions,
    load_function_contract_registry,
    validate_registry_against_manifest,
)


ROOT = Path(__file__).resolve().parents[2]
REGISTRY_PATH = ROOT / "gsl" / "FUNCTION_CONTRACTS.json"
MANIFEST_PATH = ROOT / "canonical" / "current" / "SOURCE_MANIFEST.json"


class FunctionContractCoverageTests(unittest.TestCase):
    def setUp(self) -> None:
        self.registry = load_function_contract_registry(REGISTRY_PATH)
        self.manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))

    def test_registry_is_bound_to_current_canonical_identity(self) -> None:
        validate_registry_against_manifest(self.registry, self.manifest)
        self.assertFalse(self.registry.semantic_compliance_proved)

    def test_critical_production_functions_have_declared_reference_contracts(self) -> None:
        report = audit_function_contract_coverage(ROOT, self.registry)
        records = {record.identity: record for record in report.functions}
        expected = {
            "implementation/garden_kernel/evolution_gate.py::evaluate_evolution_action",
            "implementation/garden_kernel/evolution_transport.py::evaluate_production_request",
            "implementation/garden_kernel/evolution_authority.py::can_execute",
            "implementation/garden_kernel/evolution_epoch.py::require_current_for_accumulation",
            "implementation/garden_kernel/evolution_trust.py::verify_governance_receipt",
            "implementation/garden_kernel/evolution_trust.py::verify_attestation_receipts",
        }
        self.assertTrue(expected <= set(records))
        for identity in expected:
            self.assertEqual(records[identity].coverage_state, "DECLARED_REFERENCE")
            self.assertIsNotNone(records[identity].contract_id)
            self.assertTrue(records[identity].test_refs)

    def test_frontier_is_explicit_and_never_semantic_compliance(self) -> None:
        report = audit_function_contract_coverage(ROOT, self.registry)
        frontier = [record for record in report.functions if record.coverage_state == "FRONTIER"]
        self.assertEqual(len(frontier), report.frontier_function_count)
        self.assertEqual(
            report.declared_contract_count + report.frontier_function_count,
            report.scoped_function_count,
        )
        self.assertFalse(report.semantic_compliance_proved)
        self.assertLessEqual(report.declaration_coverage_ratio, 1.0)

    def test_registry_cannot_claim_semantic_compliance(self) -> None:
        payload = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
        payload["semantic_compliance_proved"] = True
        with self.assertRaises(SemanticError):
            from tempfile import NamedTemporaryFile
            with NamedTemporaryFile("w", suffix=".json", delete=False) as handle:
                json.dump(payload, handle)
                path = handle.name
            try:
                load_function_contract_registry(path)
            finally:
                Path(path).unlink(missing_ok=True)

    def test_missing_registered_function_fails_closed(self) -> None:
        sample = self.registry.contracts[0]
        missing = replace(sample, contract_id="FC-MISSING", function="does_not_exist")
        registry = replace(
            self.registry,
            contracts=(*self.registry.contracts, missing),
        )
        with self.assertRaises(SemanticError):
            enumerate_scoped_public_functions(ROOT, registry)

    def test_contract_semantic_fields_are_nonempty(self) -> None:
        for contract in self.registry.contracts:
            self.assertTrue(contract.input_semantics)
            self.assertTrue(contract.output_semantics)
            self.assertTrue(contract.error_semantics)
            self.assertTrue(contract.unknown_semantics)
            self.assertTrue(contract.effect_semantics)
            self.assertTrue(contract.proof_obligations)
            self.assertTrue(contract.test_refs)


if __name__ == "__main__":
    unittest.main()
