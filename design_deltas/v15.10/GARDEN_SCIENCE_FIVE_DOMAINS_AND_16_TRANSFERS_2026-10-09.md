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
