import json
from pathlib import Path
import tempfile
import unittest
from concurrent.futures import ThreadPoolExecutor

from garden_kernel.core import SemanticError
from garden_kernel.completion_runner import CompletionStore, CompletionWorker, Limits, digest
from garden_kernel.process_engine import CycleBinding, ProcessState
from garden_kernel.review_packet import packet, ReviewSet
from garden_kernel.process_engine import ProcessFactory
from garden_kernel.algebra_bound_update import validate_algebra_bound_update

ROOT = Path(__file__).resolve().parents[2]
PROFILE = json.loads((ROOT / 'gsl/EVOLUTION_ALGEBRA_PROFILE.json').read_text())
BINDING = CycleBinding('cycle', '1.4', 'v15.5', PROFILE['canonical_source_root_sha256'], {'garden-main': 'a'*40})


class CompletionTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.path = str(Path(self.tmp.name) / 'state.sqlite')
        self.store = CompletionStore(self.path)
        self.store.create_cycle(BINDING, 'work', 'NON_SEMANTIC_REPAIR', PROFILE)
        self.store.configure(paused=False, pool_remaining={'routine': 1_500_000}, reconciliation_ref='test:balance')
        self.bindings = {'cycle': BINDING}

    def tearDown(self):
        self.store.close()
        self.tmp.cleanup()

    def add(self, name, **kwargs):
        self.store.enqueue(name, 'cycle', handler='test', **kwargs)

    def claim(self, now=10000):
        return self.store.claim(now, self.bindings, PROFILE)

    def done(self, claim, now=10000, cost=0):
        return self.store.finish(claim, now=now, status='SUCCEEDED', result={'evidence': 'test'}, actual_micro_usd=cost)

    def test_completion_drives_dependencies_without_clock_tick(self):
        self.add('a'); self.add('b', dependencies=['a']); self.add('c', dependencies=['b'])
        worker = CompletionWorker(self.store, {'test': lambda _: {'status':'SUCCEEDED', 'result':{'ok':True}}}, lambda:10000)
        self.assertEqual([x['task_id'] for x in worker.run_ready(lambda:self.bindings, PROFILE)], ['a','b','c'])
        self.assertEqual(worker.run_ready(lambda:self.bindings, PROFILE), [])

    def test_two_connections_cannot_both_claim(self):
        self.add('a', external=True); self.add('b', external=True)
        def claim(_):
            store = CompletionStore(self.path)
            try:
                return store.claim(10000, self.bindings, PROFILE)
            finally:
                store.close()
        with ThreadPoolExecutor(2) as pool:
            results = list(pool.map(claim, range(2)))
        self.assertEqual(sum(r is not None for r in results), 1)

    def test_crash_blocks_retries_and_late_completion(self):
        self.add('a', external=True); self.add('b')
        first = self.claim()
        self.assertIsNone(self.claim(10301))
        with self.assertRaises(SemanticError):
            self.done(first, 10301)
        self.assertIsNone(self.claim(20000))
        self.store.reconcile('a', resolution='NOT_EXECUTED', actual_micro_usd=0, evidence_ref='provider:non-execution')
        second = self.claim(20000)
        self.assertNotEqual(first['token'], second['token'])

    def test_cooldown_survives_restart_and_is_not_success(self):
        self.add('a', external=True); self.add('b', dependencies=['a'])
        first = self.claim()
        self.store.finish(first, now=10000, status='RATE_LIMITED', actual_micro_usd=0, result={'http':429}, retry_after_seconds=120)
        self.store.close(); self.store = CompletionStore(self.path)
        self.assertIsNone(self.claim(10119))
        self.assertEqual(self.claim(10120)['task_id'], 'a')

    def test_retry_bound(self):
        self.add('a')
        for now in (10000, 10100, 10300):
            claim = self.claim(now)
            state = self.store.finish(claim, now=now, status='RATE_LIMITED', result={})
        self.assertEqual(state, 'FAILED')
        self.assertIsNone(self.claim(20000))

    def test_global_daily_and_lifetime_pools(self):
        for n in 'abc':
            self.add(n, external=True, max_cost_micro_usd=600000)
        self.done(self.claim(), cost=600000)
        self.assertIsNone(self.claim())
        self.done(self.claim(100000), now=100000, cost=600000)
        self.assertIsNone(self.claim(200000))

    def test_shared_free_quota_and_pause(self):
        for n in 'abc':
            self.add(n, external=True)
        self.done(self.claim()); self.done(self.claim())
        self.assertIsNone(self.claim())
        self.store.configure(paused=True)
        self.assertIsNone(self.claim(14000))
        self.store.configure(paused=False)
        self.assertIsNotNone(self.claim(14000))

    def test_missing_charge_is_unknown_not_free_success(self):
        self.add('a', external=True, max_cost_micro_usd=10)
        first = self.claim()
        self.assertEqual(self.store.finish(first, now=10000, status='SUCCEEDED', result={}), 'UNKNOWN')
        self.add('b')
        self.assertIsNone(self.claim())

    def test_unknown_pool_and_balance_reset_blocked(self):
        self.add('a', external=True, pool='escalation', max_cost_micro_usd=1)
        self.assertIsNone(self.claim())
        self.add('b', external=True)
        self.done(self.claim())
        with self.assertRaises(SemanticError):
            self.store.configure(paused=False, pool_remaining={'routine':99999999}, reconciliation_ref='reset')

    def test_idempotency_and_dependencies(self):
        self.add('a'); self.add('a')
        with self.assertRaises(SemanticError): self.add('a', external=True)
        with self.assertRaises(SemanticError): self.add('b', dependencies=['missing'])
        with self.assertRaises(SemanticError): self.add('b', dependencies=['b'])

    def test_stale_binding_and_time_block(self):
        self.add('a')
        changed = CycleBinding('cycle','1.4','v15.5', BINDING.source_root_sha256, {'garden-main':'b'*40})
        with self.assertRaises(SemanticError): self.store.claim(10000, {'cycle':changed}, PROFILE)
        self.done(self.claim())
        with self.assertRaises(SemanticError): self.claim(9999)

    def test_chain_and_external_checkpoint(self):
        head = self.store.verify_chain()
        self.assertEqual(head, self.store.verify_chain(head))
        with self.assertRaises(SemanticError): self.store.verify_chain('a'*64)
        self.store.db.execute("UPDATE events SET record='{}' WHERE seq=1")
        with self.assertRaises(SemanticError): self.store.verify_chain()

    def test_transactional_gates_and_restore(self):
        with self.assertRaises(SemanticError):
            self.store.advance('cycle',BINDING,PROFILE,ProcessState.ROUTED,{},lambda *_:True,['source'])
        ev={'ROUTE_CLASSIFIED':{},'SEMANTIC_TOUCH_FALSE':{}}
        with self.assertRaises(SemanticError):
            self.store.advance('cycle',BINDING,PROFILE,ProcessState.ROUTED,ev,lambda *_:False,['source'])
        self.store.advance('cycle',BINDING,PROFILE,ProcessState.ROUTED,ev,lambda *_:True,['source'])
        self.store.close(); self.store=CompletionStore(self.path)
        self.assertEqual(self.store.restore('cycle',BINDING,PROFILE)[1].state,ProcessState.ROUTED)

    def test_handler_exception_halts_chain(self):
        self.add('a'); self.add('b')
        def fail(_): raise ConnectionError('secret must not appear in receipt')
        worker=CompletionWorker(self.store,{'test':fail},lambda:10000)
        self.assertEqual(worker.run_ready(lambda:self.bindings,PROFILE),[])
        self.assertIsNone(self.claim())
        self.assertNotIn('secret',str(list(self.store.db.execute('SELECT record FROM events'))))

    def test_different_worker_limits_rejected(self):
        with self.assertRaises(SemanticError): CompletionStore(self.path,Limits(free_hourly=3))


class ReviewTests(unittest.TestCase):
    def setUp(self):
        self.p=packet(BINDING,{'source':'content'},expected_objects={'source':digest('content')},exclusions={},closure_frontier=[])
        self.r=ReviewSet(self.p,['one','two'],builder_family='builder',min_families=2)

    def receipt(self,family,phase='BLIND'):
        return {'family':family,'packet_hash':self.p['packet_hash'],'cycle_id':'cycle','status':'COMPLETE',
                'findings':['explicit finding or no-change result'],'provider_response_ref':'provider:receipt','phase':phase,'peer_findings_seen':False,'blind_set_hash':digest(self.r.blind)}

    def test_missing_closure_and_wrong_content(self):
        with self.assertRaises(SemanticError): packet(BINDING,{},expected_objects={'source':digest('content')},exclusions={},closure_frontier=[])
        with self.assertRaises(SemanticError): packet(BINDING,{'source':'changed'},expected_objects={'source':digest('content')},exclusions={},closure_frontier=[])

    def test_blind_isolation_and_cross_join(self):
        with self.assertRaises(SemanticError): self.r.cross_input()
        self.r.record_blind('one',self.receipt('one'))
        self.assertNotIn('blind',self.r.blind_input('two'))
        with self.assertRaises(SemanticError): self.r.cross_input()
        with self.assertRaises(SemanticError): self.r.record_blind('one',self.receipt('one'))
        bad=self.receipt('two');bad['cycle_id']='other'
        with self.assertRaises(SemanticError): self.r.record_blind('two',bad)
        self.r.record_blind('two',self.receipt('two'))
        for f in ['one','two']: self.r.record_cross(f,self.receipt(f,'CROSS_EXAM'))
        evidence={'candidate_sha':'c'*40,'packet_hash':self.p['packet_hash']}
        with self.assertRaises(SemanticError): self.r.verified_closure(candidate_sha='c'*40,verifier_family='builder',evidence=evidence,verify=lambda _:True)
        with self.assertRaises(SemanticError): self.r.verified_closure(candidate_sha='d'*40,verifier_family='one',evidence=evidence,verify=lambda _:True)
        self.assertEqual(self.r.verified_closure(candidate_sha='c'*40,verifier_family='one',evidence=evidence,verify=lambda _:True)['status'],'VERIFIED_FIXED')


class AlgebraRepairTests(unittest.TestCase):
    def test_engine_rejects_coercion_whitespace_and_duplicate_gates(self):
        process=ProcessFactory.create('NON_SEMANTIC_REPAIR',binding=BINDING,work_id='work')
        for gates in ['ROUTE_CLASSIFIED', [123], [' ROUTE_CLASSIFIED'], ['ROUTE_CLASSIFIED']*2]:
            with self.assertRaises(SemanticError):
                process.advance(ProcessState.ROUTED,satisfied_gates=gates,algebra_profile=PROFILE,source_obligation_refs=['source'])
        for work_id in [False,123,' work ']:
            with self.assertRaises(SemanticError): ProcessFactory.create('NON_SEMANTIC_REPAIR',binding=BINDING,work_id=work_id)

    def test_ordered_trace_can_repeat_registered_operator(self):
        def load(p): return json.loads((ROOT/p).read_text())
        payload=load('reviews/evolution/algebra_bound/2026-09-15-garden-main-aab3950-bound-update.json')
        usage=load('reviews/evolution/algebra/2026-09-15-backfill-garden-main-aab3950-usage.json')
        validation=load('reviews/evolution/algebra/2026-09-15-backfill-garden-main-aab3950-validation.json')
        operator=payload['process_operator_trace'][0]
        payload['process_operator_trace']=[operator,operator]
        self.assertEqual(validate_algebra_bound_update(payload,usage,validation,PROFILE)['process_operator_trace'],[operator,operator])
        payload['process_operator_trace']=[123]
        with self.assertRaises(SemanticError): validate_algebra_bound_update(payload,usage,validation,PROFILE)
        payload['process_operator_trace']=[operator]
        payload['algebra_profile_blob_sha']='not-a-git-sha'
        with self.assertRaises(SemanticError): validate_algebra_bound_update(payload,usage,validation,PROFILE)


if __name__=='__main__': unittest.main()
