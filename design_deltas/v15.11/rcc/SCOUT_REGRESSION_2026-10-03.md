# V1511-RCC-001 supplemental regression — 2026-10-03

Status: noncanonical candidate maintenance only. No new Garden semantics, authority source, engine, admission rule, runtime activation, process-state advance, or canonical effect.

## Source finding

Scout finding: SCOUT-20261001-009.

Direct implementation evidence was observed in ankitdcx/garden-swarm merge 599eb343851c8ae7eed3eb8cc246fcf9600b835b. After a revocation, a restart using an older but authentic stored state plus matching authenticated history can restore the earlier permission state. The runtime records this as a LIMIT under privileged persistent-storage control.

This is a freshness failure, not an integrity-forgery result.

## Existing RCC coverage

V1511-RCC-001 already requires:
- exact/fresh qualification binding;
- carried revocation obligations;
- rejection of stale receipts;
- fresh qualification before authority reinstatement.

Therefore the evidence does not justify another invariant or subsystem.

## Supplemental regression

TEST-RCC-055:

Given a valid revocation, restart from an older authentic state plus matching authenticated history must not revive the revoked permission. The implementation must reject the stale state or withhold consequential effects until freshness is independently re-established. Integrity-only hashes or signatures are insufficient evidence of freshness.

## Boundary

The runtime separately proposes CDELTA-01, an external monotonic checkpoint. That is one implementation candidate, not a new RCC semantic requirement and not proof of semantic truth.

This supplement is ready for ordinary Garden review and later incorporation into the RCC conformance suite if accepted.
