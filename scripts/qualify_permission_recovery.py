#!/usr/bin/env python3
import hashlib, json, os, subprocess, sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
FILES=[ROOT/'implementation/garden_kernel/permission_recovery.py',ROOT/'implementation/tests/test_permission_recovery.py',
       ROOT/'reviews/v15.7/qualification/recovery-runtime/FUNCTION-CONTRACTS.json']
out=Path(sys.argv[1]) if len(sys.argv)>1 else ROOT/'reviews/v15.7/qualification/recovery-runtime/RUNTIME-RECEIPT.json'
env=dict(os.environ,PYTHONPATH=str(ROOT/'implementation'))
p=subprocess.run([sys.executable,'-m','unittest','implementation.tests.test_permission_recovery','-v'],cwd=ROOT,env=env,text=True,capture_output=True)
receipt={'schema':'GardenPermissionRecoveryRuntimeQualification/v1','result':'PASS' if p.returncode==0 else 'FAIL',
 'claim_boundary':'Single SQLite durability and atomic coordinator/reference-target transaction only; no distributed target, network partition, hardware, or exactly-once guarantee claimed.',
 'tla_trace_mapping':{'Claim':'claim','Admit':'admit','Revoke':'revoke','Dispatch':'dispatch','Ack':'acknowledge','LostAck':'dispatch(lose_ack=True)','Crash':'crash','Reconcile':'reconcile','LateDispatch':'stale attempt dispatch at target fence'},
 'formal_runtime_alignment':'Both the finite TLA model and runtime reference advance the per-effect target fence when a newer claim epoch is durably issued. Both reject an older worker immediately after issuance, before any newer dispatch. This is a bounded behavioral comparison, not an unbounded refinement proof.',
 'source_sha256':{str(x.relative_to(ROOT)):hashlib.sha256(x.read_bytes()).hexdigest() for x in FILES},
 'tests':{'command':p.args,'exit_code':p.returncode,'output_sha256':hashlib.sha256((p.stdout+p.stderr).encode()).hexdigest(),'output_tail':(p.stdout+p.stderr).splitlines()[-30:]},
 'qualified_semantics':['fresh permission recheck at commit boundary','monotonic persistent fencing epoch','effect identity idempotency','dispatch distinct from acknowledgement','lost acknowledgement remains uncertain','revoke before commit blocks','revoke after commit preserves effect','stale worker rejection','crash/restart reconciliation']}
out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps({'result':receipt['result'],'tests_exit':p.returncode}));raise SystemExit(p.returncode)
