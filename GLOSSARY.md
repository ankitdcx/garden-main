# Garden glossary

This glossary is a navigation aid, not a replacement for definitions in controlling source documents. Each entry identifies its status and points to a source where readers can verify the intended use. Where an acronym's expansion is not clearly established by the repository's current reader guides, this glossary does not guess an expansion.

## Core repository and source terms

| Term | Reader-facing meaning | Status / source |
|---|---|---|
| **Garden** | The evolving design specification and associated research for a governed AGI system. | Project-level description; see [Overview](OVERVIEW.md). |
| **GSL** | Garden's typed semantic language. The v45.1 baseline defines the objects, relations and design forms used by the canonical design. | Canonical; [v15.5 source guide](canonical/current/README.md). |
| **GSL v45.1** | The GSL version associated with the current canonical Garden v15.5 release. | Canonical; [source manifest](canonical/current/SOURCE_MANIFEST.json). |
| **Object** | A typed category in the GSL semantic foundation. The v45.1 baseline has 10 objects. | Canonical; five source texts. |
| **Relation** | A typed connection between GSL objects. The v45.1 baseline has 24 relations. | Canonical; five source texts. |
| **Design Form** | One of the seven design forms recorded in the v45.1 baseline. | Canonical; five source texts. |
| **Canonical source** | The source set currently holding authority in this repository. It is v15.5 / GSL v45.1. | Canonical; [source guide](canonical/current/README.md). |
| **Source manifest** | The machine-readable record of canonical source file names, byte counts and SHA-256 hashes, plus the source-root identity. | Canonical identity record; [SOURCE_MANIFEST.json](canonical/current/SOURCE_MANIFEST.json). |
| **Source root** | A digest identifying the canonical set through the manifest's declared algorithm. It identifies a source set; it does not prove semantic correctness. | Canonical identity metadata; manifest. |
| **DesignEpoch** | A source-identity label bound to a particular Garden release and source root when a process requires exact baseline identity. | Process/identity term; use the exact value declared by the applicable record. |

## Status and evidence terms

| Term | Reader-facing meaning |
|---|---|
| **Candidate** | A proposed design or successor source set that has not thereby become canonical. |
| **Delta** | An incremental proposal or source-level change package, not a complete release by default. |
| **Historical** | Preserved material whose statements describe its own earlier context and do not override current authority. |
| **UNKNOWN** | An unresolved or unavailable state. It must not be silently converted into FALSE, PASS or a negative finding. |
| **Proof** | A formal argument discharged against stated premises and obligations; not the same as review or testing. |
| **Implementation** | An executable realization of specified behavior. A specification alone is not implementation evidence. |
| **Empirical validation** | Test or observation evidence within a defined scope; it does not automatically establish universal correctness. |
| **Admission** | A separate governed act that changes a candidate's authority status. A version number, review or merge alone is not enough unless the applicable process says so. |

## Terms used in candidate and research material

These terms occur in later noncanonical materials. Their use here is deliberately scoped to those materials; this glossary does not promote them into v15.5 canonical semantics.

| Term | How it is used in the repository | Where to read |
|---|---|---|
| **GCSC** | A candidate semantic-coverage process: identify applicability; preserve subjects, relations, qualifiers and exceptions; generate bounded obligations; require witnesses; and record unavailable cases and residuals. | [GCSC/semantic-kernel candidate](design_deltas/v15.10/GENERATIVE_SEMANTIC_KERNEL_AND_DERIVED_GARDEN_CANDIDATE.md) and [REP candidate](design_deltas/v15.11/rep/GARDEN_v15.11_REP_RECONCILED_CANDIDATE.md). |
| **SAL** | In the v15.10 candidate pipeline, the component associated with structural, completeness, join, coherence and interpretation diagnostics. | [DSC candidate](design_deltas/v15.11/dsc/GARDEN_DSC_001_REV2_CANDIDATE.md) and [semantic-kernel candidate](design_deltas/v15.10/GENERATIVE_SEMANTIC_KERNEL_AND_DERIVED_GARDEN_CANDIDATE.md). |
| **SAC** | In the v15.10 candidate pipeline, the component associated with generated candidate schemas, tests and obligations. | [DSC candidate](design_deltas/v15.11/dsc/GARDEN_DSC_001_REV2_CANDIDATE.md). |
| **TRACE** | A named term in the v15.7 candidate line and related later materials. Its precise expansion and contract should be taken from the source document in which it is used, not inferred from the acronym alone. | [v15.7 candidate guide](canonical/candidates/v15.7/README.md) and [design-delta index](design_deltas/README.md). |
| **AAP / UPA** | Named process and architecture terms used in Garden source material. Their precise requirements are context-dependent; consult the controlling source section rather than relying on an abbreviated glossary paraphrase. | Five canonical source texts; start at [canonical source guide](canonical/current/README.md). |

## How to use this glossary

- Follow the source link when a term affects a design decision or interpretation.
- Check the status column before treating a candidate term as canonical.
- Prefer the controlling source's definition over a shortened reader-facing description.
- If two sources use a term differently, preserve the distinction and raise a clarification request rather than silently reconciling them.
