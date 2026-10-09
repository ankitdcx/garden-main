#!/usr/bin/env python3
"""SIC-0.1: bounded NONCANONICAL physical research adapter; standard library.
Run: python3 design_deltas/v15.10/electricity_closure.py [--details]
Not a complete GSL/SAL compiler, TREE_CORE r6, or automatic scientific admission.
No network, credentials, external actuation or paid providers.
"""
from __future__ import annotations
import argparse
import copy
import hashlib
import itertools
import json
import math
import random
import time
from collections import Counter
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
PROFILE = 'SIC-0.1/finite-physical-research'
ADMISSION = 'NONCANONICAL_RESEARCH_NO_SELF_ADMISSION'
OBJECTS = ('TIME','SPACE','THING','EVENT','ACTION','AGENCY','RULE','VALUE','CONTEXT','CLAIM')
FACETS = ('IdentityLifecycle','ScopeContext','EpistemicsProvenance','AuthorityHumanBoundary',
          'EffectsSafety','DependencyValidity','ResourceTermination','PrivacyRetention',
          'AuditExplanation','RecoveryEvolution')
FORMS = ('CONSTRUCT','CONTRACT','STATE','RELATION','PROCESS','RULE','PROJECTION')


def digest(value):
    """Research encoding, explicitly NOT GardenCanonicalEncoding/v3."""
    return hashlib.sha256(json.dumps(value, sort_keys=True, ensure_ascii=False,
        separators=(',', ':'), allow_nan=False).encode()).hexdigest()


def source_span(path, first_line, last_line):
    raw = (ROOT / path).read_bytes()
    lines = raw.splitlines(keepends=True)
    if not 1 <= first_line <= last_line <= len(lines):
        raise ValueError('invalid source span')
    start, end = sum(map(len, lines[:first_line-1])), sum(map(len, lines[:last_line]))
    return dict(path=path, first_line=first_line, last_line=last_line, start_byte=start,
        end_byte=end, source_sha256=hashlib.sha256(raw).hexdigest(),
        source_span_sha256=hashlib.sha256(raw[start:end]).hexdigest())


def signatures():
    return json.loads((HERE/'GCSC_RELATION_SIGNATURE_CANDIDATE.json').read_text())


def classify_triple(source, relation, target, registry=None):
    registry = signatures() if registry is None else registry
    if source not in OBJECTS or target not in OBJECTS:
        return 'UNRESOLVED'
    sig = registry.get('signatures',{}).get(relation)
    if sig is None:
        return 'UNRESOLVED'
    return ('SIGNATURE_PLAUSIBLE' if source in sig['source'] and target in sig['target']
            else 'INVALID_TYPE')


def l0_inventory():
    registry = signatures()
    counts = Counter(classify_triple(s,r,t,registry)
        for s,r,t in itertools.product(OBJECTS,registry['signatures'],OBJECTS))
    return dict(raw=sum(counts.values()), classifications=dict(counts),
        denominator='RAW retained; plausible denominator separately reported, no coverage claim',
        full_sal='UNKNOWN: complete finite interpretation/join registries absent',
        registry_sha256=digest(registry), placeholder='PROCESS_PLACEHOLDER excluded, not a Core Object')


def sal(s, registry=None):
    """Product diagnostics. Research interpretation cannot become semantic PASS."""
    registry = signatures() if registry is None else registry
    out = dict(structural_status='VALID', completeness_status='COMPLETE_WITHIN_PROFILE',
        join_status='NOT_EVALUATED', coherence_status='UNKNOWN',
        interpretation_status='RESEARCH_PROFILE_ONLY', diagnostics=[], missing_bindings=[])
    objects = s.get('objects', [])
    types = {o.get('id'):o.get('type') for o in objects if isinstance(o,dict) and o.get('id')}
    structure = set()
    if len(types) != len(objects):
        structure.add('INVALID_TYPE'); out['diagnostics'].append('duplicate object ID')
    for obj in objects:
        if not isinstance(obj,dict) or not obj.get('id') or obj.get('type') not in OBJECTS:
            structure.add('UNRESOLVED'); out['diagnostics'].append('unresolved object binding:'+str(obj))
    for edge in s.get('relations', []):
        status = classify_triple(types.get(edge.get('source')),edge.get('relation'),types.get(edge.get('target')),registry)
        if status != 'SIGNATURE_PLAUSIBLE':
            structure.add(status); out['diagnostics'].append(status+':'+str(edge))
        if edge.get('relation') in ('owns','delegates','acts','values') and types.get(edge.get('source')) != 'AGENCY':
            out['diagnostics'].append('PROHIBITED_PHYSICAL_ANTHROPOMORPHISM')
    out['structural_status'] = '|'.join(sorted(structure)) if structure else 'VALID'
    for facet in FACETS:
        b = s.get('facets',{}).get(facet)
        if not b or b.get('status') not in ('APPLICABLE','NOT_APPLICABLE','UNKNOWN') or not b.get('reason'):
            out['missing_bindings'].append(facet)
        elif b['status']=='UNKNOWN':
            out['missing_bindings'].append('UNKNOWN_FACET:'+facet)
    for field in ('assumptions','source_refs','constraints'):
        if not s.get(field): out['missing_bindings'].append(field)
    for port in s.get('inputs',[])+s.get('outputs',[]):
        if not port.get('unit'): out['missing_bindings'].append('unit:'+port.get('name','?'))
    out['completion_frontier'] = sorted(set(s.get('unresolved_state',[])+out['missing_bindings']))
    if out['completion_frontier']: out['completeness_status']='CONTEXT_REQUIRED'
    return out


def derive_obligations(seed):
    """Instantiate from explicit source laws, never candidate number/title keywords."""
    laws = {x['id']:x for x in seed['laws']}
    out=[]
    for s in seed['situations']:
        for key in s['constraints']:
            law=laws.get(key,{})
            out.append(dict(id=s['id']+'::'+key, owner=key, situation=s['id'],
                law_type=law.get('type','UNKNOWN'), equation=law.get('equation'),
                domain=law.get('domain'), assumptions=s['assumptions']+law.get('assumptions',[]),
                status='GENERATED_CANDIDATE' if law else 'UNKNOWN',
                applicability='REQUIRES_DOMAIN_VERIFICATION', empirical='NOT_MEASURED',
                source_refs=law.get('source_refs',[]), admission=ADMISSION))
    return out


def port_map(situation, direction):
    """Physical flow ports and explicitly owned state ports remain distinct data,
    but both may satisfy typed transfers. Conflicting dimensions fail closed.
    """
    rows=situation.get('inputs' if direction=='input' else 'outputs',[])+[
        p for p in situation.get('state_ports',[]) if p.get('direction')==direction]
    result={}
    for p in rows:
        name,unit=p['name'],p['unit']
        if name in result and result[name]!=unit: result[name]='CONFLICTING_UNITS'
        else: result[name]=unit
    return result


def audit_transitions(seed):
    """Units require exact matching; nonidentical units need an explicit adapter.
    Structural binding does not establish numerical conservation or novelty.
    """
    nodes={s['id']:s for s in seed['situations']}; out=[]
    for e in seed['transitions']:
        a,b=nodes.get(e['source']),nodes.get(e['target'])
        item=dict(id=e['id'],source=e['source'],target=e['target'],diagnostics=[],
            constraints=e.get('constraints',[]),physics_status='UNKNOWN_WITHOUT_QUANTITATIVE_STATE',
            novelty='NOT_ASSESSED_INTERFACE_AUDIT_ONLY',admission=ADMISSION)
        if a is None or b is None: item['diagnostics'].append('UNKNOWN_ENDPOINT')
        else:
            offered=port_map(a,'output'); needed=port_map(b,'input')
            sent=set(e.get('transfers',[])); required=set(e.get('required_transfers',[]))
            for v in sorted(required-sent): item['diagnostics'].append('MISSING_TRANSFER:'+v)
            for v in sorted(sent):
                if v not in offered or v not in needed: item['diagnostics'].append('UNBOUND_TRANSFER:'+v)
                elif offered[v] != needed[v] or 'CONFLICTING_UNITS' in (offered[v],needed[v]):
                    item['diagnostics'].append('UNIT_ADAPTER_REQUIRED:'+v)
            if not e.get('assumptions'): item['diagnostics'].append('CONTEXT_REQUIRED')
        item['contract_status']='UNRESOLVED' if item['diagnostics'] else 'STRUCTURALLY_BOUND'
        out.append(item)
    return out


def audit_combinations(seed, limit=1000):
    """Connected incoming pairs, with a finite named join witness (same consumer).
    These are structural pairs, not admitted full SAL multi-edge motifs.
    """
    if type(limit) is not int or limit<0: raise ValueError('invalid motif budget')
    incoming={s['id']:[] for s in seed['situations']}
    for e in seed['transitions']:
        if e['target'] in incoming: incoming[e['target']].append(e)
    motifs=[]; total=sum(len(v)*(len(v)-1)//2 for v in incoming.values())
    for target,edges in sorted(incoming.items()):
        for a,b in itertools.combinations(edges,2):
            if len(motifs)>=limit:
                return dict(status='INCOMPLETE',raw=total,checked=len(motifs),motifs=motifs)
            overlap=sorted(set(a.get('transfers',[])) & set(b.get('transfers',[])))
            motifs.append(dict(target=target,edges=[a['id'],b['id']],
                join_witness='SAME_DECLARED_CONSUMER',overlap=overlap,
                status='AMBIGUOUS_SHARED_BINDING' if overlap else 'JOINT_PHYSICS_UNKNOWN',
                obligation='bind common context/time and distinguish additive flows from duplicate state observations'))
    return dict(status='BOUNDED_ENUMERATION',raw=total,checked=len(motifs),motifs=motifs)


def audit_consumer_inputs(seed):
    """Detect omitted required ports even if edge annotations omit them too.
    An external binding needs an explicit declared source; no name-only default.
    These are documentation/context gaps, never automatically new science.
    """
    by_id={s['id']:s for s in seed['situations']}; incoming={k:set() for k in by_id}
    for e in seed['transitions']:
        source=by_id.get(e['source']); target=by_id.get(e['target'])
        if source is None or target is None: continue
        outputs=port_map(source,'output'); inputs=port_map(target,'input')
        for name in e.get('transfers',[]):
            if name in outputs and name in inputs and outputs[name]==inputs[name] and outputs[name]!='CONFLICTING_UNITS':
                incoming[e['target']].add(name)
    out=[]
    for s in seed['situations']:
        sources={p['id'] for p in seed.get('sources',[])}
        units=port_map(s,'input')
        external={p['name'] for p in s.get('external_bindings',[]) if p.get('source_ref') in sources
            and p.get('name') in units and p.get('unit')==units[p['name']]}
        required=set(units)
        out.append(dict(situation=s['id'],unbound_inputs=sorted(required-incoming[s['id']]-external),
            interpretation='UNKNOWN interface/context provenance; may be exogenous or outside map',admission=ADMISSION))
    return out


def bounded_dependency_closure(seed,max_rounds=64):
    """Propagate origin-qualified obligations, not universal physical applicability."""
    if type(max_rounds) is not int or not 0<=max_rounds<=64: raise ValueError('invalid round budget')
    closure={s['id']:{(s['id'],x) for x in s['constraints']} for s in seed['situations']}
    trace=[sum(map(len,closure.values()))]
    for i in range(max_rounds):
        new={k:set(v) for k,v in closure.items()}
        for e in seed['transitions']:
            a,b=e['source'],e['target']
            if a not in closure or b not in closure: return dict(status='UNKNOWN',trace=trace)
            new[b].update(closure[a])
        trace.append(sum(map(len,new.values())))
        if new==closure:
            return dict(status='BOUNDED_FIXED_POINT',iterations=i+1,trace=trace,
                obligations={k:sorted(v) for k,v in sorted(new.items())},physical_completeness='UNKNOWN')
        closure=new
    return dict(status='INCOMPLETE',iterations=max_rounds,trace=trace,
        continuation_frontier={k:sorted(v) for k,v in sorted(closure.items())})


def matrix(rows):
    if not rows or not rows[0] or any(len(r)!=len(rows[0]) for r in rows): raise ValueError('nonempty rectangular matrix required')
    return [[Fraction(str(x)) for x in r] for r in rows]


def nullspace(rows):
    """Exact rational elimination; no floating rank tolerance."""
    a=matrix(rows); m,n,r=len(a),len(a[0]),0; pivots=[]
    for c in range(n):
        p=next((i for i in range(r,m) if a[i][c]),None)
        if p is None: continue
        a[r],a[p]=a[p],a[r]; f=a[r][c]; a[r]=[v/f for v in a[r]]
        for i in range(m):
            if i!=r and a[i][c]:
                f=a[i][c]; a[i]=[x-f*y for x,y in zip(a[i],a[r])]
        pivots.append(c); r+=1
        if r==m: break
    vectors=[]
    for free in (c for c in range(n) if c not in pivots):
        v=[Fraction(0)]*n; v[free]=Fraction(1)
        for i,c in enumerate(pivots): v[c]=-a[i][free]
        vectors.append(v)
    return vectors


def dot(a,b):
    if len(a)!=len(b): raise ValueError('dot dimension mismatch')
    return sum(x*y for x,y in zip(a,b))


def projection_witness(observations,kernel):
    """Equal-observation, unequal-response witness on finite nonnegative cone.
    Spectral current squared [A^2], kernel [W/A^2], response [W].
    Known linear algebra; does not discover arbitrary nonlinear physics.
    """
    rows=matrix(observations); k=[Fraction(str(x)) for x in kernel]
    if len(k)!=len(rows[0]): raise ValueError('kernel dimension mismatch')
    for d in nullspace(rows):
        if dot(k,d):
            scale=Fraction(1,2)/max(map(abs,d))
            x1=[1+scale*v for v in d]; x2=[1-scale*v for v in d]
            y1=[dot(a,x1) for a in rows]; y2=[dot(a,x2) for a in rows]
            p1,p2=dot(k,x1),dot(k,x2)
            assert y1==y2 and min(x1+x2)>=0 and p1!=p2
            return dict(status='PROJECTION_NOT_CLOSED',x1=list(map(str,x1)),x2=list(map(str,x2)),
                observations=list(map(str,y1)),response1=str(p1),response2=str(p2),
                separating_threshold=str((p1+p2)/2),novelty='NOT_ESTABLISHED',admission=ADMISSION)
    return dict(status='CLOSED_FOR_DECLARED_LINEAR_RESPONSE',
        proof_scope='exact rational nullspace; declared finite nonnegative cone',admission=ADMISSION)


def synthesize_interface(observations,consumers,max_additions=8):
    """Basis extension; minimum independent rows, NOT cheapest physical sensing."""
    if type(max_additions) is not int or max_additions<0: raise ValueError('invalid addition budget')
    rows=[list(r) for r in observations]; additions=[]; witnesses=[]; unresolved=[]
    for owner,kernel in consumers:
        w=projection_witness(rows,kernel)
        if w['status']=='PROJECTION_NOT_CLOSED':
            witnesses.append(dict(owner=owner,witness=w))
            if len(additions)>=max_additions: unresolved.append(owner)
            else: rows.append(list(kernel)); additions.append(dict(owner=owner,coefficients=list(map(str,kernel))))
    return dict(status='INCOMPLETE' if unresolved else 'CLOSED_FOR_DECLARED_CONSUMERS',
        additions=additions,witnesses=witnesses,completion_frontier=unresolved,rows=rows,
        invalidators=['consumer kernel','spectral support','units','time window','measurement model'],admission=ADMISSION)


def linear_cycle():
    h=[1,5,7,11,13]; a=[[1]*5,[1,0,0,0,0]]; k=[1+x*x for x in h]
    synthesis=synthesize_interface(a,[('transformer-loss',k)])
    # Deliberate model-class perturbation; NOT a calibrated device.
    changed=[v+(3 if x==13 else 0) for v,x in zip(k,h)]
    return dict(harmonics=h,original=projection_witness(a,k),synthesis=synthesis,
        repaired=projection_witness(synthesis['rows'],k),
        changed_kernel=projection_witness(synthesis['rows'],changed),
        repaired_again=synthesize_interface(synthesis['rows'],[('changed-consumer',changed)]),
        provenance='curated known-physics test, not blind discovery')


def necessity_and_decision_cycle():
    """Test the claimed prerequisite 'always retrieve full historical spectrum'.
    This is a bounded counterexample to necessity, not universal permission to
    discard waveforms. The strong conventional kernel-aware method ties.
    """
    a=[[1,1],[1,0]]; x=[Fraction(1,4),Fraction(1,2)]; k=[2,6]
    y=[dot(r,x) for r in a]; b=moment_bounds(a,y,k)
    threshold=4
    return dict(prerequisite='retrieve full historical spectrum at decision time',
        prerequisite_used=False,retained_measurements=list(map(str,y)),
        outcome=interval_decision(b,threshold),full_state_feasible=dot(k,x)<=threshold,
        constraints=['nonnegative bounded spectrum','exact declared kernel','same time and aggregate scope'],
        status='BOUNDED_COUNTEREXAMPLE_TO_NECESSITY',
        limitations='sensing originally needed; model/profile changes reopen sufficiency; not a blind TRIZ comparison',
        decision_sufficiency='exact for declared scalar constraint; different objectives may require more state',admission=ADMISSION)


def solve_square(a, b):
    """Exact square solve; singular basis returns None."""
    a=matrix(a); n=len(a)
    if len(a[0])!=n or len(b)!=n: raise ValueError('square dimensions required')
    a=[row+[Fraction(str(v))] for row,v in zip(a,b)]
    for c in range(n):
        p=next((r for r in range(c,n) if a[r][c]),None)
        if p is None: return None
        a[c],a[p]=a[p],a[c]; f=a[c][c]; a[c]=[v/f for v in a[c]]
        for r in range(n):
            if r!=c and a[r][c]:
                f=a[r][c]; a[r]=[v-f*w for v,w in zip(a[r],a[c])]
    return [row[-1] for row in a]


def moment_bounds(observations, values, kernel, max_bases=10000):
    """Exact small-profile LP by vertex enumeration with primal/dual checks.

    min/max k.x subject to Ax=y,x>=0. Requires an all-one row (finite total
    energy) and independent observation rows. Not a general LP solver.
    Rational coefficients certify the supplied model, not uncertain reality.
    """
    a=matrix(observations); m,n=len(a),len(a[0])
    y=[Fraction(str(v)) for v in values]; k=[Fraction(str(v)) for v in kernel]
    if len(y)!=m or len(k)!=n: raise ValueError('LP dimension mismatch')
    if type(max_bases) is not int or max_bases<0: raise ValueError('invalid LP budget')
    if [Fraction(1)]*n not in a:
        return dict(status='UNKNOWN',reason='bounded total-energy row absent')
    if m>n or len(nullspace(list(map(list,zip(*a)))))>0:
        return dict(status='UNKNOWN',reason='independent-row profile required')
    total=math.comb(n,m)
    if total>max_bases:
        return dict(status='INCOMPLETE',required_bases=total,budget=max_bases)
    vertices=[]; upper_certificates=[]; lower_certificates=[]
    for support in itertools.combinations(range(n),m):
        basis=[[row[i] for i in support] for row in a]
        xb=solve_square(basis,y)
        if xb is None or min(xb)<0: continue
        x=[Fraction(0)]*n
        for j,v in zip(support,xb): x[j]=v
        assert [dot(row,x) for row in a]==y
        vertices.append((dot(k,x),x))
        dual=solve_square(list(map(list,zip(*basis))),[k[i] for i in support])
        lhs=[dot(dual,col) for col in zip(*a)]
        if all(v>=w for v,w in zip(lhs,k)): upper_certificates.append((dot(dual,y),dual))
        if all(v<=w for v,w in zip(lhs,k)): lower_certificates.append((dot(dual,y),dual))
    if not vertices:
        return dict(status='INFEASIBLE',checked_bases=total,reason='empty bounded measurement polytope')
    lo,xlo=min(vertices,key=lambda p:p[0]); hi,xhi=max(vertices,key=lambda p:p[0])
    lowdual=next((d for v,d in lower_certificates if v==lo),None)
    highdual=next((d for v,d in upper_certificates if v==hi),None)
    if lowdual is None or highdual is None:
        return dict(status='UNKNOWN',reason='missing matching dual certificate')
    return dict(status='CERTIFIED_FOR_SUPPLIED_RATIONAL_MODEL',lower=str(lo),upper=str(hi),
        lower_witness=list(map(str,xlo)),upper_witness=list(map(str,xhi)),
        lower_dual=list(map(str,lowdual)),upper_dual=list(map(str,highdual)),
        checked_bases=total,total_energy_row=a.index([Fraction(1)]*n),nominal_y=list(map(str,y)),
        input_sha256=digest({'A':[[str(v) for v in r] for r in a],
            'y':list(map(str,y)),'k':list(map(str,k))}),admission=ADMISSION)


def uncertain_bounds(bounds, observation_lower, observation_upper, coefficient_error=0):
    """Outer bounds from feasible LP duals, for intervals around nominal y.
    Error bound is uniform in the kernel [W per unit energy]; requires known
    total-energy row. No inference of that bound from model agreement.
    Caller must bind the exact mathematical profile; see qualified_decision.
    """
    if bounds.get('status')!='CERTIFIED_FOR_SUPPLIED_RATIONAL_MODEL': return dict(status='UNKNOWN')
    lo=[Fraction(str(v)) for v in observation_lower]; hi=[Fraction(str(v)) for v in observation_upper]
    lowdual=list(map(Fraction,bounds['lower_dual'])); highdual=list(map(Fraction,bounds['upper_dual']))
    eps=Fraction(str(coefficient_error))
    total_row=bounds['total_energy_row']; nominal=list(map(Fraction,bounds['nominal_y']))
    if len(lo)!=len(lowdual) or len(hi)!=len(lo) or eps<0 or any(a>b for a,b in zip(lo,hi)) or hi[total_row]<0:
        return dict(status='UNKNOWN',reason='invalid uncertainty profile')
    if any(not a<=v<=b for a,v,b in zip(lo,nominal,hi)):
        return dict(status='UNKNOWN',reason='nominal feasible witness outside measurement intervals')
    lower=sum(v*(a if v>=0 else b) for v,a,b in zip(lowdual,lo,hi))-eps*hi[total_row]
    upper=sum(v*(b if v>=0 else a) for v,a,b in zip(highdual,lo,hi))+eps*hi[total_row]
    return dict(status='CERTIFIED_OUTER_MODEL_BOUND',lower=str(lower),upper=str(upper),
        scope='provided finite support, interval measurements and externally justified uniform kernel error')


def qualified_decision(packet, expected_profile, limit):
    """Unknown profile/phase aggregation cannot be silently accepted."""
    fields=('kernel_id','harmonics','units','window_id','aggregate_terminal_scope')
    if any(k not in packet or k not in expected_profile for k in fields): return 'UNKNOWN'
    if any(packet[k]!=expected_profile[k] for k in fields): return 'NEEDS_REVALIDATION'
    if packet['aggregate_terminal_scope'] is not True: return 'UNKNOWN'
    math_input=expected_profile.get('mathematics')
    if not isinstance(math_input,dict): return 'UNKNOWN'
    try:
        valid=verify_bounds_certificate(packet.get('bounds',{}),math_input['A'],math_input['y'],math_input['k'])
    except (KeyError,ValueError,TypeError,ZeroDivisionError):
        return 'UNKNOWN'
    if not valid: return 'UNKNOWN'
    return interval_decision(packet.get('bounds',{'status':'UNKNOWN'}),limit)


def verify_bounds_certificate(bounds, observations, values, kernel):
    """Validate exact primal/dual witnesses against trusted mathematical input.
    Hash equality alone is never sufficient, nor is the claimed status label.
    """
    if bounds.get('status')!='CERTIFIED_FOR_SUPPLIED_RATIONAL_MODEL': return False
    a=matrix(observations); y=list(map(lambda v:Fraction(str(v)),values)); k=list(map(lambda v:Fraction(str(v)),kernel))
    if len(y)!=len(a) or len(k)!=len(a[0]): return False
    expected=digest({'A':[[str(v) for v in r] for r in a],'y':list(map(str,y)),'k':list(map(str,k))})
    if bounds.get('input_sha256')!=expected: return False
    for side,sign in [('lower',-1),('upper',1)]:
        x=list(map(Fraction,bounds[side+'_witness'])); dual=list(map(Fraction,bounds[side+'_dual']))
        if len(x)!=len(k) or len(dual)!=len(y) or min(x)<0: return False
        if [dot(row,x) for row in a]!=y: return False
        if any(sign*(dot(dual,col)-v)<0 for col,v in zip(zip(*a),k)): return False
        target=Fraction(bounds[side])
        if dot(dual,y)!=target or dot(k,x)!=target: return False
    return Fraction(bounds['lower'])<=Fraction(bounds['upper'])


def interval_decision(bounds, limit):
    if bounds['status']!='CERTIFIED_FOR_SUPPLIED_RATIONAL_MODEL': return 'UNKNOWN'
    limit=Fraction(str(limit))
    if Fraction(bounds['upper'])<=limit: return 'MODEL_FEASIBLE'
    if Fraction(bounds['lower'])>limit: return 'MODEL_INFEASIBLE'
    return 'NEED_ADDITIONAL_MEASUREMENT'


def revalidation_cycle():
    """Frozen synthetic workload; strong conventional LP must tie exactly."""
    h=[1,5,7,11,13,17,19,23]; old=[3000+10*i*i for i in h]
    new=[v+(120 if i==13 else 0) for i,v in zip(h,old)]
    a=[[1]*8,[1]+[0]*7,old]; rng=random.Random(20261009)
    counts=Counter(); rows=[]; start=time.perf_counter()
    for case in range(100):
        x=[Fraction(rng.randint(30,150),100)]+[Fraction(rng.randint(0,15),1000) for _ in h[1:]]
        y=[dot(r,x) for r in a]; actual=dot(new,x)
        b=moment_bounds(a,y,new); decision=interval_decision(b,4200)
        assert b['status']=='CERTIFIED_FOR_SUPPLIED_RATIONAL_MODEL'
        assert Fraction(b['lower'])<=actual<=Fraction(b['upper'])
        assert decision!='MODEL_FEASIBLE' or actual<=4200
        assert decision!='MODEL_INFEASIBLE' or actual>4200
        counts[decision]+=1
        rows.append(dict(case=case,decision=decision,actual=str(actual),lower=b['lower'],upper=b['upper']))
    seconds=time.perf_counter()-start
    # Adversarial threshold stress after the fixed workload: explicitly separate.
    # A witness pair with shared measurements forces a nonempty ambiguous case.
    witness=projection_witness(a,new)
    wx=list(map(Fraction,witness['x1'])); wy=[dot(r,wx) for r in a]
    wb=moment_bounds(a,wy,new)
    boundary=interval_decision(wb,witness['separating_threshold'])
    assert boundary=='NEED_ADDITIONAL_MEASUREMENT'
    needed=counts['NEED_ADDITIONAL_MEASUREMENT']
    return dict(profile='100 fixed synthetic exact-rational spectra, 8 bins',
        decisions=dict(counts),incorrect_certified_decisions=0,
        results_sha256=digest(rows),local_runtime_seconds=seconds,
        adversarial_boundary=dict(status=boundary,lower=wb['lower'],upper=wb['upper'],
            threshold=witness['separating_threshold'],separate_from_frozen_100=True),
        marginal_payload_bytes=dict(interval_plus_scalar_fallback=needed*32,
            always_scalar_query=100*32,always_full_spectrum=100*88,
            conventional_same_LP=needed*32),
        payload_assumptions='ILLUSTRATIVE: old 3 summaries already retained; shared update cost excluded equally; 8-byte values + 24-byte response header; exact-rational proof not yet qualified for quantized wire encoding',
        economics='UNKNOWN: bytes alone exclude LP compute, retention, protocol, sensing, uncertainty and deferred decisions',
        method_advantage='ZERO versus conventional identical kernel-aware LP',
        novelty='NOT_ESTABLISHED; known moment LP/dual certificate mathematics',admission=ADMISSION)


def run(seed=None):
    if seed is None:
        from electricity_seed import build_seed
        seed=build_seed()
    ids=[s['id'] for s in seed['situations']]
    if len(ids)!=len(set(ids)): raise ValueError('duplicate situation ID')
    return dict(profile=PROFILE,admission=ADMISSION,seed_sha256=digest(seed),
        counts=dict(stages=len(seed['stages']),situations=len(ids),transitions=len(seed['transitions']),
            laws=len(seed['laws']),instantiated_obligations=len(derive_obligations(seed))),
        coverage=dict(stages=sorted({s['stage'] for s in seed['situations']}),
            reality='UNKNOWN: bounded curated map',full_garden_conformance='NOT_ESTABLISHED',l0=l0_inventory()),
        sal={s['id']:sal(s) for s in seed['situations']},transition_audit=audit_transitions(seed),
        consumer_audit=audit_consumer_inputs(seed),
        combinations=audit_combinations(seed),dependency_closure=bounded_dependency_closure(seed),
        linear_cycle=linear_cycle(),necessity_and_decision=necessity_and_decision_cycle(),
        scientific_gates=dict(empirical='NOT_TESTED',novelty='NOT_ESTABLISHED',
            economics='NOT_MEASURED',blind_comparison='NOT_RUN',independent_family_review='NOT_RUN',tree_core='UNRESOLVED'))


def text_report(result,seed=None,details=False):
    lines=['SITUATION-TO-INVARIANT CLOSURE — SIC-0.1',ADMISSION,
        'Seed SHA256: '+result['seed_sha256'],'COUNTS: '+str(result['counts']),
        'Reality coverage UNKNOWN; full GSL/SAL not implemented.',
        'L0 candidate signatures: '+str(result['coverage']['l0']),
        'Dependency closure: '+str({k:v for k,v in result['dependency_closure'].items() if k not in ('obligations','continuation_frontier')}),
        'Connected incoming pairs: '+str({k:v for k,v in result['combinations'].items() if k!='motifs'}),
        'Scientific gates: '+str(result['scientific_gates']),
        'Linear projection cycle: '+json.dumps(result['linear_cycle'],ensure_ascii=False)]
    lines.append('Transition diagnostics: '+str(dict(Counter(d for x in result['transition_audit'] for d in x['diagnostics']))))
    if details and seed:
        lines+=['','SITUATION GRAPH — curated physical branches and lifecycle dependencies']
        for s in seed['situations']:
            lines.append(f"{s['id']} | stage {s['stage']} | {s['name']} | {s.get('branch','')}")
            for label,key in [('Inputs','inputs'),('Outputs','outputs')]:
                lines.append('  '+label+': '+'; '.join(p['name']+' ['+p['unit']+']' for p in s[key]))
            lines.append('  Rules: '+', '.join(s['constraints']))
            lines.append('  Assumptions: '+'; '.join(s['assumptions']))
            lines.append('  UNKNOWN: '+'; '.join(s['unresolved_state']))
        lines+=['','INVARIANT REGISTER']
        lines.extend(json.dumps(x,ensure_ascii=False,sort_keys=True) for x in seed['laws'])
        lines+=['','TRANSITION AUDIT']
        lines.extend(x['id']+' '+x['source']+' -> '+x['target']+' | '+x['contract_status']+' | '+
            ('; '.join(x['diagnostics']) or 'binding only; quantitative physics UNKNOWN') for x in result['transition_audit'])
    return '\n'.join(lines)+'\n'


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--details',action='store_true')
    p.add_argument('--experiments',action='store_true',help='run E1 known-physics and E2 interval-revalidation cycles')
    args=p.parse_args()
    from electricity_seed import build_seed
    seed=build_seed(); print(text_report(run(seed),seed,args.details),end='')
    if args.experiments:
        import electricity_experiment
        print('E1 transformer experiment:')
        print(json.dumps(electricity_experiment.run(),ensure_ascii=False,sort_keys=True))
        print('E2 finite-profile revalidation:')
        print(json.dumps(revalidation_cycle(),ensure_ascii=False,sort_keys=True))


if __name__=='__main__': main()
