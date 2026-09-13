import unittest

from garden_kernel.evolution_actions import CONTRACTS, EvolutionAction, EvolutionVerb
from garden_kernel.evolution_authority import EvolutionAgentRole, make_role_envelope
from garden_kernel.evolution_epoch import EvolutionArtifactBinding, EvolutionArtifactKind
from garden_kernel.evolution_gate import EvolutionGateContext, GateDecision, evaluate_evolution_action


def make_action(verb, subject):
    c = CONTRACTS[verb]
    return EvolutionAction(
        action_id=f"A-{verb.value}", verb=verb, actor_ref="agent:test",
        subject_ref=subject, input_refs=("input:1",), provenance_refs=("source:v15.5",),
        satisfied_preconditions=c.preconditions, claimed_postconditions=c.postconditions,
    )


def envelope(role, resource):
    return make_role_envelope(
        subject="agent:test", role=role, granted_by="human:root", resources={resource}
    )


def delta(epoch="v15.5"):
    return EvolutionArtifactBinding(
        artifact_id="D1", kind=EvolutionArtifactKind.DELTA, design_epoch=epoch,
        dependencies={"canonical_root": "abc"},
        required_dependencies=frozenset({"canonical_root"}), derived_from_refs=("F1",),
    )


class GateBehaviorTests(unittest.TestCase):
    def test_authorized_proposal_allows(self):
        a = make_action(EvolutionVerb.PROPOSE, "mechanism:A")
        ctx = EvolutionGateContext("v15.5", {"canonical_root": "abc"}, (envelope(EvolutionAgentRole.REVIEWER, "mechanism:A"),))
        self.assertEqual(evaluate_evolution_action(a, ctx).decision, GateDecision.ALLOW)

    def test_missing_authority_escalates(self):
        a = make_action(EvolutionVerb.PROPOSE, "mechanism:A")
        ctx = EvolutionGateContext("v15.5", {"canonical_root": "abc"}, ())
        self.assertEqual(evaluate_evolution_action(a, ctx).decision, GateDecision.ESCALATE)

    def test_stale_delta_rejects_accumulation(self):
        a = make_action(EvolutionVerb.ACCUMULATE, "successor:v15.6")
        ctx = EvolutionGateContext(
            "v15.6", {"canonical_root": "abc"},
            (envelope(EvolutionAgentRole.ACCUMULATOR, "successor:v15.6"),),
            bound_inputs=(delta("v15.5"),),
        )
        self.assertEqual(evaluate_evolution_action(a, ctx).decision, GateDecision.REJECT)

    def test_materialization_requires_fresh_review_or_human_signoff(self):
        a = make_action(EvolutionVerb.MATERIALIZE, "successor:v15.6")
        base = dict(
            current_design_epoch="v15.5",
            current_dependencies={"canonical_root": "abc"},
            authority_envelopes=(envelope(EvolutionAgentRole.MATERIALIZER, "successor:v15.6"),),
            bound_inputs=(delta(),),
        )
        self.assertEqual(evaluate_evolution_action(a, EvolutionGateContext(**base)).decision, GateDecision.ESCALATE)
        self.assertEqual(evaluate_evolution_action(a, EvolutionGateContext(**base, independent_review=True)).decision, GateDecision.ALLOW)


if __name__ == "__main__":
    unittest.main()
