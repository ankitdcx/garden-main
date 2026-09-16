import math
import unittest

from garden_kernel.physical_assurance import (TankAssumptions, TankSimulation, STPA_UNSAFE_CONTROL_ACTIONS,
    is_recoverable, signed_transfer, transfer_is_authenticated, shared_actuator_decision, takeover_recoverable_region)


class PhysicalAssuranceTests(unittest.TestCase):
    def test_derived_margin_and_region(self):
        a = TankAssumptions()
        self.assertAlmostEqual(a.intervention_margin, 0.49)
        lo, hi = takeover_recoverable_region(0.4, 0.05, a)
        self.assertAlmostEqual(lo, 0.49)
        self.assertAlmostEqual(hi, 9.51)
        self.assertTrue(is_recoverable(0.49, 0.4, 0.05, a))
        self.assertFalse(is_recoverable(0.48, 0.4, 0.05, a))

    def test_custom_envelope_uses_safe_low_and_midpoint(self):
        a = TankAssumptions(safe_low=100.0, safe_high=120.0)
        self.assertAlmostEqual(a.lower_switch_threshold, 100.49)
        self.assertAlmostEqual(a.upper_switch_threshold, 119.51)
        r = TankSimulation(initial_level=100.55, primary_command=-1.0, disturbance=-0.1, sensor_error=0.05, assumptions=a).run(1.0)
        self.assertTrue(r['safety_result']['envelope_held_at_sampled_points'])
        self.assertEqual(r['trajectory'][-1]['controller'], 'fallback')

    def test_invalid_numbers_and_assumptions_rejected(self):
        with self.assertRaises(ValueError): TankAssumptions(safe_low=1, safe_high=1)
        with self.assertRaises(ValueError): TankAssumptions(dt=math.nan)
        with self.assertRaises(ValueError): TankAssumptions(dt=1.0, monitor_period=0.1)
        with self.assertRaises(ValueError): TankAssumptions(dt=0.06, monitor_period=0.1)
        with self.assertRaises(ValueError): TankSimulation(initial_level=math.nan, primary_command=0, disturbance=0)
        with self.assertRaises(ValueError): TankSimulation(initial_level=1, primary_command=0, disturbance=0).run(math.inf)
        with self.assertRaises(ValueError): TankSimulation(initial_level=1, primary_command=0, disturbance=0).run(61)

    def test_nominal_bounded_handoff_fences_stale_primary(self):
        r = TankSimulation(initial_level=0.55, primary_command=-1.0, disturbance=-0.1, sensor_error=0.05).run(1.0)
        self.assertTrue(r['safety_result']['envelope_held_at_sampled_points'])
        self.assertGreater(r['safety_result']['rejected_stale_commands'], 0)
        self.assertEqual(r['safety_result']['assurance_loss'], [])

    def test_late_handoff_records_assurance_loss(self):
        r = TankSimulation(initial_level=0.8, primary_command=-1.0, disturbance=-0.1, sensor_error=0.05, handoff_delay=0.6).run(1.1)
        self.assertIn('LATE_HANDOFF', r['safety_result']['assurance_loss'])
        self.assertIn('SAFE_ENVELOPE_VIOLATED', r['safety_result']['assurance_loss'])

    def test_outside_recoverable_region_records_minimum_risk(self):
        r = TankSimulation(initial_level=0.2, primary_command=-1.0, disturbance=-0.1, sensor_error=0.05).run(0.2)
        self.assertIn('OUTSIDE_RECOVERABLE_REGION', r['safety_result']['assurance_loss'])
        self.assertEqual(r['trajectory'][0]['controller'], 'fallback')

    def test_bad_transfer_is_rejected(self):
        a = TankAssumptions(); t = signed_transfer('primary', 0, 1.0, 0.0, a)
        self.assertTrue(transfer_is_authenticated(t, a))
        self.assertFalse(transfer_is_authenticated(t.__class__(t.controller, t.epoch, 2.0, t.observed_at, t.mac), a))
        self.assertFalse(transfer_is_authenticated(t.__class__(t.controller, t.epoch, math.nan, t.observed_at, t.mac), a))

    def test_stale_primary_command_is_fenced_after_handoff(self):
        s = TankSimulation(initial_level=0.55, primary_command=-1.0, disturbance=-0.1, sensor_error=0.05)
        s.run(0.6)
        self.assertFalse(s.actuator_command('primary', 0, -1.0))

    def test_primary_return_requires_revalidation_and_fresh_authority(self):
        s = TankSimulation(initial_level=0.2, primary_command=-1.0, disturbance=-0.1); s.run(0.1)
        self.assertFalse(s.request_primary_return(revalidated=True, fresh_authorization=False, dwell_s=0.2))
        self.assertFalse(s.request_primary_return(revalidated=True, fresh_authorization=True, dwell_s=1.0))
        s.run(0.2)
        self.assertTrue(s.request_primary_return(revalidated=True, fresh_authorization=True, dwell_s=0.2))

    def test_primary_return_rejects_nan_and_unrecoverable_state(self):
        s = TankSimulation(initial_level=0.2, primary_command=-1.0, disturbance=-0.1); s.run(0.1)
        with self.assertRaises(ValueError): s.request_primary_return(revalidated=True, fresh_authorization=True, dwell_s=math.nan)
        s.h = -0.1
        self.assertFalse(s.request_primary_return(revalidated=True, fresh_authorization=True, dwell_s=1.0))

    def test_sensor_age_controller_timeout_and_failed_handoff_use_minimum_risk(self):
        stale = TankSimulation(initial_level=5, primary_command=0, disturbance=0, sensor_age=0.11).run(0.1)
        timeout = TankSimulation(initial_level=5, primary_command=0, disturbance=0, controller_timeout=True).run(0.1)
        failed = TankSimulation(initial_level=0.55, primary_command=-1, disturbance=-0.1, sensor_error=0.05, force_handoff_failure=True).run(0.5)
        self.assertIn('SENSOR_AGE_EXCEEDS_BOUND', stale['safety_result']['assurance_loss'])
        self.assertIn('CONTROLLER_TIMEOUT', timeout['safety_result']['assurance_loss'])
        self.assertIn('HANDOFF_FAILED', failed['safety_result']['assurance_loss'])

    def test_horizon_is_recorded_and_second_run_does_not_replay_handoff(self):
        s = TankSimulation(initial_level=0.55, primary_command=-1, disturbance=-0.1, sensor_error=0.05)
        first = s.run(0.5); completed = sum(e['event'] == 'handoff_completed' for e in first['events'])
        second = s.run(0.2)
        self.assertEqual(second['safety_result']['recorded_horizon_end_s'], 0.7)
        self.assertEqual(sum(e['event'] == 'handoff_completed' for e in second['events']), completed)

    def test_two_agent_shared_actuator_hazard_is_blocked(self):
        result = shared_actuator_decision(('agent-a', 7, 0.2), ('agent-b', 7, -0.2), trusted_coordination=True)
        self.assertFalse(result['accepted'])
        self.assertEqual(result['reason'], 'CONFLICTING_SHARED_ACTUATOR_COMMANDS')
        self.assertFalse(shared_actuator_decision(('agent-a', 7, 0.2), ('agent-b', 7, 0.2))['accepted'])
        self.assertFalse(shared_actuator_decision(('agent-a', 7, math.nan), ('agent-b', 7, 0.2), trusted_coordination=True)['accepted'])
        self.assertFalse(shared_actuator_decision(('agent-a', 7, 1.1), ('agent-b', 7, 1.1), trusted_coordination=True)['accepted'])
        self.assertTrue(shared_actuator_decision(('agent-a', 7, 0.2), ('agent-b', 7, 0.2), trusted_coordination=True)['accepted'])
        self.assertIn('UCA-7-two-agent-shared-actuator', STPA_UNSAFE_CONTROL_ACTIONS)


if __name__ == '__main__':
    unittest.main()
