import unittest

from garden_kernel.core import SemanticError
from garden_kernel.evolution_actions import EvolutionVerb
from garden_kernel.evolution_authority import (
    EvolutionAgentRole,
    EvolutionAuthorityEnvelope,
    can_execute,
    delegate_within_envelope,
    make_role_envelope,
)


class EvolutionAuthorityTests(unittest.TestCase):
    def test_role_profiles_are_narrow(self):
        reviewer = make_role_envelope(
            subject="agent:r1", role=EvolutionAgentRole.REVIEWER,
            granted_by="human:root", resources={"mechanism:A"},
        )
        self.assertTrue(can_execute((reviewer,), verb=EvolutionVerb.PROPOSE, resource="mechanism:A"))
        self.assertFalse(can_execute((reviewer,), verb=EvolutionVerb.TRIAGE, resource="mechanism:A"))

    def test_agent_cannot_self_mint(self):
        with self.assertRaises(SemanticError):
            EvolutionAuthorityEnvelope(
                subject="agent:self", role=EvolutionAgentRole.REVIEWER,
                granted_by="agent:self", actions=frozenset({EvolutionVerb.PROPOSE}),
                resources=frozenset({"mechanism:A"}), max_delegation_depth=0,
            )

    def test_agent_cannot_hold_canonical_promotion_authority(self):
        with self.assertRaises(SemanticError):
            EvolutionAuthorityEnvelope(
                subject="agent:m", role=EvolutionAgentRole.MATERIALIZER,
                granted_by="human:root", actions=frozenset({EvolutionVerb.MATERIALIZE}),
                resources=frozenset({"successor:v15.6"}), max_delegation_depth=0,
                can_promote_canon=True,
            )

    def test_delegation_cannot_expand_actions(self):
        parent = make_role_envelope(
            subject="agent:r1", role=EvolutionAgentRole.REVIEWER,
            granted_by="human:root", resources={"mechanism:A"}, max_delegation_depth=1,
        )
        with self.assertRaises(SemanticError):
            delegate_within_envelope(
                parent, child_subject="agent:r2",
                requested_actions=frozenset({EvolutionVerb.PROPOSE, EvolutionVerb.TRIAGE}),
                requested_resources=frozenset({"mechanism:A"}),
            )

    def test_delegation_cannot_expand_resources(self):
        parent = make_role_envelope(
            subject="agent:r1", role=EvolutionAgentRole.REVIEWER,
            granted_by="human:root", resources={"mechanism:A"}, max_delegation_depth=1,
        )
        with self.assertRaises(SemanticError):
            delegate_within_envelope(
                parent, child_subject="agent:r2",
                requested_actions=frozenset({EvolutionVerb.PROPOSE}),
                requested_resources=frozenset({"mechanism:A", "mechanism:B"}),
            )

    def test_valid_delegation_strictly_narrows_depth(self):
        parent = make_role_envelope(
            subject="agent:r1", role=EvolutionAgentRole.REVIEWER,
            granted_by="human:root", resources={"mechanism:A", "mechanism:B"}, max_delegation_depth=1,
        )
        child = delegate_within_envelope(
            parent, child_subject="agent:r2",
            requested_actions=frozenset({EvolutionVerb.PROPOSE}),
            requested_resources=frozenset({"mechanism:A"}),
        )
        self.assertEqual(child.max_delegation_depth, 0)
        self.assertEqual(child.granted_by, "agent:r1")


if __name__ == "__main__":
    unittest.main()
