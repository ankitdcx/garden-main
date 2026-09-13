import unittest

from garden_kernel.core import SemanticError
from garden_kernel.evolution_config import (
    PipelineConfigClass,
    PipelineConfigSnapshot,
    derive_config_delta,
)


class PipelineConfigDeltaTests(unittest.TestCase):
    def snapshot(self, values, *, epoch="v15.5", config_id="integrator", config_class=PipelineConfigClass.INTEGRATOR_PROMPT):
        return PipelineConfigSnapshot(
            config_id=config_id,
            config_class=config_class,
            design_epoch=epoch,
            values=values,
            source_obligation_refs=("Garden_System:ActionGate",),
        )

    def test_change_becomes_delta_with_exact_changed_fields(self):
        before = self.snapshot({"prompt": "A", "cadence": "hourly"})
        after = self.snapshot({"prompt": "B", "cadence": "hourly"})
        delta = derive_config_delta(
            delta_id="CFG-D1", before=before, after=after,
            provenance_refs=("change:reviewed",),
        )
        self.assertEqual(delta.changed_fields, ("prompt",))
        self.assertNotEqual(delta.before_hash, delta.after_hash)
        self.assertEqual(delta.as_epoch_binding().design_epoch, "v15.5")

    def test_noop_delta_fails(self):
        before = self.snapshot({"prompt": "A"})
        with self.assertRaises(SemanticError):
            derive_config_delta(
                delta_id="CFG-NOOP", before=before, after=before,
                provenance_refs=("change:reviewed",),
            )

    def test_cross_epoch_change_requires_rederivation(self):
        before = self.snapshot({"prompt": "A"}, epoch="v15.5")
        after = self.snapshot({"prompt": "B"}, epoch="v15.6")
        with self.assertRaises(SemanticError):
            derive_config_delta(
                delta_id="CFG-XEPOCH", before=before, after=after,
                provenance_refs=("change:reviewed",),
            )

    def test_config_cannot_silently_rebind_source_obligation(self):
        before = self.snapshot({"prompt": "A"})
        after = PipelineConfigSnapshot(
            config_id="integrator",
            config_class=PipelineConfigClass.INTEGRATOR_PROMPT,
            design_epoch="v15.5",
            values={"prompt": "B"},
            source_obligation_refs=("Other:Obligation",),
        )
        with self.assertRaises(SemanticError):
            derive_config_delta(
                delta_id="CFG-REBIND", before=before, after=after,
                provenance_refs=("change:reviewed",),
            )

    def test_snapshot_requires_source_obligation(self):
        with self.assertRaises(SemanticError):
            PipelineConfigSnapshot(
                config_id="roles",
                config_class=PipelineConfigClass.REVIEWER_ROLE,
                design_epoch="v15.5",
                values={"role": "critic"},
                source_obligation_refs=(),
            )


if __name__ == "__main__":
    unittest.main()
