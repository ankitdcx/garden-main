# Garden v15.11 candidate — Coupled Transitions and Responsibility Preservation

Revision: 1.0, 22 September 2026. Status: **DESIGN CANDIDATE — NOT CANONICALLY ADMITTED**.

This candidate translates the supplied Astra handoff into two bounded application profiles under existing Garden owners. It is not a new general theory of society or a new authority source. The normative-looking requirements below describe proposed candidate acceptance conditions; they do not amend the current baseline merely by being written.

## Scope and reuse decision

The inspected source is the 19,697-record v15.10.1 standalone catalogue, SHA-256 `fc556b192278bebf939334a98b442d593360a0666a3836e6970fa4aee86e5e65`. The source comparison found existing multi-order consequence analysis, latent and collective Human-Effect duties, unstable-feedback cases, finance-state distinctions, bottleneck reassessment and responsibility continuity. The delta is a concrete application and test specification. Existing specifications retain their own status; references to CLIC, OAC, RCC or other candidate material do not admit them or claim implementation.

**Reuse before extending.** Resolve each proposed input/output and duty against existing contracts first. Add a test or explanation when the behavior is already available. A genuinely missing field or comparator requires an explicit owner-reviewed extension. This candidate registers no new SchemaID or global vocabulary. Local variables, case labels and checker keys are specification notation only.

| Design Form | Coupled transition profile | Organizational responsibility profile |
|---|---|---|
| CONSTRUCT | Bound model, scenario, quantities and trajectory records | Bound organization, duty inventory and handover records |
| CONTRACT | Typed update, timing, accounting and model-validity conditions | Scoped duty, transfer, review, appeal and continuity conditions |
| STATE | Dated balances, capacities, exposures and current assumptions | Before/after allocations and current authorization conditions |
| RELATION | Qualified links, delays, shared causes and resource dependencies | Duties, holders, delegations, shared obligations and appeal routes |
| PROCESS | Bounded propagation, comparison, observation and invalidation | Finite mapping, assessment, handover and effect-time recheck |
| RULE | Units, valid domains, retained unknowns and hard-obligation separation | Valid disposition of each duty; functioning oversight; no authority creation |
| PROJECTION | Group/time outcome views and model-qualified explanations | Traceable decisions, responsibility views and accessible explanation |

The Forms overlap. This table organizes a proposed representation; it does not certify its type bindings or establish semantic equivalence.

## Profile A — Coupled transitions and distribution

**Disposition:** proposed v15.11 profile and acceptance requirements. Not admitted to the v15.10.1 baseline, not an economic forecast, and not a claim that a societal controller has been implemented. This is an original specification proposal derived from the supplied conversation; no external empirical findings are asserted.

**Purpose:** make Garden test an action against delayed interactions among the systems it can materially affect. A cheaper product can coexist with income loss, debt stress or reduced access to essentials. A beneficial technological loop and a harmful distribution loop can operate at the same time. Garden should represent both without deciding the outcome in advance.

The engineering object is a bounded, typed, delayed interaction model. Fluid, vortex and supercell imagery motivates questions about amplification and persistence; it supplies neither physical equations for civilization nor an evidential basis. There is no universal scalar “Outcome = forcing / damping” law in this proposal.

### A1. What already exists, and the narrow proposed addition

The retained design already requires Human-Effect Closure for direct, indirect, latent, cumulative, relational, emergent, institutional, tool-mediated and infrastructure-mediated effects. It already requires a `CausalClosureReceipt/v1` when a materially consequential causal path crosses subsystem boundaries, records known gaps, and forbids dropping an effect because another owner also participates. It already has qualified parameters, model uncertainty, future stress scenarios and a bottleneck-first funding rule.

Therefore the new contribution is **a concrete profile for applying those duties to changing, coupled systems**, with executable acceptance conditions for delays, feedback, changing constraints, household distribution and incomplete causal knowledge. It is not a new general obligation to care about indirect effects.

| Existing owner or mechanism | Proposed specialization |
|---|---|
| Human-Effect Closure and applicable domain owners | Apply existing duties to a declared time-indexed propagation scope, including exposed groups and coupled collective effects. |
| P024 Causal Safety; `CausalClosureReceipt/v1` | Bind hypothesized and supported links separately; retain assumptions, unresolved paths and the final effect classification. P024 remains the semantic owner. |
| `Engine.Compare`, CLIC, applicable ActionGate/AAP | Compare relevant alternatives and causal gaps; preserve cross-owner continuity; independently enforce current authority at an effect. |
| `REG-PARAM-001` | Type each operational constant as the applicable measured value, formal bound, engineering target or profile parameter, with units and invalidators. |
| Model/measurement/simulation foundations and applicable theory/domain owners | Bind quantity types, source/sink conventions, timing, model error and domain validity. Reusing mathematical machinery does not turn money, employment or authority into conserved physical fluids. |
| `AdversarialFutureScenario`, `FutureStressAssessment` | Store bounded scenarios, generated trajectories, affected entities, rights, uncertainty and scenario-specific results. |
| Continuous Resource Allocation and CRA-014 | Reevaluate the limiting dependency after a capacity or demand change; compare expansion, substitution, redesign and delay. |
| Profile / DynamicalSystemProfile and existing seven Design Forms | Express the specialization as a profile with controlled transitions and obligations. No new Core Object, Core Relation, schema ID or global status is proposed here. |

The `DynamicalSystemProfile` macro provides a form composition, not a fully validated implementation schema. Exact field bindings and owner acceptance remain an admission task. Mathematical variables and local report labels below are specification notation, not new Garden registry entries.

### A2. Declare a finite assessment before running it

An assessment freezes the following inputs as part of its existing profile, scenario and evaluation bindings:

- **Purpose and decision:** the question being answered; the action alternatives, including a relevant no-change alternative; applicable hard obligations; and the authorized decision owner. Inaction can have effects too.
- **Boundary:** represented entities, groups, sectors, jurisdictions, resources and outside-system interfaces. Record potentially material omitted interfaces. Include obligations concerning nonhuman life when applicable.
- **Time:** step size `Δt`, finite horizon `H` steps, event order within a step, maximum delay `D`, observation latency and parameter-validity windows. A known material deadline just beyond the horizon is an unresolved boundary, not a safe result.
- **Models and scenarios:** a finite named set of alternative model structures and scenarios. Declare which are empirical hypotheses, stress cases or synthetic checks. No default probability is assigned to a scenario.
- **Uncertainty:** allowed initial-state sets, parameter ranges, dependency constraints, model-error bounds and specified disturbances. Record the source and validity of each bound. Unknown or disputed bounds remain unknown; convenient limits cannot be presented as established limits of reality.
- **Resources and stopping:** limits on model size, expanded time steps, parameter cases, runtime and memory; numeric method and tolerances; stopping and incomplete-result behavior.
- **Materiality and observation:** the predeclared applicable materiality rules, exposed groups, effect measures, required observations, monitoring delay and invalidation triggers. These cannot be narrowed after seeing which tests pass.

The assessment output names exactly which model, scenario, parameter cases, times and groups were examined. A finite scenario set is a declared test scope, not all possible futures. Once an existing materiality rule requires assessment of a pathway, an operator cannot evade it by declining this optional implementation profile, choosing a shorter horizon, omitting a group or excluding a difficult model. An alternative qualified assessment may discharge the same duty; otherwise the material duty and unresolved scope remain visible to the applicable decision gate.

### A3. Typed delayed network and state update

For each model `m`, define a finite directed graph `G_m = (V_m, E_m)`. Nodes represent specified quantities or states, not free-floating labels such as “the economy.” Examples include a cohort's cash balance, hours of employed work, productive capacity, outstanding principal, overdue payments, available energy and access to an essential service.

Every node declares meaning, unit or enumerated type, aggregation basis, scope, valid domain, owner, time basis and observation status. Distinguish stocks (`currency`, `persons`, `kWh stored`), rates (`currency/month`, `persons/month`, `kWh/month`) and dimensionless indices. A normalized index states its normalization and denominator.

Every edge declares:

1. the source and affected state components;
2. an explicit effect function or constraint, with typed inputs and output units;
3. any delay, conditional activation, saturation, substitution or interaction;
4. scope and validity conditions;
5. whether the relationship is an observed association, a causal hypothesis or a qualified causal claim;
6. supporting references, shared-source dependencies, alternative explanations and invalidators.

An association does not enter a causal transition equation as an established cause. A scenario may explore a hypothetical causal function, but its output retains that assumption. A hypothesized edge is represented through an appropriately qualified claim; the presence of the word `causes` never upgrades its epistemic standing.

Let `x_n` be the vector of represented states at step `n`, `u_n` an action schedule, `w_n` a declared outside disturbance, and `θ` the model parameters. Define:

`x_(n+1) = F_m(x_n, x_(n-1), …, x_(n-D), u_n, w_n; θ, Δt)`.

The initial history `x_(-D), …, x_0` is an input, not silently filled with zeros. In the explicit update above, every right-hand-side state value comes from the already known snapshot `x_n` or an earlier snapshot. Evaluate every component of `x_(n+1)` from those same frozen inputs, then commit the complete next state synchronously. A cycle in the domain graph, or a link with no additional lag beyond reading `x_n`, does not create a simultaneous algebraic problem. For example, `a_(n+1) = f(b_n)` and `b_(n+1) = g(a_n)` are ordinary explicit synchronous updates.

A different, implicit model arises only when a next-state component depends on other unknown next-state components, or when unknown instantaneous variables must satisfy mutually dependent constraints. Such a model must be declared separately, for example:

`R_m(z_n; x_n, x_(n-1), …, x_(n-D), u_n, w_n; θ, Δt) = 0`,

where `z_n = (x_(n+1), y_n)` comprises the unknown next state and any explicitly declared unknown instantaneous variables `y_n`. All supplied earlier/current states remain frozen inputs. The residual equations, units, domains and unknown components must be specified; this is not an implicit reinterpretation of the explicit `F_m` update.

A cyclic dependency among those same-step unknowns requires a separately supported, bounded simultaneous solver and qualified existence/uniqueness conditions over the declared domain, or a sound set-valued treatment retaining every relevant admissible solution. No solution, uncertain existence, unsupported multiplicity or exhaustion produces an explicit affected-model non-PASS/unknown result. A convenient solution branch or lexicographic update order must not silently choose the economics. If neither supported treatment is available, mark that implicit cyclic structure unsupported for this execution profile.

Functions may be nonlinear, piecewise or state-dependent, but every operation must preserve units, domain restrictions and declared uncertainty. Reachability, discrete policy changes and delays are represented explicitly. If finite-precision arithmetic is used operationally, freeze its method, rounding and error treatment; do not insert floats into canonical semantic structures that prohibit them.

For a genuine inventory stock `s`, a permitted balance is:

`s_(n+1) = s_n + Δt × (sum of admitted inflow rates − sum of admitted outflow rates)`.

Each term must have the same stock unit after multiplying by time. Production, consumption, destruction and external transfers appear as explicit sources or sinks. A negative inventory cannot be silently clipped to zero while pretending the original demand was fulfilled: the model records unmet demand, arrears, a permitted borrowing mechanism or a rejected transition as applicable.

Not every quantity is conserved. Prices, utility, legitimacy, knowledge and authority do not inherit an inventory law merely because they appear in a graph. Accounting identities, physical conservation and behavioral hypotheses are separate contracts.

### A4. Feedback must have a mechanism and a witness

The domain interaction graph may contain cycles: these represent hypothesized feedback in the world being modeled. It is distinct from SAL's CompletionFrontier, whose DAG records completion/derivation dependencies used by semantic search. A domain cycle does not authorize a cyclic completion dependency or break the completion algorithm's termination conditions. For the explicit synchronous update, an unrolled time-indexed computation remains acyclic even when the domain graph is cyclic and some effects read `x_n` without an additional lag: computed outputs belong to `x_(n+1)`. Cyclic dependencies among unknown next-state or instantaneous variables belong to the separately declared implicit model and follow the solver rule above.

A strongly connected component identifies a possible feedback structure in the declared graph. A cycle alone proves neither amplification nor real-world causation. Its operation depends on the edge functions, delays, saturation, external conditions and current state.

For each material candidate loop, retain a bounded witness containing the participating links, qualified causal assumptions, an initiating disturbance, the time span, the effect measure and the trajectory. Compare against an explicitly specified counterfactual in which the selected feedback mechanism is held at a declared reference response. This counterfactual is a model experiment; it is not automatically an identifiable real-world intervention.

Predeclare the classification criterion. For example, for a nonnegative normalized stress measure `q`, a selected interval can compare `q_feedback(n)` with `q_reference(n)` after the initiating pulse ends, subject to a declared tolerance. Report persistence, amplification, attenuation or a mixed result **over those steps**. A trajectory can amplify and then saturate. A positive loop sign or a gain product greater than one is not by itself a global instability proof for a delayed nonlinear model.

Where a qualified differentiable local analysis is available, its Jacobian or transfer analysis may supplement the trajectories. Its point of linearization, delay representation, validity region and stability assumptions remain explicit. It does not replace the bounded nonlinear cases or establish that the selected causal structure is true.

The unemployment–income–debt–consumption–revenue–automation loop and the research–technology–lower-cost-inputs–investment loop are **candidate mechanisms for testing**. Either may weaken, reverse, saturate or fail to operate under an alternative ownership arrangement, policy, adoption rate or external condition. Shared variables can couple the loops; do not add their results as if they were independent.

### A5. Recompute constraints as scarcity moves

At each relevant state, compare proposed activity against a declared feasible set. For a simple linear resource submodel, an illustrative constraint is:

`sum_a A_(j,a,n) × y_(a,n) ≤ c_(j,n)`.

Here `y_(a,n)` is an activity rate, `A_(j,a,n)` is resource `j` consumed per unit of activity, and `c_(j,n)` is available resource `j` per unit time. The units on both sides must match. More general models may use declared nonlinear constraints, discrete availability or time-dependent capacity.

Record which constraints are binding or close to a predeclared operational margin, which are uncertain, and which become limiting after a change. “Close” depends on an explicit tolerance. A sensitivity or dual value is reported only when its optimization problem and mathematical conditions justify it. It is not the social value of the resource.

Cheap cognition can be tested alongside different energy, hardware, robotics, logistics, material, ownership and access constraints. These are alternative scenarios, not a predicted universal bottleneck sequence. New knowledge may change a coefficient, substitute a resource or create a new activity; that invalidates the affected model/parameter binding and requires re-evaluation.

Permissions, rights and legitimate authority remain hard gates with their own semantics. They cannot be purchased by adding more compute, represented as ordinary consumable capacity, or relaxed because a production target has become binding.

### A6. Keep production, claims and access in separate accounts

The assessment must not infer household well-being from aggregate output alone. Keep at least the applicable distinctions among:

| Quantity | What it answers |
|---|---|
| Productive capacity and realized physical output | What can be made, and what is actually made? |
| Ownership and distribution rights | Who is entitled to output, income or control, under which rules? |
| Liquid balances and income flows | Who can pay now, and when does income arrive? |
| Liabilities and dated payments | What is owed, by whom, in which unit, and when is it due? |
| Essential-service availability and access | Does a service exist, and can the affected person actually obtain it? |
| Price and purchasing power | What can the person's resources obtain under the scenario? |

For cohort `h`, an illustrative cash-flow schedule is:

`cash_(h,n+1) = cash_(h,n) + Δt × (wages + distributed_income + transfers − taxes − essential_spending − other_spending − cash_debt_service)`.

All rates use the same declared currency and time unit after explicit conversions. Aggregate and per-person units must not be mixed. Principal, accrued interest, arrears and cash paid require their own accounting distinctions; payment of a debt is not always identical to reduction of principal. Credits and debits of internal transfers must match the stated accounts, while any outside funding is explicit. Do not count both a transfer and the same distributed income twice.

Synthetic arithmetic example, **not a forecast**: a household starts a month with 10 currency units, receives 20, owes a payment of 30 and needs essentials costing 20. Available cash is 30 against required payments of 50: a 20-unit gap. A scenario with ample goods does not remove that dated cash gap by itself. A transfer arriving three months later does not pay this month's obligation. A proposed transfer policy also needs identified funding, authority and rights checks; the example does not authorize it.

Compare multiple bounded scenarios: employment recovery; partial job substitution with delayed retraining; broad cognitive automation; output gains with concentrated ownership; output gains with wider distribution; and adverse input shortages. Use no assumed inevitability for mass unemployment, replacement jobs, centralization or decentralization. Report group and tail outcomes as well as totals, at the privacy-preserving resolution justified for the decision. Cohort averages can conceal a materially exposed subgroup.

### A7. Uncertainty and decision results

Separate observation uncertainty, parameter uncertainty, competing causal structures, scenario uncertainty and computation error. Shared data or assumptions create dependence; duplicate model outputs do not manufacture independent support.

A finite parameter grid establishes results only at its evaluated points. Interval or set-wide claims require a sound enclosing method or an appropriate proof that covers the declared set, including dependence and numeric error. An arbitrary range is a scenario assumption, not a calibrated confidence interval. If bounds cannot be justified, report their conditional status and the open uncertainty rather than converting them into a probability.

The existing `FutureStressAssessment` outcomes remain scoped: `SURVIVES_DECLARED_SCENARIO`, `FAILS_DECLARED_SCENARIO`, `INCONCLUSIVE` or `UNKNOWN`. A successful execution of the model is not a successful safety outcome. Preserve independent logical, epistemic, authority, scope, dependency and resource assessments; do not average them into one confidence score. Effect direction (beneficial, adverse, mixed or unknown under a declared measure) is also independent of epistemic standing: an adverse prediction can be well supported, and a beneficial prediction can be unsupported. A reinforcing feedback sign is not a moral or safety classification.

A known applicable hard-obligation violation cannot be compensated for by aggregate growth. Material unresolved links, stale observations, excluded groups, an insufficient horizon, unsupported parameter bounds or exhausted search can prevent a consequential conclusion. They do not automatically freeze unrelated work: the applicable owner routes the affected action under its existing deny, condition, limit, preserve or escalate semantics. This profile grants no emergency exception and no new authority.

### A8. Three exact arithmetic fixtures

These fixtures are deliberately small and synthetic. They are complete enough to calculate independently by hand. The stated expected results are mathematical consequences of the stipulated inputs, not measured economic behavior, estimates of a real coefficient or a claim of executed Garden conformance. All quantities use exact integers or rationals.

#### Fixture A — output doubles while this month's household payment fails

Scope: one modeled household and an explicit external production/employer boundary; one step of `Δt = 1 month`; no interest, taxes, borrowing, transfers or other spending. Two scenarios share opening household cash `C_0 = 10 currency units`, essential demand `d = 20 goods units/month`, fixed price `p = 1 currency unit/goods unit`, and a debt payment due this month `D = 30 currency units`. The price and external wage payment are scenario inputs, not outputs inferred from production. Essential goods are allocated to this household first; no supply shortage exists in either scenario.

Baseline: production rate `Q = 100 goods units/month`, wage rate `W = 50 currency units/month`. Automation scenario: `Q = 200 goods units/month`, `W = 20 currency units/month`. Production labor input is stipulated as the same `1 labor-month` during the step in both scenarios, so output per labor-month doubles within this toy example. The household wage reduction is a separate stipulated distribution change; it does not follow mathematically from the output increase. Incoming household wages are an external-account outflow, so this is not a closed-economy money model.

The fixture specifies **essentials paid first, then the due debt payment** solely to make accounting deterministic. It does not claim this payment priority is a generally authorized policy.

`available = C_0 + W × Δt`

`essential_cost = p × d × Δt = 20 currency units`

`debt_paid = min(D, max(0, available − essential_cost))`

`unpaid_due = D − debt_paid`

`C_1 = available − essential_cost − debt_paid`

| Scenario | Produced goods in month | Available cash | Essentials paid | Debt paid | Unpaid due | Closing cash |
|---|---:|---:|---:|---:|---:|---:|
| Baseline | 100 | 60 | 20 | 30 | 0 | 10 |
| Automation/distribution change | 200 | 30 | 20 | 10 | 20 | 0 |

All monetary columns use currency units. Expected distinction: output per stipulated labor input increases, but the household has a 20-unit unpaid obligation. An unreceived future transfer cannot be entered in this month's available cash. The example intentionally makes no economy-wide employment claim.

#### Fixture B — the limiting resource moves twice

Scope: one production activity evaluated at three monthly snapshots; `Δt = 1 month`; no inventory carryover, capacity building delay, minimum batch, fixed cost or substitute technology. Each completed job requires `2 compute-hours/job`, `1 kWh/job` and one delivery slot. All resources below are available rates during that snapshot. Production is maximized within the three constraints; actions changing capacity are stipulated scenario inputs, not authorized investment recommendations.

`q_n = min(C_n / 2, E_n / 1, L_n)` jobs/month,

where `C` has units compute-hours/month, `E` has units kWh/month, and `L` has units jobs/month. Expected monthly completions are `q_n × Δt`.

| Snapshot | Compute capacity C | Energy capacity E | Delivery capacity L | Compute ceiling | Energy ceiling | Jobs completed | Binding resource |
|---|---:|---:|---:|---:|---:|---:|---|
| 0 | 100 | 70 | 90 | 50 jobs/month | 70 jobs/month | 50 | Compute |
| 1: more compute | 200 | 70 | 90 | 100 jobs/month | 70 jobs/month | 70 | Energy |
| 2: more energy | 200 | 110 | 90 | 100 jobs/month | 110 jobs/month | 90 | Delivery |

Compute consumption is respectively 100, 140 and 180 compute-hours; energy consumption is 50, 70 and 90 kWh; delivery use is 50, 70 and 90 jobs. All are within the corresponding monthly capacities. Expected distinction: applying the original “compute is limiting” conclusion after snapshot 0 would be wrong. No claim is made that the world's bottlenecks follow this order.

#### Fixture C — delayed feedback changes the trajectory

Scope: two dimensionless synthetic stress indices `a` and `b`, valid on `[0, 2]`, over six one-month steps. No outside forcing occurs after the initial state. Use synchronous updates, exact rational arithmetic and the initial history `a_0 = 1`, `b_0 = 0`, `b_(-1) = 0`:

`a_(n+1) = (1/2) × a_n + g × b_(n-1)`

`b_(n+1) = a_n`.

The multiplier `g` is dimensionless. Three alternatives are `g = 0` (feedback edge cut), `g = 1/4` (weaker feedback) and `g = 1` (stronger feedback). All initial values, dynamics and delays otherwise match. No state leaves its stipulated valid interval within the six steps.

| Step n | a, edge cut g=0 | a, weaker feedback g=1/4 | a, stronger feedback g=1 |
|---|---:|---:|---:|
| 0 | 1 | 1 | 1 |
| 1 | 1/2 | 1/2 | 1/2 |
| 2 | 1/4 | 1/4 | 1/4 |
| 3 | 1/8 | 3/8 | 9/8 |
| 4 | 1/16 | 5/16 | 17/16 |
| 5 | 1/32 | 7/32 | 25/32 |
| 6 | 1/64 | 13/64 | 97/64 |

For every run, `b_(n+1) = a_n` supplies the remaining outputs. Example hand check: in the strong case, `a_3 = (1/2)(1/4) + 1 = 9/8`; `a_6 = (1/2)(25/32) + 9/8 = 97/64`.

Expected distinctions: the first two steps conceal the feedback difference; at step 6 the weaker run remains below its initial stress while above the cut-edge run, and the stronger run exceeds its initial stress. These are finite trajectory comparisons. They neither demonstrate societal collapse nor justify continuing a model after a later state leaves its declared domain. Neither of the positive-feedback runs is required to increase monotonically.

### A9. Finite checks and adversarial cases

The following are proposed acceptance cases, not executed tests or registered Garden test IDs. Each implementation must bind inputs, expected behavior, owner, scope and actual result before claiming conformance.

| Local case | Adversarial construction | Required behavior |
|---|---|---|
| T01 — Units | Add a monthly rate directly to a stock; combine currencies without conversion. | Reject the typed update; identify the incompatible terms. |
| T02 — Missing history | A delayed income effect reads an undeclared pre-start state. | Return unresolved/invalid-model detail; do not assume zero history. |
| T03 — Delayed harm | Benefits appear before the horizon; a known debt deadline falls just after it. | Mark the boundary unresolved or extend the authorized assessment; no unqualified safe result. |
| T04 — Spurious causal loop | Correlated observations and repeated reports share one underlying source. | Preserve association/hypothesis status and dependence; no causal or independence promotion. |
| T05 — Saturating feedback | A candidate loop amplifies initially but saturates; a cut-loop run attenuates. | Report the finite witness and saturation; do not infer unbounded collapse. |
| T06 — Counteracting loops | Cost reduction helps essential access while job loss reduces income in another group. | Retain both pathways and group outcomes; aggregate benefit cannot erase the adverse exposure. |
| T07 — Moving constraint | Relax compute capacity until energy or delivery becomes limiting. | Recompute the feasible set and binding constraints; do not reuse the old expansion recommendation. |
| T08 — Production without liquidity | Ample goods coexist with the synthetic 20-unit cash gap above. | Record access/payment shortfall distinctly from supply; a late benefit does not satisfy an earlier obligation. |
| T09 — Accounting duplication | Two policy paths spend the same funding; principal and cash payment are conflated. | Detect inconsistent accounts or an infeasible schedule; no invented resources. |
| T10 — Uncertainty coverage | Sample endpoints pass but an interior parameter value violates an obligation. | A point sample claim stays point-scoped; set-wide conformance requires a sound covering argument. |
| T11 — Missing population | A cohort average passes while a known subgroup loses essential access. | Surface the material subgroup or mark missing resolution; no blanket population claim. |
| T12 — Model disagreement | Two admissible causal structures reverse an intervention's effect. | Preserve disagreement and affected obligations; no majority-vote truth or automatic authorization. |
| T13 — Solver and domain failure | A discontinuity breaks the solver, or a state leaves the valid domain. | Stop the affected inference with a model/numeric failure; do not silently clip or continue. |
| T14 — Budget exhaustion | The run ends before required scenario/time/group cases complete. | Report exactly what was examined and remains unexplored; no closure or fixed-point claim. |
| T15 — Unauthorized success | An intervention improves every modeled economic measure but exceeds authority. | Keep the authority gate non-PASS independently of the simulation result. |
| T16 — Stale mechanism | New ownership rules, a resource substitute or changed employment response invalidates an edge. | Invalidate dependent conclusions and rerun the affected scope under current bindings. |

The initial acceptance gate is finite: structural and unit checks; the declared cases above; a bounded scenario comparison; explicit unexplored cases; owner review of the exact bindings; and no known material omission hidden as conformance. Empirical deployment qualification is an additional step, not supplied by these synthetic cases.

### A10. GCSC integration without inflated coverage

Use this candidate to define a bounded family of **situations**: delayed effect across owners, repeated interacting actions, a feedback loop, a changing resource dependency, a distribution constraint, or a stale causal assumption. Bind those situations through existing signatures and qualifiers; SAL still determines whether a concrete representation is admissible.

Freeze a separate measurement scope before enumerating combinations: admitted node/edge types, temporal partitions, interaction witnesses, materiality, uncertainty classes, owner boundaries, scenario limits and property oracles. A scenario output must not choose its own materiality rule. Composition retains rights, uncertainty, dependence and no-authority-amplification. Missing representation is a gap or unresolved case, not semantic inadmissibility merely because the current catalogue cannot express it.

The local cases can seed candidate test and proof obligations through the existing compiler process. Generated artifacts remain candidates until the existing source owner and admission process accept them. Scenario enumeration, cycle detection, syntactic coverage, numerical execution and proved set-wide properties are different results and need different receipts. No count in this proposal changes the previously reported GCSC denominators or proves exhaustive socioeconomic coverage.

### A11. Admission boundary and smallest useful implementation

A first useful implementation can be a small deterministic reference model: several named cohorts, a few production/resource nodes, explicit liabilities, two opposed feedback mechanisms, finite delays and a finite scenario set. Freeze the inputs; execute the local acceptance cases; expose tables of group outcomes and violated/unknown obligations; then test whether this changes a real decision compared with the existing assessment workflow.

Before adoption, resolve concrete profile bindings and owner responsibilities, evaluate numeric behavior, and obtain the applicable acceptance. If the existing contracts already implement a requested behavior, add a conformance case and documentation instead of a duplicate schema. If the model cannot distinguish two decision alternatives with the available information, record that result; an elaborate diagram is not decision value.

**Not established by this candidate:** the date of an AGI transition; employment elasticities; causal coefficients; a universal economic attractor; calibrated real-world probabilities; the correctness of an ownership/distribution policy; or the power to authorize that policy. The useful claim is narrower: Garden can require explicit, bounded analysis of these mechanisms before treating a local improvement as an adequate account of its material effects.

### Profile A source bindings

The compatibility references below ground reuse; they are not a proof that this new profile is already implemented.

- `rec_eeab3707f9b8862789b8`: Human-Effect Closure explicitly includes latent, cumulative, emergent and institutional effects and rejects treating missing materiality evidence as non-material.
- `rec_6e10d0cc95db2ebdf8aa`, `rec_9620599e03617eaa50ef`: cross-subsystem `CausalClosureReceipt/v1`, owners, unresolved obligations and enforcement split.
- `rec_7eae84f778dd5536ea6c`: P024 causal semantic ownership; no duplicate truth system; lawful erasure and dependent invalidation.
- `rec_54737b09a89b95f8ff46`, `rec_75c1e1047f06ed7f9724`: bottleneck-first rule and CRA-014.
- `rec_6cda9bdb3724745db201`, `rec_5c1facf5e21ca2fd2032`: quantity/model/timing and uncertainty foundations; registry membership is not empirical validation.
- `rec_f44bbd981a955ec7dddc`, `rec_1bee8e332952658aca7a`, `rec_8686a2e432901834148b`: existing bounded future-scenario and stress-assessment contracts; no universal survival certificate.
- Current metamodel chapter: seven Forms, Profile and DynamicalSystemProfile macros, independent applicability axes and source-owner precedence.


## Profile B — Responsibility through organizational change

### B1. Scope, duties and existing owners

#### Scope

Apply this candidate check when an organizational or workflow change removes, merges, replaces or substantially weakens a role that participates in a consequential decision, its execution, its monitoring, its correction or its appeal. AI substitution is one trigger; outsourcing, reorganization and delegation can produce the same defect.

Responsibility here means a declared, actionable duty within the system. It does not predetermine criminal guilt, civil liability, moral blame or legal personhood. Those require the relevant facts, law, authority and process. Retaining a named operational role is necessary for this check but does not itself establish legitimate authority or substantive oversight.

#### Proposed condition

Before the changed workflow becomes consequential, every applicable decision, execution, oversight, correction and appeal duty must have a valid continuing allocation or a valid accepted handover. Shared duties can have multiple explicit holders; the system must show their respective scopes and how disagreements or omissions are handled. “The AI,” “the committee,” an empty role, a departed employee or an institution without a functioning representative cannot silently satisfy an allocation that requires an operative accountable principal.

The check binds the proposed change to the governing authority, current permission and consent conditions, protected interests, applicable jurisdiction, existing commitments, relevant independent review requirements and recovery arrangements. It reuses the existing owners and records. The evidence required is proportionate to the duty: a trivial scheduling change does not require the same review as allocating coercive powers or removing a medical safety check.

An accepted transfer must not enlarge the transferred authority, erase existing commitments, extinguish an affected person's rights or create permission to disclose private information. A change in internal role assignments does not by itself transfer legal responsibility. Where allocation or competent acceptance is unresolved, preserve that unresolved state and use the existing block, escalation or safe-continuity path appropriate to the effect. Do not invent a lawful successor. Do not assume that unconditional shutdown is always the safest continuity response.

At the point of effect, check the current authorization and material conditions again through Garden's existing authorization/revocation mechanism. A record of yesterday's consent is not present consent. A durable audit history must coexist with privacy minimization and valid revocation or erasure duties.

#### Existing owner bindings to investigate and reuse

These are functional bindings supported by the inspected architecture material, not a declaration that every proposed check is already implemented.

| Concern | Existing owner or contract family | Required application |
|---|---|---|
| Legitimate decision role and delegation | Capability.Authority.Governance; Capability.Authority.Law; HumanCore.DelegatedAgent; existing authority contracts | Identify the competent decision authority, delegation limits, jurisdiction and acceptance of any transfer. |
| Protected limits and personal choice | HumanCore.Constitution; Privacy and HSA consent/revocation duties | A vote, founder instruction or administrative change cannot provide another person's missing consent or weaken protected rights. |
| Retained account of the decision | Capability.Knowledge; AUD-001, AUD-002, AUD-010, AUD-011 | Preserve the basis, decision, dissent and relevant actions without indiscriminate surveillance or permanent raw-data retention. |
| Review, independence and explanation | Engine.Proof; Engine.Compliance; Engine.Explanation; AUD-005, AUD-013 | Supply the required review, expose conflicts and provide usable correction and appeal paths. A receipt alone is not truth. |
| Consequential execution | Capability.Compute.Runtime; Capability.Compute.Execution; Capability.Trust.Safety | Bind current authorization to the effect, enforce restrictions and run the appropriate block or continuity response. |
| Unfinished commitments and handover | Existing lifecycle, Transition and continuity contracts; CLIC-013..016 as candidate reinforcement | Preserve commitments and disputes across reorganization; require valid acceptance before claiming an obligation has moved. |

#### Minimum observable result

Use existing records to answer these questions for the changed workflow:

1. What decision or effect is being authorized, and within what bounds?
2. Which principal holds each applicable duty before and after the change?
3. What existing instrument permits the allocation or transfer, and who accepted it?
4. Which commitments, rights, consent conditions, review requirements and appeal paths must survive?
5. Can the relevant reviewers actually inspect the necessary material, challenge the recommendation and cause the authorized stop, correction or escalation?
6. What invalidates the decision, including withdrawal of consent, changed authority, new material information or changed jurisdiction?
7. Who observes the consequences and handles unresolved commitments after the change?

These questions are a proposed application checklist, not seven new schema fields required everywhere. Where the baseline already supplies an equivalent binding, reuse it. Where the binding is absent, state the gap rather than manufacture a successful answer.

### B2. Finite mapping procedure and positive fixtures

This supplement defines a local candidate-check procedure, not a new canonical schema or identifier family. Responsibility is a set of scoped duties and relationships, not a conserved scalar. A legitimate change may split, merge, add or release duties, but each change needs its own valid basis. An operational allocation does not determine legal culpability.

#### Frozen inputs

Before running the check, freeze a finite assessment package containing:

- The proposed organizational change, before/after workflow boundaries, consequential effect classes, assessment time and applicable design/context versions.
- The complete declared inventory of before-change duties and the independently derived inventory of duties applicable to the after-change effects. Each duty binds an existing governing contract, scope, applicability conditions and current validity basis. Do not derive the required inventory by looking only at duties the new organization already satisfies.
- A finite mapping between the two inventories, including new duties, unchanged duties, accepted transfers, splits, merges and claimed releases. Each entry identifies current and proposed holders, scope, relevant acceptance, effective time and supporting records.
- The existing authority, consent, jurisdiction, review, independence, appeal, monitoring and continuity requirements that apply to the declared workflow, together with their evidence and invalidators.
- An explicit list of excluded or unresolved areas and their justification. Also freeze the resource budget and the review/appeal capacity criteria applicable to this risk class. Capacity criteria must come from the governing owner or a separately accepted scoped assessment; the checker must not invent convenient thresholds after seeing the result.

“Complete” in this procedure means complete against these declared finite inventories and the cited governing obligations. It does not mean every possible future consequence has been discovered. If the applicable governing requirements or effect boundary cannot be resolved, report that separately as an unresolved model boundary.

#### Deterministic traversal and owner-qualified checks

1. Validate the input inventory identities, references, versions and declared scope. Reject broken references, duplicate entries that pretend to be distinct duties and silent omissions from the supplied inventories. Preserve explicit unresolved applicability rather than dropping its entry.
2. Traverse every before-duty in a fixed order. Require a recorded continuing allocation, accepted transfer, explicitly described split/merge, evidenced fulfillment, or valid release. A proposed release must pass its own governing conditions; eliminating a department is not a release. Several entries referring to the same fulfilled commitment must not create duplicate performance.
3. Traverse every after-duty in the same fixed way. Require the operative holder or explicitly scoped shared holders, current acceptance where required, and a governing basis. Duties newly required by the changed effects must appear even if there is no predecessor duty. Where holders share work, verify the boundaries, coordination and escalation arrangement against the governing contract.
4. Evaluate duty validity and transfer/release validity under the referenced owners. Evaluate decision authority, delegation and current consent separately. A holder can be identifiable and capable while lacking authority; an authorized role can still lack an accepted or valid allocation.
5. Evaluate practical review capacity separately from practical appeal capacity. Use the frozen criteria and evidence for access to the relevant material, competent staffing or service capability, conflict/independence requirements, expected workload, response limits and the operative challenge, correction or escalation path. A role title or signature alone is insufficient. A review duty marked inapplicable requires a valid applicability determination, not an empty field.
6. Check decision-to-effect timing and invalidators. Current authority/consent and other volatile prerequisites must be rebound at the consequential effect through the existing execution gate. Record unresolved commitments and the existing authorized continuity response for failed or stale prerequisites.
7. Return the independent diagnostics and every uncovered, failed, stale or deferred item. If the resource budget is exhausted, retain the unexamined inventory entries as deferred. Do not convert incomplete traversal into a valid mapping result.

The inventory traversal can be deterministic while a referenced assessment still returns unresolved: a script can detect a missing acceptance reference, but it cannot establish the legal validity of a contested transfer simply by finding a string in a file.

#### Exact local result shape

The following is an illustrative local checker output contract for this candidate review. Its keys and labels are local notation, not additions to Garden's canonical vocabulary. Each diagnostic uses `SATISFIED`, `VIOLATED`, `UNRESOLVED` or `NOT_APPLICABLE`; `NOT_APPLICABLE` requires an explicit governing basis. `SATISFIED` is limited to the stated scope and validity period.

```json
{
  "assessment_scope_ref": "existing scoped assessment reference",
  "input_commitment": "hash of the frozen finite assessment package",
  "inventory_counts": {"before": 0, "after": 0, "mapped_before": 0, "bound_after": 0},
  "diagnostics": {
    "model_boundary_and_applicability": {"status": "UNRESOLVED", "basis_refs": [], "findings": []},
    "binding_completeness": {"status": "UNRESOLVED", "basis_refs": [], "findings": []},
    "duty_and_handover_validity": {"status": "UNRESOLVED", "basis_refs": [], "findings": []},
    "authority_and_current_consent": {"status": "UNRESOLVED", "basis_refs": [], "findings": []},
    "practical_review_capacity": {"status": "UNRESOLVED", "basis_refs": [], "findings": []},
    "practical_appeal_capacity": {"status": "UNRESOLVED", "basis_refs": [], "findings": []}
  },
  "uncovered_before_duty_refs": [],
  "unbound_after_duty_refs": [],
  "deferred_item_refs": [],
  "invalidator_refs": [],
  "effect_recheck_required": true,
  "local_disposition": "UNRESOLVED",
  "existing_gate_and_continuity_refs": []
}
```

Each finding names the affected duty or effect, the failed or unresolved condition, and its basis. Counts are navigation aids; equal counts cannot establish preserved meaning. Valid splits and merges can change the counts. Empty inventories require a supported applicability finding and cannot be used to certify an unspecified workflow.

Compute the local disposition without discarding individual diagnostics:

- Any applicable `VIOLATED` result yields `BLOCKED` for the proposed consequential change, while retaining all unresolved findings.
- Otherwise, any applicable `UNRESOLVED` result, any deferred item, or any uncovered/unbound required duty yields `UNRESOLVED`.
- Otherwise return `CLEARED_WITHIN_SCOPE`, subject to the referenced existing admission gates and effect-time recheck. This local clearance supplies no new authority and is not a general safety or legality certificate.

Practical review and appeal remain distinct: adequate operational supervision does not prove that affected people can challenge a decision. A valid after-duty allocation also cannot repair an unresolved model boundary by itself.

#### Two positive fixtures

These fixtures specify expected outputs; they have not been executed against an implementation.

| Fixture | Frozen conditions | Expected result |
|---|---|---|
| Accepted lawful reorganization | A permitted service reorganization merges two scheduling teams. The finite inventory covers booking authorization, privacy handling, error correction, open commitments, supervisory review and customer appeal. Operative successor roles accept the applicable duties; prior commitments and restricted data access remain intact. The governing authority accepts the change. Any duty consolidation has explicit scope and no silently erased obligation. The retained review and appeal services meet their independently set access, staffing and response criteria; rights and current consent conditions are unchanged and rechecked as required. | All six independent diagnostics are `SATISFIED`; every before-duty has a valid disposition and every after-duty has a valid holder. No deferred items. `CLEARED_WITHIN_SCOPE`, followed by existing admission/effect gates. Fewer roles and different duty counts are permitted because the actual obligations and their valid dispositions were checked. |
| Lawful bounded automation without per-item human review | In a synthetic domain that permits it, a competent authority authorizes an automated policy for reversible appointment reminders within explicit recipient, consent, rate, content and duration bounds. No applicable contract requires a person to approve every message. Policy ownership, monitoring, revocation, exception handling, error correction and customer appeal have accepted operative holders. Independent review, where required, evaluates the bounded policy and its changes. The service demonstrates required workload and response capacity; current consent is bound before each effect. Out-of-bound cases follow the existing escalation or block path. | All six diagnostics are `SATISFIED` for the bounded workflow. The absence of per-item approval is not a failure because no such duty applies; the applicable policy-review and appeal duties remain tested. `CLEARED_WITHIN_SCOPE`, subject to the same existing gates and rechecks. A scope expansion, expired authorization, withdrawn consent or changed governing requirement invalidates the affected clearance. |

### B3. Adversarial acceptance cases

The cases below are test specifications. They have not been executed against a Garden implementation.

| Case | Failure to expose | Expected behavior |
|---|---|---|
| Human rubber stamp | A person approves thousands of high-consequence recommendations without the information, time or power required by their assigned review duty. | A signature is insufficient. Check the applicable review contract and actual ability to inspect, challenge and intervene. Do not impose per-item human review where a competent authority has lawfully approved a bounded automated policy and the domain permits it. |
| Small committee centralizes power | Removing many layers gives three people control over information, policy, execution and appeals. | Assess authority concentration, conflicts, required independence and contestability under existing governance duties. Fewer layers are neither proof of decentralization nor proof of illegitimacy. |
| Majority violates rights | A majority votes to release a minority's private records or authorize an irreversible personal change. | The voting result cannot supply missing individual consent or defeat applicable protected limits. Preserve dissent and the applicable appeal path. |
| Consent changes during execution | A patient withdraws permission after approval but before a scheduled consequential act. | Invalidate the stale permission at the effect boundary; apply the authorized cancellation, safe-continuity or other applicable lawful process. Preserve effects that already happened accurately. |
| Nobody owns the decision | A department is dissolved; its automated process continues under “organization responsibility.” | Do not claim an accepted handover. Preserve the unresolved obligation, identify the competent escalation path and prevent unauthorized consequential continuation. |
| Retrospective AI blame | The operator approved the scope, suppressed warnings and later says the model was responsible. | Retain attributable acts, decision authority, warnings and overrides. Establish any legal liability separately through due process; do not automatically exonerate or condemn the operator. |
| Competing laws or readings | A system chooses the most convenient jurisdiction or treats solver success as resolution of a legal dispute. | Preserve jurisdiction, applicability, competing readings and unresolved authority. Apply LEGAL-FORM behavior; a formal result cannot create law or select the only legally competent interpretation. |
| Nominal appeal | The same committee that made the decision controls all records and can silently dismiss every appeal. | Check the appeal and independence duties actually applicable; surface conflicts and missing access. Renaming the committee's internal retry procedure “appeal” does not establish compliance. |
| Organizational successor disappears | The intended new contractor refuses the handover or ceases operating. | A proposed transfer is not accepted responsibility. Preserve the predecessor's continuing duties where valid; otherwise retain the unresolved state and escalate without inventing a new owner. |
| Oversight without resources | The organization retains an appeal officer but removes their staff, access and intervention channel. | Verify that the retained duty remains practically performable. A role title alone cannot certify continuity of the function. |

## Existing epistemic and governance checks reused by both profiles

The anomaly → hypothesis → investigation → finding sequence is a teaching aid, not a mandatory chronological status machine. Preserve observation, report, inference, causal assumption, disputed claim and established finding separately. New information can weaken or reverse a claim. A dependent repetition or model-generated account is not independent corroboration. Investigating a possibility, naming an actor and imposing a consequence each require their applicable basis and authority; no confidence score supplies those permissions by itself.

The judicial example exercises existing law and epistemic contracts. An excellent analysis does not create a right to imprison, seize assets or otherwise impose consequences. Community voting and founder participation remain bounded by the applicable rights, consent, jurisdiction, independence and appeal duties. This is an architecture example, not advice on any jurisdiction's present law.

For organizational records, retain accountability in ways compatible with the governing privacy and lawful-erasure requirements. Keeping forbidden raw data is not justified by calling it an audit trail. Where authorized erasure removes a necessary basis, preserve permissible commitments or summaries and invalidate dependent claims as required; do not pretend the original basis remains available.

## Integration and readiness record

1. Map the exact target fields, owners, governing requirements and statuses. A profile name alone is not an admitted executable schema.
2. Freeze finite domain tables, model scopes, units, scenario inputs, uncertainty treatment, materiality, comparators, authority bindings and resource limits under the existing independent qualification path. No proposer-selected pass criteria.
3. Implement and run the applicable positive and negative acceptance cases, including unknown inputs, stale bindings, delayed effects, unauthorized beneficial outcomes and legitimate improvements. Arithmetic fixture checks alone cannot establish this gate.
4. Resolve each real empirical parameter and causal claim to adequate domain support or retain its conditional status. Show decision value against the existing assessment method; do not accept complexity as a substitute for usefulness.
5. Preserve continuing authority, practical enforcement, revocation, monitoring and recovery requirements at the effect boundary. A document rule is not proof that a safeguard works.
6. Reconcile the accepted changes through the existing owner/admission process, then update explanatory material and catalogue bindings consistently. Research, hypotheses, metaphors and humor retain their distinct roles.

No new GCSC coverage denominator, fixed point, proof result, module-suite pass or deployment qualification follows from this candidate. Its local T01–T16 cases and organizational cases are proposed test specifications. The three toy fixtures support arithmetic verification only. The package's final review record reports exactly what was checked and any remaining work.