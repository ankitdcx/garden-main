# Garden Future Work — Single Durable Index

Status: NONCANONICAL PLANNING INDEX  
Updated: 2026-09-21  
Purpose: one place to find deferred/future Garden work without treating it as accepted canon, current release work, or current operational work.

## Boundary

This file is an index, not a semantic owner and not an admission decision. Detailed issues, candidate ledgers, research handoffs, design deltas and historical evidence remain authoritative for their own exact content.

**Do not use this index to modify, review, reconcile, close, or supersede active v15.10/v15.11 work.** That work is being handled by a separate active workstream.

Current operational work such as Git-process hardening, OpenRouter/GROUP_REVIEW infrastructure, multi-model review automation, Android reviewer tooling, repository cleanup and budget/accounting hardening is also intentionally excluded from this future-work list while active.

## Future engineering foundations

- **Garden-native independent runtime** — executable Garden-owned state/goals/authority/knowledge/gates with replaceable cognitive-model backends. Existing owner: garden-swarm issue #229.
- **Minimal executable GSL semantic kernel** — bounded executable GSL semantics. Existing owner: garden-main issue #1 / WP-001.
- **Garden source → obligation extractor** — machine-readable obligation/closure extraction. Existing owner: garden-main issue #2 / WP-002.
- **GSL-KR claim/evidence/dependency store** — persistent epistemic store. Existing owner: garden-main issue #3 / WP-003.
- **Typed verifier bridge** — typed verifier classes, pinning and scoped receipts. Existing owner: garden-main issue #4 / WP-004.
- **GNR / GSL-native self-hosting** — progressively move Garden processes/control plane toward GSL-native execution and eventual self-hosting. Existing owner: garden-swarm issue #83.
- **Cross-language reference implementation** — language-neutral fixtures and a TypeScript/reference implementation after core contracts stabilize. Existing owner: garden-swarm issue #68.
- **Legacy bool receipt retirement** — migrate remaining callers to typed receipt states and remove the compatibility bool adapter when safe. Existing owner: garden-swarm issue #67.

## Future knowledge, learning and agreement work

- **GSL-KR continuous learning / CEA** — governed assimilation, correction, compression, cross-context privacy and knowledge consolidation without implying model-weight change or authority. Existing owner: garden-swarm issue #57.
- **UCAS / living agreements** — recover/compare exact agreement semantics against current Contract/Obligation/Law/Consent owners; add only a non-duplicate actor-agreement layer. Existing owner: garden-swarm issue #85; historical recovery also tracked as HCA-004 in the v15.6 candidate material.
- **Outcome-based memory/knowledge evaluation and other recovered KR candidates** — preserve candidate status until independently compared with current owners.

## Future trust, privacy and human-boundary assurance

- **Bootstrap trust root** — initial trusted-state ceremony/verifier/threshold mechanism, approval evidence, revocation/rotation and adversarial tests. Existing owner: garden-swarm issue #66.
- **Privacy routing** — fail-closed provider/model routing with typed routing receipts, classification/authority/privacy constraints and tests. Existing owner: garden-swarm issue #78.
- **Emergency + consent validity hardening** — source-independence for emergency evidence and typed consent validity; retain only gaps not already absorbed by later design. Existing owner: garden-swarm issue #17.
- **Neutral public Garden namespace / identity-privacy migration** — migrate to a neutral public namespace without changing authority semantics. Existing owners: garden-main issue #29 and garden-swarm issue #80.
- **Whole-repository external review** — periodic independent whole-repo review after a suitable low-churn/neutral-namespace execution path exists. Existing owner: garden-swarm issue #115.
- **Human Assurance Reliability / HITL workload profile** and **behavioral/normative/mechanism drift audit** — recovered historical candidates; preserve as candidate research until equivalence review.

## Future interoperability and distributed Garden

- **A2A/MCP discovery/deployment** — verify/update Garden agent discovery and interoperability against the eventual runtime architecture. Existing owner: garden-swarm issue #9.
- **Distributed compute/storage commons, contribution/reputation and knowledge-market mechanisms** — future architecture/economy work; preserve historical candidate semantics and do not infer acceptance.
- **Federation / Kindergarten recovery** — recover exact historical definitions and compare with current architecture before any promotion.
- **Justice-system end-to-end scope** — future bounded scope refinement; no new sovereign/adjudicator is implied by this index.

## Future research and experiments

- **Cross-tenant shared mutable services as covert channels** — deployment/security experiment. Existing owner: garden-main issue #54.
- **Opaque-ID equivariance for stateful tool agents** — experiment-only metamorphic/formal-verification candidate. Existing owner: garden-main issue #55.
- **Cross-scale causal discovery (HCA-001)** — candidate research.
- **TFT/VSM comparative/model-selection work (RVH-4 and related)** — empirical comparison candidate.
- **CASI adapter activation** — explicitly deferred; historical references must not silently reactivate adapters.
- **Research handoff collection** — simulation, provenance attestations, metamorphic tests, MCP hardening and related experiments; evaluate individually. Existing owner: garden-swarm issue #140.
- **SCEP implementation/profile lineage, FDE/CFBR, reasoning-strategy candidates and other recovered historical candidates** — preserve exact candidate identities/statuses in their existing ledgers; compare before reuse.

## Preservation rule

1. A future item may have detailed records elsewhere; this file points to them rather than replacing them.
2. Closing or superseding an old tracker requires either a successor reference or an explicit evidence-backed determination that it is duplicate/obsolete.
3. No candidate/research/deferred item becomes canonical merely by appearing here.
4. When a future item becomes active, move operational ownership to a dedicated issue/workstream and leave a pointer here.
5. New deferred work should be added here (or to a machine-readable successor index linked here) so chats are not the only durable record.
6. Active v15.10/v15.11 work is outside this index and must not be touched from this consolidation workstream.

## Known source families retained elsewhere

- `design_deltas/v15.6/PENDING_CANDIDATE_INDEX.json`
- `design_deltas/v15.6/ARCHIVE_DERIVED_V15_6_CANDIDATE_REGISTRY_2026-09-14.md`
- `reviews/HISTORICAL_CHAT_UPGRADE_AUDIT_2026-09-14.md`
- `reviews/MULTI_AGENT_ARCHIVE_AUDIT_2026-09-14.md`
- `reviews/HISTORY_PENDING_RECONCILIATION_2026-09-15.md`
- `reviews/PROJECT_WIDE_CHAT_UPGRADE_RECONCILIATION_2026-09-14.md`
- garden-main research/work-package issues
- garden-swarm engineering/research issues and ROADMAP

These remain evidence/detail stores. **This file is the single human-facing entry point for future work.**
