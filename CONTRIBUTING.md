# Contributing to Garden Main

Thank you for helping improve the clarity, consistency and reviewability of Garden. This repository contains design specifications, candidates, research and historical records. Contributions must preserve the distinction between explaining a design and changing its authority.

## Before proposing a change

1. Read the [Overview](OVERVIEW.md) and [Architecture](ARCHITECTURE.md).
2. Check the [current canonical source](canonical/current/README.md).
3. Search the [version history](VERSION_HISTORY.md) and [design-delta index](design_deltas/README.md) for existing work.
4. Identify whether the contribution is a clarification, correction, incremental proposal, whole-release candidate or documentation-only change.
5. Check for an existing issue or pull request addressing the same material.

## Choose the right contribution type

- **Clarification:** explain existing text without changing its meaning. Cite the exact source section or stable identifier.
- **Specification proposal:** propose a new or changed requirement. State its scope, rationale, dependencies, alternatives and expected effects.
- **Design defect:** identify a contradiction, ambiguity, missing obligation, broken reference or other concrete defect. Include a minimal reproduction or counterexample where possible.
- **Research note:** record a hypothesis, evidence, method, limitations and unresolved questions. Do not present a research result as an admitted requirement.
- **Documentation improvement:** improve navigation or readability while preserving source meaning and authority.

Use the repository's GitHub issue forms for specification proposals, clarification requests and design defects.

## Required information

A useful contribution should state:

- **Source baseline:** exact release, source root or commit against which the claim is made.
- **Location:** file path and section, stable anchor or identifier.
- **Problem or proposal:** one clearly bounded issue or change.
- **Evidence:** source quotations kept brief, test results, counterexamples, calculations or external references as appropriate.
- **Status:** established fact, interpretation, hypothesis, candidate proposal or unresolved question.
- **Impact:** affected objects, relations, rules, values, interfaces, contracts or dependent documents.
- **Alternatives:** plausible alternatives considered and why they were not selected.
- **Validation:** checks performed and checks still outstanding.

Do not turn an unknown or untested condition into a negative finding or a PASS.

## Source and authority rules

- Do not edit the five canonical source files as part of an ordinary documentation or candidate PR.
- Do not modify `canonical/current/SOURCE_MANIFEST.json` unless a separately governed canonical source update explicitly requires it.
- Put complete successor working sets under `canonical/candidates/`; put incremental proposals and research under `design_deltas/`.
- Preserve historical records. Correct their interpretation with a separate notice rather than silently rewriting their original claims.
- Keep reader guides explicitly subordinate to controlling source text.
- Do not imply that a specification is implemented, formally proved, empirically validated, certified or deployed unless the corresponding evidence exists and is cited.
- Do not claim a candidate is canonical because it is newer, merged, reviewed or tested.

## Pull-request workflow

1. Start from a fresh `main` base and create a unique work branch.
2. Keep the work package bounded and declare the expected paths and affected design areas.
3. Check open pull requests and work intents for path and semantic overlap before editing.
4. Use a draft PR for substantial work when the repository's active workstream process requires it.
5. Make the final diff match the declared scope. Update the work intent if the scope changes.
6. Validate changed Markdown links, JSON/YAML syntax, references and any directly affected tests.
7. Explain what was changed, what was not changed, and what remains unverified.
8. Resolve review threads and merge only through the repository's protected pull-request path.
9. Recheck the current base and required checks immediately before merge.

Never force-push or rewrite protected history to bypass a conflict or failed check. Never weaken a substantive gate merely to make CI pass. If the applicable repository process or required evidence is unavailable, stop and explain the blocker.

## Review expectations

Reviewers should distinguish:
- factual errors from interpretive disagreements;
- source defects from proposed redesign;
- missing evidence from evidence of absence;
- local test success from broader correctness;
- documentation changes from semantic changes.

A review or merge is not, by itself, canonical admission.
