"""Bounded EDCR candidate over CompletionStore, not a knowledge/authority store.

Trusted ingress supplies classification, lineage and policy; this module cannot
verify external evidence truth. A public adapter MUST call validate_claim directly
before its one provider call. CompletionStore owns reservations, rate limits,
unknown-charge reconciliation and process advancement. No network is used here.
"""
from __future__ import annotations
from dataclasses import dataclass, asdict
import json
from .completion_runner import digest, encoded, integer, text, timestamp
from .core import SemanticError

TRIGGERS = frozenset({'SEMANTIC_DESIGN', 'GOVERNING_ASSUMPTION', 'AUTHORITY', 'RIGHTS',
    'ACTION_GATE', 'PRIVACY', 'SECURITY', 'VERIFICATION_FAILED', 'EVIDENCE_OVERTURNS',
    'DEPENDENCY_INVALIDATED'})


@dataclass(frozen=True)
class RoutingPolicy:
    version: str = 'EDCR-REFERENCE-1'
    max_packet_chars: int = 16000
    max_ledger_observations: int = 2048
    max_observations: int = 32
    excerpt_chars: int = 500
    uncertainty_threshold: int = 70
    per_call_micro_usd: int = 100000

    def __post_init__(self):
        text(self.version)
        for key in ('max_packet_chars', 'max_ledger_observations', 'max_observations', 'excerpt_chars', 'per_call_micro_usd'):
            integer(getattr(self, key), 1)
        integer(self.uncertainty_threshold)
        if self.uncertainty_threshold > 100:
            raise SemanticError('uncertainty threshold out of range')


def normalize(observation):
    """Source-sensitive fingerprint excludes receipt time/ID only, not valid time.

    Payloads have a closed vocabulary; model claims are explicitly observations.
    Unknown hash is represented by None, never a fabricated evidence digest.
    """
    required = {'observation_id', 'subject', 'event_kind', 'event_time', 'valid_from',
        'observed_at', 'expires_at', 'changed_fields', 'sources', 'lane', 'model',
        'risk', 'uncertainty', 'contradicts', 'supersedes', 'parents', 'summary',
        'classification', 'processing_envelope', 'triggers'}
    if not isinstance(observation, dict) or set(observation) != required:
        raise SemanticError('observation fields missing or unknown')
    o = json.loads(encoded(observation))
    for key in ('observation_id', 'subject', 'event_kind', 'lane', 'summary'):
        text(o[key])
    if len(o['summary']) > 4096 or len(encoded(o)) > 32000:
        raise SemanticError('observation input exceeds bound')
    for key in ('event_time', 'valid_from', 'observed_at', 'expires_at'):
        timestamp(o[key])
    if o['expires_at'] <= o['valid_from'] or o['event_time'] > o['observed_at']:
        raise SemanticError('invalid observation time interval')
    if o['model'] is not None:
        text(o['model'])
    if o['risk'] not in {'LOW', 'MEDIUM', 'HIGH', 'CRITICAL', 'UNKNOWN'}:
        raise SemanticError('invalid risk')
    integer(o['uncertainty'])
    if o['uncertainty'] > 100:
        raise SemanticError('invalid uncertainty')
    if o['classification'] not in {'PUBLIC', 'PRIVATE'}:
        raise SemanticError('invalid classification')
    for key in ('changed_fields', 'contradicts', 'supersedes', 'parents', 'processing_envelope', 'triggers'):
        if not isinstance(o[key], list) or len(o[key]) > 64:
            raise SemanticError('bounded list required')
        for entry in o[key]:
            text(entry)
        o[key] = sorted(set(o[key]))
    if set(o['triggers']) - TRIGGERS:
        raise SemanticError('unknown materiality trigger')
    if o['observation_id'] in o['contradicts'] + o['supersedes'] + o['parents']:
        raise SemanticError('self-referential observation')
    if not isinstance(o['sources'], list) or not 1 <= len(o['sources']) <= 16:
        raise SemanticError('bounded source references required')
    for source in o['sources']:
        if not isinstance(source, dict) or set(source) != {'ref', 'sha256'}:
            raise SemanticError('source reference/hash required')
        text(source['ref'])
        h = source['sha256']
        if h is not None and (not isinstance(h, str) or len(h) != 64 or any(c not in '0123456789abcdef' for c in h)):
            raise SemanticError('malformed source digest')
    o['sources'] = sorted(o['sources'], key=encoded)
    o['fingerprint'] = digest({k:v for k,v in o.items() if k not in {'observation_id', 'observed_at'}})
    o['epistemic_status'] = 'OBSERVATION_NOT_VERIFIED_FACT'
    return o


class ContextRouter:
    def __init__(self, store, policy=RoutingPolicy()):
        self.store, self.policy = store, policy
        self.db = store.db
        self.db.executescript('''
          CREATE TABLE IF NOT EXISTS context_observations
            (fingerprint TEXT PRIMARY KEY, record TEXT NOT NULL);
          CREATE TABLE IF NOT EXISTS context_aliases
            (id TEXT PRIMARY KEY, fingerprint TEXT NOT NULL REFERENCES context_observations(fingerprint));
          CREATE TABLE IF NOT EXISTS context_routes
            (route_key TEXT PRIMARY KEY, record TEXT NOT NULL);
        ''')

    def ingest(self, observation):
        o = normalize(observation)
        with self.store.transaction():
            old = self.db.execute('SELECT fingerprint FROM context_aliases WHERE id=?', (o['observation_id'],)).fetchone()
            if old and old[0] != o['fingerprint']:
                raise SemanticError('observation ID rebound; emit successor observation')
            existing = self.db.execute('SELECT record FROM context_observations WHERE fingerprint=?', (o['fingerprint'],)).fetchone()
            if not existing:
                if self.db.execute('SELECT COUNT(*) FROM context_observations').fetchone()[0] >= self.policy.max_ledger_observations:
                    raise SemanticError('bounded observation index full; owning retention policy required')
                self.db.execute('INSERT INTO context_observations VALUES (?,?)', (o['fingerprint'], encoded(o)))
            self.db.execute('INSERT OR IGNORE INTO context_aliases VALUES (?,?)', (o['observation_id'], o['fingerprint']))
            self.store.event('CONTEXT_OBSERVATION', {'observation_id':o['observation_id'], 'fingerprint':o['fingerprint'], 'duplicate':bool(existing)})
        return {'status':'DUPLICATE' if existing else 'NEW', 'fingerprint':o['fingerprint']}

    def _context(self, subject, now):
        observations = {r[0]:json.loads(r[1]) for r in self.db.execute('SELECT fingerprint,record FROM context_observations')}
        aliases = {r[0]:r[1] for r in self.db.execute('SELECT id,fingerprint FROM context_aliases')}
        chosen = {k for k,o in observations.items() if o['subject'] == subject}
        # Preserve both outgoing and incoming contradiction edges, even cross-subject.
        missing = set()
        while True:
            expanded = set(chosen)
            for k,o in observations.items():
                targets = {aliases[x] for x in o['contradicts'] + o['supersedes'] if x in aliases}
                if k in chosen or targets & chosen:
                    expanded.add(k); expanded.update(targets)
                    missing.update(x for x in o['contradicts'] if x not in aliases)
            if expanded == chosen:
                break
            chosen = expanded
        selected = [observations[k] for k in sorted(chosen)]
        superseded = {aliases[x] for o in selected for x in o['supersedes'] if x in aliases}
        state = [{'fingerprint':o['fingerprint'],
                  'fresh':o['valid_from'] <= now < o['expires_at'] and o['observed_at'] <= now and o['fingerprint'] not in superseded,
                  'superseded':o['fingerprint'] in superseded} for o in selected]
        # Keep original relation IDs while resolving deduplicated aliases. Every
        # relation is either resolvable through this map or explicitly unknown.
        relation_ids = sorted({x for o in selected for kind in ('contradicts','supersedes','parents') for x in o[kind]})
        relation_bindings = {}
        for relation_id in relation_ids:
            target = observations.get(aliases.get(relation_id))
            if target is None:
                relation_bindings[relation_id] = {'status':'UNKNOWN'}
            elif target['classification'] != 'PUBLIC' or 'PUBLIC_REVIEW' not in target['processing_envelope']:
                relation_bindings[relation_id] = {'status':'WITHHELD_PROCESSING_ENVELOPE'}
            else:
                relation_bindings[relation_id] = {
                    'status':'IN_PACKET' if target['fingerprint'] in chosen else 'SOURCE_BACK_POINTER_ONLY',
                    'fingerprint':target['fingerprint'], 'canonical_observation_id':target['observation_id']}
        return selected, state, sorted(missing), relation_bindings

    def route(self, *, cycle_id, question, subject, now, cost_bound_micro_usd=None, closure=None, observed_binding=None):
        text(cycle_id); text(question); text(subject); timestamp(now)
        if len(question) > 2000:
            raise SemanticError('question exceeds bound')
        if cost_bound_micro_usd is not None:
            integer(cost_bound_micro_usd)
        with self.store.transaction():
            observations, state, missing, relation_bindings = self._context(subject, now)
            closure_binding, source_binding, adequacy_failures = self._adequacy(closure, observed_binding, cycle_id)
            binding = {'cycle_id':cycle_id, 'question':question, 'subject':subject,
                       'policy':asdict(self.policy), 'state':state, 'missing_contradictions':missing,
                       'relation_bindings':relation_bindings, 'closure':closure_binding, 'source_binding':source_binding}
            route_key = digest(binding)
            prior = self.db.execute('SELECT record FROM context_routes WHERE route_key=?', (route_key,)).fetchone()
            if prior:
                result = json.loads(prior[0])
            else:
                fresh = [o for o,s in zip(observations,state) if s['fresh']]
                reasons = set()
                for o in fresh:
                    if o['risk'] in {'HIGH','CRITICAL'}: reasons.add('HIGH_RISK')
                    if o['risk'] == 'UNKNOWN' or o['uncertainty'] >= self.policy.uncertainty_threshold: reasons.add('UNCERTAINTY')
                    reasons.update(o['triggers'])
                    if o['contradicts']: reasons.add('CONTRADICTION')
                result = {'schema':'GardenContextRoutingReceipt/v1', 'route_key':route_key,
                    'binding':binding, 'assessed_at':now, 'reasons':sorted(reasons),
                    'materiality':'MATERIAL' if reasons else 'NOT_MATERIAL',
                    'status':'NOT_MATERIAL', 'authorization_effect':'NONE', 'provider_calls':0,
                    'frontier_cost_benchmark':'NOT_MEASURED_NO_LIVE_PROVIDER', 'packet':None,
                    'context_adequacy':'SUFFICIENT_BOUNDED' if not adequacy_failures else 'UNKNOWN_OR_INCOMPLETE',
                    'frontier_lane':'EXTERNAL_CHATGPT_FRONTIER_REVIEW_NOT_AUTOMATICALLY_INVOKED'}
                if reasons:
                    blockers = list(adequacy_failures)
                    if missing: blockers.append('UNRESOLVED_CONTRADICTION')
                    if any(o['classification'] != 'PUBLIC' or 'PUBLIC_REVIEW' not in o['processing_envelope'] for o in observations): blockers.append('PROCESSING_ENVELOPE')
                    if len(observations) > self.policy.max_observations: blockers.append('CONTEXT_COUNT_BOUND')
                    if cost_bound_micro_usd is None: blockers.append('UNKNOWN_COST_BOUND')
                    elif cost_bound_micro_usd > self.policy.per_call_micro_usd: blockers.append('PER_CALL_CAP')
                    entries=[]
                    for o,s in zip(observations,state):
                        e = {**o, 'summary':o['summary'][:self.policy.excerpt_chars],
                            'use':'CURRENT_OBSERVATION' if s['fresh'] else 'HISTORICAL_ONLY_REVALIDATION_REQUIRED',
                            'omitted_summary_chars':max(0,len(o['summary'])-self.policy.excerpt_chars)}
                        entries.append(e)
                    payload={'schema':'GardenContextPacket/v1','question':question,'subject':subject,
                        'policy':asdict(self.policy), 'source_observations_root':digest(state),
                        'observations':entries, 'relation_bindings':relation_bindings,
                        'source_binding':source_binding, 'closure':closure_binding,
                        'unknowns':sorted(set(missing) | {k for k,v in relation_bindings.items() if v['status'] in {'UNKNOWN','WITHHELD_PROCESSING_ENVELOPE'}}),
                        'compression':{'policy':self.policy.version,'method':'BOUNDED_SUMMARY_PREFIX_WITH_FULL_REFERENCES',
                            'semantic_loss_bound':'UNKNOWN; excerpt never substitutes for underlying evidence',
                            'omitted_observations':[], 'raw_evidence_deleted':False},
                        'epistemic_status':'DERIVED_CONTEXT_NOT_PROOF_TRUTH_AUTHORITY_OR_CANON',
                        'whole_source_review':'NOT_SATISFIED_BY_THIS_PACKET'}
                    if len(encoded({**payload, 'packet_hash':digest(payload)})) > self.policy.max_packet_chars: blockers.append('CONTEXT_CHARACTER_BOUND')
                    result['blockers']=blockers
                    if not blockers:
                        result['packet']={**payload,'packet_hash':digest(payload)}
                        result['status']='QUEUED_CANDIDATE_REVIEW'
                        result['task_id']='context-'+route_key
                        result['cost_bound_micro_usd']=cost_bound_micro_usd
                # Cost uncertainty is retriable after trusted pricing is available;
                # no admitted route or consumed event is persisted in that case.
                if not result.get('blockers'):
                    self.db.execute('INSERT INTO context_routes VALUES (?,?)',(route_key,encoded(result)))
                elif reasons:
                    result['status']='PACKET_INCOMPLETE' if adequacy_failures else 'BLOCKED'
                    if adequacy_failures:
                        result['context_expansion_request']={'status':'REQUIRED','reasons':adequacy_failures,'automatic_whole_context_fetch':False}
                self.store.event('CONTEXT_ROUTING', result)
        if result['status'] == 'QUEUED_CANDIDATE_REVIEW':
            # Deterministic task identity makes retry after crash-before-enqueue safe.
            self.store.enqueue(result['task_id'],cycle_id,handler='context_specialist_public', external=True,
                pool='routine',max_cost_micro_usd=result['cost_bound_micro_usd'],packet_hash=result['packet']['packet_hash'])
        return json.loads(encoded(result))

    def validate_claim(self, claim, *, now, closure=None, observed_binding=None):
        """Mandatory trusted-adapter seam immediately before external dispatch.

        Rechecks latest relevant context and freshness; does not grant authority or
        replace the CompletionStore lease/budget and existing public adapter gates.
        """
        timestamp(now)
        row=self.db.execute('SELECT record FROM context_routes WHERE route_key=?', (claim['task_id'].removeprefix('context-'),)).fetchone()
        task=self.db.execute('SELECT state,token,lease,spec FROM tasks WHERE id=?',(claim['task_id'],)).fetchone()
        if not row or not task or task['state']!='RUNNING' or task['token']!=claim['token'] or task['lease']<=now:
            raise SemanticError('unclaimed or stale context task')
        if encoded(claim['spec']) != task['spec'] or claim['spec']['handler'] != 'context_specialist_public':
            raise SemanticError('dispatch specification rebound')
        receipt=json.loads(row[0]); p=receipt['packet']; b=receipt['binding']
        cb,sb,failures=self._adequacy(closure,observed_binding,b['cycle_id'])
        if failures or cb!=b.get('closure') or sb!=b.get('source_binding'):
            raise SemanticError('source epoch/root or closure drift; expanded revalidation required')
        _,state,missing,relation_bindings=self._context(b['subject'],now)
        if receipt['materiality']!='MATERIAL' or b['policy']!=asdict(self.policy) or b['state']!=state or b['missing_contradictions']!=missing or b.get('relation_bindings')!=relation_bindings or p.get('relation_bindings')!=relation_bindings:
            raise SemanticError('context or policy drift; re-evaluate before provider call')
        if claim['spec']['packet_hash']!=p['packet_hash'] or digest({k:v for k,v in p.items() if k!='packet_hash'})!=p['packet_hash']:
            raise SemanticError('context packet hash mismatch')
        return json.loads(encoded(p))

    def _adequacy(self, closure, observed_binding, cycle_id):
        """Trusted closure-verifier seam; an observation/model assertion is insufficient.

        This reference checks bindings and explicit sufficiency fields, not the
        truth of closure evidence. Deployment must authenticate that verifier.
        """
        fields={'status','evidence_ref','dependency_root','design_epoch','source_root_sha256',
                'whole_context_required','cross_owner_high_risk','affected_scope_bounded','contradiction_context_sufficient'}
        if not isinstance(closure,dict) or set(closure)!=fields or observed_binding is None:
            return {'status':'UNKNOWN'},None,['CLOSURE_UNKNOWN']
        closure=json.loads(encoded(closure))
        source={'design_epoch':observed_binding.design_epoch,'source_root_sha256':observed_binding.source_root_sha256,
                'repo_heads':dict(observed_binding.repo_heads)}
        failures=[]
        if closure['status']!='SUFFICIENT_BOUNDED':failures.append('CLOSURE_INCOMPLETE')
        if not isinstance(closure['evidence_ref'],str) or not closure['evidence_ref'].strip():failures.append('CLOSURE_EVIDENCE_UNKNOWN')
        h=closure['dependency_root']
        if not isinstance(h,str) or len(h)!=64 or any(c not in '0123456789abcdef' for c in h):failures.append('DEPENDENCY_ROOT_UNKNOWN')
        for key,required in [('whole_context_required',False),('cross_owner_high_risk',False),('affected_scope_bounded',True),('contradiction_context_sufficient',True)]:
            if closure[key] is not required:failures.append(key.upper())
        row=self.db.execute('SELECT record FROM cycles WHERE id=?',(cycle_id,)).fetchone()
        existing=json.loads(row[0])['binding'] if row else {}
        if observed_binding.cycle_id!=cycle_id or any(source[k]!=existing.get(k) for k in source):failures.append('SOURCE_BINDING_CHANGED')
        if any(closure[k]!=source[k] for k in ('design_epoch','source_root_sha256')):failures.append('CLOSURE_SOURCE_CHANGED')
        return closure,source,failures

    def frontier_request(self, route_key, *, now, closure=None, observed_binding=None):
        """Create a manual ChatGPT handoff artifact; never enqueue a provider call.

        A bounded specialist must finish first. This is a request, not evidence
        that ChatGPT reviewed it, a handoff was sent, or independent quorum met.
        """
        timestamp(now);text(route_key)
        row=self.db.execute('SELECT record FROM context_routes WHERE route_key=?',(route_key,)).fetchone()
        if not row:raise SemanticError('material routing receipt absent')
        receipt=json.loads(row[0]);b=receipt['binding'];packet=receipt['packet']
        if receipt['materiality']!='MATERIAL' or packet is None:raise SemanticError('material adequate packet required')
        task=self.db.execute('SELECT state FROM tasks WHERE id=?',(receipt['task_id'],)).fetchone()
        if not task or task['state']!='SUCCEEDED':raise SemanticError('bounded specialist review not complete')
        cb,sb,failures=self._adequacy(closure,observed_binding,b['cycle_id'])
        _,state,missing,relations=self._context(b['subject'],now)
        if failures or b['policy']!=asdict(self.policy) or cb!=b['closure'] or sb!=b['source_binding'] or state!=b['state'] or missing!=b['missing_contradictions'] or relations!=b['relation_bindings']:
            raise SemanticError('handoff context inadequate or stale; request expansion')
        if packet['packet_hash']!=digest({k:v for k,v in packet.items() if k!='packet_hash'}):raise SemanticError('packet hash mismatch')
        request={'schema':'GardenFrontierReviewRequest/v1','lane':'EXTERNAL_CHATGPT_FRONTIER_REVIEW',
                 'status':'MANUAL_HANDOFF_REQUEST_NOT_SENT','provider_boundary':'NOT_OPENROUTER',
                 'materiality_receipt_ref':route_key,'packet':packet,'packet_hash':packet['packet_hash'],
                 'specialist_task_ref':receipt['task_id'],'source_binding':sb,
                 'authorization_effect':'NONE','canonical_admission':False}
        return {**request,'request_id':digest(request)}

    @staticmethod
    def model_output_observation(output, *, model, response_ref):
        """Provider prose can be retained only as attributed, unadmitted material."""
        text(output); text(model); text(response_ref)
        if len(output)>16000:
            raise SemanticError('model output exceeds bound')
        return {'content':output,'model':model,'response_ref':response_ref,
                'status':'UNVERIFIED_MODEL_PROPOSAL','authority':'NONE','canonical_admission':False}
