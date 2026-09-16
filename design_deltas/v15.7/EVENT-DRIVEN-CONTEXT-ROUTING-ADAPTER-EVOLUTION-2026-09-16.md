# Garden v15.7 EDCR adapter-evolution dependency — 2026-09-16

Status: NON_CANONICAL_CANDIDATE NOTE / PROPOSAL_ONLY / NO AUTHORITY / NO PROMOTION
Parent candidate: CAND-EDCR-001

The current public EDCR adapter carries ordinary `GardenNormalizedContextObservation/v1` records. It does not yet admit action-eligible artifacts, operational causal claims, protected/redacted provenance manifests, embedded GSL declarations, or other owner-qualified typed extensions.

If a future EDCR adapter revision introduces any such typed data, that revision must:

1. explicitly version the adapter schema/profile;
2. preserve the originating type, provenance and existing semantic owner through normalization and routing;
3. default ordinary observations to `NOT_ACTION_ELIGIBLE_AND_NOT_CAUSAL_UNLESS_EXPLICITLY_TYPED_AND_VALIDATED`;
4. invoke the applicable existing Compile, authority-provenance/intersection, causal-level, provenance-manifest, catalogue and assurance owners before downstream use;
5. fail closed on unrecognized, unresolved or incompletely bound typed extensions;
6. never let adapter parsing, routing, compression, model output or reviewer agreement create authority, increase causal strength, create protected status, or admit semantics;
7. add executable owner invocation only when the corresponding typed field/class actually enters the adapter.

The adapter transports owner-qualified data. It does not become a new authority source, causal owner, provenance owner or semantic owner.

This note activates no new runtime type and creates no canonical effect.
