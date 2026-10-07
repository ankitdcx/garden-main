# Garden — Representation Escape & Independence Hardening

**Patch:** `GARDEN-REP-2026-09-22`  
**Existing candidate:** `V1511-REP-001` · **Reconciled revision:** 1.1 · **Date:** 2026-09-22  
**Status:** ADDITIVE NONCANONICAL CANDIDATE — admission, domain-profile qualification and integrated certification remain required.  
**Canonical effect:** NONE. This document proposes a revision of the existing candidate, not a second registration.

## 1. The problem and the limited change

Independent reasoners do not necessarily provide independent verification when they inherit the same representation. A common transformation can remove a material fact before any reasoner receives it. Different models may then agree because none can inspect the missing fact.

Garden already records computational representations and their losses, varies reasoning strategies, compares alternatives, investigates counterexamples, tracks dependencies and evaluates verifier independence. This candidate adds two explicit obligations to those mechanisms: select representation coverage for the actual decision, and evaluate whether shared representation losses undermine the particular corroboration claim. It does not create another Garden subsystem.

The operation is to route the same subject through qualified, materially different representations where the applicable profile requires them. It is not to imitate a novice. Nor is every differently named view independent, every common source disqualifying, or every task required to use multiple views.

The rules below are candidate requirements. “SHALL” describes the proposed contract if admitted; it does not assert that Garden already implements or satisfies it. The included executable reference checks are bounded synthetic receipt replays. They do not discover unknown representations, authenticate evidence or certify Garden.

## 2. Identity and the abstraction model

The supplied labels `REP-001..009` and `TEST-REP-001..008` conflict with existing BRIDGE identifiers. BRIDGE retains its identifiers and meaning. This revision uses candidate-local `REPESC-001..009` and `TEST-REPESC-*`; a registry update requires separate admission. Original labels remain source-qualified aliases in §11, never ambiguous global aliases.

The new abstract model remains the organizing model:

| Candidate element | Existing expression | Meaning retained |
| --- | --- | --- |
| RepresentationPortfolio | Registry macro; CONSTRUCT, STATE, RELATION, RULE, PROJECTION | Finite, versioned entries and their qualification state. |
| RepresentationCoverageProfile | Profile macro, with its property and authority contracts | Context-specific obligations, selection rules and bounds. |
| Transformation and comparison | PROJECTION and Function contracts | Subject binding, preserved/lost properties, comparison meaning and validity. |
| REPESC rules | RULE and CONTRACT | Guards on coverage and corroboration; no execution authority. |
| Route and assessment records | Existing Receipt macro | Evidence, provenance, dependency bindings and result state. |
| Routing and invalidation | PROCESS, STATE and RELATION | Bounded evaluation and affected-use reopening. |

`CAUSAL_GRAPH`, `AUTHORITY_GRAPH` and the other representation kinds are task/profile classifications. They are neither additional Design Forms nor additional Core Objects. A macro or kind label supplies no proof of semantic equivalence, adequacy or independence.

GCSC applies the existing semantic-coverage process to these contracts: identify applicability; preserve subject, relation, qualifiers and exceptions; generate bounded obligations; require witnesses; record unavailable cases and residuals. Merely counting kinds, successfully parsing this document or executing the reference fixtures cannot discharge GCSC semantic-closure obligations. Any structured projection that omits material clauses remains partial and cannot replace the controlling text.

## 3. Contracts and their existing owners

These are specializations of existing registry, profile, BRIDGE, reasoning, assurance, comparison and receipt contracts. The names identify semantic contracts, not new storage services or universal schema families. Reuse existing qualified fields and references when they already represent the required meaning.

### 3.1 RepresentationPortfolio

A finite versioned registry SHALL identify `PortfolioID`, `Version`, `DesignEpoch` and `ResearchFrontierRef`. Its entries SHALL have stable representation identity and declare:

| Required meaning | Minimum content |
| --- | --- |
| Kind | `RepresentationKind`, with its definition and purpose-relative distinctness criteria. Encoding is recorded separately. |
| Subject binding | Source object/snapshot, decision context, properties checked and relevant source lineage. |
| Transform/projection | Qualified transformation reference and version, preprocessing lineage, input/output contract and validity domain. |
| Applicability | Conditions under which the representation is qualified for the property and assurance obligation. |
| Preservation and loss | Properties intentionally preserved or suppressed, `KnownLosses`, unknown preservation claims and supporting BRIDGE records. |
| Shared dependencies | `KnownSharedAssumptions`, material shared transforms, data/evidence lineage and failure-mode dependencies. |
| Relations | `IndependenceRelations` and distinctness/complementarity claims, each scoped, evidenced and invalidatable. |
| Qualification | Admission/qualification status, responsible owner, evidence, freshness and invalidators. |

This entry structure retains the supplied `RepresentationKind[]`, `Transform/Projection[]`, `ApplicabilityConditions[]`, `KnownLosses[]`, `KnownSharedAssumptions[]` and `IndependenceRelations[]` meanings while binding each value to the entry it describes. Unassociated parallel arrays do not establish those bindings.

Illustrative kinds are `SOURCE_TEXT`, `SEMANTIC_MODEL`, `CAUSAL_GRAPH`, `AUTHORITY_GRAPH`, `RESOURCE_FLOW`, `TEMPORAL_MODEL`, `STATE_TRANSITION_MODEL`, `PHYSICAL_MODEL`, `HUMAN_EFFECT_MODEL` and `GEOMETRIC/STRUCTURAL_MODEL`. This list is neither exhaustive nor universally mandatory.

An entry with missing required loss declarations or demonstrated undeclared material suppression SHALL NOT qualify for the affected obligation. Research use can retain an unqualified entry with its status explicit. A declaration is evidence of what was declared; it is not proof that every loss has been found.

### 3.2 RepresentationCoverageProfile

`RequiredRepresentationCoverage(Context) -> RepresentationCoverageProfile` SHALL be a bounded interpretation of an admitted, versioned profile rule table. Reuse existing profile selection and reasoning-plan machinery. A function name without a qualified domain table is not an operational implementation.

The profile SHALL preserve the supplied fields: `ProfileID`, `RiskClass`, `ConsequenceClass`, `RequiredRepresentationKinds[]`, `MinimumKindDiversity`, `OptionalRepresentations[]`, `SearchBudget`, `StoppingRule` and `ResidualUnknownPolicy`. It SHALL also bind the profile/rule-table version and DesignEpoch, decision and property scope, applicability evidence, qualified alternatives, distinctness criteria, required comparison and shared-loss checks, validity conditions, dependency closure and selection authority.

Selection SHALL follow this finite procedure:

1. Bind the subject, purpose, source snapshot, context, profile table and relevant registry versions before using evaluated results to satisfy the profile. A proposer cannot select a weaker profile because its chosen representation concealed a trigger.
2. Evaluate every rule-table row with the existing explicit TRUE/FALSE/UNKNOWN semantics. TRUE contributes its obligations; FALSE contributes none. UNKNOWN preserves potentially applicable obligations and its diagnostic. It cannot silently become FALSE.
3. Form the union of applicable obligations and the least fixed point of their declared dependencies within the finite registered set. A qualified alternative discharges only the exact obligation for which the profile admitted it. Conflicts, missing input classes and unresolved applicability remain non-qualifying unless an admitted conservative rule completely resolves them.
4. Freeze the resulting requirements and exact coverage predicate. Extra optional work, a high score or agreement elsewhere cannot compensate for a missing mandatory obligation.
5. Stop at the declared resource bound. Record unperformed obligations and the remaining frontier; follow existing defer/non-admission rules for affected consequential use. Exhaustion is not successful completion.

No universal `K=3`, `D=2` or similar threshold is introduced. A qualified low-impact profile can require no additional route. A qualified proof case can require one decisive method where existing assurance policy allows it. Mandatory additional properties remain mandatory even when one property has a decisive proof.

## 4. Three different representation claims

Keep these claims separate:

| Claim | What must be established |
| --- | --- |
| Kind distinctness | Two routes differ materially for the stated purpose, beyond encoding or a trivial transformation. |
| Coverage complementarity | A route exposes or separately checks a relevant property/failure mode that another route omits or obscures. |
| Representation independence for corroboration | Shared representation assumptions, transformations or losses do not defeat the specified independent-checking claim under the applicable failure model. |

No row entails another. Two representations of the same source may provide qualified complementary coverage while sharing data lineage. Two differently named kinds may inherit the same decisive loss. Pairwise distinctness does not prove independence of the entire verifier group or probabilistic independence.

Assess each relation against the route pair or set, property/claim, context, subject snapshot, validity bindings, relevant failure model and supporting evidence. Record SATISFIED, VIOLATED or UNKNOWN through existing result types. Missing distinctness evidence is UNKNOWN, not invented sameness or independence. Where group dependence is material, assess the group dependency rather than extrapolating from pairwise results.

For a profile that uses a minimum distinct-kind count, count qualified witnesses only. One bounded reference procedure enumerates eligible distinct-kind subsets of the required size in a stable order. A subset qualifies only if every required pairwise distinctness obligation is established. A known false pair disqualifies that subset even if another pair is unknown. If all subsets in the finite current eligible pool are disqualified, the count is insufficient for that pool. If an unresolved subset or unsearched budget remainder could qualify, preserve UNKNOWN. Neither result claims that future routes cannot qualify. Mandatory-route completion is a separate check.

This counting procedure does not determine semantic distinctness from names; it consumes scoped evidence from its owner. It does not replace required property coverage or group-independence obligations.

## 5. Candidate invariants

### REPESC-001 — Representation non-completeness

For consequential reasoning, familiarity, conventionality, historical success or dominance of an active representation SHALL NOT constitute evidence that it is complete for the present purpose. A separately justified bounded correspondence/completeness proof remains valid within its declared semantic closure; familiarity and agreement cannot substitute for that proof.

### REPESC-002 — Profile-selected routing

A consequential conclusion SHALL satisfy the representation obligations of its applicable qualified coverage profile before the affected acceptance or corroboration claim qualifies. “Orthogonal routing” means deliberately using qualified materially different views where required; the word itself establishes no independence. Missing profile qualification or unresolved applicability SHALL remain explicit and non-qualifying for the affected obligation.

### REPESC-003 — Kind distinctness

Multiple transformations derived from substantially the same abstraction SHALL NOT satisfy representation-diversity requirements merely because their encodings differ. Distinctness SHALL be assessed for the declared purpose and checked properties using §4, without treating different labels as evidence.

### REPESC-004 — Material divergence and propagation

Information from a required representation that could materially change the conclusion, assumptions, uncertainty, authority assessment or human effects SHALL reopen the affected conclusion. The same applies to material information actually discovered through an optional route. Potentially material divergence whose relevance remains unresolved SHALL not be silently dismissed.

Use a precommitted, purpose-relative materiality predicate and semantically compatible property comparisons. Through the existing dependency owner, invalidate/recompute the affected downstream closure as applicable, preserve evidence of both versions, and retain unaffected valid conclusions. Unknown or bounded-out dependency closure SHALL not justify consequential reuse of possibly affected claims.

### REPESC-005 — Bounded convergence

Agreement alone across qualified required representations establishes at most a scoped `PRESUMED_CONVERGENT` result after mandatory coverage and required comparisons are satisfied and material divergence is resolved. Convergence is scoped to the profile's explicitly bound comparison obligations; it does not assert that every route answers the same question or that every possible pair was compared. It SHALL NOT establish unconditional `REPRESENTATION_COMPLETE`, `PROVEN_COMPLETE` or an equivalent universal claim. A separately valid bounded proof is not demoted by this rule.

### REPESC-006 — Coverage failure

Failure to evaluate a mandatory representation or satisfy another mandatory coverage obligation for consequential reasoning yields UNKNOWN/INCOMPLETE for the affected coverage, not PASS. A known violation remains recorded as a violation; missing evidence elsewhere cannot erase it. A scoped result for an unaffected obligation can remain valid.

### REPESC-007 — Open representation frontier

The registered portfolio SHALL be treated as finite and epistemically incomplete. Discovery or generation of unregistered kinds belongs to the existing Research Frontier process, with materially relevant unresolved questions recorded there. Research cannot silently activate or certify a proposed kind.

Generic uncertainty that unknown kinds may exist does not impose infinite search on every task. A known or plausibly material uncovered obligation follows the applicable residual-unknown policy and existing hard gates. Bounds and residuals SHALL remain visible.

### REPESC-008 — Constitutional precedence

REP expands epistemic inspection only. It SHALL NOT create authority or weaken constitutional, rights, consent, privacy, safety, evidence, Human-Effect Closure, legal or other hard gates. Successful coverage and useful analysis are not execution permission. Existing owners retain those decisions.

### REPESC-009 — Portfolio diversity integrity

As the anti-gaming enforcement of REPESC-003, a portfolio SHALL NOT satisfy diversity requirements through nominal, syntactic or trivially transformed variants of substantially the same relevant representation kind. `AST`, whitespace-stripped AST, comment-stripped AST and normalized AST do not become four qualified kinds by listing them separately.

Where required distinctness cannot be established, retain UNKNOWN for that distinctness claim; where required representation-independence evidence cannot be established, retain `REPRESENTATION_INDEPENDENCE = UNKNOWN`. Do not infer either claim from the other. This rule uses the same distinctness predicate as REPESC-003, not a competing second definition.

## 6. Independent verification

Two reasoners SHALL NOT be considered fully substantively independent merely because they are different models or processes when their conclusions materially depend on the same potentially lossy representation.

Record the following separately, with their applicable scope, failure model, evidence and current status: `ModelIndependence`, `DataIndependence`, `EvidenceIndependence`, `ReasoningStrategyIndependence`, `RepresentationIndependence`, and `AuthorityIndependence`. Retain existing lineage, trust-root and control distinctions where applicable. Do not automatically collapse these into `Independent=true` or multiply statistical confidence from their labels.

Shared source material is not, by itself, a reason to reject every verification claim. The question is whether common transformations, assumptions or losses defeat the particular property-specific corroboration claim. A materially shared blind spot makes an unsupported independent-corroboration claim ineligible. An unresolved correlation question remains unresolved. Neither observation automatically determines authority/control independence or the adequacy of a separately qualified proof checker.

Where the RCC candidate applies, reuse its threat-model-bound control, correlation, competence and quorum checks. This patch supplies representation lineage and shared-loss information to those checks; it does not ratify RCC, redefine control independence or claim to complete substantive-independence inference.

## 7. Results, freshness and correction

Record a logical product through existing receipts rather than a single success flag:

| Result component | Required distinction |
| --- | --- |
| Input and profile validity | Qualified, current and scope-compatible versus missing, stale, conflicting or unresolved. |
| Mandatory coverage | Per-obligation completion and the unperformed frontier. |
| Kind-diversity obligation | Qualified witness, insufficient current pool or unresolved/bounded search. |
| Comparison | Presumed convergence, material divergence, unresolved comparison or legitimately not required. |
| Independence | Each required dimension and material group dependencies, without cross-dimension inference. |
| Existing gates | Their current results and authority, preserved independently of REP coverage. |

Complete mandatory routing does not imply agreement, truth or authority. A qualified one-route profile can establish `BOUNDED_COVERAGE_SATISFIED` without claiming multi-representation convergence. Equal answer strings are not a semantic comparison receipt. Material dissent from an evaluated optional view cannot be omitted to manufacture convergence.

Bind outputs to their source snapshot, profile and rule-table versions, transform/registry versions, property scope and validity domain. Each required comparison identity SHALL bind its intended claim, checked properties and participating representation identities. Renaming a repeated A–B comparison cannot satisfy an A–C obligation; comparing a route with itself cannot establish cross-view convergence. Conflicting requirement flags or wrong-claim receipts are invalid inputs, not evidence of agreement. A material change to these bindings or supporting independence evidence stales the affected result under existing dependency rules. A synthetic `current=true` field is not authentication of these conditions; a deployed implementation must check the actual owner evidence.

## 8. Reuse and boundaries

| Existing mechanism | Reuse | Candidate increment |
| --- | --- | --- |
| BRIDGE | Representation contracts, transforms, declared losses, source bindings, correspondence proofs and invalidators. | Require profile-selected representation-kind coverage and common-loss assessment for the decision. |
| Assurance and independent verification | Task-relative qualification, common-mode analysis, evidence lineage and explicit UNKNOWN. | Record representation dependence as its own dimension and apply it to the corroboration claim. |
| ReasoningStrategyPortfolio / reasoning plans | Qualified portfolio selection, versions, alternatives, evidence and bounds. | Add representation selection as a separate dimension; strategy/model diversity is not representation diversity. |
| Compare | Typed comparisons, mappings, alternative analysis and bidirectional gaps. | Compare aligned decision properties across selected representations. |
| GCL | Qualified causal models, baselines, assumptions and evidence. | Route to causal views when required; a graph label supplies no causal warrant. |
| CDDT | Bounded counterexample and alternative search, loss examination and uncertainty. | Investigate representation-exposed divergences using the same mechanisms. |
| HEC | Direct, indirect, delayed and uncertain human-effect obligations. | Keep relevant human effects visible across representations; REP cannot narrow HEC. |
| Dependency / validity | Affected-claim invalidation, freshness and rechecking. | Add current profile/transform/loss evidence as dependencies. |
| Research Frontier | Owned questions, evidence gaps, discriminating work and reactivation. | Record materially relevant unrepresented properties or unknown kinds. |
| GCSC | Bounded semantic obligation generation, qualifications and residual coverage. | Check this specialization without converting view counts into semantic completeness. |

BRIDGE's assurance-selected multiple-method rule and its valid bounded correspondence-proof route remain intact. This candidate is a specialization and integration condition over overlapping existing mechanisms, not proof that those mechanisms never examine representations.

## 9. Conformance specifications and executable scope

The following eleven behaviors retain the union of the user's eight tests and the existing repository candidate's ten. Test IDs denote specifications. A passing reference fixture tests only its encoded bounded case and supplied premises.

| Candidate test | Required oracle |
| --- | --- |
| TEST-REPESC-001 — Familiar representation trap | A planted material property omitted by the conventional view is exposed by an applicable alternative, and its conclusion is reopened. Attempting another view alone is insufficient. |
| TEST-REPESC-002 — Fake diversity | Four syntactic AST variants do not satisfy a multi-kind obligation. |
| TEST-REPESC-003 — Divergence propagation | Reopen the changed claim and invalidate its affected dependants; retain a disconnected valid branch. Incomplete closure suspends possibly affected uses. |
| TEST-REPESC-004 — False completeness | Qualified agreement yields at most scoped presumed convergence; reject promotion to unconditional completeness or authority. |
| TEST-REPESC-005 — Missing mandatory view | Missing required coverage remains non-qualifying even if optional views agree. |
| TEST-REPESC-006 — Unknown distinctness | Required distinctness without adequate evidence remains UNKNOWN. |
| TEST-REPESC-007 — Shared blind spot | Different models sharing a named material preprocessing loss cannot claim independent corroboration for that property. |
| TEST-REPESC-008 — Constitutional non-override | Useful, successful representation analysis preserves a blocking existing gate and creates no authority. |
| TEST-REPESC-009 — Risk-sensitive coverage | Qualified low- and high-consequence profiles can differ. No universal multi-kind constant is imposed; a permitted bounded single-route case can succeed. |
| TEST-REPESC-010 — Research boundary | Preserve the open frontier within the declared bound. Generic unknown kinds alone do not block forever; a material uncovered obligation receives its existing non-qualifying disposition. |
| TEST-REPESC-011 — Loss declaration | Missing required loss declarations or demonstrated undeclared material suppression prevent qualification for the affected obligation. |

Further focused fixtures check a positive multi-view case, explicit comparison versus matching strings, stale scope, optional material dissent, non-transitive distinctness, search exhaustion, known false pairs alongside unknown pairs, uncertain authority independence, cyclic/bounded dependency traversal, and pairwise diversity with group correlation. The accompanying receipt lists precisely which cases were executed and their expected outcomes.

The reference evaluator consumes synthetic profile resolution, qualification, freshness, relation evidence and gate results as premises. It does not implement the admitted profile-table selector, prove transformations faithful, recover arbitrary hidden properties, establish empirical independence, verify authority, or provide a Garden execution path. The planted latency example demonstrates one known loss: a mean of 60 ms for `[20,20,20,20,220]` does not establish that every event is below 100 ms. It is not a general discovery algorithm.

Before admission, qualify real domain tables and evidence producers; bind these contracts into actual reasoning, assurance, dependency and GCSC owners; run their applicable integrated conformance and adversarial gates; and resolve any remaining source conflicts. Reference replay success is not that admission.

## 10. Limitations and non-normative inspiration

**REP proves bounded representation coverage, never universal meta-layer coverage.**

This sentence states the intended upper bound on a qualified implementation's claim. This candidate and its trace do not themselves supply a formal proof. A proof claim additionally requires its applicable proof contract and sound checking evidence. Even a completely enumerated finite registry is not a complete representation of reality.

REP cannot guarantee that every relevant representation has been considered; discover kinds no one has conceived; prove that its portfolio is epistemically complete; guarantee the best route was selected; or guarantee independence in every material respect. It does not make unbounded meta-layer search decidable.

The prompt **“Can I describe this object without using its conventional name or assumed function?”** is retained as a non-normative research/reasoning aid. Success or failure is not evidence, certification or a conformance result. The observation that a fluent reader sees meaning while a non-reader notices script geometry is motivation. `NOVICE VIEW`, `EXPERT VIEW` and the embroidery metaphor do not enter normative Garden as representation kinds or requirements.

## 11. Source-qualified migration and preservation

| Supplied patch-local rule | Reconciled candidate-local rule | Treatment |
| --- | --- | --- |
| REP-001 | REPESC-001 | Preserve non-completeness; protect valid bounded proofs. |
| REP-002 | REPESC-002 | Preserve routing; specify qualified profile selection. |
| REP-003 | REPESC-003 | Preserve substantive distinctness. |
| REP-004 | REPESC-004 | Preserve reopening; include actually discovered optional material dissent and bounded affected closure. |
| REP-005 | REPESC-005 | Preserve agreement's upper bound; separate it from proof. |
| REP-006 | REPESC-006 | Preserve non-PASS for missing mandatory coverage and retain known violations. |
| REP-007 | REPESC-007 | Preserve open frontier without requiring infinite search. |
| REP-008 | REPESC-008 | Preserve all existing hard gates. |
| REP-009 | REPESC-009 | Preserve anti-gaming as explicit enforcement of rule 003. |

The first eight supplied `TEST-REP-00n` labels map, in their original order, to `TEST-REPESC-00n`. These aliases refer only to `GARDEN-REP-2026-09-22`. BRIDGE's identically spelled source labels continue to resolve to BRIDGE.

| Existing repository candidate test | Reconciled specification |
| --- | --- |
| REP-T001 / list 1 — Same-kind gaming | TEST-REPESC-002 |
| REP-T002 / list 2 — Orthogonal discovery | TEST-REPESC-001 and its reopening obligation in 003 |
| REP-T003 / list 3 — False completeness | TEST-REPESC-004 |
| REP-T004 / list 4 — Missing coverage | TEST-REPESC-005 |
| REP-T005 / list 5 — Risk sensitivity | TEST-REPESC-009 |
| REP-T006 / list 6 — Downstream invalidation | TEST-REPESC-003 |
| REP-T007 / list 7 — Research boundary | TEST-REPESC-010 |
| REP-T008 / list 8 — Authority boundary | TEST-REPESC-008 |
| REP-T009 / list 9 — Verifier independence | TEST-REPESC-007 |
| REP-T010 / list 10 — Loss declaration | TEST-REPESC-011 |

The reconciliation was compared with the recovered v15.x corpus, the standalone abstraction/GCSC candidate, and the repository candidate pinned at commit `daecae76e877daccf5bdf2a3ec64424afe7b0d0a`, together with the candidate-sweep branch pinned in the audit manifest. Source preservation, collision scanning, semantic review and runtime certification are different claims. The companion audit states the exact retrieved scope, failures or exclusions, and verification performed. No assertion of exhaustive access to all project chats or repository history is made.