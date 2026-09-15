#!/usr/bin/env python3
"""Authoritative update gate. Run this file from a trusted BASE checkout only.

Candidate files are Git blob data, never imports or executable programs.
The caller must pin the checkout and head to the GitHub event's base/head OIDs.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import subprocess
import sys

TRUSTED_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TRUSTED_ROOT/'implementation'))
from garden_kernel.base_admission import base_pinned_attestation, change_bindings
from garden_kernel.evolution_transport import evaluate_production_request, load_authority_registry, load_source_identity
from garden_kernel.evolution_trust import governance_receipt_from_changed_paths, PROTECTED_CONSTITUTIONAL_PATHS, PROTECTED_CONSTITUTIONAL_PREFIXES

# Executed from the already-admitted base; candidate edits cannot weaken this set.
PROTECTED_CONSTITUTIONAL_PATHS.update({
    'scripts/gate_hourly_evolution.py':'ACTION_GATE_RULES',
    'scripts/gate_human_admitted_update.py':'ACTION_GATE_RULES',
    'implementation/garden_kernel/base_admission.py':'HUMAN_ATTESTATION_RULES',
    'implementation/garden_kernel/evolution_trust.py':'CONSTITUTIONAL_CLASSIFICATION_RULES',
})
PROTECTED_CONSTITUTIONAL_PREFIXES.update({
    'implementation/garden_kernel/':'TRUSTED_VERIFIER_DEPENDENCIES',
    '.github/workflows/':'ACTION_GATE_EXECUTION_RULES',
    'governance/human_admissions/':'HUMAN_ATTESTATION_RULES',
})


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--base',required=True);p.add_argument('--head',required=True)
    p.add_argument('--repository',required=True);p.add_argument('--pull-request',type=int,required=True)
    p.add_argument('--output',required=True);a=p.parse_args()
    report={'schema':'GardenTrustedBaseUpdateGate/v1','status':'REJECT','base':a.base,'head':a.head,
            'repository':a.repository,'pull_request':a.pull_request,'receipts':[],
            'execution_boundary':'Base checkout only; candidate blobs are data; no signature or independent review claimed.'}
    try:
        def git(*args):return subprocess.check_output(['git',*args],cwd=TRUSTED_ROOT,text=True).strip()
        base=git('rev-parse',a.base+'^{commit}');head=git('rev-parse',a.head+'^{commit}')
        if git('rev-parse','HEAD') != base:
            raise ValueError('verifier checkout is not the event base commit')
        if git('status','--porcelain','--untracked-files=no'):
            raise ValueError('trusted checkout has tracked modifications')
        subprocess.run(['git','merge-base','--is-ancestor',base,head],cwd=TRUSTED_ROOT,check=True)
        identity=load_source_identity(TRUSTED_ROOT/'canonical/current/SOURCE_MANIFEST.json')
        authorities=load_authority_registry(TRUSTED_ROOT/'governance/evolution_authority_registry.json',identity)
        changes=change_bindings(TRUSTED_ROOT,base,head)
        requests=[x for x in git('ls-tree','-r','--name-only',head,'reviews/evolution/production').splitlines() if x.endswith('.json')]
        if not requests:raise ValueError('no production actions')
        for path in requests:
            request=json.loads(git('show',head+':'+path))
            action_id=request['action']['action_id']
            gov=governance_receipt_from_changed_paths(action_id=action_id,design_epoch=identity.design_epoch,
                source_root_sha256=identity.source_root_sha256,changed_paths=changes,base_ref=base,head_ref=head)
            receipts,attestors = (), {}
            if gov['tier'] == 'CONSTITUTIONAL':
                receipts,attestors=base_pinned_attestation(root=TRUSTED_ROOT,base_ref=base,head_ref=head,
                    repository=a.repository,pull_request=a.pull_request,request=request,design_epoch=identity.design_epoch,
                    source_root_sha256=identity.source_root_sha256)
            result=evaluate_production_request(request,identity,authorities,trusted_governance_receipt=gov,
                trusted_attestation_receipts=receipts,trusted_attestors=attestors)
            report['receipts'].append(result)
        report['status']='ALLOW' if all(x['decision']=='ALLOW' for x in report['receipts']) else 'REJECT'
    except Exception as exc:
        report['error']=f'{type(exc).__name__}: {exc}'
    out=Path(a.output);out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({'status':report['status'],'checked':len(report['receipts']),'error':report.get('error')}))
    return 0 if report['status']=='ALLOW' else 1

if __name__=='__main__':raise SystemExit(main())
