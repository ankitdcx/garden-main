# GARDEN v15.10 — COMPLETE SCIENTIFIC RESEARCH REGISTER — 2026-10-09

Status: NONCANONICAL RESEARCH; NOT 100 verified discoveries. This consolidated file contains all scientific proposal registers and evidence summaries produced today. It preserves the source sections below as historical records, including older claims corrected by later addenda. **When statements conflict, the latest explicit correction and evidence boundary controls.** The source text is not itself an admitted Garden design update.

## Contents
1. 100 candidate scientific theory upgrades — REV3 and its corrections
2. Candidate 026 synthetic benchmark gap closure
3. Five domain investigations and sixteen transfers
4. Consolidated 33 high-value opportunity investigations

## Evidence and corrections
- No novel scientific law has been independently established. Worldwide novelty screening, real-world validation and comprehensive 100-theory derivations remain pending.
- REV3 states that the 100 mechanisms were keyword-derived hints, not actual residual-based diagnoses.
- Candidate 026 thermal memory is established physics; benchmark evidence tests a modelling procedure, not discovery of new physics.
- Dollar figures supplied as total industry losses or theoretical opportunity must not be counted as Garden-specific incremental savings.
- The full scientific text is unified here. **Executable source code and machine-readable results remain separate supporting assets** because merging them as prose would make them less usable.
- Garden's canonical Book, Technical Core and Catalogue remain unchanged.

## Supporting reproducible assets
- `garden_candidate026_harness.py`
- `garden_candidate026_harness_results.json`
- `garden_candidate026_strong_comparator.py`
- `garden_candidate026_strong_results.json`
- `garden_candidate026_strong_results_high_noise.json`

## Original source identities
1. `Garden_v15_10_Scientific_Theory_Upgrades_100_REV3.txt` — Git blob 3caa7db98f118a22de20fb6749f2b79cefd8fea0
2. `GARDEN_SCIENCE_REV3_GAP_CLOSURE_2026-10-09.md` — Git blob 088c1c767175d01cbc1ee34c000f9bfa8d0e68d6
3. `GARDEN_SCIENCE_FIVE_DOMAINS_AND_16_TRANSFERS_2026-10-09.md` — Git blob 5710d99e091b7b80b421b3bad029a03197f7d8b6
4. `GARDEN_SCIENCE_HIGH_VALUE_OPPORTUNITIES_FINAL_2026-10-09.md` — Git blob d0dc9ffb56a81c0a70b2f2cc61a9d9872edc22cc

---


---
# PART 1: Garden_v15_10_Scientific_Theory_Upgrades_100_REV3.txt

REV3 EVIDENCE / CORRECTION ADDENDUM — controlling over earlier REV2 assertions

1. SOURCE AND EVIDENCE STATUS
The 100 records are proposed research questions, not 100 residual-derived mechanisms. The label classifier used keyword matches in candidate titles. Only ten have mathematical worked examples; none has a documented worldwide novelty search or real-world test. Candidate 026 has one reproducible synthetic benchmark, not a strong-baseline comparison.

2. CANDIDATE 026 SYNTHETIC EXECUTION
Simulation: C1=2, C2=4, interface h=0.9, environmental g=0.24; dt=0.25, training steps=320, test steps=160, observation noise sigma=0.012; 100 independent seeds per condition. One-body null: C=2, g=0.35. Comparison: ARX(1,1) versus ARX(2,2), fixed regularization. The more complex model is NOT assumed to represent a real hidden thermal state merely because it predicts better.
Uncalibrated 10% held-out improvement + training BIC gate: 99/100 false selections on null, 100/100 selections on hidden-state simulations. This exposed a serious errors-in-variables/model-selection failure.
Calibration: 100 independent one-body null simulations define the 95th-percentile held-out gain threshold = 0.3350; require also BIC improvement >=10. On distinct evaluation seeds: null false selections = 3/100; two-body selections = 94/100. Median held-out gain: null 0.2343; two-body 0.4268. These outcomes depend on chosen parameters/noise/forcing and cannot be generalized without sensitivity and stronger baseline tests.
Source: garden_candidate026_harness.py; output: garden_candidate026_harness_results.json. Exact script and results should be retained together.

3. CANDIDATE 026 THEORY EQUATION CONTRACT (EXECUTED MODEL)
Variables T1,T2 are temperature departures [K]; u is applied thermal power [W]; C1,C2 are heat capacities [J/K]; h,g are conductances [W/K]; t [s].
C1*dT1/dt = u - g*T1 - h*(T1-T2)
C2*dT2/dt = h*(T1-T2)
Domain: C1,C2>0, h,g>=0, bounded forcing; zero initial absolute-temperature interpretation is not assumed. For h>0 and g>0, the linear system is asymptotically stable. Energy balance: d(C1*T1+C2*T2)/dt = u - g*T1. In the limit h=0, T1 obeys the one-body model C1*dT1/dt=u-g*T1; this is a precise decoupling limit, not a generic claim that all single-body models are equivalent.
Identifiability: not proven for all observation schedules. Observation: noisy T1 only; u known. Derived hidden-state dynamics are established thermal RC mathematics. No new physical law is claimed.

4. LIMITS / FALSIFIERS / NEXT GATES
The current harness compares ARX1 and ARX2, NOT a noise-aware Kalman state-space baseline, nonlinear model, or modern system-identification package. A stronger comparison must control observation-noise bias and fit/compute budgets. Required: parameter sensitivity, multiple noise levels, calibrated null power, time-horizon holdouts, state-space comparator, code review, literature review, experimental preregistration. Synthetic selection is not physical discovery.
For the 100 cases, equation contracts remain incomplete except for the explicit candidate-026 model and illustrative examples. The source catalogue and TREE_CORE integrity issues remain separately UNVERIFIED; do not treat this appendix as fixing truncated gzip, stale schema IDs or source-retention defects.

5. TRIAGE / PRIORITY / INFRASTRUCTURE
Scores are provisional planning judgments (1=low,5=high), not estimated success probabilities.
Candidate 026 thermal memory: tractability 5, benefit 4, novelty likelihood 1 (established RC dynamics); infrastructure: heater, two thermometers, heat flux logger.
Candidate 002 electrolyte concentration variance: tractability 3, benefit 4, novelty likelihood 2; infrastructure: electrochemical cell and spatial concentration diagnostics.
Candidate 006 battery heat-current covariance: tractability 3, benefit 5, novelty likelihood 2; infrastructure: battery thermal imaging and local current diagnostics.
Candidate 017 parallel Arrhenius barriers: tractability 4, benefit 3, novelty likelihood 1 (established mixture kinetics); infrastructure: controlled-temperature reaction measurement.
Candidate 036 fatigue closure memory: tractability 3, benefit 5, novelty likelihood 1 (established load-sequence effects); infrastructure: cyclic load rig and crack monitoring.
Group 001–010 battery; 011–020 catalysis/kinetics; 021–025 nucleation; 026–030 heat transfer; 031–040 transport/fracture; 041–050 turbulence/solar; 051–100 remaining domain-specific rigs. Shared hardware is a planning idea, not confirmed feasibility.

6. CROSS-REFERENCE TO TREE_CORE
Each eventual admission candidate needs an atomic owner record (source span/hash, version, status), two-way source/graph retention, an equation contract, an independently checked derivation, a proof/simulation/empirical/novelty status vector, and no-self-admission. These are REQUIRED gates, not passed tests.

7. REVIEW ERRATA
The REV2 worked 017 derivation gives POSITIVE curvature d^2 ln(k)/d(1/T)^2 = Var_w(E)/R^2 >= 0. Any review describing negative curvature is incorrect. REV2 worked 041 conditions on a variable not necessarily available at prediction time; its Bayes-risk inequality is not an implementable turbulence-closure gain without forecasting that variable. The REV2 summary table's 'mechanism unresolved' entry for 017 conflicts with its worked derivation; the worked model is a known parallel-pathway mechanism, not a novel discovery. Other title hints require actual residual-based reclassification.

8. PENDING STATUS
Global literature novelty checks 0/100 completed; full domain-specific equation contracts 1/100 candidate (026 illustrative); worked examples 10/100; empirical validations 0/100; state-of-the-art baseline comparisons 0/100; TREE_CORE integrity repair not performed. NO GLOBAL NOVELTY OR REAL-WORLD IMPROVEMENT CLAIM.

--- ORIGINAL REGISTER WITH CORRECTED LABELS BELOW ---

GARDEN v15.10 — SCIENTIFIC THEORY UPGRADE REGISTER — REVISION 3
Date: 2026-10-09 | Status: RESEARCH CANDIDATE / NOT CANONICALLY ADMITTED
Scope: 100 candidate investigations across 20 families. This is NOT 100 discoveries.
REV3 correction: REV2 mechanisms were keyword/title hints, NOT residual-based diagnoses; the 100 records use repeated diagnostic templates. Ten worked examples are not ten novel laws. Candidate 026 now has an executed, null-calibrated synthetic harness.

A. PROJECTION-DRIVEN MECHANISM
1. Freeze each baseline with source/version, equations, units, state variables, domain and strongest available extensions.
2. Construct typed GSL situation graph: 10 core object kinds, applicable 24 relations, seven Design Forms; explicitly mark non-applicable objects/relations.
3. Define a PROJECTION from detailed physical state to baseline observables; identify two physically possible detailed states sharing the same projected state.
4. Compare their futures. If distinct, the projection is not closed under the stated dynamics. Record exact or empirical residual and its uncertainty.
5. Diagnose residuals: spatial covariance, network connectivity, hidden relaxation, switching, coupling, or UNKNOWN. Never assign mechanisms by record index.
6. Derive a minimal extension using dimensioned state variables and physically valid conservation/positivity/symmetry constraints; recover the baseline in a declared limit.
7. Attach TheoryEquationContract: equation, units, assumptions, validity domain, falsifiers, limits, numerical tolerances, identifiability and source evidence.
8. Attack with adversarial limiting cases and counterexamples; compare with strongest modern baseline at matched parameters, data, complexity and compute.
9. Use preregistered signed/magnitude predictions when derivable, held-out tests, power planning, multiplicity correction and explicit failure/UNKNOWN statuses.
10. Separate derivation, code, synthetic recovery, empirical fit, global novelty and utility. No candidate self-admits. Preserve source hashes and review receipts.

B. GARDEN v15.10 SEMANTIC CROSSWALK
10 Objects: TIME, SPACE, THING, EVENT, ACTION, AGENCY, RULE, VALUE, CONTEXT, CLAIM.
24 relations: identifies, causes, governs, values, frames, acts, obeys, assesses, contextualizes, controls, partOf, dependsOn, owns, delegates, references, derivedFrom, equivalentTo, contradicts, supports, blocks, hasHypothesis, supersedes, conflictsWith, originatesFrom.
7 Forms: CONSTRUCT, CONTRACT, STATE, RELATION, PROCESS, RULE, PROJECTION.
Facets: IdentityLifecycle; ScopeContext; EpistemicsProvenance; AuthorityHumanBoundary; EffectsSafety; DependencyValidity; ResourceTermination; PrivacyRetention; AuditExplanation; RecoveryEvolution.
Three-source boundary: Book explanatory; Technical mechanics; Catalogue domain semantics. Scientific findings are separate candidate records and do not overwrite controlling sources.
Only physically meaningful relations are instantiated. AGENCY, owns, delegates and authority effects are normally not attributes of molecules or physical fields.
The 'approximation/limit' edge is a proposed typed scientific extension, NOT a 25th core relation; it may be encoded as a qualified derivedFrom relationship plus explicit limit contract.
TREE_CORE dependency: exact owner/source span and content hash; two-way retention; fail-closed deterministic build, schema consistency, CRC/integrity verification. These gates remain unverified here.

C. SUMMARY TABLE
ID | Family | Upgrade question | Title-derived mechanism HINT (not verified) | Benefit if validated
001 | Battery electrochemistry | interfacial stress memory | dynamic hidden state / delay | safer fast charging
002 | Battery electrochemistry | electrolyte concentration variance | heterogeneity / joint distribution | safer fast charging
003 | Battery electrochemistry | particle-size/contact covariance | heterogeneity / joint distribution | safer fast charging
004 | Battery electrochemistry | thermal-gradient persistence | heterogeneity / joint distribution | safer fast charging
005 | Battery electrochemistry | SEI connectivity hysteresis | network / geometry | safer fast charging
006 | Battery degradation | local heat-current covariance | heterogeneity / joint distribution | longer battery lifetime
007 | Battery degradation | charge-rest sequencing | dynamic hidden state / delay | longer battery lifetime
008 | Battery degradation | fracture-assisted reaction area | network / geometry | longer battery lifetime
009 | Battery degradation | lithium inventory redistribution | dynamic hidden state / delay | longer battery lifetime
010 | Battery degradation | electrode pore-network fragmentation | network / geometry | longer battery lifetime
011 | Heterogeneous catalysis | surface reconstruction memory | dynamic hidden state / delay | lower-energy chemical manufacture
012 | Heterogeneous catalysis | adsorbate-neighbor correlations | heterogeneity / joint distribution | lower-energy chemical manufacture
013 | Heterogeneous catalysis | pulsed feed phase | state switching / hysteresis | lower-energy chemical manufacture
014 | Heterogeneous catalysis | active-site network percolation | network / geometry | lower-energy chemical manufacture
015 | Heterogeneous catalysis | poison desorption history | dynamic hidden state / delay | lower-energy chemical manufacture
016 | Chemical kinetics | competing-pathway occupancy | coupled latent kinetics | better reactor efficiency
017 | Chemical kinetics | barrier-distribution curvature | established parallel-pathway mixture; worked derivation | better reactor efficiency
018 | Chemical kinetics | solvent reorganization lag | dynamic hidden state / delay | better reactor efficiency
019 | Chemical kinetics | reactant clustering | network / geometry | better reactor efficiency
020 | Chemical kinetics | intermediate trapping memory | dynamic hidden state / delay | better reactor efficiency
021 | Nucleation | subcritical-cluster history | dynamic hidden state / delay | crystal and drug formulation
022 | Nucleation | surface-defect localization | mechanism unresolved — requires domain diagnostics | crystal and drug formulation
023 | Nucleation | solvent pulse memory | dynamic hidden state / delay | crystal and drug formulation
024 | Nucleation | impurity-cluster correlations | heterogeneity / joint distribution | crystal and drug formulation
025 | Nucleation | spatial supersaturation intermittency | heterogeneity / joint distribution | crystal and drug formulation
026 | Heat transfer | interface thermal memory | dynamic hidden state / delay | chip and battery cooling
027 | Heat transfer | anisotropic domain connectivity | network / geometry | chip and battery cooling
028 | Heat transfer | nonlocal hotspot coupling | coupled latent kinetics | chip and battery cooling
029 | Heat transfer | phase-transition latent-heat lag | state switching / hysteresis | chip and battery cooling
030 | Heat transfer | thermal-contact ageing | network / geometry | chip and battery cooling
031 | Fluid transport | pore-throat network damage | network / geometry | filtration and groundwater
032 | Fluid transport | wetting-front hysteresis | state switching / hysteresis | filtration and groundwater
033 | Fluid transport | particle clogging topology | network / geometry | filtration and groundwater
034 | Fluid transport | pressure-cycling memory | dynamic hidden state / delay | filtration and groundwater
035 | Fluid transport | multi-scale channel connectivity | network / geometry | filtration and groundwater
036 | Fracture mechanics | overload sequence memory | dynamic hidden state / delay | safer infrastructure
037 | Fracture mechanics | microcrack orientation correlations | heterogeneity / joint distribution | safer infrastructure
038 | Fracture mechanics | corrosion-fatigue coupling | coupled latent kinetics | safer infrastructure
039 | Fracture mechanics | grain-boundary connectivity | network / geometry | safer infrastructure
040 | Fracture mechanics | residual-stress redistribution | dynamic hidden state / delay | safer infrastructure
041 | Turbulence | intermittency-conditioned closure | heterogeneity / joint distribution | efficient transport and turbines
042 | Turbulence | wall-history dependence | dynamic hidden state / delay | efficient transport and turbines
043 | Turbulence | coherent-structure topology | network / geometry | efficient transport and turbines
044 | Turbulence | pressure-strain lag | dynamic hidden state / delay | efficient transport and turbines
045 | Turbulence | cross-scale transfer memory | dynamic hidden state / delay | efficient transport and turbines
046 | Solar cells | mobile-ion interface memory | dynamic hidden state / delay | longer-lasting solar modules
047 | Solar cells | trap-occupancy hysteresis | state switching / hysteresis | longer-lasting solar modules
048 | Solar cells | grain-boundary topology | network / geometry | longer-lasting solar modules
049 | Solar cells | humidity-illumination covariance | heterogeneity / joint distribution | longer-lasting solar modules
050 | Solar cells | contact ageing kinetics | network / geometry | longer-lasting solar modules
051 | Photosynthesis | dynamic disorder correlation | heterogeneity / joint distribution | artificial photosynthesis
052 | Photosynthesis | reaction-center occupancy feedback | coupled latent kinetics | artificial photosynthesis
053 | Photosynthesis | vibrational mode intermittency | heterogeneity / joint distribution | artificial photosynthesis
054 | Photosynthesis | antenna topology adaptation | network / geometry | artificial photosynthesis
055 | Photosynthesis | nonphotochemical quenching memory | dynamic hidden state / delay | artificial photosynthesis
056 | Neuroscience | phase-lag memory | state switching / hysteresis | better neural diagnostics
057 | Neuroscience | cell-type interaction topology | network / geometry | better neural diagnostics
058 | Neuroscience | adaptation-state retention | dynamic hidden state / delay | better neural diagnostics
059 | Neuroscience | dendritic compartment coupling | coupled latent kinetics | better neural diagnostics
060 | Neuroscience | glial metabolic feedback | coupled latent kinetics | better neural diagnostics
061 | Pharmacokinetics | transporter saturation history | dynamic hidden state / delay | precision dosing
062 | Pharmacokinetics | protein-binding displacement lag | dynamic hidden state / delay | precision dosing
063 | Pharmacokinetics | organ perfusion covariance | heterogeneity / joint distribution | precision dosing
064 | Pharmacokinetics | intracellular sequestration memory | dynamic hidden state / delay | precision dosing
065 | Pharmacokinetics | circadian clearance state | coupled latent kinetics | precision dosing
066 | Ecology | interaction-network rewiring | network / geometry | ecosystem resilience
067 | Ecology | seed-bank recovery memory | dynamic hidden state / delay | ecosystem resilience
068 | Ecology | spatial refuge connectivity | network / geometry | ecosystem resilience
069 | Ecology | predator-switching lag | state switching / hysteresis | ecosystem resilience
070 | Ecology | nutrient feedback delay | dynamic hidden state / delay | ecosystem resilience
071 | Epidemiology | contact-network memory | network / geometry | more accurate outbreak forecasts
072 | Epidemiology | infection-age infectiousness | mechanism unresolved — requires domain diagnostics | more accurate outbreak forecasts
073 | Epidemiology | regional mixing covariance | heterogeneity / joint distribution | more accurate outbreak forecasts
074 | Epidemiology | behavioral response lag | dynamic hidden state / delay | more accurate outbreak forecasts
075 | Epidemiology | immunity heterogeneity topology | heterogeneity / joint distribution | more accurate outbreak forecasts
076 | Soil biogeochemistry | mineral-accessibility topology | network / geometry | soil management and climate
077 | Soil biogeochemistry | wet-dry pulse memory | dynamic hidden state / delay | soil management and climate
078 | Soil biogeochemistry | microbial enzyme allocation | coupled latent kinetics | soil management and climate
079 | Soil biogeochemistry | aggregate fragmentation | network / geometry | soil management and climate
080 | Soil biogeochemistry | root-exudate spatial coupling | coupled latent kinetics | soil management and climate
081 | Climate dynamics | ocean vertical heat memory | dynamic hidden state / delay | better adaptation planning
082 | Climate dynamics | cloud-regime transition persistence | state switching / hysteresis | better adaptation planning
083 | Climate dynamics | land-moisture feedback | coupled latent kinetics | better adaptation planning
084 | Climate dynamics | aerosol-pattern covariance | heterogeneity / joint distribution | better adaptation planning
085 | Climate dynamics | ice-albedo spatial connectivity | network / geometry | better adaptation planning
086 | Materials mechanics | dislocation network topology | network / geometry | stronger lightweight materials
087 | Materials mechanics | grain-boundary slip memory | dynamic hidden state / delay | stronger lightweight materials
088 | Materials mechanics | strain-rate history | dynamic hidden state / delay | stronger lightweight materials
089 | Materials mechanics | phase-boundary stress covariance | heterogeneity / joint distribution | stronger lightweight materials
090 | Materials mechanics | defect-cluster intermittency | heterogeneity / joint distribution | stronger lightweight materials
091 | Protein kinetics | conformational-state memory | dynamic hidden state / delay | biomanufacturing
092 | Protein kinetics | substrate microdomain gradients | heterogeneity / joint distribution | biomanufacturing
093 | Protein kinetics | crowding-induced correlation | heterogeneity / joint distribution | biomanufacturing
094 | Protein kinetics | allosteric network topology | network / geometry | biomanufacturing
095 | Protein kinetics | product inhibition lag | dynamic hidden state / delay | biomanufacturing
096 | Optical materials | nano-inclusion spatial correlation | heterogeneity / joint distribution | sensors and photonics
097 | Optical materials | interface exciton coupling | coupled latent kinetics | sensors and photonics
098 | Optical materials | temperature-dependent disorder | heterogeneity / joint distribution | sensors and photonics
099 | Optical materials | nonlocal scattering memory | dynamic hidden state / delay | sensors and photonics
100 | Optical materials | defect-network percolation | network / geometry | sensors and photonics

D. TEN MATHEMATICAL WORKED EXAMPLES
WORKED 002 — Battery electrochemistry: electrolyte concentration variance
Model/assumptions: For local electrolyte concentration c(x), let i(x)=i0 exp(-a/c(x)) for c>0, a>0 (illustrative transport-limited constitutive law, not universal Butler–Volmer). Aggregate I=E[i(c)].
Derived result: Taylor expansion gives I-i(E[c]) = (1/2)i''(cbar)Var(c)+O(E|c-cbar|^3), with i''(c)=i(c)*a*(a-2c)/c^4. Thus the leading correction is POSITIVE if cbar<a/2 and NEGATIVE if cbar>a/2, for sufficiently small variance.
Discriminating experiment: Two otherwise matched cells with the same mean c but different measured concentration variance should show the predicted sign change when a/cbar crosses 2. Reject if sign fails after independent measurement of a and confound controls.
Standing: derivation under stated illustrative assumptions; global novelty not established; no real-world test performed.

WORKED 006 — Battery degradation: local heat-current covariance
Model/assumptions: Assume local degradation r(x)=k exp[-E/(R T(x))] j(x)^p, T>0, j>0, k>0, E>0; compare E[r] with r(E[T],E[j]).
Derived result: The second-order correction includes r_Tj Cov(T,j), where r_Tj=r*E*p/(R*T^2*j)>0 for p>0. Thus POSITIVE temperature-current covariance raises the leading-order degradation rate, all else equal; other variance terms can counteract it.
Discriminating experiment: With independently measured T(x), j(x), compare matched-mean cells having different Cov(T,j); preregister a positive partial contribution, not an unconditional net effect.
Standing: derivation under stated illustrative assumptions; global novelty not established; no real-world test performed.

WORKED 017 — Chemical kinetics: barrier-distribution curvature
Model/assumptions: For parallel pathways k(T)=sum_j A_j exp[-E_j/(R T)], A_j>0 and constant E_j, set u=1/T.
Derived result: d² ln k / du² = Var_w(E)/R² >=0, with weights w_j=k_j/k. Strict curvature occurs if at least two contributing barriers differ.
Discriminating experiment: A measured negative curvature of ln k versus 1/T beyond uncertainty falsifies this restricted parallel-Arrhenius class; compare against known variable-prefactor and changing-mechanism alternatives.
Standing: derivation under stated illustrative assumptions; global novelty not established; no real-world test performed.

WORKED 026 — Heat transfer: interface thermal memory
Model/assumptions: Two lumped thermal bodies exchange heat with interfacial conductance h and temperatures T1,T2: C1*T1'=Q1-h(T1-T2); C2*T2'=Q2+h(T1-T2).
Derived result: Eliminating T2 produces a convolution-memory contribution to T1 with characteristic timescale tau=C2/h (when Q2=0 and coefficients constant); an instantaneous single-temperature model cannot generally reproduce the same transient for different T2(0).
Discriminating experiment: Prepare equal T1(0) but different T2(0); predict different initial slopes by -h*Delta(T1-T2)/C1. Known thermal RC mathematics; novelty requires better identification or new domain-specific limit.
Standing: derivation under stated illustrative assumptions; global novelty not established; no real-world test performed.

WORKED 036 — Fracture mechanics: overload sequence memory
Model/assumptions: For a simple crack-length model da/dN=C[DeltaK(a)]^m g(z), add a measured closure state z with dz/dN=-(z-z_eq(DeltaK))/n0; C>0, n0>0.
Derived result: At identical crack length and present DeltaK, histories with distinct z imply different da/dN. As n0->0, z tracks z_eq and the reduced baseline is recovered if g(z_eq)=1 under the chosen calibration.
Discriminating experiment: Compare overload-first and no-overload histories at matched present DeltaK and crack length; preregister the direction only after calibrating the closure-state sign. Load-sequence effects are established; no global novelty claim.
Standing: derivation under stated illustrative assumptions; global novelty not established; no real-world test performed.

WORKED 041 — Turbulence: intermittency-conditioned closure
Model/assumptions: Let q be local turbulent kinetic energy flux and y its coarse state. Introduce a measured intermittency indicator chi and model E[q|y,chi] rather than E[q|y].
Derived result: By the law of total variance, Var(q|y)=E[Var(q|y,chi)|y]+Var(E[q|y,chi]|y); conditioning cannot increase the optimal squared-error Bayes prediction risk in expectation.
Discriminating experiment: On held-out flow regimes, test whether measured chi yields nonzero conditional-mean variance and improves flux prediction at matched complexity; this is an information-theoretic guarantee, not a new turbulence law.
Standing: derivation under stated illustrative assumptions; global novelty not established; no real-world test performed.

WORKED 063 — Pharmacokinetics: organ perfusion covariance
Model/assumptions: Let organ extraction flux be F(Q,C)=Q*C*E(Q) with variable perfusion Q and extraction E(Q), C fixed in a short window.
Derived result: E[F(Q,C)]-F(E[Q],C) ~= (C/2) [2 E'(Qbar)+Qbar E''(Qbar)] Var(Q); the sign depends on the extraction law, not on 'heterogeneity' alone.
Discriminating experiment: Measure Q distribution and extraction curve independently, then preregister the predicted signed correction; reject if matched-mean experiments disagree.
Standing: derivation under stated illustrative assumptions; global novelty not established; no real-world test performed.

WORKED 072 — Epidemiology: infection-age infectiousness
Model/assumptions: Use infection-age density i(t,a) and infectivity beta(a). Incidence J(t)=S(t)/N * integral beta(a)i(t,a) da.
Derived result: The aggregate SIR incidence beta_bar*S*I/N is exact at an instant only if beta_bar equals the current infection-age weighted mean. Equal I can imply different J for different age distributions.
Discriminating experiment: Compare cohorts matched on S,I,N but different measured infection-age distributions; predict incidence from beta(a) fixed on training data. Age-structured models are established.
Standing: derivation under stated illustrative assumptions; global novelty not established; no real-world test performed.

WORKED 081 — Climate dynamics: ocean vertical heat memory
Model/assumptions: Two-box ocean heat model: C_s*T_s'=F-lambda*T_s-k(T_s-T_d); C_d*T_d'=k(T_s-T_d).
Derived result: At fixed T_s and forcing F, the surface warming rate differs by (k/C_s)*Delta T_d across histories. A one-box model based only on current T_s cannot be exact for both.
Discriminating experiment: Compare historical forcings that produce matched surface temperature but different subsurface heat content; test out-of-sample surface response. Two-box climate models are established.
Standing: derivation under stated illustrative assumptions; global novelty not established; no real-world test performed.

WORKED 096 — Optical materials: nano-inclusion spatial correlation
Model/assumptions: For dilute scatterers with positions r_i and single-scatterer amplitude f(q), total amplitude A(q)=f(q)*sum_i exp(i q.r_i).
Derived result: E[|A(q)|²]=|f(q)|² [N + sum_(i!=j) E exp(i q.(r_i-r_j))]; identical number density but different pair correlations yield different intensity.
Discriminating experiment: Fabricate matched-density samples with different pair correlations; preregister scattering contrast at chosen q. This is established structure-factor physics.
Standing: derivation under stated illustrative assumptions; global novelty not established; no real-world test performed.

E. 100 INDIVIDUAL CANDIDATE CONTRACTS (PROVISIONAL; 90 WITHOUT WORKED DERIVATIONS)
001. Battery electrochemistry — interfacial stress memory
Existing reference model: Butler–Volmer / porous-electrode; primary observable: charge-transfer rate.
Observed/latent variable to examine: interfacial stress memory.
Unverified title-derived mechanism hint: dynamic hidden state / delay. Use matched present-state trajectories with different prior forcing histories for interfacial stress memory; check whether their subsequent responses diverge.
Candidate construction: Introduce a physically measured relaxing state or convolution kernel; estimate its timescale from perturbation data, not arbitrary fitting.
Garden graph: THING=physical components; TIME=trajectory; SPACE=physical domain; EVENT=state transition; ACTION=controlled perturbation where applicable; AGENCY=experimenter/controller only; RULE=physical conservation; VALUE=declared performance measure; CONTEXT=experimental conditions; CLAIM=testable mechanism. Applicable edges: partOf, dependsOn, contextualizes, derivedFrom, supports/contradicts; use causes only after causal identification.
Seven forms: CONSTRUCT=system; CONTRACT=units/domain; STATE=measured and hidden variables; RELATION=typed dependencies; PROCESS=state evolution; RULE=physical constraints; PROJECTION=baseline observable.
Falsification protocol: Use matched present-state trajectories with different prior forcing histories for interfacial stress memory; check whether their subsequent responses diverge. Fit extension and strong modern reference model on training experiments; compare blinded held-out predictive likelihood/error under matched complexity and budget. If no robust improvement, reject the increment.
Benefit if validated: safer fast charging.
Evidence: CANDIDATE; domain-specific equation contract INCOMPLETE; numerical result NOT RUN; literature novelty UNKNOWN; empirical verification NOT DONE.

002. Battery electrochemistry — electrolyte concentration variance
Existing reference model: Butler–Volmer / porous-electrode; primary observable: charge-transfer rate.
Observed/latent variable to examine: electrolyte concentration variance.
Unverified title-derived mechanism hint: heterogeneity / joint distribution. Measure paired local fields or event-resolved distributions for electrolyte concentration variance; compare joint-data model with independently shuffled marginals.
Candidate construction: Add a measured joint-distribution statistic, not a free coefficient; derive aggregate response by averaging the local law and quantify the residual.
Garden graph: THING=physical components; TIME=trajectory; SPACE=physical domain; EVENT=state transition; ACTION=controlled perturbation where applicable; AGENCY=experimenter/controller only; RULE=physical conservation; VALUE=declared performance measure; CONTEXT=experimental conditions; CLAIM=testable mechanism. Applicable edges: partOf, dependsOn, contextualizes, derivedFrom, supports/contradicts; use causes only after causal identification.
Seven forms: CONSTRUCT=system; CONTRACT=units/domain; STATE=measured and hidden variables; RELATION=typed dependencies; PROCESS=state evolution; RULE=physical constraints; PROJECTION=baseline observable.
Falsification protocol: Measure paired local fields or event-resolved distributions for electrolyte concentration variance; compare joint-data model with independently shuffled marginals. Fit extension and strong modern reference model on training experiments; compare blinded held-out predictive likelihood/error under matched complexity and budget. If no robust improvement, reject the increment.
Benefit if validated: safer fast charging.
Evidence: CANDIDATE; domain-specific equation contract INCOMPLETE; numerical result NOT RUN; literature novelty UNKNOWN; empirical verification NOT DONE.

003. Battery electrochemistry — particle-size/contact covariance
Existing reference model: Butler–Volmer / porous-electrode; primary observable: charge-transfer rate.
Observed/latent variable to examine: particle-size/contact covariance.
Unverified title-derived mechanism hint: heterogeneity / joint distribution. Measure paired local fields or event-resolved distributions for particle-size/contact covariance; compare joint-data model with independently shuffled marginals.
Candidate construction: Add a measured joint-distribution statistic, not a free coefficient; derive aggregate response by averaging the local law and quantify the residual.
Garden graph: THING=physical components; TIME=trajectory; SPACE=physical domain; EVENT=state transition; ACTION=controlled perturbation where applicable; AGENCY=experimenter/controller only; RULE=physical conservation; VALUE=declared performance measure; CONTEXT=experimental conditions; CLAIM=testable mechanism. Applicable edges: partOf, dependsOn, contextualizes, derivedFrom, supports/contradicts; use causes only after causal identification.
Seven forms: CONSTRUCT=system; CONTRACT=units/domain; STATE=measured and hidden variables; RELATION=typed dependencies; PROCESS=state evolution; RULE=physical constraints; PROJECTION=baseline observable.
Falsification protocol: Measure paired local fields or event-resolved distributions for particle-size/contact covariance; compare joint-data model with independently shuffled marginals. Fit extension and strong modern reference model on training experiments; compare blinded held-out predictive likelihood/error under matched complexity and budget. If no robust improvement, reject the increment.
Benefit if validated: safer fast charging.
Evidence: CANDIDATE; domain-specific equation contract INCOMPLETE; numerical result NOT RUN; literature novelty UNKNOWN; empirical verification NOT DONE.

004. Battery electrochemistry — thermal-gradient persistence
Existing reference model: Butler–Volmer / porous-electrode; primary observable: charge-transfer rate.
Observed/latent variable to examine: thermal-gradient persistence.
Unverified title-derived mechanism hint: heterogeneity / joint distribution. Measure paired local fields or event-resolved distributions for thermal-gradient persistence; compare joint-data model with independently shuffled marginals.
Candidate construction: Add a measured joint-distribution statistic, not a free coefficient; derive aggregate response by averaging the local law and quantify the residual.
Garden graph: THING=physical components; TIME=trajectory; SPACE=physical domain; EVENT=state transition; ACTION=controlled perturbation where applicable; AGENCY=experimenter/controller only; RULE=physical conservation; VALUE=declared performance measure; CONTEXT=experimental conditions; CLAIM=testable mechanism. Applicable edges: partOf, dependsOn, contextualizes, derivedFrom, supports/contradicts; use causes only after causal identification.
Seven forms: CONSTRUCT=system; CONTRACT=units/domain; STATE=measured and hidden variables; RELATION=typed dependencies; PROCESS=state evolution; RULE=physical constraints; PROJECTION=baseline observable.
Falsification protocol: Measure paired local fields or event-resolved distributions for thermal-gradient persistence; compare joint-data model with independently shuffled marginals. Fit extension and strong modern reference model on training experiments; compare blinded held-out predictive likelihood/error under matched complexity and budget. If no robust improvement, reject the increment.
Benefit if validated: safer fast charging.
Evidence: CANDIDATE; domain-specific equation contract INCOMPLETE; numerical result NOT RUN; literature novelty UNKNOWN; empirical verification NOT DONE.

005. Battery electrochemistry — SEI connectivity hysteresis
Existing reference model: Butler–Volmer / porous-electrode; primary observable: charge-transfer rate.
Observed/latent variable to examine: SEI connectivity hysteresis.
Unverified title-derived mechanism hint: network / geometry. Image or reconstruct the evolving contact/connection graph underlying SEI connectivity hysteresis; hold aggregate counts fixed while varying graph statistics.
Candidate construction: Represent adjacency/connectivity explicitly; project to a minimal measurable graph statistic and check whether equal aggregate states have different futures.
Garden graph: THING=physical components; TIME=trajectory; SPACE=physical domain; EVENT=state transition; ACTION=controlled perturbation where applicable; AGENCY=experimenter/controller only; RULE=physical conservation; VALUE=declared performance measure; CONTEXT=experimental conditions; CLAIM=testable mechanism. Applicable edges: partOf, dependsOn, contextualizes, derivedFrom, supports/contradicts; use causes only after causal identification.
Seven forms: CONSTRUCT=system; CONTRACT=units/domain; STATE=measured and hidden variables; RELATION=typed dependencies; PROCESS=state evolution; RULE=physical constraints; PROJECTION=baseline observable.
Falsification protocol: Image or reconstruct the evolving contact/connection graph underlying SEI connectivity hysteresis; hold aggregate counts fixed while varying graph statistics. Fit extension and strong modern reference model on training experiments; compare blinded held-out predictive likelihood/error under matched complexity and budget. If no robust improvement, reject the increment.
Benefit if validated: safer fast charging.
Evidence: CANDIDATE; domain-specific equation contract INCOMPLETE; numerical result NOT RUN; literature novelty UNKNOWN; empirical verification NOT DONE.

006. Battery degradation — local heat-current covariance
Existing reference model: SEI growth / cycle-life models; primary observable: capacity-fade rate.
Observed/latent variable to examine: local heat-current covariance.
Unverified title-derived mechanism hint: heterogeneity / joint distribution. Measure paired local fields or event-resolved distributions for local heat-current covariance; compare joint-data model with independently shuffled marginals.
Candidate construction: Add a measured joint-distribution statistic, not a free coefficient; derive aggregate response by averaging the local law and quantify the residual.
Garden graph: THING=physical components; TIME=trajectory; SPACE=physical domain; EVENT=state transition; ACTION=controlled perturbation where applicable; AGENCY=experimenter/controller only; RULE=physical conservation; VALUE=declared performance measure; CONTEXT=experimental conditions; CLAIM=testable mechanism. Applicable edges: partOf, dependsOn, contextualizes, derivedFrom, supports/contradicts; use causes only after causal identification.
Seven forms: CONSTRUCT=system; CONTRACT=units/domain; STATE=measured and hidden variables; RELATION=typed dependencies; PROCESS=state evolution; RULE=physical constraints; PROJECTION=baseline observable.
Falsification protocol: Measure paired local fields or event-resolved distributions for local heat-current covariance; compare joint-data model with independently shuffled marginals. Fit extension and strong modern reference model on training experiments; compare blinded held-out predictive likelihood/error under matched complexity and budget. If no robust improvement, reject the increment.
Benefit if validated: longer battery lifetime.
Evidence: CANDIDATE; domain-specific equation contract INCOMPLETE; numerical result NOT RUN; literature novelty UNKNOWN; empirical verification NOT DONE.

007. Battery degradation — charge-rest sequencing
Existing reference model: SEI growth / cycle-life models; primary observable: capacity-fade rate.
Observed/latent variable to examine: charge-rest sequencing.
Unverified title-derived mechanism hint: dynamic hidden state / delay. Use matched present-state trajectories with different prior forcing histories for charge-rest sequencing; check whether their subsequent responses diverge.
Candidate construction: Introduce a physically measured relaxing state or convolution kernel; estimate its timescale from perturbation data, not arbitrary fitting.
Garden graph: THING=physical components; TIME=trajectory; SPACE=physical domain; EVENT=state transition; ACTION=controlled perturbation where applicable; AGENCY=experimenter/controller only; RULE=physical conservation; VALUE=declared performance measure; CONTEXT=experimental conditions; CLAIM=testable mechanism. Applicable edges: partOf, dependsOn, contextualizes, derivedFrom, supports/contradicts; use causes only after causal identification.
Seven forms: CONSTRUCT=system; CONTRACT=units/domain; STATE=measured and hidden variables; RELATION=typed dependencies; PROCESS=state evolution; RULE=physical constraints; PROJECTION=baseline observable.
Falsification protocol: Use matched present-state trajectories with different prior forcing histories for charge-rest sequencing; check whether their subsequent responses diverge. Fit extension and strong modern reference model on training experiments; compare blinded held-out predictive likelihood/error under matched complexity and budget. If no robust improvement, reject the increment.
Benefit if validated: longer battery lifetime.
Evidence: CANDIDATE; domain-specific equation contract INCOMPLETE; numerical result NOT RUN; literature novelty UNKNOWN; empirical verification NOT DONE.

008. Battery degradation — fracture-assisted reaction area
Existing reference model: SEI growth / cycle-life models; primary observable: capacity-fade rate.
Observed/latent variable to examine: fracture-assisted reaction area.
Unverified title-derived mechanism hint: network / geometry. Image or reconstruct the evolving contact/connection graph underlying fracture-assisted reaction area; hold aggregate counts fixed while varying graph statistics.
Candidate construction: Represent adjacency/connectivity explicitly; project to a minimal measurable graph statistic and check whether equal aggregate states have different futures.
Garden graph: THING=physical components; TIME=trajectory; SPACE=physical domain; EVENT=state transition; ACTION=controlled perturbation where applicable; AGENCY=experimenter/controller only; RULE=physical conservation; VALUE=declared performance measure; CONTEXT=experimental conditions; CLAIM=testable mechanism. Applicable edges: partOf, dependsOn, contextualizes, derivedFrom, supports/contradicts; use causes only after causal identification.
Seven forms: CONSTRUCT=system; CONTRACT=units/domain; STATE=measured and hidden variables; RELATION=typed dependencies; PROCESS=state evolution; RULE=physical constraints; PROJECTION=baseline observable.
Falsification protocol: Image or reconstruct the evolving contact/connection graph underlying fracture-assisted reaction area; hold aggregate counts fixed while varying graph statistics. Fit extension and strong modern reference model on training experiments; compare blinded held-out predictive likelihood/error under matched complexity and budget. If no robust improvement, reject the increment.
Benefit if validated: longer battery lifetime.
Evidence: CANDIDATE; domain-specific equation contract INCOMPLETE; numerical result NOT RUN; literature novelty UNKNOWN; empirical verification NOT DONE.

009. Battery degradation — lithium inventory redistribution
Existing reference model: SEI growth / cycle-life models; primary observable: capacity-fade rate.
Observed/latent variable to examine: lithium inventory redistribution.
Unverified title-derived mechanism hint: dynamic hidden state / delay. Use matched present-state trajectories with different prior forcing histories for lithium inventory redistribution; check whether their subsequent responses diverge.
Candidate construction: Introduce a physically measured relaxing state or convolution kernel; estimate its timescale from perturbation data, not arbitrary fitting.
Garden graph: THING=physical components; TIME=trajectory; SPACE=physical domain; EVENT=state transition; ACTION=controlled perturbation where applicable; AGENCY=experimenter/controller only; RULE=physical conservation; VALUE=declared performance measure; CONTEXT=experimental conditions; CLAIM=testable mechanism. Applicable edges: partOf, dependsOn, contextualizes, derivedFrom, supports/contradicts; use causes only after causal identification.
Seven forms: CONSTRUCT=system; CONTRACT=units/domain; STATE=measured and hidden variables; RELATION=typed dependencies; PROCESS=state evolution; RULE=physical constraints; PROJECTION=baseline observable.
Falsification protocol: Use matched present-state trajectories with different prior forcing histories for lithium inventory redistribution; check whether their subsequent responses diverge. Fit extension and strong modern reference model on training experiments; compare blinded held-out predictive likelihood/error under matched complexity and budget. If no robust improvement, reject the increment.
Benefit if validated: longer battery lifetime.
Evidence: CANDIDATE; domain-specific equation contract INCOMPLETE; numerical result NOT RUN; literature novelty UNKNOWN; empirical verification NOT DONE.

010. Battery degradation — electrode pore-network fragmentation
Existing reference model: SEI growth / cycle-life models; primary observable: capacity-fade rate.
Observed/latent variable to examine: electrode pore-network fragmentation.
Unverified title-derived mechanism hint: network / geometry. Image or reconstruct the evolving contact/connection graph underlying electrode pore-network fragmentation; hold aggregate counts fixed while varying graph statistics.
Candidate construction: Represent adjacency/connectivity explicitly; project to a minimal measurable graph statistic and check whether equal aggregate states have different futures.
Garden graph: THING=physical components; TIME=trajectory; SPACE=physical domain; EVENT=state transition; ACTION=controlled perturbation where applicable; AGENCY=experimenter/controller only; RULE=physical conservation; VALUE=declared performance measure; CONTEXT=experimental conditions; CLAIM=testable mechanism. Applicable edges: partOf, dependsOn, contextualizes, derivedFrom, supports/contradicts; use causes only after causal identification.
Seven forms: CONSTRUCT=system; CONTRACT=units/domain; STATE=measured and hidden variables; RELATION=typed dependencies; PROCESS=state evolution; RULE=physical constraints; PROJECTION=baseline observable.
Falsification protocol: Image or reconstruct the evolving contact/connection graph underlying electrode pore-network fragmentation; hold aggregate counts fixed while varying graph statistics. Fit extension and strong modern reference model on training experiments; compare blinded held-out predictive likelihood/error under matched complexity and budget. If no robust improvement, reject the increment.
Benefit if validated: longer battery lifetime.
Evidence: CANDIDATE; domain-specific equation contract INCOMPLETE; numerical result NOT RUN; literature novelty UNKNOWN; empirical verification NOT DONE.

011. Heterogeneous catalysis — surface reconstruction memory
Existing reference model: Sabatier / Langmuir–Hinshelwood; primary observable: turnover frequency.
Observed/latent variable to examine: surface reconstruction memory.
Unverified title-derived mechanism hint: dynamic hidden state / delay. Use matched present-state trajectories with different prior forcing histories for surface reconstruction memory; check whether their subsequent responses diverge.
Candidate construction: Introduce a physically measured relaxing state or convolution kernel; estimate its timescale from perturbation data, not arbitrary fitting.
Garden graph: THING=physical components; TIME=trajectory; SPACE=physical domain; EVENT=state transition; ACTION=controlled perturbation where applicable; AGENCY=experimenter/controller only; RULE=physical conservation; VALUE=declared performance measure; CONTEXT=experimental conditions; CLAIM=testable mechanism. Applicable edges: partOf, dependsOn, contextualizes, derivedFrom, supports/contradicts; use causes only after causal identification.
Seven forms: CONSTRUCT=system; CONTRACT=units/domain; STATE=measured and hidden variables; RELATION=typed dependencies; PROCESS=state evolution; RULE=physical constraints; PROJECTION=baseline observable.
Falsification protocol: Use matched present-state trajectories with different prior forcing histories for surface reconstruction memory; check whether their subsequent responses diverge. Fit extension and strong modern reference model on training experiments; compare blinded held-out predictive likelihood/error under matched complexity and budget. If no robust improvement, reject the increment.
Benefit if validated: lower-energy chemical manufacture.
Evidence: CANDIDATE; domain-specific equation contract INCOMPLETE; numerical result NOT RUN; literature novelty UNKNOWN; empirical verification NOT DONE.

012. Heterogeneous catalysis — adsorbate-neighbor correlations
Existing reference model: Sabatier / Langmuir–Hinshelwood; primary observable: turnover frequency.
Observed/latent variable to examine: adsorbate-neighbor correlations.
Unverified title-derived mechanism hint: heterogeneity / joint distribution. Measure paired local fields or event-resolved distributions for adsorbate-neighbor correlations; compare joint-data model with independently shuffled marginals.
Candidate construction: Add a measured joint-distribution statistic, not a free coefficient; derive aggregate response by averaging the local law and quantify the residual.
Garden graph: THING=physical components; TIME=trajectory; SPACE=physical domain; EVENT=state transition; ACTION=controlled perturbation where applicable; AGENCY=experimenter/controller only; RULE=physical conservation; VALUE=declared performance measure; CONTEXT=experimental conditions; CLAIM=testable mechanism. Applicable edges: partOf, dependsOn, contextualizes, derivedFrom, supports/contradicts; use causes only after causal identification.
Seven forms: CONSTRUCT=system; CONTRACT=units/domain; STATE=measured and hidden variables; RELATION=typed dependencies; PROCESS=state evolution; RULE=physical constraints; PROJECTION=baseline observable.
Falsification protocol: Measure paired local fields or event-resolved distributions for adsorbate-neighbor correlations; compare joint-data model with independently shuffled marginals. Fit extension and strong modern reference model on training experiments; compare blinded held-out predictive likelihood/error under matched complexity and budget. If no robust improvement, reject the increment.
Benefit if validated: lower-energy chemical manufacture.
Evidence: CANDIDATE; domain-specific equation contract INCOMPLETE; numerical result NOT RUN; literature novelty UNKNOWN; empirical verification NOT DONE.

013. Heterogeneous catalysis — pulsed feed phase
Existing reference model: Sabatier / Langmuir–Hinshelwood; primary observable: turnover frequency.
Observed/latent variable to examine: pulsed feed phase.
Unverified title-derived mechanism hint: state switching / hysteresis. Cycle the driving variable in both directions and record branch-dependent response for pulsed feed phase; test whether a single-valued constitutive law fails.
Candidate construction: Introduce a branch/state variable with experimentally constrained transition rules; verify return-point and cycling behavior only if observed.
Garden graph: THING=physical components; TIME=trajectory; SPACE=physical domain; EVENT=state transition; ACTION=controlled perturbation where applicable; AGENCY=experimenter/controller only; RULE=physical conservation; VALUE=declared performance measure; CONTEXT=experimental conditions; CLAIM=testable mechanism. Applicable edges: partOf, dependsOn, contextualizes, derivedFrom, supports/contradicts; use causes only after causal identification.
Seven forms: CONSTRUCT=system; CONTRACT=units/domain; STATE=measured and hidden variables; RELATION=typed dependencies; PROCESS=state evolution; RULE=physical constraints; PROJECTION=baseline observable.
Falsification protocol: Cycle the driving variable in both directions and record branch-dependent response for pulsed feed phase; test whether a single-valued constitutive law fails. Fit extension and strong modern reference model on training experiments; compare blinded held-out predictive likelihood/error under matched complexity and budget. If no robust improvement, reject the increment.
Benefit if validated: lower-energy chemical manufacture.
Evidence: CANDIDATE; domain-specific equation contract INCOMPLETE; numerical result NOT RUN; literature novelty UNKNOWN; empirical verification NOT DONE.

014. Heterogeneous catalysis — active-site network percolation
Existing reference model: Sabatier / Langmuir–Hinshelwood; primary observable: turnover frequency.
Observed/latent variable to examine: active-site network percolation.
Unverified title-derived mechanism hint: network / geometry. Image or reconstruct the evolving contact/connection graph underlying active-site network percolation; hold aggregate counts fixed while varying graph statistics.
Candidate construction: Represent adjacency/connectivity explicitly; project to a minimal measurable graph statistic and check whether equal aggregate states have different futures.
Garden graph: THING=physical components; TIME=trajectory; SPACE=physical domain; EVENT=state transition; ACTION=controlled perturbation where applicable; AGENCY=experimenter/controller only; RULE=physical conservation; VALUE=declared performance measure; CONTEXT=experimental conditions; CLAIM=testable mechanism. Applicable edges: partOf, dependsOn, contextualizes, derivedFrom, supports/contradicts; use causes only after causal identification.
Seven forms: CONSTRUCT=system; CONTRACT=units/domain; STATE=measured and hidden variables; RELATION=typed dependencies; PROCESS=state evolution; RULE=physical constraints; PROJECTION=baseline observable.
Falsification protocol: Image or reconstruct the evolving contact/connection graph underlying active-site network percolation; hold aggregate counts fixed while varying graph statistics. Fit extension and strong modern reference model on training experiments; compare blinded held-out predictive likelihood/error under matched complexity and budget. If no robust improvement, reject the increment.
Benefit if validated: lower-energy chemical manufacture.
Evidence: CANDIDATE; domain-specific equation contract INCOMPLETE; numerical result NOT RUN; literature novelty UNKNOWN; empirical verification NOT DONE.

015. Heterogeneous catalysis — poison desorption history
Existing reference model: Sabatier / Langmuir–Hinshelwood; primary observable: turnover frequency.
Observed/latent variable to examine: poison desorption history.
Unverified title-derived mechanism hint: dynamic hidden state / delay. Use matched present-state trajectories with different prior forcing histories for poison desorption history; check whether their subsequent responses diverge.
Candidate construction: Introduce a physically measured relaxing state or convolution kernel; estimate its timescale from perturbation data, not arbitrary fitting.
Garden graph: THING=physical components; TIME=trajectory; SPACE=physical domain; EVENT=state transition; ACTION=controlled perturbation where applicable; AGENCY=experimenter/controller only; RULE=physical conservation; VALUE=declared performance measure; CONTEXT=experimental conditions; CLAIM=testable mechanism. Applicable edges: partOf, dependsOn, contextualizes, derivedFrom, supports/contradicts; use causes only after causal identification.
Seven forms: CONSTRUCT=system; CONTRACT=units/domain; STATE=measured and hidden variables; RELATION=typed dependencies; PROCESS=state evolution; RULE=physical constraints; PROJECTION=baseline observable.
Falsification protocol: Use matched present-state trajectories with different prior forcing histories for poison desorption history; check whether their subsequent responses diverge. Fit extension and strong modern reference model on training experiments; compare blinded held-out predictive likelihood/error under matched complexity and budget. If no robust improvement, reject the increment.
Benefit if validated: lower-energy chemical manufacture.
Evidence: CANDIDATE; domain-specific equation contract INCOMPLETE; numerical result NOT RUN; literature novelty UNKNOWN; empirical verification NOT DONE.

016. Chemical kinetics — competing-pathway occupancyExisting reference model: Arrhenius / transition-state theory; primary observable: effective reaction rate.
Observed/latent variable to examine: competing-pathway occupancy.
Unverified title-derived mechanism hint: coupled latent kinetics. Measure the candidate intermediate state for competing-pathway occupancy during perturbation/recovery; test whether it predicts held-out transients beyond baseline variables.
Candidate construction: Introduce a measurable intermediate and couple it by mass/energy-balanced rate equations; test observability and parameter identifiability.
Garden graph: THING=physical components; TIME=trajectory; SPACE=physical domain; EVENT=state transition; ACTION=controlled perturbation where applicable; AGENCY=experimenter/controller only; RULE=physical conservation; VALUE=declared performance measure; CONTEXT=experimental conditions; CLAIM=testable mechanism. Applicable edges: partOf, dependsOn, contextualizes, derivedFrom, supports/contradicts; use causes only after causal identification.
Seven forms: CONSTRUCT=system; CONTRACT=units/domain; STATE=measured and hidden variables; RELATION=typed dependencies; PROCESS=state evolution; RULE=physical constraints; PROJECTION=baseline observable.
Falsification protocol: Measure the candidate intermediate state for competing-pathway occupancy during perturbation/recovery; test whether it predicts held-out transients beyond baseline variables. Fit extension and strong modern reference model on training experiments; compare blinded held-out predictive likelihood/error under matched complexity and budget. If no robust improvement, reject the increment.
Benefit if validated: better reactor efficiency.
Evidence: CANDIDATE; domain-specific equation contract INCOMPLETE; numerical result NOT RUN; literature novelty UNKNOWN; empirical verification NOT DONE.

017. Chemical kinetics — barrier-distribution curvature
Existing reference model: Arrhenius / transition-state theory; primary observable: effective reaction rate.
Observed/latent variable to examine: barrier-distribution curvature.
Unverified title-derived mechanism hint: mechanism unresolved — requires domain diagnostics. Collect perturbation-response measurements for barrier-distribution curvature; identify residual structure before selecting an extension.
Candidate construction: Do not choose a mechanism before observing structured residuals; record an unresolved research question.
Garden graph: THING=physical components; TIME=trajectory; SPACE=physical domain; EVENT=state transition; ACTION=controlled perturbation where applicable; AGENCY=experimenter/controller only; RULE=physical conservation; VALUE=declared performance measure; CONTEXT=experimental conditions; CLAIM=testable mechanism. Applicable edges: partOf, dependsOn, contextualizes, derivedFrom, supports/contradicts; use causes only after causal identification.
Seven forms: CONSTRUCT=system; CONTRACT=units/domain; STATE=measured and hidden variables; RELATION=typed dependencies; PROCESS=state evolution; RULE=physical constraints; PROJECTION=baseline observable.
Falsification protocol: Collect perturbation-response measurements for barrier-distribution curvature; identify residual structure before selecting an extension. Fit extension and strong modern reference model on training experiments; compare blinded held-out predictive likelihood/error under matched complexity and budget. If no robust improvement, reject the increment.
Benefit if validated: better reactor efficiency.
Evidence: CANDIDATE; domain-specific equation contract INCOMPLETE; numerical result NOT RUN; literature novelty UNKNOWN; empirical verification NOT DONE.

018. Chemical kinetics — solvent reorganization lag
Existing reference model: Arrhenius / transition-state theory; primary observable: effective reaction rate.
Observed/latent variable to examine: solvent reorganization lag.
Unverified title-derived mechanism hint: dynamic hidden state / delay. Use matched present-state trajectories with different prior forcing histories for solvent reorganization lag; check whether their subsequent responses diverge.
Candidate construction: Introduce a physically measured relaxing state or convolution kernel; estimate its timescale from perturbation data, not arbitrary fitting.
Garden graph: THING=physical components; TIME=trajectory; SPACE=physical domain; EVENT=state transition; ACTION=controlled perturbation where applicable; AGENCY=experimenter/controller only; RULE=physical conservation; VALUE=declared performance measure; CONTEXT=experimental conditions; CLAIM=testable mechanism. Applicable edges: partOf, dependsOn, contextualizes, derivedFrom, supports/contradicts; use causes only after causal identification.
Seven forms: CONSTRUCT=system; CONTRACT=units/domain; STATE=measured and hidden variables; RELATION=typed dependencies; PROCESS=state evolution; RULE=physical constraints; PROJECTION=baseline observable.
Falsification protocol: Use matched present-state trajectories with different prior forcing histories for solvent reorganization lag; check whether their subsequent responses diverge. Fit extension and strong modern reference model on training experiments; compare blinded held-out predictive likelihood/error under matched complexity and budget. If no robust improvement, reject the increment.
Benefit if validated: better reactor efficiency.
Evidence: CANDIDATE; domain-specific equation contract INCOMPLETE; numerical result NOT RUN; literature novelty UNKNOWN; empirical verification NOT DONE.

019. Chemical kinetics — reactant clustering
Existing reference model: Arrhenius / transition-state theory; primary observable: effective reaction rate.
Observed/latent variable to examine: reactant clustering.
Unverified title-derived mechanism hint: network / geometry. Image or reconstruct the evolving contact/connection graph underlying reactant clustering; hold aggregate counts fixed while varying graph statistics.
Candidate construction: Represent adjacency/connectivity explicitly; project to a minimal measurable graph statistic and check whether equal aggregate states have different futures.
Garden graph: THING=physical components; TIME=trajectory; SPACE=physical domain; EVENT=state transition; ACTION=controlled perturbation where applicable; AGENCY=experimenter/controller only; RULE=physical conservation; VALUE=declared performance measure; CONTEXT=experimental conditions; CLAIM=testable mechanism. Applicable edges: partOf, dependsOn, contextualizes, derivedFrom, supports/contradicts; use causes only after causal identification.
Seven forms: CONSTRUCT=system; CONTRACT=units/domain; STATE=measured and hidden variables; RELATION=typed dependencies; PROCESS=state evolution; RULE=physical constraints; PROJECTION=baseline observable.
Falsification protocol: Image or reconstruct the evolving contact/connection graph underlying reactant clustering; hold aggregate counts fixed while varying graph statistics. Fit extension and strong modern reference model on training experiments; compare blinded held-out predictive likelihood/error under matched complexity and budget. If no robust improvement, reject the increment.
Benefit if validated: better reactor efficiency.
Evidence: CANDIDATE; domain-specific equation contract INCOMPLETE; numerical result NOT RUN; literature novelty UNKNOWN; empirical verification NOT DONE.

020. Chemical kinetics — intermediate trapping memory
Existing reference model: Arrhenius / transition-state theory; primary observable: effective reaction rate.
Observed/latent variable to examine: intermediate trapping memory.
Unverified title-derived mechanism hint: dynamic hidden state / delay. Use matched present-state trajectories with different prior forcing histories for intermediate trapping memory; check whether their subsequent responses diverge.
Candidate construction: Introduce a physically measured relaxing state or convolution kernel; estimate its timescale from perturbation data, not arbitrary fitting.
Garden graph: THING=physical components; TIME=trajectory; SPACE=physical domain; EVENT=state transition; ACTION=controlled perturbation where applicable; AGENCY=experimenter/controller only; RULE=physical conservation; VALUE=declared performance measure; CONTEXT=experimental conditions; CLAIM=testable mechanism. Applicable edges: partOf, dependsOn, contextualizes, derivedFrom, supports/contradicts; use causes only after causal identification.
Seven forms: CONSTRUCT=system; CONTRACT=units/domain; STATE=measured and hidden variables; RELATION=typed dependencies; PROCESS=state evolution; RULE=physical constraints; PROJECTION=baseline observable.
Falsification protocol: Use matched present-state trajectories with different prior forcing histories for intermediate trapping memory; check whether their subsequent responses diverge. Fit extension and strong modern reference model on training experiments; compare blinded held-out predictive likelihood/error under matched complexity and budget. If no robust improvement, reject the increment.
Benefit if validated: better reactor efficiency.
Evidence: CANDIDATE; domain-specific equation contract INCOMPLETE; numerical result NOT RUN; literature novelty UNKNOWN; empirical verification NOT DONE.

021. Nucleation — subcritical-cluster history
Existing reference model: classical nucleation theory; primary observable: nucleation hazard.
Observed/latent variable to examine: subcritical-cluster history.
Unverified title-derived mechanism hint: dynamic hidden state / delay. Use matched present-state trajectories with different prior forcing histories for subcritical-cluster history; check whether their subsequent responses diverge.
Candidate construction: Introduce a physically measured relaxing state or convolution kernel; estimate its timescale from perturbation data, not arbitrary fitting.
Garden graph: THING=physical components; TIME=trajectory; SPACE=physical domain; EVENT=state transition; ACTION=controlled perturbation where applicable; AGENCY=experimenter/controller only; RULE=physical conservation; VALUE=declared performance measure; CONTEXT=experimental conditions; CLAIM=testable mechanism. Applicable edges: partOf, dependsOn, contextualizes, derivedFrom, supports/contradicts; use causes only after causal identification.
Seven forms: CONSTRUCT=system; CONTRACT=units/domain; STATE=measured and hidden variables; RELATION=typed dependencies; PROCESS=state evolution; RULE=physical constraints; PROJECTION=baseline observable.
Falsification protocol: Use matched present-state trajectories with different prior forcing histories for subcritical-cluster history; check whether their subsequent responses diverge. Fit extension and strong modern reference model on training experiments; compare blinded held-out predictive likelihood/error under matched complexity and budget. If no robust improvement, reject the increment.
Benefit if validated: crystal and drug formulation.
Evidence: CANDIDATE; domain-specific equation contract INCOMPLETE; numerical result NOT RUN; literature novelty UNKNOWN; empirical verification NOT DONE.

022. Nucleation — surface-defect localization
Existing reference model: classical nucleation theory; primary observable: nucleation hazard.
Observed/latent variable to examine: surface-defect localization.
Unverified title-derived mechanism hint: mechanism unresolved — requires domain diagnostics. Collect perturbation-response measurements for surface-defect localization; identify residual structure before selecting an extension.
Candidate construction: Do not choose a mechanism before observing structured residuals; record an unresolved research question.
Garden graph: THING=physical components; TIME=trajectory; SPACE=physical domain; EVENT=state transition; ACTION=controlled perturbation where applicable; AGENCY=experimenter/controller only; RULE=physical conservation; VALUE=declared performance measure; CONTEXT=experimental conditions; CLAIM=testable mechanism. Applicable edges: partOf, dependsOn, contextualizes, derivedFrom, supports/contradicts; use causes only after causal identification.
Seven forms: CONSTRUCT=system; CONTRACT=units/domain; STATE=measured and hidden variables; RELATION=typed dependencies; PROCESS=state evolution; RULE=physical constraints; PROJECTION=baseline observable.
Falsification protocol: Collect perturbation-response measurements for surface-defect localization; identify residual structure before selecting an extension. Fit extension and strong modern reference model on training experiments; compare blinded held-out predictive likelihood/error under matched complexity and budget. If no robust improvement, reject the increment.
Benefit if validated: crystal and drug formulation.
Evidence: CANDIDATE; domain-specific equation contract INCOMPLETE; numerical result NOT RUN; literature novelty UNKNOWN; empirical verification NOT DONE.

023. Nucleation — solvent pulse memory
Existing reference model: classical nucleation theory; primary observable: nucleation hazard.
Observed/latent variable to examine: solvent pulse memory.
Unverified title-derived mechanism hint: dynamic hidden state / delay. Use matched present-state trajectories with different prior forcing histories for solvent pulse memory; check whether their subsequent responses diverge.
Candidate construction: Introduce a physically measured relaxing state or convolution kernel; estimate its timescale from perturbation data, not arbitrary fitting.
Garden graph: THING=physical components; TIME=trajectory; SPACE=physical domain; EVENT=state transition; ACTION=controlled perturbation where applicable; AGENCY=experimenter/controller only; RULE=physical conservation; VALUE=declared performance measure; CONTEXT=experimental conditions; CLAIM=testable mechanism. Applicable edges: partOf, dependsOn, contextualizes, derivedFrom, supports/contradicts; use causes only after causal identification.
Seven forms: CONSTRUCT=system; CONTRACT=units/domain; STATE=measured and hidden variables; RELATION=typed dependencies; PROCESS=state evolution; RULE=physical constraints; PROJECTION=baseline observable.
Falsification protocol: Use matched present-state trajectories with different prior forcing histories for solvent pulse memory; check whether their subsequent responses diverge. Fit extension and strong modern reference model on training experiments; compare blinded held-out predictive likelihood/error under matched complexity and budget. If no robust improvement, reject the increment.
Benefit if validated: crystal and drug formulation.
Evidence: CANDIDATE; domain-specific equation contract INCOMPLETE; numerical result NOT RUN; literature novelty UNKNOWN; empirical verification NOT DONE.

024. Nucleation — impurity-cluster correlations
Existing reference model: classical nucleation theory; primary observable: nucleation hazard.
Observed/latent variable to examine: impurity-cluster correlations.
Unverified title-derived mechanism hint: heterogeneity / joint distribution. Measure paired local fields or event-resolved distributions for impurity-cluster correlations; compare joint-data model with independently shuffled marginals.
Candidate construction: Add a measured joint-distribution statistic, not a free coefficient; derive aggregate response by averaging the local law and quantify the residual.
Garden graph: THING=physical components; TIME=trajectory; SPACE=physical domain; EVENT=state transition; ACTION=controlled perturbation where applicable; AGENCY=experimenter/controller only; RULE=physical conservation; VALUE=declared performance measure; CONTEXT=experimental conditions; CLAIM=testable mechanism. Applicable edges: partOf, dependsOn, contextualizes, derivedFrom, supports/contradicts; use causes only after causal identification.
Seven forms: CONSTRUCT=system; CONTRACT=units/domain; STATE=measured and hidden variables; RELATION=typed dependencies; PROCESS=state evolution; RULE=physical constraints; PROJECTION=baseline observable.
Falsification protocol: Measure paired local fields or event-resolved distributions for impurity-cluster correlations; compare joint-data model with independently shuffled marginals. Fit extension and strong modern reference model on training experiments; compare blinded held-out predictive likelihood/error under matched complexity and budget. If no robust improvement, reject the increment.
Benefit if validated: crystal and drug formulation.
Evidence: CANDIDATE; domain-specific equation contract INCOMPLETE; numerical result NOT RUN; literature novelty UNKNOWN; empirical verification NOT DONE.

025. Nucleation — spatial supersaturation intermittency
Existing reference model: classical nucleation theory; primary observable: nucleation hazard.
Observed/latent variable to examine: spatial supersaturation intermittency.
Unverified title-derived mechanism hint: heterogeneity / joint distribution. Measure paired local fields or event-resolved distributions for spatial supersaturation intermittency; compare joint-data model with independently shuffled marginals.
Candidate construction: Add a measured joint-distribution statistic, not a free coefficient; derive aggregate response by averaging the local law and quantify the residual.
Garden graph: THING=physical components; TIME=trajectory; SPACE=physical domain; EVENT=state transition; ACTION=controlled perturbation where applicable; AGENCY=experimenter/controller only; RULE=physical conservation; VALUE=declared performance measure; CONTEXT=experimental conditions; CLAIM=testable mechanism. Applicable edges: partOf, dependsOn, contextualizes, derivedFrom, supports/contradicts; use causes only after causal identification.
Seven forms: CONSTRUCT=system; CONTRACT=units/domain; STATE=measured and hidden variables; RELATION=typed dependencies; PROCESS=state evolution; RULE=physical constraints; PROJECTION=baseline observable.
Falsification protocol: Measure paired local fields or event-resolved distributions for spatial supersaturation intermittency; compare joint-data model with independently shuffled marginals. Fit extension and strong modern reference model on training experiments; compare blinded held-out predictive likelihood/error under matched complexity and budget. If no robust improvement, reject the increment.
Benefit if validated: crystal and drug formulation.
Evidence: CANDIDATE; domain-specific equation contract INCOMPLETE; numerical result NOT RUN; literature novelty UNKNOWN; empirical verification NOT DONE.

026. Heat transfer — interface thermal memory
Existing reference model: Fourier conduction; primary observable: heat flux.
Observed/latent variable to examine: interface thermal memory.
Unverified title-derived mechanism hint: dynamic hidden state / delay. Use matched present-state trajectories with different prior forcing histories for interface thermal memory; check whether their subsequent responses diverge.
Candidate construction: Introduce a physically measured relaxing state or convolution kernel; estimate its timescale from perturbation data, not arbitrary fitting.
Garden graph: THING=physical components; TIME=trajectory; SPACE=physical domain; EVENT=state transition; ACTION=controlled perturbation where applicable; AGENCY=experimenter/controller only; RULE=physical conservation; VALUE=declared performance measure; CONTEXT=experimental conditions; CLAIM=testable mechanism. Applicable edges: partOf, dependsOn, contextualizes, derivedFrom, supports/contradicts; use causes only after causal identification.
Seven forms: CONSTRUCT=system; CONTRACT=units/domain; STATE=measured and hidden variables; RELATION=typed dependencies; PROCESS=state evolution; RULE=physical constraints; PROJECTION=baseline observable.
Falsification protocol: Use matched present-state trajectories with different prior forcing histories for interface thermal memory; check whether their subsequent responses diverge. Fit extension and strong modern reference model on training experiments; compare blinded held-out predictive likelihood/error under matched complexity and budget. If no robust improvement, reject the increment.
Benefit if validated: chip and battery cooling.
Evidence: CANDIDATE; domain-specific equation contract INCOMPLETE; numerical result NOT RUN; literature novelty UNKNOWN; empirical verification NOT DONE.

027. Heat transfer — anisotropic domain connectivity
Existing reference model: Fourier conduction; primary observable: heat flux.
Observed/latent variable to examine: anisotropic domain connectivity.
Unverified title-derived mechanism hint: network / geometry. Image or reconstruct the evolving contact/connection graph underlying anisotropic domain connectivity; hold aggregate counts fixed while varying graph statistics.
Candidate construction: Represent adjacency/connectivity explicitly; project to a minimal measurable graph statistic and check whether equal aggregate states have different futures.
Garden graph: THING=physical components; TIME=trajectory; SPACE=physical domain; EVENT=state transition; ACTION=controlled perturbation where applicable; AGENCY=experimenter/controller only; RULE=physical conservation; VALUE=declared performance measure; CONTEXT=experimental conditions; CLAIM=testable mechanism. Applicable edges: partOf, dependsOn, contextualizes, derivedFrom, supports/contradicts; use causes only after causal identification.
Seven forms: CONSTRUCT=system; CONTRACT=units/domain; STATE=measured and hidden variables; RELATION=typed dependencies; PROCESS=state evolution; RULE=physical constraints; PROJECTION=baseline observable.
Falsification protocol: Image or reconstruct the evolving contact/connection graph underlying anisotropic domain connectivity; hold aggregate counts fixed while varying graph statistics. Fit extension and strong modern reference model on training experiments; compare blinded held-out predictive likelihood/error under matched complexity and budget. If no robust improvement, reject the increment.
Benefit if validated: chip and battery cooling.
Evidence: CANDIDATE; domain-specific equation contract INCOMPLETE; numerical result NOT RUN; literature novelty UNKNOWN; empirical verification NOT DONE.

028. Heat transfer — nonlocal hotspot coupling
Existing reference model: Fourier conduction; primary observable: heat flux.
Observed/latent variable to examine: nonlocal hotspot coupling.
Unverified title-derived mechanism hint: coupled latent kinetics. Measure the candidate intermediate state for nonlocal hotspot coupling during perturbation/recovery; test whether it predicts held-out transients beyond baseline variables.
Candidate construction: Introduce a measurable intermediate and couple it by mass/energy-balanced rate equations; test observability and parameter identifiability.
Garden graph: THING=physical components; TIME=trajectory; SPACE=physical domain; EVENT=state transition; ACTION=controlled perturbation where applicable; AGENCY=experimenter/controller only; RULE=physical conservation; VALUE=declared performance measure; CONTEXT=experimental conditions; CLAIM=testable mechanism. Applicable edges: partOf, dependsOn, contextualizes, derivedFrom, supports/contradicts; use causes only after causal identification.
Seven forms: CONSTRUCT=system; CONTRACT=units/domain; STATE=measured and hidden variables; RELATION=typed dependencies; PROCESS=state evolution; RULE=physical constraints; PROJECTION=baseline observable.
Falsification protocol: Measure the candidate intermediate state for nonlocal hotspot coupling during perturbation/recovery; test whether it predicts held-out transients beyond baseline variables. Fit extension and strong modern reference model on training experiments; compare blinded held-out predictive likelihood/error under matched complexity and budget. If no robust improvement, reject the increment.
Benefit if validated: chip and battery cooling.
Evidence: CANDIDATE; domain-specific equation contract INCOMPLETE; numerical result NOT RUN; literature novelty UNKNOWN; empirical verification NOT DONE.

029. Heat transfer — phase-transition latent-heat lag
Existing reference model: Fourier conduction; primary observable: heat flux.
Observed/latent variable to examine: phase-transition latent-heat lag.
Unverified title-derived mechanism hint: state switching / hysteresis. Cycle the driving variable in both directions and record branch-dependent response for phase-transition latent-heat lag; test whether a single-valued constitutive law fails.
Candidate construction: Introduce a branch/state variable with experimentally constrained transition rules; verify return-point and cycling behavior only if observed.
Garden graph: THING=physical components; TIME=trajectory; SPACE=physical domain; EVENT=state transition; ACTION=controlled perturbation where applicable; AGENCY=experimenter/controller only; RULE=physical conservation; VALUE=declared performance measure; CONTEXT=experimental conditions; CLAIM=testable mechanism. Applicable edges: partOf, dependsOn, contextualizes, derivedFrom, supports/contradicts; use causes only after causal identification.
Seven forms: CONSTRUCT=system; CONTRACT=units/domain; STATE=measured and hidden variables; RELATION=typed dependencies; PROCESS=state evolution; RULE=physical constraints; PROJECTION=baseline observable.
Falsification protocol: Cycle the driving variable in both directions and record branch-dependent response for phase-transition latent-heat lag; test whether a single-valued constitutive law fails. Fit extension and strong modern reference model on training experiments; compare blinded held-out predictive likelihood/error under matched complexity and budget. If no robust improvement, reject the increment.
Benefit if validated: chip and battery cooling.
Evidence: CANDIDATE; domain-specific equation contract INCOMPLETE; numerical result NOT RUN; literature novelty UNKNOWN; empirical verification NOT DONE.

030. Heat transfer — thermal-contact ageing
Existing reference model: Fourier conduction; primary observable: heat flux.
Observed/latent variable to examine: thermal-contact ageing.
Unverified title-derived mechanism hint: network / geometry. Image or reconstruct the evolving contact/connection graph underlying thermal-contact ageing; hold aggregate counts fixed while varying graph statistics.
Candidate construction: Represent adjacency/connectivity explicitly; project to a minimal measurable graph statistic and check whether equal aggregate states have different futures.
Garden graph: THING=physical components; TIME=trajectory; SPACE=physical domain; EVENT=state transition; ACTION=controlled perturbation where applicable; AGENCY=experimenter/controller only; RULE=physical conservation; VALUE=declared performance measure; CONTEXT=experimental conditions; CLAIM=testable mechanism. Applicable edges: partOf, dependsOn, contextualizes, derivedFrom, supports/contradicts; use causes only after causal identification.
Seven forms: CONSTRUCT=system; CONTRACT=units/domain; STATE=measured and hidden variables; RELATION=typed dependencies; PROCESS=state evolution; RULE=physical constraints; PROJECTION=baseline observable.
Falsification protocol: Image or reconstruct the evolving contact/connection graph underlying thermal-contact ageing; hold aggregate counts fixed while varying graph statistics. Fit extension and strong modern reference model on training experiments; compare blinded held-out predictive likelihood/error under matched complexity and budget. If no robust improvement, reject the increment.
Benefit if validated: chip and battery cooling.
Evidence: CANDIDATE; domain-specific equation contract INCOMPLETE; numerical result NOT RUN; literature novelty UNKNOWN; empirical verification NOT DONE.

031. Fluid transport — pore-throat network damage
Existing reference model: Darcy porous-flow law; primary observable: effective permeability.
Observed/latent variable to examine: pore-throat network damage.
Unverified title-derived mechanism hint: network / geometry. Image or reconstruct the evolving contact/connection graph underlying pore-throat network damage; hold aggregate counts fixed while varying graph statistics.
Candidate construction: Represent adjacency/connectivity explicitly; project to a minimal measurable graph statistic and check whether equal aggregate states have different futures.
Garden graph: THING=physical components; TIME=trajectory; SPACE=physical domain; EVENT=state transition; ACTION=controlled perturbation where applicable; AGENCY=experimenter/controller only; RULE=physical conservation; VALUE=declared performance measure; CONTEXT=experimental conditions; CLAIM=testable mechanism. Applicable edges: partOf, dependsOn, contextualizes, derivedFrom, supports/contradicts; use causes only after causal identification.
Seven forms: CONSTRUCT=system; CONTRACT=units/domain; STATE=measured and hidden variables; RELATION=typed dependencies; PROCESS=state evolution; RULE=physical constraints; PROJECTION=baseline observable.
Falsification protocol: Image or reconstruct the evolving contact/connection graph underlying pore-throat network damage; hold aggregate counts fixed while varying graph statistics. Fit extension and strong modern reference model on training experiments; compare blinded held-out predictive likelihood/error under matched complexity and budget. If no robust improvement, reject the increment.
Benefit if validated: filtration and groundwater.
Evidence: CANDIDATE; domain-specific equation contract INCOMPLETE; numerical result NOT RUN; literature novelty UNKNOWN; empirical verification NOT DONE.

032. Fluid transport — wetting-front hysteresis
Existing reference model: Darcy porous-flow law; primary observable: effective permeability.
Observed/latent variable to examine: wetting-front hysteresis.
Unverified title-derived mechanism hint: state switching / hysteresis. Cycle the driving variable in both directions and record branch-dependent response for wetting-front hysteresis; test whether a single-valued constitutive law fails.
Candidate construction: Introduce a branch/state variable with experimentally constrained transition rules; verify return-point and cycling behavior only if observed.
Garden graph: THING=physical components; TIME=trajectory; SPACE=physical domain; EVENT=state transition; ACTION=controlled perturbation where applicable; AGENCY=experimenter/controller only; RULE=physical conservation; VALUE=declared performance measure; CONTEXT=experimental conditions; CLAIM=testable mechanism. Applicable edges: partOf, dependsOn, contextualizes, derivedFrom, supports/contradicts; use causes only after causal identification.
Seven forms: CONSTRUCT=system; CONTRACT=units/domain; STATE=measured and hidden variables; RELATION=typed dependencies; PROCESS=state evolution; RULE=physical constraints; PROJECTION=baseline observable.
Falsification protocol: Cycle the driving variable in both directions and record branch-dependent response for wetting-front hysteresis; test whether a single-valued constitutive law fails. Fit extension and strong modern reference model on training experiments; compare blinded held-out predictive likelihood/error under matched complexity and budget. If no robust improvement, reject the increment.
Benefit if validated: filtration and groundwater.
Evidence: CANDIDATE; domain-specific equation contract INCOMPLETE; numerical result NOT RUN; literature novelty UNKNOWN; empirical verification NOT DONE.

033. Fluid transport — particle clogging topology
Existing reference model: Darcy porous-flow law; primary observable: effective permeability.
Observed/latent variable to examine: particle clogging topology.
Unverified title-derived mechanism hint: network / geometry. Image or reconstruct the evolving contact/connection graph underlying particle clogging topology; hold aggregate counts fixed while varying graph statistics.
Candidate construction: Represent adjacency/connectivity explicitly; project to a minimal measurable graph statistic and check whether equal aggregate states have different futures.
Garden graph: THING=physical components; TIME=trajectory; SPACE=physical domain; EVENT=state transition; ACTION=controlled perturbation where applicable; AGENCY=experimenter/controller only; RULE=physical conservation; VALUE=declared performance measure; CONTEXT=experimental conditions; CLAIM=testable mechanism. Applicable edges: partOf, dependsOn, contextualizes, derivedFrom, supports/contradicts; use causes only after causal identification.
Seven forms: CONSTRUCT=system; CONTRACT=units/domain; STATE=measured and hidden variables; RELATION=typed dependencies; PROCESS=state evolution; RULE=physical constraints; PROJECTION=baseline observable.
Falsification protocol: Image or reconstruct the evolving contact/connection graph underlying particle clogging topology; hold aggregate counts fixed while varying graph statistics. Fit extension and strong modern reference model on training experiments; compare blinded held-out predictive likelihood/error under matched complexity and budget. If no robust improvement, reject the increment.
Benefit if validated: filtration and groundwater.
Evidence: CANDIDATE; domain-specific equation contract INCOMPLETE; numerical result NOT RUN; literature novelty UNKNOWN; empirical verification NOT DONE.

034. Fluid transport — pressure-cycling memory
Existing reference model: Darcy porous-flow law; primary observable: effective permeability.
Observed/latent variable to examine: pressure-cycling memory.
Unverified title-derived mechanism hint: dynamic hidden state / delay. Use matched present-state trajectories with different prior forcing histories for pressure-cycling memory; check whether their subsequent responses diverge.
Candidate construction: Introduce a physically measured relaxing state or convolution kernel; estimate its timescale from perturbation data, not arbitrary fitting.
Garden graph: THING=physical components; TIME=trajectory; SPACE=physical domain; EVENT=state transition; ACTION=controlled perturbation where applicable; AGENCY=experimenter/controller only; RULE=physical conservation; VALUE=declared performance measure; CONTEXT=experimental conditions; CLAIM=testable mechanism. Applicable edges: partOf, dependsOn, contextualizes, derivedFrom, supports/contradicts; use causes only after causal identification.
Seven forms: CONSTRUCT=system; CONTRACT=units/domain; STATE=measured and hidden variables; RELATION=typed dependencies; PROCESS=state evolution; RULE=physical constraints; PROJECTION=baseline observable.
Falsification protocol: Use matched present-state trajectories with different prior forcing histories for pressure-cycling memory; check whether their subsequent responses diverge. Fit extension and strong modern reference model on training experiments; compare blinded held-out predictive likelihood/error under matched complexity and budget. If no robust improvement, reject the increment.
Benefit if validated: filtration and groundwater.
Evidence: CANDIDATE; domain-specific equation contract INCOMPLETE; numerical result NOT RUN; literature novelty UNKNOWN; empirical verification NOT DONE.

035. Fluid transport — multi-scale channel connectivity
Existing reference model: Darcy porous-flow law; primary observable: effective permeability.
Observed/latent variable to examine: multi-scale channel connectivity.
Unverified title-derived mechanism hint: network / geometry. Image or reconstruct the evolving contact/connection graph underlying multi-scale channel connectivity; hold aggregate counts fixed while varying graph statistics.
Candidate construction: Represent adjacency/connectivity explicitly; project to a minimal measurable graph statistic and check whether equal aggregate states have different futures.
Garden graph: THING=physical components; TIME=trajectory; SPACE=physical domain; EVENT=state transition; ACTION=controlled perturbation where applicable; AGENCY=experimenter/controller only; RULE=physical conservation; VALUE=declared performance measure; CONTEXT=experimental conditions; CLAIM=testable mechanism. Applicable edges: partOf, dependsOn, contextualizes, derivedFrom, supports/contradicts; use causes only after causal identification.
Seven forms: CONSTRUCT=system; CONTRACT=units/domain; STATE=measured and hidden variables; RELATION=typed dependencies; PROCESS=state evolution; RULE=physical constraints; PROJECTION=baseline observable.
Falsification protocol: Image or reconstruct the evolving contact/connection graph underlying multi-scale channel connectivity; hold aggregate counts fixed while varying graph statistics. Fit extension and strong modern reference model on training experiments; compare blinded held-out predictive likelihood/error under matched complexity and budget. If no robust improvement, reject the increment.
Benefit if validated: filtration and groundwater.
Evidence: CANDIDATE; domain-specific equation contract INCOMPLETE; numerical result NOT RUN; literature novelty UNKNOWN; empirical verification NOT DONE.

036. Fracture mechanics — overload sequence memory
Existing reference model: Paris crack-growth law; primary observable: crack advance per cycle.
Observed/latent variable to examine: overload sequence memory.
Unverified title-derived mechanism hint: dynamic hidden state / delay. Use matched present-state trajectories with different prior forcing histories for overload sequence memory; check whether their subsequent responses diverge.
Candidate construction: Introduce a physically measured relaxing state or convolution kernel; estimate its timescale from perturbation data, not arbitrary fitting.
Garden graph: THING=physical components; TIME=trajectory; SPACE=physical domain; EVENT=state transition; ACTION=controlled perturbation where applicable; AGENCY=experimenter/controller only; RULE=physical conservation; VALUE=declared performance measure; CONTEXT=experimental conditions; CLAIM=testable mechanism. Applicable edges: partOf, dependsOn, contextualizes, derivedFrom, supports/contradicts; use causes only after causal identification.
Seven forms: CONSTRUCT=system; CONTRACT=units/domain; STATE=measured and hidden variables; RELATION=typed dependencies; PROCESS=state evolution; RULE=physical constraints; PROJECTION=baseline observable.
Falsification protocol: Use matched present-state trajectories with different prior forcing histories for overload sequence memory; check whether their subsequent responses diverge. Fit extension and strong modern reference model on training experiments; compare blinded held-out predictive likelihood/error under matched complexity and budget. If no robust improvement, reject the increment.
Benefit if validated: safer infrastructure.
Evidence: CANDIDATE; domain-specific equation contract INCOMPLETE; numerical result NOT RUN; literature novelty UNKNOWN; empirical verification NOT DONE.

037. Fracture mechanics — microcrack orientation correlations
Existing reference model: Paris crack-growth law; primary observable: crack advance per cycle.
Observed/latent variable to examine: microcrack orientation correlations.
Unverified title-derived mechanism hint: heterogeneity / joint distribution. Measure paired local fields or event-resolved distributions for microcrack orientation correlations; compare joint-data model with independently shuffled marginals.
Candidate construction: Add a measured joint-distribution statistic, not a free coefficient; derive aggregate response by averaging the local law and quantify the residual.
Garden graph: THING=physical components; TIME=trajectory; SPACE=physical domain; EVENT=state transition; ACTION=controlled perturbation where applicable; AGENCY=experimenter/controller only; RULE=physical conservation; VALUE=declared performance measure; CONTEXT=experimental conditions; CLAIM=testable mechanism. Applicable edges: partOf, dependsOn, contextualizes, derivedFrom, supports/contradicts; use causes only after causal identification.
Seven forms: CONSTRUCT=system; CONTRACT=units/domain; STATE=measured and hidden variables; RELATION=typed dependencies; PROCESS=state evolution; RULE=physical constraints; PROJECTION=baseline observable.
Falsification protocol: Measure paired local fields or event-resolved distributions for microcrack orientation correlations; compare joint-data model with independently shuffled marginals. Fit extension and strong modern reference model on training experiments; compare blinded held-out predictive likelihood/error under matched complexity and budget. If no robust improvement, reject the increment.
Benefit if validated: safer infrastructure.
Evidence: CANDIDATE; domain-specific equation contract INCOMPLETE; numerical result NOT RUN; literature novelty UNKNOWN; empirical verification NOT DONE.

038. Fracture mechanics — corrosion-fatigue coupling
Existing reference model: Paris crack-growth law; primary observable: crack advance per cycle.
Observed/latent variable to examine: corrosion-fatigue coupling.
Unverified title-derived mechanism hint: coupled latent kinetics. Measure the candidate intermediate state for corrosion-fatigue coupling during perturbation/recovery; test whether it predicts held-out transients beyond baseline variables.
Candidate construction: Introduce a measurable intermediate and couple it by mass/energy-balanced rate equations; test observability and parameter identifiability.
Garden graph: THING=physical components; TIME=trajectory; SPACE=physical domain; EVENT=state transition; ACTION=controlled perturbation where applicable; AGENCY=experimenter/controller only; RULE=physical conservation; VALUE=declared performance measure; CONTEXT=experimental conditions; CLAIM=testable mechanism. Applicable edges: partOf, dependsOn, contextualizes, derivedFrom, supports/contradicts; use causes only after causal identification.
Seven forms: CONSTRUCT=system; CONTRACT=units/domain; STATE=measured and hidden variables; RELATION=typed dependencies; PROCESS=state evolution; RULE=physical constraints; PROJECTION=baseline observable.
Falsification protocol: Measure the candidate intermediate state for corrosion-fatigue coupling during perturbation/recovery; test whether it predicts held-out transients beyond baseline variables. Fit extension and strong modern reference model on training experiments; compare blinded held-out predictive likelihood/error under matched complexity and budget. If no robust improvement, reject the increment.
Benefit if validated: safer infrastructure.
Evidence: CANDIDATE; domain-specific equation contract INCOMPLETE; numerical result NOT RUN; literature novelty UNKNOWN; empirical verification NOT DONE.

039. Fracture mechanics — grain-boundary connectivity
Existing reference model: Paris crack-growth law; primary observable: crack advance per cycle.
Observed/latent variable to examine: grain-boundary connectivity.
Unverified title-derived mechanism hint: network / geometry. Image or reconstruct the evolving contact/connection graph underlying grain-boundary connectivity; hold aggregate counts fixed while varying graph statistics.
Candidate construction: Represent adjacency/connectivity explicitly; project to a minimal measurable graph statistic and check whether equal aggregate states have different futures.
Garden graph: THING=physical components; TIME=trajectory; SPACE=physical domain; EVENT=state transition; ACTION=controlled perturbation where applicable; AGENCY=experimenter/controller only; RULE=physical conservation; VALUE=declared performance measure; CONTEXT=experimental conditions; CLAIM=testable mechanism. Applicable edges: partOf, dependsOn, contextualizes, derivedFrom, supports/contradicts; use causes only after causal identification.
Seven forms: CONSTRUCT=system; CONTRACT=units/domain; STATE=measured and hidden variables; RELATION=typed dependencies; PROCESS=state evolution; RULE=physical constraints; PROJECTION=baseline observable.
Falsification protocol: Image or reconstruct the evolving contact/connection graph underlying grain-boundary connectivity; hold aggregate counts fixed while varying graph statistics. Fit extension and strong modern reference model on training experiments; compare blinded held-out predictive likelihood/error under matched complexity and budget. If no robust improvement, reject the increment.
Benefit if validated: safer infrastructure.
Evidence: CANDIDATE; domain-specific equation contract INCOMPLETE; numerical result NOT RUN; literature novelty UNKNOWN; empirical verification NOT DONE.

040. Fracture mechanics — residual-stress redistribution
Existing reference model: Paris crack-growth law; primary observable: crack advance per cycle.
Observed/latent variable to examine: residual-stress redistribution.
Unverified title-derived mechanism hint: dynamic hidden state / delay. Use matched present-state trajectories with different prior forcing histories for residual-stress redistribution; check whether their subsequent responses diverge.
Candidate construction: Introduce a physically measured relaxing state or convolution kernel; estimate its timescale from perturbation data, not arbitrary fitting.
Garden graph: THING=physical components; TIME=trajectory; SPACE=physical domain; EVENT=state transition; ACTION=controlled perturbation where applicable; AGENCY=experimenter/controller only; RULE=physical conservation; VALUE=declared performance measure; CONTEXT=experimental conditions; CLAIM=testable mechanism. Applicable edges: partOf, dependsOn, contextualizes, derivedFrom, supports/contradicts; use causes only after causal identification.
Seven forms: CONSTRUCT=system; CONTRACT=units/domain; STATE=measured and hidden variables; RELATION=typed dependencies; PROCESS=state evolution; RULE=physical constraints; PROJECTION=baseline observable.
Falsification protocol: Use matched present-state trajectories with different prior forcing histories for residual-stress redistribution; check whether their subsequent responses diverge. Fit extension and strong modern reference model on training experiments; compare blinded held-out predictive likelihood/error under matched complexity and budget. If no robust improvement, reject the increment.
Benefit if validated: safer infrastructure.
Evidence: CANDIDATE; domain-specific equation contract INCOMPLETE; numerical result NOT RUN; literature novelty UNKNOWN; empirical verification NOT DONE.

041. Turbulence — intermittency-conditioned closure
Existing reference model: Reynolds-averaged closure; primary observable: unresolved stress tensor.
Observed/latent variable to examine: intermittency-conditioned closure.
Unverified title-derived mechanism hint: heterogeneity / joint distribution. Measure paired local fields or event-resolved distributions for intermittency-conditioned closure; compare joint-data model with independently shuffled marginals.
Candidate construction: Add a measured joint-distribution statistic, not a free coefficient; derive aggregate response by averaging the local law and quantify the residual.
Garden graph: THING=physical components; TIME=trajectory; SPACE=physical domain; EVENT=state transition; ACTION=controlled perturbation where applicable; AGENCY=experimenter/controller only; RULE=physical conservation; VALUE=declared performance measure; CONTEXT=experimental conditions; CLAIM=testable mechanism. Applicable edges: partOf, dependsOn, contextualizes, derivedFrom, supports/contradicts; use causes only after causal identification.
Seven forms: CONSTRUCT=system; CONTRACT=units/domain; STATE=measured and hidden variables; RELATION=typed dependencies; PROCESS=state evolution; RULE=physical constraints; PROJECTION=baseline observable.
Falsification protocol: Measure paired local fields or event-resolved distributions for intermittency-conditioned closure; compare joint-data model with independently shuffled marginals. Fit extension and strong modern reference model on training experiments; compare blinded held-out predictive likelihood/error under matched complexity and budget. If no robust improvement, reject the increment.
Benefit if validated: efficient transport and turbines.
Evidence: CANDIDATE; domain-specific equation contract INCOMPLETE; numerical result NOT RUN; literature novelty UNKNOWN; empirical verification NOT DONE.

042. Turbulence — wall-history dependence
Existing reference model: Reynolds-averaged closure; primary observable: unresolved stress tensor.
Observed/latent variable to examine: wall-history dependence.
Unverified title-derived mechanism hint: dynamic hidden state / delay. Use matched present-state trajectories with different prior forcing histories for wall-history dependence; check whether their subsequent responses diverge.
Candidate construction: Introduce a physically measured relaxing state or convolution kernel; estimate its timescale from perturbation data, not arbitrary fitting.
Garden graph: THING=physical components; TIME=trajectory; SPACE=physical domain; EVENT=state transition; ACTION=controlled perturbation where applicable; AGENCY=experimenter/controller only; RULE=physical conservation; VALUE=declared performance measure; CONTEXT=experimental conditions; CLAIM=testable mechanism. Applicable edges: partOf, dependsOn, contextualizes, derivedFrom, supports/contradicts; use causes only after causal identification.
Seven forms: CONSTRUCT=system; CONTRACT=units/domain; STATE=measured and hidden variables; RELATION=typed dependencies; PROCESS=state evolution; RULE=physical constraints; PROJECTION=baseline observable.
Falsification protocol: Use matched present-state trajectories with different prior forcing histories for wall-history dependence; check whether their subsequent responses diverge. Fit extension and strong modern reference model on training experiments; compare blinded held-out predictive likelihood/error under matched complexity and budget. If no robust improvement, reject the increment.
Benefit if validated: efficient transport and turbines.
Evidence: CANDIDATE; domain-specific equation contract INCOMPLETE; numerical result NOT RUN; literature novelty UNKNOWN; empirical verification NOT DONE.

043. Turbulence — coherent-structure topology
Existing reference model: Reynolds-averaged closure; primary observable: unresolved stress tensor.
Observed/latent variable to examine: coherent-structure topology.
Unverified title-derived mechanism hint: network / geometry. Image or reconstruct the evolving contact/connection graph underlying coherent-structure topology; hold aggregate counts fixed while varying graph statistics.
Candidate construction: Represent adjacency/connectivity explicitly; project to a minimal measurable graph statistic and check whether equal aggregate states have different futures.
Garden graph: THING=physical components; TIME=trajectory; SPACE=physical domain; EVENT=state transition; ACTION=controlled perturbation where applicable; AGENCY=experimenter/controller only; RULE=physical conservation; VALUE=declared performance measure; CONTEXT=experimental conditions; CLAIM=testable mechanism. Applicable edges: partOf, dependsOn, contextualizes, derivedFrom, supports/contradicts; use causes only after causal identification.
Seven forms: CONSTRUCT=system; CONTRACT=units/domain; STATE=measured and hidden variables; RELATION=typed dependencies; PROCESS=state evolution; RULE=physical constraints; PROJECTION=baseline observable.
Falsification protocol: Image or reconstruct the evolving contact/connection graph underlying coherent-structure topology; hold aggregate counts fixed while varying graph statistics. Fit extension and strong modern reference model on training experiments; compare blinded held-out predictive likelihood/error under matched complexity and budget. If no robust improvement, reject the increment.
Benefit if validated: efficient transport and turbines.
Evidence: CANDIDATE; domain-specific equation contract INCOMPLETE; numerical result NOT RUN; literature novelty UNKNOWN; empirical verification NOT DONE.

044. Turbulence — pressure-strain lag
Existing reference model: Reynolds-averaged closure; primary observable: unresolved stress tensor.
Observed/latent variable to examine: pressure-strain lag.
Unverified title-derived mechanism hint: dynamic hidden state / delay. Use matched present-state trajectories with different prior forcing histories for pressure-strain lag; check whether their subsequent responses diverge.
Candidate construction: Introduce a physically measured relaxing state or convolution kernel; estimate its timescale from perturbation data, not arbitrary fitting.
Garden graph: THING=physical components; TIME=trajectory; SPACE=physical domain; EVENT=state transition; ACTION=controlled perturbation where applicable; AGENCY=experimenter/controller only; RULE=physical conservation; VALUE=declared performance measure; CONTEXT=experimental conditions; CLAIM=testable mechanism. Applicable edges: partOf, dependsOn, contextualizes, derivedFrom, supports/contradicts; use causes only after causal identification.
Seven forms: CONSTRUCT=system; CONTRACT=units/domain; STATE=measured and hidden variables; RELATION=typed dependencies; PROCESS=state evolution; RULE=physical constraints; PROJECTION=baseline observable.
Falsification protocol: Use matched present-state trajectories with different prior forcing histories for pressure-strain lag; check whether their subsequent responses diverge. Fit extension and strong modern reference model on training experiments; compare blinded held-out predictive likelihood/error under matched complexity and budget. If no robust improvement, reject the increment.
Benefit if validated: efficient transport and turbines.
Evidence: CANDIDATE; domain-specific equation contract INCOMPLETE; numerical result NOT RUN; literature novelty UNKNOWN; empirical verification NOT DONE.

045. Turbulence — cross-scale transfer memory
Existing reference model: Reynolds-averaged closure; primary observable: unresolved stress tensor.
Observed/latent variable to examine: cross-scale transfer memory.
Unverified title-derived mechanism hint: dynamic hidden state / delay. Use matched present-state trajectories with different prior forcing histories for cross-scale transfer memory; check whether their subsequent responses diverge.
Candidate construction: Introduce a physically measured relaxing state or convolution kernel; estimate its timescale from perturbation data, not arbitrary fitting.
Garden graph: THING=physical components; TIME=trajectory; SPACE=physical domain; EVENT=state transition; ACTION=controlled perturbation where applicable; AGENCY=experimenter/controller only; RULE=physical conservation; VALUE=declared performance measure; CONTEXT=experimental conditions; CLAIM=testable mechanism. Applicable edges: partOf, dependsOn, contextualizes, derivedFrom, supports/contradicts; use causes only after causal identification.
Seven forms: CONSTRUCT=system; CONTRACT=units/domain; STATE=measured and hidden variables; RELATION=typed dependencies; PROCESS=state evolution; RULE=physical constraints; PROJECTION=baseline observable.
Falsification protocol: Use matched present-state trajectories with different prior forcing histories for cross-scale transfer memory; check whether their subsequent responses diverge. Fit extension and strong modern reference model on training experiments; compare blinded held-out predictive likelihood/error under matched complexity and budget. If no robust improvement, reject the increment.
Benefit if validated: efficient transport and turbines.
Evidence: CANDIDATE; domain-specific equation contract INCOMPLETE; numerical result NOT RUN; literature novelty UNKNOWN; empirical verification NOT DONE.

046. Solar cells — mobile-ion interface memory
Existing reference model: drift–diffusion photovoltaic model; primary observable: carrier recombination rate.
Observed/latent variable to examine: mobile-ion interface memory.
Unverified title-derived mechanism hint: dynamic hidden state / delay. Use matched present-state trajectories with different prior forcing histories for mobile-ion interface memory; check whether their subsequent responses diverge.
Candidate construction: Introduce a physically measured relaxing state or convolution kernel; estimate its timescale from perturbation data, not arbitrary fitting.
Garden graph: THING=physical components; TIME=trajectory; SPACE=physical domain; EVENT=state transition; ACTION=controlled perturbation where applicable; AGENCY=experimenter/controller only; RULE=physical conservation; VALUE=declared performance measure; CONTEXT=experimental conditions; CLAIM=testable mechanism. Applicable edges: partOf, dependsOn, contextualizes, derivedFrom, supports/contradicts; use causes only after causal identification.
Seven forms: CONSTRUCT=system; CONTRACT=units/domain; STATE=measured and hidden variables; RELATION=typed dependencies; PROCESS=state evolution; RULE=physical constraints; PROJECTION=baseline observable.
Falsification protocol: Use matched present-state trajectories with different prior forcing histories for mobile-ion interface memory; check whether their subsequent responses diverge. Fit extension and strong modern reference model on training experiments; compare blinded held-out predictive likelihood/error under matched complexity and budget. If no robust improvement, reject the increment.
Benefit if validated: longer-lasting solar modules.
Evidence: CANDIDATE; domain-specific equation contract INCOMPLETE; numerical result NOT RUN; literature novelty UNKNOWN; empirical verification NOT DONE.

047. Solar cells — trap-occupancy hysteresis
Existing reference model: drift–diffusion photovoltaic model; primary observable: carrier recombination rate.
Observed/latent variable to examine: trap-occupancy hysteresis.
Unverified title-derived mechanism hint: state switching / hysteresis. Cycle the driving variable in both directions and record branch-dependent response for trap-occupancy hysteresis; test whether a single-valued constitutive law fails.
Candidate construction: Introduce a branch/state variable with experimentally constrained transition rules; verify return-point and cycling behavior only if observed.
Garden graph: THING=physical components; TIME=trajectory; SPACE=physical domain; EVENT=state transition; ACTION=controlled perturbation where applicable; AGENCY=experimenter/controller only; RULE=physical conservation; VALUE=declared performance measure; CONTEXT=experimental conditions; CLAIM=testable mechanism. Applicable edges: partOf, dependsOn, contextualizes, derivedFrom, supports/contradicts; use causes only after causal identification.
Seven forms: CONSTRUCT=system; CONTRACT=units/domain; STATE=measured and hidden variables; RELATION=typed dependencies; PROCESS=state evolution; RULE=physical constraints; PROJECTION=baseline observable.
Falsification protocol: Cycle the driving variable in both directions and record branch-dependent response for trap-occupancy hysteresis; test whether a single-valued constitutive law fails. Fit extension and strong modern reference model on training experiments; compare blinded held-out predictive likelihood/error under matched complexity and budget. If no robust improvement, reject the increment.
Benefit if validated: longer-lasting solar modules.
Evidence: CANDIDATE; domain-specific equation contract INCOMPLETE; numerical result NOT RUN; literature novelty UNKNOWN; empirical verification NOT DONE.

048. Solar cells — grain-boundary topology
Existing reference model: drift–diffusion photovoltaic model; primary observable: carrier recombination rate.
Observed/latent variable to examine: grain-boundary topology.
Unverified title-derived mechanism hint: network / geometry. Image or reconstruct the evolving contact/connection graph underlying grain-boundary topology; hold aggregate counts fixed while varying graph statistics.
Candidate construction: Represent adjacency/connectivity explicitly; project to a minimal measurable graph statistic and check whether equal aggregate states have different futures.
Garden graph: THING=physical components; TIME=trajectory; SPACE=physical domain; EVENT=state transition; ACTION=controlled perturbation where applicable; AGENCY=experimenter/controller only; RULE=physical conservation; VALUE=declared performance measure; CONTEXT=experimental conditions; CLAIM=testable mechanism. Applicable edges: partOf, dependsOn, contextualizes, derivedFrom, supports/contradicts; use causes only after causal identification.
Seven forms: CONSTRUCT=system; CONTRACT=units/domain; STATE=measured and hidden variables; RELATION=typed dependencies; PROCESS=state evolution; RULE=physical constraints; PROJECTION=baseline observable.
Falsification protocol: Image or reconstruct the evolving contact/connection graph underlying grain-boundary topology; hold aggregate counts fixed while varying graph statistics. Fit extension and strong modern reference model on training experiments; compare blinded held-out predictive likelihood/error under matched complexity and budget. If no robust improvement, reject the increment.
Benefit if validated: longer-lasting solar modules.
Evidence: CANDIDATE; domain-specific equation contract INCOMPLETE; numerical result NOT RUN; literature novelty UNKNOWN; empirical verification NOT DONE.

049. Solar cells — humidity-illumination covariance
Existing reference model: drift–diffusion photovoltaic model; primary observable: carrier recombination rate.
Observed/latent variable to examine: humidity-illumination covariance.
Unverified title-derived mechanism hint: heterogeneity / joint distribution. Measure paired local fields or event-resolved distributions for humidity-illumination covariance; compare joint-data model with independently shuffled marginals.
Candidate construction: Add a measured joint-distribution statistic, not a free coefficient; derive aggregate response by averaging the local law and quantify the residual.
Garden graph: THING=physical components; TIME=trajectory; SPACE=physical domain; EVENT=state transition; ACTION=controlled perturbation where applicable; AGENCY=experimenter/controller only; RULE=physical conservation; VALUE=declared performance measure; CONTEXT=experimental conditions; CLAIM=testable mechanism. Applicable edges: partOf, dependsOn, contextualizes, derivedFrom, supports/contradicts; use causes only after causal identification.
Seven forms: CONSTRUCT=system; CONTRACT=units/domain; STATE=measured and hidden variables; RELATION=typed dependencies; PROCESS=state evolution; RULE=physical constraints; PROJECTION=baseline observable.
Falsification protocol: Measure paired local fields or event-resolved distributions for humidity-illumination covariance; compare joint-data model with independently shuffled marginals. Fit extension and strong modern reference model on training experiments; compare blinded held-out predictive likelihood/error under matched complexity and budget. If no robust improvement, reject the increment.
Benefit if validated: longer-lasting solar modules.
Evidence: CANDIDATE; domain-specific equation contract INCOMPLETE; numerical result NOT RUN; literature novelty UNKNOWN; empirical verification NOT DONE.

050. Solar cells — contact ageing kinetics
Existing reference model: drift–diffusion photovoltaic model; primary observable: carrier recombination rate.
Observed/latent variable to examine: contact ageing kinetics.
Unverified title-derived mechanism hint: network / geometry. Image or reconstruct the evolving contact/connection graph underlying contact ageing kinetics; hold aggregate counts fixed while varying graph statistics.
Candidate construction: Represent adjacency/connectivity explicitly; project to a minimal measurable graph statistic and check whether equal aggregate states have different futures.
Garden graph: THING=physical components; TIME=trajectory; SPACE=physical domain; EVENT=state transition; ACTION=controlled perturbation where applicable; AGENCY=experimenter/controller only; RULE=physical conservation; VALUE=declared performance measure; CONTEXT=experimental conditions; CLAIM=testable mechanism. Applicable edges: partOf, dependsOn, contextualizes, derivedFrom, supports/contradicts; use causes only after causal identification.
Seven forms: CONSTRUCT=system; CONTRACT=units/domain; STATE=measured and hidden variables; RELATION=typed dependencies; PROCESS=state evolution; RULE=physical constraints; PROJECTION=baseline observable.
Falsification protocol: Image or reconstruct the evolving contact/connection graph underlying contact ageing kinetics; hold aggregate counts fixed while varying graph statistics. Fit extension and strong modern reference model on training experiments; compare blinded held-out predictive likelihood/error under matched complexity and budget. If no robust improvement, reject the increment.
Benefit if validated: longer-lasting solar modules.
Evidence: CANDIDATE; domain-specific equation contract INCOMPLETE; numerical result NOT RUN; literature novelty UNKNOWN; empirical verification NOT DONE.

051. Photosynthesis — dynamic disorder correlation
Existing reference model: exciton transport / trapping; primary observable: reaction-center capture yield.
Observed/latent variable to examine: dynamic disorder correlation.
Unverified title-derived mechanism hint: heterogeneity / joint distribution. Measure paired local fields or event-resolved distributions for dynamic disorder correlation; compare joint-data model with independently shuffled marginals.
Candidate construction: Add a measured joint-distribution statistic, not a free coefficient; derive aggregate response by averaging the local law and quantify the residual.
Garden graph: THING=physical components; TIME=trajectory; SPACE=physical domain; EVENT=state transition; ACTION=controlled perturbation where applicable; AGENCY=experimenter/controller only; RULE=physical conservation; VALUE=declared performance measure; CONTEXT=experimental conditions; CLAIM=testable mechanism. Applicable edges: partOf, dependsOn, contextualizes, derivedFrom, supports/contradicts; use causes only after causal identification.
Seven forms: CONSTRUCT=system; CONTRACT=units/domain; STATE=measured and hidden variables; RELATION=typed dependencies; PROCESS=state evolution; RULE=physical constraints; PROJECTION=baseline observable.
Falsification protocol: Measure paired local fields or event-resolved distributions for dynamic disorder correlation; compare joint-data model with independently shuffled marginals. Fit extension and strong modern reference model on training experiments; compare blinded held-out predictive likelihood/error under matched complexity and budget. If no robust improvement, reject the increment.
Benefit if validated: artificial photosynthesis.
Evidence: CANDIDATE; domain-specific equation contract INCOMPLETE; numerical result NOT RUN; literature novelty UNKNOWN; empirical verification NOT DONE.

052. Photosynthesis — reaction-center occupancy feedback
Existing reference model: exciton transport / trapping; primary observable: reaction-center capture yield.
Observed/latent variable to examine: reaction-center occupancy feedback.
Unverified title-derived mechanism hint: coupled latent kinetics. Measure the candidate intermediate state for reaction-center occupancy feedback during perturbation/recovery; test whether it predicts held-out transients beyond baseline variables.
Candidate construction: Introduce a measurable intermediate and couple it by mass/energy-balanced rate equations; test observability and parameter identifiability.Garden graph: THING=physical components; TIME=trajectory; SPACE=physical domain; EVENT=state transition; ACTION=controlled perturbation where applicable; AGENCY=experimenter/controller only; RULE=physical conservation; VALUE=declared performance measure; CONTEXT=experimental conditions; CLAIM=testable mechanism. Applicable edges: partOf, dependsOn, contextualizes, derivedFrom, supports/contradicts; use causes only after causal identification.
Seven forms: CONSTRUCT=system; CONTRACT=units/domain; STATE=measured and hidden variables; RELATION=typed dependencies; PROCESS=state evolution; RULE=physical constraints; PROJECTION=baseline observable.
Falsification protocol: Measure the candidate intermediate state for reaction-center occupancy feedback during perturbation/recovery; test whether it predicts held-out transients beyond baseline variables. Fit extension and strong modern reference model on training experiments; compare blinded held-out predictive likelihood/error under matched complexity and budget. If no robust improvement, reject the increment.
Benefit if validated: artificial photosynthesis.
Evidence: CANDIDATE; domain-specific equation contract INCOMPLETE; numerical result NOT RUN; literature novelty UNKNOWN; empirical verification NOT DONE.

053. Photosynthesis — vibrational mode intermittency
Existing reference model: exciton transport / trapping; primary observable: reaction-center capture yield.
Observed/latent variable to examine: vibrational mode intermittency.
Unverified title-derived mechanism hint: heterogeneity / joint distribution. Measure paired local fields or event-resolved distributions for vibrational mode intermittency; compare joint-data model with independently shuffled marginals.
Candidate construction: Add a measured joint-distribution statistic, not a free coefficient; derive aggregate response by averaging the local law and quantify the residual.
Garden graph: THING=physical components; TIME=trajectory; SPACE=physical domain; EVENT=state transition; ACTION=controlled perturbation where applicable; AGENCY=experimenter/controller only; RULE=physical conservation; VALUE=declared performance measure; CONTEXT=experimental conditions; CLAIM=testable mechanism. Applicable edges: partOf, dependsOn, contextualizes, derivedFrom, supports/contradicts; use causes only after causal identification.
Seven forms: CONSTRUCT=system; CONTRACT=units/domain; STATE=measured and hidden variables; RELATION=typed dependencies; PROCESS=state evolution; RULE=physical constraints; PROJECTION=baseline observable.
Falsification protocol: Measure paired local fields or event-resolved distributions for vibrational mode intermittency; compare joint-data model with independently shuffled marginals. Fit extension and strong modern reference model on training experiments; compare blinded held-out predictive likelihood/error under matched complexity and budget. If no robust improvement, reject the increment.
Benefit if validated: artificial photosynthesis.
Evidence: CANDIDATE; domain-specific equation contract INCOMPLETE; numerical result NOT RUN; literature novelty UNKNOWN; empirical verification NOT DONE.

054. Photosynthesis — antenna topology adaptation
Existing reference model: exciton transport / trapping; primary observable: reaction-center capture yield.
Observed/latent variable to examine: antenna topology adaptation.
Unverified title-derived mechanism hint: network / geometry. Image or reconstruct the evolving contact/connection graph underlying antenna topology adaptation; hold aggregate counts fixed while varying graph statistics.
Candidate construction: Represent adjacency/connectivity explicitly; project to a minimal measurable graph statistic and check whether equal aggregate states have different futures.
Garden graph: THING=physical components; TIME=trajectory; SPACE=physical domain; EVENT=state transition; ACTION=controlled perturbation where applicable; AGENCY=experimenter/controller only; RULE=physical conservation; VALUE=declared performance measure; CONTEXT=experimental conditions; CLAIM=testable mechanism. Applicable edges: partOf, dependsOn, contextualizes, derivedFrom, supports/contradicts; use causes only after causal identification.
Seven forms: CONSTRUCT=system; CONTRACT=units/domain; STATE=measured and hidden variables; RELATION=typed dependencies; PROCESS=state evolution; RULE=physical constraints; PROJECTION=baseline observable.
Falsification protocol: Image or reconstruct the evolving contact/connection graph underlying antenna topology adaptation; hold aggregate counts fixed while varying graph statistics. Fit extension and strong modern reference model on training experiments; compare blinded held-out predictive likelihood/error under matched complexity and budget. If no robust improvement, reject the increment.
Benefit if validated: artificial photosynthesis.
Evidence: CANDIDATE; domain-specific equation contract INCOMPLETE; numerical result NOT RUN; literature novelty UNKNOWN; empirical verification NOT DONE.

055. Photosynthesis — nonphotochemical quenching memory
Existing reference model: exciton transport / trapping; primary observable: reaction-center capture yield.
Observed/latent variable to examine: nonphotochemical quenching memory.
Unverified title-derived mechanism hint: dynamic hidden state / delay. Use matched present-state trajectories with different prior forcing histories for nonphotochemical quenching memory; check whether their subsequent responses diverge.
Candidate construction: Introduce a physically measured relaxing state or convolution kernel; estimate its timescale from perturbation data, not arbitrary fitting.
Garden graph: THING=physical components; TIME=trajectory; SPACE=physical domain; EVENT=state transition; ACTION=controlled perturbation where applicable; AGENCY=experimenter/controller only; RULE=physical conservation; VALUE=declared performance measure; CONTEXT=experimental conditions; CLAIM=testable mechanism. Applicable edges: partOf, dependsOn, contextualizes, derivedFrom, supports/contradicts; use causes only after causal identification.
Seven forms: CONSTRUCT=system; CONTRACT=units/domain; STATE=measured and hidden variables; RELATION=typed dependencies; PROCESS=state evolution; RULE=physical constraints; PROJECTION=baseline observable.
Falsification protocol: Use matched present-state trajectories with different prior forcing histories for nonphotochemical quenching memory; check whether their subsequent responses diverge. Fit extension and strong modern reference model on training experiments; compare blinded held-out predictive likelihood/error under matched complexity and budget. If no robust improvement, reject the increment.
Benefit if validated: artificial photosynthesis.
Evidence: CANDIDATE; domain-specific equation contract INCOMPLETE; numerical result NOT RUN; literature novelty UNKNOWN; empirical verification NOT DONE.

056. Neuroscience — phase-lag memory
Existing reference model: neural mass / firing-rate model; primary observable: population response.
Observed/latent variable to examine: phase-lag memory.
Unverified title-derived mechanism hint: state switching / hysteresis. Cycle the driving variable in both directions and record branch-dependent response for phase-lag memory; test whether a single-valued constitutive law fails.
Candidate construction: Introduce a branch/state variable with experimentally constrained transition rules; verify return-point and cycling behavior only if observed.
Garden graph: THING=physical components; TIME=trajectory; SPACE=physical domain; EVENT=state transition; ACTION=controlled perturbation where applicable; AGENCY=experimenter/controller only; RULE=physical conservation; VALUE=declared performance measure; CONTEXT=experimental conditions; CLAIM=testable mechanism. Applicable edges: partOf, dependsOn, contextualizes, derivedFrom, supports/contradicts; use causes only after causal identification.
Seven forms: CONSTRUCT=system; CONTRACT=units/domain; STATE=measured and hidden variables; RELATION=typed dependencies; PROCESS=state evolution; RULE=physical constraints; PROJECTION=baseline observable.
Falsification protocol: Cycle the driving variable in both directions and record branch-dependent response for phase-lag memory; test whether a single-valued constitutive law fails. Fit extension and strong modern reference model on training experiments; compare blinded held-out predictive likelihood/error under matched complexity and budget. If no robust improvement, reject the increment.
Benefit if validated: better neural diagnostics.
Evidence: CANDIDATE; domain-specific equation contract INCOMPLETE; numerical result NOT RUN; literature novelty UNKNOWN; empirical verification NOT DONE.

057. Neuroscience — cell-type interaction topology
Existing reference model: neural mass / firing-rate model; primary observable: population response.
Observed/latent variable to examine: cell-type interaction topology.
Unverified title-derived mechanism hint: network / geometry. Image or reconstruct the evolving contact/connection graph underlying cell-type interaction topology; hold aggregate counts fixed while varying graph statistics.
Candidate construction: Represent adjacency/connectivity explicitly; project to a minimal measurable graph statistic and check whether equal aggregate states have different futures.
Garden graph: THING=physical components; TIME=trajectory; SPACE=physical domain; EVENT=state transition; ACTION=controlled perturbation where applicable; AGENCY=experimenter/controller only; RULE=physical conservation; VALUE=declared performance measure; CONTEXT=experimental conditions; CLAIM=testable mechanism. Applicable edges: partOf, dependsOn, contextualizes, derivedFrom, supports/contradicts; use causes only after causal identification.
Seven forms: CONSTRUCT=system; CONTRACT=units/domain; STATE=measured and hidden variables; RELATION=typed dependencies; PROCESS=state evolution; RULE=physical constraints; PROJECTION=baseline observable.
Falsification protocol: Image or reconstruct the evolving contact/connection graph underlying cell-type interaction topology; hold aggregate counts fixed while varying graph statistics. Fit extension and strong modern reference model on training experiments; compare blinded held-out predictive likelihood/error under matched complexity and budget. If no robust improvement, reject the increment.
Benefit if validated: better neural diagnostics.
Evidence: CANDIDATE; domain-specific equation contract INCOMPLETE; numerical result NOT RUN; literature novelty UNKNOWN; empirical verification NOT DONE.

058. Neuroscience — adaptation-state retention
Existing reference model: neural mass / firing-rate model; primary observable: population response.
Observed/latent variable to examine: adaptation-state retention.
Unverified title-derived mechanism hint: dynamic hidden state / delay. Use matched present-state trajectories with different prior forcing histories for adaptation-state retention; check whether their subsequent responses diverge.
Candidate construction: Introduce a physically measured relaxing state or convolution kernel; estimate its timescale from perturbation data, not arbitrary fitting.
Garden graph: THING=physical components; TIME=trajectory; SPACE=physical domain; EVENT=state transition; ACTION=controlled perturbation where applicable; AGENCY=experimenter/controller only; RULE=physical conservation; VALUE=declared performance measure; CONTEXT=experimental conditions; CLAIM=testable mechanism. Applicable edges: partOf, dependsOn, contextualizes, derivedFrom, supports/contradicts; use causes only after causal identification.
Seven forms: CONSTRUCT=system; CONTRACT=units/domain; STATE=measured and hidden variables; RELATION=typed dependencies; PROCESS=state evolution; RULE=physical constraints; PROJECTION=baseline observable.
Falsification protocol: Use matched present-state trajectories with different prior forcing histories for adaptation-state retention; check whether their subsequent responses diverge. Fit extension and strong modern reference model on training experiments; compare blinded held-out predictive likelihood/error under matched complexity and budget. If no robust improvement, reject the increment.
Benefit if validated: better neural diagnostics.
Evidence: CANDIDATE; domain-specific equation contract INCOMPLETE; numerical result NOT RUN; literature novelty UNKNOWN; empirical verification NOT DONE.

059. Neuroscience — dendritic compartment coupling
Existing reference model: neural mass / firing-rate model; primary observable: population response.
Observed/latent variable to examine: dendritic compartment coupling.
Unverified title-derived mechanism hint: coupled latent kinetics. Measure the candidate intermediate state for dendritic compartment coupling during perturbation/recovery; test whether it predicts held-out transients beyond baseline variables.
Candidate construction: Introduce a measurable intermediate and couple it by mass/energy-balanced rate equations; test observability and parameter identifiability.
Garden graph: THING=physical components; TIME=trajectory; SPACE=physical domain; EVENT=state transition; ACTION=controlled perturbation where applicable; AGENCY=experimenter/controller only; RULE=physical conservation; VALUE=declared performance measure; CONTEXT=experimental conditions; CLAIM=testable mechanism. Applicable edges: partOf, dependsOn, contextualizes, derivedFrom, supports/contradicts; use causes only after causal identification.
Seven forms: CONSTRUCT=system; CONTRACT=units/domain; STATE=measured and hidden variables; RELATION=typed dependencies; PROCESS=state evolution; RULE=physical constraints; PROJECTION=baseline observable.
Falsification protocol: Measure the candidate intermediate state for dendritic compartment coupling during perturbation/recovery; test whether it predicts held-out transients beyond baseline variables. Fit extension and strong modern reference model on training experiments; compare blinded held-out predictive likelihood/error under matched complexity and budget. If no robust improvement, reject the increment.
Benefit if validated: better neural diagnostics.
Evidence: CANDIDATE; domain-specific equation contract INCOMPLETE; numerical result NOT RUN; literature novelty UNKNOWN; empirical verification NOT DONE.

060. Neuroscience — glial metabolic feedback
Existing reference model: neural mass / firing-rate model; primary observable: population response.
Observed/latent variable to examine: glial metabolic feedback.
Unverified title-derived mechanism hint: coupled latent kinetics. Measure the candidate intermediate state for glial metabolic feedback during perturbation/recovery; test whether it predicts held-out transients beyond baseline variables.
Candidate construction: Introduce a measurable intermediate and couple it by mass/energy-balanced rate equations; test observability and parameter identifiability.
Garden graph: THING=physical components; TIME=trajectory; SPACE=physical domain; EVENT=state transition; ACTION=controlled perturbation where applicable; AGENCY=experimenter/controller only; RULE=physical conservation; VALUE=declared performance measure; CONTEXT=experimental conditions; CLAIM=testable mechanism. Applicable edges: partOf, dependsOn, contextualizes, derivedFrom, supports/contradicts; use causes only after causal identification.
Seven forms: CONSTRUCT=system; CONTRACT=units/domain; STATE=measured and hidden variables; RELATION=typed dependencies; PROCESS=state evolution; RULE=physical constraints; PROJECTION=baseline observable.
Falsification protocol: Measure the candidate intermediate state for glial metabolic feedback during perturbation/recovery; test whether it predicts held-out transients beyond baseline variables. Fit extension and strong modern reference model on training experiments; compare blinded held-out predictive likelihood/error under matched complexity and budget. If no robust improvement, reject the increment.
Benefit if validated: better neural diagnostics.
Evidence: CANDIDATE; domain-specific equation contract INCOMPLETE; numerical result NOT RUN; literature novelty UNKNOWN; empirical verification NOT DONE.

061. Pharmacokinetics — transporter saturation history
Existing reference model: compartment PK model; primary observable: tissue drug concentration.
Observed/latent variable to examine: transporter saturation history.
Unverified title-derived mechanism hint: dynamic hidden state / delay. Use matched present-state trajectories with different prior forcing histories for transporter saturation history; check whether their subsequent responses diverge.
Candidate construction: Introduce a physically measured relaxing state or convolution kernel; estimate its timescale from perturbation data, not arbitrary fitting.
Garden graph: THING=physical components; TIME=trajectory; SPACE=physical domain; EVENT=state transition; ACTION=controlled perturbation where applicable; AGENCY=experimenter/controller only; RULE=physical conservation; VALUE=declared performance measure; CONTEXT=experimental conditions; CLAIM=testable mechanism. Applicable edges: partOf, dependsOn, contextualizes, derivedFrom, supports/contradicts; use causes only after causal identification.
Seven forms: CONSTRUCT=system; CONTRACT=units/domain; STATE=measured and hidden variables; RELATION=typed dependencies; PROCESS=state evolution; RULE=physical constraints; PROJECTION=baseline observable.
Falsification protocol: Use matched present-state trajectories with different prior forcing histories for transporter saturation history; check whether their subsequent responses diverge. Fit extension and strong modern reference model on training experiments; compare blinded held-out predictive likelihood/error under matched complexity and budget. If no robust improvement, reject the increment.
Benefit if validated: precision dosing.
Evidence: CANDIDATE; domain-specific equation contract INCOMPLETE; numerical result NOT RUN; literature novelty UNKNOWN; empirical verification NOT DONE.

062. Pharmacokinetics — protein-binding displacement lag
Existing reference model: compartment PK model; primary observable: tissue drug concentration.
Observed/latent variable to examine: protein-binding displacement lag.
Unverified title-derived mechanism hint: dynamic hidden state / delay. Use matched present-state trajectories with different prior forcing histories for protein-binding displacement lag; check whether their subsequent responses diverge.
Candidate construction: Introduce a physically measured relaxing state or convolution kernel; estimate its timescale from perturbation data, not arbitrary fitting.
Garden graph: THING=physical components; TIME=trajectory; SPACE=physical domain; EVENT=state transition; ACTION=controlled perturbation where applicable; AGENCY=experimenter/controller only; RULE=physical conservation; VALUE=declared performance measure; CONTEXT=experimental conditions; CLAIM=testable mechanism. Applicable edges: partOf, dependsOn, contextualizes, derivedFrom, supports/contradicts; use causes only after causal identification.
Seven forms: CONSTRUCT=system; CONTRACT=units/domain; STATE=measured and hidden variables; RELATION=typed dependencies; PROCESS=state evolution; RULE=physical constraints; PROJECTION=baseline observable.
Falsification protocol: Use matched present-state trajectories with different prior forcing histories for protein-binding displacement lag; check whether their subsequent responses diverge. Fit extension and strong modern reference model on training experiments; compare blinded held-out predictive likelihood/error under matched complexity and budget. If no robust improvement, reject the increment.
Benefit if validated: precision dosing.
Evidence: CANDIDATE; domain-specific equation contract INCOMPLETE; numerical result NOT RUN; literature novelty UNKNOWN; empirical verification NOT DONE.

063. Pharmacokinetics — organ perfusion covariance
Existing reference model: compartment PK model; primary observable: tissue drug concentration.
Observed/latent variable to examine: organ perfusion covariance.
Unverified title-derived mechanism hint: heterogeneity / joint distribution. Measure paired local fields or event-resolved distributions for organ perfusion covariance; compare joint-data model with independently shuffled marginals.
Candidate construction: Add a measured joint-distribution statistic, not a free coefficient; derive aggregate response by averaging the local law and quantify the residual.
Garden graph: THING=physical components; TIME=trajectory; SPACE=physical domain; EVENT=state transition; ACTION=controlled perturbation where applicable; AGENCY=experimenter/controller only; RULE=physical conservation; VALUE=declared performance measure; CONTEXT=experimental conditions; CLAIM=testable mechanism. Applicable edges: partOf, dependsOn, contextualizes, derivedFrom, supports/contradicts; use causes only after causal identification.
Seven forms: CONSTRUCT=system; CONTRACT=units/domain; STATE=measured and hidden variables; RELATION=typed dependencies; PROCESS=state evolution; RULE=physical constraints; PROJECTION=baseline observable.
Falsification protocol: Measure paired local fields or event-resolved distributions for organ perfusion covariance; compare joint-data model with independently shuffled marginals. Fit extension and strong modern reference model on training experiments; compare blinded held-out predictive likelihood/error under matched complexity and budget. If no robust improvement, reject the increment.
Benefit if validated: precision dosing.
Evidence: CANDIDATE; domain-specific equation contract INCOMPLETE; numerical result NOT RUN; literature novelty UNKNOWN; empirical verification NOT DONE.

064. Pharmacokinetics — intracellular sequestration memory
Existing reference model: compartment PK model; primary observable: tissue drug concentration.
Observed/latent variable to examine: intracellular sequestration memory.
Unverified title-derived mechanism hint: dynamic hidden state / delay. Use matched present-state trajectories with different prior forcing histories for intracellular sequestration memory; check whether their subsequent responses diverge.
Candidate construction: Introduce a physically measured relaxing state or convolution kernel; estimate its timescale from perturbation data, not arbitrary fitting.
Garden graph: THING=physical components; TIME=trajectory; SPACE=physical domain; EVENT=state transition; ACTION=controlled perturbation where applicable; AGENCY=experimenter/controller only; RULE=physical conservation; VALUE=declared performance measure; CONTEXT=experimental conditions; CLAIM=testable mechanism. Applicable edges: partOf, dependsOn, contextualizes, derivedFrom, supports/contradicts; use causes only after causal identification.
Seven forms: CONSTRUCT=system; CONTRACT=units/domain; STATE=measured and hidden variables; RELATION=typed dependencies; PROCESS=state evolution; RULE=physical constraints; PROJECTION=baseline observable.
Falsification protocol: Use matched present-state trajectories with different prior forcing histories for intracellular sequestration memory; check whether their subsequent responses diverge. Fit extension and strong modern reference model on training experiments; compare blinded held-out predictive likelihood/error under matched complexity and budget. If no robust improvement, reject the increment.
Benefit if validated: precision dosing.
Evidence: CANDIDATE; domain-specific equation contract INCOMPLETE; numerical result NOT RUN; literature novelty UNKNOWN; empirical verification NOT DONE.

065. Pharmacokinetics — circadian clearance state
Existing reference model: compartment PK model; primary observable: tissue drug concentration.
Observed/latent variable to examine: circadian clearance state.
Unverified title-derived mechanism hint: coupled latent kinetics. Measure the candidate intermediate state for circadian clearance state during perturbation/recovery; test whether it predicts held-out transients beyond baseline variables.
Candidate construction: Introduce a measurable intermediate and couple it by mass/energy-balanced rate equations; test observability and parameter identifiability.
Garden graph: THING=physical components; TIME=trajectory; SPACE=physical domain; EVENT=state transition; ACTION=controlled perturbation where applicable; AGENCY=experimenter/controller only; RULE=physical conservation; VALUE=declared performance measure; CONTEXT=experimental conditions; CLAIM=testable mechanism. Applicable edges: partOf, dependsOn, contextualizes, derivedFrom, supports/contradicts; use causes only after causal identification.
Seven forms: CONSTRUCT=system; CONTRACT=units/domain; STATE=measured and hidden variables; RELATION=typed dependencies; PROCESS=state evolution; RULE=physical constraints; PROJECTION=baseline observable.
Falsification protocol: Measure the candidate intermediate state for circadian clearance state during perturbation/recovery; test whether it predicts held-out transients beyond baseline variables. Fit extension and strong modern reference model on training experiments; compare blinded held-out predictive likelihood/error under matched complexity and budget. If no robust improvement, reject the increment.
Benefit if validated: precision dosing.
Evidence: CANDIDATE; domain-specific equation contract INCOMPLETE; numerical result NOT RUN; literature novelty UNKNOWN; empirical verification NOT DONE.

066. Ecology — interaction-network rewiring
Existing reference model: Lotka–Volterra dynamics; primary observable: population growth rate.
Observed/latent variable to examine: interaction-network rewiring.
Unverified title-derived mechanism hint: network / geometry. Image or reconstruct the evolving contact/connection graph underlying interaction-network rewiring; hold aggregate counts fixed while varying graph statistics.
Candidate construction: Represent adjacency/connectivity explicitly; project to a minimal measurable graph statistic and check whether equal aggregate states have different futures.
Garden graph: THING=physical components; TIME=trajectory; SPACE=physical domain; EVENT=state transition; ACTION=controlled perturbation where applicable; AGENCY=experimenter/controller only; RULE=physical conservation; VALUE=declared performance measure; CONTEXT=experimental conditions; CLAIM=testable mechanism. Applicable edges: partOf, dependsOn, contextualizes, derivedFrom, supports/contradicts; use causes only after causal identification.
Seven forms: CONSTRUCT=system; CONTRACT=units/domain; STATE=measured and hidden variables; RELATION=typed dependencies; PROCESS=state evolution; RULE=physical constraints; PROJECTION=baseline observable.
Falsification protocol: Image or reconstruct the evolving contact/connection graph underlying interaction-network rewiring; hold aggregate counts fixed while varying graph statistics. Fit extension and strong modern reference model on training experiments; compare blinded held-out predictive likelihood/error under matched complexity and budget. If no robust improvement, reject the increment.
Benefit if validated: ecosystem resilience.
Evidence: CANDIDATE; domain-specific equation contract INCOMPLETE; numerical result NOT RUN; literature novelty UNKNOWN; empirical verification NOT DONE.

067. Ecology — seed-bank recovery memory
Existing reference model: Lotka–Volterra dynamics; primary observable: population growth rate.
Observed/latent variable to examine: seed-bank recovery memory.
Unverified title-derived mechanism hint: dynamic hidden state / delay. Use matched present-state trajectories with different prior forcing histories for seed-bank recovery memory; check whether their subsequent responses diverge.
Candidate construction: Introduce a physically measured relaxing state or convolution kernel; estimate its timescale from perturbation data, not arbitrary fitting.
Garden graph: THING=physical components; TIME=trajectory; SPACE=physical domain; EVENT=state transition; ACTION=controlled perturbation where applicable; AGENCY=experimenter/controller only; RULE=physical conservation; VALUE=declared performance measure; CONTEXT=experimental conditions; CLAIM=testable mechanism. Applicable edges: partOf, dependsOn, contextualizes, derivedFrom, supports/contradicts; use causes only after causal identification.
Seven forms: CONSTRUCT=system; CONTRACT=units/domain; STATE=measured and hidden variables; RELATION=typed dependencies; PROCESS=state evolution; RULE=physical constraints; PROJECTION=baseline observable.
Falsification protocol: Use matched present-state trajectories with different prior forcing histories for seed-bank recovery memory; check whether their subsequent responses diverge. Fit extension and strong modern reference model on training experiments; compare blinded held-out predictive likelihood/error under matched complexity and budget. If no robust improvement, reject the increment.
Benefit if validated: ecosystem resilience.
Evidence: CANDIDATE; domain-specific equation contract INCOMPLETE; numerical result NOT RUN; literature novelty UNKNOWN; empirical verification NOT DONE.

068. Ecology — spatial refuge connectivity
Existing reference model: Lotka–Volterra dynamics; primary observable: population growth rate.
Observed/latent variable to examine: spatial refuge connectivity.
Unverified title-derived mechanism hint: network / geometry. Image or reconstruct the evolving contact/connection graph underlying spatial refuge connectivity; hold aggregate counts fixed while varying graph statistics.
Candidate construction: Represent adjacency/connectivity explicitly; project to a minimal measurable graph statistic and check whether equal aggregate states have different futures.
Garden graph: THING=physical components; TIME=trajectory; SPACE=physical domain; EVENT=state transition; ACTION=controlled perturbation where applicable; AGENCY=experimenter/controller only; RULE=physical conservation; VALUE=declared performance measure; CONTEXT=experimental conditions; CLAIM=testable mechanism. Applicable edges: partOf, dependsOn, contextualizes, derivedFrom, supports/contradicts; use causes only after causal identification.
Seven forms: CONSTRUCT=system; CONTRACT=units/domain; STATE=measured and hidden variables; RELATION=typed dependencies; PROCESS=state evolution; RULE=physical constraints; PROJECTION=baseline observable.
Falsification protocol: Image or reconstruct the evolving contact/connection graph underlying spatial refuge connectivity; hold aggregate counts fixed while varying graph statistics. Fit extension and strong modern reference model on training experiments; compare blinded held-out predictive likelihood/error under matched complexity and budget. If no robust improvement, reject the increment.
Benefit if validated: ecosystem resilience.
Evidence: CANDIDATE; domain-specific equation contract INCOMPLETE; numerical result NOT RUN; literature novelty UNKNOWN; empirical verification NOT DONE.

069. Ecology — predator-switching lag
Existing reference model: Lotka–Volterra dynamics; primary observable: population growth rate.
Observed/latent variable to examine: predator-switching lag.
Unverified title-derived mechanism hint: state switching / hysteresis. Cycle the driving variable in both directions and record branch-dependent response for predator-switching lag; test whether a single-valued constitutive law fails.
Candidate construction: Introduce a branch/state variable with experimentally constrained transition rules; verify return-point and cycling behavior only if observed.
Garden graph: THING=physical components; TIME=trajectory; SPACE=physical domain; EVENT=state transition; ACTION=controlled perturbation where applicable; AGENCY=experimenter/controller only; RULE=physical conservation; VALUE=declared performance measure; CONTEXT=experimental conditions; CLAIM=testable mechanism. Applicable edges: partOf, dependsOn, contextualizes, derivedFrom, supports/contradicts; use causes only after causal identification.
Seven forms: CONSTRUCT=system; CONTRACT=units/domain; STATE=measured and hidden variables; RELATION=typed dependencies; PROCESS=state evolution; RULE=physical constraints; PROJECTION=baseline observable.
Falsification protocol: Cycle the driving variable in both directions and record branch-dependent response for predator-switching lag; test whether a single-valued constitutive law fails. Fit extension and strong modern reference model on training experiments; compare blinded held-out predictive likelihood/error under matched complexity and budget. If no robust improvement, reject the increment.
Benefit if validated: ecosystem resilience.
Evidence: CANDIDATE; domain-specific equation contract INCOMPLETE; numerical result NOT RUN; literature novelty UNKNOWN; empirical verification NOT DONE.

070. Ecology — nutrient feedback delay
Existing reference model: Lotka–Volterra dynamics; primary observable: population growth rate.
Observed/latent variable to examine: nutrient feedback delay.
Unverified title-derived mechanism hint: dynamic hidden state / delay. Use matched present-state trajectories with different prior forcing histories for nutrient feedback delay; check whether their subsequent responses diverge.
Candidate construction: Introduce a physically measured relaxing state or convolution kernel; estimate its timescale from perturbation data, not arbitrary fitting.
Garden graph: THING=physical components; TIME=trajectory; SPACE=physical domain; EVENT=state transition; ACTION=controlled perturbation where applicable; AGENCY=experimenter/controller only; RULE=physical conservation; VALUE=declared performance measure; CONTEXT=experimental conditions; CLAIM=testable mechanism. Applicable edges: partOf, dependsOn, contextualizes, derivedFrom, supports/contradicts; use causes only after causal identification.
Seven forms: CONSTRUCT=system; CONTRACT=units/domain; STATE=measured and hidden variables; RELATION=typed dependencies; PROCESS=state evolution; RULE=physical constraints; PROJECTION=baseline observable.
Falsification protocol: Use matched present-state trajectories with different prior forcing histories for nutrient feedback delay; check whether their subsequent responses diverge. Fit extension and strong modern reference model on training experiments; compare blinded held-out predictive likelihood/error under matched complexity and budget. If no robust improvement, reject the increment.
Benefit if validated: ecosystem resilience.
Evidence: CANDIDATE; domain-specific equation contract INCOMPLETE; numerical result NOT RUN; literature novelty UNKNOWN; empirical verification NOT DONE.

071. Epidemiology — contact-network memory
Existing reference model: SIR / SEIR compartments; primary observable: incidence rate.
Observed/latent variable to examine: contact-network memory.
Unverified title-derived mechanism hint: network / geometry. Image or reconstruct the evolving contact/connection graph underlying contact-network memory; hold aggregate counts fixed while varying graph statistics.
Candidate construction: Represent adjacency/connectivity explicitly; project to a minimal measurable graph statistic and check whether equal aggregate states have different futures.
Garden graph: THING=physical components; TIME=trajectory; SPACE=physical domain; EVENT=state transition; ACTION=controlled perturbation where applicable; AGENCY=experimenter/controller only; RULE=physical conservation; VALUE=declared performance measure; CONTEXT=experimental conditions; CLAIM=testable mechanism. Applicable edges: partOf, dependsOn, contextualizes, derivedFrom, supports/contradicts; use causes only after causal identification.
Seven forms: CONSTRUCT=system; CONTRACT=units/domain; STATE=measured and hidden variables; RELATION=typed dependencies; PROCESS=state evolution; RULE=physical constraints; PROJECTION=baseline observable.
Falsification protocol: Image or reconstruct the evolving contact/connection graph underlying contact-network memory; hold aggregate counts fixed while varying graph statistics. Fit extension and strong modern reference model on training experiments; compare blinded held-out predictive likelihood/error under matched complexity and budget. If no robust improvement, reject the increment.
Benefit if validated: more accurate outbreak forecasts.
Evidence: CANDIDATE; domain-specific equation contract INCOMPLETE; numerical result NOT RUN; literature novelty UNKNOWN; empirical verification NOT DONE.

072. Epidemiology — infection-age infectiousness
Existing reference model: SIR / SEIR compartments; primary observable: incidence rate.
Observed/latent variable to examine: infection-age infectiousness.
Unverified title-derived mechanism hint: mechanism unresolved — requires domain diagnostics. Collect perturbation-response measurements for infection-age infectiousness; identify residual structure before selecting an extension.
Candidate construction: Do not choose a mechanism before observing structured residuals; record an unresolved research question.
Garden graph: THING=physical components; TIME=trajectory; SPACE=physical domain; EVENT=state transition; ACTION=controlled perturbation where applicable; AGENCY=experimenter/controller only; RULE=physical conservation; VALUE=declared performance measure; CONTEXT=experimental conditions; CLAIM=testable mechanism. Applicable edges: partOf, dependsOn, contextualizes, derivedFrom, supports/contradicts; use causes only after causal identification.
Seven forms: CONSTRUCT=system; CONTRACT=units/domain; STATE=measured and hidden variables; RELATION=typed dependencies; PROCESS=state evolution; RULE=physical constraints; PROJECTION=baseline observable.
Falsification protocol: Collect perturbation-response measurements for infection-age infectiousness; identify residual structure before selecting an extension. Fit extension and strong modern reference model on training experiments; compare blinded held-out predictive likelihood/error under matched complexity and budget. If no robust improvement, reject the increment.
Benefit if validated: more accurate outbreak forecasts.
Evidence: CANDIDATE; domain-specific equation contract INCOMPLETE; numerical result NOT RUN; literature novelty UNKNOWN; empirical verification NOT DONE.

073. Epidemiology — regional mixing covariance
Existing reference model: SIR / SEIR compartments; primary observable: incidence rate.
Observed/latent variable to examine: regional mixing covariance.
Unverified title-derived mechanism hint: heterogeneity / joint distribution. Measure paired local fields or event-resolved distributions for regional mixing covariance; compare joint-data model with independently shuffled marginals.
Candidate construction: Add a measured joint-distribution statistic, not a free coefficient; derive aggregate response by averaging the local law and quantify the residual.
Garden graph: THING=physical components; TIME=trajectory; SPACE=physical domain; EVENT=state transition; ACTION=controlled perturbation where applicable; AGENCY=experimenter/controller only; RULE=physical conservation; VALUE=declared performance measure; CONTEXT=experimental conditions; CLAIM=testable mechanism. Applicable edges: partOf, dependsOn, contextualizes, derivedFrom, supports/contradicts; use causes only after causal identification.
Seven forms: CONSTRUCT=system; CONTRACT=units/domain; STATE=measured and hidden variables; RELATION=typed dependencies; PROCESS=state evolution; RULE=physical constraints; PROJECTION=baseline observable.
Falsification protocol: Measure paired local fields or event-resolved distributions for regional mixing covariance; compare joint-data model with independently shuffled marginals. Fit extension and strong modern reference model on training experiments; compare blinded held-out predictive likelihood/error under matched complexity and budget. If no robust improvement, reject the increment.
Benefit if validated: more accurate outbreak forecasts.
Evidence: CANDIDATE; domain-specific equation contract INCOMPLETE; numerical result NOT RUN; literature novelty UNKNOWN; empirical verification NOT DONE.

074. Epidemiology — behavioral response lag
Existing reference model: SIR / SEIR compartments; primary observable: incidence rate.
Observed/latent variable to examine: behavioral response lag.
Unverified title-derived mechanism hint: dynamic hidden state / delay. Use matched present-state trajectories with different prior forcing histories for behavioral response lag; check whether their subsequent responses diverge.
Candidate construction: Introduce a physically measured relaxing state or convolution kernel; estimate its timescale from perturbation data, not arbitrary fitting.
Garden graph: THING=physical components; TIME=trajectory; SPACE=physical domain; EVENT=state transition; ACTION=controlled perturbation where applicable; AGENCY=experimenter/controller only; RULE=physical conservation; VALUE=declared performance measure; CONTEXT=experimental conditions; CLAIM=testable mechanism. Applicable edges: partOf, dependsOn, contextualizes, derivedFrom, supports/contradicts; use causes only after causal identification.
Seven forms: CONSTRUCT=system; CONTRACT=units/domain; STATE=measured and hidden variables; RELATION=typed dependencies; PROCESS=state evolution; RULE=physical constraints; PROJECTION=baseline observable.
Falsification protocol: Use matched present-state trajectories with different prior forcing histories for behavioral response lag; check whether their subsequent responses diverge. Fit extension and strong modern reference model on training experiments; compare blinded held-out predictive likelihood/error under matched complexity and budget. If no robust improvement, reject the increment.
Benefit if validated: more accurate outbreak forecasts.
Evidence: CANDIDATE; domain-specific equation contract INCOMPLETE; numerical result NOT RUN; literature novelty UNKNOWN; empirical verification NOT DONE.

075. Epidemiology — immunity heterogeneity topology
Existing reference model: SIR / SEIR compartments; primary observable: incidence rate.
Observed/latent variable to examine: immunity heterogeneity topology.
Unverified title-derived mechanism hint: heterogeneity / joint distribution. Measure paired local fields or event-resolved distributions for immunity heterogeneity topology; compare joint-data model with independently shuffled marginals.
Candidate construction: Add a measured joint-distribution statistic, not a free coefficient; derive aggregate response by averaging the local law and quantify the residual.
Garden graph: THING=physical components; TIME=trajectory; SPACE=physical domain; EVENT=state transition; ACTION=controlled perturbation where applicable; AGENCY=experimenter/controller only; RULE=physical conservation; VALUE=declared performance measure; CONTEXT=experimental conditions; CLAIM=testable mechanism. Applicable edges: partOf, dependsOn, contextualizes, derivedFrom, supports/contradicts; use causes only after causal identification.
Seven forms: CONSTRUCT=system; CONTRACT=units/domain; STATE=measured and hidden variables; RELATION=typed dependencies; PROCESS=state evolution; RULE=physical constraints; PROJECTION=baseline observable.
Falsification protocol: Measure paired local fields or event-resolved distributions for immunity heterogeneity topology; compare joint-data model with independently shuffled marginals. Fit extension and strong modern reference model on training experiments; compare blinded held-out predictive likelihood/error under matched complexity and budget. If no robust improvement, reject the increment.
Benefit if validated: more accurate outbreak forecasts.
Evidence: CANDIDATE; domain-specific equation contract INCOMPLETE; numerical result NOT RUN; literature novelty UNKNOWN; empirical verification NOT DONE.

076. Soil biogeochemistry — mineral-accessibility topology
Existing reference model: soil carbon pool models; primary observable: carbon mineralization rate.
Observed/latent variable to examine: mineral-accessibility topology.
Unverified title-derived mechanism hint: network / geometry. Image or reconstruct the evolving contact/connection graph underlying mineral-accessibility topology; hold aggregate counts fixed while varying graph statistics.
Candidate construction: Represent adjacency/connectivity explicitly; project to a minimal measurable graph statistic and check whether equal aggregate states have different futures.
Garden graph: THING=physical components; TIME=trajectory; SPACE=physical domain; EVENT=state transition; ACTION=controlled perturbation where applicable; AGENCY=experimenter/controller only; RULE=physical conservation; VALUE=declared performance measure; CONTEXT=experimental conditions; CLAIM=testable mechanism. Applicable edges: partOf, dependsOn, contextualizes, derivedFrom, supports/contradicts; use causes only after causal identification.
Seven forms: CONSTRUCT=system; CONTRACT=units/domain; STATE=measured and hidden variables; RELATION=typed dependencies; PROCESS=state evolution; RULE=physical constraints; PROJECTION=baseline observable.
Falsification protocol: Image or reconstruct the evolving contact/connection graph underlying mineral-accessibility topology; hold aggregate counts fixed while varying graph statistics. Fit extension and strong modern reference model on training experiments; compare blinded held-out predictive likelihood/error under matched complexity and budget. If no robust improvement, reject the increment.
Benefit if validated: soil management and climate.
Evidence: CANDIDATE; domain-specific equation contract INCOMPLETE; numerical result NOT RUN; literature novelty UNKNOWN; empirical verification NOT DONE.

077. Soil biogeochemistry — wet-dry pulse memory
Existing reference model: soil carbon pool models; primary observable: carbon mineralization rate.
Observed/latent variable to examine: wet-dry pulse memory.
Unverified title-derived mechanism hint: dynamic hidden state / delay. Use matched present-state trajectories with different prior forcing histories for wet-dry pulse memory; check whether their subsequent responses diverge.
Candidate construction: Introduce a physically measured relaxing state or convolution kernel; estimate its timescale from perturbation data, not arbitrary fitting.
Garden graph: THING=physical components; TIME=trajectory; SPACE=physical domain; EVENT=state transition; ACTION=controlled perturbation where applicable; AGENCY=experimenter/controller only; RULE=physical conservation; VALUE=declared performance measure; CONTEXT=experimental conditions; CLAIM=testable mechanism. Applicable edges: partOf, dependsOn, contextualizes, derivedFrom, supports/contradicts; use causes only after causal identification.
Seven forms: CONSTRUCT=system; CONTRACT=units/domain; STATE=measured and hidden variables; RELATION=typed dependencies; PROCESS=state evolution; RULE=physical constraints; PROJECTION=baseline observable.
Falsification protocol: Use matched present-state trajectories with different prior forcing histories for wet-dry pulse memory; check whether their subsequent responses diverge. Fit extension and strong modern reference model on training experiments; compare blinded held-out predictive likelihood/error under matched complexity and budget. If no robust improvement, reject the increment.
Benefit if validated: soil management and climate.
Evidence: CANDIDATE; domain-specific equation contract INCOMPLETE; numerical result NOT RUN; literature novelty UNKNOWN; empirical verification NOT DONE.

078. Soil biogeochemistry — microbial enzyme allocation
Existing reference model: soil carbon pool models; primary observable: carbon mineralization rate.
Observed/latent variable to examine: microbial enzyme allocation.
Unverified title-derived mechanism hint: coupled latent kinetics. Measure the candidate intermediate state for microbial enzyme allocation during perturbation/recovery; test whether it predicts held-out transients beyond baseline variables.
Candidate construction: Introduce a measurable intermediate and couple it by mass/energy-balanced rate equations; test observability and parameter identifiability.
Garden graph: THING=physical components; TIME=trajectory; SPACE=physical domain; EVENT=state transition; ACTION=controlled perturbation where applicable; AGENCY=experimenter/controller only; RULE=physical conservation; VALUE=declared performance measure; CONTEXT=experimental conditions; CLAIM=testable mechanism. Applicable edges: partOf, dependsOn, contextualizes, derivedFrom, supports/contradicts; use causes only after causal identification.
Seven forms: CONSTRUCT=system; CONTRACT=units/domain; STATE=measured and hidden variables; RELATION=typed dependencies; PROCESS=state evolution; RULE=physical constraints; PROJECTION=baseline observable.
Falsification protocol: Measure the candidate intermediate state for microbial enzyme allocation during perturbation/recovery; test whether it predicts held-out transients beyond baseline variables. Fit extension and strong modern reference model on training experiments; compare blinded held-out predictive likelihood/error under matched complexity and budget. If no robust improvement, reject the increment.
Benefit if validated: soil management and climate.
Evidence: CANDIDATE; domain-specific equation contract INCOMPLETE; numerical result NOT RUN; literature novelty UNKNOWN; empirical verification NOT DONE.

079. Soil biogeochemistry — aggregate fragmentation
Existing reference model: soil carbon pool models; primary observable: carbon mineralization rate.
Observed/latent variable to examine: aggregate fragmentation.
Unverified title-derived mechanism hint: network / geometry. Image or reconstruct the evolving contact/connection graph underlying aggregate fragmentation; hold aggregate counts fixed while varying graph statistics.
Candidate construction: Represent adjacency/connectivity explicitly; project to a minimal measurable graph statistic and check whether equal aggregate states have different futures.
Garden graph: THING=physical components; TIME=trajectory; SPACE=physical domain; EVENT=state transition; ACTION=controlled perturbation where applicable; AGENCY=experimenter/controller only; RULE=physical conservation; VALUE=declared performance measure; CONTEXT=experimental conditions; CLAIM=testable mechanism. Applicable edges: partOf, dependsOn, contextualizes, derivedFrom, supports/contradicts; use causes only after causal identification.
Seven forms: CONSTRUCT=system; CONTRACT=units/domain; STATE=measured and hidden variables; RELATION=typed dependencies; PROCESS=state evolution; RULE=physical constraints; PROJECTION=baseline observable.
Falsification protocol: Image or reconstruct the evolving contact/connection graph underlying aggregate fragmentation; hold aggregate counts fixed while varying graph statistics. Fit extension and strong modern reference model on training experiments; compare blinded held-out predictive likelihood/error under matched complexity and budget. If no robust improvement, reject the increment.
Benefit if validated: soil management and climate.
Evidence: CANDIDATE; domain-specific equation contract INCOMPLETE; numerical result NOT RUN; literature novelty UNKNOWN; empirical verification NOT DONE.

080. Soil biogeochemistry — root-exudate spatial coupling
Existing reference model: soil carbon pool models; primary observable: carbon mineralization rate.
Observed/latent variable to examine: root-exudate spatial coupling.
Unverified title-derived mechanism hint: coupled latent kinetics. Measure the candidate intermediate state for root-exudate spatial coupling during perturbation/recovery; test whether it predicts held-out transients beyond baseline variables.
Candidate construction: Introduce a measurable intermediate and couple it by mass/energy-balanced rate equations; test observability and parameter identifiability.
Garden graph: THING=physical components; TIME=trajectory; SPACE=physical domain; EVENT=state transition; ACTION=controlled perturbation where applicable; AGENCY=experimenter/controller only; RULE=physical conservation; VALUE=declared performance measure; CONTEXT=experimental conditions; CLAIM=testable mechanism. Applicable edges: partOf, dependsOn, contextualizes, derivedFrom, supports/contradicts; use causes only after causal identification.
Seven forms: CONSTRUCT=system; CONTRACT=units/domain; STATE=measured and hidden variables; RELATION=typed dependencies; PROCESS=state evolution; RULE=physical constraints; PROJECTION=baseline observable.
Falsification protocol: Measure the candidate intermediate state for root-exudate spatial coupling during perturbation/recovery; test whether it predicts held-out transients beyond baseline variables. Fit extension and strong modern reference model on training experiments; compare blinded held-out predictive likelihood/error under matched complexity and budget. If no robust improvement, reject the increment.
Benefit if validated: soil management and climate.
Evidence: CANDIDATE; domain-specific equation contract INCOMPLETE; numerical result NOT RUN; literature novelty UNKNOWN; empirical verification NOT DONE.

081. Climate dynamics — ocean vertical heat memory
Existing reference model: energy-balance / ocean uptake; primary observable: heat uptake.
Observed/latent variable to examine: ocean vertical heat memory.
Unverified title-derived mechanism hint: dynamic hidden state / delay. Use matched present-state trajectories with different prior forcing histories for ocean vertical heat memory; check whether their subsequent responses diverge.
Candidate construction: Introduce a physically measured relaxing state or convolution kernel; estimate its timescale from perturbation data, not arbitrary fitting.
Garden graph: THING=physical components; TIME=trajectory; SPACE=physical domain; EVENT=state transition; ACTION=controlled perturbation where applicable; AGENCY=experimenter/controller only; RULE=physical conservation; VALUE=declared performance measure; CONTEXT=experimental conditions; CLAIM=testable mechanism. Applicable edges: partOf, dependsOn, contextualizes, derivedFrom, supports/contradicts; use causes only after causal identification.
Seven forms: CONSTRUCT=system; CONTRACT=units/domain; STATE=measured and hidden variables; RELATION=typed dependencies; PROCESS=state evolution; RULE=physical constraints; PROJECTION=baseline observable.
Falsification protocol: Use matched present-state trajectories with different prior forcing histories for ocean vertical heat memory; check whether their subsequent responses diverge. Fit extension and strong modern reference model on training experiments; compare blinded held-out predictive likelihood/error under matched complexity and budget. If no robust improvement, reject the increment.
Benefit if validated: better adaptation planning.
Evidence: CANDIDATE; domain-specific equation contract INCOMPLETE; numerical result NOT RUN; literature novelty UNKNOWN; empirical verification NOT DONE.

082. Climate dynamics — cloud-regime transition persistence
Existing reference model: energy-balance / ocean uptake; primary observable: heat uptake.
Observed/latent variable to examine: cloud-regime transition persistence.
Unverified title-derived mechanism hint: state switching / hysteresis. Cycle the driving variable in both directions and record branch-dependent response for cloud-regime transition persistence; test whether a single-valued constitutive law fails.
Candidate construction: Introduce a branch/state variable with experimentally constrained transition rules; verify return-point and cycling behavior only if observed.
Garden graph: THING=physical components; TIME=trajectory; SPACE=physical domain; EVENT=state transition; ACTION=controlled perturbation where applicable; AGENCY=experimenter/controller only; RULE=physical conservation; VALUE=declared performance measure; CONTEXT=experimental conditions; CLAIM=testable mechanism. Applicable edges: partOf, dependsOn, contextualizes, derivedFrom, supports/contradicts; use causes only after causal identification.
Seven forms: CONSTRUCT=system; CONTRACT=units/domain; STATE=measured and hidden variables; RELATION=typed dependencies; PROCESS=state evolution; RULE=physical constraints; PROJECTION=baseline observable.
Falsification protocol: Cycle the driving variable in both directions and record branch-dependent response for cloud-regime transition persistence; test whether a single-valued constitutive law fails. Fit extension and strong modern reference model on training experiments; compare blinded held-out predictive likelihood/error under matched complexity and budget. If no robust improvement, reject the increment.
Benefit if validated: better adaptation planning.
Evidence: CANDIDATE; domain-specific equation contract INCOMPLETE; numerical result NOT RUN; literature novelty UNKNOWN; empirical verification NOT DONE.

083. Climate dynamics — land-moisture feedback
Existing reference model: energy-balance / ocean uptake; primary observable: heat uptake.
Observed/latent variable to examine: land-moisture feedback.
Unverified title-derived mechanism hint: coupled latent kinetics. Measure the candidate intermediate state for land-moisture feedback during perturbation/recovery; test whether it predicts held-out transients beyond baseline variables.
Candidate construction: Introduce a measurable intermediate and couple it by mass/energy-balanced rate equations; test observability and parameter identifiability.
Garden graph: THING=physical components; TIME=trajectory; SPACE=physical domain; EVENT=state transition; ACTION=controlled perturbation where applicable; AGENCY=experimenter/controller only; RULE=physical conservation; VALUE=declared performance measure; CONTEXT=experimental conditions; CLAIM=testable mechanism. Applicable edges: partOf, dependsOn, contextualizes, derivedFrom, supports/contradicts; use causes only after causal identification.
Seven forms: CONSTRUCT=system; CONTRACT=units/domain; STATE=measured and hidden variables; RELATION=typed dependencies; PROCESS=state evolution; RULE=physical constraints; PROJECTION=baseline observable.
Falsification protocol: Measure the candidate intermediate state for land-moisture feedback during perturbation/recovery; test whether it predicts held-out transients beyond baseline variables. Fit extension and strong modern reference model on training experiments; compare blinded held-out predictive likelihood/error under matched complexity and budget. If no robust improvement, reject the increment.
Benefit if validated: better adaptation planning.
Evidence: CANDIDATE; domain-specific equation contract INCOMPLETE; numerical result NOT RUN; literature novelty UNKNOWN; empirical verification NOT DONE.

084. Climate dynamics — aerosol-pattern covariance
Existing reference model: energy-balance / ocean uptake; primary observable: heat uptake.
Observed/latent variable to examine: aerosol-pattern covariance.
Unverified title-derived mechanism hint: heterogeneity / joint distribution. Measure paired local fields or event-resolved distributions for aerosol-pattern covariance; compare joint-data model with independently shuffled marginals.
Candidate construction: Add a measured joint-distribution statistic, not a free coefficient; derive aggregate response by averaging the local law and quantify the residual.
Garden graph: THING=physical components; TIME=trajectory; SPACE=physical domain; EVENT=state transition; ACTION=controlled perturbation where applicable; AGENCY=experimenter/controller only; RULE=physical conservation; VALUE=declared performance measure; CONTEXT=experimental conditions; CLAIM=testable mechanism. Applicable edges: partOf, dependsOn, contextualizes, derivedFrom, supports/contradicts; use causes only after causal identification.
Seven forms: CONSTRUCT=system; CONTRACT=units/domain; STATE=measured and hidden variables; RELATION=typed dependencies; PROCESS=state evolution; RULE=physical constraints; PROJECTION=baseline observable.
Falsification protocol: Measure paired local fields or event-resolved distributions for aerosol-pattern covariance; compare joint-data model with independently shuffled marginals. Fit extension and strong modern reference model on training experiments; compare blinded held-out predictive likelihood/error under matched complexity and budget. If no robust improvement, reject the increment.
Benefit if validated: better adaptation planning.
Evidence: CANDIDATE; domain-specific equation contract INCOMPLETE; numerical result NOT RUN; literature novelty UNKNOWN; empirical verification NOT DONE.

085. Climate dynamics — ice-albedo spatial connectivity
Existing reference model: energy-balance / ocean uptake; primary observable: heat uptake.
Observed/latent variable to examine: ice-albedo spatial connectivity.
Unverified title-derived mechanism hint: network / geometry. Image or reconstruct the evolving contact/connection graph underlying ice-albedo spatial connectivity; hold aggregate counts fixed while varying graph statistics.
Candidate construction: Represent adjacency/connectivity explicitly; project to a minimal measurable graph statistic and check whether equal aggregate states have different futures.
Garden graph: THING=physical components; TIME=trajectory; SPACE=physical domain; EVENT=state transition; ACTION=controlled perturbation where applicable; AGENCY=experimenter/controller only; RULE=physical conservation; VALUE=declared performance measure; CONTEXT=experimental conditions; CLAIM=testable mechanism. Applicable edges: partOf, dependsOn, contextualizes, derivedFrom, supports/contradicts; use causes only after causal identification.
Seven forms: CONSTRUCT=system; CONTRACT=units/domain; STATE=measured and hidden variables; RELATION=typed dependencies; PROCESS=state evolution; RULE=physical constraints; PROJECTION=baseline observable.
Falsification protocol: Image or reconstruct the evolving contact/connection graph underlying ice-albedo spatial connectivity; hold aggregate counts fixed while varying graph statistics. Fit extension and strong modern reference model on training experiments; compare blinded held-out predictive likelihood/error under matched complexity and budget. If no robust improvement, reject the increment.
Benefit if validated: better adaptation planning.
Evidence: CANDIDATE; domain-specific equation contract INCOMPLETE; numerical result NOT RUN; literature novelty UNKNOWN; empirical verification NOT DONE.

086. Materials mechanics — dislocation network topology
Existing reference model: constitutive stress–strain laws; primary observable: plastic strain rate.
Observed/latent variable to examine: dislocation network topology.
Unverified title-derived mechanism hint: network / geometry. Image or reconstruct the evolving contact/connection graph underlying dislocation network topology; hold aggregate counts fixed while varying graph statistics.
Candidate construction: Represent adjacency/connectivity explicitly; project to a minimal measurable graph statistic and check whether equal aggregate states have different futures.
Garden graph: THING=physical components; TIME=trajectory; SPACE=physical domain; EVENT=state transition; ACTION=controlled perturbation where applicable; AGENCY=experimenter/controller only; RULE=physical conservation; VALUE=declared performance measure; CONTEXT=experimental conditions; CLAIM=testable mechanism. Applicable edges: partOf, dependsOn, contextualizes, derivedFrom, supports/contradicts; use causes only after causal identification.
Seven forms: CONSTRUCT=system; CONTRACT=units/domain; STATE=measured and hidden variables; RELATION=typed dependencies; PROCESS=state evolution; RULE=physical constraints; PROJECTION=baseline observable.
Falsification protocol: Image or reconstruct the evolving contact/connection graph underlying dislocation network topology; hold aggregate counts fixed while varying graph statistics. Fit extension and strong modern reference model on training experiments; compare blinded held-out predictive likelihood/error under matched complexity and budget. If no robust improvement, reject the increment.
Benefit if validated: stronger lightweight materials.
Evidence: CANDIDATE; domain-specific equation contract INCOMPLETE; numerical result NOT RUN; literature novelty UNKNOWN; empirical verification NOT DONE.

087. Materials mechanics — grain-boundary slip memory
Existing reference model: constitutive stress–strain laws; primary observable: plastic strain rate.
Observed/latent variable to examine: grain-boundary slip memory.
Unverified title-derived mechanism hint: dynamic hidden state / delay. Use matched present-state trajectories with different prior forcing histories for grain-boundary slip memory; check whether their subsequent responses diverge.
Candidate construction: Introduce a physically measured relaxing state or convolution kernel; estimate its timescale from perturbation data, not arbitrary fitting.
Garden graph: THING=physical components; TIME=trajectory; SPACE=physical domain; EVENT=state transition; ACTION=controlled perturbation where applicable; AGENCY=experimenter/controller only; RULE=physical conservation; VALUE=declared performance measure; CONTEXT=experimental conditions; CLAIM=testable mechanism. Applicable edges: partOf, dependsOn, contextualizes, derivedFrom, supports/contradicts; use causes only after causal identification.
Seven forms: CONSTRUCT=system; CONTRACT=units/domain; STATE=measured and hidden variables; RELATION=typed dependencies; PROCESS=state evolution; RULE=physical constraints; PROJECTION=baseline observable.
Falsification protocol: Use matched present-state trajectories with different prior forcing histories for grain-boundary slip memory; check whether their subsequent responses diverge. Fit extension and strong modern reference model on training experiments; compare blinded held-out predictive likelihood/error under matched complexity and budget. If no robust improvement, reject the increment.
Benefit if validated: stronger lightweight materials.
Evidence: CANDIDATE; domain-specific equation contract INCOMPLETE; numerical result NOT RUN; literature novelty UNKNOWN; empirical verification NOT DONE.

088. Materials mechanics — strain-rate history
Existing reference model: constitutive stress–strain laws; primary observable: plastic strain rate.
Observed/latent variable to examine: strain-rate history.
Unverified title-derived mechanism hint: dynamic hidden state / delay. Use matched present-state trajectories with different prior forcing histories for strain-rate history; check whether their subsequent responses diverge.
Candidate construction: Introduce a physically measured relaxing state or convolution kernel; estimate its timescale from perturbation data, not arbitrary fitting.
Garden graph: THING=physical components; TIME=trajectory; SPACE=physical domain; EVENT=state transition; ACTION=controlled perturbation where applicable; AGENCY=experimenter/controller only; RULE=physical conservation; VALUE=declared performance measure; CONTEXT=experimental conditions; CLAIM=testable mechanism. Applicable edges: partOf, dependsOn, contextualizes, derivedFrom, supports/contradicts; use causes only after causal identification.
Seven forms: CONSTRUCT=system; CONTRACT=units/domain; STATE=measured and hidden variables; RELATION=typed dependencies; PROCESS=state evolution; RULE=physical constraints; PROJECTION=baseline observable.
Falsification protocol: Use matched present-state trajectories with different prior forcing histories for strain-rate history; check whether their subsequent responses diverge. Fit extension and strong modern reference model on training experiments; compare blinded held-out predictive likelihood/error under matched complexity and budget. If no robust improvement, reject the increment.
Benefit if validated: stronger lightweight materials.Evidence: CANDIDATE; domain-specific equation contract INCOMPLETE; numerical result NOT RUN; literature novelty UNKNOWN; empirical verification NOT DONE.

089. Materials mechanics — phase-boundary stress covariance
Existing reference model: constitutive stress–strain laws; primary observable: plastic strain rate.
Observed/latent variable to examine: phase-boundary stress covariance.
Unverified title-derived mechanism hint: heterogeneity / joint distribution. Measure paired local fields or event-resolved distributions for phase-boundary stress covariance; compare joint-data model with independently shuffled marginals.
Candidate construction: Add a measured joint-distribution statistic, not a free coefficient; derive aggregate response by averaging the local law and quantify the residual.
Garden graph: THING=physical components; TIME=trajectory; SPACE=physical domain; EVENT=state transition; ACTION=controlled perturbation where applicable; AGENCY=experimenter/controller only; RULE=physical conservation; VALUE=declared performance measure; CONTEXT=experimental conditions; CLAIM=testable mechanism. Applicable edges: partOf, dependsOn, contextualizes, derivedFrom, supports/contradicts; use causes only after causal identification.
Seven forms: CONSTRUCT=system; CONTRACT=units/domain; STATE=measured and hidden variables; RELATION=typed dependencies; PROCESS=state evolution; RULE=physical constraints; PROJECTION=baseline observable.
Falsification protocol: Measure paired local fields or event-resolved distributions for phase-boundary stress covariance; compare joint-data model with independently shuffled marginals. Fit extension and strong modern reference model on training experiments; compare blinded held-out predictive likelihood/error under matched complexity and budget. If no robust improvement, reject the increment.
Benefit if validated: stronger lightweight materials.
Evidence: CANDIDATE; domain-specific equation contract INCOMPLETE; numerical result NOT RUN; literature novelty UNKNOWN; empirical verification NOT DONE.

090. Materials mechanics — defect-cluster intermittency
Existing reference model: constitutive stress–strain laws; primary observable: plastic strain rate.
Observed/latent variable to examine: defect-cluster intermittency.
Unverified title-derived mechanism hint: heterogeneity / joint distribution. Measure paired local fields or event-resolved distributions for defect-cluster intermittency; compare joint-data model with independently shuffled marginals.
Candidate construction: Add a measured joint-distribution statistic, not a free coefficient; derive aggregate response by averaging the local law and quantify the residual.
Garden graph: THING=physical components; TIME=trajectory; SPACE=physical domain; EVENT=state transition; ACTION=controlled perturbation where applicable; AGENCY=experimenter/controller only; RULE=physical conservation; VALUE=declared performance measure; CONTEXT=experimental conditions; CLAIM=testable mechanism. Applicable edges: partOf, dependsOn, contextualizes, derivedFrom, supports/contradicts; use causes only after causal identification.
Seven forms: CONSTRUCT=system; CONTRACT=units/domain; STATE=measured and hidden variables; RELATION=typed dependencies; PROCESS=state evolution; RULE=physical constraints; PROJECTION=baseline observable.
Falsification protocol: Measure paired local fields or event-resolved distributions for defect-cluster intermittency; compare joint-data model with independently shuffled marginals. Fit extension and strong modern reference model on training experiments; compare blinded held-out predictive likelihood/error under matched complexity and budget. If no robust improvement, reject the increment.
Benefit if validated: stronger lightweight materials.
Evidence: CANDIDATE; domain-specific equation contract INCOMPLETE; numerical result NOT RUN; literature novelty UNKNOWN; empirical verification NOT DONE.

091. Protein kinetics — conformational-state memory
Existing reference model: Michaelis–Menten enzyme kinetics; primary observable: effective catalytic rate.
Observed/latent variable to examine: conformational-state memory.
Unverified title-derived mechanism hint: dynamic hidden state / delay. Use matched present-state trajectories with different prior forcing histories for conformational-state memory; check whether their subsequent responses diverge.
Candidate construction: Introduce a physically measured relaxing state or convolution kernel; estimate its timescale from perturbation data, not arbitrary fitting.
Garden graph: THING=physical components; TIME=trajectory; SPACE=physical domain; EVENT=state transition; ACTION=controlled perturbation where applicable; AGENCY=experimenter/controller only; RULE=physical conservation; VALUE=declared performance measure; CONTEXT=experimental conditions; CLAIM=testable mechanism. Applicable edges: partOf, dependsOn, contextualizes, derivedFrom, supports/contradicts; use causes only after causal identification.
Seven forms: CONSTRUCT=system; CONTRACT=units/domain; STATE=measured and hidden variables; RELATION=typed dependencies; PROCESS=state evolution; RULE=physical constraints; PROJECTION=baseline observable.
Falsification protocol: Use matched present-state trajectories with different prior forcing histories for conformational-state memory; check whether their subsequent responses diverge. Fit extension and strong modern reference model on training experiments; compare blinded held-out predictive likelihood/error under matched complexity and budget. If no robust improvement, reject the increment.
Benefit if validated: biomanufacturing.
Evidence: CANDIDATE; domain-specific equation contract INCOMPLETE; numerical result NOT RUN; literature novelty UNKNOWN; empirical verification NOT DONE.

092. Protein kinetics — substrate microdomain gradients
Existing reference model: Michaelis–Menten enzyme kinetics; primary observable: effective catalytic rate.
Observed/latent variable to examine: substrate microdomain gradients.
Unverified title-derived mechanism hint: heterogeneity / joint distribution. Measure paired local fields or event-resolved distributions for substrate microdomain gradients; compare joint-data model with independently shuffled marginals.
Candidate construction: Add a measured joint-distribution statistic, not a free coefficient; derive aggregate response by averaging the local law and quantify the residual.
Garden graph: THING=physical components; TIME=trajectory; SPACE=physical domain; EVENT=state transition; ACTION=controlled perturbation where applicable; AGENCY=experimenter/controller only; RULE=physical conservation; VALUE=declared performance measure; CONTEXT=experimental conditions; CLAIM=testable mechanism. Applicable edges: partOf, dependsOn, contextualizes, derivedFrom, supports/contradicts; use causes only after causal identification.
Seven forms: CONSTRUCT=system; CONTRACT=units/domain; STATE=measured and hidden variables; RELATION=typed dependencies; PROCESS=state evolution; RULE=physical constraints; PROJECTION=baseline observable.
Falsification protocol: Measure paired local fields or event-resolved distributions for substrate microdomain gradients; compare joint-data model with independently shuffled marginals. Fit extension and strong modern reference model on training experiments; compare blinded held-out predictive likelihood/error under matched complexity and budget. If no robust improvement, reject the increment.
Benefit if validated: biomanufacturing.
Evidence: CANDIDATE; domain-specific equation contract INCOMPLETE; numerical result NOT RUN; literature novelty UNKNOWN; empirical verification NOT DONE.

093. Protein kinetics — crowding-induced correlation
Existing reference model: Michaelis–Menten enzyme kinetics; primary observable: effective catalytic rate.
Observed/latent variable to examine: crowding-induced correlation.
Unverified title-derived mechanism hint: heterogeneity / joint distribution. Measure paired local fields or event-resolved distributions for crowding-induced correlation; compare joint-data model with independently shuffled marginals.
Candidate construction: Add a measured joint-distribution statistic, not a free coefficient; derive aggregate response by averaging the local law and quantify the residual.
Garden graph: THING=physical components; TIME=trajectory; SPACE=physical domain; EVENT=state transition; ACTION=controlled perturbation where applicable; AGENCY=experimenter/controller only; RULE=physical conservation; VALUE=declared performance measure; CONTEXT=experimental conditions; CLAIM=testable mechanism. Applicable edges: partOf, dependsOn, contextualizes, derivedFrom, supports/contradicts; use causes only after causal identification.
Seven forms: CONSTRUCT=system; CONTRACT=units/domain; STATE=measured and hidden variables; RELATION=typed dependencies; PROCESS=state evolution; RULE=physical constraints; PROJECTION=baseline observable.
Falsification protocol: Measure paired local fields or event-resolved distributions for crowding-induced correlation; compare joint-data model with independently shuffled marginals. Fit extension and strong modern reference model on training experiments; compare blinded held-out predictive likelihood/error under matched complexity and budget. If no robust improvement, reject the increment.
Benefit if validated: biomanufacturing.
Evidence: CANDIDATE; domain-specific equation contract INCOMPLETE; numerical result NOT RUN; literature novelty UNKNOWN; empirical verification NOT DONE.

094. Protein kinetics — allosteric network topology
Existing reference model: Michaelis–Menten enzyme kinetics; primary observable: effective catalytic rate.
Observed/latent variable to examine: allosteric network topology.
Unverified title-derived mechanism hint: network / geometry. Image or reconstruct the evolving contact/connection graph underlying allosteric network topology; hold aggregate counts fixed while varying graph statistics.
Candidate construction: Represent adjacency/connectivity explicitly; project to a minimal measurable graph statistic and check whether equal aggregate states have different futures.
Garden graph: THING=physical components; TIME=trajectory; SPACE=physical domain; EVENT=state transition; ACTION=controlled perturbation where applicable; AGENCY=experimenter/controller only; RULE=physical conservation; VALUE=declared performance measure; CONTEXT=experimental conditions; CLAIM=testable mechanism. Applicable edges: partOf, dependsOn, contextualizes, derivedFrom, supports/contradicts; use causes only after causal identification.
Seven forms: CONSTRUCT=system; CONTRACT=units/domain; STATE=measured and hidden variables; RELATION=typed dependencies; PROCESS=state evolution; RULE=physical constraints; PROJECTION=baseline observable.
Falsification protocol: Image or reconstruct the evolving contact/connection graph underlying allosteric network topology; hold aggregate counts fixed while varying graph statistics. Fit extension and strong modern reference model on training experiments; compare blinded held-out predictive likelihood/error under matched complexity and budget. If no robust improvement, reject the increment.
Benefit if validated: biomanufacturing.
Evidence: CANDIDATE; domain-specific equation contract INCOMPLETE; numerical result NOT RUN; literature novelty UNKNOWN; empirical verification NOT DONE.

095. Protein kinetics — product inhibition lag
Existing reference model: Michaelis–Menten enzyme kinetics; primary observable: effective catalytic rate.
Observed/latent variable to examine: product inhibition lag.
Unverified title-derived mechanism hint: dynamic hidden state / delay. Use matched present-state trajectories with different prior forcing histories for product inhibition lag; check whether their subsequent responses diverge.
Candidate construction: Introduce a physically measured relaxing state or convolution kernel; estimate its timescale from perturbation data, not arbitrary fitting.
Garden graph: THING=physical components; TIME=trajectory; SPACE=physical domain; EVENT=state transition; ACTION=controlled perturbation where applicable; AGENCY=experimenter/controller only; RULE=physical conservation; VALUE=declared performance measure; CONTEXT=experimental conditions; CLAIM=testable mechanism. Applicable edges: partOf, dependsOn, contextualizes, derivedFrom, supports/contradicts; use causes only after causal identification.
Seven forms: CONSTRUCT=system; CONTRACT=units/domain; STATE=measured and hidden variables; RELATION=typed dependencies; PROCESS=state evolution; RULE=physical constraints; PROJECTION=baseline observable.
Falsification protocol: Use matched present-state trajectories with different prior forcing histories for product inhibition lag; check whether their subsequent responses diverge. Fit extension and strong modern reference model on training experiments; compare blinded held-out predictive likelihood/error under matched complexity and budget. If no robust improvement, reject the increment.
Benefit if validated: biomanufacturing.
Evidence: CANDIDATE; domain-specific equation contract INCOMPLETE; numerical result NOT RUN; literature novelty UNKNOWN; empirical verification NOT DONE.

096. Optical materials — nano-inclusion spatial correlation
Existing reference model: effective-medium / radiative transfer; primary observable: effective optical response.
Observed/latent variable to examine: nano-inclusion spatial correlation.
Unverified title-derived mechanism hint: heterogeneity / joint distribution. Measure paired local fields or event-resolved distributions for nano-inclusion spatial correlation; compare joint-data model with independently shuffled marginals.
Candidate construction: Add a measured joint-distribution statistic, not a free coefficient; derive aggregate response by averaging the local law and quantify the residual.
Garden graph: THING=physical components; TIME=trajectory; SPACE=physical domain; EVENT=state transition; ACTION=controlled perturbation where applicable; AGENCY=experimenter/controller only; RULE=physical conservation; VALUE=declared performance measure; CONTEXT=experimental conditions; CLAIM=testable mechanism. Applicable edges: partOf, dependsOn, contextualizes, derivedFrom, supports/contradicts; use causes only after causal identification.
Seven forms: CONSTRUCT=system; CONTRACT=units/domain; STATE=measured and hidden variables; RELATION=typed dependencies; PROCESS=state evolution; RULE=physical constraints; PROJECTION=baseline observable.
Falsification protocol: Measure paired local fields or event-resolved distributions for nano-inclusion spatial correlation; compare joint-data model with independently shuffled marginals. Fit extension and strong modern reference model on training experiments; compare blinded held-out predictive likelihood/error under matched complexity and budget. If no robust improvement, reject the increment.
Benefit if validated: sensors and photonics.
Evidence: CANDIDATE; domain-specific equation contract INCOMPLETE; numerical result NOT RUN; literature novelty UNKNOWN; empirical verification NOT DONE.

097. Optical materials — interface exciton coupling
Existing reference model: effective-medium / radiative transfer; primary observable: effective optical response.
Observed/latent variable to examine: interface exciton coupling.
Unverified title-derived mechanism hint: coupled latent kinetics. Measure the candidate intermediate state for interface exciton coupling during perturbation/recovery; test whether it predicts held-out transients beyond baseline variables.
Candidate construction: Introduce a measurable intermediate and couple it by mass/energy-balanced rate equations; test observability and parameter identifiability.
Garden graph: THING=physical components; TIME=trajectory; SPACE=physical domain; EVENT=state transition; ACTION=controlled perturbation where applicable; AGENCY=experimenter/controller only; RULE=physical conservation; VALUE=declared performance measure; CONTEXT=experimental conditions; CLAIM=testable mechanism. Applicable edges: partOf, dependsOn, contextualizes, derivedFrom, supports/contradicts; use causes only after causal identification.
Seven forms: CONSTRUCT=system; CONTRACT=units/domain; STATE=measured and hidden variables; RELATION=typed dependencies; PROCESS=state evolution; RULE=physical constraints; PROJECTION=baseline observable.
Falsification protocol: Measure the candidate intermediate state for interface exciton coupling during perturbation/recovery; test whether it predicts held-out transients beyond baseline variables. Fit extension and strong modern reference model on training experiments; compare blinded held-out predictive likelihood/error under matched complexity and budget. If no robust improvement, reject the increment.
Benefit if validated: sensors and photonics.
Evidence: CANDIDATE; domain-specific equation contract INCOMPLETE; numerical result NOT RUN; literature novelty UNKNOWN; empirical verification NOT DONE.

098. Optical materials — temperature-dependent disorder
Existing reference model: effective-medium / radiative transfer; primary observable: effective optical response.
Observed/latent variable to examine: temperature-dependent disorder.
Unverified title-derived mechanism hint: heterogeneity / joint distribution. Measure paired local fields or event-resolved distributions for temperature-dependent disorder; compare joint-data model with independently shuffled marginals.
Candidate construction: Add a measured joint-distribution statistic, not a free coefficient; derive aggregate response by averaging the local law and quantify the residual.
Garden graph: THING=physical components; TIME=trajectory; SPACE=physical domain; EVENT=state transition; ACTION=controlled perturbation where applicable; AGENCY=experimenter/controller only; RULE=physical conservation; VALUE=declared performance measure; CONTEXT=experimental conditions; CLAIM=testable mechanism. Applicable edges: partOf, dependsOn, contextualizes, derivedFrom, supports/contradicts; use causes only after causal identification.
Seven forms: CONSTRUCT=system; CONTRACT=units/domain; STATE=measured and hidden variables; RELATION=typed dependencies; PROCESS=state evolution; RULE=physical constraints; PROJECTION=baseline observable.
Falsification protocol: Measure paired local fields or event-resolved distributions for temperature-dependent disorder; compare joint-data model with independently shuffled marginals. Fit extension and strong modern reference model on training experiments; compare blinded held-out predictive likelihood/error under matched complexity and budget. If no robust improvement, reject the increment.
Benefit if validated: sensors and photonics.
Evidence: CANDIDATE; domain-specific equation contract INCOMPLETE; numerical result NOT RUN; literature novelty UNKNOWN; empirical verification NOT DONE.

099. Optical materials — nonlocal scattering memory
Existing reference model: effective-medium / radiative transfer; primary observable: effective optical response.
Observed/latent variable to examine: nonlocal scattering memory.
Unverified title-derived mechanism hint: dynamic hidden state / delay. Use matched present-state trajectories with different prior forcing histories for nonlocal scattering memory; check whether their subsequent responses diverge.
Candidate construction: Introduce a physically measured relaxing state or convolution kernel; estimate its timescale from perturbation data, not arbitrary fitting.
Garden graph: THING=physical components; TIME=trajectory; SPACE=physical domain; EVENT=state transition; ACTION=controlled perturbation where applicable; AGENCY=experimenter/controller only; RULE=physical conservation; VALUE=declared performance measure; CONTEXT=experimental conditions; CLAIM=testable mechanism. Applicable edges: partOf, dependsOn, contextualizes, derivedFrom, supports/contradicts; use causes only after causal identification.
Seven forms: CONSTRUCT=system; CONTRACT=units/domain; STATE=measured and hidden variables; RELATION=typed dependencies; PROCESS=state evolution; RULE=physical constraints; PROJECTION=baseline observable.
Falsification protocol: Use matched present-state trajectories with different prior forcing histories for nonlocal scattering memory; check whether their subsequent responses diverge. Fit extension and strong modern reference model on training experiments; compare blinded held-out predictive likelihood/error under matched complexity and budget. If no robust improvement, reject the increment.
Benefit if validated: sensors and photonics.
Evidence: CANDIDATE; domain-specific equation contract INCOMPLETE; numerical result NOT RUN; literature novelty UNKNOWN; empirical verification NOT DONE.

100. Optical materials — defect-network percolation
Existing reference model: effective-medium / radiative transfer; primary observable: effective optical response.
Observed/latent variable to examine: defect-network percolation.
Unverified title-derived mechanism hint: network / geometry. Image or reconstruct the evolving contact/connection graph underlying defect-network percolation; hold aggregate counts fixed while varying graph statistics.
Candidate construction: Represent adjacency/connectivity explicitly; project to a minimal measurable graph statistic and check whether equal aggregate states have different futures.
Garden graph: THING=physical components; TIME=trajectory; SPACE=physical domain; EVENT=state transition; ACTION=controlled perturbation where applicable; AGENCY=experimenter/controller only; RULE=physical conservation; VALUE=declared performance measure; CONTEXT=experimental conditions; CLAIM=testable mechanism. Applicable edges: partOf, dependsOn, contextualizes, derivedFrom, supports/contradicts; use causes only after causal identification.
Seven forms: CONSTRUCT=system; CONTRACT=units/domain; STATE=measured and hidden variables; RELATION=typed dependencies; PROCESS=state evolution; RULE=physical constraints; PROJECTION=baseline observable.
Falsification protocol: Image or reconstruct the evolving contact/connection graph underlying defect-network percolation; hold aggregate counts fixed while varying graph statistics. Fit extension and strong modern reference model on training experiments; compare blinded held-out predictive likelihood/error under matched complexity and budget. If no robust improvement, reject the increment.
Benefit if validated: sensors and photonics.
Evidence: CANDIDATE; domain-specific equation contract INCOMPLETE; numerical result NOT RUN; literature novelty UNKNOWN; empirical verification NOT DONE.

F. ADMISSION AND STATISTICAL CONTROLS
100 screened hypotheses imply multiple-comparison risk. Pre-register one primary endpoint per shortlisted candidate; use a suitable familywise or false-discovery-rate procedure and independent replication.
A model's zero-coupling baseline limit is necessary but insufficient. Require structural identifiability, numerical stability, dimensional validity and out-of-distribution testing.
Gate G: THEORY_READY requires source pin + dimensional contract + derivation + synthetic recovery + novelty search + strong baseline comparison. EMPIRICALLY_SUPPORTED additionally requires independent data.
Unresolved TREE_CORE build-integrity issues (truncated gzip, stale schema identifiers, nondeterminism) must not be silently marked PASS; this document is not a proof of canonical compilation.
Final: This revision fixes the index-driven form assignment and supplies ten mathematical examples, but does not establish a globally novel scientific law or 100 fully derived upgrades.


---
# PART 2: GARDEN_SCIENCE_REV3_GAP_CLOSURE_2026-10-09.md

# Garden v15.10 scientific discovery — gap-closure evidence

Date: 2026-10-09
Status: NONCANONICAL / SCIENTIFIC RESEARCH / NOT DISCOVERY

## Scope and limitations
This addendum does NOT claim to fix all 100 scientific candidates. The 100 proposals remain largely un-derived; novelty is unverified. The current evidence repairs one important benchmark comparator weakness for Candidate 026.

## Candidate 026: noise-aware output-error comparator
- Synthetic source: `garden_candidate026_harness.py` (unchanged reference generator).
- New comparator: `garden_candidate026_strong_comparator.py`.
- Fits one-body and two-body thermal RC state-space models to noisy observed temperature using least squares of **simulation output**, not regression on noisy lagged outputs.
- Zero-order-hold discretization, positive capacities and conductances via log parameters, fitted initial temperatures, one fixed starting point per model, SciPy `least_squares` with parameter bounds.
- Selection rule: training BIC(two-body) <= training BIC(one-body)-10. Held-out MSE reported separately and not used to select model.
- Noise sigma=0.012, 20 null + 20 hidden-state synthetic cases: 0/20 false selections; 20/20 detections.
- Noise sigma=0.024, 12 null + 12 hidden-state synthetic cases: 0/12 false selections; 12/12 detections.
- These counts are finite-sample results, not guarantees; comparator is given both candidate model families, so it is not a blind scientific discovery benchmark.
- The earlier ARX result (3/100 null false positives after calibration) remains as a historical diagnostic; it is no longer presented as the best baseline.

## Corrections to prior claims
- Keyword-based mechanism hints are NOT residual-driven discoveries.
- '100 distinct diagnostics' is false. 100 entries are research prompts; only ten contain worked mathematics.
- Candidate 017: positive Arrhenius log-rate curvature under constant positive prefactors and fixed barriers.
- Candidate 041: information-theoretic conditioning inequality does not supply an implementable closure without a forecast of the conditioning variable.
- Candidate 072: infection-age model is established, not unresolved as a mathematical mechanism.
- Candidate 026: two-body RC physics is established. No claim of scientific novelty.

## Explicit pending gates
1. Global literature novelty search for 100/100: NOT DONE.
2. Strongest current domain-specific baselines for 100/100: NOT DONE.
3. Full dimensioned TheoryEquationContracts for remaining 99: NOT DONE.
4. Blind residual-driven mechanism identification on unseen problems: NOT DONE.
5. Real-world held-out experiments: NOT DONE.
6. TREE_CORE build integrity, CRC, schema and deterministic compilation repairs: NOT DONE.
7. Multiplicity-adjusted registered primary endpoints for a shortlisted candidate set: NOT DONE.

## Proposed acceptance gates
- G0: Pin current baseline theory and strongest alternatives.
- G1: Define projection and find independent physical states with same projected state but different futures.
- G2: Diagnose residual without title or mechanism leakage; report UNKNOWN when insufficient.
- G3: Derive typed equations with units, limits, identifiability, conservation and positivity checks.
- G4: Compare against noise-aware state-space and domain-specific baselines, with held-out forcing and matched budget.
- G5: Search literature for novelty; downgrade rediscovered results to known mechanisms.
- G6: Pre-register signed/magnitude predictions, multiple-comparison controls and independent replication.
- G7: Human-reviewed scientific status; no self-admission or overwrite of controlling Garden sources.

## Reproduction
From this directory with NumPy and SciPy installed:
`python garden_candidate026_strong_comparator.py --n 20 --output garden_candidate026_strong_results.json`
`python garden_candidate026_strong_comparator.py --n 12 --noise 0.024 --seed 20000 --output garden_candidate026_strong_results_high_noise.json`

The harness imports `garden_candidate026_harness.py` for synthetic trajectory generation. Numerical results may vary with dependency versions; reproducible pinned environments are a future gate.


---
# PART 3: GARDEN_SCIENCE_FIVE_DOMAINS_AND_16_TRANSFERS_2026-10-09.md

# Garden v15.10 — Five Domain Investigations and Sixteen Transfer Candidates
Date: 2026-10-09
Status: NONCANONICAL RESEARCH / hypotheses, not discoveries
Source: user-supplied five principal ideas and sixteen application ideas; Garden REV3 candidate register.
Evidence scope: selective literature reconnaissance, analytical derivations under declared toy-model assumptions, no empirical benchmark or independent novelty certification.

## 0. Universal projection-to-discovery contract
For each investigation, freeze the strongest available baseline; define detailed state X, observable Y=A(X), physical dynamics T, and an admissible context C. Search for X1,X2 with A(X1)=A(X2) but A(T(X1)) != A(T(X2)). The difference is evidence that Y alone is not dynamically closed, not automatically a new physical law. Derive a minimal additional measurable state Z; check units, invariants, identifiability, limiting behavior, causal alternatives, held-out forecast skill, strong-baseline parity, multiplicity and literature priority.
GSL: TIME/SPACE/THING/EVENT/ACTION/AGENCY/RULE/VALUE/CONTEXT/CLAIM; apply only valid relations from the 24-core registry; seven forms CONSTRUCT, CONTRACT, STATE, RELATION, PROCESS, RULE, PROJECTION. For physical systems, AGENCY ordinarily means experimenter/controller, not matter. Evidence/proof/novelty/utility remain separate. UNKNOWN != PASS. No self-admission.
Proposed typed science-specific "approximates-in-limit" contract is an annotation on a derivation, not a new Garden core relation.
Scientific status fields: hypothesis, dimensional check, analytical result, synthetic test, literature comparison, empirical test, benefit.
For each candidate, demand a comparator using the best current domain model rather than a textbook strawman. Blinding: do not disclose the hidden mechanism in the candidate title given to the discovery model.

## 1. Macroeconomic liquidity and transaction networks
BASELINE: Heterogeneous-agent macroeconomics, agent-based monetary networks, input-output and payment networks already model many distributional and network effects; representative-agent DSGE is not universal.
Detailed state: regional balances m_i [currency], edge flows f_ij [currency/time], delayed settlements q_ij(t,s), local prices and output. Projection: aggregate money M=sum_i m_i and national velocity V. 
Candidate network-delay model: dm_i/dt = transfers_i + income_i - spending_i + sum_j(f_ji-f_ij); settlement arrivals may be represented by integral_0^infty K_ij(s) f_ji(t-s) ds with normalized K_ij(s) [1/time]. Settlement pipeline balances must be included for conservation. Units: currency/time on both sides.
Derived distinction: two networks with the same M and average V but different edge bottlenecks can have different settlement-time distributions. This is a counterexample to a model using M,V alone; not a novel economic law.
Signed test: at matched total transfer volume and region size, a measured increase in edge bottleneck concentration predicts increased upper-tail settlement latency if routing and service rates are held fixed; not necessarily higher inflation or GDP.
Strong comparators: heterogeneous-agent New Keynesian, agent-based payment network, queueing-network models; compare distributional and regional out-of-sample prediction, not only aggregate GDP.
Data: anonymized payments/settlement timestamps, regional price indices, GST receipts and transfer histories. Guard against re-identification and intervention harms.
Benefit: better regional transfer targeting and cashflow resilience IF proven; cannot promise optimized GST windfalls or neutralized inflation.
Status: equation-level candidate; novelty UNKNOWN; no data fit.

## 2. Quantum transport / active matter
BASELINE: quantum kinetic equations, NEGF, Lindblad/open-system models and non-Markovian transport already include coherence, scattering and memory. "Infinite Electron Theorem" is a proposed name, not a recognized demonstrated theorem.
Detailed state: density operator rho(t), contacts, fields, phonon bath; projection to current I(t) and local density n(x,t).
Candidate: drho/dt = L0[rho(t)] + integral_0^t K(t-s)[rho(s)] ds + drive(t), with K a superoperator of units 1/time^2 (when integrating ds) and trace-preserving, Hermiticity-preserving conditions; complete positivity is nontrivial and must be checked. Currents must satisfy charge continuity.
Analytical distinction: identical instantaneous density/current with different system-bath correlations can yield different subsequent current; memoryless projection may be insufficient.
Falsifier: measure pump-probe transient conductivity and fit NEGF/non-Markovian baseline; hold out pulse sequences; reject if additional memory structure has no independent predictive benefit.
Benefit: improved transport design or reduced losses IF validated. Memory alone implies neither zero resistance nor room-temperature superconductivity. Active matter and electron transport are not interchangeable physical theories.
Status: conditional modelling direction; no theorem or superconducting evidence.

## 3. Deterministic AI safety / hardware kernels
BASELINE: runtime verification, BFT protocols, formal methods, watchdogs, control barrier functions and hardware fault tolerance are established; none generally guarantees truthful semantic outputs.
Detailed state: processor timing, scheduler, sensor freshness, network faults, model action proposals and physical plant state. Projection to "heartbeat present" and "action allowed".
Candidate: barrier h(x)>=0 for physical safety set; require along continuous plant trajectories dot h(x,u)+alpha(h(x))>=0 with model uncertainty margins, verified actuator bounds, trusted state estimates, and sampled-data corrections. A 5.5 kHz heartbeat has period ~181.8 microseconds; frequency alone does not imply correctness.
Failure counterexample: two systems with identical heartbeat timing can execute different unsafe commands. Therefore heartbeat is not a semantic invariant.
Test: inject missed deadlines, Byzantine messages, sensor spoofing, model hallucinations and stale commitments; compare conventional certified runtime assurance and fault-tolerant control at identical fault budgets.
Benefit: potentially more dependable industrial control; "zero hallucination", universal semantic closure and SEP/licensing income NOT established.
Status: no deterministic semantic guarantee; focus on bounded physical safety only.

## 4. Modular urban architecture (100 m x 100 m cells)
BASELINE: district digital twins, multi-energy microgrids, water-energy-food nexus, integrated transport planning and vertical farm models already exist.
Detailed state: nodal electricity/water/waste stocks, battery state, occupancy, transit flows, crop biomass, weather, costs. Projection to mean per-cell demand and annual yields.
Proposed dynamic coupling: dE_i/dt = generation_i + imports_i - demand_i - exports_i - losses_i, with energy units and inter-node power flows integrated in time. Water and food have distinct mass balances; no shared "kinetics" term should be used without physically typed mappings.
Derived distinction: equal annual average load does not imply equal coincident peak load; network congestion depends on joint time series and edge capacity.
Experiment: simulated multi-cell scenarios with weather/load/crop time series; compare multi-energy district optimization, robust MPC and independent per-cell planning. Primary endpoint: lifecycle cost subject to reliability, water and food constraints. Test outage resilience separately.
Benefit: possible infrastructure savings, not elimination of overprovisioning or guaranteed self-sufficiency.
Literature: 2026 district digital-twin reviews already identify cross-system integration and sequential planning; claim novelty only for a specific independently verified capability.
Status: feasible digital-twin research; unverified savings.

## 5. Advanced semiconductor yield / local thermo-mechanical stress
BASELINE: advanced foundries already use process TCAD, electrothermal, stress and defect statistics; "2 nm" is a process-node designation, not a literal universal feature width. Sub-nanometer predictive scales need atomistic methods where relevant.
Detailed state: local temperature T(x,t) [K], strain epsilon [dimensionless], stress sigma [Pa], defect density d(x,t) [1/m^3], feature geometry, process history. Projection to wafer mean temperature and nominal recipe.
Candidate model: rho*c_p*dT/dt = div(k grad T)+Q; thermoelastic constitutive sigma=C:(epsilon-alpha*(T-T0)I); local hazard lambda(x,t)=lambda0 exp[-Ea/(kB*T)] g(sigma/sigma0,d/d0) [1/(m^3 s)] with calibrated dimensionless g. Total expected defect count Lambda=int_volume int_time lambda dx dt. If a Poisson model is independently justified, P(no modeled defects)=exp(-Lambda); spatial dependence/clustered defects can invalidate Poisson.
Derived mathematical consequence: E[lambda(T,sigma)] generally differs from lambda(E[T],E[sigma]); the second-order correction contains lambda_Tsigma Cov(T,sigma) and variance terms. Sign must be computed from the calibrated constitutive function, not asserted.
Falsifier: paired wafers with matched mean thermal histories but different measured spatial covariance; preregister signed yield prediction from independently calibrated hazard law; compare TCAD + established statistical process control + advanced defect models, with held-out lots and process splits.
Benefit: higher yield and fewer scrap lots if incremental prediction survives strongest existing comparators; no numeric savings asserted.
Status: dimensionally specified conditional hazard candidate; physical calibration, identifiability, novelty and yield data pending.

## 6. Cross-domain shortlist of sixteen further investigations
All are candidate investigations, not independently validated novelty. Each requires a source-pinned strongest comparator and its own equation contract.
ID | Domain | Observable projection loss | Discriminating experiment | Potential benefit
A01 | Solid-state batteries | lithium inventory location hidden by capacity total | matched capacity, differing relaxation histories; impedance and plating measurements | longer life
A02 | Polymer electrolyte fuel cells | local flooding distribution hidden by mean humidity | matched mean humidity, different spatial saturation maps | lower catalyst costs
A03 | Polymer gel elasticity | crosslink topology hidden by average chain density | matched density, different topology and cyclic response | tougher gels
A04 | Photovoltaic encapsulants | humidity-stress joint history hidden by average weather | humidity-mechanical accelerated ageing with held-out cycles | reduced delamination
A05 | Continuous-flow reactors | intermediate occupation hidden by bulk conversion | transient spectroscopy during feed pulses | higher yield
A06 | Protein formulations | pair-correlation hidden by mean concentration | scattering plus aggregation-rate prediction | longer shelf life
A07 | Pharmaceutical crystallization | subcritical-cluster history hidden by supersaturation | matched supersaturation, varied preconditioning | reproducible polymorphs
A08 | Groundwater remediation | capillary hysteresis hidden by saturation | wetting/drainage reversal curves with tracer transport | improved cleanup
A09 | Structural fatigue | closure state hidden by present DeltaK | matched DeltaK, differing overload histories | inspection optimization
A10 | Precision agriculture | moisture-nutrient spatial covariance hidden by field averages | spatial sensors, randomized irrigation plots | reduced runoff
A11 | Photonic sensors | pair correlation hidden by inclusion density | matched density, varied structure factor | higher sensitivity
A12 | Neuromorphic computing | glial/metabolic state hidden by firing rate | paired electrophysiology and metabolism under stimulation | energy efficiency
A13 | Epidemic forecasting | infection-age distribution hidden by I total | age-of-infection surveillance and blind incidence forecast | staffing forecasts
A14 | Precision dosing | transporter and circadian state hidden by plasma concentration | repeated sampling across dosing times; safety-governed studies | dose precision
A15 | Neural mass models | phase-lag state hidden by mean firing rate | multichannel recordings and prospective seizure forecast | improved diagnostics
A16 | Ecosystem resilience | refuge topology hidden by species counts | repeated perturbation with spatial refuge maps | conservation resilience

## 7. Verification and status ledger
Analytical modelling sketches: five principal cases. Empirical runs: 0. Strong-baseline benchmark runs: 0. Full novelty searches: 0. Selective prior-art reconnaissance: district digital twins only. Verified global novelty: 0. Accepted scientific discoveries: 0.
Candidate priority: semiconductor (measurable but data access difficult); macro liquidity (public and private data constraints); urban (digital twin datasets and complex scope); AI hardware (physical safety only); quantum transport (high theory and instrumentation burden).
Scientific gates: source pin; exact dimensions; conserved quantities; counterexample to closure; derived term; parameter identifiability; uncertainty; preregistered signed prediction; strong baseline; blind holdout; literature review; independent replication; conditional benefit.
Tree Core and Garden v15.10 remain unchanged; do not infer canonical admission, executable GSL compliance, or source-retention closure from this document.
References for initial reconnaissance:
- Jalilzadeh et al. 2026, A comprehensive review and framework on applications of digital twins for energy transition at district level, Renewable and Sustainable Energy Reviews 234, 116872. DOI 10.1016/j.rser.2026.116872.
- Frontiers in Sustainable Cities (2026), Digital twins for sustainable urban energy systems: systematic review of market mechanisms, flexibility, and coordination at district scale. DOI 10.3389/frsc.2026.1837026.
- Frontiers in Sustainable Food Systems (2026), Optimizing urban agriculture with digital twins. DOI 10.3389/fsufs.2026.1871684.



---
# PART 4: GARDEN_SCIENCE_HIGH_VALUE_OPPORTUNITIES_FINAL_2026-10-09.md

# Garden v15.10 — High-Value Scientific Opportunity Register (Consolidated)
Date: 2026-10-09
Status: NONCANONICAL RESEARCH CANDIDATES; no verified new scientific discoveries.
Scope: 33 distinct opportunity lines from the user's twelve earlier proposals, four technical proposals, and seventeen broader industry proposals. Related lines intentionally overlap; benefits MUST NOT be summed.

## Executive assessment
This is an opportunity and falsification register, not proof of scientific novelty or an economic forecast. The user's supplied dollar figures ($150B+ heat, $875B corrosion, $540B food, $870B diagnostics, etc.) describe alleged total costs, addressable opportunities or illustrative industry claims; they are NOT validated incremental Garden benefits. None has been independently audited here. Success probabilities like 'High' from the source material are replaced with qualitative experimental tractability; probability of a novel scientific improvement remains UNKNOWN for every line.

## Garden v15.10 mechanism
Freeze modern domain baseline and primary observations. Map TIME, SPACE, THING, EVENT, ACTION, AGENCY (only where genuinely applicable), RULE, VALUE, CONTEXT and CLAIM. Add only type-valid edges among the 24 GSL relations, and instantiate CONSTRUCT, CONTRACT, STATE, RELATION, PROCESS, RULE and PROJECTION. Define detailed state X, observable abstraction Y=A(X), and controlled evolution T. Look for x1,x2 with identical A(x) but measurably distinct future A(Tx); derive missing state Z only when a real closure failure is observed or proved. Apply dimensional/conservation/causal/identifiability checks; distinguish predictive gain from mechanism novelty. Compare against the strongest modern baseline under matched compute/data/complexity; use blinded held-out evaluation, preregistered endpoints and multiplicity controls. Preserve source spans, equation contracts, status receipts, TREE_CORE dependencies and no-self-admission. Unknown stays UNKNOWN.

## Economic quantification protocol
For each case calculate incremental value = affected annual cost base × eligible fraction × incremental performance gain × adoption fraction − incremental deployment and operating cost. Bound uncertainty and avoid double counting across food/cold-chain, grid rating/congestion/losses, cement energy/carbon, industrial heat/cooling, and semiconductor equipment. A claim such as '15–30% more line capacity' does not imply 15–30% lower grid costs; neither an industry loss total nor a technical potential equals recoverable incremental benefit. 'Everyone knows' accelerates parallel testing and diffusion but not physical qualification, clinical approval or infrastructure deployment.
All timelines below are *initial controlled demonstration or pilot* windows with adequate resources, not guaranteed proof of scientific novelty or global rollout. Wide deployment can take additional years.

## Summary table
| ID | Field | Candidate abstraction / testable variable | Conditional benefit | Initial test window | Experimental tractability |
|---|---|---|---|---|---|
| 01 | Industrial motor systems | Joint load/pressure/vibration histories | Energy and maintenance cost | 3–12 mo | High |
| 02 | Food preservation | Microbial growth integrated with time-temperature and package transport | Spoilage avoided | 3–12 mo | High |
| 03 | Industrial waste heat | Time-temperature-grade and network matching | Fuel and heat costs | 6–24 mo | High |
| 04 | Water distribution | Pressure transient and deterioration-network memory | Water and pumping losses | 6–18 mo | High |
| 05 | Industrial membrane separation | Fouling state and local concentration polarization | Energy and membrane life | 6–18 mo | High |
| 06 | Cold-chain refrigeration | Thermal inertia, humidity, compressor switching | Energy and food quality | 3–12 mo | High |
| 07 | Methane leak detection | Intermittent emissions with plume and sensor uncertainty | Recovered gas and avoided emissions | 3–12 mo | High |
| 08 | Cement kiln efficiency | Particle thermal histories and calcination reaction gradients | Fuel and reject reduction | 6–24 mo | Medium |
| 09 | Fertilizer efficiency | Soil N transport, microbial state, rainfall history | Yield and fertilizer savings | 1–3 yr | Medium |
| 10 | Grid congestion optimization | Correlated flows, topology, storage and constraints | Congestion and curtailment | 6–24 mo | High |
| 11 | Mining processing | Ore texture/fracture and liberation distributions | Energy and recovery | 6–24 mo | Medium |
| 12 | Building cooling | Thermal mass, humidity and occupancy lag | Electricity and comfort | 3–12 mo | High |
| 13 | Dynamic transmission line rating | Conductor thermal memory and span-wise weather fields | Congestion, capacity and deferred construction | 6–24 mo | High |
| 14 | Biopharma bioreactor yield | Local shear/oxygen distribution and metabolic lag | Batch yield and reduced failures | 1–5 yr | Medium |
| 15 | Metal additive manufacturing | Melt-pool thermal cycles, grain topology and residual stress | Lower rejection and rework | 1–4 yr | Medium |
| 16 | Direct air capture | Water/CO2 coadsorption hysteresis and pore-network aging | Lower regeneration energy and sorbent replacement | 1–5 yr | Medium |
| 17 | Corrosion prevention | Coating defects, electrochemistry and stress/flow histories | Avoided maintenance and failures | 1–5 yr | High |
| 18 | Healthcare diagnostic error | Longitudinal evidence, uncertainty, workflow and escalation | Avoidable patient harm and care costs | 2–7 yr | Medium |
| 19 | Drug discovery | Assay uncertainty, synthesis feasibility and distribution shift | Lower R&D cost per successful therapy | 1–7 yr | Medium |
| 20 | Grid transmission losses | Electrical topology, reactive flow, conductor state | Reduced electrical losses | 1–5 yr | Medium |
| 21 | Mining haulage efficiency | Haul cycles, terrain, state-of-charge and dispatch | Fuel and maintenance | 1–4 yr | High |
| 22 | Water treatment energy | Membrane state, feed salinity, pressure recovery | Electricity and water cost | 1–4 yr | High |
| 23 | Semiconductor fab energy | Tool-level thermal states and facility utility timing | Electricity and throughput | 1–4 yr | High |
| 24 | Agricultural climate yield loss | Heat stress timing, water/nutrient state and cultivar response | Avoided crop losses | 2–10 yr | Medium |
| 25 | Aviation fuel efficiency | Weather, routing, wake, aircraft state and operations | Fuel burn | 1–6 yr | Medium |
| 26 | Shipping fuel efficiency | Hull fouling, wind assistance, route/weather state | Fuel burn | 1–6 yr | High |
| 27 | Steel energy and carbon | Ore quality, furnace thermal profile and reduction kinetics | Fuel and emissions | 2–10 yr | Medium |
| 28 | Cement carbon capture | Flue composition, solvent state and heat integration | Avoided emissions and energy | 2–10 yr | Medium |
| 29 | Construction material reuse | Quality uncertainty, structural grading and logistics topology | Material and disposal costs | 1–7 yr | Medium |
| 30 | Textile recycling | Fiber blend identification, degradation and sorting dynamics | Recovered material and avoided disposal | 1–7 yr | Medium |
| 31 | Data-center cooling | Chip heat flux, coolant dynamics and facility power state | Electricity and capital utilization | 6–36 mo | High |
| 32 | Soil carbon verification | Mineral accessibility, wet/dry microbial memory | Cheaper credible carbon measurement | 1–5 yr | Medium |
| 33 | Precision chemical reactors | Intermediate populations and feed pulse histories | Higher conversion/selectivity | 6–24 mo | High |

## Individual investigations
### 01 — Industrial motor systems
**Projection gap to test:** Joint load/pressure/vibration histories.
**Strong modern comparator:** Motor-system digital twins, optimal pump/compressor control.
**Proposed experiment:** Measure the stated missing variables directly where possible, construct matched aggregate states with contrasting local histories or topology, then compare out-of-sample outcomes under matched parameter and computational budgets. A domain-specific preregistration must supply signed predictions, primary endpoint, sample-size/power calculation, units, error tolerance and falsifiers before testing. This is a study design, not a completed experiment.
**Conditional economic benefit:** Energy and maintenance cost. Formula: affected cost base × verified incremental gain × practical adoption − implementation cost; no numerical incremental saving has been established.
**Earliest controlled test:** 3–12 mo (scenario); experimental tractability high, not probability of discovery.
**Critical qualification:** Large electricity exposure; no attributable Garden savings established.
**Evidence status:** HYPOTHESIS; full TheoryEquationContract NOT COMPLETE; strong-baseline test NOT RUN; literature novelty NOT CERTIFIED; real-world validation NOT DONE.

### 02 — Food preservation
**Projection gap to test:** Microbial growth integrated with time-temperature and package transport.
**Strong modern comparator:** Predictive microbiology and modern cold-chain control.
**Proposed experiment:** Measure the stated missing variables directly where possible, construct matched aggregate states with contrasting local histories or topology, then compare out-of-sample outcomes under matched parameter and computational budgets. A domain-specific preregistration must supply signed predictions, primary endpoint, sample-size/power calculation, units, error tolerance and falsifiers before testing. This is a study design, not a completed experiment.
**Conditional economic benefit:** Spoilage avoided. Formula: affected cost base × verified incremental gain × practical adoption − implementation cost; no numerical incremental saving has been established.
**Earliest controlled test:** 3–12 mo (scenario); experimental tractability high, not probability of discovery.
**Critical qualification:** Food waste total is not wholly addressable.
**Evidence status:** HYPOTHESIS; full TheoryEquationContract NOT COMPLETE; strong-baseline test NOT RUN; literature novelty NOT CERTIFIED; real-world validation NOT DONE.

### 03 — Industrial waste heat
**Projection gap to test:** Time-temperature-grade and network matching.
**Strong modern comparator:** Pinch analysis, exergy optimization, heat-storage dispatch.
**Proposed experiment:** Measure the stated missing variables directly where possible, construct matched aggregate states with contrasting local histories or topology, then compare out-of-sample outcomes under matched parameter and computational budgets. A domain-specific preregistration must supply signed predictions, primary endpoint, sample-size/power calculation, units, error tolerance and falsifiers before testing. This is a study design, not a completed experiment.
**Conditional economic benefit:** Fuel and heat costs. Formula: affected cost base × verified incremental gain × practical adoption − implementation cost; no numerical incremental saving has been established.
**Earliest controlled test:** 6–24 mo (scenario); experimental tractability high, not probability of discovery.
**Critical qualification:** Do not equate theoretical heat resource with realizable savings.
**Evidence status:** HYPOTHESIS; full TheoryEquationContract NOT COMPLETE; strong-baseline test NOT RUN; literature novelty NOT CERTIFIED; real-world validation NOT DONE.

### 04 — Water distribution
**Projection gap to test:** Pressure transient and deterioration-network memory.
**Strong modern comparator:** Hydraulic digital twins, leak detection, pressure management.
**Proposed experiment:** Measure the stated missing variables directly where possible, construct matched aggregate states with contrasting local histories or topology, then compare out-of-sample outcomes under matched parameter and computational budgets. A domain-specific preregistration must supply signed predictions, primary endpoint, sample-size/power calculation, units, error tolerance and falsifiers before testing. This is a study design, not a completed experiment.
**Conditional economic benefit:** Water and pumping losses. Formula: affected cost base × verified incremental gain × practical adoption − implementation cost; no numerical incremental saving has been established.
**Earliest controlled test:** 6–18 mo (scenario); experimental tractability high, not probability of discovery.
**Critical qualification:** Commercial non-revenue water is not all physical leakage.
**Evidence status:** HYPOTHESIS; full TheoryEquationContract NOT COMPLETE; strong-baseline test NOT RUN; literature novelty NOT CERTIFIED; real-world validation NOT DONE.

### 05 — Industrial membrane separation
**Projection gap to test:** Fouling state and local concentration polarization.
**Strong modern comparator:** Multiphysics membrane fouling and optimal cleaning.
**Proposed experiment:** Measure the stated missing variables directly where possible, construct matched aggregate states with contrasting local histories or topology, then compare out-of-sample outcomes under matched parameter and computational budgets. A domain-specific preregistration must supply signed predictions, primary endpoint, sample-size/power calculation, units, error tolerance and falsifiers before testing. This is a study design, not a completed experiment.
**Conditional economic benefit:** Energy and membrane life. Formula: affected cost base × verified incremental gain × practical adoption − implementation cost; no numerical incremental saving has been established.
**Earliest controlled test:** 6–18 mo (scenario); experimental tractability high, not probability of discovery.
**Critical qualification:** Must outperform existing adaptive cleaning.
**Evidence status:** HYPOTHESIS; full TheoryEquationContract NOT COMPLETE; strong-baseline test NOT RUN; literature novelty NOT CERTIFIED; real-world validation NOT DONE.

### 06 — Cold-chain refrigeration
**Projection gap to test:** Thermal inertia, humidity, compressor switching.
**Strong modern comparator:** Model-predictive refrigeration and demand response.
**Proposed experiment:** Measure the stated missing variables directly where possible, construct matched aggregate states with contrasting local histories or topology, then compare out-of-sample outcomes under matched parameter and computational budgets. A domain-specific preregistration must supply signed predictions, primary endpoint, sample-size/power calculation, units, error tolerance and falsifiers before testing. This is a study design, not a completed experiment.
**Conditional economic benefit:** Energy and food quality. Formula: affected cost base × verified incremental gain × practical adoption − implementation cost; no numerical incremental saving has been established.
**Earliest controlled test:** 3–12 mo (scenario); experimental tractability high, not probability of discovery.
**Critical qualification:** Overlaps food preservation; count benefit once.
**Evidence status:** HYPOTHESIS; full TheoryEquationContract NOT COMPLETE; strong-baseline test NOT RUN; literature novelty NOT CERTIFIED; real-world validation NOT DONE.

### 07 — Methane leak detection
**Projection gap to test:** Intermittent emissions with plume and sensor uncertainty.
**Strong modern comparator:** Atmospheric inversion and probabilistic leak localization.
**Proposed experiment:** Measure the stated missing variables directly where possible, construct matched aggregate states with contrasting local histories or topology, then compare out-of-sample outcomes under matched parameter and computational budgets. A domain-specific preregistration must supply signed predictions, primary endpoint, sample-size/power calculation, units, error tolerance and falsifiers before testing. This is a study design, not a completed experiment.
**Conditional economic benefit:** Recovered gas and avoided emissions. Formula: affected cost base × verified incremental gain × practical adoption − implementation cost; no numerical incremental saving has been established.
**Earliest controlled test:** 3–12 mo (scenario); experimental tractability high, not probability of discovery.
**Critical qualification:** Avoid counting carbon and gas benefits twice.
**Evidence status:** HYPOTHESIS; full TheoryEquationContract NOT COMPLETE; strong-baseline test NOT RUN; literature novelty NOT CERTIFIED; real-world validation NOT DONE.

### 08 — Cement kiln efficiency
**Projection gap to test:** Particle thermal histories and calcination reaction gradients.
**Strong modern comparator:** Kiln CFD and process control.
**Proposed experiment:** Measure the stated missing variables directly where possible, construct matched aggregate states with contrasting local histories or topology, then compare out-of-sample outcomes under matched parameter and computational budgets. A domain-specific preregistration must supply signed predictions, primary endpoint, sample-size/power calculation, units, error tolerance and falsifiers before testing. This is a study design, not a completed experiment.
**Conditional economic benefit:** Fuel and reject reduction. Formula: affected cost base × verified incremental gain × practical adoption − implementation cost; no numerical incremental saving has been established.
**Earliest controlled test:** 6–24 mo (scenario); experimental tractability medium, not probability of discovery.
**Critical qualification:** Separate efficiency from carbon capture.
**Evidence status:** HYPOTHESIS; full TheoryEquationContract NOT COMPLETE; strong-baseline test NOT RUN; literature novelty NOT CERTIFIED; real-world validation NOT DONE.

### 09 — Fertilizer efficiency
**Projection gap to test:** Soil N transport, microbial state, rainfall history.
**Strong modern comparator:** Reactive transport and precision nutrient management.
**Proposed experiment:** Measure the stated missing variables directly where possible, construct matched aggregate states with contrasting local histories or topology, then compare out-of-sample outcomes under matched parameter and computational budgets. A domain-specific preregistration must supply signed predictions, primary endpoint, sample-size/power calculation, units, error tolerance and falsifiers before testing. This is a study design, not a completed experiment.
**Conditional economic benefit:** Yield and fertilizer savings. Formula: affected cost base × verified incremental gain × practical adoption − implementation cost; no numerical incremental saving has been established.
**Earliest controlled test:** 1–3 yr (scenario); experimental tractability medium, not probability of discovery.
**Critical qualification:** Field-season replication required.
**Evidence status:** HYPOTHESIS; full TheoryEquationContract NOT COMPLETE; strong-baseline test NOT RUN; literature novelty NOT CERTIFIED; real-world validation NOT DONE.

### 10 — Grid congestion optimization
**Projection gap to test:** Correlated flows, topology, storage and constraints.
**Strong modern comparator:** AC optimal power flow, stochastic unit commitment.
**Proposed experiment:** Measure the stated missing variables directly where possible, construct matched aggregate states with contrasting local histories or topology, then compare out-of-sample outcomes under matched parameter and computational budgets. A domain-specific preregistration must supply signed predictions, primary endpoint, sample-size/power calculation, units, error tolerance and falsifiers before testing. This is a study design, not a completed experiment.
**Conditional economic benefit:** Congestion and curtailment. Formula: affected cost base × verified incremental gain × practical adoption − implementation cost; no numerical incremental saving has been established.
**Earliest controlled test:** 6–24 mo (scenario); experimental tractability high, not probability of discovery.
**Critical qualification:** Overlaps dynamic line rating.
**Evidence status:** HYPOTHESIS; full TheoryEquationContract NOT COMPLETE; strong-baseline test NOT RUN; literature novelty NOT CERTIFIED; real-world validation NOT DONE.

### 11 — Mining processing
**Projection gap to test:** Ore texture/fracture and liberation distributions.
**Strong modern comparator:** Comminution digital twins and mineral separation.
**Proposed experiment:** Measure the stated missing variables directly where possible, construct matched aggregate states with contrasting local histories or topology, then compare out-of-sample outcomes under matched parameter and computational budgets. A domain-specific preregistration must supply signed predictions, primary endpoint, sample-size/power calculation, units, error tolerance and falsifiers before testing. This is a study design, not a completed experiment.
**Conditional economic benefit:** Energy and recovery. Formula: affected cost base × verified incremental gain × practical adoption − implementation cost; no numerical incremental saving has been established.
**Earliest controlled test:** 6–24 mo (scenario); experimental tractability medium, not probability of discovery.
**Critical qualification:** Ore variability must be held out.
**Evidence status:** HYPOTHESIS; full TheoryEquationContract NOT COMPLETE; strong-baseline test NOT RUN; literature novelty NOT CERTIFIED; real-world validation NOT DONE.

### 12 — Building cooling
**Projection gap to test:** Thermal mass, humidity and occupancy lag.
**Strong modern comparator:** Building MPC and calibrated energy models.
**Proposed experiment:** Measure the stated missing variables directly where possible, construct matched aggregate states with contrasting local histories or topology, then compare out-of-sample outcomes under matched parameter and computational budgets. A domain-specific preregistration must supply signed predictions, primary endpoint, sample-size/power calculation, units, error tolerance and falsifiers before testing. This is a study design, not a completed experiment.
**Conditional economic benefit:** Electricity and comfort. Formula: affected cost base × verified incremental gain × practical adoption − implementation cost; no numerical incremental saving has been established.
**Earliest controlled test:** 3–12 mo (scenario); experimental tractability high, not probability of discovery.
**Critical qualification:** Overlaps data-center cooling only partly.
**Evidence status:** HYPOTHESIS; full TheoryEquationContract NOT COMPLETE; strong-baseline test NOT RUN; literature novelty NOT CERTIFIED; real-world validation NOT DONE.

### 13 — Dynamic transmission line rating
**Projection gap to test:** Conductor thermal memory and span-wise weather fields.
**Strong modern comparator:** IEEE/CIGRE dynamic line rating and thermal state estimation.
**Proposed experiment:** Measure the stated missing variables directly where possible, construct matched aggregate states with contrasting local histories or topology, then compare out-of-sample outcomes under matched parameter and computational budgets. A domain-specific preregistration must supply signed predictions, primary endpoint, sample-size/power calculation, units, error tolerance and falsifiers before testing. This is a study design, not a completed experiment.
**Conditional economic benefit:** Congestion, capacity and deferred construction. Formula: affected cost base × verified incremental gain × practical adoption − implementation cost; no numerical incremental saving has been established.
**Earliest controlled test:** 6–24 mo (scenario); experimental tractability high, not probability of discovery.
**Critical qualification:** 15–30% capacity is a site-specific hypothesis, not guaranteed.
**Evidence status:** HYPOTHESIS; full TheoryEquationContract NOT COMPLETE; strong-baseline test NOT RUN; literature novelty NOT CERTIFIED; real-world validation NOT DONE.

### 14 — Biopharma bioreactor yield
**Projection gap to test:** Local shear/oxygen distribution and metabolic lag.
**Strong modern comparator:** CFD-population balance and cell-culture kinetic models.
**Proposed experiment:** Measure the stated missing variables directly where possible, construct matched aggregate states with contrasting local histories or topology, then compare out-of-sample outcomes under matched parameter and computational budgets. A domain-specific preregistration must supply signed predictions, primary endpoint, sample-size/power calculation, units, error tolerance and falsifiers before testing. This is a study design, not a completed experiment.
**Conditional economic benefit:** Batch yield and reduced failures. Formula: affected cost base × verified incremental gain × practical adoption − implementation cost; no numerical incremental saving has been established.
**Earliest controlled test:** 1–5 yr (scenario); experimental tractability medium, not probability of discovery.
**Critical qualification:** 10L-to-2000L+ qualification and product-specific risks.
**Evidence status:** HYPOTHESIS; full TheoryEquationContract NOT COMPLETE; strong-baseline test NOT RUN; literature novelty NOT CERTIFIED; real-world validation NOT DONE.

### 15 — Metal additive manufacturing
**Projection gap to test:** Melt-pool thermal cycles, grain topology and residual stress.
**Strong modern comparator:** Thermo-mechanical LPBF and microstructure models.
**Proposed experiment:** Measure the stated missing variables directly where possible, construct matched aggregate states with contrasting local histories or topology, then compare out-of-sample outcomes under matched parameter and computational budgets. A domain-specific preregistration must supply signed predictions, primary endpoint, sample-size/power calculation, units, error tolerance and falsifiers before testing. This is a study design, not a completed experiment.
**Conditional economic benefit:** Lower rejection and rework. Formula: affected cost base × verified incremental gain × practical adoption − implementation cost; no numerical incremental saving has been established.
**Earliest controlled test:** 1–4 yr (scenario); experimental tractability medium, not probability of discovery.
**Critical qualification:** Rosenthal is not modern strongest baseline.
**Evidence status:** HYPOTHESIS; full TheoryEquationContract NOT COMPLETE; strong-baseline test NOT RUN; literature novelty NOT CERTIFIED; real-world validation NOT DONE.

### 16 — Direct air capture
**Projection gap to test:** Water/CO2 coadsorption hysteresis and pore-network aging.
**Strong modern comparator:** Competitive adsorption and transient sorbent-cycle models.
**Proposed experiment:** Measure the stated missing variables directly where possible, construct matched aggregate states with contrasting local histories or topology, then compare out-of-sample outcomes under matched parameter and computational budgets. A domain-specific preregistration must supply signed predictions, primary endpoint, sample-size/power calculation, units, error tolerance and falsifiers before testing. This is a study design, not a completed experiment.
**Conditional economic benefit:** Lower regeneration energy and sorbent replacement. Formula: affected cost base × verified incremental gain × practical adoption − implementation cost; no numerical incremental saving has been established.
**Earliest controlled test:** 1–5 yr (scenario); experimental tractability medium, not probability of discovery.
**Critical qualification:** $100/t is an aspiration; no trillion-dollar market established.
**Evidence status:** HYPOTHESIS; full TheoryEquationContract NOT COMPLETE; strong-baseline test NOT RUN; literature novelty NOT CERTIFIED; real-world validation NOT DONE.

### 17 — Corrosion prevention
**Projection gap to test:** Coating defects, electrochemistry and stress/flow histories.
**Strong modern comparator:** Corrosion risk digital twins and physics-based monitoring.
**Proposed experiment:** Measure the stated missing variables directly where possible, construct matched aggregate states with contrasting local histories or topology, then compare out-of-sample outcomes under matched parameter and computational budgets. A domain-specific preregistration must supply signed predictions, primary endpoint, sample-size/power calculation, units, error tolerance and falsifiers before testing. This is a study design, not a completed experiment.
**Conditional economic benefit:** Avoided maintenance and failures. Formula: affected cost base × verified incremental gain × practical adoption − implementation cost; no numerical incremental saving has been established.
**Earliest controlled test:** 1–5 yr (scenario); experimental tractability high, not probability of discovery.
**Critical qualification:** $2.5T corrosion cost and 35% avoidable are external estimates, not incremental gain.
**Evidence status:** HYPOTHESIS; full TheoryEquationContract NOT COMPLETE; strong-baseline test NOT RUN; literature novelty NOT CERTIFIED; real-world validation NOT DONE.

### 18 — Healthcare diagnostic error
**Projection gap to test:** Longitudinal evidence, uncertainty, workflow and escalation.
**Strong modern comparator:** Validated diagnostic decision support and clinical trials.
**Proposed experiment:** Measure the stated missing variables directly where possible, construct matched aggregate states with contrasting local histories or topology, then compare out-of-sample outcomes under matched parameter and computational budgets. A domain-specific preregistration must supply signed predictions, primary endpoint, sample-size/power calculation, units, error tolerance and falsifiers before testing. This is a study design, not a completed experiment.
**Conditional economic benefit:** Avoidable patient harm and care costs. Formula: affected cost base × verified incremental gain × practical adoption − implementation cost; no numerical incremental saving has been established.
**Earliest controlled test:** 2–7 yr (scenario); experimental tractability medium, not probability of discovery.
**Critical qualification:** $870B estimate is unverified and not attributable to AI.
**Evidence status:** HYPOTHESIS; full TheoryEquationContract NOT COMPLETE; strong-baseline test NOT RUN; literature novelty NOT CERTIFIED; real-world validation NOT DONE.

### 19 — Drug discovery
**Projection gap to test:** Assay uncertainty, synthesis feasibility and distribution shift.
**Strong modern comparator:** Modern structure-based and experimental active learning.
**Proposed experiment:** Measure the stated missing variables directly where possible, construct matched aggregate states with contrasting local histories or topology, then compare out-of-sample outcomes under matched parameter and computational budgets. A domain-specific preregistration must supply signed predictions, primary endpoint, sample-size/power calculation, units, error tolerance and falsifiers before testing. This is a study design, not a completed experiment.
**Conditional economic benefit:** Lower R&D cost per successful therapy. Formula: affected cost base × verified incremental gain × practical adoption − implementation cost; no numerical incremental saving has been established.
**Earliest controlled test:** 1–7 yr (scenario); experimental tractability medium, not probability of discovery.
**Critical qualification:** Computational speedups do not equal drug development savings.
**Evidence status:** HYPOTHESIS; full TheoryEquationContract NOT COMPLETE; strong-baseline test NOT RUN; literature novelty NOT CERTIFIED; real-world validation NOT DONE.

### 20 — Grid transmission losses
**Projection gap to test:** Electrical topology, reactive flow, conductor state.
**Strong modern comparator:** AC power flow, HVDC planning, loss optimization.
**Proposed experiment:** Measure the stated missing variables directly where possible, construct matched aggregate states with contrasting local histories or topology, then compare out-of-sample outcomes under matched parameter and computational budgets. A domain-specific preregistration must supply signed predictions, primary endpoint, sample-size/power calculation, units, error tolerance and falsifiers before testing. This is a study design, not a completed experiment.
**Conditional economic benefit:** Reduced electrical losses. Formula: affected cost base × verified incremental gain × practical adoption − implementation cost; no numerical incremental saving has been established.
**Earliest controlled test:** 1–5 yr (scenario); experimental tractability medium, not probability of discovery.
**Critical qualification:** Distinct from congestion and DLR; avoid overlap.
**Evidence status:** HYPOTHESIS; full TheoryEquationContract NOT COMPLETE; strong-baseline test NOT RUN; literature novelty NOT CERTIFIED; real-world validation NOT DONE.

### 21 — Mining haulage efficiency
**Projection gap to test:** Haul cycles, terrain, state-of-charge and dispatch.
**Strong modern comparator:** Fleet routing and hybrid/electric haul optimization.
**Proposed experiment:** Measure the stated missing variables directly where possible, construct matched aggregate states with contrasting local histories or topology, then compare out-of-sample outcomes under matched parameter and computational budgets. A domain-specific preregistration must supply signed predictions, primary endpoint, sample-size/power calculation, units, error tolerance and falsifiers before testing. This is a study design, not a completed experiment.
**Conditional economic benefit:** Fuel and maintenance. Formula: affected cost base × verified incremental gain × practical adoption − implementation cost; no numerical incremental saving has been established.
**Earliest controlled test:** 1–4 yr (scenario); experimental tractability high, not probability of discovery.
**Critical qualification:** Electrification savings already studied.
**Evidence status:** HYPOTHESIS; full TheoryEquationContract NOT COMPLETE; strong-baseline test NOT RUN; literature novelty NOT CERTIFIED; real-world validation NOT DONE.

### 22 — Water treatment energy
**Projection gap to test:** Membrane state, feed salinity, pressure recovery.
**Strong modern comparator:** Modern reverse osmosis energy-recovery and MPC.
**Proposed experiment:** Measure the stated missing variables directly where possible, construct matched aggregate states with contrasting local histories or topology, then compare out-of-sample outcomes under matched parameter and computational budgets. A domain-specific preregistration must supply signed predictions, primary endpoint, sample-size/power calculation, units, error tolerance and falsifiers before testing. This is a study design, not a completed experiment.
**Conditional economic benefit:** Electricity and water cost. Formula: affected cost base × verified incremental gain × practical adoption − implementation cost; no numerical incremental saving has been established.
**Earliest controlled test:** 1–4 yr (scenario); experimental tractability high, not probability of discovery.
**Critical qualification:** RO-PRO claims need site-specific energy accounting.
**Evidence status:** HYPOTHESIS; full TheoryEquationContract NOT COMPLETE; strong-baseline test NOT RUN; literature novelty NOT CERTIFIED; real-world validation NOT DONE.

### 23 — Semiconductor fab energy
**Projection gap to test:** Tool-level thermal states and facility utility timing.
**Strong modern comparator:** Fab digital twins, lithography scheduling and cooling optimization.
**Proposed experiment:** Measure the stated missing variables directly where possible, construct matched aggregate states with contrasting local histories or topology, then compare out-of-sample outcomes under matched parameter and computational budgets. A domain-specific preregistration must supply signed predictions, primary endpoint, sample-size/power calculation, units, error tolerance and falsifiers before testing. This is a study design, not a completed experiment.
**Conditional economic benefit:** Electricity and throughput. Formula: affected cost base × verified incremental gain × practical adoption − implementation cost; no numerical incremental saving has been established.
**Earliest controlled test:** 1–4 yr (scenario); experimental tractability high, not probability of discovery.
**Critical qualification:** cuLitho mask compute claims not directly fab-wide savings.
**Evidence status:** HYPOTHESIS; full TheoryEquationContract NOT COMPLETE; strong-baseline test NOT RUN; literature novelty NOT CERTIFIED; real-world validation NOT DONE.

### 24 — Agricultural climate yield loss
**Projection gap to test:** Heat stress timing, water/nutrient state and cultivar response.
**Strong modern comparator:** Crop process models and breeding trials.
**Proposed experiment:** Measure the stated missing variables directly where possible, construct matched aggregate states with contrasting local histories or topology, then compare out-of-sample outcomes under matched parameter and computational budgets. A domain-specific preregistration must supply signed predictions, primary endpoint, sample-size/power calculation, units, error tolerance and falsifiers before testing. This is a study design, not a completed experiment.
**Conditional economic benefit:** Avoided crop losses. Formula: affected cost base × verified incremental gain × practical adoption − implementation cost; no numerical incremental saving has been established.
**Earliest controlled test:** 2–10 yr (scenario); experimental tractability medium, not probability of discovery.
**Critical qualification:** Yield-loss statistics are not Garden benefit.
**Evidence status:** HYPOTHESIS; full TheoryEquationContract NOT COMPLETE; strong-baseline test NOT RUN; literature novelty NOT CERTIFIED; real-world validation NOT DONE.

### 25 — Aviation fuel efficiency
**Projection gap to test:** Weather, routing, wake, aircraft state and operations.
**Strong modern comparator:** Flight planning and fleet operations optimization.
**Proposed experiment:** Measure the stated missing variables directly where possible, construct matched aggregate states with contrasting local histories or topology, then compare out-of-sample outcomes under matched parameter and computational budgets. A domain-specific preregistration must supply signed predictions, primary endpoint, sample-size/power calculation, units, error tolerance and falsifiers before testing. This is a study design, not a completed experiment.
**Conditional economic benefit:** Fuel burn. Formula: affected cost base × verified incremental gain × practical adoption − implementation cost; no numerical incremental saving has been established.
**Earliest controlled test:** 1–6 yr (scenario); experimental tractability medium, not probability of discovery.
**Critical qualification:** Formation flight certification distinct from software routing.
**Evidence status:** HYPOTHESIS; full TheoryEquationContract NOT COMPLETE; strong-baseline test NOT RUN; literature novelty NOT CERTIFIED; real-world validation NOT DONE.

### 26 — Shipping fuel efficiency
**Projection gap to test:** Hull fouling, wind assistance, route/weather state.
**Strong modern comparator:** Voyage optimization, wind assist and hull monitoring.
**Proposed experiment:** Measure the stated missing variables directly where possible, construct matched aggregate states with contrasting local histories or topology, then compare out-of-sample outcomes under matched parameter and computational budgets. A domain-specific preregistration must supply signed predictions, primary endpoint, sample-size/power calculation, units, error tolerance and falsifiers before testing. This is a study design, not a completed experiment.
**Conditional economic benefit:** Fuel burn. Formula: affected cost base × verified incremental gain × practical adoption − implementation cost; no numerical incremental saving has been established.
**Earliest controlled test:** 1–6 yr (scenario); experimental tractability high, not probability of discovery.
**Critical qualification:** Overlaps shipping decarbonization benefits.
**Evidence status:** HYPOTHESIS; full TheoryEquationContract NOT COMPLETE; strong-baseline test NOT RUN; literature novelty NOT CERTIFIED; real-world validation NOT DONE.

### 27 — Steel energy and carbon
**Projection gap to test:** Ore quality, furnace thermal profile and reduction kinetics.
**Strong modern comparator:** Plant energy integration, DRI and electric furnace models.
**Proposed experiment:** Measure the stated missing variables directly where possible, construct matched aggregate states with contrasting local histories or topology, then compare out-of-sample outcomes under matched parameter and computational budgets. A domain-specific preregistration must supply signed predictions, primary endpoint, sample-size/power calculation, units, error tolerance and falsifiers before testing. This is a study design, not a completed experiment.
**Conditional economic benefit:** Fuel and emissions. Formula: affected cost base × verified incremental gain × practical adoption − implementation cost; no numerical incremental saving has been established.
**Earliest controlled test:** 2–10 yr (scenario); experimental tractability medium, not probability of discovery.
**Critical qualification:** Hydrogen routes may increase near-term cost.
**Evidence status:** HYPOTHESIS; full TheoryEquationContract NOT COMPLETE; strong-baseline test NOT RUN; literature novelty NOT CERTIFIED; real-world validation NOT DONE.

### 28 — Cement carbon capture
**Projection gap to test:** Flue composition, solvent state and heat integration.
**Strong modern comparator:** Capture process optimization and clinker substitution.
**Proposed experiment:** Measure the stated missing variables directly where possible, construct matched aggregate states with contrasting local histories or topology, then compare out-of-sample outcomes under matched parameter and computational budgets. A domain-specific preregistration must supply signed predictions, primary endpoint, sample-size/power calculation, units, error tolerance and falsifiers before testing. This is a study design, not a completed experiment.
**Conditional economic benefit:** Avoided emissions and energy. Formula: affected cost base × verified incremental gain × practical adoption − implementation cost; no numerical incremental saving has been established.
**Earliest controlled test:** 2–10 yr (scenario); experimental tractability medium, not probability of discovery.
**Critical qualification:** Carbon price savings depend on policy.
**Evidence status:** HYPOTHESIS; full TheoryEquationContract NOT COMPLETE; strong-baseline test NOT RUN; literature novelty NOT CERTIFIED; real-world validation NOT DONE.

### 29 — Construction material reuse
**Projection gap to test:** Quality uncertainty, structural grading and logistics topology.
**Strong modern comparator:** Life-cycle assessment and structural reuse certification.
**Proposed experiment:** Measure the stated missing variables directly where possible, construct matched aggregate states with contrasting local histories or topology, then compare out-of-sample outcomes under matched parameter and computational budgets. A domain-specific preregistration must supply signed predictions, primary endpoint, sample-size/power calculation, units, error tolerance and falsifiers before testing. This is a study design, not a completed experiment.
**Conditional economic benefit:** Material and disposal costs. Formula: affected cost base × verified incremental gain × practical adoption − implementation cost; no numerical incremental saving has been established.
**Earliest controlled test:** 1–7 yr (scenario); experimental tractability medium, not probability of discovery.
**Critical qualification:** Single-case reused-wood percentages do not generalize.
**Evidence status:** HYPOTHESIS; full TheoryEquationContract NOT COMPLETE; strong-baseline test NOT RUN; literature novelty NOT CERTIFIED; real-world validation NOT DONE.

### 30 — Textile recycling
**Projection gap to test:** Fiber blend identification, degradation and sorting dynamics.
**Strong modern comparator:** NIR sorting and mechanical/chemical recycling models.
**Proposed experiment:** Measure the stated missing variables directly where possible, construct matched aggregate states with contrasting local histories or topology, then compare out-of-sample outcomes under matched parameter and computational budgets. A domain-specific preregistration must supply signed predictions, primary endpoint, sample-size/power calculation, units, error tolerance and falsifiers before testing. This is a study design, not a completed experiment.
**Conditional economic benefit:** Recovered material and avoided disposal. Formula: affected cost base × verified incremental gain × practical adoption − implementation cost; no numerical incremental saving has been established.
**Earliest controlled test:** 1–7 yr (scenario); experimental tractability medium, not probability of discovery.
**Critical qualification:** Textile waste tonnage not equal economic savings.
**Evidence status:** HYPOTHESIS; full TheoryEquationContract NOT COMPLETE; strong-baseline test NOT RUN; literature novelty NOT CERTIFIED; real-world validation NOT DONE.

### 31 — Data-center cooling
**Projection gap to test:** Chip heat flux, coolant dynamics and facility power state.
**Strong modern comparator:** Liquid cooling, CFD and facility MPC.
**Proposed experiment:** Measure the stated missing variables directly where possible, construct matched aggregate states with contrasting local histories or topology, then compare out-of-sample outcomes under matched parameter and computational budgets. A domain-specific preregistration must supply signed predictions, primary endpoint, sample-size/power calculation, units, error tolerance and falsifiers before testing. This is a study design, not a completed experiment.
**Conditional economic benefit:** Electricity and capital utilization. Formula: affected cost base × verified incremental gain × practical adoption − implementation cost; no numerical incremental saving has been established.
**Earliest controlled test:** 6–36 mo (scenario); experimental tractability high, not probability of discovery.
**Critical qualification:** Reported 40–48% and 75% savings are context-specific, unverified here.
**Evidence status:** HYPOTHESIS; full TheoryEquationContract NOT COMPLETE; strong-baseline test NOT RUN; literature novelty NOT CERTIFIED; real-world validation NOT DONE.

### 32 — Soil carbon verification
**Projection gap to test:** Mineral accessibility, wet/dry microbial memory.
**Strong modern comparator:** Soil carbon process models and MRV protocols.
**Proposed experiment:** Measure the stated missing variables directly where possible, construct matched aggregate states with contrasting local histories or topology, then compare out-of-sample outcomes under matched parameter and computational budgets. A domain-specific preregistration must supply signed predictions, primary endpoint, sample-size/power calculation, units, error tolerance and falsifiers before testing. This is a study design, not a completed experiment.
**Conditional economic benefit:** Cheaper credible carbon measurement. Formula: affected cost base × verified incremental gain × practical adoption − implementation cost; no numerical incremental saving has been established.
**Earliest controlled test:** 1–5 yr (scenario); experimental tractability medium, not probability of discovery.
**Critical qualification:** Requires field verification and permanence controls.
**Evidence status:** HYPOTHESIS; full TheoryEquationContract NOT COMPLETE; strong-baseline test NOT RUN; literature novelty NOT CERTIFIED; real-world validation NOT DONE.

### 33 — Precision chemical reactors
**Projection gap to test:** Intermediate populations and feed pulse histories.
**Strong modern comparator:** Detailed reaction kinetics and real-time spectroscopy.
**Proposed experiment:** Measure the stated missing variables directly where possible, construct matched aggregate states with contrasting local histories or topology, then compare out-of-sample outcomes under matched parameter and computational budgets. A domain-specific preregistration must supply signed predictions, primary endpoint, sample-size/power calculation, units, error tolerance and falsifiers before testing. This is a study design, not a completed experiment.
**Conditional economic benefit:** Higher conversion/selectivity. Formula: affected cost base × verified incremental gain × practical adoption − implementation cost; no numerical incremental saving has been established.
**Earliest controlled test:** 6–24 mo (scenario); experimental tractability high, not probability of discovery.
**Critical qualification:** Overlaps general membrane/process efficiency in some plants.
**Evidence status:** HYPOTHESIS; full TheoryEquationContract NOT COMPLETE; strong-baseline test NOT RUN; literature novelty NOT CERTIFIED; real-world validation NOT DONE.

## Four requested technical proposals — special constraints
- Dynamic line rating: existing real-time thermal line rating is an established field; demonstrate improvement over deployed DLR/forecasting, not static ratings alone. Span-wise wind covariance may matter, but do not presume a free 15–30% capacity increase.
- Bioreactors: modern CFD and process analytical technology already model gradients. A batch failure may have major indirect cost, but 5–10× material write-off is not validated as a universal multiplier.
- Additive manufacturing: Rosenthal-type models are not state of the art; benchmark against modern melt-pool and microstructure prediction. Destructive qualification and material-specific standards are essential.
- Direct air capture: competitive humidity adsorption and hysteresis are researched. A hypothetical $100/ton capture cost does not create a proven trillion-dollar industry.

## Prioritization
Fastest measurable pilot: motor optimization, refrigeration, industrial heat, methane leak detection, membrane operations, building cooling and data-center cooling.
High impact but access-limited: dynamic line rating, semiconductor fab optimization, industrial bioreactors and macroeconomic payment networks.
Long qualification: health diagnostics, drug discovery, aerospace additive manufacturing, steel decarbonization, DAC, agricultural resilience.
Highest priority for *discovery-method evaluation*: choose one problem with raw observations, modern benchmark, hidden mechanism not given to the model, and a blind holdout. Run an independent conventional discovery baseline and Garden under equal budget. This is still pending.

## Verification ledger
New discovery proved: 0. Empirically validated incremental benefits: 0. Strong-baseline benchmark comparisons for these 33: 0. Literature novelty reviews completed: 0. Cross-domain Garden advantage demonstrated: NO. Existing Candidate 026 synthetic thermal experiment remains an engineering test, not evidence of new physics. This register is an additive scientific research artifact; Garden core and canonical sources remain unchanged.



---
# APPENDIX — ORIGINAL EXECUTABLE SOURCE AND MACHINE RESULTS (ARCHIVED IN ONE FILE)

The following blocks preserve the original files exactly as GitHub text content. To rerun, copy a Python block into its stated filename; JSON blocks are archived run outputs, not new validations. The original scripts may contain absolute output paths and require NumPy/SciPy.

## garden_candidate026_harness.py

```python
#!/usr/bin/env python3
"""Reproducible candidate-026 synthetic closure experiment; no empirical/novelty claim."""
import json
import numpy as np
from scipy.linalg import expm

DT=0.25
TRAIN=320
TEST=160

def trajectory(seed, two_body, sigma=0.012):
    rng=np.random.default_rng(seed)
    n=TRAIN+TEST+2
    u=np.zeros(n)
    for t in range(n):
        u[t]=1.2*np.sin(0.073*t)+0.6*np.sin(0.019*t+0.7)+(0.8 if (t//29)%2 else -0.4)+0.2*rng.normal()
    if two_body:
        C1,C2,h,g=2.0,4.0,0.9,0.24
        # C1 dT1/dt = u - g*T1 - h*(T1-T2); C2 dT2/dt = h*(T1-T2)
        A=np.array([[-(g+h)/C1,h/C1],[h/C2,-h/C2]])
        B=np.array([[1/C1],[0.]])
        M=np.zeros((3,3));M[:2,:2]=A;M[:2,2:]=B
        E=expm(M*DT);Ad=E[:2,:2];Bd=E[:2,2]
        x=np.array([0.1,-0.6]); y=[]
        for k in range(n):
            y.append(x[0]);x=Ad@x+Bd*u[k]
    else:
        C,g=2.0,0.35
        a=np.exp(-g/C*DT);b=(1-a)/g
        x=0.1;y=[]
        for k in range(n):
            y.append(x);x=a*x+b*u[k]
    return np.asarray(y)+sigma*rng.normal(size=n),u

def matrices(y,u,p):
    # ARX(p,p) uses current and p-1 previous y and u to predict next sample
    X=[];z=[];ts=[]
    for t in range(p-1,len(y)-1):
        X.append([*([y[t-j] for j in range(p)]),*([u[t-j] for j in range(p)]),1.])
        z.append(y[t+1]);ts.append(t)
    return np.array(X),np.array(z),np.array(ts)

def evaluate(y,u,p):
    X,z,t=matrices(y,u,p)
    tr=t<TRAIN-1;te=t>=TRAIN
    # Fixed ridge is part of the preregistered model, not tuned on test.
    lam=1e-5
    L=np.eye(X.shape[1]);L[-1,-1]=0
    beta=np.linalg.solve(X[tr].T@X[tr]+lam*L,X[tr].T@z[tr])
    pred=X@beta
    train_mse=np.mean((z[tr]-pred[tr])**2)
    test_mse=np.mean((z[te]-pred[te])**2)
    # Training BIC with parameter penalty
    bic=tr.sum()*np.log(max(train_mse,1e-15))+X.shape[1]*np.log(tr.sum())
    return dict(train_mse=float(train_mse),test_mse=float(test_mse),bic=float(bic),coefficients=beta.tolist())

def run():
    # Calibrate the threshold on independent one-body null simulations; measurement noise can make ARX2 look better even when no hidden physical state exists.
    null_calibration=[]
    for seed in range(100):
        yc,uc=trajectory(seed+5000,False)
        bc=evaluate(yc,uc,1);ec=evaluate(yc,uc,2)
        null_calibration.append(1-ec['test_mse']/bc['test_mse'])
    null_threshold=float(np.quantile(null_calibration,0.95))
    allout={}
    for label,two in [('null_one_body',False),('hidden_two_body',True)]:
        entries=[]
        for seed in range(100):
            y,u=trajectory(seed+1000,two)
            b=evaluate(y,u,1);e=evaluate(y,u,2)
            improvement=1-e['test_mse']/b['test_mse']
            # require >= 10% test improvement AND BIC improvement of at least 10
            selected=improvement>null_threshold and e['bic']<=b['bic']-10
            entries.append({'seed':seed,'baseline_test_mse':b['test_mse'],'extension_test_mse':e['test_mse'],'fractional_improvement':improvement,'selected':selected,'delta_bic':e['bic']-b['bic']})
        allout[label]={'n':len(entries),'selection_rate':sum(x['selected'] for x in entries)/len(entries),'median_test_improvement':float(np.median([x['fractional_improvement'] for x in entries])),'median_baseline_mse':float(np.median([x['baseline_test_mse'] for x in entries])),'median_extension_mse':float(np.median([x['extension_test_mse'] for x in entries])),'cases':entries}
    allout['design']={'null_calibration_quantile':0.95,'null_calibration_threshold':null_threshold,'calibration_seeds':100,'dt':DT,'train_steps':TRAIN,'test_steps':TEST,'noise_sd':0.012,'seeds_per_condition':100,'comparison':'ARX(1,1) vs ARX(2,2) with equal train/test sequences','selection_rule':'heldout MSE improvement above independent null 95th percentile AND training BIC decreases by >=10','scope':'synthetic only; comparator is not strongest modern system identification; no novelty claim'}
    return allout
if __name__=='__main__':
    r=run()
    with open('/mnt/data/garden_candidate026_harness_results.json','w') as f:json.dump(r,f,indent=2)
    print('calibrated_null_threshold=',round(r['design']['null_calibration_threshold'],4))
    for key in ['null_one_body','hidden_two_body']:
        a=r[key];print(key,'n=',a['n'],'selection=',a['selection_rate'],'median_gain=',round(a['median_test_improvement'],4),'baseline_mse=',round(a['median_baseline_mse'],7),'extended_mse=',round(a['median_extension_mse'],7))
```

## garden_candidate026_strong_comparator.py

```python
#!/usr/bin/env python3
"""Noise-aware output-error thermal RC benchmark; synthetic research only."""
import argparse, json
import numpy as np
from scipy.linalg import expm
from scipy.optimize import least_squares
from garden_candidate026_harness import trajectory, TRAIN, TEST, DT

def simulate(u, p, order):
    # Parameters positive, initial temperatures unrestricted; zero-order-held forcing.
    if order == 1:
        C,g=np.exp(p[:2]); x=p[2]; a=np.exp(-g/C*DT); b=-np.expm1(-g/C*DT)/g
        y=np.empty(len(u))
        for t,ut in enumerate(u):
            y[t]=x;x=a*x+b*ut
        return y
    C1,C2,h,g=np.exp(p[:4]); x=np.array(p[4:6],float)
    A=np.array([[-(g+h)/C1,h/C1],[h/C2,-h/C2]])
    B=np.array([[1/C1],[0.]])
    M=np.zeros((3,3));M[:2,:2]=A;M[:2,2:]=B
    E=expm(M*DT);ad=E[:2,:2];bd=E[:2,2]
    y=np.empty(len(u))
    for t,ut in enumerate(u):
        y[t]=x[0];x=ad@x+bd*ut
    return y

def fit(y,u,order):
    starts=([np.log(2),np.log(.35),float(y[0])],) if order==1 else ([np.log(2),np.log(4),np.log(.9),np.log(.24),float(y[0]),float(y[0])],)
    best=None
    for start in starts:
        start=np.array(start)
        nphys=2 if order==1 else 4
        lo=np.r_[np.full(nphys,-5.),np.full(order,-20.)]
        hi=np.r_[np.full(nphys,5.),np.full(order,20.)]
        result=least_squares(lambda p:simulate(u[:TRAIN],p,order)-y[:TRAIN],start,bounds=(lo,hi),max_nfev=250,ftol=1e-8,xtol=1e-8,gtol=1e-8)
        sse=float(np.sum(result.fun**2))
        if best is None or sse<best[0]:best=(sse,result.x,result.success)
    sse,p,success=best
    full=simulate(u,p,order)
    test_mse=float(np.mean((full[TRAIN:TRAIN+TEST]-y[TRAIN:TRAIN+TEST])**2))
    bic=TRAIN*np.log(max(sse/TRAIN,1e-15))+len(p)*np.log(TRAIN)
    return dict(bic=float(bic),test_mse=test_mse,fit_success=bool(success),params=p.tolist())

def run(n,noise,seed_start):
    out={'settings':{'n_per_class':n,'noise_sd':noise,'seed_start':seed_start,'selection_rule':'training BIC improvement >=10; output-error model, holdout reported independently','scope':'synthetic, structure-aware comparator; not blind discovery'}}
    for label,two in [('null_one_body',False),('hidden_two_body',True)]:
        cases=[]
        for k in range(n):
            y,u=trajectory(seed_start+k+(100000 if two else 0),two,sigma=noise)
            a=fit(y,u,1);b=fit(y,u,2)
            cases.append({'seed':k,'selected_two_body':b['bic']<=a['bic']-10,'delta_bic':b['bic']-a['bic'],'one_body_test_mse':a['test_mse'],'two_body_test_mse':b['test_mse'],'fit_success':a['fit_success'] and b['fit_success']})
        out[label]={'n':n,'selected':sum(c['selected_two_body'] for c in cases),'selection_rate':float(np.mean([c['selected_two_body'] for c in cases])),'median_one_body_test_mse':float(np.median([c['one_body_test_mse'] for c in cases])),'median_two_body_test_mse':float(np.median([c['two_body_test_mse'] for c in cases])),'cases':cases}
    return out
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--n',type=int,default=20);ap.add_argument('--noise',type=float,default=.012);ap.add_argument('--seed',type=int,default=9100);ap.add_argument('--output',default='garden_candidate026_strong_results.json');a=ap.parse_args()
    r=run(a.n,a.noise,a.seed)
    with open(a.output,'w') as f:json.dump(r,f,indent=2)
    print({k:(r[k]['selected'],r[k]['n']) for k in ['null_one_body','hidden_two_body']})
```

## garden_candidate026_harness_results.json

```json
{
  "null_one_body": {
    "n": 100,
    "selection_rate": 0.03,
    "median_test_improvement": 0.23427863255783482,
    "median_baseline_mse": 0.00027082133338073597,
    "median_extension_mse": 0.0002055136788148182,
    "cases": [
      {
        "seed": 0,
        "baseline_test_mse": 0.00019873583775642013,
        "extension_test_mse": 0.00016647625062907322,
        "fractional_improvement": 0.16232395471060312,
        "selected": false,
        "delta_bic": -113.65984101025742
      },
      {
        "seed": 1,
        "baseline_test_mse": 0.00027828653922571306,
        "extension_test_mse": 0.00020107092744710186,
        "fractional_improvement": 0.2774680083106106,
        "selected": false,
        "delta_bic": -62.455383408767375
      },
      {
        "seed": 2,
        "baseline_test_mse": 0.0002865711384744909,
        "extension_test_mse": 0.00021152500586136782,
        "fractional_improvement": 0.26187610173382236,
        "selected": false,
        "delta_bic": -49.86640303714057
      },
      {
        "seed": 3,
        "baseline_test_mse": 0.0002497210572498129,
        "extension_test_mse": 0.00016859390769214988,
        "fractional_improvement": 0.324871079960654,
        "selected": false,
        "delta_bic": -72.52359008611757
      },
      {
        "seed": 4,
        "baseline_test_mse": 0.00028823632684717106,
        "extension_test_mse": 0.00019679101044466773,
        "fractional_improvement": 0.31725812427171796,
        "selected": false,
        "delta_bic": -91.25610095761158
      },
      {
        "seed": 5,
        "baseline_test_mse": 0.0002462238988134198,
        "extension_test_mse": 0.00018374337566771516,
        "fractional_improvement": 0.25375490944138723,
        "selected": false,
        "delta_bic": -66.60046854957181
      },
      {
        "seed": 6,
        "baseline_test_mse": 0.00025473697219622075,
        "extension_test_mse": 0.00019933237555198625,
        "fractional_improvement": 0.21749727244758577,
        "selected": false,
        "delta_bic": -86.02262764537045
      },
      {
        "seed": 7,
        "baseline_test_mse": 0.0002696805808842687,
        "extension_test_mse": 0.00018181031027744878,
        "fractional_improvement": 0.3258309156658512,
        "selected": false,
        "delta_bic": -77.52041241794132
      },
      {
        "seed": 8,
        "baseline_test_mse": 0.00030815528049112914,
        "extension_test_mse": 0.0002294424586341251,
        "fractional_improvement": 0.2554323318151608,
        "selected": false,
        "delta_bic": -86.86847111564975
      },
      {
        "seed": 9,
        "baseline_test_mse": 0.00021917964556997027,
        "extension_test_mse": 0.0002045279539459371,
        "fractional_improvement": 0.06684786621463801,
        "selected": false,
        "delta_bic": -68.99019165569598
      },
      {
        "seed": 10,
        "baseline_test_mse": 0.00030991191393282,
        "extension_test_mse": 0.00023035287492149194,
        "fractional_improvement": 0.25671500653754853,
        "selected": false,
        "delta_bic": -135.07596171506793
      },
      {
        "seed": 11,
        "baseline_test_mse": 0.0002644264194164256,
        "extension_test_mse": 0.00020704659075294413,
        "fractional_improvement": 0.21699733631047735,
        "selected": false,
        "delta_bic": -48.75845760014363
      },
      {
        "seed": 12,
        "baseline_test_mse": 0.00028922187426545977,
        "extension_test_mse": 0.00021295900847914868,
        "fractional_improvement": 0.26368291119057574,
        "selected": false,
        "delta_bic": -72.06347114942628
      },
      {
        "seed": 13,
        "baseline_test_mse": 0.0003178638519126059,
        "extension_test_mse": 0.00023662193183713297,
        "fractional_improvement": 0.25558716282658567,
        "selected": false,
        "delta_bic": -58.484016983293714
      },
      {
        "seed": 14,
        "baseline_test_mse": 0.00026572730006332396,
        "extension_test_mse": 0.0002016628527593627,
        "fractional_improvement": 0.24109095034155092,
        "selected": false,
        "delta_bic": -57.335251317382244
      },
      {
        "seed": 15,
        "baseline_test_mse": 0.0002494946691671808,
        "extension_test_mse": 0.00018909047783035208,
        "fractional_improvement": 0.24210614013701925,
        "selected": false,
        "delta_bic": -72.15549719201908
      },
      {
        "seed": 16,
        "baseline_test_mse": 0.0003397885220479293,
        "extension_test_mse": 0.00021978507898421686,
        "fractional_improvement": 0.3531709733467253,
        "selected": true,
        "delta_bic": -64.24895913087494
      },
      {
        "seed": 17,
        "baseline_test_mse": 0.00026460270544061994,
        "extension_test_mse": 0.00020378238731729665,
        "fractional_improvement": 0.22985523909154482,
        "selected": false,
        "delta_bic": -53.11171758794899
      },
      {
        "seed": 18,
        "baseline_test_mse": 0.0002949099169842335,
        "extension_test_mse": 0.00019641195270142002,
        "fractional_improvement": 0.33399339462727995,
        "selected": false,
        "delta_bic": -59.18233650503589
      },
      {
        "seed": 19,
        "baseline_test_mse": 0.00022017017117148877,
        "extension_test_mse": 0.00018396193592402267,
        "fractional_improvement": 0.16445568014417267,
        "selected": false,
        "delta_bic": -80.48032629077125
      },
      {
        "seed": 20,
        "baseline_test_mse": 0.0002556605471589855,
        "extension_test_mse": 0.00019908301348167307,
        "fractional_improvement": 0.22129943124204077,
        "selected": false,
        "delta_bic": -44.81713611756186
      },
      {
        "seed": 21,
        "baseline_test_mse": 0.0002647700698106152,
        "extension_test_mse": 0.00017840873787085702,
        "fractional_improvement": 0.3261748278479162,
        "selected": false,
        "delta_bic": -82.51460442553434
      },
      {
        "seed": 22,
        "baseline_test_mse": 0.0002517426538592286,
        "extension_test_mse": 0.00022072385085699275,
        "fractional_improvement": 0.12321631843756276,
        "selected": false,
        "delta_bic": -51.48570027312553
      },
      {
        "seed": 23,
        "baseline_test_mse": 0.00029668034098836175,
        "extension_test_mse": 0.0002330000171033878,
        "fractional_improvement": 0.21464288355888073,
        "selected": false,
        "delta_bic": -116.00907142552069
      },
      {
        "seed": 24,
        "baseline_test_mse": 0.00023654513478154,
        "extension_test_mse": 0.00017772951897291088,
        "fractional_improvement": 0.24864436913043242,
        "selected": false,
        "delta_bic": -93.42712007746559
      },
      {
        "seed": 25,
        "baseline_test_mse": 0.0002562913330576512,
        "extension_test_mse": 0.000205928490607553,
        "fractional_improvement": 0.19650622535397777,
        "selected": false,
        "delta_bic": -88.60215173788129
      },
      {
        "seed": 26,
        "baseline_test_mse": 0.0002993608843863014,
        "extension_test_mse": 0.00022450057572502685,
        "fractional_improvement": 0.25006710150105416,
        "selected": false,
        "delta_bic": -57.34911469153758
      },
      {
        "seed": 27,
        "baseline_test_mse": 0.0002536926789277872,
        "extension_test_mse": 0.0002055634374415421,
        "fractional_improvement": 0.18971474340394723,
        "selected": false,
        "delta_bic": -74.88915503231465
      },
      {
        "seed": 28,
        "baseline_test_mse": 0.00026758640959065214,
        "extension_test_mse": 0.00021238460532953637,
        "fractional_improvement": 0.20629524625545181,
        "selected": false,
        "delta_bic": -84.65221868936533
      },
      {
        "seed": 29,
        "baseline_test_mse": 0.00030742945215215677,
        "extension_test_mse": 0.00022426920802621537,
        "fractional_improvement": 0.2705018778902898,
        "selected": false,
        "delta_bic": -66.72002921785679
      },
      {
        "seed": 30,
        "baseline_test_mse": 0.00027818997696322194,
        "extension_test_mse": 0.00021412445282512822,
        "fractional_improvement": 0.23029414947815852,
        "selected": false,
        "delta_bic": -75.26071672981061
      },
      {
        "seed": 31,
        "baseline_test_mse": 0.00023806135917334994,
        "extension_test_mse": 0.00018275821357971429,
        "fractional_improvement": 0.2323062666938962,
        "selected": false,
        "delta_bic": -76.27239956589574
      },
      {
        "seed": 32,
        "baseline_test_mse": 0.0002551439529589555,
        "extension_test_mse": 0.00019709427231447184,
        "fractional_improvement": 0.2275173680240895,
        "selected": false,
        "delta_bic": -108.63758846384644
      },
      {
        "seed": 33,
        "baseline_test_mse": 0.00023653810668924265,
        "extension_test_mse": 0.0001721646594720561,
        "fractional_improvement": 0.2721483152046982,
        "selected": false,
        "delta_bic": -82.2258424008678
      },
      {
        "seed": 34,
        "baseline_test_mse": 0.00033400279135619565,
        "extension_test_mse": 0.00023517105550461862,
        "fractional_improvement": 0.29590092780445776,
        "selected": false,
        "delta_bic": -84.78074237431474
      },
      {
        "seed": 35,
        "baseline_test_mse": 0.0003529869872636391,
        "extension_test_mse": 0.00027780939465253847,
        "fractional_improvement": 0.2129755354266133,
        "selected": false,
        "delta_bic": -53.90524108703039
      },
      {
        "seed": 36,
        "baseline_test_mse": 0.00024131239716918676,
        "extension_test_mse": 0.00018588270369774694,
        "fractional_improvement": 0.22970097732930583,
        "selected": false,
        "delta_bic": -70.34111025168067
      },
      {
        "seed": 37,
        "baseline_test_mse": 0.00023530739390847157,
        "extension_test_mse": 0.0001897175204780408,
        "fractional_improvement": 0.19374603013182,
        "selected": false,
        "delta_bic": -109.25109353162406
      },
      {
        "seed": 38,
        "baseline_test_mse": 0.000309222947344839,
        "extension_test_mse": 0.00022060435081967372,
        "fractional_improvement": 0.28658480001595643,
        "selected": false,
        "delta_bic": -65.52665478441804
      },
      {
        "seed": 39,
        "baseline_test_mse": 0.00028327360366239813,
        "extension_test_mse": 0.00021212551065232326,
        "fractional_improvement": 0.2511638645119517,
        "selected": false,
        "delta_bic": -78.80745531413413
      },
      {
        "seed": 40,
        "baseline_test_mse": 0.0002565095584831722,
        "extension_test_mse": 0.00022930692860620075,
        "fractional_improvement": 0.10604918599458746,
        "selected": false,
        "delta_bic": -70.21033716553802
      },
      {
        "seed": 41,
        "baseline_test_mse": 0.0002937163265884116,
        "extension_test_mse": 0.00022825712735498164,
        "fractional_improvement": 0.22286537487975178,
        "selected": false,
        "delta_bic": -56.918429619696326
      },
      {
        "seed": 42,
        "baseline_test_mse": 0.0002587222871710074,
        "extension_test_mse": 0.00018880500835113834,
        "fractional_improvement": 0.27024064909280865,
        "selected": false,
        "delta_bic": -82.77616873558372
      },
      {
        "seed": 43,
        "baseline_test_mse": 0.00030334406497913344,
        "extension_test_mse": 0.00024219857789238843,
        "fractional_improvement": 0.20157139745243113,
        "selected": false,
        "delta_bic": -63.88604610038419
      },
      {
        "seed": 44,
        "baseline_test_mse": 0.00031139362308928094,
        "extension_test_mse": 0.00023199962531581403,
        "fractional_improvement": 0.2549634670929132,
        "selected": false,
        "delta_bic": -46.99290012164147
      },
      {
        "seed": 45,
        "baseline_test_mse": 0.0003245961264613478,
        "extension_test_mse": 0.00022395183269623552,
        "fractional_improvement": 0.31006005790120483,
        "selected": false,
        "delta_bic": -86.29716154150583
      },
      {
        "seed": 46,
        "baseline_test_mse": 0.0002580830456130225,
        "extension_test_mse": 0.00018965625552591812,
        "fractional_improvement": 0.2651347744466158,
        "selected": false,
        "delta_bic": -70.04109971888874
      },
      {
        "seed": 47,
        "baseline_test_mse": 0.0002550139349760091,
        "extension_test_mse": 0.00017746814491806528,
        "fractional_improvement": 0.30408452018607957,
        "selected": false,
        "delta_bic": -52.2891432487354
      },
      {
        "seed": 48,
        "baseline_test_mse": 0.00029565354973068626,
        "extension_test_mse": 0.000237577777969481,
        "fractional_improvement": 0.19643184333185593,
        "selected": false,
        "delta_bic": -55.526975647466315
      },      {
        "seed": 49,
        "baseline_test_mse": 0.0002886466783747069,
        "extension_test_mse": 0.00022480925418624434,
        "fractional_improvement": 0.22116112524805132,
        "selected": false,
        "delta_bic": -84.00070883411672
      },
      {
        "seed": 50,
        "baseline_test_mse": 0.000244485345236849,
        "extension_test_mse": 0.0002106851769103933,
        "fractional_improvement": 0.13825028364669978,
        "selected": false,
        "delta_bic": -89.9178766327318
      },
      {
        "seed": 51,
        "baseline_test_mse": 0.0003228140740845782,
        "extension_test_mse": 0.0002812153499546095,
        "fractional_improvement": 0.12886279586146465,
        "selected": false,
        "delta_bic": -58.086054323517146
      },
      {
        "seed": 52,
        "baseline_test_mse": 0.00020460442295593633,
        "extension_test_mse": 0.00016577697329124571,
        "fractional_improvement": 0.18976837892234866,
        "selected": false,
        "delta_bic": -107.56513111778577
      },
      {
        "seed": 53,
        "baseline_test_mse": 0.00029246883069899125,
        "extension_test_mse": 0.0002054639201880943,
        "fractional_improvement": 0.2974843859530534,
        "selected": false,
        "delta_bic": -78.49664395152467
      },
      {
        "seed": 54,
        "baseline_test_mse": 0.0002548123019559472,
        "extension_test_mse": 0.0002259522768024434,
        "fractional_improvement": 0.11325993655711808,
        "selected": false,
        "delta_bic": -110.8459354563197
      },
      {
        "seed": 55,
        "baseline_test_mse": 0.0003077293833963271,
        "extension_test_mse": 0.00020475810736275948,
        "fractional_improvement": 0.33461632716739986,
        "selected": false,
        "delta_bic": -101.83833663504993
      },
      {
        "seed": 56,
        "baseline_test_mse": 0.0002997432936157013,
        "extension_test_mse": 0.00023055873317615825,
        "fractional_improvement": 0.2308127051150778,
        "selected": false,
        "delta_bic": -96.47743929142143
      },
      {
        "seed": 57,
        "baseline_test_mse": 0.0002353431559755305,
        "extension_test_mse": 0.00020392828919169566,
        "fractional_improvement": 0.1334853637600626,
        "selected": false,
        "delta_bic": -94.89465704629538
      },
      {
        "seed": 58,
        "baseline_test_mse": 0.0002798083759843391,
        "extension_test_mse": 0.00023089632694063737,
        "fractional_improvement": 0.17480552135594152,
        "selected": false,
        "delta_bic": -74.45150003557956
      },
      {
        "seed": 59,
        "baseline_test_mse": 0.00029042500094604833,
        "extension_test_mse": 0.00022014726526419293,
        "fractional_improvement": 0.24198238943936767,
        "selected": false,
        "delta_bic": -75.39459556854763
      },
      {
        "seed": 60,
        "baseline_test_mse": 0.000260961733623587,
        "extension_test_mse": 0.00020797747975297723,
        "fractional_improvement": 0.2030345719079052,
        "selected": false,
        "delta_bic": -105.97533629554118
      },
      {
        "seed": 61,
        "baseline_test_mse": 0.00035553701076446317,
        "extension_test_mse": 0.0002655675921544438,
        "fractional_improvement": 0.2530521883405902,
        "selected": false,
        "delta_bic": -85.00726856550227
      },
      {
        "seed": 62,
        "baseline_test_mse": 0.0002911335353974393,
        "extension_test_mse": 0.00022485466216318165,
        "fractional_improvement": 0.22765798225126277,
        "selected": false,
        "delta_bic": -57.09966100650399
      },
      {
        "seed": 63,
        "baseline_test_mse": 0.00017385438098854345,
        "extension_test_mse": 0.00014903887660364706,
        "fractional_improvement": 0.14273729683309888,
        "selected": false,
        "delta_bic": -56.620629883963375
      },
      {
        "seed": 64,
        "baseline_test_mse": 0.0002993381269437084,
        "extension_test_mse": 0.00023149576122285007,
        "fractional_improvement": 0.22664124484755765,
        "selected": false,
        "delta_bic": -75.84346216994163
      },
      {
        "seed": 65,
        "baseline_test_mse": 0.00029249889295314635,
        "extension_test_mse": 0.000203727454699761,
        "fractional_improvement": 0.30349324524659005,
        "selected": false,
        "delta_bic": -60.56720388227859
      },
      {
        "seed": 66,
        "baseline_test_mse": 0.00026382123791762166,
        "extension_test_mse": 0.00018766502102431784,
        "fractional_improvement": 0.2886659826722655,
        "selected": false,
        "delta_bic": -66.75302890350622
      },
      {
        "seed": 67,
        "baseline_test_mse": 0.0002674488064803012,
        "extension_test_mse": 0.0002060906205786896,
        "fractional_improvement": 0.22942030181066042,
        "selected": false,
        "delta_bic": -59.356378530131224
      },
      {
        "seed": 68,
        "baseline_test_mse": 0.0002922870081989449,
        "extension_test_mse": 0.00022365186107630887,
        "fractional_improvement": 0.23482106695594074,
        "selected": false,
        "delta_bic": -77.1868315104889
      },
      {
        "seed": 69,
        "baseline_test_mse": 0.0002467091661793763,
        "extension_test_mse": 0.00019419987411324618,
        "fractional_improvement": 0.21283883724025032,
        "selected": false,
        "delta_bic": -91.21566954224909
      },
      {
        "seed": 70,
        "baseline_test_mse": 0.00028276106589440357,
        "extension_test_mse": 0.0002192149684955807,
        "fractional_improvement": 0.22473425468891817,
        "selected": false,
        "delta_bic": -80.15202773578949
      },
      {
        "seed": 71,
        "baseline_test_mse": 0.00028755929139703427,
        "extension_test_mse": 0.0002103336981166224,
        "fractional_improvement": 0.26855537480715996,
        "selected": false,
        "delta_bic": -85.13447344166161
      },
      {
        "seed": 72,
        "baseline_test_mse": 0.0003058051833173975,
        "extension_test_mse": 0.0002156802317184016,
        "fractional_improvement": 0.29471361675859664,
        "selected": false,
        "delta_bic": -60.05283131533042
      },
      {
        "seed": 73,
        "baseline_test_mse": 0.0002719620858772033,
        "extension_test_mse": 0.00019862104672890336,
        "fractional_improvement": 0.26967376320762215,
        "selected": false,
        "delta_bic": -53.42134556152632
      },
      {
        "seed": 74,
        "baseline_test_mse": 0.00030441512224929477,
        "extension_test_mse": 0.0002210158385382417,
        "fractional_improvement": 0.27396563973177024,
        "selected": false,
        "delta_bic": -64.98648772978868
      },
      {
        "seed": 75,
        "baseline_test_mse": 0.0002827611379188747,
        "extension_test_mse": 0.00021758220231684477,
        "fractional_improvement": 0.2305088177312754,
        "selected": false,
        "delta_bic": -97.6286011078978
      },
      {
        "seed": 76,
        "baseline_test_mse": 0.00025421414284128486,
        "extension_test_mse": 0.00019264503230777646,
        "fractional_improvement": 0.24219388365008565,
        "selected": false,
        "delta_bic": -57.062432127695956
      },
      {
        "seed": 77,
        "baseline_test_mse": 0.00022318188539895844,
        "extension_test_mse": 0.00018601191699319801,
        "fractional_improvement": 0.1665456331248194,
        "selected": false,
        "delta_bic": -81.06999069821995
      },
      {
        "seed": 78,
        "baseline_test_mse": 0.00026889195217415696,
        "extension_test_mse": 0.00018391083564564187,
        "fractional_improvement": 0.3160418742226774,
        "selected": false,
        "delta_bic": -76.31533411853297
      },
      {
        "seed": 79,
        "baseline_test_mse": 0.0002861602193797375,
        "extension_test_mse": 0.00022473859652987255,
        "fractional_improvement": 0.2146406757130621,
        "selected": false,
        "delta_bic": -83.85741132813428
      },
      {
        "seed": 80,
        "baseline_test_mse": 0.00029405169528491345,
        "extension_test_mse": 0.0002282380413026154,
        "fractional_improvement": 0.22381661128846642,
        "selected": false,
        "delta_bic": -73.2103889787445
      },
      {
        "seed": 81,
        "baseline_test_mse": 0.0002791966343696168,
        "extension_test_mse": 0.00021828937605745962,
        "fractional_improvement": 0.2181518357113309,
        "selected": false,
        "delta_bic": -27.31357774044136
      },
      {
        "seed": 82,
        "baseline_test_mse": 0.00026306115684153925,
        "extension_test_mse": 0.0002040414332624091,
        "fractional_improvement": 0.22435742428777505,
        "selected": false,
        "delta_bic": -67.74455771164867
      },
      {
        "seed": 83,
        "baseline_test_mse": 0.00023054924201742875,
        "extension_test_mse": 0.0001785843947484105,
        "fractional_improvement": 0.2253958712433758,
        "selected": false,
        "delta_bic": -93.02210581588133
      },
      {
        "seed": 84,
        "baseline_test_mse": 0.00025519456669246426,
        "extension_test_mse": 0.00020035360077040446,
        "fractional_improvement": 0.21489864236862377,
        "selected": false,
        "delta_bic": -61.24048220223585
      },
      {
        "seed": 85,
        "baseline_test_mse": 0.00023686872363212625,
        "extension_test_mse": 0.0001765496328675616,
        "fractional_improvement": 0.2546519854526865,
        "selected": false,
        "delta_bic": -79.30547113751345
      },
      {
        "seed": 86,
        "baseline_test_mse": 0.0003190766838691943,
        "extension_test_mse": 0.00024750052949142873,
        "fractional_improvement": 0.2243227349294763,
        "selected": false,
        "delta_bic": -58.2186323487781
      },
      {
        "seed": 87,
        "baseline_test_mse": 0.00022448741680398455,
        "extension_test_mse": 0.0001823529588907302,
        "fractional_improvement": 0.1876918471116127,
        "selected": false,
        "delta_bic": -54.09027060426797
      },
      {
        "seed": 88,
        "baseline_test_mse": 0.00024648639229910913,
        "extension_test_mse": 0.0001900286949556804,
        "fractional_improvement": 0.22904995613274182,
        "selected": false,
        "delta_bic": -84.5915084517219
      },
      {
        "seed": 89,
        "baseline_test_mse": 0.00023977355951035546,
        "extension_test_mse": 0.00017403467463585393,
        "fractional_improvement": 0.27417070092610596,
        "selected": false,
        "delta_bic": -51.32731586467162
      },
      {
        "seed": 90,
        "baseline_test_mse": 0.00031626835150767873,
        "extension_test_mse": 0.0002289582994686019,
        "fractional_improvement": 0.27606319640540133,
        "selected": false,
        "delta_bic": -60.32936117351983
      },
      {
        "seed": 91,
        "baseline_test_mse": 0.00029264336525977694,
        "extension_test_mse": 0.00020215255346346214,
        "fractional_improvement": 0.3092187369974607,
        "selected": false,
        "delta_bic": -54.92011069312002
      },
      {
        "seed": 92,
        "baseline_test_mse": 0.0003275983782728194,
        "extension_test_mse": 0.00020363975245227085,
        "fractional_improvement": 0.3783859568355906,
        "selected": true,
        "delta_bic": -85.25019736219565
      },
      {
        "seed": 93,
        "baseline_test_mse": 0.0002628418543127558,
        "extension_test_mse": 0.00018879143565523072,
        "fractional_improvement": 0.281729935482088,
        "selected": false,
        "delta_bic": -58.00629596212548
      },
      {
        "seed": 94,
        "baseline_test_mse": 0.00026795367244195756,
        "extension_test_mse": 0.0001915376052588764,
        "fractional_improvement": 0.2851838770735039,
        "selected": false,
        "delta_bic": -42.20272839769177
      },
      {
        "seed": 95,
        "baseline_test_mse": 0.00035299166856989057,
        "extension_test_mse": 0.0002201993012147566,
        "fractional_improvement": 0.37619122256660775,
        "selected": true,
        "delta_bic": -71.04446321967953
      },
      {
        "seed": 96,
        "baseline_test_mse": 0.0002581232874100935,
        "extension_test_mse": 0.00019653352846048976,
        "fractional_improvement": 0.23860597611153544,
        "selected": false,
        "delta_bic": -85.99606438952333
      },
      {
        "seed": 97,
        "baseline_test_mse": 0.00022305952120550704,
        "extension_test_mse": 0.00018990607178236518,
        "fractional_improvement": 0.14863050563350422,
        "selected": false,
        "delta_bic": -77.19225727667254
      },
      {
        "seed": 98,
        "baseline_test_mse": 0.00027926164308594457,
        "extension_test_mse": 0.00021398808833919674,
        "fractional_improvement": 0.2337361981597289,
        "selected": false,
        "delta_bic": -60.50960057665952
      },      {
        "seed": 99,
        "baseline_test_mse": 0.00028565239072205574,
        "extension_test_mse": 0.00019681261649651225,
        "fractional_improvement": 0.31100658391473424,
        "selected": false,
        "delta_bic": -43.729547578578604
      }
    ]
  },
  "hidden_two_body": {
    "n": 100,
    "selection_rate": 0.94,
    "median_test_improvement": 0.42682542639779375,
    "median_baseline_mse": 0.0010072891914217046,
    "median_extension_mse": 0.0005803607637812262,
    "cases": [
      {
        "seed": 0,
        "baseline_test_mse": 0.000931166283960303,
        "extension_test_mse": 0.00045589214951625973,
        "fractional_improvement": 0.5104073704458836,
        "selected": true,
        "delta_bic": -142.2564373522673
      },
      {
        "seed": 1,
        "baseline_test_mse": 0.0009509512033152075,
        "extension_test_mse": 0.0005793437056320881,
        "fractional_improvement": 0.39077451754371917,
        "selected": true,
        "delta_bic": -178.79590943936955
      },
      {
        "seed": 2,
        "baseline_test_mse": 0.0010354555775450157,
        "extension_test_mse": 0.000603912922624424,
        "fractional_improvement": 0.4167659765218955,
        "selected": true,
        "delta_bic": -196.65234110382653
      },
      {
        "seed": 3,
        "baseline_test_mse": 0.0009740356630674754,
        "extension_test_mse": 0.0005475500085152399,
        "fractional_improvement": 0.4378542498219504,
        "selected": true,
        "delta_bic": -177.60774860107313
      },
      {
        "seed": 4,
        "baseline_test_mse": 0.0011340981133290443,
        "extension_test_mse": 0.0006185600560076522,
        "fractional_improvement": 0.45457976806616485,
        "selected": true,
        "delta_bic": -159.36492928763755
      },
      {
        "seed": 5,
        "baseline_test_mse": 0.0009877111216330284,
        "extension_test_mse": 0.0005409421941596958,
        "fractional_improvement": 0.45232752541519317,
        "selected": true,
        "delta_bic": -159.3956435333398
      },
      {
        "seed": 6,
        "baseline_test_mse": 0.0009864020306292766,
        "extension_test_mse": 0.0005383990855128435,
        "fractional_improvement": 0.454178855279352,
        "selected": true,
        "delta_bic": -145.72339158261457
      },
      {
        "seed": 7,
        "baseline_test_mse": 0.0009325851021041311,
        "extension_test_mse": 0.0005766794159457965,
        "fractional_improvement": 0.38163346739651716,
        "selected": true,
        "delta_bic": -178.45348012808927
      },
      {
        "seed": 8,
        "baseline_test_mse": 0.0010961599586664919,
        "extension_test_mse": 0.0006567881691704792,
        "fractional_improvement": 0.40082816930342924,
        "selected": true,
        "delta_bic": -179.0272854169184
      },
      {
        "seed": 9,
        "baseline_test_mse": 0.0009426963053229814,
        "extension_test_mse": 0.0004276619256961624,
        "fractional_improvement": 0.5463417823095857,
        "selected": true,
        "delta_bic": -208.40740575627524
      },
      {
        "seed": 10,
        "baseline_test_mse": 0.001088171635794564,
        "extension_test_mse": 0.0006314054326590406,
        "fractional_improvement": 0.4197556599625948,
        "selected": true,
        "delta_bic": -158.45755040590166
      },
      {
        "seed": 11,
        "baseline_test_mse": 0.001040189266344104,
        "extension_test_mse": 0.000528247826802892,
        "fractional_improvement": 0.49216181718592855,
        "selected": true,
        "delta_bic": -209.56091279347083
      },
      {
        "seed": 12,
        "baseline_test_mse": 0.0010419215329086043,
        "extension_test_mse": 0.0005987953982707529,
        "fractional_improvement": 0.4252970311505422,
        "selected": true,
        "delta_bic": -205.5122186066742
      },
      {
        "seed": 13,
        "baseline_test_mse": 0.0011332710500576541,
        "extension_test_mse": 0.0006729675282373793,
        "fractional_improvement": 0.40617248785880244,
        "selected": true,
        "delta_bic": -197.591173840593
      },
      {
        "seed": 14,
        "baseline_test_mse": 0.0009705903319177083,
        "extension_test_mse": 0.0005618626132331451,
        "fractional_improvement": 0.42111249746017176,
        "selected": true,
        "delta_bic": -204.14992836782767
      },
      {
        "seed": 15,
        "baseline_test_mse": 0.001105962604928769,
        "extension_test_mse": 0.0005329265478810852,
        "fractional_improvement": 0.5181333026034736,
        "selected": true,
        "delta_bic": -186.89123099647577
      },
      {
        "seed": 16,
        "baseline_test_mse": 0.000987646664474323,
        "extension_test_mse": 0.0007106268894150769,
        "fractional_improvement": 0.2804846966264909,
        "selected": false,
        "delta_bic": -157.50264741859064
      },
      {
        "seed": 17,
        "baseline_test_mse": 0.001061871309697895,
        "extension_test_mse": 0.0005509126402414145,
        "fractional_improvement": 0.4811869995826984,
        "selected": true,
        "delta_bic": -181.47946206730194
      },
      {
        "seed": 18,
        "baseline_test_mse": 0.001056234498018817,
        "extension_test_mse": 0.0006627837466761293,
        "fractional_improvement": 0.3725032197686071,
        "selected": true,
        "delta_bic": -165.5528637409393
      },
      {
        "seed": 19,
        "baseline_test_mse": 0.0008684175191698624,
        "extension_test_mse": 0.00043949090212378557,
        "fractional_improvement": 0.49391750808539225,
        "selected": true,
        "delta_bic": -174.78914739405582
      },
      {
        "seed": 20,
        "baseline_test_mse": 0.0009639782565436441,
        "extension_test_mse": 0.0005119778078337138,
        "fractional_improvement": 0.46889070955872325,
        "selected": true,
        "delta_bic": -225.53178310226258
      },
      {
        "seed": 21,
        "baseline_test_mse": 0.0010666755000319445,
        "extension_test_mse": 0.0005867367443322342,
        "fractional_improvement": 0.44993885739884076,
        "selected": true,
        "delta_bic": -153.32636849620394
      },
      {
        "seed": 22,
        "baseline_test_mse": 0.0010347818949561448,
        "extension_test_mse": 0.000511897225506027,
        "fractional_improvement": 0.5053090627105321,
        "selected": true,
        "delta_bic": -209.56418542626534
      },
      {
        "seed": 23,
        "baseline_test_mse": 0.0010326918277093033,
        "extension_test_mse": 0.000592725448156885,
        "fractional_improvement": 0.42603840540536,
        "selected": true,
        "delta_bic": -155.0678199849499
      },
      {
        "seed": 24,
        "baseline_test_mse": 0.0009741255701136522,
        "extension_test_mse": 0.000511289941676626,
        "fractional_improvement": 0.4751293289457813,
        "selected": true,
        "delta_bic": -178.52145759757695
      },
      {
        "seed": 25,
        "baseline_test_mse": 0.0010059794987172146,
        "extension_test_mse": 0.0005400750618273482,
        "fractional_improvement": 0.46313512102778365,
        "selected": true,
        "delta_bic": -160.63773738862255
      },
      {
        "seed": 26,
        "baseline_test_mse": 0.0009886367935733652,
        "extension_test_mse": 0.0006331290903842926,
        "fractional_improvement": 0.3595938422482867,
        "selected": true,
        "delta_bic": -177.00027150804408
      },
      {
        "seed": 27,
        "baseline_test_mse": 0.0009906500460025794,
        "extension_test_mse": 0.000524842342489702,
        "fractional_improvement": 0.4702040901249446,
        "selected": true,
        "delta_bic": -179.4154553648791
      },
      {
        "seed": 28,
        "baseline_test_mse": 0.001008396223439421,
        "extension_test_mse": 0.0005680475200292055,
        "fractional_improvement": 0.43668222190309436,
        "selected": true,
        "delta_bic": -151.99886830597416
      },
      {
        "seed": 29,
        "baseline_test_mse": 0.0010070430241087057,
        "extension_test_mse": 0.000652921234032089,
        "fractional_improvement": 0.35164514484377274,
        "selected": true,
        "delta_bic": -208.13891900190265
      },
      {
        "seed": 30,
        "baseline_test_mse": 0.001176751701376267,
        "extension_test_mse": 0.0005784469420818424,
        "fractional_improvement": 0.5084375561936123,
        "selected": true,
        "delta_bic": -164.37546385514952
      },
      {
        "seed": 31,
        "baseline_test_mse": 0.0010692063029304995,
        "extension_test_mse": 0.000522825768985507,
        "fractional_improvement": 0.5110150701950251,
        "selected": true,
        "delta_bic": -159.0878200227162
      },
      {
        "seed": 32,
        "baseline_test_mse": 0.0009434466779259172,
        "extension_test_mse": 0.0005537418535009567,
        "fractional_improvement": 0.4130650237506709,
        "selected": true,
        "delta_bic": -142.917553392012
      },
      {
        "seed": 33,
        "baseline_test_mse": 0.0009655691390469053,
        "extension_test_mse": 0.0005034944509518325,
        "fractional_improvement": 0.47855163282370217,
        "selected": true,
        "delta_bic": -164.2394635580963
      },
      {
        "seed": 34,
        "baseline_test_mse": 0.001011637652384741,
        "extension_test_mse": 0.0007670770536839552,
        "fractional_improvement": 0.24174722849063723,
        "selected": false,
        "delta_bic": -175.68183783035283
      },
      {
        "seed": 35,
        "baseline_test_mse": 0.0010489318173868623,
        "extension_test_mse": 0.0007064365745052282,
        "fractional_improvement": 0.3265181179601081,
        "selected": false,
        "delta_bic": -195.53712112777157
      },
      {
        "seed": 36,
        "baseline_test_mse": 0.0008876228372770754,
        "extension_test_mse": 0.0005022230401930949,
        "fractional_improvement": 0.43419319659040745,
        "selected": true,
        "delta_bic": -216.08776008805216
      },
      {
        "seed": 37,
        "baseline_test_mse": 0.0009615306294524156,
        "extension_test_mse": 0.0005001826710218718,
        "fractional_improvement": 0.4798057849631664,
        "selected": true,
        "delta_bic": -163.351178605305
      },
      {
        "seed": 38,
        "baseline_test_mse": 0.0010371671107535874,
        "extension_test_mse": 0.0006212318220985437,
        "fractional_improvement": 0.4010301564160016,
        "selected": true,
        "delta_bic": -201.42787151046468
      },
      {
        "seed": 39,
        "baseline_test_mse": 0.0010081075647408676,
        "extension_test_mse": 0.0005892452397832663,
        "fractional_improvement": 0.4154936830230702,
        "selected": true,
        "delta_bic": -187.8096190791839
      },
      {
        "seed": 40,
        "baseline_test_mse": 0.0009523247406205403,
        "extension_test_mse": 0.0005156648757784922,
        "fractional_improvement": 0.4585199210066915,
        "selected": true,
        "delta_bic": -172.6465366243342
      },
      {
        "seed": 41,
        "baseline_test_mse": 0.0009186949247452626,
        "extension_test_mse": 0.0005793494256757616,
        "fractional_improvement": 0.3693777879132132,
        "selected": true,
        "delta_bic": -167.84288535698488
      },
      {
        "seed": 42,
        "baseline_test_mse": 0.0011166178765029504,
        "extension_test_mse": 0.0005801097726219624,
        "fractional_improvement": 0.48047601168739695,
        "selected": true,
        "delta_bic": -152.9250820725165
      },
      {
        "seed": 43,
        "baseline_test_mse": 0.0010656515257562844,
        "extension_test_mse": 0.0006428034164873556,
        "fractional_improvement": 0.3967977327005062,
        "selected": true,
        "delta_bic": -208.45018707740337
      },
      {
        "seed": 44,
        "baseline_test_mse": 0.0010569139433976116,
        "extension_test_mse": 0.0006366979480562121,
        "fractional_improvement": 0.39758771086939293,
        "selected": true,
        "delta_bic": -186.18456597085333
      },
      {
        "seed": 45,
        "baseline_test_mse": 0.0010705872505926712,
        "extension_test_mse": 0.0006717132715851347,
        "fractional_improvement": 0.37257493846178535,
        "selected": true,
        "delta_bic": -167.83509439208865
      },
      {
        "seed": 46,
        "baseline_test_mse": 0.0010294835172922083,
        "extension_test_mse": 0.0005651192836961252,
        "fractional_improvement": 0.45106524368401146,
        "selected": true,
        "delta_bic": -203.6980514168008
      },
      {
        "seed": 47,
        "baseline_test_mse": 0.0010692882281742792,
        "extension_test_mse": 0.0005860669585731574,
        "fractional_improvement": 0.4519092765345243,
        "selected": true,
        "delta_bic": -181.34092847271768      },
      {
        "seed": 48,
        "baseline_test_mse": 0.0010327801261308897,
        "extension_test_mse": 0.0006146864572004122,
        "fractional_improvement": 0.40482350342737927,
        "selected": true,
        "delta_bic": -205.36241289527015
      },
      {
        "seed": 49,
        "baseline_test_mse": 0.0010075863723288721,
        "extension_test_mse": 0.0006225788507967839,
        "fractional_improvement": 0.38210870264373065,
        "selected": true,
        "delta_bic": -183.52612796447647
      },
      {
        "seed": 50,
        "baseline_test_mse": 0.0008666730183465599,
        "extension_test_mse": 0.0004723551429430209,
        "fractional_improvement": 0.4549788294503725,
        "selected": true,
        "delta_bic": -141.138628911272
      },
      {
        "seed": 51,
        "baseline_test_mse": 0.00092399569390097,
        "extension_test_mse": 0.0006238258988972943,
        "fractional_improvement": 0.32486059944327694,
        "selected": false,
        "delta_bic": -179.95590470227398
      },
      {
        "seed": 52,
        "baseline_test_mse": 0.0009501497190012652,
        "extension_test_mse": 0.00045892404466731947,
        "fractional_improvement": 0.5169981788241644,
        "selected": true,
        "delta_bic": -132.46503318228315
      },
      {
        "seed": 53,
        "baseline_test_mse": 0.0009508311732057911,
        "extension_test_mse": 0.0006286130079852244,
        "fractional_improvement": 0.33888052295781024,
        "selected": true,
        "delta_bic": -194.23877122889417
      },
      {
        "seed": 54,
        "baseline_test_mse": 0.0009753572507595445,
        "extension_test_mse": 0.0005378776093481462,
        "fractional_improvement": 0.4485327207756109,
        "selected": true,
        "delta_bic": -128.1881208721902
      },
      {
        "seed": 55,
        "baseline_test_mse": 0.0011191240964748437,
        "extension_test_mse": 0.0006672735524982732,
        "fractional_improvement": 0.40375374402165554,
        "selected": true,
        "delta_bic": -183.13005444137798
      },
      {
        "seed": 56,
        "baseline_test_mse": 0.0010713867537012868,
        "extension_test_mse": 0.0006171156691859379,
        "fractional_improvement": 0.4240028943292351,
        "selected": true,
        "delta_bic": -142.9707023099927
      },
      {
        "seed": 57,
        "baseline_test_mse": 0.0009521676947447144,
        "extension_test_mse": 0.0004863064598760173,
        "fractional_improvement": 0.48926385282752016,
        "selected": true,
        "delta_bic": -164.9066932389037
      },
      {
        "seed": 58,
        "baseline_test_mse": 0.0008731136542402143,
        "extension_test_mse": 0.0005737783020444705,
        "fractional_improvement": 0.3428366407306116,
        "selected": true,
        "delta_bic": -172.26570453886507
      },
      {
        "seed": 59,
        "baseline_test_mse": 0.00098057344970835,
        "extension_test_mse": 0.0006314331484561624,
        "fractional_improvement": 0.35605726562964934,
        "selected": true,
        "delta_bic": -191.04502734711195
      },
      {
        "seed": 60,
        "baseline_test_mse": 0.0009933193010457433,
        "extension_test_mse": 0.0005685636036856229,
        "fractional_improvement": 0.4276124473902275,
        "selected": true,
        "delta_bic": -153.05921598465784
      },
      {
        "seed": 61,
        "baseline_test_mse": 0.0010053301081007111,
        "extension_test_mse": 0.0007273277999373849,
        "fractional_improvement": 0.27652838199438146,
        "selected": false,
        "delta_bic": -168.51119665117358
      },
      {
        "seed": 62,
        "baseline_test_mse": 0.0009748663535775817,
        "extension_test_mse": 0.0005991185970253233,
        "fractional_improvement": 0.3854351472623223,
        "selected": true,
        "delta_bic": -214.70610636915399
      },
      {
        "seed": 63,
        "baseline_test_mse": 0.0008546210911351526,
        "extension_test_mse": 0.0003588989298902655,
        "fractional_improvement": 0.5800490607907218,
        "selected": true,
        "delta_bic": -197.73352182181634
      },
      {
        "seed": 64,
        "baseline_test_mse": 0.0009243716331369208,
        "extension_test_mse": 0.0006008789382589454,
        "fractional_improvement": 0.3499595652672508,
        "selected": true,
        "delta_bic": -167.98984336671356
      },
      {
        "seed": 65,
        "baseline_test_mse": 0.0010060034296368976,
        "extension_test_mse": 0.0006231023976634237,
        "fractional_improvement": 0.38061603041619496,
        "selected": true,
        "delta_bic": -181.96609530593605
      },
      {
        "seed": 66,
        "baseline_test_mse": 0.0010009981772699393,
        "extension_test_mse": 0.0005490379955542127,
        "fractional_improvement": 0.4515094952004558,
        "selected": true,
        "delta_bic": -202.0261987651038
      },
      {
        "seed": 67,
        "baseline_test_mse": 0.0010572400969446646,
        "extension_test_mse": 0.0005543764781988136,
        "fractional_improvement": 0.47563805061791053,
        "selected": true,
        "delta_bic": -177.72111435688157
      },
      {
        "seed": 68,
        "baseline_test_mse": 0.0009443910033788268,
        "extension_test_mse": 0.000594579339259638,
        "fractional_improvement": 0.37040978034271643,
        "selected": true,
        "delta_bic": -152.17048368882752
      },
      {
        "seed": 69,
        "baseline_test_mse": 0.0009420182968847063,
        "extension_test_mse": 0.0005139656056775973,
        "fractional_improvement": 0.45439955107315544,
        "selected": true,
        "delta_bic": -149.3606749928781
      },
      {
        "seed": 70,
        "baseline_test_mse": 0.0010728753045213522,
        "extension_test_mse": 0.0005966991517028921,
        "fractional_improvement": 0.44383177691921916,
        "selected": true,
        "delta_bic": -221.68646110284635
      },
      {
        "seed": 71,
        "baseline_test_mse": 0.00104854483162641,
        "extension_test_mse": 0.0006039638251534976,
        "fractional_improvement": 0.42399809055690796,
        "selected": true,
        "delta_bic": -155.57946603236178
      },
      {
        "seed": 72,
        "baseline_test_mse": 0.0010075353587347038,
        "extension_test_mse": 0.0006349589706295529,
        "fractional_improvement": 0.36978988863779894,
        "selected": true,
        "delta_bic": -166.4238523081831
      },
      {
        "seed": 73,
        "baseline_test_mse": 0.0010957839875332567,
        "extension_test_mse": 0.0005806117549404902,
        "fractional_improvement": 0.47014031821406876,
        "selected": true,
        "delta_bic": -216.55663459631933
      },
      {
        "seed": 74,
        "baseline_test_mse": 0.0010497075411592361,
        "extension_test_mse": 0.0006115969103061122,
        "fractional_improvement": 0.41736446931618676,
        "selected": true,
        "delta_bic": -214.54992225180877
      },
      {
        "seed": 75,
        "baseline_test_mse": 0.0010210141630192765,
        "extension_test_mse": 0.000590997185606586,
        "fractional_improvement": 0.42116651559570173,
        "selected": true,
        "delta_bic": -157.5144299815097
      },
      {
        "seed": 76,
        "baseline_test_mse": 0.0010559883388456324,
        "extension_test_mse": 0.000540599098794947,
        "fractional_improvement": 0.4880633820389437,
        "selected": true,
        "delta_bic": -177.28829194538503
      },
      {
        "seed": 77,
        "baseline_test_mse": 0.0010236543816832201,
        "extension_test_mse": 0.00046260756536361836,
        "fractional_improvement": 0.548082269131754,
        "selected": true,
        "delta_bic": -198.56307425122804
      },
      {
        "seed": 78,
        "baseline_test_mse": 0.0010387324628059777,
        "extension_test_mse": 0.0005922127935807155,
        "fractional_improvement": 0.4298697549309831,
        "selected": true,
        "delta_bic": -189.76880728587685
      },
      {
        "seed": 79,
        "baseline_test_mse": 0.000906311768735253,
        "extension_test_mse": 0.0005906984346174624,
        "fractional_improvement": 0.34823925386980814,
        "selected": true,
        "delta_bic": -176.6875050762401
      },
      {
        "seed": 80,
        "baseline_test_mse": 0.0009831932828093118,
        "extension_test_mse": 0.000596963638486453,
        "fractional_improvement": 0.39283185826826605,
        "selected": true,
        "delta_bic": -170.78642427216846
      },
      {
        "seed": 81,
        "baseline_test_mse": 0.0010202758256349503,
        "extension_test_mse": 0.0005818928404475747,
        "fractional_improvement": 0.42967104989923277,
        "selected": true,
        "delta_bic": -205.30632737460428
      },
      {
        "seed": 82,
        "baseline_test_mse": 0.0009650779447060802,
        "extension_test_mse": 0.0005412833562340015,
        "fractional_improvement": 0.4391299073787741,
        "selected": true,
        "delta_bic": -177.79628326794227
      },
      {
        "seed": 83,
        "baseline_test_mse": 0.000908527754601769,
        "extension_test_mse": 0.0004977864498117976,
        "fractional_improvement": 0.45209549483714984,
        "selected": true,
        "delta_bic": -135.233678934806
      },
      {
        "seed": 84,
        "baseline_test_mse": 0.0010553906262471037,
        "extension_test_mse": 0.000525133411574025,
        "fractional_improvement": 0.5024274439111107,
        "selected": true,
        "delta_bic": -168.3937285982979
      },
      {
        "seed": 85,
        "baseline_test_mse": 0.0010105551427363408,
        "extension_test_mse": 0.000511247971158638,
        "fractional_improvement": 0.4940919604106895,
        "selected": true,
        "delta_bic": -177.62448479345676
      },
      {
        "seed": 86,
        "baseline_test_mse": 0.0010691142791486336,
        "extension_test_mse": 0.0006589355070689756,
        "fractional_improvement": 0.38366223338284766,
        "selected": true,
        "delta_bic": -181.06266988485868
      },
      {
        "seed": 87,
        "baseline_test_mse": 0.0008711140509705646,
        "extension_test_mse": 0.0004706344742286651,
        "fractional_improvement": 0.4597326564709858,
        "selected": true,
        "delta_bic": -182.54234304430702
      },
      {
        "seed": 88,
        "baseline_test_mse": 0.0010212667762497913,
        "extension_test_mse": 0.0005361075363651267,
        "fractional_improvement": 0.4750563233499331,
        "selected": true,
        "delta_bic": -159.12476670026444
      },
      {
        "seed": 89,
        "baseline_test_mse": 0.0009400033705567559,
        "extension_test_mse": 0.0005281813915855658,
        "fractional_improvement": 0.4381069173478298,
        "selected": true,
        "delta_bic": -187.30418237157164
      },
      {
        "seed": 90,
        "baseline_test_mse": 0.0010429039738561229,
        "extension_test_mse": 0.0006646948097024638,
        "fractional_improvement": 0.362650036470027,
        "selected": true,
        "delta_bic": -177.92457835992036
      },
      {
        "seed": 91,
        "baseline_test_mse": 0.0010558690988310686,
        "extension_test_mse": 0.0006516121945481764,
        "fractional_improvement": 0.3828664980634786,
        "selected": true,
        "delta_bic": -210.2871240999084
      },
      {
        "seed": 92,
        "baseline_test_mse": 0.0010773862192852068,
        "extension_test_mse": 0.0007051357904738606,
        "fractional_improvement": 0.3455125210885992,
        "selected": true,
        "delta_bic": -150.89585428269447
      },
      {
        "seed": 93,
        "baseline_test_mse": 0.0009344000173210275,
        "extension_test_mse": 0.0005666253954599812,
        "fractional_improvement": 0.3935944082230166,
        "selected": true,
        "delta_bic": -203.60841107141323
      },
      {
        "seed": 94,
        "baseline_test_mse": 0.0010283599350043,
        "extension_test_mse": 0.0005958665154458671,
        "fractional_improvement": 0.4205661897520585,
        "selected": true,
        "delta_bic": -216.0285718700984
      },
      {
        "seed": 95,
        "baseline_test_mse": 0.0009238155756243623,
        "extension_test_mse": 0.0007782507590377014,
        "fractional_improvement": 0.15756913005962336,
        "selected": false,
        "delta_bic": -236.92635540206538
      },
      {
        "seed": 96,
        "baseline_test_mse": 0.0009619407481941634,
        "extension_test_mse": 0.0005481030643309453,
        "fractional_improvement": 0.43021120026374726,
        "selected": true,
        "delta_bic": -157.15122733277576
      },
      {
        "seed": 97,
        "baseline_test_mse": 0.0009449242707187386,
        "extension_test_mse": 0.0004723855533454715,
        "fractional_improvement": 0.5000810456628864,
        "selected": true,
        "delta_bic": -172.96919548609912      },
      {
        "seed": 98,
        "baseline_test_mse": 0.0009648582215787646,
        "extension_test_mse": 0.00058962918310469,
        "fractional_improvement": 0.3888955186183729,
        "selected": true,
        "delta_bic": -194.1258179651545
      },
      {
        "seed": 99,
        "baseline_test_mse": 0.0010137526513780116,
        "extension_test_mse": 0.0006303505663360575,
        "fractional_improvement": 0.3782008209998652,
        "selected": true,
        "delta_bic": -187.96252213954222
      }
    ]
  },
  "design": {
    "null_calibration_quantile": 0.95,
    "null_calibration_threshold": 0.3349669840926629,
    "calibration_seeds": 100,
    "dt": 0.25,
    "train_steps": 320,
    "test_steps": 160,
    "noise_sd": 0.012,
    "seeds_per_condition": 100,
    "comparison": "ARX(1,1) vs ARX(2,2) with equal train/test sequences",
    "selection_rule": "heldout MSE improvement above independent null 95th percentile AND training BIC decreases by >=10",
    "scope": "synthetic only; comparator is not strongest modern system identification; no novelty claim"
  }
}
```

## garden_candidate026_strong_results.json

```json
{
  "settings": {
    "n_per_class": 20,
    "noise_sd": 0.012,
    "seed_start": 9100,
    "selection_rule": "training BIC improvement >=10; output-error model, holdout reported independently",
    "scope": "synthetic, structure-aware comparator; not blind discovery"
  },
  "null_one_body": {
    "n": 20,
    "selected": 0,
    "selection_rate": 0.0,
    "median_one_body_test_mse": 0.00014255991593650828,
    "median_two_body_test_mse": 0.00014238829717013737,
    "cases": [
      {
        "seed": 0,
        "selected_two_body": false,
        "delta_bic": 16.66201087961508,
        "one_body_test_mse": 0.00015684928445602138,
        "two_body_test_mse": 0.00015686561752899063,
        "fit_success": true
      },
      {
        "seed": 1,
        "selected_two_body": false,
        "delta_bic": 16.62367690515748,
        "one_body_test_mse": 0.00015615777803504034,
        "two_body_test_mse": 0.0001560533688002183,
        "fit_success": true
      },
      {
        "seed": 2,
        "selected_two_body": false,
        "delta_bic": 17.23229949216966,
        "one_body_test_mse": 0.00014152032139551463,
        "two_body_test_mse": 0.00014152539035769098,
        "fit_success": true
      },
      {
        "seed": 3,
        "selected_two_body": false,
        "delta_bic": 16.27620393793859,
        "one_body_test_mse": 0.00017643229452801056,
        "two_body_test_mse": 0.00017651011617180528,
        "fit_success": true
      },
      {
        "seed": 4,
        "selected_two_body": false,
        "delta_bic": 14.746907353672668,
        "one_body_test_mse": 0.0001490042968507361,
        "two_body_test_mse": 0.0001482839103178329,
        "fit_success": true
      },
      {
        "seed": 5,
        "selected_two_body": false,
        "delta_bic": 15.346535176593989,
        "one_body_test_mse": 0.00014197919999438306,
        "two_body_test_mse": 0.00014198847935118316,
        "fit_success": true
      },
      {
        "seed": 6,
        "selected_two_body": false,
        "delta_bic": 14.135857221133847,
        "one_body_test_mse": 0.0001485792641453727,
        "two_body_test_mse": 0.0001494300272784113,
        "fit_success": true
      },
      {
        "seed": 7,
        "selected_two_body": false,
        "delta_bic": 11.33548601389748,
        "one_body_test_mse": 0.00013779700250837686,
        "two_body_test_mse": 0.00013993009284183597,
        "fit_success": true
      },
      {
        "seed": 8,
        "selected_two_body": false,
        "delta_bic": 16.286969299730117,
        "one_body_test_mse": 0.00013939018307104252,
        "two_body_test_mse": 0.00013879468256711223,
        "fit_success": true
      },
      {
        "seed": 9,
        "selected_two_body": false,
        "delta_bic": 13.35569074863588,
        "one_body_test_mse": 0.00014314063187863353,
        "two_body_test_mse": 0.00014278811498909155,
        "fit_success": true
      },
      {
        "seed": 10,
        "selected_two_body": false,
        "delta_bic": 12.1479628970269,
        "one_body_test_mse": 0.0001350831535784048,
        "two_body_test_mse": 0.00013599077691469878,
        "fit_success": true
      },
      {
        "seed": 11,
        "selected_two_body": false,
        "delta_bic": 15.7039402780415,
        "one_body_test_mse": 0.00014568402660198958,
        "two_body_test_mse": 0.00014661512408935677,
        "fit_success": true
      },
      {
        "seed": 12,
        "selected_two_body": false,
        "delta_bic": 16.61457186062262,
        "one_body_test_mse": 0.00011293501114262362,
        "two_body_test_mse": 0.00011296027480824605,
        "fit_success": true
      },
      {
        "seed": 13,
        "selected_two_body": false,
        "delta_bic": 16.41846595285233,
        "one_body_test_mse": 9.865936423235743e-05,
        "two_body_test_mse": 9.863984297239492e-05,
        "fit_success": true
      },
      {
        "seed": 14,
        "selected_two_body": false,
        "delta_bic": 16.29381403333946,
        "one_body_test_mse": 0.00015509509572934175,
        "two_body_test_mse": 0.00015515379840436096,
        "fit_success": true
      },
      {
        "seed": 15,
        "selected_two_body": false,
        "delta_bic": 16.29077960704626,
        "one_body_test_mse": 0.00013082687795578778,
        "two_body_test_mse": 0.00013195939316450027,
        "fit_success": true
      },
      {
        "seed": 16,
        "selected_two_body": false,
        "delta_bic": 15.383975554776953,
        "one_body_test_mse": 0.00014180189976825835,
        "two_body_test_mse": 0.00014171003587185152,
        "fit_success": true
      },
      {
        "seed": 17,
        "selected_two_body": false,
        "delta_bic": 16.821861551854,
        "one_body_test_mse": 0.00012187629564208149,
        "two_body_test_mse": 0.00012211789489789362,
        "fit_success": true
      },
      {
        "seed": 18,
        "selected_two_body": false,
        "delta_bic": 15.980636140839579,
        "one_body_test_mse": 0.00016332494659008695,
        "two_body_test_mse": 0.0001634611505429217,
        "fit_success": true
      },
      {
        "seed": 19,
        "selected_two_body": false,
        "delta_bic": 16.530113906308543,
        "one_body_test_mse": 0.0001468680817966044,
        "two_body_test_mse": 0.00014653941685051594,
        "fit_success": true
      }
    ]
  },
  "hidden_two_body": {
    "n": 20,
    "selected": 20,
    "selection_rate": 1.0,
    "median_one_body_test_mse": 0.14034082639592027,
    "median_two_body_test_mse": 0.00015104904379459458,
    "cases": [
      {
        "seed": 0,
        "selected_two_body": true,
        "delta_bic": -2224.271865054028,
        "one_body_test_mse": 0.13670878896968788,
        "two_body_test_mse": 0.00017329737253183466,
        "fit_success": true
      },
      {
        "seed": 1,
        "selected_two_body": true,
        "delta_bic": -2253.6835650236444,
        "one_body_test_mse": 0.1447332185700308,
        "two_body_test_mse": 0.0001437717178780509,
        "fit_success": true
      },
      {
        "seed": 2,
        "selected_two_body": true,
        "delta_bic": -2271.9687422752745,
        "one_body_test_mse": 0.14224221992038572,
        "two_body_test_mse": 0.00016304009686487166,
        "fit_success": true
      },
      {
        "seed": 3,
        "selected_two_body": true,
        "delta_bic": -2192.0310452480753,
        "one_body_test_mse": 0.13261065042464665,
        "two_body_test_mse": 0.00016145273675245657,
        "fit_success": true
      },
      {
        "seed": 4,
        "selected_two_body": true,
        "delta_bic": -2182.512320145861,
        "one_body_test_mse": 0.14329948157558,
        "two_body_test_mse": 0.00015366329482786488,
        "fit_success": true
      },
      {
        "seed": 5,
        "selected_two_body": true,
        "delta_bic": -2212.92242219475,
        "one_body_test_mse": 0.13439063597581968,
        "two_body_test_mse": 0.000139061365207882,
        "fit_success": true
      },
      {
        "seed": 6,
        "selected_two_body": true,
        "delta_bic": -2215.989153958835,
        "one_body_test_mse": 0.14380767187942173,
        "two_body_test_mse": 0.00013498836291495707,
        "fit_success": true
      },
      {
        "seed": 7,
        "selected_two_body": true,
        "delta_bic": -2218.1019358847807,
        "one_body_test_mse": 0.14336935045939833,
        "two_body_test_mse": 0.00014740077262304058,
        "fit_success": true
      },
      {
        "seed": 8,
        "selected_two_body": true,
        "delta_bic": -2274.1334441241943,
        "one_body_test_mse": 0.14486219379079227,
        "two_body_test_mse": 0.00015436319796592737,
        "fit_success": true
      },
      {
        "seed": 9,
        "selected_two_body": true,
        "delta_bic": -2238.8697164658106,
        "one_body_test_mse": 0.13991201079110427,
        "two_body_test_mse": 0.00013389043432298023,
        "fit_success": true
      },
      {
        "seed": 10,
        "selected_two_body": true,
        "delta_bic": -2209.0295900584038,
        "one_body_test_mse": 0.13887642033946737,
        "two_body_test_mse": 0.00014466120314670524,
        "fit_success": true
      },
      {
        "seed": 11,
        "selected_two_body": true,
        "delta_bic": -2260.3159844837564,
        "one_body_test_mse": 0.13955738863012737,
        "two_body_test_mse": 0.00015368484101271128,
        "fit_success": true
      },
      {
        "seed": 12,
        "selected_two_body": true,
        "delta_bic": -2192.432503149486,
        "one_body_test_mse": 0.14064372420388105,
        "two_body_test_mse": 0.00014451420471018025,
        "fit_success": true
      },
      {
        "seed": 13,
        "selected_two_body": true,
        "delta_bic": -2217.6728655586894,
        "one_body_test_mse": 0.13662950467753862,
        "two_body_test_mse": 0.0001590389622988972,
        "fit_success": true
      },
      {
        "seed": 14,
        "selected_two_body": true,
        "delta_bic": -2198.6552564930944,
        "one_body_test_mse": 0.1393308573453668,
        "two_body_test_mse": 0.00013016486956951367,
        "fit_success": true
      },
      {
        "seed": 15,
        "selected_two_body": true,
        "delta_bic": -2212.4155204115687,
        "one_body_test_mse": 0.13892998223125907,
        "two_body_test_mse": 0.00016228554834689024,
        "fit_success": true
      },
      {
        "seed": 16,
        "selected_two_body": true,
        "delta_bic": -2195.348967856825,
        "one_body_test_mse": 0.1400379285879595,
        "two_body_test_mse": 0.0001612286276923376,
        "fit_success": true
      },
      {
        "seed": 17,
        "selected_two_body": true,
        "delta_bic": -2249.0780960371903,
        "one_body_test_mse": 0.14497225614373616,
        "two_body_test_mse": 0.00014735071326666183,
        "fit_success": true
      },
      {
        "seed": 18,
        "selected_two_body": true,
        "delta_bic": -2233.850174328479,
        "one_body_test_mse": 0.14106711129527555,
        "two_body_test_mse": 0.00016537643104541302,
        "fit_success": true
      },
      {
        "seed": 19,
        "selected_two_body": true,
        "delta_bic": -2189.0659758720035,
        "one_body_test_mse": 0.1438338563863643,
        "two_body_test_mse": 0.00014843479276132427,
        "fit_success": true
      }
    ]
  }
}
```

## garden_candidate026_strong_results_high_noise.json

```json
{
  "settings": {
    "n_per_class": 12,
    "noise_sd": 0.024,
    "seed_start": 20000,
    "selection_rule": "training BIC improvement >=10; output-error model, holdout reported independently",
    "scope": "synthetic, structure-aware comparator; not blind discovery"
  },
  "null_one_body": {
    "n": 12,
    "selected": 0,
    "selection_rate": 0.0,
    "median_one_body_test_mse": 0.0005756285124799893,
    "median_two_body_test_mse": 0.000576069886389842,
    "cases": [
      {
        "seed": 0,
        "selected_two_body": false,
        "delta_bic": 15.7673779160109,
        "one_body_test_mse": 0.0005062516057914952,
        "two_body_test_mse": 0.0005048952548625293,
        "fit_success": true
      },
      {
        "seed": 1,
        "selected_two_body": false,
        "delta_bic": 16.957627750847678,
        "one_body_test_mse": 0.0005800886734957207,
        "two_body_test_mse": 0.0005736290950819489,
        "fit_success": true
      },
      {
        "seed": 2,
        "selected_two_body": false,
        "delta_bic": 15.136055321002004,
        "one_body_test_mse": 0.0005778766777919754,
        "two_body_test_mse": 0.0005795814868940266,
        "fit_success": true
      },
      {
        "seed": 3,
        "selected_two_body": false,
        "delta_bic": 17.259531012786738,
        "one_body_test_mse": 0.0005733803471680033,
        "two_body_test_mse": 0.0005735796319220863,
        "fit_success": true
      },
      {
        "seed": 4,
        "selected_two_body": false,
        "delta_bic": 17.298523860387377,
        "one_body_test_mse": 0.0005872063971715834,
        "two_body_test_mse": 0.0005872386459212254,
        "fit_success": true
      },
      {
        "seed": 5,
        "selected_two_body": false,
        "delta_bic": 15.0480928987904,
        "one_body_test_mse": 0.0005690493599791637,
        "two_body_test_mse": 0.0005785106776977349,
        "fit_success": true
      },
      {
        "seed": 6,
        "selected_two_body": false,
        "delta_bic": 10.348280343327588,
        "one_body_test_mse": 0.0005059677104947377,
        "two_body_test_mse": 0.0005087044292988492,
        "fit_success": true
      },
      {
        "seed": 7,
        "selected_two_body": false,
        "delta_bic": 15.76882448601782,
        "one_body_test_mse": 0.0005306577964467234,
        "two_body_test_mse": 0.0005302331130088123,
        "fit_success": true
      },
      {
        "seed": 8,
        "selected_two_body": false,
        "delta_bic": 13.714377542331022,
        "one_body_test_mse": 0.0006903524115653088,
        "two_body_test_mse": 0.0007016698810257539,
        "fit_success": true
      },
      {
        "seed": 9,
        "selected_two_body": false,
        "delta_bic": 16.48119671532777,
        "one_body_test_mse": 0.0006627856375363542,
        "two_body_test_mse": 0.0006618602342260236,
        "fit_success": true
      },
      {
        "seed": 10,
        "selected_two_body": false,
        "delta_bic": 15.095362267318706,
        "one_body_test_mse": 0.000664182538572646,
        "two_body_test_mse": 0.0006668384631118181,
        "fit_success": true
      },
      {
        "seed": 11,
        "selected_two_body": false,
        "delta_bic": 16.907107596612605,
        "one_body_test_mse": 0.0005539073283680285,
        "two_body_test_mse": 0.0005542926083952267,
        "fit_success": true
      }
    ]
  },
  "hidden_two_body": {
    "n": 12,
    "selected": 12,
    "selection_rate": 1.0,
    "median_one_body_test_mse": 0.1416331587718357,
    "median_two_body_test_mse": 0.0005658233858947532,
    "cases": [
      {
        "seed": 0,
        "selected_two_body": true,
        "delta_bic": -1765.984347708308,
        "one_body_test_mse": 0.14249106778518522,
        "two_body_test_mse": 0.0006883567427452853,
        "fit_success": true
      },
      {
        "seed": 1,
        "selected_two_body": true,
        "delta_bic": -1796.4073115450176,
        "one_body_test_mse": 0.13506837919394538,
        "two_body_test_mse": 0.0005832979223974895,
        "fit_success": true
      },
      {
        "seed": 2,
        "selected_two_body": true,
        "delta_bic": -1742.798976852671,
        "one_body_test_mse": 0.14164971379117608,
        "two_body_test_mse": 0.0004964844419233889,
        "fit_success": true
      },
      {
        "seed": 3,
        "selected_two_body": true,
        "delta_bic": -1759.4478478601436,
        "one_body_test_mse": 0.13946554602515931,
        "two_body_test_mse": 0.0005936929532263965,
        "fit_success": true
      },
      {
        "seed": 4,
        "selected_two_body": true,
        "delta_bic": -1791.6782069053004,
        "one_body_test_mse": 0.14608703430860986,
        "two_body_test_mse": 0.00047486619942145505,
        "fit_success": true
      },
      {
        "seed": 5,
        "selected_two_body": true,
        "delta_bic": -1743.2247208671117,
        "one_body_test_mse": 0.13794907362122982,
        "two_body_test_mse": 0.0005569619181398598,
        "fit_success": true
      },
      {
        "seed": 6,
        "selected_two_body": true,
        "delta_bic": -1815.449851312178,
        "one_body_test_mse": 0.13846395402821796,
        "two_body_test_mse": 0.0005746848536496465,
        "fit_success": true
      },
      {
        "seed": 7,
        "selected_two_body": true,
        "delta_bic": -1793.7962949269684,
        "one_body_test_mse": 0.1335409975934418,
        "two_body_test_mse": 0.0004986772244578266,
        "fit_success": true
      },
      {
        "seed": 8,
        "selected_two_body": true,
        "delta_bic": -1766.5738396126021,
        "one_body_test_mse": 0.14606389162941108,
        "two_body_test_mse": 0.0005393622435879788,
        "fit_success": true
      },
      {
        "seed": 9,
        "selected_two_body": true,
        "delta_bic": -1761.1827136975207,
        "one_body_test_mse": 0.1416166037524953,
        "two_body_test_mse": 0.0005099747818620873,
        "fit_success": true
      },
      {
        "seed": 10,
        "selected_two_body": true,
        "delta_bic": -1766.6280302357989,
        "one_body_test_mse": 0.14169198192736338,
        "two_body_test_mse": 0.0006445407513893927,
        "fit_success": true
      },
      {
        "seed": 11,
        "selected_two_body": true,
        "delta_bic": -1757.6165406513546,
        "one_body_test_mse": 0.14297118234811937,
        "two_body_test_mse": 0.0006003968270390358,
        "fit_success": true
      }
    ]
  }
}
```
