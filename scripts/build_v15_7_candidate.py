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
    names=['TRACE-CANDIDATE.md','COGNITIVE-INCREMENT-CANDIDATE.md','COGNITIVE-CORE-CANDIDATE.md','COGNITIVE-COMPARE-CANDIDATE.md','DESIGN-CLOSURE-CANDIDATE.md']
    sources={name:(delta/name).read_text() for name in names}
    extensions={
        'User':'[H-V15-7] Direct v15.7 human guide\nThe retained v15.6 draft contains all 15 engineering patterns, 38 additional work items and 174 prior queue dispositions. This version adds TRACE, explanation competition and skill acquisition, seven-function cognitive qualification, ten-system comparative coverage and design closure. The canonical predecessor is v15.5. All proposals remain subject to their explicit qualification and admission rules.\nSee [T-V15-7], [TH-V15-7] and [A-V15-7].\n',
        'System':'[S-V15-7] Integrated candidate flow\nPropose, authorize, execute, observe, evaluate and retry or finish under one immutable grant. A separate bounded recovery allowance handles abort, uncertain completion and containment. Explanation competition selects authorized distinguishing observations; candidate skills require bounded qualification. Qualification, comparison and design closure proceed independently; combined claims require their applicable evidence. Component success does not admit failed composition. Exact requirements are in [T-V15-7] and [A-V15-7].\n',
        'Technical':'[T-V15-7] Runtime and cognitive candidate requirements\nThese extensions reuse existing Reason, execution/authority, Knowledge, Proof and Audit responsibilities; exact unresolved machine bindings remain unresolved.\n\n'+'\n\n'.join(sources[n] for n in names[:3]),
        'Theories':'[TH-V15-7] Comparative coverage program\n'+sources['COGNITIVE-COMPARE-CANDIDATE.md'],
        'Annexure':'[A-V15-7] Design closure and source provenance\n'+sources['DESIGN-CLOSURE-CANDIDATE.md']+'\nSource files and hashes:\n'+json.dumps({n:sha(s.encode()) for n,s in sources.items()},indent=2)+'\nThe five new programs are specified, not completed qualification or comparative findings. Earlier reviews apply only to their exact v15.6 inputs; they are not v15.7 approval.\n'
    }
    rows={};retention=[]
    for role,row in prior['files'].items():
        raw=(old/row['name']).read_bytes();assert sha(raw)==row['sha256']
        name=f'Garden_{role}_v15.7_FULL_CANDIDATE_2026-09-15.txt'
        header=(f'GARDEN v15.7 — FULL FIVE-FILE WORKING CANDIDATE — {role.upper()} — 2026-09-15\n'
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
    manifest={'schema':'GardenCanonicalSourceManifest/v1','release':'Garden v15.7','gsl':'v45.1','date':'2026-09-15','status':'WORKING_FIVE_FILE_CANDIDATE_NOT_CANONICAL','files':rows,'source_root_algorithm':canonical['source_root_algorithm'],'source_root_sha256':root,'predecessor_release':canonical['release'],'predecessor_source_root_sha256':canonical['source_root_sha256'],'retained_draft_source_root_sha256':prior['source_root_sha256']}
    dump(target/'SOURCE_MANIFEST.json',manifest)
    dump(ev/'RETENTION-RECEIPT.json',{'status':'PASS','scope':'Exact draft bytes retained, including its exact v15.5 source layers. No semantic admission.','files':retention})
    before=build_inventory(source_dir=old,manifest=prior,process_version='1.4')
    after=build_inventory(source_dir=target,manifest=manifest,process_version='1.4')
    old_refs={r for u in before.units for r in u.unresolved_references};refs={r for u in after.units for r in u.unresolved_references}
    dump(ev/'REFERENCE-CLOSURE-RECEIPT.json',{'status':'INCONCLUSIVE','source_root_sha256':root,'scope':'Existing bounded explicit anchor parser, not full semantic/GSL closure','unresolved':sorted(refs),'newly_unresolved':sorted(refs-old_refs),'counts':after.counts(),'qualified_review_units':0,'semantic_closure_complete':False})
    dump(ev/'SOURCE-INTEGRATION-RECEIPT.json',{'status':'CANDIDATE_MATERIALIZED_NOT_ADMITTED','repository_registration_base':'5a5fb60d54f9bb9310ea734657394c1c2de2f4fd','registration_base_scope':'Historical GitHub source-registration base, not the local build commit','workspace_commit':subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),'workspace_dirty':bool(subprocess.check_output(['git','status','--porcelain'],cwd=ROOT,text=True).strip()),'builder_sha256':sha(Path(__file__).read_bytes()),'new_programs':[{ 'path':'design_deltas/v15.7/'+n,'sha256':sha(s.encode()),'incorporated_complete_text':True} for n,s in sources.items()],'carried_forward_draft':prior['source_root_sha256'],'candidate_source_root_sha256':root,'comparison':'Retain five programs independently; no-addition leaves agreed work scattered, standalone replacement loses inherited work. Full cumulative draft selected; no superiority or completion claims.'})
    print(json.dumps({'root':root,'five_files':len(rows),'retention':all(r['exact'] for r in retention),'new_unresolved':len(refs-old_refs)}))

if __name__=='__main__':main()
