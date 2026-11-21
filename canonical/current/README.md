# Current Garden source identity

**Current canonical source: Garden v15.5 / GSL v45.1, dated 2026-09-12.**

This directory contains the only canonical source release in this repository. The five full source texts are:

| Role | File |
|---|---|
| User | [Garden_User_v15.5_FULL_2026-09-12.txt](Garden_User_v15.5_FULL_2026-09-12.txt) |
| System | [Garden_System_v15.5_FULL_2026-09-12.txt](Garden_System_v15.5_FULL_2026-09-12.txt) |
| Technical | [Garden_Technical_v15.5_FULL_2026-09-12.txt](Garden_Technical_v15.5_FULL_2026-09-12.txt) |
| Annexure | [Garden_Annexure_v15.5_FULL_2026-09-12.txt](Garden_Annexure_v15.5_FULL_2026-09-12.txt) |
| Theories | [Garden_Theories_v15.5_FULL_2026-09-12.txt](Garden_Theories_v15.5_FULL_2026-09-12.txt) |

## How to read the five files

- **User** — human-facing design, user experience, user rights and interaction expectations.
- **System** — system-level structure, components and flows.
- **Technical** — detailed technical design and operational contracts.
- **Annexure** — supporting clauses, registers, detailed material and cross-references.
- **Theories** — theory and reference-architecture material.

These role descriptions are reading aids. Consult the documents themselves for their full scope and controlling definitions.

## Verify source identity

[`SOURCE_MANIFEST.json`](SOURCE_MANIFEST.json) pins the exact file names, byte counts and SHA-256 hashes, and records the source-root algorithm and digest.

From this directory, run:

```sh
sha256sum Garden_User_v15.5_FULL_2026-09-12.txt \
  Garden_System_v15.5_FULL_2026-09-12.txt \
  Garden_Technical_v15.5_FULL_2026-09-12.txt \
  Garden_Annexure_v15.5_FULL_2026-09-12.txt \
  Garden_Theories_v15.5_FULL_2026-09-12.txt
```

Compare each digest and byte count with the corresponding role in the manifest. A matching set verifies file identity against that manifest. It does **not** establish semantic completeness, consistency, proof, implementation, empirical validation, certification or deployment.

## Authority boundary

Later material under [`canonical/candidates/`](../candidates/) and [`design_deltas/`](../../design_deltas/) is noncanonical unless separately admitted. Do not replace these files in place as part of candidate work. Preserve this source set as the immutable predecessor baseline.

Run `python3 verification/check_design.py` from the repository root to verify the five required roles, sizes, hashes, source root and complete structural verdict against the [recorded receipt](../../verification/v15.5/Garden_v15.5_ReferenceClosureReceipt_2026-09-12.json). The [archived scanner](../../verification/v15.5/garden_reference_closure_v15_5.py) emits its verdict as JSON. The wrapper makes any failed check return a nonzero exit status.
