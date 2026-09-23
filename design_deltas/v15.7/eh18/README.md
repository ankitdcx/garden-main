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
5. fresh-authority/revalidation checks before primary return.

`ELIGIBLE_FOR_BOUNDED_SIMULATION` means only that the supplied case may proceed to the remaining trajectory, timing, proof and independent-review work. It is not `SAFE`, `PASS`, certification, authority or deployment permission.

## Normal and failure cases

- Normal bounded case: current epoch and authority, authenticated state, qualified fallback, trusted actuator, current dependency/timing/resource evidence, allowed error/delay, and a reachable interval contained by `[0,10]`.
- Failure cases: delayed or stale commands, missing authority, unqualified/shared-suspect fallback, unauthenticated state, violated error/delay assumptions, untrusted actuator, unknown dependency/timing evidence, unknown resource bounds, state outside the recoverable region/envelope, or premature primary return.

## Acceptance and regression criteria

- `TEST-EH-18-001..007` have direct deterministic reference tests.
- The candidate contract parses, binds to the exact v15.7 manifest and enumerates every public function in its one-file scope as either declared or explicit frontier.
- Canonical v15.5 and all five v15.7 candidate source files/manifests remain byte-identical.
- No result sets `safety_certified=true`; no function performs an external effect.
- CCC-001..010, stale-epoch rejection and fresh-authorization recovery remain stronger controlling obligations.

## Costs, alternatives and unresolved work

Cost is one small pure reference module, one contract declaration and deterministic tests. Runtime/latency measurements, fallback hardware/resource floor, real actuator dynamics, common-cause independence, continuous-time proof, numerical-solver error, domain loss function, privacy-approved independent-family review and deployment safety case remain unresolved.

`DO_NOTHING` to Garden's design remains justified: the principle already exists. `DO_NOTHING` to qualification leaves EH-18 non-executable. Generic retry or unconditional shutdown is not an equivalent replacement because the domain safety case must decide minimum continuity versus shutdown.

Independent review status remains `REVIEW_BLOCKED_PROVIDER_PIPELINE`. No OpenRouter request or legacy worker dispatch is part of this package.
