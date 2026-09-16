#!/usr/bin/env python3
"""Run bounded reference scenarios and write an honest qualification receipt."""
from __future__ import annotations
import hashlib, json, platform, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'implementation'))
from garden_kernel.physical_assurance import STPA_UNSAFE_CONTROL_ACTIONS, TankSimulation


def file_hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    scenarios = {
        'bounded_lower_handoff': TankSimulation(initial_level=0.55, primary_command=-1.0, disturbance=-0.1, sensor_error=0.05).run(1.0),
        'handoff_delay_counterexample': TankSimulation(initial_level=0.8, primary_command=-1.0, disturbance=-0.1, sensor_error=0.05, handoff_delay=0.6).run(1.1),
        'outside_recoverable_minimum_risk': TankSimulation(initial_level=0.2, primary_command=-1.0, disturbance=-0.1, sensor_error=0.05).run(0.2),
        'controller_timeout_minimum_risk': TankSimulation(initial_level=5.0, primary_command=0.0, disturbance=0.0, controller_timeout=True).run(0.2),
        'failed_handoff_minimum_risk': TankSimulation(initial_level=0.55, primary_command=-1.0, disturbance=-0.1, sensor_error=0.05, force_handoff_failure=True).run(0.5),
    }
    out = ROOT / 'reviews/v15.7/qualification/physical'
    out.mkdir(parents=True, exist_ok=True)
    receipt = {
        'schema': 'GardenPhysicalAssuranceReceipt/v1', 'kind': 'BOUNDED_REFERENCE_SIMULATION_NOT_HARDWARE',
        'status': 'BOUNDED_SCENARIOS_EXECUTED_NOT_CERTIFIED', 'source_delta_refs': ['V156-EH-18', 'V156-EH-19'],
        'implementation_sha256': file_hash(ROOT / 'implementation/garden_kernel/physical_assurance.py'),
        'runner_sha256': file_hash(Path(__file__)), 'python': platform.python_version(), 'platform': platform.platform(),
        'stpa_unsafe_control_actions': STPA_UNSAFE_CONTROL_ACTIONS, 'scenarios': scenarios,
        'summary': {'bounded_handoff_envelope_held': scenarios['bounded_lower_handoff']['safety_result']['envelope_held_at_sampled_points'], 'counterexample_records_loss': bool(scenarios['handoff_delay_counterexample']['safety_result']['assurance_loss']), 'outside_region_records_loss': bool(scenarios['outside_recoverable_minimum_risk']['safety_result']['assurance_loss']), 'controller_timeout_records_loss': 'CONTROLLER_TIMEOUT' in scenarios['controller_timeout_minimum_risk']['safety_result']['assurance_loss'], 'failed_handoff_records_loss': 'HANDOFF_FAILED' in scenarios['failed_handoff_minimum_risk']['safety_result']['assurance_loss']},
        'limitations': ['No hardware actuation', 'No claim of fallback independence or certification', 'Only declared finite scenarios and Euler samples were checked', 'This receipt does not discharge required continuous-time proof, STPA completeness, or production qualification.']
    }
    (out / 'physical-assurance-receipt.json').write_text(json.dumps(receipt, indent=2) + '\n')
    (out / 'README.md').write_text('# Bounded physical assurance qualification\n\nThis directory contains deterministic reference-simulation evidence only. It is not a physical safety case, hardware test, independence claim, or certification. The receipt retains trajectories, assumptions, scenario outcomes, and explicit counterexamples.\n')
    print(json.dumps({'receipt': str(out / 'physical-assurance-receipt.json'), 'status': receipt['status']}, indent=2))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
