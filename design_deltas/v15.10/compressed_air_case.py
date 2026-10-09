#!/usr/bin/env python3
"""Retrospective electricity-end-use case and bounded counterfactual calculation.

No plant control, full TREE_CORE implementation, discovery or field validation.
Run directly for a deterministic plain-text map, audit and experiment record.
The numerical two-compressor example is synthetic, NOT a Visteon reconstruction.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib

from electricity_closure import (FACETS, sal, derive_obligations,
    audit_transitions, audit_consumer_inputs, audit_combinations, digest)

HERE = Path(__file__).resolve().parent
STATUS = 'NONCANONICAL_RESEARCH; RETROSPECTIVE_KNOWN_ENGINEERING'
SOURCES = {
    'DOE-VISTEON': 'https://www.compressedairchallenge.org/data/sites/1/media/library/casestudies/Visteon-CompAir-Steel.pdf',
    'DOE-AWHC': 'https://www1.eere.energy.gov/manufacturing/tech_assistance/pdfs/bp_cs_americanwaterheater.pdf',
    'DOE-SOURCEBOOK': 'https://www1.eere.energy.gov/manufacturing/tech_assistance/pdfs/compressed_air_sourcebook.pdf',
    'DOE-AIRMASTER': 'https://www.energy.gov/sites/prod/files/2014/04/f15/airmaster_user_manual.pdf',
    'AUTHOR-MODEL': 'This file: explicit synthetic equation contracts; no field parameters',
}

# Each row is a physically distinct situation, not a Cartesian node template.
# A generic audit model; actual Visteon P&ID, dryer/receiver design and historian
# were not supplied. Maintenance/control events are distinct from physical flow.
ROWS = [
 ('CA01','supply','Motor and compressor convert electricity to compressed air',
  'grid_kw,inlet_kg_s,mode_command','hot_air_kg_s,compressor_kw,actual_mode',
  'ENERGY,MASS,MODE_POWER','Compressor maps and restart constraints UNKNOWN'),
 ('CA02','supply','Condition air and remove heat and condensate',
  'hot_air_kg_s','clean_air_kg_s,dewpoint_K,treatment_kw',
  'MASS,ENERGY,QUALITY','Actual dryer type, purge and drain flows UNKNOWN'),
 ('CA03','supply','Receiver stores mass and energy between demand events',
  'clean_air_kg_s,network_draw_kg_s','header_Pa,receiver_K,stored_kg',
  'MASS,ENERGY,INVENTORY','Receiver volume, heat exchange and initial state UNKNOWN'),
 ('CA04','delivery','Pipe network supplies useful and parasitic branches',
  'header_Pa,dewpoint_K,demand_kg_s,leak_kg_s','network_draw_kg_s,terminal_Pa,terminal_dewpoint_K',
  'MASS,PRESSURE,QUALITY','Spatial pressure losses and terminal requirements UNKNOWN'),
 ('CA05','delivery','End use performs production during an active cycle',
  'terminal_Pa,terminal_dewpoint_K,production_schedule','demand_kg_s,good_units_s,production_active,quality_record',
  'PRESSURE,QUALITY,SERVICE','End-use flow/quality envelopes and product mix UNKNOWN'),
 ('CA06','delivery','Leaks and idle branches discharge air without useful output',
  'header_Pa,leak_conductance,isolation_command','leak_kg_s',
  'MASS,LEAK','Remaining legitimate idle demand must be separated from leakage'),
 ('CA07','control','Sensors sample electrical and pneumatic state',
  'compressor_kw,actual_mode,treatment_kw,header_Pa,receiver_K,stored_kg,terminal_Pa,terminal_dewpoint_K,quality_record,leak_kg_s,good_units_s',
  'observed_state','MEASUREMENT','Meter calibration, time alignment and uncertainty UNKNOWN'),
 ('CA08','control','Sequencer selects supply modes for the next interval',
  'observed_state,operating_envelope','mode_command',
  'MASS,PRESSURE,DISPATCH','Capacity reserve, starts/hour and response limits UNKNOWN'),
 ('CA09','control','Idle-production event changes branch isolation',
  'production_active,isolation_permit','isolation_command',
  'SERVICE,DISPATCH','Stored-pressure and process interlocks require plant authorization'),
 ('CA10','recovery','Inspection distinguishes repairable leaks from required demand',
  'observed_state,recurrence_flag','repair_targets',
  'MEASUREMENT,SERVICE','Off-shift flow alone does not identify each defect'),
 ('CA11','recovery','Authorized maintenance repairs a located defect',
  'repair_targets,maintenance_permit','leak_conductance,repair_event',
  'SERVICE,MEASUREMENT','Repair persistence and downtime costs UNKNOWN'),
 ('CA12','recovery','Compare matched service and storage before accepting savings',
  'observed_state,repair_event,tariff,capital_and_maintenance','recurrence_flag,net_value',
  'INVENTORY,SERVICE,VALUE,MEASUREMENT','Raw interval data unavailable; Visteon project cost UNKNOWN (AWHC reports cost)'),
]

UNITS = dict(grid_kw='kW', inlet_kg_s='kg/s', mode_command='1',
 hot_air_kg_s='kg/s', compressor_kw='kW', actual_mode='1', clean_air_kg_s='kg/s',
 dewpoint_K='K', treatment_kw='kW', network_draw_kg_s='kg/s', header_Pa='Pa',
 receiver_K='K', stored_kg='kg', demand_kg_s='kg/s', leak_kg_s='kg/s',
 terminal_Pa='Pa', terminal_dewpoint_K='K', production_schedule='1',
 good_units_s='1/s', production_active='1', leak_conductance='kg/(s*Pa)',
 isolation_command='1', observed_state='TYPED_RECORD_V1', operating_envelope='TYPED_RECORD_V1',
 isolation_permit='1', recurrence_flag='1', repair_targets='TYPED_RECORD_V1',
 maintenance_permit='1', repair_event='TYPED_RECORD_V1', tariff='USD/kWh',
 capital_and_maintenance='TYPED_RECORD_V1', quality_record='TYPED_RECORD_V1', net_value='USD/year')

# These are constitutive/engineering contracts unless explicitly exact balances.
LAW_ROWS = [
 ('MASS','EXACT_CLASSICAL_BALANCE','dm/dt = sum(mdot_in)-sum(mdot_out)',
  'kg/s on both sides; all leaks, drains, purge, blow-off and storage included'),
 ('ENERGY','EXACT_CLASSICAL_BALANCE','dE_cv/dt = Qdot + Wdot_in + sum(mdot*(h+v^2/2+g*z))_in-out',
  'W on both sides; stored/internal, kinetic, potential and material-flow energy included'),
 ('INVENTORY','CONSTITUTIVE_AND_COMPARISON','m=P_abs*V/(R*T); matched tests require equal initial/final m,U',
  'Ideal gas, uniform temperature; Pa*m^3/(J/(kg*K)*K)=kg; real-gas correction if material'),
 ('PRESSURE','ENGINEERING_CONSTRAINT','p_terminal(t) >= p_required(t), within upper rated limits',
  'Pa; constraints at each consumer across transient events, not just mean header'),
 ('QUALITY','ENGINEERING_CONSTRAINT','dewpoint_terminal <= specified_limit; contamination within specification',
  'K; pressure-dew-point definition, operating pressure and product requirements bound'),
 ('MODE_POWER','EMPIRICAL_MODEL','P=n*P_u+(P_l-P_u)*q/q_max; 0<=q<=n*q_max',
  'kW; identical ideal load/unload units, cycling losses ignored; measured maps supersede'),
 ('LEAK','SCOPED_CONSTITUTIVE','mdot_leak=C(T,gas,orifice)*P_abs',
  'kg/s; choked ideal-gas branch at fixed temperature only, not universal leak law'),
 ('DISPATCH','ENGINEERING_CONSTRAINT','available_supply+permitted_storage_draw >= demand+losses',
  'kg/s; recovery, reserve, pressure, starts and failure response are separate limits'),
 ('SERVICE','ENGINEERING_CONSTRAINT','delivered output, quality and reliability must meet the same contract',
  'No dollar saving from reducing required service or omitting repair/quality costs'),
 ('MEASUREMENT','EVIDENCE_CONSTRAINT','align clocks, calibrate meters, retain uncertainty and before/after context',
  'UNKNOWN measurements cannot establish savings or cause physical actuation'),
 ('VALUE','ECONOMIC_CONDITION','net=avoided_total_bill+avoided_maintenance-added_cost-annualized_capital',
  'USD/year; equal service and inventory; no double counting energy and bill savings'),
]

def split(s):
    return s.split(',')

def build_case():
    facets = {
      'IdentityLifecycle':'Stable CA identities; repair and recurrence retain history',
      'ScopeContext':'Electricity end use; physical layout is an audit abstraction, not an observed P&ID',
      'EpistemicsProvenance':'Historical external case evidence separate from synthetic model and UNKNOWN plant data',
      'AuthorityHumanBoundary':'Human operator/maintainer authorizes intervention; no autonomous actuation',
      'EffectsSafety':'Retain pressure, stored-energy isolation, process quality and equipment limits',
      'DependencyValidity':'Invalidate predictions when compressor maps, schedules or requirements change',
      'ResourceTermination':'Finite curated nodes/edges; no automatic recursive self-feeding expansion',
      'PrivacyRetention':'No personal data used; operational data access/retention not yet specified',
      'AuditExplanation':'Source-bound claims; independently meter energy and normalize output',
      'RecoveryEvolution':'Detect recurrent leaks and restore service on pressure or quality failure',
    }
    situations=[]
    for ident,group,name,ins,outs,laws,unknown in ROWS:
        o=[dict(id='equipment',type='THING'),dict(id='event',type='EVENT'),
           dict(id='context',type='CONTEXT'),dict(id='constraint',type='RULE'),
           dict(id='time',type='TIME'),dict(id='location',type='SPACE')]
        relations=[dict(source='context',relation='frames',target='event'),
                   dict(source='event',relation='dependsOn',target='equipment')]
        if group in ('control','recovery'):
            o.extend([dict(id='operator',type='AGENCY'),dict(id='intervention',type='ACTION')])
            relations.append(dict(source='operator',relation='acts',target='intervention'))
        if ident=='CA12':
            o.extend([dict(id='benefit',type='VALUE'),dict(id='estimate',type='CLAIM')])
            relations.append(dict(source='estimate',relation='references',target='benefit'))
        situations.append(dict(id=ident,name=name,parent_id='CA/'+group,objects=o,relations=relations,
          forms=['CONSTRUCT','CONTRACT','STATE','RELATION','PROCESS','RULE','PROJECTION'],
          facets={k:dict(status='APPLICABLE',reason=v) for k,v in facets.items()},
          inputs=[dict(name=v,unit=UNITS[v]) for v in split(ins)],
          outputs=[dict(name=v,unit=UNITS[v]) for v in split(outs)],
          constraints=split(laws),assumptions=['Case-specific physical data required; no full GSL/SAL conformance'],
          unresolved_state=[unknown],source_refs=['DOE-VISTEON','DOE-SOURCEBOOK','AUTHOR-MODEL']))
    # Explicit physical/information dependencies. A shared-consumer pair is not
    # a claim that simultaneous states or numerical conservation were verified.
    edges=[('CA01','CA02','hot_air_kg_s'),('CA02','CA03','clean_air_kg_s'),
      ('CA02','CA04','dewpoint_K'),('CA03','CA04','header_Pa'),
      ('CA04','CA03','network_draw_kg_s'),('CA04','CA05','terminal_Pa,terminal_dewpoint_K'),
      ('CA05','CA04','demand_kg_s'),('CA06','CA04','leak_kg_s'),('CA03','CA06','header_Pa'),
      ('CA01','CA07','compressor_kw,actual_mode'),('CA02','CA07','treatment_kw'),
      ('CA03','CA07','header_Pa,receiver_K,stored_kg'),('CA04','CA07','terminal_Pa,terminal_dewpoint_K'),
      ('CA05','CA07','good_units_s,quality_record'),('CA06','CA07','leak_kg_s'),
      ('CA07','CA08','observed_state'),('CA08','CA01','mode_command'),
      ('CA05','CA09','production_active'),('CA09','CA06','isolation_command'),
      ('CA07','CA10','observed_state'),('CA10','CA11','repair_targets'),
      ('CA11','CA06','leak_conductance'),('CA11','CA12','repair_event'),
      ('CA07','CA12','observed_state'),('CA12','CA10','recurrence_flag')]
    transitions=[dict(id=f'CAT{i:02}',source=a,target=b,transfers=split(v),required_transfers=split(v),
      assumptions=['Ports require common equipment/context/time; cyclic edges are dependencies, not time travel'])
      for i,(a,b,v) in enumerate(edges,1)]
    laws=[dict(id=i,type=t,equation=e,domain=d,assumptions=[d],
      falsifier='Independent measurement violates the scoped relationship outside uncertainty, or domain fails',
      source_refs=['AUTHOR-MODEL','DOE-SOURCEBOOK']) for i,t,e,d in LAW_ROWS]
    return dict(situations=situations,transitions=transitions,laws=laws,
      sources=[dict(id=k,url=v) for k,v in SOURCES.items()])

def bank_kw(demand, on, *, capacity=F(1), loaded=F(200), unloaded=F(60)):
    """Average steady-state toy; not instantaneous dispatch/safety qualification."""
    demand,capacity,loaded,unloaded=map(F,(demand,capacity,loaded,unloaded))
    if type(on) is not int or on<0 or demand<0 or capacity<=0 or not 0<=unloaded<=loaded:
        raise ValueError('invalid physical domain')
    if demand>on*capacity:
        return None
    return on*unloaded+(loaded-unloaded)*demand/capacity

def experiment():
    # FIXED SYNTHETIC CONTRACT: useful demand 1kg/s; leak0.2->0kg/s;
    # two units, each capacity1kg/s, loaded200kW/unloaded60kW;
    # 8000h/y and $0.10/kWh. Same terminal service; no storage depletion;
    # no required spinning reserve; auxiliaries unchanged; costs not assumed zero.
    old=bank_kw(F('1.2'),2)
    repaired=bank_kw(F(1),2)
    coordinated=bank_kw(F(1),1)
    assert (old,repaired,coordinated)==(288,260,200)
    assert bank_kw(F('1.2'),1) is None  # sequencing alone cannot meet demand
    assert bank_kw(F('1.05'),1) is None  # 5% sustained headroom null
    assert bank_kw(0,0)==0
    # If supply compensates a removed leak by equal blow-off, demand stays1.2:
    assert old-bank_kw(F('1.2'),2)==0
    # Projection loss: same flow/header pressure; mode count changes power.
    assert bank_kw(1,2)-bank_kw(1,1)==60
    # Compare a constraint-derived minimum unit count with conventional exhaustive
    # feasible-action optimization. These are known equivalent calculations.
    for demand in [F(i,20) for i in range(1,41)]:
        feasible=[(bank_kw(demand,n),n) for n in range(3) if bank_kw(demand,n) is not None]
        conventional=min(feasible)[1]
        closure_rule=(demand.numerator+demand.denominator-1)//demand.denominator
        assert conventional==closure_rule
    # A low-pressure receiver cannot finance permanent flow deficit.
    # 1m3 tank, 300K, R287J/(kg*K), usable pressure band20kPa:
    usable_mass=F(20000,287*300)
    seconds_at_five_percent_deficit=usable_mass/F('0.05')
    hourly=F(8000)*F('0.10')
    ledger=dict(baseline_kw=old,repair_only_kw=repaired,coordinated_kw=coordinated,
      repair_only_saving_kw=old-repaired,combined_saving_kw=old-coordinated,
      additional_dispatch_saving_after_repair_kw=repaired-coordinated,
      repair_only_gross_usd_year=(old-repaired)*hourly,
      combined_gross_usd_year=(old-coordinated)*hourly,
      allowed_extra_annual_cost_vs_repair_only=(repaired-coordinated)*hourly,
      illustrative_100_site_gross_usd_year=100*(old-coordinated)*hourly,
      tank_seconds_at_5pct_deficit=seconds_at_five_percent_deficit,
      garden_extra_vs_same_conventional_dispatch=F(0),
      awhc_simple_payback_months=F(228000,160000)*12)
    return ledger

def checks(seed):
    import copy
    edges=audit_transitions(seed)
    assert all(e['contract_status']=='STRUCTURALLY_BOUND' for e in edges)
    assert all(sal(s)['structural_status']=='VALID' for s in seed['situations'])
    assert all(sal(s)['completeness_status']=='CONTEXT_REQUIRED' for s in seed['situations'])
    damaged=copy.deepcopy(seed)
    damaged['situations'][1]['inputs'][0]['unit']='m3/s'
    assert any('UNIT_ADAPTER_REQUIRED:hot_air_kg_s' in x['diagnostics'] for x in audit_transitions(damaged))
    damaged=copy.deepcopy(seed)
    damaged['transitions']=[e for e in damaged['transitions'] if e['id']!='CAT17']
    assert 'mode_command' in audit_consumer_inputs(damaged)[0]['unbound_inputs']
    experiment()

def report():
    seed=build_case(); checks(seed)
    obligations=derive_obligations(seed)
    unresolved=audit_consumer_inputs(seed)
    motifs=audit_combinations(seed)
    lines=[STATUS,'Coverage is of this declared audit model, never of all plant reality.',
      f"situations={len(seed['situations'])}; transitions={len(seed['transitions'])}; laws={len(seed['laws'])}; bindings={len(obligations)}; connected_incoming_pairs={motifs['checked']}",
      'unbound_external_inputs='+str(sum(len(x['unbound_inputs']) for x in unresolved)),
      'TREE routing: ROOT source/status/facets; TRUNK typed audit and comparison; BOUNDARY compressed-air equations and plant adapters.',
      'Not TREE_CORE-r6: no claim of canonical encoding, source retention or admission.',
      'Seven Forms interpreted as system components / interface contracts / persistent state / dependencies / event processes / scoped rules / coarse views.',
      'All ten facets bound per situation; quantitative site applicability remains UNKNOWN.']
    for s in seed['situations']:
        lines.append(f"{s['id']} | {s['parent_id']} | {s['name']} | {','.join(s['constraints'])}")
        lines.append('  UNKNOWN: '+s['unresolved_state'][0])
    for e in seed['transitions']:
        lines.append(f"{e['id']} {e['source']} -> {e['target']} : "+','.join(e['transfers']))
    for r in seed['laws']:
        lines.append(f"{r['id']} [{r['type']}] {r['equation']} | {r['domain']}")
    for a in unresolved:
        if a['unbound_inputs']:
            lines.append(a['situation']+' REQUIRED_CONTEXT: '+','.join(a['unbound_inputs']))
    lines.append('Port status: all declared transfers structurally bound; numerical physics NOT_VERIFIED.')
    lines.append('Synthetic model arithmetic and nulls (not historical plant measurements):')
    for k,v in experiment().items():
        lines.append(f'{k}={float(v):.9g} [exact {v}]')
    for path in ('V15_10_ABSTRACTION_GCSC_DELTA.md','TREE_CORE_v0.8.1_2026-09-23.txt'):
        data=(HERE/path).read_bytes()
        lines.append('Garden source '+path+' SHA256 '+hashlib.sha256(data).hexdigest())
    lines.append('Research seed digest (not canonical Garden encoding): '+digest(seed))
    return '\n'.join(lines)+'\n'

if __name__=='__main__':
    print(report(),end='')
