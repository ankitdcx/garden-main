# Garden — project overview

## What Garden is

Garden is an evolving design specification for a governed artificial general intelligence (AGI) system. Its purpose is to describe a coherent system architecture for representing entities and events, reasoning about claims and context, applying rules and values, coordinating actions and agencies, and preserving evidence, authority and accountability.

Garden is a **design project**. The canonical documents specify intended structure and behavior; they do not, by themselves, establish that a complete system exists, works, is safe, or has been independently validated.

## The problem it addresses

An increasingly capable AI system needs more than a language model that produces plausible answers. A serious system design must also make explicit:

- what entities, events, actions and claims it is reasoning about;
- where information came from and how reliable it is;
- which rules, values and permissions apply;
- who or what has authority to decide or act;
- how uncertainty, missing information and conflicting evidence are represented;
- how actions, effects, failures and corrections are recorded;
- how human interests, oversight and accountability remain visible;
- how the design can evolve without silently changing its source of authority.

Garden's documents attempt to specify these concerns as connected design obligations rather than isolated features.

## What is in this repository

This repository is primarily a **specification and research repository**, not an application source tree.

| Artifact | What it is for |
|---|---|
| Five canonical source texts | The current controlling design baseline: User, System, Technical, Annexure and Theories |
| Whole-release candidates | Complete proposed successor source sets; noncanonical until separately admitted |
| Design deltas | Smaller proposals, technical additions, research, source extracts and recovery records |
| Historical archive | Earlier source material preserved for comparison and provenance |
| Reader guides | Explanations and navigation aids; they do not replace controlling source text |

## The current canonical baseline

The current canonical release is **Garden v15.5 / GSL v45.1**, dated 2026-09-12. The five source texts are:

1. User
2. System
3. Technical
4. Annexure
5. Theories

The source manifest records each file's name, byte count and SHA-256 hash, together with the source-root identity. Begin with the [canonical source guide](canonical/current/README.md).

## How to read Garden

A practical first reading sequence is:

1. Read this overview to understand the project boundary.
2. Read [ARCHITECTURE.md](ARCHITECTURE.md) to understand the repository's authority model.
3. Use [GLOSSARY.md](GLOSSARY.md) when unfamiliar terms appear.
4. Read the canonical User and System sources for the human-facing and system-level design.
5. Consult the Technical and Annexure sources for detailed contracts, structures and supporting material.
6. Consult Theories for theory and reference-architecture material.
7. Read candidates and deltas only after understanding the canonical baseline; keep their noncanonical status visible.

The five canonical documents are large. Read them by their own headings and stable identifiers rather than treating the repository as a single linear book.

## Who this is for

- **Researchers** examining the concepts, theories, assumptions and open questions.
- **System designers** studying how the components and obligations fit together.
- **Implementers** translating specified contracts into executable systems, while separately validating that implementation.
- **Reviewers** checking consistency, evidence, provenance, safety and authority boundaries.
- **New readers** who want to understand the design before entering its technical detail.

## What this repository does not establish

The presence of a specification does not prove that its requirements are complete, mutually consistent, formally proved, implemented or empirically satisfied. A successful hash check proves byte identity only. A candidate is not canonical because it is newer, more detailed or has received positive reviews.

For the version lineage, see [VERSION_HISTORY.md](VERSION_HISTORY.md). To propose a correction or extension, see [CONTRIBUTING.md](CONTRIBUTING.md).
