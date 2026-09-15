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

    def test_exactly_one_active_garden_scheduler(self):
        self.assertEqual(self.binding["scheduling_topology"], "SINGLE_SERIAL_COORDINATOR")
        self.assertEqual(self.binding["active_driver_count"], 1)
        self.assertEqual(len(self.binding["active_bindings"]), 1)
        driver = self.binding["active_bindings"][0]
        self.assertEqual(driver["lane"], "Garden Coordinator")
        self.assertEqual(self.schedule["active_driver"]["lane"], "Garden Coordinator")
        self.assertEqual(driver["max_material_work_units_per_run"], 1)
        self.assertEqual(driver["max_external_provider_calls_in_parallel"], 1)

    def test_absorbed_workers_are_not_active_schedulers(self):
        active = {item["lane"] for item in self.binding["active_bindings"]}
        absorbed = {item["lane"] for item in self.binding["absorbed_disabled_workers"]}
        self.assertFalse(active & absorbed)
        self.assertIn("Garden ChatGPT Reviewer", absorbed)
        self.assertIn("Garden Pipeline Health", absorbed)
        self.assertIn("Garden Maintenance", absorbed)

    def test_weekly_brief_is_disabled_not_scheduled(self):
        disabled = {item["lane"]: item["status"] for item in self.binding["disabled_non_garden_scheduled_tasks"]}
        self.assertEqual(disabled.get("AI Architecture Brief"), "DISABLED_BY_HUMAN_REQUEST")
        self.assertEqual(self.schedule["disabled_schedules"]["AI Architecture Brief"], "DISABLED_BY_HUMAN_REQUEST")

    def test_serialization_and_transient_failure_are_fail_closed(self):
        policy = self.binding["serialization_policy"]
        self.assertTrue(policy["one_material_work_unit_per_run"])
        self.assertFalse(policy["parallel_garden_stages"])
        self.assertFalse(policy["parallel_external_provider_calls"])
        self.assertIn("NO_STATE_ADVANCE", policy["transient_rate_limit"])
        required = {"MULTIPLE_ACTIVE_GARDEN_SCHEDULERS", "TRANSIENT_FAILURE_STATE_ADVANCE", "ALGEBRA_TRANSITION_INVALID"}
        self.assertTrue(required <= set(self.binding["fail_closed"]))

    def test_schedule_has_no_parallel_lane_arrays(self):
        self.assertNotIn("hourly_cycle", self.schedule)
        self.assertNotIn("daily", self.schedule)
        self.assertNotIn("periodic", self.schedule)
        self.assertEqual(self.schedule["active_driver"]["max_material_work_units_per_run"], 1)
        self.assertEqual(self.schedule["active_driver"]["max_external_provider_calls_in_parallel"], 1)


if __name__ == "__main__":
    unittest.main()
