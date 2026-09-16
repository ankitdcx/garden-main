#!/usr/bin/env python3
"""Run bounded TLC checks with pinned tool identity and typed outcomes."""
from __future__ import annotations
import argparse, hashlib, json, re, subprocess, tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];MODEL=ROOT/'formal/permission_recovery/Recovery.tla';CONFIG=ROOT/'formal/permission_recovery/Recovery.cfg'
EXPECTED_JAR_SHA256='20322939d1b55bb0a3f674ab34bb69b87c711a6b35559d32445cb7d7f6d3bb58'
DOWNLOAD_URL='https://github.com/tlaplus/tlaplus/releases/download/v1.8.0/tla2tools.jar'
def sha256(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def classify(output,returncode,*,negative=False):
    generated=re.search(r'(\d+) states generated',output);distinct=re.search(r'(\d+) distinct states found',output);depth=re.search(r'depth of the complete state graph search is (\d+)',output)
    complete='Model checking completed. No error has been found.' in output and returncode==0
    violations=re.findall(r'Invariant\s+(\S+)\s+is violated',output);named=violations==['NoStaleFenceAccepted'];any_bad=bool(violations);counts=all(x is not None for x in (generated,distinct,depth))
    if negative and named and counts and returncode==12:outcome,reason='COUNTEREXAMPLE','EXPECTED_NOSTALEFENCEACCEPTED_VIOLATION'
    elif negative and named:outcome,reason='INCOMPLETE','COUNTEREXAMPLE_EXIT_OR_COUNTS_MISMATCH'
    elif not negative and complete and counts and not any_bad:outcome,reason='COMPLETED_WITHIN_BOUNDS','TLC_SUCCESS_MARKER_AND_COMPLETE_COUNTS'
    elif any_bad:outcome,reason='COUNTEREXAMPLE','UNEXPECTED_OR_WRONG_INVARIANT_COUNTEREXAMPLE'
    else:outcome,reason='INCOMPLETE','TOOL_ERROR_OR_PARSE_INCOMPLETE'
    return {'outcome':outcome,'reason':reason,'exit_code':returncode,'states_generated':int(generated.group(1)) if generated else None,'distinct_states':int(distinct.group(1)) if distinct else None,'search_depth':int(depth.group(1)) if depth else None,'violated_invariant':'NoStaleFenceAccepted' if named else None,'output_sha256':hashlib.sha256(output.encode()).hexdigest(),'output_tail':output.splitlines()[-40:]}
def run_tlc(jar,cfg,timeout,*,negative=False):
    with tempfile.TemporaryDirectory(prefix='garden-tlc-') as metadir:
        command=['java','-cp',str(jar),'tlc2.TLC','-cleanup','-noGenerateSpecTE','-metadir',metadir,'-deadlock','-config',str(cfg),str(MODEL)]
        try:p=subprocess.run(command,cwd=MODEL.parent,text=True,capture_output=True,timeout=timeout)
        except subprocess.TimeoutExpired as exc:
            output=(exc.stdout or '')+(exc.stderr or '');output=output.decode(errors='replace') if isinstance(output,bytes) else output
            result=classify(output,124,negative=negative);result.update(outcome='INCOMPLETE',reason='TIMEOUT',timeout_seconds=timeout,command=command);return result
        except OSError as exc:
            result=classify(str(exc),127,negative=negative);result.update(outcome='INCOMPLETE',reason='TOOL_EXECUTION_ERROR',timeout_seconds=timeout,command=command);return result
    result=classify(p.stdout+p.stderr,p.returncode,negative=negative);result.update(timeout_seconds=timeout,command=command);return result
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--tlc-jar',required=True);ap.add_argument('--output',required=True);ap.add_argument('--timeout',type=float,default=60.0);ap.add_argument('--expected-jar-sha256',default=EXPECTED_JAR_SHA256);a=ap.parse_args()
    jar=Path(a.tlc_jar).resolve();actual=sha256(jar) if jar.is_file() else None
    receipt={'schema':'GardenPermissionRecoveryBoundedCheck/v1','scope':'Two workers, one idempotent effect target, epochs 0..3.','claim_boundary':'Finite-state TLC exploration only; not an unbounded refinement proof, production validation, or hardware qualification.','model':{'path':str(MODEL.relative_to(ROOT)),'sha256':sha256(MODEL)},'config':{'path':str(CONFIG.relative_to(ROOT)),'sha256':sha256(CONFIG)},'checker':{'path':'scripts/check_permission_recovery.py','sha256':sha256(Path(__file__))},'tool_provenance':{'download_url':DOWNLOAD_URL,'license':'UNKNOWN_NOT_ASSERTED_BY_THIS_RECEIPT','expected_jar_sha256':a.expected_jar_sha256,'observed_jar_sha256':actual}}
    if a.timeout<=0 or a.expected_jar_sha256!=EXPECTED_JAR_SHA256 or actual!=EXPECTED_JAR_SHA256:
        reason='INVALID_TIMEOUT' if a.timeout<=0 else ('CONFIGURED_PIN_MISMATCH' if a.expected_jar_sha256!=EXPECTED_JAR_SHA256 else 'TOOL_SHA256_MISMATCH')
        receipt.update(positive={'outcome':'INCOMPLETE','reason':reason},negative_control={'outcome':'INCOMPLETE','reason':'NOT_RUN'},adjudication={'result':'INCOMPLETE'})
    else:
        try:h=subprocess.run(['java','-cp',str(jar),'tlc2.TLC','-help'],text=True,capture_output=True,timeout=a.timeout)
        except (subprocess.TimeoutExpired,OSError) as exc:
            receipt.update(positive={'outcome':'INCOMPLETE','reason':'TOOL_VERSION_PROBE_FAILED','detail':type(exc).__name__},negative_control={'outcome':'INCOMPLETE','reason':'NOT_RUN'},adjudication={'result':'INCOMPLETE'})
            out=Path(a.output);out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps({'result':'INCOMPLETE'}));return 2
        receipt['tool_provenance']['version']=next((x.strip() for x in (h.stdout+h.stderr).splitlines() if 'Version' in x),'UNKNOWN')
        if receipt['tool_provenance']['version']=='UNKNOWN':
            receipt.update(positive={'outcome':'INCOMPLETE','reason':'TOOL_VERSION_PROBE_FAILED'},negative_control={'outcome':'INCOMPLETE','reason':'NOT_RUN'},adjudication={'result':'INCOMPLETE'})
            out=Path(a.output);out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps({'result':'INCOMPLETE'}));return 2
        positive=run_tlc(jar,CONFIG,a.timeout);text=CONFIG.read_text().replace('EnforceFence = TRUE','EnforceFence = FALSE')
        with tempfile.NamedTemporaryFile('w',suffix='.cfg',dir=MODEL.parent,delete=False) as f:f.write(text);negcfg=Path(f.name)
        try:negative=run_tlc(jar,negcfg,a.timeout,negative=True)
        finally:negcfg.unlink(missing_ok=True)
        negative.update(mutation='EnforceFence=FALSE',expected='NoStaleFenceAccepted counterexample')
        result='PASS' if positive['outcome']=='COMPLETED_WITHIN_BOUNDS' and negative['outcome']=='COUNTEREXAMPLE' and negative['violated_invariant']=='NoStaleFenceAccepted' else ('INCOMPLETE' if 'INCOMPLETE' in {positive['outcome'],negative['outcome']} else 'FAIL')
        receipt.update(positive=positive,negative_control=negative,adjudication={'result':result,'positive_complete':positive['outcome']=='COMPLETED_WITHIN_BOUNDS','named_negative_control_detected':negative.get('violated_invariant')=='NoStaleFenceAccepted'})
    out=Path(a.output);out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps({'result':receipt['adjudication']['result']}));return 0 if receipt['adjudication']['result']=='PASS' else 2
if __name__=='__main__':raise SystemExit(main())
