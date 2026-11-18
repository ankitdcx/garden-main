# v15.6–v15.9 structured-record consolidation audit — 2026-11-18

## Scope and result

This change consolidates all JSON files found in `design_deltas/v15.6/` and `design_deltas/v15.7/` into readable Markdown records. The audit covered the complete recursive Git tree for these version folders.

- v15.6: 21 JSON source files consolidated into five Markdown documents.
- v15.7: one JSON source file consolidated into one Markdown document.
- v15.8, v15.9 and v15.9.1: zero JSON files were present. Their existing source-labelled Markdown/text files remain separate; README navigation has been added.
- Total: 22 JSON files removed from the working tree and their complete structured data represented in Markdown.
- No v15.10 or v15.11 files were changed.

The Markdown rendering retains object keys, nested objects, ordered arrays, scalar values and candidate dispositions. It is a readable structured rendering, not a claim of byte-for-byte identity. Original Git blob IDs below identify the exact pre-consolidation source blobs in repository history. Git history is retained.

## v15.6 source mapping

| Original JSON source | Original Git blob SHA-1 | Consolidated destination |
|---|---|---|
| `CATALOG_ADDITIONS.json` | `686814d908083d486829841b2913a8ef2754796a` | [Design delta and catalogue records](V15.6_DESIGN_DELTA_AND_CATALOGUE_RECORDS.md) |
| `DELTASET-2026-09-13-GSL-GAP-CLOSURE.json` | `7e65cae59203d9d953c95f7179642ee23973b8e3` | [Design delta and catalogue records](V15.6_DESIGN_DELTA_AND_CATALOGUE_RECORDS.md) |
| `DELTASET-2026-09-14-CONSTITUTIONAL-EVENT-HARDENING.json` | `6707665cd9c14196e4954cf94904eb8b7e06b216` | [Design delta and catalogue records](V15.6_DESIGN_DELTA_AND_CATALOGUE_RECORDS.md) |
| `DELTASET-2026-09-14-GAIA-NAMING.json` | `d3be0565611e6240420b9ac778fa944054c47d56` | [Design delta and catalogue records](V15.6_DESIGN_DELTA_AND_CATALOGUE_RECORDS.md) |
| `DELTASET-2026-09-14-HISTORICAL-CHAT-RECOVERY.json` | `291686dee2c7e5bf185ecb58f9fd0423a7853600` | [Design delta and catalogue records](V15.6_DESIGN_DELTA_AND_CATALOGUE_RECORDS.md) |
| `DELTASET-2026-09-14-KR-CEA.json` | `2316a6f920c2db2f7b79bed0ed24dcd9ccb6fd09` | [Design delta and catalogue records](V15.6_DESIGN_DELTA_AND_CATALOGUE_RECORDS.md) |
| `DELTASET-2026-09-14-MULTI-AGENT-ARCHIVE-RECOVERY.json` | `b8694d5df362576fb681af88fbb69fc44c69418f` | [Design delta and catalogue records](V15.6_DESIGN_DELTA_AND_CATALOGUE_RECORDS.md) |
| `DELTASET-2026-09-15-SUCCESSOR-PROCESS-HARDENING.json` | `519c4f4b93e3b00ba934a3781b828e4743ebc4bd` | [Successor-process hardening history](V15.6_SUCCESSOR_PROCESS_HARDENING_HISTORY.md) |
| `DELTASET-2026-09-15-SUCCESSOR-PROCESS-HARDENING-V1.1.json` | `e45848c77d9dc0973a26b8a64560b7eb728d4c3e` | [Successor-process hardening history](V15.6_SUCCESSOR_PROCESS_HARDENING_HISTORY.md) |
| `DELTASET-2026-09-15-SUCCESSOR-PROCESS-HARDENING-V1.2.json` | `68ab8759d477c984ba161f36f0feabf99b37abad` | [Successor-process hardening history](V15.6_SUCCESSOR_PROCESS_HARDENING_HISTORY.md) |
| `DELTASET-2026-09-15-SUCCESSOR-PROCESS-HARDENING-V1.3.json` | `9cf6c6e9927ba70287f4e84fc74c994bca6e1b5e` | [Successor-process hardening history](V15.6_SUCCESSOR_PROCESS_HARDENING_HISTORY.md) |
| `DELTASET-2026-09-15-SUCCESSOR-PROCESS-HARDENING-V1.4.json` | `4db45c29587b1afc82cfec842169a3087c3f4963` | [Successor-process hardening history](V15.6_SUCCESSOR_PROCESS_HARDENING_HISTORY.md) |
| `PROCESS-CANDIDATE-GardenCanonicalUpdateProcess-v1.0.json` | `29d2e6666e404c591ac5995bcf8d3e7a999b678a` | [Canonical update process history](V15.6_CANONICAL_UPDATE_PROCESS_HISTORY.md) |
| `PROCESS-CANDIDATE-GardenCanonicalUpdateProcess-v1.1.json` | `a7813bec92861862ae7c77736a08ee87a20becd4` | [Canonical update process history](V15.6_CANONICAL_UPDATE_PROCESS_HISTORY.md) |
| `PROCESS-CANDIDATE-GardenCanonicalUpdateProcess-v1.2.json` | `ffad3502b9fcaca9cd92aa95e37417fc0f022fa3` | [Canonical update process history](V15.6_CANONICAL_UPDATE_PROCESS_HISTORY.md) |
| `PROCESS-CANDIDATE-GardenCanonicalUpdateProcess-v1.3.json` | `e22ed573bb9a31e3cc4caa18a19969ea8664c6e1` | [Canonical update process history](V15.6_CANONICAL_UPDATE_PROCESS_HISTORY.md) |
| `PROCESS-CANDIDATE-GardenCanonicalUpdateProcess-v1.4.json` | `8e22dccd656ae0f0e638d88fe39028d463ec96f2` | [Canonical update process history](V15.6_CANONICAL_UPDATE_PROCESS_HISTORY.md) |
| `SIMPLIFICATION-RECEIPT-v15.6-BOOTSTRAP-2026-09-15.json` | `da5afabd211eb3d7a91ecc4861b4d94b7b3e2bde` | [Canonical update process history](V15.6_CANONICAL_UPDATE_PROCESS_HISTORY.md) |
| `PENDING_CANDIDATE_INDEX.json` | `ae5362c9e81aa66621d036bac1b1906bb1f104d5` | [Candidate index and reconciliation register](V15.6_CANDIDATE_INDEX_AND_RECONCILIATION.md) |
| `PENDING-RECONCILIATION-2026-09-15.json` | `96aa7e0a960bb1a2d2e47e7fac35441ed97dca08` | [Candidate index and reconciliation register](V15.6_CANDIDATE_INDEX_AND_RECONCILIATION.md) |
| `DELTASET-2026-09-15-ENGINEERING-HARDENING.json` | `c4896584afbee4b2ce48b63a7ae6c95159907ccf` | [Engineering hardening specification](V15.6_ENGINEERING_HARDENING_SPECIFICATION.md) |

## v15.7 source mapping

| Original JSON source | Original Git blob SHA-1 | Consolidated destination |
|---|---|---|
| `PENDING_CANDIDATE_INDEX.json` | `22ca435f6949b289191cd478b5e39b2cc010e3aa` | [v15.7 candidate register](../v15.7/V15.7_CANDIDATE_REGISTER.md) |

## v15.8–v15.9.1

No JSON files were present in the audited v15.8, v15.9 or v15.9.1 folders. Existing source-specific text files were not flattened into one document because their source boundaries, provenance and distinct review roles are useful. README navigation was added for each folder.

## Preservation and authority boundary

- The consolidation is a format/navigation change only.
- It does not merge candidate semantics, resolve conflicts, claim all revisions are equivalent, or select a winning revision.
- v15.6 process candidates v1.0–v1.4 and successor-process hardening base/v1.1–v1.4 remain individually identifiable.
- The engineering specification retains its 20 patches and 38 work-register entries.
- The reconciliation register retains its 19 source-file records, 174 reconciliation records, 17 process-field refinements, embedded external source and qualification limits.
- The v15.6 and v15.7 indexes remain tracking records, not admission authority.
- Canonical v15.5 / GSL v45.1 is unchanged. v15.10 and v15.11 are outside this change.
