# Comparative cognitive coverage — Candidate B
Patch ID: GARDEN-v15.7-COGNITIVE-COMPARE-01
Status: NON_CANONICAL_CANDIDATE_PENDING_RECONCILIATION
Revision: consolidated split Candidate B, including all accepted reconciliation outputs.
Release: v15.7 per latest user instruction; supersedes conversational GARDEN-v15.6-COGNITIVE-COMPARE-01. No v15.6 source changes.

## Purpose and independence
A finite mechanism comparison produces an actionable coverage/gap report. It is separate from Cognitive qualification (COGNITIVE-CORE-CANDIDATE.md). Either may proceed before the other finishes; superiority claims require valid experiments and applicable qualification.
No comparison outcome, adequacy, safety, capability, new engine or canonical admission is asserted by this registration.

## Fixed comparison set: ten
Pin exact artifacts during reconciliation. Comparison is at mechanism scope, not a ranking of interchangeable whole-world systems.
| Comparator | Initial type and bounded focus |
|---|---|
| Soar | Cognitive architecture: operator selection, memory, learning |
| ACT-R | Cognitive architecture: memory/processing and cognitive modelling |
| OpenCog Hyperon | Cognitive architecture: representations and integrated reasoning/learning |
| OpenNARS | Reasoning architecture: uncertainty and resource-bounded reasoning/control |
| DreamerV3 | Learning algorithm/world-model system: predictive control |
| SIMA 2 | Documented embodied agent: instructed action in virtual environments |
| LeCun autonomous machine-intelligence proposal | SPECIFICATION_ONLY: proposed world-model/planning/learning architecture |
| ReAct | Agent method: reasoning/tool interaction |
| AlphaEvolve | Evaluated search system: proposal/evaluation/search |
| LangGraph | Agent framework: orchestration, persistent execution and integration only |
Adding/replacing comparators requires explicit scope revision. Classify the actual accessible artifact: a runnable implementation is not assumed merely because a system is documented. Do not attribute underlying-model intelligence to an orchestration framework.
Pin paper identifier plus explicit revision/version and content hash, with retrieval date; pin software release/commit, dependencies and configuration. If immutable artifacts or needed access are unavailable, record unresolved evidence rather than fabricate a pin.

## Comparison rows and allowed dispositions
Each row binds comparator artifact/type, precise mechanism and purpose, Garden source/implementation counterpart, evidence, scope and disposition.
- EQUIVALENT_COVERAGE: identified mechanism addresses the requirement; performance equivalence is separate.
- DIFFERENT_TRADE_OFF: both address it with different assumptions, costs or benefits.
- SPECIFICATION_GAP: relevant requirement lacks an adequate specified Garden mechanism.
- IMPLEMENTATION_GAP: specified Garden mechanism lacks sufficient implementation for evaluation, supported by direct evidence.
- MEASURED_DEFICIT: valid experiment demonstrates worse performance on a declared criterion.
- UNRESOLVED: insufficient mapping/evidence, with no defect inferred.
- NOT_APPLICABLE: outside approved scope, with explicit reason.
For SPECIFICATION_ONLY comparator rows permit only SPECIFICATION_GAP, DIFFERENT_TRADE_OFF, EQUIVALENT_COVERAGE (explicitly specification level), UNRESOLVED or NOT_APPLICABLE. Forbid MEASURED_DEFICIT and IMPLEMENTATION_GAP from such comparisons. Independently discovered Garden implementation gaps become separately evidenced findings, not conclusions attributed to a proposal.
Every unresolved row requires missing evidence, reason, bounded resolution work item OR an explicitly approved scope exclusion. Excluded rows never count as resolved coverage. Unknown is not an escape from recording actual review work.

## Required report and completion fields
- Scope/version of comparison program and all ten pinned or explicitly unresolved artifact identities.
- Per-comparator scope table: mechanisms actually reviewed, out-of-scope mechanisms/reasons, accessible artifact type and evidence limits.
- Per-mechanism Garden counterpart, disposition and source/evidence references.
- Specification-only disposition validation result.
- Resolved / unresolved / excluded counts with an explicit row-counting rule. NOT_APPLICABLE/excluded rows are not successes. A wholly unresolved report cannot claim substantive resolved coverage.
- Missing evidence, resolution tasks, approved exclusions and routing of resulting findings.
- Required claim boundary: completion establishes every bounded row was reviewed and accounted for; NOT that mechanisms are adequate, safe or capable. Report completion is not gap closure.
Findings route separately as specification work, implementation work, measured deficits or investigation; reuse existing work identities where equivalent. No missing code is automatically a design defect.
Changes to comparator scope, budget or evaluation criteria require the applicable authorized decision. Comparative experiments use protected evaluation and matched-condition/limitation discipline from Candidate A where applicable; documentation review is not measured superiority.
Current evidence: conversational design review only; no first-pass comparison or source reconciliation performed by registration.
Next work: produce the comparator-scope table and evidence-pinned rows. Reconciliation may yield existing coverage, smaller amendments or blocked scope rather than new features.
