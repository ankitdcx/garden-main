# Garden Main

Garden's canonical design source, successor candidates, technical proposals, research and historical records.

**Current authority:** [Garden v15.5 / GSL v45.1](canonical/current/README.md). This is the only canonical release in this repository.

**Use terms:** [LICENSE](LICENSE).

## Design and version map

| Version / area | Repository location | What it contains | Status |
|---|---|---|---|
| **v15.5 / GSL v45.1** | [`canonical/current/`](canonical/current/) | Five controlling source texts: User, System, Technical, Annexure and Theories; plus the source manifest. GSL baseline: 10 Objects, 24 Relations and 7 Forms. | **Canonical current** |
| v15.6 | [Full candidate](canonical/candidates/v15.6/README.md) · [supporting deltas](design_deltas/v15.6/) | Complete five-file successor working candidate, plus separate engineering, governance, GSL, process and recovery materials. | Noncanonical candidate |
| v15.7 | [Full candidate](canonical/candidates/v15.7/README.md) · [supporting deltas](design_deltas/v15.7/) | Complete five-file successor working candidate; cognitive qualification, TRACE, design closure and additional human/evidence/privacy proposals. | Noncanonical candidate |
| v15.8 | [`design_deltas/v15.8/`](design_deltas/v15.8/) | Source-labelled additions and recovery material from the v15.8 working line. | Historical/noncanonical deltas |
| v15.9 | [`design_deltas/v15.9/`](design_deltas/v15.9/) | P001–P037 review material and selected source-level closure clauses. | Historical/noncanonical deltas |
| v15.9.1 | [`design_deltas/v15.9.1/`](design_deltas/v15.9.1/) | GCSC, SAL and SAC source extracts and detailed semantic patches. | Historical/noncanonical deltas |
| v15.10 | [`design_deltas/v15.10/`](design_deltas/v15.10/README.md) | Generative design and abstraction work: GCSC coverage, semantic-kernel/reconstruction ideas, theory discovery, recursive compression, Tree Core, retention and scientific research. | Noncanonical working design/research |
| v15.11 | [`design_deltas/v15.11/`](design_deltas/v15.11/) | Focused additive candidates, including RCC, REP, VEI, ERC, SHR, QSE/Rev 2, DSC, CEA, MCC, USM and transition/responsibility work. | Noncanonical candidate set |
| Future v16 | [Design path](design_deltas/FUTURE_V16_NONCANONICAL_DESIGN_NOTE.md) | Evaluation and reconstruction plan for a possible successor; no v16 release is created by this note. | Experimental planning only |
| Historical archive | [`history/`](history/) | Preserved standalone 50-module design master and its historical interpretation notice. | Historical; not current authority |

**Important distinction:** `canonical/candidates/` contains complete five-file successor candidates (currently v15.6 and v15.7). `design_deltas/` contains incremental proposals, source extracts, technical/research records and recovery material. These are different kinds of artifacts, not duplicate release folders.

## Repository map

| Path | Purpose |
|---|---|
| [`canonical/current/`](canonical/current/) | Sole canonical source; five source texts and `SOURCE_MANIFEST.json`. |
| [`canonical/candidates/`](canonical/candidates/README.md) | Complete, noncanonical successor working candidates. |
| [`design_deltas/`](design_deltas/README.md) | Versioned incremental candidates, technical proposals, research, recovery records and navigation indexes. |
| [`history/`](history/) | Historical source archive; retained for provenance and comparison, not authority. |
| [`LICENSE`](LICENSE) | Published use terms. |

## Reading and authority

- Start with [the current source guide](canonical/current/README.md) for the controlling baseline.
- Use the [15.x consolidation index](design_deltas/GARDEN_15X_NONCANONICAL_CONSOLIDATION_INDEX.md) to navigate candidate lineage and individual proposals.
- Use the [future-v16 note](design_deltas/FUTURE_V16_NONCANONICAL_DESIGN_NOTE.md) only as an evaluation plan.
- Use the [scientific research register](design_deltas/v15.10/GARDEN_SCIENCE_ALL_2026-10-09.txt) for the v15.10 research corpus.

A later version number, folder name, generated output, model agreement or passing local test does not promote a candidate. v15.5 / GSL v45.1 remains canonical unless a successor is separately reviewed and admitted.

**Evidence boundary:** specification, formal proof, implementation, empirical validation and external certification are distinct. Source hashes verify file identity, not semantic completeness or correctness.
