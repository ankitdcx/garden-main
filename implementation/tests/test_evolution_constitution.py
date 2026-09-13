import unittest

from garden_kernel.evolution_actions import CONTRACTS, EvolutionAction, EvolutionVerb
from garden_kernel.evolution_authority import EvolutionAgentRole, make_role_envelope
from garden_kernel.evolution_config import PipelineConfigClass, PipelineConfigSnapshot, derive_config_delta
from garden_kernel.evolution_constitution import GovernanceTier, classify_config_delta
from garden_kernel.evolution_gate import EvolutionGateContext, GateDecision, evaluate_evolution_action


class ConstitutionalTierTests(unittest.TestCase):
    def delta(self, config_class):
        before = PipelineConfigSnapshot(
            config_id="policy",
            config_class=config_class,
            design_epoch="v15.5",
            values={"mode": "A"},
            source_obligation_refs=("Garden_System:ActionGate",),
        )
        after = PipelineConfigSnapshot(
            config_id="policy",
            config_class=config_class,
            design_epoch="v15.5",
            values={"mode": "B"},
            source_obligation_refs=("Garden_System:ActionGate",),
        )
        return derive_config_delta(
            delta_id=f"D-{config_class.value}", before=before, after=after,
            provenance_refs=("review:1",),
        )

    def test_gate_authority_and_epoch_policy_are_constitutional(self):
        for cls in (
            PipelineConfigClass.ACTION_GATE_POLICY,
            PipelineConfigClass.AUTHORITY_ENVELOPE_POLICY,
            PipelineConfigClass.DESIGN_EPOCH_POLICY,
        ):
            with self.subTest(config_class=cls.value):
                self.assertEqual(classify_config_delta(self.delta(cls)).tier, GovernanceTier.CONSTITUTIONAL)

    def test_integrator_prompt_is_ordinary(self):
        self.assertEqual(
            classify_config_delta(self.delta(PipelineConfigClass.INTEGRATOR_PROMPT)).tier,
            GovernanceTier.ORDINARY,
        )

    def test_constitutional_change_escalates_without_human_signoff(self):
        contract = CONTRACTS[EvolutionVerb.TRIAGE]
        action = EvolutionAction(
            action_id="A-CONST", verb=EvolutionVerb.TRIAGE,
            actor_ref="agent:integrator", subject_ref="config:policy",
            input_refs=("D1",), provenance_refs=("review:1",),
            satisfied_preconditions=contract.preconditions,
            claimed_postconditions=contract.postconditions,
        )
        env = make_role_envelope(
            subject="agent:integrator", role=EvolutionAgentRole.INTEGRATOR,
            granted_by="human:root", resources={"config:policy"},
        )
        no_human = EvolutionGateContext(
            current_design_epoch="v15.5", current_dependencies={},
            authority_envelopes=(env,), governance_tier=GovernanceTier.CONSTITUTIONAL,
        )
        with_human = EvolutionGateContext(
            current_design_epoch="v15.5", current_dependencies={},
            authority_envelopes=(env,), governance_tier=GovernanceTier.CONSTITUTIONAL,
            human_signoff=True,
        )
        self.assertEqual(evaluate_evolution_action(action, no_human).decision, GateDecision.ESCALATE)
        self.assertEqual(evaluate_evolution_action(action, with_human).decision, GateDecision.ALLOW)


if __name__ == "__main__":
    unittest.main()
