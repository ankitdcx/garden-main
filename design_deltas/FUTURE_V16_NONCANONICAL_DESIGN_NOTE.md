# Future Garden v16 — noncanonical design path

**STATUS: NONCANONICAL EXPERIMENTAL PLANNING NOTE.** No v16 release exists by virtue of this note. No candidate is admitted; canonical/current v15.5, LICENSE and economic terms remain unchanged.

**Goal:** a coherent possible successor built by selectively integrating independently qualified candidates while retaining every material predecessor obligation, exception, scope and unknown. Document format (five-file or equivalent structured form) is a design choice, not an admission rule.

## Stage 0 — freeze sources
Freeze v15.5 `canonical/current/` and its source manifest, DesignEpoch, registries and CORPUS_INDEX snapshot. Freeze every candidate's exact source edition/hash/status. Do not modify canonical source during candidate synthesis.

## Stage 1 — ownership and equivalence
Complete [cross-version ownership map](CROSS_VERSION_OWNERSHIP_MAP.md). For each candidate identify controlling existing owner, actual incremental semantics, DO_NOTHING/simpler alternative, required dependencies and invalidators. Explicitly record conflicts and duplicate/overlapping owners.

## Stage 2 — reconstruction/no-loss
Run GSK reconstruction on held-out predecessor obligations and exceptions. Require exact source→successor atomic mappings, ObligationDiff, source-independent reconstruction and independently verified receipts before retiring any predecessor wording. Apply comparable tests to MCC, USM, RSDC and IDTD outputs. Hash equality detects change, not semantic equivalence.

## Stage 3 — bounded evaluation priorities
1. RCC + VEI: control and actual-effect integrity.
2. USM + MCC: situation typing and material context closure.
3. DSC-001 Rev 2: evaluate reproducible frozen-snapshot compilation and bounded obligation audit before any completeness claim; unimplemented candidate.
4. REP + SHR: representation independence and historical search reuse.
5. IDTD + RSDC: theory discovery and recursive compression.
6. CEA / V1511-KR-001: **already a full specified candidate**, but still requires implementation, tests, adversarial review and admission qualification.
7. Other recovered directions only after owner collision/equivalence checks.

This order is an evaluation preference, not a schedule or permission to skip prerequisite controls.

## Stage 4 — draft successor only
A future proposal may use `canonical/candidates/v16-draft/` or equivalent noncanonical workspace. Each candidate change must carry: exact source candidate ID/edition/hash, owner, applicability, ObligationDiff, reconstruction/no-loss evidence, failure and fallback, tests/receipts, UNKNOWN/CONFLICT/INCOMPLETE items and source→successor links. Mark **NONCANONICAL EXPERIMENTAL**. Do not create the directory until there is a substantive source-bound draft.

## Stage 5 — independent admission
Separate proposer, falsifier and admission authority. Apply REP independence discipline, rights/consent/privacy/safety/Human-Effect/authority/law reviews, external verification where required, and the explicit legitimate human admission boundary. Independent review and evidence do not themselves promote a release.

## Hard invariants
- No generated/consolidated material self-admits.
- No silent loss of predecessor obligations, exceptions, non-laws or negative cases.
- UNKNOWN/CONFLICT/INCOMPLETE do not become PASS by packaging.
- Capability, consensus, cryptographic authenticity or success do not create authority.
- Rights, consent, privacy, safety and Human-Effect constraints remain applicable.
- Specification ≠ formal proof ≠ implementation ≠ empirical validation ≠ external certification.

**Non-effects:** This note does not create Garden v16, merge prior versions, promote candidates, authorize execution, alter LICENSE or economic terms, or supersede v15.5.
