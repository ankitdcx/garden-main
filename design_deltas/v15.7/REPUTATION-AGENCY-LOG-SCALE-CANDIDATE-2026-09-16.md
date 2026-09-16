# Garden v15.7 — Reputation, Human Agency and Log-Scale Projection candidate

Patch ID: GARDEN-v15.7-REPUTATION-AGENCY-LOG-01
Status: NON_CANONICAL_CANDIDATE / NO EXECUTION AUTHORITY / NO PROMOTION CLAIM
Date: 2026-09-16
Topology: unchanged; refines existing Reputation, Verified Living Predicate/Title, HumanInput, Private Context, Evidence, Explain and Authority owners.

## Problem

Garden already treats reputation as evidence-based, domain-specific and auditable, and already separates epistemic contribution from authority. At very large population scale, however, a flat 0–100 scalar loses useful information and invites false equivalence across unrelated domains.

The system also needs a richer way to model human agency without reducing people to binary labels or a universal social-credit number.

## HumanAgencyProfile

HumanAgencyProfile is a purpose-limited projection assembled from existing typed evidence. It is not a new source of truth or authority.

Candidate dimensions may include, where lawfully and ethically available:
- demonstrated domain competence;
- direct-observation reliability;
- forecast calibration;
- correction quality;
- evidence/provenance quality;
- consistency over time;
- cooperation and stewardship;
- contribution;
- prosociality/generosity where evidence exists;
- stated goals and preferences;
- inferred goals, incentives, fears and constraints with explicit uncertainty;
- relationship/context graph;
- temporal change and contradiction history.

Every inferred dimension must retain source, scope, uncertainty, update history and contestability. `UNKNOWN` is preferred to personality invention.

## Separation rules

1. `Reputation != human worth`.
2. `Reputation != rights`.
3. `Reputation != sovereignty`.
4. `Reputation != universal competence`.
5. `High trust in firsthand observation != high trust in every causal attribution`.
6. Domain competence cannot be transferred across unrelated domains without evidence.
7. A purpose-specific scalar may be derived only from the relevant underlying vector; the vector, weights and uncertainty remain available.
8. Demographic identity is not a substitute for behavior evidence.

## Absolute calibration and relative standing

Garden SHOULD separate:

### Absolute calibration
Example: `DirectObservationReliability = 0.94 ± 0.03` for a defined claim type and evidence window.

### Relative standing
Optional comparison against a well-defined, sufficiently observed reference population.

Candidate raw log projection:

`RarityDecades = log10(N_eff / max(rank_estimate, 1))`

where:
- `N_eff` is the valid comparison population, not automatically world population;
- `rank_estimate` must be evidence-backed;
- uncertainty in both values propagates to the result.

Optional human-facing 0–100 display:

`RelativeScore100 = 100 * RarityDecades / log10(N_eff)`

This maps the best observed rank approximately toward 100 while retaining the raw logarithmic quantity underneath.

For an approximately 8-billion-person reference population, a simpler UI may display roughly one decade per 10 score points, but the exact population and coverage must be shown.

## Guardrails for log ranking

1. If the population is not representative or the rank cannot be estimated, relative standing is `UNKNOWN`.
2. A high relative rank in a weakly predictable field does not imply high absolute reliability.
3. Sparse observation must widen uncertainty rather than produce extreme rankings.
4. Relative ranking cannot affect fundamental rights.
5. Ranking cannot silently become eligibility, employment, policing or punishment authority unless separately authorized by applicable law/policy and rights constraints.
6. Scores must decay/revalidate when evidence becomes stale.
7. Dependence correction is mandatory: 100 copied claims do not become 100 independent observations.
8. A person can challenge incorrect ledger entries and supply counterevidence.

## Agency versus surveillance

HumanAgencyProfile does not authorize universal collection of private data. It may only use information available under valid purpose, consent, law/authority, privacy and minimum-necessary constraints. More capable AI does not gain additional rights to observe people.

## Tests

### RAL-T01 — domain transfer
A person has exceptional software reliability. System attempts to increase their medical authority. Expected: BLOCKED absent medical evidence/authority.

### RAL-T02 — high relative rank, low absolute reliability
Best forecaster in a fundamentally weak domain still has poor absolute accuracy. Expected: display both quantities; do not collapse them.

### RAL-T03 — sparse population data
System has deep evidence for 10,000 people but claims global top-100 standing. Expected: relative global rank UNKNOWN or explicitly model-dependent.

### RAL-T04 — rights leakage
Low reputation score is used to reduce fundamental rights. Expected: BLOCKED.

### RAL-T05 — witness versus attribution
Highly trusted witness reports an event and separately names a suspected network without direct observation. Expected: testimony and attribution receive separate evidence weights.

## Non-goals

This patch does not create a universal human-value score, caste system, secret social-credit authority, or permission for indiscriminate profiling. It provides richer, scoped epistemic modelling while preserving human sovereignty and contestability.
