# v15.10 Future Abstraction — Compact Generative Garden

**Status:** NONCANONICAL CANDIDATE SUMMARY  
**Canonical effect:** NONE  
**Purpose:** concise statement of the future abstraction/compression direction. This complements the fuller generative-semantic-kernel candidate and does not replace retained Garden source.

## Core idea

Do not maintain thousands of independent rules when many are consequences of deeper rules.

Future Garden should aim for:

    SMALL EXPLICIT KERNEL
    + SEMANTIC GRAMMAR
    + FUNDAMENTAL RIGHTS / VALUES
    + VERIFIED DOMAIN KNOWLEDGE
    + GCSC / SAL / MATERIALITY / SAC
    =
    LARGE VERIFIED DERIVED GARDEN

The goal is not to delete complexity. It is to factor it.

## 1. Keep irreducible foundations explicit

Keep explicit:
- fundamental human rights and values;
- constitutional commitments;
- definitions of authority, consent, evidence, person, action, claim and other protected concepts;
- uncertainty semantics;
- core objects, relations, forms and qualifiers;
- fundamental meta-invariants;
- generator/checker/admission boundaries.

Example: `AGENCY × ACTION × affects × HUMAN` cannot by itself derive "humans have bodily-autonomy rights." That normative commitment must be supplied. Once supplied, many consequences can be generated.

## 2. Generate derivable detail

Use the v15.10 semantic grammar (six Pillars, ten Core Objects, twenty-four Core Relations, seven Design Forms plus context/facets/qualifiers) to represent situations.

GCSC explores typed situations. SAL rejects semantically invalid combinations without turning UNKNOWN into rejection or permission. Materiality determines applicable obligations. SAC derives candidate engineering artifacts.

A meaningful situation can generate:
- invariants;
- schema fields/bindings;
- FunctionContracts;
- state machines;
- dependencies and invalidators;
- tests and counterexamples;
- proof/assurance obligations;
- audit/explanation requirements;
- recovery/rollback/compensation requirements.

Thus the target is a complete semantic obligation package, not merely generated invariants.

## 3. Why generation is needed

Even simple relation chains create a huge raw space:

    2 objects: 10^2 × 24   = 2,400
    3 objects: 10^3 × 24^2 = 576,000
    4 objects: 10^4 × 24^3 = 138,240,000
    5 objects: 10^5 × 24^4 = 33,177,600,000

Real situations also contain branching, cycles, multiple agents, time, context, uncertainty, state changes and human effects.

Therefore do not enumerate blindly:

    raw combinations
          |
          v
         SAL
          |
          v
      materiality
          |
          v
    bounded GCSC search
          |
          v
         SAC

Search meaningful semantic classes toward a declared bounded fixed point.

## 4. Deeper invariant families

Exploratory situation tests repeatedly suggest that many specialized Garden rules may reduce to a few deeper families.

### Protected-property non-generation

Authority, consent, evidence status, substantive independence, certification, permission and similar protected properties cannot appear merely through composition or transformation without valid grounding.

This can subsume many specialized rules about delegation, swarms, proxies, tools, recursion and self-modification.

### Obligation non-erasure

Transformation, projection, abstraction, composition or optimization cannot silently remove an applicable material obligation.

Examples: summarization cannot erase uncertainty; delegation cannot erase human-effect checks; compression cannot erase specialist exceptions; optimization cannot turn hard rights into disposable preferences.

### Reachable dependency invalidation

When a material dependency changes, materially dependent conclusions must be reconsidered.

This can unify stale evidence, revoked authority, expired consent, erased data, changed models, broken assumptions, changed law/context and changed trust roots.

### Dimension-wise reversibility

Reversibility belongs to individual effects/state dimensions rather than an entire operation.

An internal database state may be reversible while a disclosure, physical effect or learned information is not.

## 5. Human-rights example

If the explicit seed says a competent person controls applicable interventions on their body, the semantic machinery can derive candidate consequences such as:
- applicable consent is required;
- consent binds to the actual person/action/scope/context/time;
- consent to X does not automatically authorize Y;
- material changes require reassessment;
- revoked/stale/UNKNOWN consent does not silently authorize execution;
- delegation and multi-agent splitting do not bypass the right;
- indirect/delayed effects remain governed;
- optimization benefit and greater capability do not create permission;
- exceptions require separately valid rules/authority.

One fundamental right can therefore generate a large specialized obligation family.

## 6. Compile rather than regenerate constantly

Do not derive everything from scratch for every runtime action.

Prefer:

    seed
      |
      v
    generate
      |
      v
    verify / falsify / compare
      |
      v
    compile + content-address + cache
      |
      v
    runtime lookup

Known situations use qualified compiled closure. Materially novel situations trigger bounded generation/research and remain UNKNOWN/BLOCKED/ESCALATED where qualification is required but absent.

Generated artifacts should be reproducibly bound to seed version, situation, context, domain inputs, generator version and qualification profile.

## 7. Use current Garden as the answer key

Do not delete the large retained Garden now.

Instead:
1. extract a proposed minimal kernel;
2. hide a bounded set of supposedly derivable Garden semantics;
3. give the generator only the kernel and permitted external inputs;
4. test whether it reconstructs the hidden invariants, schemas, contracts, tests, proofs, failure states, exceptions, dependencies and recovery rules;
5. classify misses and false positives;
6. improve the kernel/grammar/generator;
7. repeat with independently frozen held-out sets.

Only demonstrated reconstruction supports moving an explicit item to derived/compiled status.

## 8. Measure semantic compression

Illustrative example only:

    original Garden:       15,000 semantic items
    irreducible kernel:     1,500
    reproducibly derived:  13,500
    semantic compression:      90%

The actual percentage is unknown.

Current exploratory reasoning suggests a **hypothesis** that perhaps 70–90% of detailed technical material could eventually become derived/compiled rather than independently hand-maintained. This is not a measured result and must not be used as a deletion criterion.

## 9. Generated Garden may become larger than current Garden

Successful abstraction should do more than reproduce existing rules.

If a compact kernel regenerates the retained Garden and GCSC then discovers valid obligations for situations humans never considered, the result is simultaneously:
- smaller at the fundamental-source layer;
- more systematic;
- easier to regenerate/check;
- potentially more complete at the derived layer.

So abstraction is both compression and design-space exploration.

## 10. Bounded fixed-point process

    kernel G0
       |
       v
    generate situations
       |
       v
    derive obligations/artifacts
       |
       v
    compare with closure
       |
       +-- already implied ----------> reuse
       +-- stronger equivalent ------> candidate simplification
       +-- uncovered meaningful case -> candidate extension
       +-- contradiction ------------> reopen assumptions/design
       |
       v
    verify / repair
       |
       v
    repeat toward bounded G*

A bounded fixed point means no new material class appears within the declared finite search/profile/budget. It does not mean all possible future situations have been solved.

## 11. Final direction

Long-term Garden can aim to move from:

    MANUALLY ENUMERATED GARDEN
              |
              v
    SEMANTICALLY FACTORED GARDEN
              |
              v
       SMALL EXPLICIT KERNEL
      + VERIFIED GENERATIVE CLOSURE
              |
              v
       DERIVED / COMPILED GARDEN

Keep what is genuinely fundamental explicit. Reproducibly derive what is truly a consequence. Load and verify empirical/domain facts rather than inventing them.

Until reconstruction and adversarial tests demonstrate lossless derivability, the existing full Garden remains the regression oracle and must not be removed merely because a model claims it can regenerate it.
