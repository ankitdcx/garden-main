# v15.9 P037 — mandatory functional corrective overlay

**Status:** reviewed v15.9 working-candidate semantics; no canonical or production certification. **Precedence:** this P037 overlay controls conflicting staged packet wording in v15.9. Source: `Garden_v15.9_CONSOLIDATED_UPGRADE_COMPLETE_CROSS_REVIEWED_WORKING_CANDIDATE_2026-09-18.txt`, section `P037 mandatory final repairs`.

## Enforceable conditions

1. **Appeal/contestability.** For consequential or material-rights proceedings, preserve any mandatory appeal/contestability route. “Optional” describes party invocation or procedural qualification, **not** deletion of a required route. Test: proceedings cannot be closed with a mandatory route absent.
2. **Credential verification.** Verifier-UNKNOWN and unsupported-profile are distinct typed **non-PASS** results; neither is invalid nor PASS. Test: unsupported profile cannot authenticate an action.
3. **Urgent-preservation expiry.** Expiry invalidates the effect across retry, failover and queued replay. Post-expiry execution requires fresh current authority and all required fresh evaluations. Uncertain prior effects retain **PARTIAL_EFFECT / OUTCOME_UNKNOWN** and require reconciliation. Test: stale queued authorization cannot execute after expiry.
4. **CausalClosureReceipt owner.** P024 Causal Safety owns `CausalClosureReceipt`; no unrelated module may silently redefine its semantics.
5. **Lawful erasure.** Remove protected evidence payload while retaining only the strongest lawful minimum tombstone/surrogate. Dependent conclusions become **STALE / NEEDS_REVALIDATION** when their evidence basis is removed. Test: erased evidence cannot continue to support an unqualified current conclusion.
6. **GSL compatibility.** `predecessor_gsl_compatibility_status=NOT_STATED` unless exact proof supports `VERIFIED_COMPATIBLE`. Do not infer compatibility from matching version strings.
7. **Release generation order.** Generate `CurrentReadingMap` from fixed final bytes before `ReleaseManifest`. Freeze `UpgradeTraceabilityTable` covering P001–P037 before manifest computation. Manifest binds six deliverables plus CurrentReadingMap and UpgradeTraceabilityTable; compute detached digest after manifest finalization.
8. **Release and re-review.** Release labels are administrative, not authorizing. A new material semantic edit re-enters applicable P035 review/independence/qualification before closure. Test: relabeling cannot turn UNKNOWN into PASS or confer authority.

## Inherited limits
Hard rights/consent/privacy/authority/safety/law gates remain separately applicable. No single PASS overrides another mandatory UNKNOWN/STALE/FAIL. This delta is limited to P037; the full P001–P036 source-anchored functional extraction is still outstanding and must not be claimed complete.
