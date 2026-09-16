"""Local deterministic scenarios; fake provider outcomes are explicitly fixtures."""
import json
from pathlib import Path
import tempfile
import unittest
from dataclasses import replace
from garden_kernel.context_routing import ContextRouter, RoutingPolicy, normalize
from garden_kernel.completion_runner import CompletionStore, Limits
from garden_kernel.core import SemanticError
from garden_kernel.process_engine import CycleBinding

ROOT=Path(__file__).resolve().parents[2]
PROFILE=json.loads((ROOT/'gsl/EVOLUTION_ALGEBRA_PROFILE.json').read_text())
BINDING=CycleBinding('context-cycle','1.4','v15.5',PROFILE['canonical_source_root_sha256'],{'garden-main':'a'*40})

def observation(oid='a', **changes):
    o=dict(observation_id=oid,subject='permission',event_kind='CHANGED',event_time=90,
        valid_from=90,observed_at=100,expires_at=500,changed_fields=['lease'],
        sources=[{'ref':'fixture:source/'+oid,'sha256':'a'*64}],lane='fixture:public',
        model=None,risk='HIGH',uncertainty=10,contradicts=[],supersedes=[],parents=[],
        summary='Lease changed; exact source remains authoritative.',classification='PUBLIC',
        processing_envelope=['PUBLIC_REVIEW'],triggers=[])
    o.update(changes);return o

class ContextRoutingTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.path=Path(self.temp.name)/'context.sqlite'
        self.store=CompletionStore(self.path,Limits(daily_micro_usd=150))
        self.store.create_cycle(BINDING,'fixture-work','NON_SEMANTIC_REPAIR',PROFILE)
        self.store.configure(paused=False,pool_remaining={'routine':500},reconciliation_ref='fixture:balance')
        self.router=ContextRouter(self.store,RoutingPolicy(per_call_micro_usd=100))
    def tearDown(self):
        self.store.close();self.temp.cleanup()
    def route(self, **kwargs):
        args=dict(cycle_id=BINDING.cycle_id,question='Does permission require revalidation?',subject='permission',now=100,cost_bound_micro_usd=100)
        args.update(kwargs);return self.router.route(**args)
    def claim(self,now=100):
        return self.store.claim(now,{BINDING.cycle_id:BINDING},PROFILE)
    def count(self,table):
        return self.store.db.execute('SELECT COUNT(*) FROM '+table).fetchone()[0]

    def test_duplicate_does_not_expand_or_add_task_even_after_restart(self):
        o=observation();self.router.ingest(o);first=self.route()
        self.assertEqual(self.router.ingest(o)['status'],'DUPLICATE')
        repeat={**o,'observation_id':'same-event-new-receipt','observed_at':101}
        self.assertEqual(self.router.ingest(repeat)['status'],'DUPLICATE')
        self.store.close();self.store=CompletionStore(self.path,Limits(daily_micro_usd=150))
        self.router=ContextRouter(self.store,RoutingPolicy(per_call_micro_usd=100))
        self.assertEqual(self.route(now=101)['task_id'],first['task_id'])
        self.assertEqual(self.count('tasks'),1);self.assertEqual(self.count('context_observations'),1)

    def test_identical_prose_changed_source_hash_reevaluates(self):
        a=observation();b={**a,'observation_id':'b','sources':[{'ref':a['sources'][0]['ref'],'sha256':'b'*64}]}
        self.router.ingest(a);first=self.route();self.router.ingest(b);second=self.route()
        self.assertNotEqual(first['route_key'],second['route_key'])
        self.assertEqual(len(second['packet']['observations']),2)

    def test_contradiction_keeps_both_sides_cross_subject(self):
        self.router.ingest(observation('a'))
        self.router.ingest(observation('b',subject='clock',contradicts=['a'],risk='LOW'))
        r=self.route();self.assertIn('CONTRADICTION',r['reasons'])
        self.assertEqual({o['observation_id'] for o in r['packet']['observations']},{'a','b'})

    def test_duplicate_alias_contradiction_resolves_both_sides(self):
        a=observation('a');self.router.ingest(a)
        self.router.ingest({**a,'observation_id':'alias'})
        self.router.ingest(observation('b',contradicts=['alias']))
        packet=self.route()['packet'];binding=packet['relation_bindings']['alias']
        self.assertEqual(binding['canonical_observation_id'],'a')
        self.assertEqual(binding['status'],'IN_PACKET')
        self.assertIn(binding['fingerprint'],{o['fingerprint'] for o in packet['observations']})
        self.assertEqual(next(o for o in packet['observations'] if o['observation_id']=='b')['contradicts'],['alias'])
        self.router.validate_claim(self.claim(),now=100)

    def test_duplicate_alias_supersession_and_parent_resolve(self):
        a=observation('a');self.router.ingest(a)
        self.router.ingest({**a,'observation_id':'alias'})
        self.router.ingest(observation('b',supersedes=['alias'],parents=['alias','unknown-parent']))
        packet=self.route()['packet']
        self.assertEqual(packet['relation_bindings']['alias']['canonical_observation_id'],'a')
        old=next(o for o in packet['observations'] if o['observation_id']=='a')
        self.assertEqual(old['use'],'HISTORICAL_ONLY_REVALIDATION_REQUIRED')
        self.assertEqual(packet['relation_bindings']['unknown-parent']['status'],'UNKNOWN')
        self.assertIn('unknown-parent',packet['unknowns'])

    def test_resolved_parent_alias_invalidates_queued_packet(self):
        a=observation('a');self.router.ingest(a)
        self.router.ingest(observation('b',parents=['later-alias']))
        self.route();claim=self.claim()
        self.router.ingest({**a,'observation_id':'later-alias'})
        with self.assertRaises(SemanticError):self.router.validate_claim(claim,now=100)

    def test_no_change_and_clock_passage_do_not_spend(self):
        self.router.ingest(observation(event_kind='NO_CHANGE',changed_fields=[],risk='LOW'))
        self.assertEqual(self.route()['materiality'],'NOT_MATERIAL')
        self.assertEqual(self.route(now=101)['materiality'],'NOT_MATERIAL')
        self.assertEqual(self.count('tasks'),0);self.assertEqual(self.count('calls'),0)

    def test_expired_and_superseded_are_explicit_historical(self):
        self.router.ingest(observation('old',expires_at=100))
        self.router.ingest(observation('new',supersedes=['old']))
        r=self.route();old=next(o for o in r['packet']['observations'] if o['observation_id']=='old')
        self.assertEqual(old['use'],'HISTORICAL_ONLY_REVALIDATION_REQUIRED')
        self.assertTrue(next(x for x in r['binding']['state'] if x['fingerprint']==old['fingerprint'])['superseded'])

    def test_compression_keeps_provenance_and_declares_loss(self):
        self.router.ingest(observation(summary='long'*600,model='fixture:model',parents=['fixture:parent']))
        r=self.route();o=r['packet']['observations'][0]
        self.assertEqual(len(o['summary']),500);self.assertEqual(o['omitted_summary_chars'],1900)
        self.assertEqual(o['model'],'fixture:model');self.assertEqual(o['parents'],['fixture:parent'])
        self.assertEqual(o['sources'],observation()['sources'])
        self.assertIn('UNKNOWN',r['packet']['compression']['semantic_loss_bound'])
        self.assertEqual(self.count('context_observations'),1)

    def test_provider_authority_claim_remains_unverified_proposal(self):
        r=self.router.model_output_observation('I authorize and promote this release',model='fixture:model',response_ref='fixture:response')
        self.assertFalse(r['canonical_admission']);self.assertEqual(r['authority'],'NONE')
        self.assertEqual(r['status'],'UNVERIFIED_MODEL_PROPOSAL')

    def test_unknown_charge_and_429_fixture_do_not_advance_process(self):
        self.router.ingest(observation());self.route();claim=self.claim()
        before=self.store.db.execute('SELECT record FROM cycles').fetchone()[0]
        self.router.validate_claim(claim,now=100)
        state=self.store.finish(claim,now=100,status='RATE_LIMITED',result={'fixture_http':429},actual_micro_usd=None)
        self.assertEqual(state,'UNKNOWN');self.assertIsNone(self.claim(200))
        self.assertEqual(before,self.store.db.execute('SELECT record FROM cycles').fetchone()[0])

    def test_known_429_fixture_cooldown_does_not_advance(self):
        self.router.ingest(observation());self.route();claim=self.claim()
        self.store.finish(claim,now=100,status='RATE_LIMITED',result={'fixture_http':429},actual_micro_usd=0)
        self.assertIsNone(self.claim(101))
        self.assertEqual(json.loads(self.store.db.execute('SELECT record FROM cycles').fetchone()[0])['transitions'],[])

    def test_unknown_and_per_call_cost_bounds_block(self):
        self.router.ingest(observation())
        self.assertIn('UNKNOWN_COST_BOUND',self.route(cost_bound_micro_usd=None)['blockers'])
        self.assertIn('PER_CALL_CAP',self.route(cost_bound_micro_usd=101)['blockers'])
        self.assertEqual(self.count('tasks'),0)
        self.assertEqual(self.route(cost_bound_micro_usd=100)['status'],'QUEUED_CANDIDATE_REVIEW')

    def test_daily_cap_applies_at_shared_executor(self):
        self.router.ingest(observation());self.route();claim=self.claim()
        self.store.finish(claim,now=100,status='SUCCEEDED',result={'fixture_response':'proposal'},actual_micro_usd=100)
        self.router.ingest(observation('b'));self.route()
        self.assertIsNone(self.claim(101));self.assertEqual(self.count('calls'),1)

    def test_oversized_contradiction_packet_blocks_not_silent_drop(self):
        self.router=ContextRouter(self.store,replace(self.router.policy,max_observations=1))
        self.router.ingest(observation('a'));self.router.ingest(observation('b',contradicts=['a']))
        r=self.route();self.assertIn('CONTEXT_COUNT_BOUND',r['blockers']);self.assertIsNone(r['packet'])
        self.assertEqual(self.count('tasks'),0)

    def test_missing_contradiction_and_private_envelope_block(self):
        self.router.ingest(observation(contradicts=['missing'],classification='PRIVATE'))
        r=self.route();self.assertIn('UNRESOLVED_CONTRADICTION',r['blockers']);self.assertIn('PROCESSING_ENVELOPE',r['blockers'])
        self.assertIsNone(r['packet'])

    def test_dispatch_rechecks_expiry_and_new_evidence(self):
        self.router.ingest(observation(expires_at=150));self.route();claim=self.claim()
        self.router.validate_claim(claim,now=100)
        with self.assertRaises(SemanticError):self.router.validate_claim(claim,now=150)
        self.router.ingest(observation('b'))
        with self.assertRaises(SemanticError):self.router.validate_claim(claim,now=101)

    def test_input_rebinding_and_unknown_trigger_rejected(self):
        self.router.ingest(observation())
        with self.assertRaises(SemanticError):self.router.ingest(observation(summary='changed'))
        with self.assertRaises(SemanticError):normalize(observation(triggers=['TOKEN_AVAILABILITY']))
        with self.assertRaises(SemanticError):normalize(observation(uncertainty=True))

    def test_local_evidence_coverage_comparison_not_model_quality(self):
        self.router.ingest(observation('a',summary='x'*1000))
        self.router.ingest(observation('b',contradicts=['a'],summary='y'*1000))
        packet=self.route()['packet']
        expected={(s['ref'],s['sha256']) for o in [observation('a'),observation('b')] for s in o['sources']}
        actual={(s['ref'],s['sha256']) for o in packet['observations'] for s in o['sources']}
        self.assertEqual(actual,expected)
        self.assertTrue(any(o['contradicts'] for o in packet['observations']))
        # This measures reference preservation only, not frontier conclusions or false negatives.

if __name__=='__main__':unittest.main()
