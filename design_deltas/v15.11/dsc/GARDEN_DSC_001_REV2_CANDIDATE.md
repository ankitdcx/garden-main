# GARDEN-DSC-001 Rev 2 — Deterministic Semantic Compilation & Auditable Coverage

**Status:** NONCANONICAL ADDITIVE CANDIDATE — NOT IMPLEMENTED, TESTED, CERTIFIED OR ADMITTED. **Canonical effect:** NONE. **Target:** v15.10 GCSC/SAL/Materiality/SAC and v15.11 USM-001. **Topology:** no new engine, semantic root, authority source or automatic registered SchemaID.

## 1. Exact claim and boundary
DSC is a cross-owner **reproducibility and audit contract**, not a guarantee of semantic closure for arbitrary real-world situations. For a frozen qualified `ScenarioSnapshot`, deterministic registries and mapping profile, logical budget, execution variant, encoding version, privacy commitment parameters and source epoch, conforming implementations MUST produce the same canonical *semantic* output or an explicit discrepancy. Matching hashes do not establish correctness, completeness, evidence independence, medical/legal authority or action permission.

**Pre-freeze interpretation:** real-world language, video, speech, observations and records enter existing USM/Evidence/Provenance owners. Models/humans may propose alternative readings. A qualified freeze records interpretations, ambiguities, source lineage and missing data. Deterministic DSC starts **only after this freeze**. A changed interpretation or source requires a new snapshot/epoch or qualified version, not silent reuse.

## 2. Owner reuse and collision rules
- USM SituationFact, MappingProfile and SituationMappingReceipt own source/interpretation mapping. `ScenarioSnapshot/v1` and `SemanticInterpretationSet/v1` are **candidate views/profiles**, not duplicate evidence stores.
- GSL v45.1 owns objects/relations/forms and typing. v15.10 S0/S1/S2 source build remains an explicitly distinct **finite projection variant**; bounded GCSC L0–L5 is a separate **exploration variant**. No implicit fixed-point equivalence or source supersession.
- SAL owns structural, completeness, join, coherence and interpretation diagnostics; Materiality owns obligation-profile evaluation independent of current test inventory; SAC owns generated candidate schemas/tests/obligations.
- Tree Core owns historical source/owner crosswalk; REP/TRACE own representation/independence challenges; Knowledge/Reason/Proof retain epistemic ownership; RCC/VEI retain continuing authority/real-effect verification.
- Proposed `DeterministicGenerationProfile/v1`, `InvariantApplicabilityReceipt/v1`, `SemanticClosureReceipt/v1` and `IndependentEquivalenceReceipt/v1` are **profile/receipt candidates**, pending collision and SchemaID review. Names are not admissions.

## 3. Frozen execution profile (candidate fields)
```text
DSCProfile {
  source_snapshot_root, interpretation_set_root, mapping_profile_root,
  semantic_registry_root, relation_signature_root, materiality_rules_root,
  invariant_owner_registry_root, dependency_graph_root, design_epoch,
  execution_variant: FINITE_S0_S1_S2 | BOUNDED_GCSC_EXPLORATION,
  compiler_version, checker_version, canonical_encoding_version,
  interpretation_limit, motif_limit, max_depth, logical_step_budget,
  traversal_order, deterministic_tie_break, reduction_equivalence_rules,
  stop_rule, commitment_profile_ref, commitment_nonce_or_key_ref,
  privacy_scope, applicable_law_and_authority_refs
}
```
Inputs MUST be fully versioned and source-bound. Canonical encoding requires an explicit frozen rule (e.g. a qualified RFC 8785/JCS profile with declared Unicode and number handling or deterministic CBOR). **Do not silently import an encoding standard**: the selected v15.10 GardenCanonicalEncoding/v3 semantics and any proposed external encoding must be compared and explicitly selected per execution variant. Reject duplicate keys, noncanonical encodings and ambiguous numeric semantics. Use logical operation budgets rather than wall-clock timing for reproducibility. Canonical semantic identity excludes nondeterministic logging/receipt timestamps and run-specific metadata.

## 4. Bounded algorithm
```text
DSC(frozen_snapshot, frozen_profile):
  validate exact source/epoch, scope, registries and encoding
  enumerate supported interpretation alternatives in fixed order
      up to declared logical budget and interpretation_limit
  preserve unexpanded alternatives in a stable, reproducible frontier
  compile typed GSL graph without upgrading CLAIM to established fact
  if FINITE_S0_S1_S2: execute the selected finite source projection contract
  else: generate bounded GCSC motifs using frozen traversal/reduction
  run SAL structural/completeness/join/coherence/interpretation checks
  derive and compose material obligation profiles independently of coverage
  resolve each evaluated applicable invariant to its qualified owner
      or emit owner/status UNKNOWN, UNMAPPED or CONFLICT
  SAC derives only source-bound candidate artifacts for genuine uncovered gaps
  propagate invalidations over explicit typed dependency edges
  preserve budget/frontier, ambiguity, contradiction and non-PASS statuses
  canonicalize graph, obligations, diagnostics, frontier and candidate artifacts
  emit source-bound SemanticClosureReceipt and qualification statuses
```
**Budget rule:** resource exhaustion returns `INCOMPLETE` with stable frontier and coverage denominators. It never returns false COMPLETE or silently drops material alternatives. Finite budget bounds work; it cannot guarantee all interpretations or obligations are discovered. If registry or privacy permission is missing, emit typed UNKNOWN/RESTRICTED as applicable, never infer PASS.

## 5. Privacy and equivalence
Canonical *semantic output* equality is distinct from disclosure-safe receipts. Plain hashes of low-entropy protected patient facts are unsafe. Privacy receipts use a frozen, domain-separated, authorized keyed commitment or appropriately nonce-bound commitment profile. Key/nonce identity and access rules are part of frozen comparison inputs; secret values need not be disclosed. Compare deterministic protected commitments only within authorized scope. Different authorized privacy parameters may produce different receipt bytes even when semantic results are equivalent; emit an equivalence receipt with explicit comparison level (byte/structure/semantic) and access limitation.

`IndependentEquivalenceReceipt` must disclose implementer/reviewer identity, model-family/tool/specification/registry/common-source lineage, shared failure modes, independently frozen reference fixtures, output roots, comparison level, differences, limits and reviewer qualification. Two implementations sharing one design misconception do not prove completeness.

## 6. Explicit dependency and coverage boundary
DependencyClosureIndex is a candidate view over existing qualified dependency owners, with typed source → claim → obligation → derived artifact → decision edges, invalidators and epoch/time scope. On changed evidence, consent, authority, context, law, model or registry, recompute the **reachable materially dependent** closure. Missing dependency edges are UNKNOWN, not evidence of independence.

For a **declared finite independently constructed** obligation reference universe `O_ref` and qualified matching relation, measure:
```text
recall = |O_generated ∩ O_ref| / |O_ref|
precision = |O_generated ∩ O_ref| / |O_generated|
```
State empty-denominator behavior explicitly in the frozen metric profile (UNDEFINED/NOT_APPLICABLE, never invented 100%). The reference oracle must disclose author/source lineage, domain, scope, known omissions and potential shared representations. These are bounded empirical metrics, not proofs of universal completeness. Track `INCOMPLETE` frequency, false-PASS rate, valid-class coverage, unknown preservation and invalidation accuracy separately.

## 7. Rev 2 invariant obligations
Original DSC-001..012 retained as candidate requirements, with the following clarifications:
- **DSC-001:** identical *qualified frozen inputs and complete execution profiles* yield byte-identical canonical semantic outputs under a declared encoding; private receipt identity may differ across authorized commitment profiles.
- **DSC-002:** ambiguous facts preserve alternatives; **DSC-003:** no silent source/contradiction/qualifier/obligation loss; **DSC-004:** frozen registry-driven typing, not runtime model intuition.
- **DSC-005:** materiality independent of current invariant/test coverage; **DSC-006:** applicable invariants bind owner or unresolved; **DSC-007:** composition cannot erase obligations/amplify authority.
- **DSC-008:** bounded exhaustion yields INCOMPLETE with frontier; **DSC-009:** typed reachable dependency invalidation with unknown edges explicit.
- **DSC-010:** no generated confidence/reproducibility authority; **DSC-011:** implementation agreement is not semantic completeness; **DSC-012:** privacy/access applies to retrieval, joins, derivations and receipts.
- **DSC-013:** natural-language interpretation is outside deterministic execution until qualified/frozen.
- **DSC-014:** deterministic bounded interpretation expansion retains material unexpanded alternatives.
- **DSC-015:** canonical identity excludes nondeterministic metadata; protected commitments use frozen privacy-safe parameters.
- **DSC-016:** independent equivalence discloses common authorship, model, data, registry and evidence lineage.
- **DSC-017:** completeness claims are scoped to a finite reference universe and independently qualified oracle.

## 8. Tests and qualification (ALL UNEXECUTED)
Retain DSC-T01..T14 from Rev 1: repeated hospital snapshot hash; independent implementation comparison; conflicting family claims; missing directive UNKNOWN≠ABSENT; confidence≠authority; expired junior grant; changed recovery-probability evidence; last ventilator allocation; bounded frontier; hidden-obligation miss despite hash equality; forbidden cross-hospital join; order-invariant qualified fact-ledger normalization; ambiguous wording alternatives; new invariant under changed epoch/profile. T14 is not an invariant-numbering defect: test and invariant namespaces differ.

Add:
- DSC-T15: interpretation branching exceeds budget → stable INCOMPLETE frontier and measurable incomplete rate.
- DSC-T16: shuffled raw text does not claim determinism before qualified freeze; shuffled equivalent **frozen facts** normalize identically.
- DSC-T17: two independent implementations with shared training/spec lineage disclose dependence and cannot claim independent completeness.
- DSC-T18: small-domain protected facts do not appear as guessable plain hashes in public receipts; changing authorized commitment nonce changes protected receipt but not qualified semantic result.
- DSC-T19: changed evidence invalidates exactly reachable typed dependents; missing edges remain UNKNOWN.
- DSC-T20: identical semantic inputs with different wall-clock performance and same logical budget produce identical outputs.
- DSC-T21: FINITE_S0_S1_S2 and BOUNDED_GCSC profiles are labelled distinctly; neither silently claims the other's closure.
- DSC-T22: empty reference denominator returns UNDEFINED/NOT_APPLICABLE, not 100% coverage.
- DSC-T23: independent oracle injects ~20 hidden obligations; quantify misses/false positives and retain UNKNOWN.
- DSC-T24: run a nonmedical fixture (flood infrastructure or financial incident), compare invariants and incomplete rates.

First qualification milestone: freeze hospital + second-domain fixtures; implement stages 1–4 in **two independently authored languages** with fixed encoding and logical budgets; independently prepare reference obligations; report byte/structural/semantic disagreement, false PASS, miss/precision/recall, INCOMPLETE rate and shared-dependency disclosures. A passing fixture is not a general correctness proof.

## 9. Admission and source-retention gate
Perform GSL-COMPARE collision review against USM/GCSC/SAL/SAC, Tree Core, REP, TRACE and existing encoding/receipts; compare DO_NOTHING and simpler profile extension; preserve exact source/owner/epoch and status axes. Run adversarial independent review, executable conformance, privacy/rights/consent/authority/Human-Effect/law checks and source-to-successor no-loss mapping. **No DSC output, compiler, generated test or reviewer consensus may self-admit.** This patch does not change v15.5, v15.10's selected executable source semantics, LICENSE or any actual medical decision authority.
