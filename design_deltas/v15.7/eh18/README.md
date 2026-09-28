# EH-18 bounded machine qualification reference

Status: **REVIEW_PENDING / NONCANONICAL / NOT ACTIVATED**

This package continues existing work identity `WP-DESIGN-CLOSURE-V15-7`. It does not add a new safety principle. Garden v15.5 already owns critical-continuity containment, authority revocation, fallback handoff and recovery. Garden v15.7 `[T-EH-18]` already defines the single-tank example and `TEST-EH-18-001..007`; the unresolved item is executable binding and qualification.

## Exact bindings

- Canonical DesignEpoch: `Garden-v15.5@63561ce9fcd4a72f44af333662b342fd18c4e99930209c30c5f801bcc5c74598`.
- Candidate: Garden v15.7 source root `eb4d5306a8f7dcca75f8cf7d60f6441bdf5b35bccb86ac2362b33f241af1591a`.
- Candidate Technical SHA-256: `57535dc10839a6b278b0e05d257db5455e48cf376fdf1112f447e8b6257da68f`.
- Candidate anchor: `[T-EH-18]`; owner: `Capability.Trust.Safety`.
- Existing artifact contracts: `CriticalContinuityContainmentContract` (`SCHEMA-958DDFB791`) and `SafeControlHandoffReceipt` (`SCHEMA-8E127067C8`).

## Smallest implemented reference

`design_deltas/v15.7/eh18/reference/eh18_reference.py` provides a pure, candidate-contained pre-admission calculation:

1. exact Decimal arithmetic for the proposed `0.49 m` switch margin;
2. the delay/error-dependent recoverable center interval and closed-form reachable interval;
3. epoch and authority fencing for actuator commands;
4. distinct fail-closed results for stale, malformed, unknown, resource-unknown, violated-assumption, untrusted-state/actuator, outside-region and assurance-loss cases;
5. composed command admission that cannot remain `ACCEPTED` when any handoff prerequisite fails or is unknown;
6. an explicit minimum-risk-response frontier: failed handoffs require a qualified domain safety case, while this non-activating reference selects no action;
7. typed `PASS | FAIL | UNKNOWN | STALE | RESOURCE_UNKNOWN` prerequisite states, retained by owner-named field in the receipt rather than collapsed into booleans;
8. a typed primary-return disposition that preserves failed, unknown, stale, resource-unknown, malformed and safety-override blocks;
9. total fail-closed handling for wrong request object types and falsey non-Boolean safety-override values, which cannot escape as exceptions or compose to `ALLOWED`.

`ELIGIBLE_FOR_BOUNDED_SIMULATION` means only that the supplied case may proceed to the remaining trajectory, timing, proof and independent-review work. It is not `SAFE`, `PASS`, certification, authority or deployment permission.

## Normal and failure cases

- Normal bounded case: current epoch and authority, authenticated state, qualified fallback, trusted actuator, current dependency/timing/resource evidence, allowed error/delay, and a reachable interval contained by `[0,10]`.
- Failure cases: delayed or stale commands, missing authority, unqualified/shared-suspect fallback, unauthenticated state, invalid or unknown dependency/timing evidence, insufficient or unknown resource bounds, violated error/delay assumptions, untrusted actuator, state outside the recoverable region/envelope, or premature primary return.

## Acceptance and regression criteria

- The locally executable arithmetic, admission and fencing portions of `TEST-EH-18-001..007` have direct deterministic reference checks. These checks do not complete bounded dynamics analysis, measured trajectories/timing, numerical-error accounting, minimum-risk action selection or deployment qualification.
- `TEST-EH-18-004/005` failures cannot compose to command acceptance and explicitly return `REQUIRED_UNRESOLVED_DOMAIN_SAFETY_CASE` with no selected action or safety-case reference.
- `FAIL`, `UNKNOWN`, `STALE` and `RESOURCE_UNKNOWN` remain distinct for every handoff prerequisite and in primary-return gating; malformed runtime values remain `MALFORMED`; the complete named status snapshot remains visible in the receipt.
- Wrong request object types return a non-authorizing `MALFORMED` receipt instead of raising before a receipt exists. Primary-return gating accepts only an actual Boolean override flag; `None`, `0`, empty strings and other falsey substitutes cannot compose to `ALLOWED`.
- The candidate contract parses, binds to the exact v15.7 manifest and enumerates every public function in its one-file scope as either declared or explicit frontier.
- The blind-review packet includes exact, mechanically rechecked excerpts for `[T-EH-18]`, its seven tests, the canonical handoff contracts, `FUNC-001..010`, `RESULT-ALG-001..008`, `CCC-001..010` and `TEST-CCC-001..006`; reviewers need not trust the patch's paraphrase of its source obligations.
- Canonical v15.5 and all five v15.7 candidate source files/manifests remain byte-identical.
- No result sets `safety_certified=true`; no function performs an external effect.
- CCC-001..010, stale-epoch rejection and fresh-authorization recovery remain stronger controlling obligations.

## Costs, alternatives and unresolved work

Cost is one small pure reference module, one contract declaration and deterministic tests. Typed prerequisite states add modest caller/serialization complexity, but avoid the larger ambiguity and unsafe conversion risk of treating explicit failure, missing evidence, stale evidence and resource uncertainty as the same Boolean. Runtime/latency measurements, fallback hardware/resource floor, real actuator dynamics, common-cause independence, continuous-time proof, numerical-solver error, qualified minimum-risk action selection under a domain loss function/safety case, privacy-approved independent-family review and deployment qualification remain unresolved.

`DO_NOTHING` to Garden's design remains justified: the principle already exists. `DO_NOTHING` to qualification leaves EH-18 non-executable. Generic retry or unconditional shutdown is not an equivalent replacement because the domain safety case must decide minimum continuity versus shutdown.

Independent review status remains `REVIEW_BLOCKED_PROVIDER_PIPELINE`. No OpenRouter request or legacy worker dispatch is part of this package.
