# Garden v15.11 candidate: Recursive Control Closure

Candidate: **V1511-RCC-001**  
Patch: **GARDEN-RCI-RCC-2026-09-22**, revision 1.4  
Status: **CANDIDATE_DESIGN — NOT CANONICALLY ADMITTED**

[Full candidate specification](GARDEN_v15.11_RCC_CANDIDATE.md) · [Manifest](CANDIDATE_MANIFEST.json) · [Validation and remaining work](VALIDATION.md)

## What this fixes, in simple words

An AI upgrade should go ahead only while its safeguards still work for what it can now do.

- Small changes must be checked together, so thousands of small edits cannot hide one dangerous change.
- The system proposing an upgrade must not control the people or systems approving it.
- The checker must be able to check the actual change. A familiar checker does not automatically remain good enough forever.
- If an old safeguard stops working, permissions depending on it pause. Essential work needs a separately safe handover.
- Saying an action is forbidden is different from actually preventing it.
- A system cannot approve removing its own final safeguards.
- Improvements that meet the requirements must still be allowed through.

## Is it worth adding?

Yes, as a focused design hardening candidate. It adds concrete rules for what must happen when AI capability, access, autonomy or safeguards change. Its strongest additions are cumulative checking, task-specific checker adequacy, and immediate suspension of permissions that depend on failed assumptions.

The patch adds no new engine or separate scheduler. It also avoids requiring a generally smarter checker for every upgrade: a small protected checker can check suitable bounded claims.

It is not an implemented safety guarantee. The 54 cases are test specifications; target-specific rules, software, real enforcement and executed verification remain to be supplied. It does not solve ownership of compute or guarantee control over systems outside Garden.

## Version and preservation boundary

This is an additive candidate for the v15.10 working design's v15.11 successor. It is not a complete v15.11 source release. The connected repository still binds canonical/current to Garden v15.5 and its materialized candidate pointer to v15.7; this package does not rewrite either identity.

The [earlier v15.11 candidate ledger](https://github.com/ankitdcx/garden-main/blob/2d86894cbde364706463a3658f43dea41dcc0b6f/design_deltas/v15.11/PENDING_CANDIDATES_2026-09-20.md) is retained on its original branch. [PR #95](https://github.com/ankitdcx/garden-main/pull/95) was closed without merging. RCC supplements its admission, assurance, authority and evolution themes; no prior candidate is removed, superseded or silently admitted. This directory is not an exhaustive candidate index.

The user authorized this candidate registration and repository publication on 2026-09-22. That authorization is not represented as implementation certification or canonical admission. No paid model calls were made.

