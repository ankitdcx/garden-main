# GARDEN-USM-001 — Universal Situation Mapping

**Status:** NONCANONICAL ADDITIVE CANDIDATE · NOT IMPLEMENTED/ADMITTED  
**Target:** v15.10 GSL/GCSC/SAL/SAC; v15.11 candidate integration  
**Compatibility:** MCC-001, RSDC-001, IDTD-001, REP, RCC, VEI, Human-Effect  
**Topology / authority:** No new top-level Form, engine, rights source or authority.

## Purpose and ownership

Map messy real-world information into deterministic, typed GSL graphs without converting model interpretations into authoritative facts. Reuse existing Evidence/Provenance, DesignEpoch, GSL Context/Frame, SAL, Materiality, Human-Effect, ActionGate and VEI owners. The Situation Fact Ledger is a *client/view* of the existing evidence machinery, not a parallel authoritative evidence store.

```text
Text/speech/video/sensors/documents/APIs/human reports
 → source snapshots and evidence-bound candidate extraction
 → Situation Fact Ledger (alternatives, uncertainty, contradictions)
 → frozen deterministic compiler (facts + registry + mapping profile)
 → typed GSL situation graph → MCC context closure
 → GCSC/SAL/Materiality/SAC → RSDC/IDTD candidates
 → independent verification → existing admission/ActionGate/VEI
```

## Typed records

```text
SituationFact {
 FactID, SourceRef, SourceSpan, ObservedContent,
 CandidateObjectTypes[], CandidateRelations[],
 SubjectRef, PredicateRef, ObjectRef, TimeRef, SpaceRef,
 ContextRefs[], EvidenceRefs[], Confidence, Uncertainty,
 Alternatives[], Contradictions[], Status
}
MappingProfile {
 ProfileID, Version, DesignEpoch, RegistryRoot, MappingRulesRoot,
 TypeSignatures, CanonicalizationRules, IdentityResolutionRules,
 EvidenceQualificationRefs[], AmbiguityRules, HumanEffectBindings,
 Applicability, Invalidators[], ResourceBounds
}
SituationMappingReceipt {
 SourceSnapshotRoot, FactLedgerRoot, SemanticRegistryVersion,
 MappingProfileVersion, DesignEpoch, GSLGraphRoot,
 ObjectsGenerated, RelationsGenerated, ContextsExpanded,
 Ambiguities[], Contradictions[], UnresolvedFacts[],
 MaterialityDecisions[], CoverageFrontier[],
 ValidationResults[], IndependentReviewRefs[], Status
}
```

## Deterministic compiler

`G = Compile(FrozenFactLedger F, Registry R, MappingProfile P)`.

Identical canonical F/R/P must produce byte-identical graph and diagnostics under a declared interpreter. This is **reproducibility, not factual truth**. Model-proposed interpretations remain proposals. SAL type-validity is not evidence validity. A CLAIM cannot become an established EVENT or stronger fact without the existing independently qualified evidence/validation path. Unknown source meaning retains alternatives and UNKNOWN; no most-likely guess silently becomes authorization.

Use the existing 10 GSL objects, 24 relations and seven Forms. A person represented as an entity/THING remains a rights-bearing human and may also have AGENCY; ontological typing never removes personhood or rights.

## Six binding refinements

- **USM-R01 Claim promotion:** CLAIM → established EVENT/fact requires qualified evidence, never mapper assertion.
- **USM-R02 Evidence ownership:** ledger reuses Evidence/Provenance identifiers, source spans, trust/status and invalidators; no independent truth store.
- **USM-R03 Epoch binding:** MappingProfile changes are DesignEpoch-sensitive. Material rule/registry/source changes invalidate and recompile affected graphs, preserving predecessor receipts.
- **USM-R04 Adversarial robustness:** incomplete, contradictory, misleading, selectively quoted or malicious inputs preserve alternatives, contradictions and non-PASS status; prompt injection is treated as untrusted source content, not compiler instruction.
- **USM-R05 Human-Effect closure:** any potentially human-affecting fact/graph remains subject to existing rights, consent, privacy, authority, safety and Human-Effect checks.
- **USM-R06 Coverage honesty:** a compiled graph cannot claim complete real-world representation without evidence-bound declared scope, source coverage and unresolved frontier.

## Context, identity and ambiguity

Layer 0: direct source observations and candidate facts. Layer 1: material law, authority, affected persons and dependencies. Layer 2+: MCC expands potentially material nested GSL contexts to a bounded fixed point or explicit unresolved frontier. Layers are search priorities, not hard depth caps.

Example: “AI approved payment” produces candidate interpretations RECOMMENDED / AUTHORIZED / EXECUTED, with status UNRESOLVED until evidence distinguishes them. Identity merging requires qualified equivalence across source, principal, time, scope and uncertainty.

## Hard invariants

- USM-I01 Every material graph element traces to a qualified source fact, explicit seed or reproducible derivation.
- USM-I02 Valid JSON or deterministic compilation does not establish truth.
- USM-I03 No unsupported CLAIM promotion or invented meaning.
- USM-I04 No uncertainty, contradiction, exception or source provenance erased by normalization.
- USM-I05 No mapping-generated authority, rights waiver, consent or certification.
- USM-I06 Human rights and Human-Effect obligations survive all mappings.
- USM-I07 Material source/profile changes invalidate affected graph/closure receipts.
- USM-I08 No unsupported completeness or independence claim.

## Tests and admission

Freeze source, ledger, profile, registry, graph and expected statuses. Test equivalent facts in different descriptions (semantic consistency); materially changed facts (semantic sensitivity); misleading summary; contradictory evidence; claim/event distinction; multiple roles for a person; context cycles; changed jurisdiction; source/profile drift; malicious instructions; unknown authorization; Human-Effect binding; incomplete coverage. Independently compare meaning and failure behavior, not merely hashes. Test success is bounded to frozen fixtures and cannot self-admit the candidate.

**Result:** USM is a non-authoritative compilation front-end, not a new constitutional layer.
