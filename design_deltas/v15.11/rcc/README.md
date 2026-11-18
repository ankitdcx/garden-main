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

This is an additive candidate for the v15.10 working design's v15.11 successor. It is not a complete v15.11 source release. The repository's only canonical source remains Garden v15.5 in `canonical/current/`. The v15.7 five-file candidate is retained separately; no selected-candidate pointer is present in the current tree.

The earlier [v15.11 pending-candidate ledger snapshot](https://github.com/ankitdcx/garden-main/blob/2d86894cbde364706463a3658f43dea41dcc0b6f/design_deltas/v15.11/PENDING_CANDIDATES_2026-09-20.md) was associated with [PR #95](https://github.com/ankitdcx/garden-main/pull/95), which closed without merging. That snapshot is not present in the current tree. RCC supplements its admission, assurance, authority and evolution themes; no prior candidate is removed, superseded or silently admitted. This directory is not an exhaustive candidate index.

## 2026-10-09 reconciliation

RCC relates to [VEI](../vei/README.md) (effect enforcement), [ERC](../erc/README.md) (evaluation reachability), [REP](../rep/README.md) (independent representation), [MCC](../GARDEN_MCC_001_CANDIDATE.md) (context closure), and [USM](../GARDEN_USM_001_CANDIDATE.md) (situation mapping).
