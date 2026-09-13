import unittest

from garden_kernel.evolution_gate import GateDecision


class GateSmokeTest(unittest.TestCase):
    def test_gate_decisions_are_closed(self):
        self.assertEqual({x.value for x in GateDecision}, {"ALLOW", "REJECT", "ESCALATE"})


if __name__ == "__main__":
    unittest.main()
