# Whole-release candidates

**Noncanonical:** this directory holds complete five-file Garden successor working candidates. The current canonical source remains [Garden v15.5 / GSL v45.1](../current/README.md).

## Available candidates

- [v15.6](v15.6/README.md) — complete five-file successor working candidate.
- [v15.7](v15.7/README.md) — complete five-file successor working candidate.

Each candidate directory contains five source texts. Each edition manifest binds the current file bytes and identifies the original manifest in Git history. Additional amendments have their own source boundaries.

## How to use a candidate

1. Establish the current canonical baseline in [`canonical/current/`](../current/).
2. Read the candidate's own README and all five source texts.
3. Compare all five source roles, not just the version banner or one file.
4. Consult the related [incremental design deltas](../../design_deltas/README.md), which may contain supporting patches, process drafts, recovery notes or evidence.
5. Record omissions, conflicts, unresolved obligations and validation limits.
6. Treat the result as a candidate unless a separate governed admission record establishes otherwise.

## Do not confuse the two structures

The similarly named [`design_deltas/v15.6`](../../design_deltas/v15.6/) and [`design_deltas/v15.7`](../../design_deltas/v15.7/) folders contain supporting incremental work. They are not duplicate five-file releases.

Unlike `canonical/current/`, the v15.6 and v15.7 candidate directories do not currently contain source manifests. Any byte-identity or semantic comparison must therefore establish and record its own exact inputs. Hash equality alone would not prove semantic equivalence, completeness, correctness or admission.

A later version number, a selected-candidate pointer, positive review or successful local check does not make a candidate canonical.
