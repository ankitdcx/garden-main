from copy import deepcopy
from dataclasses import replace
import unittest

from garden_kernel.core import SemanticError
from garden_kernel.process_engine import CycleBinding, ProcessFactory, ProcessRoute, ProcessState
from test_process_engine import PROFILE, REFS, binding


class ProcessRestoreTests(unittest.TestCase):
    def setUp(self):
        self.binding = binding()
        process = ProcessFactory.create(ProcessRoute.NON_SEMANTIC_REPAIR, binding=self.binding, work_id='repair')
        self.route = process.route_receipt()
        self.receipts = []
        for target in (ProcessState.ROUTED, ProcessState.IMPLEMENTED, ProcessState.VERIFIED, ProcessState.CLOSED):
            self.receipts.append(process.advance(target, satisfied_gates=sorted(process.required_gates(target)), algebra_profile=PROFILE, source_obligation_refs=REFS))

    def restore(self, receipts=None, route=None, observed=None):
        return ProcessFactory.restore(self.route if route is None else route, self.receipts if receipts is None else receipts,
                                      binding=observed or self.binding, work_id='repair', algebra_profile=PROFILE)

    def test_roundtrip_each_prefix_and_resume_next_action(self):
        states = [ProcessState.CREATED, ProcessState.ROUTED, ProcessState.IMPLEMENTED, ProcessState.VERIFIED, ProcessState.CLOSED]
        for count, state in enumerate(states):
            restored = self.restore(self.receipts[:count])
            self.assertEqual(restored.state, state)
            if count < len(self.receipts):
                target = states[count + 1]
                emitted = restored.advance(target, satisfied_gates=sorted(restored.required_gates(target)), algebra_profile=PROFILE, source_obligation_refs=REFS)
                self.assertEqual(emitted, self.receipts[count])

    def test_missing_duplicate_and_reordered_receipts_are_rejected(self):
        for rows in (self.receipts[1:], self.receipts[:1] + self.receipts, list(reversed(self.receipts)), self.receipts[:1] + self.receipts[2:]):
            with self.assertRaises(SemanticError): self.restore(rows)

    def test_cross_cycle_and_tampered_evidence_are_rejected(self):
        edits = {'cycle_id': 'another-cycle', 'work_id': 'other-work', 'route': 'PATCH_DELTA',
                 'repo_heads': {'garden-main': 'c' * 40}, 'required_gates': [],
                 'satisfied_gates': [], 'process_operator': 'COMPOSE', 'algebra_validation': {},
                 'authorization_result': 'AUTHORIZED', 'from_state': 'VERIFIED', 'schema': 'invented'}
        for field, value in edits.items():
            with self.subTest(field=field):
                rows = deepcopy(self.receipts); rows[0][field] = value
                with self.assertRaises(SemanticError): self.restore(rows)

    def test_moved_observed_head_and_wrong_route_receipt_are_rejected(self):
        with self.assertRaises(SemanticError):
            self.restore(observed=replace(self.binding, repo_heads={'garden-main': 'c' * 40}))
        route = deepcopy(self.route); route['work_id'] = 'other-work'
        with self.assertRaises(SemanticError): self.restore(route=route)

    def test_invalid_bindings_do_not_silently_drop_a_repository(self):
        for changes in ({'cycle_id': None}, {'source_root_sha256': 'not-a-digest'},
                        {'repo_heads': {'garden-main': 'a' * 40, 'garden-swarm': ''}},
                        {'repo_heads': {'garden-main': None}}, {'repo_heads': {' garden-main': 'a' * 40}}):
            with self.subTest(changes=changes), self.assertRaises(SemanticError): replace(self.binding, **changes)
