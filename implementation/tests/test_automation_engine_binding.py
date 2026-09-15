from __future__ import annotations

import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[2]


class AutomationEngineBindingTests(unittest.TestCase):
    def setUp(self) -> None:
        self.binding = json.loads((ROOT / "governance/AUTOMATION_ENGINE_BINDING_v1.json").read_text(encoding="utf-8"))
        self.schedule = json.loads((ROOT / "governance/PROCESS_EXECUTION_SCHEDULE_v1.json").read_text(encoding="utf-8"))
        self.profile = json.loads((ROOT / "governance/PROCESS_ENGINE_IMPLEMENTATION_v1.json").read_text(encoding="utf-8"))

    def test_binding_points_to_current_engine_and_process(self):
        self.assertEqual(self.binding["engine_id"], "GardenProcessEngine@1")
        self.assertEqual(self.binding["governing_process"], "GardenCanonicalUpdateProcess@1.4")
        self.assertEqual(self.schedule["engine_id"], "GardenProcessEngine@1")
        self.assertEqual(self.profile["automation_binding_manifest"], "governance/AUTOMATION_ENGINE_BINDING_v1.json")

    def test_every_scheduled_garden_lane_has_exactly_one_binding(self):
        scheduled = []
        for section in ("hourly_cycle", "daily", "periodic"):
            for item in self.schedule[section]:
                if item["mode"] != "EXTERNAL_RESEARCH_DELIVERY":
                    scheduled.append(item["lane"])
        bound = [item["lane"] for item in self.binding["bindings"]]
        self.assertEqual(len(bound), len(set(bound)))
        self.assertEqual(set(scheduled), set(bound))

    def test_automation_ids_are_unique(self):
        ids = [item["automation_id"] for item in self.binding["bindings"]]
        self.assertEqual(len(ids), len(set(ids)))

    def test_pre_process_discovery_cannot_mutate_engine_state(self):
        scouts = [item for item in self.binding["bindings"] if item["mode"] == "PRE_PROCESS_DISCOVERY"]
        self.assertTrue(scouts)
        self.assertTrue(all(item.get("engine_state_mutation") is False for item in scouts))

    def test_non_garden_research_is_explicitly_outside_process_state(self):
        names = {item["lane"] for item in self.binding["non_garden_scheduled_tasks"]}
        self.assertIn("AI Architecture Brief", names)

    def test_fail_closed_codes_cover_engine_drift(self):
        required = {"MISSING_ENGINE_BINDING", "LOCAL_ROUTE_OVERRIDE", "ILLEGAL_PROCESS_TRANSITION", "MISSING_ENGINE_RECEIPT", "STALE_CYCLE_BINDING", "ALGEBRA_TRANSITION_INVALID", "AUTHORITY_CLAIM_FROM_ALGEBRA"}
        self.assertTrue(required <= set(self.binding["fail_closed"]))


if __name__ == "__main__":
    unittest.main()
