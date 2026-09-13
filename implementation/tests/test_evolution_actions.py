import unittest

from garden_kernel.core import SemanticError
from garden_kernel.evolution_actions import (
    CONTRACTS,
    Condition,
    EvolutionAction,
    EvolutionVerb,
    validate_action_shape,
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


if __name__ == "__main__":
    unittest.main()
