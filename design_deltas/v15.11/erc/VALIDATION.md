# v15.11 ERC candidate — validation and scout reconciliation

Date: 2026-09-23  
Observed repository base: `a9a1290e353a2c8c783edf5f5e8b4a121456a987`  
Scope: candidate packaging and source/evidence reconciliation only.

## What was checked

- Current v15.11 candidate set contains RCC, REP and SHR as separate noncanonical deltas.
- RCC already owns containment/exposure, cumulative/trajectory closure, assumption validity, continuing authority and positive/negative qualification behavior.
- Existing Garden source contains evidence/provenance and dependency machinery; prior candidate work also already discusses matched-budget improvement assessment and progress/stall measurement.
- The scout record itself marks SCOUT-20260923-004 as NEEDS_SOURCE_COMPARISON and reports no live security experiment.

## Scout finding dispositions

### SCOUT-20260917-001 — compact progress/retrieval
**Disposition:** REUSE / NO NEW v15.11 MODULE.

Reason: useful workflow discipline, but the scout itself labels the Garden-design effect NEEDS_SOURCE_COMPARISON. Existing Garden work already contains checkpoints, provenance and retrieval/requalification machinery. Treat future measured delivery results as implementation/process evidence, not as a new Garden theory.

### SCOUT-20260917-002 — useful completion metrics
**Disposition:** PARTIALLY_PRESENT / NO DUPLICATE MODULE.

Reason: existing candidate material already requires matched-budget comparison, DO_NOTHING, progress/stall measures, verification cost and repair-aware evaluation. Future implementation may add missing telemetry fields, but no new top-level v15.11 semantics are justified by the scout result alone.

### SCOUT-20260917-003 — capability dependencies / combinations
**Disposition:** REUSED AS SUPPORTING RATIONALE FOR ERC.

Reason: the dependency hypothesis becomes concrete in SCOUT-20260923-004: individually ordinary capabilities can compose into a materially different reachable path. ERC expresses only that narrow containment specialization.

### SCOUT-20260923-004 — transitive evaluation containment
**Disposition:** NEW EXPERIMENT-FIRST CANDIDATE V1511-ERC-001.

Reason: current searches found broad containment and dependency machinery but did not find an explicit existing contract that requires evaluation containment to enumerate transitive reachable service/credential/persistence edges under a cumulative action budget. Because the exact authorized v15.10 full target was not proven available in this repo state, this remains candidate-level and requires full semantic source comparison before any admission claim.

### Provenance experiment: unsupported promotions 6/10 -> 0/10
**Disposition:** SUPPORT EXISTING EVIDENCE/PROVENANCE PRACTICE; NO NEW MODULE.

The experiment is meaningful for scout recordkeeping, but Garden already distinguishes evidence/provenance, observations, assumptions and authority. Use this as implementation/evaluation evidence for record typing, not as proof of a new architecture gap.

### Protected audit-channel exploratory insight
**Disposition:** ALREADY SUBSTANTIALLY PRESENT / TEST IDEA ONLY.

The scout found existing whistleblower/witness-protection semantics. Preserve the proposed topology experiment (restricted vs open vs protected audit channel) as a future bounded test if useful; do not duplicate the principle.

### Stale-coordinator fencing exploratory idea
**Disposition:** NEEDS SOURCE/IMPLEMENTATION COMPARISON; NO v15.11 DELTA YET.

Garden already uses DesignEpoch/state binding. A monotonic fencing-token requirement may be valuable at a concrete write boundary, but no implementation comparison or failing test was established. First simulate overlapping coordinators and require stale-epoch mutation rejection.

## Validation status

Completed:
- candidate scope reduction;
- ownership/reuse analysis against accessible current repo material;
- no-new-top-level-architecture decision;
- explicit positive and negative conformance fixtures;
- scout finding deduplication.

Not completed:
- exact full v15.10 target-source closure;
- GSL runtime execution;
- bounded ERC staging experiment;
- independent security review;
- implementation binding;
- canonical admission.

Therefore **V1511-ERC-001 remains EXPERIMENT-FIRST and NONCANONICAL**.
