# Garden Main

Garden is an evolving design specification for a governed AGI system. It describes how an AI system should represent the world, reason about information, make decisions, act, learn and remain accountable to human interests.

The repository contains **design artifacts and research records**, not a claim that a complete AGI system has been implemented or validated. Its documents are intended for researchers, system designers, implementers, reviewers and anyone who wants to inspect how the design is structured.

## Current authority

> **Canonical release: Garden v15.5 / GSL v45.1 (2026-09-12)**

The only canonical release in this repository is the five-file source in [`canonical/current/`](canonical/current/). Its exact file identities are pinned by [`SOURCE_MANIFEST.json`](canonical/current/SOURCE_MANIFEST.json).

Later version numbers, candidate folders, generated documents, reviews or passing tests do not change canonical status. A successor requires separate review and admission.

## Start here

| I want to… | Start with |
|---|---|
| Understand Garden without reading the full specification | [Overview](OVERVIEW.md) |
| Read the current canonical source | [Canonical source guide](canonical/current/README.md) |
| Compare releases and historical work | [Version history](VERSION_HISTORY.md) |
| Explore incremental proposals and research | [Design deltas](design_deltas/README.md) |

## Version map

| Material | Location | Status |
|---|---|---|
| **v15.5 / GSL v45.1** | [Canonical source](canonical/current/) | **Canonical** |
| v15.6 | [Full candidate](canonical/candidates/v15.6/README.md) · [supporting deltas](design_deltas/v15.6/) | Noncanonical candidate |
| v15.7 | [Full candidate](canonical/candidates/v15.7/README.md) · [supporting deltas](design_deltas/v15.7/) | Noncanonical candidate |
| v15.8–v15.9.1 | [Versioned deltas](design_deltas/README.md) | Historical/noncanonical |
| v15.10 | [Working design and research](design_deltas/v15.10/README.md) | Noncanonical working design |
| v15.11 | [Candidate set](design_deltas/v15.11/CANDIDATE_RETENTION_LEDGER.md) | Noncanonical candidate work |
| v16.0 (working candidate) | [Candidate workspace](design_deltas/v16/README.md) · [HOME-001](design_deltas/v16/GARDEN_HOME_001_CANDIDATE.md) · [FOOD-001](design_deltas/v16/GARDEN_FOOD_001_CANDIDATE.md) | Noncanonical partial candidate; proprietary modular business framework and two detailed assets; **not** a full successor release |
| Future v16 full successor | [Evaluation note](design_deltas/FUTURE_V16_NONCANONICAL_DESIGN_NOTE.md) | Planning only |
| Earlier design master | [Historical archive](history/README.md) | Historical; not current authority |

For the complete lineage and status distinctions, see [VERSION_HISTORY.md](VERSION_HISTORY.md).

## Garden v16 — proprietary business assets

The Garden owner designates the universal modular business framework, its industry applications and the two detailed business designs as proprietary assets, with all legally available rights reserved:

| Asset | Business design |
|---|---|
| [BIZ-001](design_deltas/v16/GARDEN_BIZ_001_FRAMEWORK.md) | Universal modular business design · [40-industry register](design_deltas/v16/GARDEN_BIZ_001_INDUSTRY_REGISTER.md) |
| [HOME-001](design_deltas/v16/GARDEN_HOME_001_CANDIDATE.md) | Modular housing and construction systems — detailed design |
| [FOOD-001](design_deltas/v16/GARDEN_FOOD_001_CANDIDATE.md) | Modular food outlet and chain operating systems — detailed design |
| FASHION-001 / PERFUME-001 | Next user-directed business designs; reserved identifiers, templates only |
| [Industry templates](design_deltas/v16/GARDEN_BIZ_001_TEMPLATE.md) | Common template plus 38 non-detailed industry seeds (including fashion and perfume) |

None of these protected assets is offered for free use, open-source licensing, independent commercial implementation or franchising. Prior written authorization is required for use of the owner's protected rights, subject to applicable law and binding existing rights. See the [v16 proprietary-business rights notice](design_deltas/v16/README.md#proprietary-business-assets) and [LICENSE](LICENSE). Business-asset designation is distinct from technical validation, patent grants, company registration and canonical admission. The existing sale offer is unchanged.

## Repository map

- [`canonical/current/`](canonical/current/) — the five controlling v15.5 source texts and their manifest.
- [`canonical/candidates/`](canonical/candidates/) — complete five-file successor working candidates.
- [`design_deltas/`](design_deltas/) — incremental proposals, source extracts, research, recovery records and indexes.
- [`history/`](history/) — preserved historical material for provenance and comparison.
- [`LICENSE`](LICENSE) — published use terms.

## Authority and evidence boundaries

- Canonical source, candidate source, incremental delta and historical archive are different artifact classes.
- A later version label does not supersede an earlier canonical source.
- A hash verifies file identity, not semantic completeness or correctness.
- Specification, formal proof, implementation, empirical validation, certification and deployment are distinct claims.
- A proposal, review, model response or local test cannot admit itself into canonical status.
