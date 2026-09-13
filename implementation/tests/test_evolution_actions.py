import unittest

from garden_kernel.core import SemanticError
from garden_kernel.evolution_actions import (
    CONTRACTS,
    Condition,
    EvolutionAction,
    EvolutionVerb,
    validate_action_shape,
)
from garden_kernel.evolution_epoch import (
    BindingStatus,
    EvolutionArtifactBinding,
    EvolutionArtifactKind,
    require_current_for_accumulation,
    validate_evolution_binding,
)


class EvolutionActionContractTests(unittest.TestCase):
    def make_valid(self, verb: EvolutionVerb) -> EvolutionAction:
        contract = CONTRACTS[verb]
        return EvolutionAction(
            action_id=f"ACT-{verb.value}",
            verb=verb,
            actor_ref="agent:test",
            subject_ref="subject:test",
            input_refs=("input:1",),
            provenance_refs=("source:v15.5",),
            satisfied_preconditions=contract.preconditions,
            claimed_postconditions=contract.postconditions,
        )

    def test_exact_five_pipeline_verbs(self):
        self.assertEqual(
            {v.value for v in EvolutionVerb},
            {"PROPOSE", "TRIAGE", "TEST", "ACCUMULATE", "MATERIALIZE"},
        )

    def test_every_verb_has_explicit_pre_and_post_conditions(self):
        self.assertEqual(set(CONTRACTS), set(EvolutionVerb))
        for verb, contract in CONTRACTS.items():
            with self.subTest(verb=verb.value):
                self.assertTrue(contract.preconditions)
                self.assertTrue(contract.postconditions)

    def test_all_valid_shapes_pass_step1_validation(self):
        for verb in EvolutionVerb:
            with self.subTest(verb=verb.value):
                validate_action_shape(self.make_valid(verb))

    def test_missing_precondition_fails_closed(self):
        valid = self.make_valid(EvolutionVerb.PROPOSE)
        broken = EvolutionAction(
            action_id=valid.action_id,
            verb=valid.verb,
            actor_ref=valid.actor_ref,
            subject_ref=valid.subject_ref,
            input_refs=valid.input_refs,
            provenance_refs=valid.provenance_refs,
            satisfied_preconditions=valid.satisfied_preconditions - {Condition.PROVENANCE_PRESENT},
            claimed_postconditions=valid.claimed_postconditions,
        )
        with self.assertRaises(SemanticError):
            validate_action_shape(broken)

    def test_missing_postcondition_fails_closed(self):
        valid = self.make_valid(EvolutionVerb.MATERIALIZE)
        broken = EvolutionAction(
            action_id=valid.action_id,
            verb=valid.verb,
            actor_ref=valid.actor_ref,
            subject_ref=valid.subject_ref,
            input_refs=valid.input_refs,
            provenance_refs=valid.provenance_refs,
            satisfied_preconditions=valid.satisfied_preconditions,
            claimed_postconditions=valid.claimed_postconditions - {Condition.PREDECESSOR_UNCHANGED},
        )
        with self.assertRaises(SemanticError):
            validate_action_shape(broken)

    def test_materialize_never_implies_promotion(self):
        post = CONTRACTS[EvolutionVerb.MATERIALIZE].postconditions
        self.assertIn(Condition.CANONICAL_POINTER_UNCHANGED, post)
        self.assertIn(Condition.PREDECESSOR_UNCHANGED, post)

    def test_mutating_actions_cannot_expand_authority_by_contract(self):
        for verb in (EvolutionVerb.PROPOSE, EvolutionVerb.TRIAGE, EvolutionVerb.ACCUMULATE, EvolutionVerb.MATERIALIZE):
            with self.subTest(verb=verb.value):
                self.assertIn(Condition.NO_AUTHORITY_EXPANSION, CONTRACTS[verb].postconditions)

    def test_missing_provenance_is_rejected_at_construction(self):
        contract = CONTRACTS[EvolutionVerb.TEST]
        with self.assertRaises(SemanticError):
            EvolutionAction(
                action_id="ACT-NO-PROV",
                verb=EvolutionVerb.TEST,
                actor_ref="agent:test",
                subject_ref="subject:test",
                input_refs=("input:1",),
                provenance_refs=(),
                satisfied_preconditions=contract.preconditions,
                claimed_postconditions=contract.postconditions,
            )


class EvolutionEpochTests(unittest.TestCase):
    def binding(self, *, artifact_id="F1", kind=EvolutionArtifactKind.FINDING, epoch="v15.5", dep="abc", declare_closure=True):
        return EvolutionArtifactBinding(
            artifact_id=artifact_id,
            kind=kind,
            design_epoch=epoch,
            dependencies={"canonical_root": dep},
            required_dependencies=frozenset({"canonical_root"}) if declare_closure else None,
            derived_from_refs=("source:review",),
        )

    def test_current_binding_passes(self):
        result = validate_evolution_binding(
            self.binding(),
            current_design_epoch="v15.5",
            current_dependencies={"canonical_root": "abc"},
        )
        self.assertEqual(result.status, BindingStatus.CURRENT)

    def test_epoch_change_marks_finding_stale(self):
        result = validate_evolution_binding(
            self.binding(epoch="v15.5"),
            current_design_epoch="v15.6",
            current_dependencies={"canonical_root": "abc"},
        )
        self.assertEqual(result.status, BindingStatus.STALE)

    def test_dependency_change_marks_test_stale(self):
        result = validate_evolution_binding(
            self.binding(artifact_id="T1", kind=EvolutionArtifactKind.TEST, dep="old"),
            current_design_epoch="v15.5",
            current_dependencies={"canonical_root": "new"},
        )
        self.assertEqual(result.status, BindingStatus.STALE)

    def test_undeclared_closure_is_unknown(self):
        result = validate_evolution_binding(
            self.binding(declare_closure=False),
            current_design_epoch="v15.5",
            current_dependencies={"canonical_root": "abc"},
        )
        self.assertEqual(result.status, BindingStatus.UNKNOWN)

    def test_stale_or_unknown_artifact_cannot_accumulate(self):
        for binding, epoch, deps in (
            (self.binding(epoch="v15.5"), "v15.6", {"canonical_root": "abc"}),
            (self.binding(declare_closure=False), "v15.5", {"canonical_root": "abc"}),
        ):
            with self.subTest(binding=binding.artifact_id, epoch=epoch):
                with self.assertRaises(SemanticError):
                    require_current_for_accumulation(
                        (binding,),
                        current_design_epoch=epoch,
                        current_dependencies=deps,
                    )

    def test_rederived_current_artifact_can_accumulate(self):
        rederived = EvolutionArtifactBinding(
            artifact_id="F1-R1",
            kind=EvolutionArtifactKind.FINDING,
            design_epoch="v15.6",
            dependencies={"canonical_root": "new"},
            required_dependencies=frozenset({"canonical_root"}),
            derived_from_refs=("F1",),
        )
        require_current_for_accumulation(
            (rederived,),
            current_design_epoch="v15.6",
            current_dependencies={"canonical_root": "new"},
        )


if __name__ == "__main__":
    unittest.main()
