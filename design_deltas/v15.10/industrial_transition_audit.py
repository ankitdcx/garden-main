#!/usr/bin/env python3
"""NONCANONICAL finite research harness: reference-state closure, not new physics.

Run with --upstream /path/to/MEASUR-Tools-Suite to compile the pinned ORIGINAL
implementation and check the counterexamples. No downloads or upstream edits.
The corrected model is a research comparator, not a production library patch.
"""
from __future__ import annotations
import argparse
from dataclasses import dataclass
import hashlib
import math
from pathlib import Path
import subprocess
import tempfile

from electricity_closure import (sal, derive_obligations, audit_transitions,
    audit_combinations, audit_consumer_inputs)

UPSTREAM = '0669b456c67bd8b9c1656a83cd7d35d68a2701d5'
SOURCE_HASHES = {
    'include/treasureHunt/compressed_air_pressure_reduction.h':
        '9eb5875f3561b481380e65ef952ab1a97627242773f86f7c777099ca7ad0c0fb',
    'src/treasureHunt/compressed_air_pressure_reduction.cpp':
        '65ebe5cfae4c1548cb54564b2224ad220811e125612a6a567bb431f1b68dabc4',
    'include/physics/constants.h':
        'f215f700a87fc776154984d8d5c83ebee5b6cfa344d6a369ff34292ac24a5844',
}
B = .395 / 1.395


def require(condition, message):
    if not condition:
        raise ValueError(message)


def work_factor(gauge_psi, atmosphere_psia):
    """Dimensionless ideal pressure-work factor; no independent field accuracy."""
    require(all(math.isfinite(v) for v in (gauge_psi, atmosphere_psia)), 'finite pressures required')
    require(gauge_psi >= 0 and atmosphere_psia > 0, 'invalid compression domain')
    return math.expm1(B * math.log1p(gauge_psi / atmosphere_psia))


@dataclass(frozen=True)
class PowerAnchor:
    power_kw: float
    gauge_psi: float
    atmosphere_psia: float
    basis: str
    duty_id: str
    fixed_kw: float = 0.0

    def __post_init__(self):
        require(self.basis in ('MEASURED_AT_BASELINE', 'RATED_AT_REFERENCE'), 'unknown power basis')
        require(bool(self.duty_id), 'physical duty/context identity required')
        require(all(math.isfinite(v) for v in (self.power_kw, self.fixed_kw)), 'finite power required')
        require(0 <= self.fixed_kw <= self.power_kw, 'invalid fixed/scalable power split')
        require(work_factor(self.gauge_psi, self.atmosphere_psia) > 0, 'positive reference compression required')

    def at(self, gauge_psi, atmosphere_psia, duty_id):
        require(duty_id == self.duty_id, 'changed flow/control/temperature/efficiency context')
        return self.fixed_kw + (self.power_kw-self.fixed_kw) * (
            work_factor(gauge_psi, atmosphere_psia) /
            work_factor(self.gauge_psi, self.atmosphere_psia))


def annual_saving(anchor, baseline_psi, proposed_psi, atmosphere_psia,
                  hours, price_per_kwh, duty_id):
    require(all(math.isfinite(v) and v >= 0 for v in (hours, price_per_kwh)), 'invalid annualization')
    return (anchor.at(baseline_psi, atmosphere_psia, duty_id) -
            anchor.at(proposed_psi, atmosphere_psia, duty_id)) * hours * price_per_kwh


def legacy_modified_kw(power_kw, proposed_psi, atmosphere_psia, rated_psi):
    """Mathematical comparator to pinned code, verified by optional native probe."""
    return power_kw * work_factor(proposed_psi, atmosphere_psia) / work_factor(rated_psi, 14.7)


# Explicit source-owned engineering requirements, not discovered physical laws.
LAWS = [
 ('MASS', 'EXACT_CLASSICAL_BALANCE', 'dm/dt=sum(mdot_in)-sum(mdot_out)',
  'kg/s; all purge/leaks/storage included; no nuclear reactions'),
 ('ENERGY', 'EXACT_CLASSICAL_BALANCE', 'dU/dt=Qdot+Wdot+enthalpy_in-enthalpy_out',
  'W; declared control volume; kinetic/potential terms included if material'),
 ('SERVICE', 'ENGINEERING_CONSTRAINT', 'same useful flow, terminal pressure minimum, quality and availability',
  'Site limits UNKNOWN; reducing required service cannot count as saving'),
 ('ANCHOR', 'REPRESENTATION_CONSTRAINT', 'power travels with basis, reference pressure, atmosphere and duty identity',
  'kW alone does not identify an operating state; gauge and absolute pressure distinct'),
 ('WORK', 'SCOPED_CONSTITUTIVE_MODEL', 'P=Pf+(Pref-Pf)*F(p,a)/F(pref,aref)',
  'kW; fixed mass flow, inlet temperature, efficiency and control mode; F dimensionless; no centrifugal qualification'),
 ('IDENTITY', 'DERIVED_COMPARISON_INVARIANT', 'same state, duration and tariff => delta_cost=0',
  'Physical identity independent of correctness of the chosen pressure-work law'),
 ('COMPOSITION', 'DERIVED_MODEL_INVARIANT', 'F(c)/F(a)=[F(b)/F(a)]*[F(c)/F(b)]',
  'One unchanged positive work-factor model and duty; no double application of correction'),
 ('VALUE', 'ECONOMIC_CONDITION', 'net=verified avoided bill-all added annual costs',
  'currency/year; measurement uncertainty and comparator retained; calculator error is not energy saved'),
 ('EVIDENCE', 'EVIDENCE_CONSTRAINT', 'prediction status distinct from field evidence and scientific admission',
  'Hash binds bytes, not truth; independent validation needed'),
]

# Physical operation is followed by observation, proposed intervention and decision.
ROWS = [
 ('P01','Intake and compress air','mass_in,grid_kw','compressed_mass,power_kw','MASS,ENERGY,SERVICE'),
 ('P02','Deliver required air through network','compressed_mass','duty_id,p0,a0','MASS,SERVICE'),
 ('P03','Measure baseline power and operating context','power_kw,duty_id,p0,a0','measured_kw,measured_p,measured_a,measured_duty','ANCHOR,EVIDENCE'),
 ('P04','Choose measured or nameplate power reference','measured_kw,measured_p,measured_a,measured_duty','anchor_kw,anchor_p,anchor_a,basis,anchor_duty','ANCHOR'),
 ('P05','Serialize reference across UI and library boundary','anchor_kw,anchor_p,anchor_a,basis,anchor_duty','bound_anchor','ANCHOR,IDENTITY'),
 ('P06','Select feasible pressure intervention','duty_id,p0,a0','p1,comparison_context','SERVICE,EVIDENCE'),
 ('P07','Evaluate both states using common reference','bound_anchor,p1,comparison_context','baseline_kw,modified_kw','WORK,IDENTITY,COMPOSITION'),
 ('P08','Annualize matched operating states','baseline_kw,modified_kw,hours,tariff','gross_value','IDENTITY,VALUE'),
 ('P09','Rank investment against all added costs','gross_value,annual_cost','decision','VALUE,EVIDENCE'),
 ('P10','Authorize and meter matched intervention','decision,duty_id','field_evidence','SERVICE,EVIDENCE'),
 ('P11','Compare prediction with independent evidence','gross_value,field_evidence','qualified_claim','IDENTITY,VALUE,EVIDENCE'),
]
UNITS = dict(mass_in='kg/s', grid_kw='kW', compressed_mass='kg/s', power_kw='kW',
 duty_id='CONTEXT_ID', p0='psig', a0='psia', measured_kw='kW', measured_p='psig',
 measured_a='psia', measured_duty='CONTEXT_ID', anchor_kw='kW', anchor_p='psig',
 anchor_a='psia', basis='POWER_BASIS_ENUM', anchor_duty='CONTEXT_ID', bound_anchor='POWER_ANCHOR_V1',
 p1='psig', comparison_context='MATCHED_DUTY_V1', baseline_kw='kW', modified_kw='kW',
 hours='h/year', tariff='USD/kWh', gross_value='USD/year', annual_cost='USD/year',
 decision='DECISION_V1', field_evidence='EVIDENCE_V1', qualified_claim='CLAIM_V1')
EDGES = [
 ('P01','P02','compressed_mass'),('P01','P03','power_kw'),
 ('P02','P03','duty_id,p0,a0'),('P03','P04','measured_kw,measured_p,measured_a,measured_duty'),
 ('P04','P05','anchor_kw,anchor_p,anchor_a,basis,anchor_duty'),
 ('P02','P06','duty_id,p0,a0'),('P05','P07','bound_anchor'),
 ('P06','P07','p1,comparison_context'),('P07','P08','baseline_kw,modified_kw'),
 ('P08','P09','gross_value'),('P09','P10','decision'),('P02','P10','duty_id'),
 ('P10','P11','field_evidence'),('P08','P11','gross_value'),
]


def situation_graph(repaired=False):
    facets = {
     'IdentityLifecycle':'Retain machine, power reference, model version and duty identity',
     'ScopeContext':'Same useful duty; explicit atmospheric reference and pressure units',
     'EpistemicsProvenance':'Pinned upstream source; assumed numerical example; field data UNKNOWN',
     'AuthorityHumanBoundary':'Only authorized operator may implement pressure change; no actuation here',
     'EffectsSafety':'Terminal service and equipment limits UNKNOWN until plant qualified',
     'DependencyValidity':'Changing inlet temperature, flow, control or efficiency invalidates fixed-duty model',
     'ResourceTermination':'Finite curated graph; pure checks; no S1 self-feed',
     'PrivacyRetention':'Public code and synthetic data only; operational access not supplied',
     'AuditExplanation':'Preserve original and repaired estimates, falsifiers and negative results',
     'RecoveryEvolution':'Reject ambiguous power reference; use qualified baseline pending repair',
    }
    sources=[dict(id='MODEL',url='This file: derived reference-state contract'),
             dict(id='UPSTREAM',url='https://github.com/ORNL-AMO/MEASUR-Tools-Suite/tree/'+UPSTREAM),
             dict(id='EXTERNAL_REQUIRED',url='UNKNOWN: site-authorized physical data required')]
    situations=[]
    external={'P01':['mass_in','grid_kw'], 'P08':['hours','tariff'], 'P09':['annual_cost']}
    for ident,name,ins,outs,laws in ROWS:
        objects=[dict(id='equipment',type='THING'),dict(id='state_context',type='CONTEXT'),
                 dict(id='constraint',type='RULE'),dict(id='event',type='EVENT'),
                 dict(id='time',type='TIME'),dict(id='place',type='SPACE')]
        rel=[dict(source='state_context',relation='frames',target='event')]
        if ident in ('P04','P06','P09','P10'):
            objects.extend([dict(id='operator',type='AGENCY'),dict(id='choice',type='ACTION')])
            rel.append(dict(source='operator',relation='acts',target='choice'))
        if ident in ('P08','P09','P11'):
            objects.extend([dict(id='estimate',type='CLAIM'),dict(id='benefit',type='VALUE')])
            rel.append(dict(source='estimate',relation='references',target='benefit'))
        forms=['STATE','RELATION','PROCESS','RULE','CONTRACT']
        if ident in ('P01','P02'): forms.append('CONSTRUCT')
        if ident in ('P03','P04','P05','P08'): forms.append('PROJECTION')
        situations.append(dict(id=ident,name=name,objects=objects,relations=rel,forms=forms,
          facets={k:dict(status='APPLICABLE',reason=v) for k,v in facets.items()},
          inputs=[dict(name=v,unit=UNITS[v]) for v in ins.split(',')],
          outputs=[dict(name=v,unit=UNITS[v]) for v in outs.split(',')],
          constraints=laws.split(','),source_refs=['MODEL','UPSTREAM'],
          assumptions=['Physical applicability needs site qualification; structural diagnostics are not full SAL'],
          unresolved_state=['Actual site data and economic incidence UNKNOWN'],
          external_bindings=[dict(name=v,unit=UNITS[v],source_ref='EXTERNAL_REQUIRED')
                             for v in external.get(ident,[])]))
    edges=[]
    for i,(a,b,variables) in enumerate(EDGES,1):
        required=variables.split(',')
        # An explicit research obligation exposed by the code/caller audit.
        # Existing API carries some numbers but drops their power basis and local reference semantics.
        sent=['anchor_kw','anchor_p'] if b=='P05' and not repaired else required
        edges.append(dict(id=f'PT{i:02}',source=a,target=b,transfers=sent,
            required_transfers=required,assumptions=['Common machine/time/duty required; not established by labels']))
    laws=[dict(id=i,type=t,equation=e,domain=d,assumptions=[d],source_refs=['MODEL'],
               falsifier='Identity or balance counterexample within scope, or independent data outside uncertainty')
          for i,t,e,d in LAWS]
    return dict(situations=situations,transitions=edges,laws=laws,sources=sources)


def experiment():
    results={}
    for label,a,rated,proposed in [
        ('api_reference_noop',14.7,125,100),('api_reference_reduction',14.7,125,90),
        ('ui_local_atmosphere_noop',12,100,100),('ui_local_atmosphere_reduction',12,100,90),
        ('standard_atmosphere_null',14.7,100,100)]:
        anchor=PowerAnchor(100,100,a,'MEASURED_AT_BASELINE','fixed-duty')
        old=legacy_modified_kw(100,proposed,a,rated)
        new=anchor.at(proposed,a,'fixed-duty')
        results[label]=dict(legacy_modified_kw=old,corrected_modified_kw=new,
           legacy_saving_per_year=(100-old)*800,corrected_saving_per_year=(100-new)*800)
    gross=results['ui_local_atmosphere_reduction']['corrected_saving_per_year']
    results['conditional_decision']=dict(assumed_annual_cost=2000,
        net_at_all_power_scalable=gross-2000,net_at_70_percent_scalable=.7*gross-2000,
        minimum_scalable_fraction=2000/gross,field_value='UNKNOWN',population='UNKNOWN')
    return results


def check_invariants():
    count=0
    def close(a,b):
        nonlocal count
        require(math.isclose(a,b,rel_tol=1e-11,abs_tol=1e-9), f'check failed: {a} vs {b}')
        count+=1
    for ambient in (10,12,14.7,15.5):
        for pressure in (40,100,125,175):
            for fixed in (0,30,100):
                anchor=PowerAnchor(100,pressure,ambient,'MEASURED_AT_BASELINE','D',fixed)
                close(annual_saving(anchor,pressure,pressure,ambient,8000,.1,'D'),0)
                for proposed in (pressure*.7,pressure*.9):
                    power=anchor.at(proposed,ambient,'D')
                    require(fixed <= power <= 100, 'pressure-work monotonicity')
                    count+=1
                    # Equivalent nameplate re-expression must not alter either state.
                    rated=PowerAnchor(anchor.at(150,14.7,'D'),150,14.7,'RATED_AT_REFERENCE','D',fixed)
                    close(annual_saving(anchor,pressure,proposed,ambient,8000,.1,'D'),
                          annual_saving(rated,pressure,proposed,ambient,8000,.1,'D'))
                    intermediate=PowerAnchor(power,proposed,ambient,'MEASURED_AT_BASELINE','D',fixed)
                    close(intermediate.at(20,ambient,'D'),anchor.at(20,ambient,'D'))
    for args in [(100,0,14.7,'MEASURED_AT_BASELINE','D',0),
                 (100,100,0,'MEASURED_AT_BASELINE','D',0),
                 (100,100,14.7,'UNKNOWN','D',0),(100,100,14.7,'MEASURED_AT_BASELINE','D',101)]:
        try: PowerAnchor(*args)
        except ValueError: count+=1
        else: raise RuntimeError('invalid anchor accepted')
    try: PowerAnchor(100,100,14.7,'MEASURED_AT_BASELINE','D').at(90,14.7,'changed-duty')
    except ValueError: count+=1
    else: raise RuntimeError('changed duty accepted')
    # Known code failure and unaffected null are both required.
    r=experiment()
    require(abs(r['ui_local_atmosphere_noop']['legacy_saving_per_year'])>9000,'missing legacy witness')
    close(r['standard_atmosphere_null']['legacy_saving_per_year'],0)
    return count


def native_probe(upstream):
    upstream=Path(upstream).resolve()
    head=subprocess.check_output(['git','-C',str(upstream),'rev-parse','HEAD'],text=True).strip()
    require(head==UPSTREAM,'wrong upstream commit; do not silently update frozen experiment')
    for path,expected in SOURCE_HASHES.items():
        require(hashlib.sha256((upstream/path).read_bytes()).hexdigest()==expected,'source bytes changed: '+path)
    driver=r'''#include <iostream>
#include <iomanip>
#include "treasureHunt/compressed_air_pressure_reduction.h"
int main(){using namespace compressed_air_pressure_reduction;
 for(double a: {12.0,14.7}) for(double rated: {100.0,125.0}) for(double p: {90.0,100.0}) {
  auto b=compressedAirPressureReduction({{true,8000,.1,100,100,p,a,rated}});
  auto m=compressedAirPressureReduction({{false,8000,.1,100,100,p,a,rated}});
  std::cout<<std::setprecision(17)<<a<<" "<<rated<<" "<<p<<" "<<b.energy_cost-m.energy_cost<<"\n";
 }}
'''
    with tempfile.TemporaryDirectory(prefix='garden-pressure-probe-') as tmp:
        tmp=Path(tmp); (tmp/'probe.cpp').write_text(driver)
        subprocess.run(['g++','-std=c++17','-I',str(upstream/'include'),str(tmp/'probe.cpp'),
            str(upstream/'src/treasureHunt/compressed_air_pressure_reduction.cpp'),'-o',str(tmp/'probe')],check=True)
        lines=subprocess.check_output([str(tmp/'probe')],text=True).splitlines()
    for line in lines:
        a,rated,p,native=map(float,line.split())
        expected=(100-legacy_modified_kw(100,p,a,rated))*800
        require(math.isclose(native,expected,rel_tol=1e-11,abs_tol=1e-8),'native comparator differs')
    return len(lines)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--upstream',type=Path)
    parser.add_argument('--details',action='store_true')
    args=parser.parse_args()
    print('NONCANONICAL RESEARCH: implementation defect; physical novelty and field savings NOT ESTABLISHED')
    for repaired in (False,True):
        graph=situation_graph(repaired)
        diagnostics=audit_transitions(graph)
        print('repaired=',repaired,'situations=',len(graph['situations']),
              'transitions=',len(graph['transitions']),'law_families=',len(graph['laws']),
              'bindings=',len(derive_obligations(graph)),
              'incoming_pairs=',audit_combinations(graph)['checked'],
              'missing_transfer_obligations=',sum(len(x['diagnostics']) for x in diagnostics),
              'unbound_inputs=',sum(len(x['unbound_inputs']) for x in audit_consumer_inputs(graph)))
        require(all(sal(s)['structural_status']=='VALID' for s in graph['situations']),'typed graph invalid')
        if args.details:
            for s in graph['situations']: print(s['id'],s['name'],'RULES',','.join(s['constraints']))
            for d in diagnostics: print(d['id'],d['source'],'->',d['target'],d['contract_status'],d['diagnostics'])
    print('Metamorphic/domain checks passed:',check_invariants())
    print('Original pinned native C++ comparisons:',native_probe(args.upstream) if args.upstream else 'NOT_RUN (supply --upstream)')
    for key,value in experiment().items(): print(key,value)
    print('Full GSL/SAL semantics UNKNOWN; source-level UI trace only; installed WASM/browser NOT_TESTED')


if __name__=='__main__':
    main()
