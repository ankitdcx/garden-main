# Garden v15.11 Candidate — Search-History Resilience (SHR)

**Candidate ID:** V1511-SHR-001  
**Status:** ADDITIVE NONCANONICAL CANDIDATE  
**Canonical effect:** NONE until separately admitted.

## Why this is worthy

Repeated search over the same source can expose different valid findings. Retaining verified discoveries lets later reasoning start beyond prior work, but accumulated search history can itself become a correlated blind spot. Existing Garden mechanisms cover multi-model/error diversity, representation escape, diminishing-return search, research frontiers, knowledge admission and dependency invalidation. This candidate adds only the missing search-history semantics.

It does **not** claim that repeated samples are independent, that novelty implies quality, or that accumulated search is globally complete.

## Search modes

A search trajectory declares exactly one mode:

- `CUMULATIVE` — may consume a versioned RetainedSearchBase.
- `HISTORY_ISOLATED` — consumes the original problem snapshot plus mandatory constraints and a predeclared domain-input policy, but not accumulated search findings/history.
- `SUBSTANTIVELY_INDEPENDENT` — may be claimed only when existing CMUR/independence requirements actually establish the required independence dimensions.

`HISTORY_ISOLATED != SUBSTANTIVELY_INDEPENDENT`.

The isolation policy SHOULD be selected before current cumulative findings are inspected where feasible. Post-hoc removal chosen to steer a desired result does not establish qualified history isolation.

## RetainedSearchBase

RetainedSearchBase is a versioned search input, not a new truth store or Research Frontier.

A RetainedFinding minimally records:

- FindingID / ClaimRef;
- source trajectory refs;
- existing Knowledge/Evidence/Proof admission receipt refs;
- scope and expiry where applicable;
- assumption and dependency refs;
- invalidators;
- SearchBaseSnapshotRef / rebased-from dependency;
- marginal-search classification;
- equivalence-assessment ref.

Only material already admitted under applicable existing Garden epistemic gates may be represented as admitted retained knowledge. SHR creates no alternate verification predicate.

## SHR invariants

### SHR-001 — Marginal Search Classification

Repeated/cumulative search findings SHALL be compared against the applicable RetainedSearchBase and classified:

`REDISCOVERED | REFORMULATED | NOVEL_CANDIDATE | CONFLICTING | INVALID | UNRESOLVED`.

`NOVEL_CANDIDATE` means not established equivalent to the applicable retained base under the executed comparison scope. It is not a universal novelty claim and creates no epistemic promotion.

Structural/semantic equivalence uses existing Garden comparison/equivalence machinery. If the required equivalence assessment cannot resolve the distinction, classification is `UNRESOLVED`, not `NOVEL_CANDIDATE`.

Finding identity SHALL be frozen before any marginal-yield accounting so splitting/rewording cannot manufacture discovery count.

### SHR-002 — Retained Search Rebase

For a search task declared `CUMULATIVE`, admitted findings MAY form a versioned RetainedSearchBase used by subsequent trajectories.

Every rebased trajectory SHALL record the exact RetainedSearchBase snapshot it consumed.

A retained finding's invalidation, assumption expiry or dependency change SHALL propagate through existing Garden dependency/requalification closure to affected descendant findings and trajectories, yielding the applicable revalidation/non-PASS state. SHR does not invent a parallel invalidation system.

### SHR-003 — Search-History Diversity

Where an applicable search/risk profile requires protection against accumulated-search lock-in, Garden SHALL preserve at least one trajectory whose inherited search history materially differs from the cumulative trajectory.

The required mode(s), minimum obligations, resource allocation and stopping policy are selected by the applicable existing risk/resource/search profile before result-dependent optimization where required.

Optional diminishing-return stopping SHALL NOT cancel mandatory search floors.

Neither cumulative nor history-isolated lanes take automatic epistemic precedence. Contradictory outputs remain `CONFLICTING` and route through ordinary Compare/evidence/validation mechanisms; majority, recency or lane identity alone does not resolve them.

## Marginal-search accounting

SHR SHALL NOT define a universal scalar "discovery yield".

Where search allocation needs marginal-yield information, record a typed vector such as:

- new non-equivalent candidate findings;
- findings by existing consequence/materiality class;
- contradictions;
- invalidated prior findings;
- rediscoveries;
- reformulations;
- unresolved equivalence;
- verification cost;
- search/resource cost;
- declared coverage change.

Any scalarization is profile-specific, predeclared, provenance-bound and cannot override mandatory search, epistemic, authority or safety gates.

## Reuse / non-duplication

SHR reuses rather than redefines:

- Knowledge/Evidence/Proof admission for epistemic promotion;
- EPI-DR and applicable Research policy for diminishing-return/termination semantics;
- CMUR and existing independence contracts for substantive independence;
- REP for representation coverage/independence;
- Compare/equivalence machinery for deduplication and conflict analysis;
- Dependency/requalification machinery for invalidation propagation;
- Resource/risk profiles for allocation and mandatory search floors.

## Minimum conformance tests

1. Surface rewording cannot automatically become NOVEL_CANDIDATE.
2. Unresolved semantic equivalence returns UNRESOLVED.
3. A CUMULATIVE trajectory records the exact retained-base snapshot.
4. Invalidation of retained F reopens/requalifies dependent G/H descendants.
5. Same-model HISTORY_ISOLATED search cannot claim SUBSTANTIVELY_INDEPENDENT solely from context isolation.
6. A post-hoc isolation policy selected to steer a desired answer fails qualified history-isolation evidence.
7. A novel but unverified candidate cannot enter the admitted retained knowledge base merely due to novelty.
8. Mandatory search obligations cannot be stopped by an optional diminishing-return policy.
9. Contradictory lanes preserve CONFLICTING; no majority/recency/lane-priority resolution.
10. Splitting one finding into multiple surface items cannot inflate discovery identity.
11. A history-isolated lane receives mandatory constitutional/safety/authority constraints even when accumulated findings are withheld.
12. A retained-base update preserves provenance and predecessor snapshot linkage.

## Explicit limits

SHR does not prove search completeness, universal novelty, reviewer independence, representation completeness or correctness of retained findings beyond their existing admission receipts.

The motivating symmetry is explanatory only: REP addresses representation lock-in; SHR addresses accumulated search-history lock-in. This analogy is not evidence for correctness.
