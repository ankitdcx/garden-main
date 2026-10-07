# Contributing to Garden Main

This repository is a **design archive and candidate corpus**. It does not currently contain the former runtime, work-package, review-automation or deployment workspace.

## Contribution scope

Useful contributions include:
- corrections to retained design text or metadata;
- recovery of a demonstrably missing Garden design requirement;
- bounded improvements to an existing noncanonical candidate;
- a new candidate that addresses a concrete gap not already owned by existing Garden material;
- clearer source/status/dependency information that reduces ambiguity without changing meaning.

Do not add runtime, deployment, automation or review infrastructure merely to recreate the old workspace unless that is separately and deliberately chosen.

## Candidate requirements

A new or materially changed candidate should state, as applicable:

1. **Status** — normally noncanonical candidate/research until separately admitted.
2. **Problem** — the concrete failure mode or missing capability.
3. **Existing owners** — what current Garden material already governs the area.
4. **Incremental change** — what is actually new rather than duplicated.
5. **Dependencies and invalidators** — what the candidate relies on and what reopens it.
6. **Authority/effect boundary** — especially for rights, consent, privacy, safety, security, law or material human effects.
7. **Failure/UNKNOWN behavior** — uncertainty must not silently become PASS.
8. **Tests, counterexamples or falsifiers** where the proposal is sufficiently specified.
9. **Remaining work** — distinguish specification, proof, implementation, empirical validation and certification.

Keep the smallest sufficient artifact set. A concise full specification is preferable to generated bulk, duplicate status receipts or hash-only pointers.

## Status discipline

- Garden v15.5 / GSL v45.1 under `canonical/current/` remains canonical unless separately admitted.
- Material under `canonical/candidates/` and `design_deltas/` is not canonical merely because it is newer.
- Model agreement, generated artifacts, hashes, passing local tests or repository placement do not create semantic authority.
- Preserve counterexamples, unresolved conflicts and material UNKNOWN states.
- Do not silently delete predecessor meaning when simplifying or abstracting a design.
- Capability does not create authority.
- Applicable Human-Effect, rights, consent, privacy, safety, security and law constraints remain binding.

## Changing canonical source

This repository no longer carries the former automated admission machinery.

Any future proposal to change `canonical/current/` therefore needs a separately defined review/admission procedure appropriate to the consequence of the change. At minimum it must identify the exact source being changed, preserve or explicitly dispose of predecessor obligations, expose unresolved conflicts, use appropriate independent falsification/review, and retain the human decision boundary required by the controlling Garden design.

Until such a promotion is explicitly completed, keep the work under the appropriate candidate/delta path.

## Repository map

See `README.md` for the human-readable overview and `CORPUS_INDEX.json` for the compact machine-readable status/path index.
