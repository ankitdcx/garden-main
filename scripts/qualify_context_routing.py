#!/usr/bin/env python3
"""Execute bounded local EDCR scenarios; never invent live provider benchmarks."""
import hashlib
import io
import json
import platform
import sys
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'implementation'))
sys.path.insert(0,str(ROOT/'implementation/tests'))
from garden_kernel.context_routing import ContextRouter,RoutingPolicy
from garden_kernel.completion_runner import CompletionStore,Limits,encoded
from test_context_routing import observation,BINDING,PROFILE,CLOSURE

class RecordedResults(unittest.TextTestResult):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs);self.scenarios=[]
    def addSuccess(self,test):
        super().addSuccess(test);self.scenarios.append({'scenario':test.id(),'result':'PASS'})
    def addFailure(self,test,err):
        super().addFailure(test,err);self.scenarios.append({'scenario':test.id(),'result':'FAIL'})
    def addError(self,test,err):
        super().addError(test,err);self.scenarios.append({'scenario':test.id(),'result':'ERROR'})

def main():
    stream=io.StringIO()
    result=unittest.TextTestRunner(stream=stream,verbosity=2,resultclass=RecordedResults).run(
        unittest.defaultTestLoader.discover(str(ROOT/'implementation/tests'),pattern='test_context_routing.py'))
    with tempfile.TemporaryDirectory() as directory:
        store=CompletionStore(Path(directory)/'state.sqlite',Limits(daily_micro_usd=150))
        store.create_cycle(BINDING,'fixture','NON_SEMANTIC_REPAIR',PROFILE)
        router=ContextRouter(store,RoutingPolicy(per_call_micro_usd=100))
        obs=[observation('a',summary=('first '*300).strip()),observation('b',contradicts=['a'],summary=('counter '*300).strip())]
        raw=[router.ingest(o) for o in obs];raw.append(router.ingest(obs[0]))
        r=router.route(cycle_id=BINDING.cycle_id,question='Fixture contradiction?',subject='permission',now=100,cost_bound_micro_usd=100,closure=CLOSURE,observed_binding=BINDING)
        packet=r['packet'];store.close()
    paths=['implementation/garden_kernel/context_routing.py','implementation/garden_kernel/completion_runner.py',
           'implementation/tests/test_context_routing.py','scripts/qualify_context_routing.py',
           'design_deltas/v15.7/EVENT-DRIVEN-CONTEXT-ROUTING-CANDIDATE.md',
           'design_deltas/v15.7/EVENT-DRIVEN-CONTEXT-ROUTING-CORRECTION-2026-09-16.md',
           'governance/EVENT_DRIVEN_WORK_POLICY_v1.json']
    implementation_path='implementation/garden_kernel/context_routing.py'
    impl_hash=hashlib.sha256((ROOT/implementation_path).read_bytes()).hexdigest()
    specs=[
        ('NORMALIZE','normalize','Capability.Knowledge','[T-KNOWLEDGE]',
         ['Closed observation fields; bounded canonical strings/lists; valid UTC intervals; source refs with known hash or explicit None'],
         ['Deterministic source-sensitive fingerprint excludes only receipt ID/time','Observation remains unverified; model provenance retained'],
         ['SemanticError for malformed fields, oversized input or invalid interval'],
         'No persistent mutation; no network', ['test_input_rebinding_and_unknown_trigger_rejected','test_identical_prose_changed_source_hash_reevaluates']),
        ('INGEST','ContextRouter.ingest','Capability.Knowledge','[T-KNOWLEDGE]',
         ['Trusted ingress classification/provenance; normalize succeeds; shared CompletionStore available'],
         ['Atomic immutable record plus source-sensitive aliases; replay deduplicated','Rebound observation IDs rejected; index capacity bounded'],
         ['SemanticError on rebound ID or full bounded index','SQLite transaction failure rolls back mutation'],
         'Writes bounded context index and audit event; never deletes external evidence',
         ['test_duplicate_does_not_expand_or_add_task_even_after_restart']),
        ('ROUTE','ContextRouter.route','Capability.Compute.Execution','[T-PROCESS]',
         ['Bounded question and current cycle; explicit policy; trusted cost upper bound for queued specialist review; explicit sufficient closure and current source binding'],
         ['Reason-coded materiality; NOT_MATERIAL produces no task','Required contradictory/provenance data retained or packet blocked; all original relation IDs resolve through hash-bound alias mapping or remain explicitly unknown','Deterministic task identity and packet hash; no process advancement'],
         ['BLOCKED for missing contradictions, envelope restriction, packet bounds or unknown/excessive cost','SemanticError or SQLite error for malformed input/persistence failure'],
         'Writes routing/audit record and optionally idempotent external-review task; does not call provider',
         ['test_no_change_and_clock_passage_do_not_spend','test_unknown_and_per_call_cost_bounds_block','test_oversized_contradiction_packet_blocks_not_silent_drop','test_daily_cap_applies_at_shared_executor','test_duplicate_alias_contradiction_resolves_both_sides','test_duplicate_alias_supersession_and_parent_resolve']),
        ('VALIDATE','ContextRouter.validate_claim','Capability.Compute.Execution','[T-FUNCTION-CONTRACT]',
         ['Claim matches persisted RUNNING token, lease and specification; trusted current clock; actual public adapter calls immediately before dispatch'],
         ['Reject drift in current context, expiry, policy or packet hash','Return detached bounded packet only for matching materiality receipt'],
         ['SemanticError on unclaimed/stale token, context drift or hash/spec mismatch'],
         'Read-only validation; grants no authority and performs no network effect',
         ['test_dispatch_rechecks_expiry_and_new_evidence','test_resolved_parent_alias_invalidates_queued_packet']),
        ('FRONTIER-REQUEST','ContextRouter.frontier_request','Capability.Compute.Execution','[T-PROCESS]',
         ['Material receipt; sufficient explicitly verified bounded closure; current source binding; specialist task succeeded'],
         ['Deterministic manual GardenFrontierReviewRequest/v1; no credential or provider-model routing fields','No queue insertion, automatic ChatGPT invocation, authority or canonical admission'],
         ['SemanticError on missing specialist completion, stale source/closure/context or inadequate packet'],
         'Returns manual handoff artifact only; does not send it',
         ['test_specialist_queue_is_separate_from_manual_chatgpt_request','test_source_epoch_and_closure_drift_reject_dispatch','test_changed_policy_blocks_manual_handoff_after_specialist_completion']),
        ('MODEL-OUTPUT','ContextRouter.model_output_observation','Capability.Knowledge','[T-KNOWLEDGE]',
         ['Bounded provider text; model identity and response reference supplied'],
         ['Output always UNVERIFIED_MODEL_PROPOSAL with authority NONE and canonical_admission false'],
         ['SemanticError for malformed or oversized output'],
         'Returns attributed proposal record only; no storage, admission or network',
         ['test_provider_authority_claim_remains_unverified_proposal'])]
    contracts=[]
    for suffix,function,owner,anchor,pre,post,errors,effects,tests in specs:
        c={'contract_id':'QEDCR-FC-'+suffix,'version':'1.0.0','function':function,'path':implementation_path,
           'source_sha256':impl_hash,'owner':owner,'owner_anchor':anchor,
           'source_schema_reference':'FunctionContract SCHEMA-AF063594FE',
           'public_consequential_boundary':function,'preconditions':pre,'postconditions':post,
           'affects':['CONTEXT','AUDIT','REVIEW_ADMISSION'],
           'input_semantics':'; '.join(pre),'output_semantics':'; '.join(post),
           'proof_obligations':['context-is-not-authority','source-provenance-preserved','unknowns-not-promoted','declared-resource-bounds'],
           'failures':errors,'error_semantics':'; '.join(errors),
           'unknown_semantics':'Unknown cost blocks queueing; unknown external charge is retained by CompletionStore; source/hash uncertainty and historical observations remain explicit; no unknown becomes truth or authority.',
           'effect_semantics':effects,
           'resources_and_termination':{'observation_input_max_chars':32000,'summary_max_chars':4096,'source_ref_max_count':16,
             'list_max_count':64,'default_ledger_observations':2048,'default_packet_observations':32,
             'default_packet_chars':16000,'question_max_chars':2000,'algorithm':'Finite bounded ledger scan and fixed-point relation closure; SQLite timeout inherited from CompletionStore; no external retries here.'},
           'dependencies':['CompletionStore.transaction/event/enqueue/claim/finish','completion_runner.digest/encoded validation helpers','SemanticError','SQLite','versioned RoutingPolicy'],
           'invalidators':['implementation or contract body change','policy version/threshold/budget change','source observation/freshness/contradiction/supersession change','cycle/packet/token/lease drift','authority/public-processing envelope change'],
           'authority_and_consent':'Public review envelope required; no grants created; existing process/ActionGate/provider guards remain controlling.',
           'provenance':'Source file SHA-256, candidate ID, owner anchor, observation source/model ancestry, routing receipt and packet hash; external results must carry actual provider response identity.',
           'test_refs':['implementation/tests/test_context_routing.py'],
           'test_cases':['ContextRoutingTests.'+t for t in tests],
           'body_hash_algorithm':'sha256(canonical-json(contract excluding body_sha256))'}
        c['body_sha256']=hashlib.sha256(encoded(c).encode()).hexdigest();contracts.append(c)
    contract_registry={'schema':'GardenFunctionContractRegistry/v1',
        'registry_id':'GARDEN-EDCR-BOUNDED-DECLARATIONS-v1',
        'design_epoch':'v15.5','canonical_source_root_sha256':'63561ce9fcd4a72f44af333662b342fd18c4e99930209c30c5f801bcc5c74598',
        'scope_globs':[implementation_path],'semantic_compliance_proved':False,
        'status':'DECLARATION_ONLY_NOT_MACHINE_ADMISSION','source_schema_reference':'FunctionContract SCHEMA-AF063594FE',
        'source_delta_references':['CAND-EDCR-001'],'contracts':contracts,
        'limitations':['These local declarations do not allocate canonical machine FunctionContract identities or confer execution authority.',
          'No external provider adapter or production trust-boundary qualification is established.']}
    receipt={'schema':'GardenContextRoutingQualificationReceipt/v1','candidate':'CAND-EDCR-001',
        'status':'BOUNDED_LOCAL_SCENARIOS_PASS_NOT_PRODUCTION_QUALIFIED' if result.wasSuccessful() else 'LOCAL_SCENARIOS_FAILED',
        'executed_at':datetime.now(timezone.utc).isoformat(),'python':platform.python_version(),
        'source_hashes':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},
        'tests_run':result.testsRun,'scenarios':result.scenarios,
        'fixture_metrics':{'raw_event_count':len(raw),'unique_observations':sum(x['status']=='NEW' for x in raw),
            'duplicate_observations':sum(x['status']=='DUPLICATE' for x in raw),
            'raw_summary_characters':sum(len(o['summary']) for o in obs),
            'packet_summary_characters':sum(len(o['summary']) for o in packet['observations']),
            'full_packet_characters':len(encoded(packet)),'source_refs_before':sum(len(o['sources']) for o in obs),
            'source_refs_after':sum(len(o['sources']) for o in packet['observations']),
            'live_provider_calls':0,'external_spend_micro_usd':0,'input_tokens':None,'output_tokens':None},
        'frontier_quality_and_cost_benchmark':{'status':'NOT_EXECUTED_NO_LIVE_AUTHORIZED_PROVIDER',
            'conclusion_preservation':None,'false_negative_rate':None,'provider_cost_savings':None},
        'authority_effect':'NONE','canonical_promotion':False,
        'owner_anchors':['[T-PROCESS]','[T-KNOWLEDGE]','[T-EVENT-CONTRACT]','[T-FUNCTION-CONTRACT]','[T-PROVENANCE-EXT]'],
        'runtime_seams':{'ingress':'ContextRouter.ingest requires trusted classification/provenance input',
            'admission':'ContextRouter.route -> CompletionStore.enqueue with deterministic task and packet identity',
            'dispatch':'CompletionStore.claim -> ContextRouter.validate_claim with fresh source/closure -> separately qualified context_specialist_public adapter; frontier_request returns separate manual ChatGPT artifact',
            'completion':'CompletionStore.finish preserves rate-limit/unknown-charge state; no automatic Process.advance',
            'retention':'Bounded indexed observation view; never deletes external raw evidence; capacity rejects new intake'},
        'limitations':['Local fixture results are not external provider results.',
            'No truth verification, production trust-boundary isolation or whole-source completeness claim.',
            'Whole-repository generalization remains partial/unimplemented; source correction is enforced only by this bounded core.',
            'Closure sufficiency is supplied by a trusted verifier seam, not proved by self-asserted observation/model content.',
            'No live provider adapter activated. It must enforce validate_claim immediately before its single call and ordinary provider/publication guards.',
            'Future adversarial caller changes between check and external call require deployment-level serialized ingress or equivalent fencing; no distributed atomicity proof.',
            'Automatic active-high-value maximum-staleness scheduling and durable batch-provider adapter remain deferred.',
            'Summary truncation declares unknown semantic loss; contradictory/source refs are preserved or packet blocked.',
            'Local source-reference coverage is measured; frontier quality, false negatives, independent-family quorum and cost savings are not measured.']}
    out=ROOT/'reviews/v15.7/qualification/context-routing';out.mkdir(parents=True,exist_ok=True)
    (out/'FUNCTION-CONTRACTS.json').write_text(json.dumps(contract_registry,indent=2)+'\n')
    receipt['function_contract_declarations_sha256']=hashlib.sha256((out/'FUNCTION-CONTRACTS.json').read_bytes()).hexdigest()
    (out/'context-routing-receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
    (out/'unit-scenarios.txt').write_text(stream.getvalue())
    (out/'README.md').write_text('# Bounded EDCR reference qualification\n\nRun `python scripts/qualify_context_routing.py`. Receipts cover deterministic local source-sensitive deduplication, bounded context, provenance/contradiction/freshness handling and the shared completion executor’s conservative budget/recovery paths. Provider responses in tests are explicitly fixtures. No external provider was called; no frontier quality or cost benchmark is claimed.\n\nExisting owner anchors: Technical `[T-PROCESS]`, `[T-KNOWLEDGE]`, `[T-EVENT-CONTRACT]`, `[T-FUNCTION-CONTRACT]`, `[T-PROVENANCE-EXT]`. This indexed observation view creates no new truth or authority owner. Model outputs remain unverified proposals.\n\nDispatch seam: `CompletionStore.claim` then mandatory `ContextRouter.validate_claim` in the trusted public specialist adapter with explicit trusted closure/source binding immediately before its one provider call; frontier_request creates a separate manual ChatGPT request after specialist completion; `CompletionStore.finish` handles accounting/unknown outcome. The reference does not activate or qualify a live public adapter.\n')
    print(json.dumps({'status':receipt['status'],'tests_run':result.testsRun,'live_provider_calls':0,'receipt':str(out/'context-routing-receipt.json')}))
    return 0 if result.wasSuccessful() else 1
if __name__=='__main__':raise SystemExit(main())
