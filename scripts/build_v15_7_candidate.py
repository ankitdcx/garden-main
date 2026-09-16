#!/usr/bin/env python3
"""Materialize direct v15.7 from the preserved v15.6 draft and pinned candidates."""
import hashlib
import json
from pathlib import Path
import sys
import subprocess

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'implementation'))
from garden_kernel.section_units import build_inventory

def sha(b): return hashlib.sha256(b).hexdigest()
def dump(p,v):
    p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(v,indent=2,ensure_ascii=False)+'\n')

def main():
    old=ROOT/'canonical/candidates/v15.6'
    target=ROOT/'canonical/candidates/v15.7';target.mkdir(parents=True,exist_ok=True)
    ev=ROOT/'reviews/v15.7';ev.mkdir(parents=True,exist_ok=True)
    delta=ROOT/'design_deltas/v15.7'
    prior=json.loads((old/'SOURCE_MANIFEST.json').read_text())
    canonical=json.loads((ROOT/'canonical/current/SOURCE_MANIFEST.json').read_text())
    names=['TRACE-CANDIDATE.md','COGNITIVE-INCREMENT-CANDIDATE.md','COGNITIVE-CORE-CANDIDATE.md','COGNITIVE-COMPARE-CANDIDATE.md','DESIGN-CLOSURE-CANDIDATE.md','EVENT-DRIVEN-CONTEXT-ROUTING-CANDIDATE.md','BOUNDED-IMPLEMENTATION-CONTRACTS.md','EVENT-DRIVEN-CONTEXT-ROUTING-CORRECTION-2026-09-16.md']
    sources={name:(delta/name).read_text() for name in names}
    extensions={
        'User':'[H-V15-7] Direct v15.7 human guide\nThe retained v15.6 draft contains all 15 engineering patterns, 38 additional work items and 174 prior queue dispositions. This version adds TRACE, explanation competition and skill acquisition, seven-function cognitive qualification, ten-system comparative coverage and design closure. The canonical predecessor is v15.5. All proposals remain subject to their explicit qualification and admission rules.\nSee [T-V15-7], [TH-V15-7] and [A-V15-7].\n',
        'System':'[S-V15-7] Integrated candidate flow\nPropose, authorize, execute, observe, evaluate and retry or finish under one immutable grant. A separate bounded recovery allowance handles abort, uncertain completion and containment. Explanation competition selects authorized distinguishing observations; candidate skills require bounded qualification. Qualification, comparison and design closure proceed independently; combined claims require their applicable evidence. Component success does not admit failed composition. Exact requirements are in [T-V15-7] and [A-V15-7].\n',
        'Technical':'[T-V15-7] Runtime and cognitive candidate requirements\nThese extensions reuse existing Reason, execution/authority, Knowledge, Proof and Audit responsibilities; exact unresolved machine bindings remain unresolved.\n\n'+'\n\n'.join(sources[n] for n in names[:3]),
        'Theories':'[TH-V15-7] Comparative coverage program\n'+sources['COGNITIVE-COMPARE-CANDIDATE.md'],
        'Annexure':'[A-V15-7] Design closure and source provenance\n'+sources['DESIGN-CLOSURE-CANDIDATE.md']+'\nSource files and hashes:\n'+json.dumps({n:sha(s.encode()) for n,s in sources.items()},indent=2)+'\nThe five new programs are specified, not completed qualification or comparative findings. Earlier reviews apply only to their exact v15.6 inputs; they are not v15.7 approval.\n'
    }
    extensions['User'] += '\nThere are five design documents, with separate responsibilities: User (human control and use), System (architecture and interactions), Technical (contracts and implementations), Annexure (registries and evidence), and Theories (reasoning and comparisons). A combined text export is a convenience copy. Event-driven context routing adds selective synthesis while retaining provenance, freshness and contradictions. Bounded executable reference packages are now available; their results do not qualify the complete design. See reviews/v15.7/qualification/OBLIGATION-REGISTER.json for all outstanding obligations.\n'
    extensions['System'] += '\nEvent-driven context routing extends the existing Process, Knowledge, Evidence and receipt boundaries. Recovery, release verification and physical fallback reference packages exercise selected boundaries under explicit assumptions. They add no top-level engine or authority source and are not automatically connected to live execution.\n'
    extensions['Technical'] += '\n\n' + sources['EVENT-DRIVEN-CONTEXT-ROUTING-CANDIDATE.md'] + '\n\n' + sources['EVENT-DRIVEN-CONTEXT-ROUTING-CORRECTION-2026-09-16.md'] + '\n\n' + sources['BOUNDED-IMPLEMENTATION-CONTRACTS.md']
    extensions['Annexure'] = extensions['Annexure'].replace('The five new programs are specified, not completed qualification or comparative findings.', 'Six candidate programs, the current EDCR amendment and one implementation-boundary specification are incorporated. Executed reference evidence is scoped in reviews/v15.7/qualification; no complete-design qualification or comparative finding is inferred.')
    rows={};retention=[]
    for role,row in prior['files'].items():
        raw=(old/row['name']).read_bytes();assert sha(raw)==row['sha256']
        name=f'Garden_{role}_v15.7_FULL_CANDIDATE_2026-09-16.txt'
        header=(f'GARDEN v15.7 — FULL FIVE-FILE WORKING CANDIDATE — {role.upper()} — 2026-09-16\n'
          'Status: WORKING_FIVE_FILE_CANDIDATE / NOT CANONICAL / NOT CERTIFIED\n'
          'Canonical predecessor: v15.5; retained draft lineage: v15.6; GSL v45.1; topology unchanged.\n'
          'Direct version jump authorized by user. Old embedded banners describe retained historical/draft layers.\n'
          'No intermediate v15.6 promotion is claimed or required to prepare this candidate.\n'
          'New programs are specified requirements; unresolved admission/implementation/evaluation work remains explicit.\n'
          'BEGIN RETAINED V15.6 DRAFT\n').encode()
        result=header+raw+('\nEND RETAINED V15.6 DRAFT\n\nBEGIN V15.7 EXTENSION\n'+extensions[role]+'\nEND V15.7 EXTENSION\n').encode()
        (target/name).write_bytes(result);rows[role]={'name':name,'bytes':len(result),'sha256':sha(result)}
        retention.append({'role':role,'retained_offset':len(header),'retained_bytes':len(raw),'draft_sha256':sha(raw),'exact':result[len(header):len(header)+len(raw)]==raw})
    root=sha(json.dumps(sorted([{'role':r,**v} for r,v in rows.items()],key=lambda x:x['role']),sort_keys=True,separators=(',',':'),ensure_ascii=False).encode())
    manifest={'schema':'GardenCanonicalSourceManifest/v1','release':'Garden v15.7','gsl':'v45.1','date':'2026-09-16','status':'WORKING_FIVE_FILE_CANDIDATE_NOT_CANONICAL','files':rows,'source_root_algorithm':canonical['source_root_algorithm'],'source_root_sha256':root,'predecessor_release':canonical['release'],'predecessor_source_root_sha256':canonical['source_root_sha256'],'retained_draft_source_root_sha256':prior['source_root_sha256']}
    dump(target/'SOURCE_MANIFEST.json',manifest)
    dump(ROOT/'canonical/candidates/CURRENT_CANDIDATE.json',{'release':'Garden v15.7','status':'WORKING_FIVE_FILE_CANDIDATE','manifest':'canonical/candidates/v15.7/SOURCE_MANIFEST.json','source_root_sha256':root,'canonical':False})
    dump(ev/'RETENTION-RECEIPT.json',{'status':'PASS','scope':'Exact draft bytes retained, including its exact v15.5 source layers. No semantic admission.','files':retention})
    before=build_inventory(source_dir=old,manifest=prior,process_version='1.4')
    after=build_inventory(source_dir=target,manifest=manifest,process_version='1.4')
    old_refs={r for u in before.units for r in u.unresolved_references};refs={r for u in after.units for r in u.unresolved_references}
    dump(ev/'REFERENCE-CLOSURE-RECEIPT.json',{'status':'INCONCLUSIVE','source_root_sha256':root,'scope':'Existing bounded explicit anchor parser, not full semantic/GSL closure','unresolved':sorted(refs),'newly_unresolved':sorted(refs-old_refs),'counts':after.counts(),'qualified_review_units':0,'semantic_closure_complete':False})
    dump(ev/'SOURCE-INTEGRATION-RECEIPT.json',{'status':'CANDIDATE_MATERIALIZED_NOT_ADMITTED','repository_registration_base':'5caf3845c2c43e6a6fe91ced3b79760527d680d2','registration_base_scope':'GitHub input snapshot containing six registered candidates; local history uses a materialized snapshot','workspace_commit':subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),'workspace_dirty':bool(subprocess.check_output(['git','status','--porcelain'],cwd=ROOT,text=True).strip()),'builder_sha256':sha(Path(__file__).read_bytes()),'new_programs':[{ 'path':'design_deltas/v15.7/'+n,'sha256':sha(s.encode()),'incorporated_complete_text':True} for n,s in sources.items()],'carried_forward_draft':prior['source_root_sha256'],'candidate_source_root_sha256':root,'comparison':'Retain six programs independently; no-addition leaves agreed work scattered, standalone replacement loses inherited work. Full cumulative draft selected; no superiority or completion claims.'})
    print(json.dumps({'root':root,'five_files':len(rows),'retention':all(r['exact'] for r in retention),'new_unresolved':len(refs-old_refs)}))

if __name__=='__main__':main()
