import unittest

from garden_kernel.core import SemanticError
from garden_kernel.evolution_epoch import EvolutionArtifactBinding, EvolutionArtifactKind


class DeltaSourceObligationTests(unittest.TestCase):
    def test_delta_without_source_obligation_is_rejected(self):
        with self.assertRaises(SemanticError):
            EvolutionArtifactBinding(
                artifact_id="D-NO-SOURCE",
                kind=EvolutionArtifactKind.DELTA,
                design_epoch="v15.5",
                dependencies={"canonical_root": "abc"},
                required_dependencies=frozenset({"canonical_root"}),
                derived_from_refs=("finding:F1",),
            )

    def test_delta_with_source_obligation_is_constructible(self):
        binding = EvolutionArtifactBinding(
            artifact_id="D-SOURCE",
            kind=EvolutionArtifactKind.DELTA,
            design_epoch="v15.5",
            dependencies={"canonical_root": "abc"},
            required_dependencies=frozenset({"canonical_root"}),
            derived_from_refs=("finding:F1",),
            source_obligation_refs=("Garden_System:ActionGate",),
        )
        self.assertEqual(binding.source_obligation_refs, ("Garden_System:ActionGate",))


if __name__ == "__main__":
    unittest.main()
