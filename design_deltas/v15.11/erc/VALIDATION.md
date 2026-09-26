# v15.11 ERC candidate — validation and scout reconciliation

Date: 2026-09-26  
Revision: 1.1  
Observed repository base: `a9a1290e353a2c8c783edf5f5e8b4a121456a987`  
Scope: candidate packaging and source/evidence reconciliation only.

## What was checked

- Current v15.11 candidate set on the observed base contains RCC, REP and SHR as separate noncanonical deltas.
- RCC already owns containment/exposure, cumulative/trajectory closure, assumption validity, continuing authority and positive/negative qualification behavior.
- Canonical Garden v15.5 already contains broad Security, Evidence/Provenance, incident-learning, dependency/requalification, uncertainty and DO_NOTHING owners.
- Searches of the observed repository did not find the seven-field ERC fixture projection `fixture_id, surface_class, trigger_class, causal_role, evidence_outcome_class, source_lineage_refs, unknowns` as one existing evaluation contract.
- Existing Garden semantics already require source/evidence binding and distinguish report completion from substantive closure in multiple candidate/process artifacts; therefore false-success evidence does not justify a new top-level completion subsystem.
- Existing dependency/freshness semantics already support requalification on material model/harness change; version-scoped prompt/scaffold findings are retained as a regression requirement, not a new owner.

## Scout finding dispositions

### SCOUT-20260917-001 — compact progress/retrieval
**Disposition:** REUSE / NO NEW v15.11 MODULE.

The scout's three-run checkpoint test supports its own compact-resumption discipline. It does not establish a Garden-wide speedup or justify new architecture.

### SCOUT-20260917-002 — useful completion metrics / false-success resistance
**Disposition:** PARTIALLY_PRESENT; ADD ERC EVIDENCE CONSTRAINT, NO NEW MODULE.

Garden already has typed evidence/receipts and explicit bounded-completion semantics. New evidence that agents/judges can confidently misreport success strengthens a narrow rule for ERC fixtures: PASS/completion must bind to the environment/task evidence required by the fixture. Agent language or judge impression alone cannot substitute for stronger required evidence.

Added: ERC-010 and TEST-ERC-012 equivalent fixture.

### SCOUT-20260917-003 — capability dependencies / model-harness transfer
**Disposition:** REUSED AS SUPPORTING RATIONALE / REGRESSION TEST.

The transitive-combination finding supports ERC itself. Cross-version intervention reversal reinforces existing dependency/freshness semantics: model/harness changes trigger re-test when they are material to an intervention result.

Added: model/harness binding in EvaluationFixtureEvidenceRecord and TEST 15. No new invariant owner is created for generic versioning.

### SCOUT-20260923-004 — transitive evaluation containment
**Disposition:** EXPERIMENT-FIRST CANDIDATE V1511-ERC-001, retained.

Scout triage source comparison is now materially stronger than on 23 September: canonical v15.5 contains broad containment owners, but no exact evaluation-specific transitive reachability profile was found for dead drops, metadata, credential/identity minting, restart persistence and cumulative probing.

A synthetic graph test found four multi-hop paths missed by a direct-boundary baseline and zero on an isolated control. This supports the graph-check mechanism only; it is not staging/runtime containment evidence.

### SCOUT-20260925-005 — incident records as evaluation-coverage audit
**Disposition:** TESTED_SUPPORTED; INCORPORATE MINIMAL FIELD PROJECTION.

A bounded manual projection classified all ten ERC conformance fixtures. Eight were no-adversary failure tests and two positive/authority controls; all ten were synthetic demonstrations. The surviving omission was not a missing security invariant but implicit metadata.

Added under existing Evaluation/Evidence owners:
`EvaluationFixtureEvidenceRecord` projection with:
- fixture_id;
- surface_class;
- trigger_class;
- causal_role;
- evidence_outcome_class;
- source_lineage_refs;
- environment/task evidence refs;
- model/harness/setup ref;
- conditional stochastic-measurement ref;
- unknowns.

This field set audits coverage; it does not estimate deployment risk.

### Security metric validity — repeated runs / variance
**Disposition:** ADD CONDITIONAL EVIDENCE RULE; NO NEW MODULE.

The 26 September scout source reports widespread omission of repeated runs/variance in agent-security evaluations and shows that a small true rate difference can be misranked under finite sampling. Garden already owns uncertainty/evidence. ERC therefore adds only the specialization: when stochasticity materially affects a comparative conclusion, bind the setup and sufficient repetition/uncertainty evidence for that claim. No universal run count is invented.

Added: ERC-011 and TEST 13.

### Incident corpus prevalence / reporting incentives
**Disposition:** ADD CLAIM BOUNDARY; NO NEW MODULE.

Public/voluntary incident corpora are useful for finding omitted surfaces, not for converting raw counts into deployment prevalence or vendor risk without denominator/selection evidence.

Added: ERC-012 and TEST 14. Existing whistleblower/incident-learning semantics remain controlling.

### DO_NOTHING conditional reversal
**Disposition:** ALREADY PRESENT / NO ERC CHANGE.

Canonical Garden already models DO_NOTHING as a real comparator with evolving environment, uncertainty and monitoring. The scout re-analysis reinforces condition-stratified comparison but does not justify duplicate semantics.

### StateComp / DTOC context compression
**Disposition:** NO v15.11 ERC CHANGE.

These results support reversible, model-bound context management but are outside ERC and remain transfer-limited. They do not justify a new Garden module from this evidence.

### Protected audit-channel exploratory insight
**Disposition:** ALREADY SUBSTANTIALLY PRESENT / TEST IDEA ONLY.

Existing whistleblower/witness-protection and incident-learning owners cover the principle. No duplicate rule added.

### Stale-coordinator fencing exploratory idea
**Disposition:** NEEDS IMPLEMENTATION COUNTEREXAMPLE / NO v15.11 DELTA YET.

DesignEpoch/state binding exists. Add a monotonic fencing-token rule only if a concrete overlapping-run test demonstrates a stale writer can still commit.

## Validation status

Completed:
- candidate scope reduction;
- source/owner reuse comparison against the observed repository;
- no-new-top-level-architecture decision;
- synthetic transitive-graph mechanism test from scout evidence;
- ten-fixture coverage-metadata projection;
- explicit positive/negative conformance fixtures;
- scout finding deduplication;
- revision 1.1 evidence/measurement hardening.

Not completed:
- exact full v15.10/v15.11 target-source closure for admission;
- GSL runtime execution;
- bounded no-secrets ERC staging experiment;
- independent security review;
- independent repetition of the ten-fixture metadata mapping;
- implementation binding;
- canonical admission.

Therefore **V1511-ERC-001 revision 1.1 remains EXPERIMENT-FIRST and NONCANONICAL**.
