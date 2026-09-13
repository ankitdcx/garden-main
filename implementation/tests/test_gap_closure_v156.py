from __future__ import annotations

import hashlib
import unittest

from garden_kernel.authority_path import (
    ActionEligibleArtifact,
    AuthorityProvenanceChain,
    AuthorityScope,
    authorize_artifact_trigger,
)
from garden_kernel.bootstrap_trust import (
    BootstrapTrustRootCeremonyReceipt,
    FrozenVerifierBinding,
    require_first_epoch_acceptance,
)
from garden_kernel.causality import (
    CausalLevel,
    CausalRelationLevelBinding,
    compose_causal_path,
    require_causal_level,
)
from garden_kernel.core import SemanticError
from garden_kernel.language_semantics import (
    LetBinding,
    LetForm,
    QueryDestinationKind,
    QueryResultBinding,
    bind_query_result,
)
from garden_kernel.provenance_manifest import (
    AuthorizedProvenanceView,
    ProvenanceClassManifest,
    ProvenanceDisposition,
    classify_node_class,
)
from garden_kernel.reasoning_profile import (
    ReasonMode,
    SanityGateResult,
    TransitionSanityInput,
    evaluate_transition_sanity,
    parse_reason_mode,
)


SHA_A = hashlib.sha256(b"a").hexdigest()
SHA_B = hashlib.sha256(b"b").hexdigest()


class V156GapClosureTests(unittest.TestCase):
    def test_first_epoch_requires_ceremony_transcript(self) -> None:
        with self.assertRaises(SemanticError):
            require_first_epoch_acceptance(
                candidate_design_epoch="v15.6-bootstrap",
                candidate_source_root=SHA_A,
                receipt=None,
            )
        verifier = FrozenVerifierBinding(
            binding_id="FVB-1",
            verifier_id="verifier:independent-1",
            verifier_version="1",
            verifier_hash=SHA_B,
            implementation_lineage="lineage:independent",
            test_corpus_root=SHA_A,
            independent_from_submitter=True,
        )
        receipt = BootstrapTrustRootCeremonyReceipt(
            ceremony_id="BTRC-1",
            candidate_design_epoch="v15.6-bootstrap",
            candidate_source_root=SHA_A,
            submitter_ref="human-source:submitter",
            participant_refs=("human-source:submitter", "auditor:independent"),
            witness_refs=("witness:external",),
            constitutional_authority_ref="authority:human-sovereign",
            transcript_sha256=SHA_B,
            frozen_verifiers=(verifier,),
            result="PASS",
        )
        require_first_epoch_acceptance(
            candidate_design_epoch="v15.6-bootstrap",
            candidate_source_root=SHA_A,
            receipt=receipt,
        )

    def test_shared_state_authority_amplification(self) -> None:
        writer = AuthorityScope(
            subject="agent:A",
            actions=frozenset({"write:Knowledge"}),
            resources=frozenset({"Knowledge"}),
            source_ref="env:A",
        )
        actor = AuthorityScope(
            subject="agent:B",
            actions=frozenset({"act:tool_x"}),
            resources=frozenset({"tool_x"}),
            source_ref="env:B",
        )
        artifact = ActionEligibleArtifact(
            artifact_id="claim:1",
            target_action="act:tool_x",
            target_resource="tool_x",
            authority_chain=AuthorityProvenanceChain(
                chain_id="chain:1",
                controlling_scopes=(writer,),
                provenance_refs=("claim:1", "env:A"),
            ),
        )
        self.assertFalse(authorize_artifact_trigger(acting_scope=actor, artifact=artifact))

        principal = AuthorityScope(
            subject="principal:P",
            actions=frozenset({"write:Knowledge", "act:tool_x"}),
            resources=frozenset({"Knowledge", "tool_x"}),
            source_ref="principal:P",
        )
        authorized_artifact = ActionEligibleArtifact(
            artifact_id="claim:2",
            target_action="act:tool_x",
            target_resource="tool_x",
            authority_chain=AuthorityProvenanceChain(
                chain_id="chain:2",
                controlling_scopes=(principal,),
                provenance_refs=("claim:2", "principal:P"),
            ),
        )
        self.assertTrue(
            authorize_artifact_trigger(acting_scope=actor, artifact=authorized_artifact)
        )

    def test_let_without_in_has_defined_scope(self) -> None:
        with self.assertRaises(SemanticError):
            LetBinding(
                name="x",
                bound_expression_ref="expr:5",
                form=LetForm.EXPRESSION,
            )
        stmt = LetBinding(
            name="x",
            bound_expression_ref="expr:5",
            form=LetForm.STATEMENT,
            enclosing_scope_ref="block:1",
        )
        self.assertEqual(stmt.result_type, "Unit")

    def test_query_result_destination_is_explicit(self) -> None:
        local = bind_query_result(
            query_ref="query:q",
            into_id="x",
            scope_ref="block:1",
            declared_output_ref=None,
            function_contract_ref=None,
        )
        self.assertEqual(local.destination_kind, QueryDestinationKind.LOCAL_BINDING)
        declared = bind_query_result(
            query_ref="query:q",
            into_id=None,
            scope_ref=None,
            declared_output_ref="output:answers",
            function_contract_ref="fc:module",
        )
        self.assertEqual(declared.destination_kind, QueryDestinationKind.DECLARED_OUTPUT)
        with self.assertRaisesRegex(SemanticError, "QUERY_RESULT_UNCONSUMED"):
            bind_query_result(
                query_ref="query:q",
                into_id=None,
                scope_ref=None,
                declared_output_ref=None,
                function_contract_ref=None,
            )

    def test_causes_requires_explicit_level(self) -> None:
        c0 = CausalRelationLevelBinding("A", "B", CausalLevel.C0_CORRELATION)
        with self.assertRaisesRegex(SemanticError, "CAUSAL_LEVEL_UNDERFLOW"):
            require_causal_level(c0, minimum_level=CausalLevel.C2_MECHANISTIC)
        c2 = CausalRelationLevelBinding(
            "A",
            "B",
            CausalLevel.C2_MECHANISTIC,
            model_refs=("model:m",),
            assumption_refs=("assumption:a",),
        )
        require_causal_level(c2, minimum_level=CausalLevel.C2_MECHANISTIC)
        c1 = CausalRelationLevelBinding("B", "C", CausalLevel.C1_TEMPORAL)
        self.assertEqual(compose_causal_path((c2, c1)), CausalLevel.C1_TEMPORAL)

    def test_r0_is_not_reason_mode(self) -> None:
        with self.assertRaisesRegex(SemanticError, "R0_IS_SANITY_GATE_NOT_REASON_MODE"):
            parse_reason_mode("R0")
        self.assertEqual(parse_reason_mode("R1"), ReasonMode.R1_LOCAL)
        self.assertEqual(
            evaluate_transition_sanity(
                TransitionSanityInput(
                    transition_ref="t:1",
                    declared_abstraction="process",
                    input_type="A",
                    output_type="B",
                    scope_ref="scope:1",
                    obvious_contradiction=False,
                    admissibility_known=True,
                )
            ),
            SanityGateResult.PASS,
        )

    def test_redaction_distinct_from_absence(self) -> None:
        manifest = ProvenanceClassManifest(
            manifest_id="prov:1",
            expected_node_classes=frozenset({"Observation", "Evidence", "Claim"}),
            expected_edge_kinds=frozenset({"derivedFrom", "supports"}),
            protected_node_classes=frozenset({"Observation"}),
        )
        view = AuthorizedProvenanceView(
            manifest_commitment=manifest.commitment,
            visible_node_counts={"Evidence": 1},
            redacted_node_classes=frozenset({"Observation"}),
            visible_edge_counts={"supports": 1},
            redacted_edge_kinds=frozenset(),
        )
        self.assertEqual(
            classify_node_class(manifest, view, "Observation"),
            ProvenanceDisposition.REDACTED,
        )
        self.assertEqual(
            classify_node_class(manifest, view, "Claim"),
            ProvenanceDisposition.PROVENANCE_GAP,
        )
        self.assertEqual(
            classify_node_class(manifest, view, "Model"),
            ProvenanceDisposition.NOT_APPLICABLE,
        )


if __name__ == "__main__":
    unittest.main()
