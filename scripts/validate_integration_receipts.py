#!/usr/bin/env python3
"""Validate load-bearing Garden integration-decision admission rules."""
from __future__ import annotations
import argparse, json
from pathlib import Path
VERDICTS={"ACCEPT_IMPLEMENTATION","ACCEPT_DESIGN_DELTA_CANDIDATE","ALREADY_COVERED","REJECT_INSUFFICIENT_EVIDENCE","REJECT_DUPLICATE","DEFER"}
def validate(data:dict)->list[str]:
    errors=[]
    for key in ["schema","decision_id","finding_id","created_at","source","severity","verdict","reason","evidence","affected","uncertainty","what_would_overturn","outcome"]:
        if key not in data: errors.append(f"missing required field: {key}")
    if data.get("schema")!="IntegrationDecisionReceipt/v1": errors.append("schema must be IntegrationDecisionReceipt/v1")
    if data.get("verdict") not in VERDICTS: errors.append("unsupported verdict")
    source=data.get("source") or {}
    for key in ("agent","agent_family","task_id"):
        if not source.get(key): errors.append(f"source.{key} is required")
    evidence=data.get("evidence") or {}
    if "supplied_search_trace" not in evidence: errors.append("evidence.supplied_search_trace is required")
    if "whole_source_search_trace" not in evidence: errors.append("evidence.whole_source_search_trace is required (null when not applicable)")
    reproduction=evidence.get("reproduction") or {}
    if "required" not in reproduction or "status" not in reproduction: errors.append("evidence.reproduction requires required + status")
    severity=data.get("severity"); semantic=data.get("verdict")=="ACCEPT_DESIGN_DELTA_CANDIDATE"; high=severity in {"HIGH","CRITICAL"}
    if (high or semantic) and reproduction.get("required") is not True: errors.append("HIGH/CRITICAL or semantic delta requires independent reproduction flag")
    if (high or semantic) and reproduction.get("status") not in {"REPRODUCED","UNAVAILABLE"}: errors.append("required reproduction must be REPRODUCED or explicitly UNAVAILABLE before admission")
    if semantic and not data.get("do_nothing_comparison"): errors.append("semantic design delta requires do_nothing_comparison")
    if semantic and not (data.get("outcome") or {}).get("delta_ids"): errors.append("semantic design delta requires at least one delta_id")
    if data.get("claim_class") in {"CANONICAL_ABSENCE","CANONICAL_COVERAGE"}:
        trace=evidence.get("whole_source_search_trace")
        if not trace: errors.append("canonical absence/coverage claim requires whole-source search trace")
        elif trace.get("coverage")!="ALL_FIVE_CURRENT_CANONICAL_FILES_LEXICAL": errors.append("whole-source search trace must cover all five current canonical files")
        elif len(trace.get("sources") or [])!=5: errors.append("whole-source search trace must bind exactly five source files")
    return errors
def main()->int:
    p=argparse.ArgumentParser(); p.add_argument("paths",nargs="+"); args=p.parse_args(); failed=False
    for raw in args.paths:
        path=Path(raw); data=json.loads(path.read_text(encoding="utf-8")); errors=validate(data)
        if errors:
            failed=True; print(f"FAIL {path}"); [print(f"  - {e}") for e in errors]
        else: print(f"PASS {path}")
    return 1 if failed else 0
if __name__=="__main__": raise SystemExit(main())
