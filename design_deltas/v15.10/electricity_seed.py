"""Bounded, curated physical seed for a noncanonical Garden research adapter.

No graph coverage percentage establishes physical completeness. Generic laws are
imported science; equation contracts are scoped modelling commitments, not new laws.
No grid-control or deployment permission is represented by this dataset.
"""
from __future__ import annotations
import copy
import hashlib
from pathlib import Path

CORE_OBJECTS = ['TIME','SPACE','THING','EVENT','ACTION','AGENCY','RULE','VALUE','CONTEXT','CLAIM']
CORE_RELATIONS = ['identifies','causes','governs','values','frames','acts','obeys','assesses','contextualizes','controls','partOf','dependsOn','owns','delegates','references','derivedFrom','equivalentTo','contradicts','supports','blocks','hasHypothesis','supersedes','conflictsWith','originatesFrom']
DESIGN_FORMS = ['CONSTRUCT','CONTRACT','STATE','RELATION','PROCESS','RULE','PROJECTION']
FACETS = ['IdentityLifecycle','ScopeContext','EpistemicsProvenance','AuthorityHumanBoundary','EffectsSafety','DependencyValidity','ResourceTermination','PrivacyRetention','AuditExplanation','RecoveryEvolution']

STAGES = [
(1,'Energy source and resource extraction'),(2,'Energy conversion'),
(3,'Generator or photovoltaic operation'),(4,'Power conditioning and voltage transformation'),
(5,'High-voltage transmission'),(6,'Substations and switching'),(7,'Distribution'),
(8,'Storage'),(9,'End-use conversion'),(10,'Useful work'),(11,'Waste heat'),
(12,'Equipment degradation'),(13,'Maintenance'),(14,'Decommissioning and recycling')]

# Evidence accessibility is stated, rather than pretending a catalogue abstract is
# a full reading of a technical standard. Equations below are author-written
# textbook formulations with explicit limits, not verbatim standard requirements.
SOURCES = [
{'id':'PHY-THERMO','title':'DOE-HDBK-1012/1-92: Thermodynamics, Heat Transfer, and Fluid Flow, volume 1','url':'https://www.energy.gov/ehss/articles/doe-hdbk-10121-92','status':'OFFICIAL_SCOPE_PAGE_READ; established physical balance formulations; numeric design limits not imported'},
{'id':'PHY-HEAT','title':'DOE Fundamentals Handbook: Thermodynamics, Heat Transfer, and Fluid Flow, volume 2','url':'https://www.osti.gov/biblio/10170081','status':'OFFICIAL_SEARCH_ABSTRACT; full text retrieval failed'},
{'id':'PHY-ELECTRIC','title':'DOE-HDBK-1011/2-92: Electrical Science','url':'https://www.energy.gov/ehss/articles/doe-hdbk-10112-92','status':'OFFICIAL_SCOPE_PAGE_READ; foundational textbook relations; not an installation standard'},
{'id':'PHY-PUMP','title':'DOE: Pump Systems and Improving Pumping System Performance sourcebook','url':'https://www.energy.gov/cmei/ito/pump-systems','status':'OFFICIAL_PAGE_READ; system-level comparator and publication locator'},
{'id':'PHY-PV','title':'PVWatts Version 1 Technical Reference, NREL/TP-6A20-60272','url':'https://www.nrel.gov/docs/fy14osti/60272.pdf','status':'OFFICIAL_SEARCH_ABSTRACT; full text retrieval failed; scoped approximation only'},
{'id':'PHY-LINE','title':'IEEE 738-2023: Current-Temperature Relationship of Bare Overhead Conductors','url':'https://standards.ieee.org/ieee/738/10207/','status':'OFFICIAL_ABSTRACT_READ; full standard not accessed; no conformance claim'},
{'id':'PHY-LINE-AGE','title':'Extension of dynamic line rating models with the effect of conductor aging (2022)','url':'https://ieeexplore.ieee.org/document/9857524/','status':'PRIMARY_PUBLICATION_SEARCH_ABSTRACT; established candidate-comparator prior art'},
{'id':'PHY-LINE-SAG','title':'Conductor Temperature Estimation and Prediction at Thermal Transient State in Dynamic Line Rating Application (2018)','url':'https://ieeexplore.ieee.org/document/8352008/','status':'PRIMARY_PUBLICATION_SEARCH_ABSTRACT; sag and tension measurement context'},
{'id':'PHY-DLR','title':'Hourly Dynamic Line Ratings for Existing Transmission Across the Contiguous United States (Preliminary Results)','url':'https://research-hub.nlr.gov/en/publications/hourly-dynamic-line-ratings-for-existing-transmission-across-the-/','status':'NATIONAL_LAB_SEARCH_ABSTRACT; weather and thermal state coupling'},
]

# law tuple = id, class, equation, domain, explicit assumptions, falsifier/model
# rejection condition, variable dimensions, source references. No empirical or
# engineering constraint is mislabeled an exact invariant.
LAW_ROWS = [
('MASS','EXACT_BALANCE','dm_cv/dt = sum(mdot_in)-sum(mdot_out)','nonrelativistic control volume with reaction species tracked','No unmodelled mass ports; chemical changes preserve total mass to engineering precision','Residual exceeds combined measurement/model tolerance after all ports included','m:kg;mdot:kg/s;t:s','PHY-THERMO'),
('ENERGY','EXACT_BALANCE','dE_cv/dt = Qdot-Wdot+sum(mdot*(h+v^2/2+g*z))_in-out','classical control volume, consistent enthalpy convention','All material, electrical, radiative and mechanical ports counted; signed terms','Energy residual cannot be explained by uncertainty or omitted storage/ports','E:J;Qdot:W;Wdot:W;h:J/kg;v:m/s;g:m/s^2;z:m','PHY-THERMO'),
('CHARGE','EXACT_BALANCE','dQ_cv/dt = - integral_surface(J dot n dA)','electrical control volume','Conduction and charge accumulation distinguished','Nonzero continuity residual with sufficient spatial/time resolution','Q:C;J:A/m^2;A:m^2;t:s','PHY-ELECTRIC'),
('KCL','CONDITIONAL_REDUCTION','sum(I_branch)=0','lumped electrical node','Charge storage at node negligible on selected time scale','Unmodelled capacitance makes branch-current sum measurably nonzero','I:A','PHY-ELECTRIC'),
('OHM','CONSTITUTIVE','V=I*R(T); R=R0*(1+alpha*(T-T0))','ohmic conductor in calibrated temperature band','Geometry fixed; linear temperature coefficient valid locally; skin effects included in effective R if relevant','Measured V/I or temperature coefficient outside contract tolerance','V:V;I:A;R:ohm;alpha:1/K;T:K','PHY-ELECTRIC'),
('JOULE','CONSTITUTIVE','P_loss=I_rms^2*R_ac','passive resistive element','R_ac includes waveform/frequency effects; constant R during averaging window','Energy measurement inconsistent with frequency-aware resistance model','P_loss:W;I_rms:A;R_ac:ohm','PHY-ELECTRIC'),
('ACPOWER','CONDITIONAL_REDUCTION','P=3*V_phase_rms*I_phase_rms*cos(phi)','balanced sinusoidal three-phase system','No significant harmonics or phase imbalance; phase voltage convention','Harmonic or imbalance contributions change real power materially','P:W;V_phase_rms:V;I_phase_rms:A;phi:rad','PHY-ELECTRIC'),
('FARADAY','EXACT_FIELD_LAW','emf=-d(lambda_B)/dt','stationary circuit path; moving-path emf needs motional term','lambda_B is total oriented flux linkage, equal to N*Phi_B for N identical turns','Flux/emf mismatch after motional and parasitic terms resolved','emf:V;lambda_B:Wb;t:s','PHY-ELECTRIC'),
('TORQUE','CONDITIONAL_BALANCE','J_rot*domega/dt=tau_drive-tau_load-tau_loss','rigid rotating shaft equivalent','Equivalent inertia and shaft coupling applicable; torsional modes omitted','Torsional or variable-inertia effects exceed error budget','J_rot:kg*m^2;omega:1/s;tau:N*m;t:s','PHY-ELECTRIC'),
('SHAFT','KINEMATIC_POWER','P_shaft=tau*omega','rotational power port','Consistent signed torque and angular velocity','Input/output mechanical energy fails balanced accounting','P_shaft:W;tau:N*m;omega:1/s','PHY-ELECTRIC'),
('HEAT','CONSTITUTIVE','Qdot_cond=-k*A*dT/dx; Qdot_conv=h*A*(T-Ta)','Fourier conduction and boundary convective closure','Local material/flow coefficients calibrated; continuum; no universal h','Independent temperature/flux profile disagrees outside tolerance','Qdot:W;k:W/(m*K);A:m^2;h:W/(m^2*K);T:K;x:m','PHY-HEAT'),
('RAD','CONSTITUTIVE','Qdot_rad=epsilon*sigma*A*(T^4-Tsur^4)','gray diffuse exchange with large isothermal surroundings','View factor one or explicitly absorbed into model; Kelvin temperatures','Geometry/spectral effects create material systematic residual','Qdot:W;epsilon:1;sigma:W/(m^2*K^4);A:m^2;T:K','PHY-HEAT'),
('THERMAL','CONDITIONAL_BALANCE','C*dT/dt=P_in+Q_abs-Q_loss','lumped thermal state','Biot/time-scale validity tested; positive C; all sources/sinks counted','Persistent internal gradients defeat single-temperature closure','C:J/K;T:K;t:s;P_in:W;Q_abs:W;Q_loss:W','PHY-HEAT,PHY-LINE'),
('ENTROPY','SECOND_LAW_CONSTRAINT','dS_cv/dt=sum(Qdot_j/T_j)+Sdot_mass+Sdot_gen; Sdot_gen>=0','thermodynamic control volume','Reservoir temperatures positive; entropy ports and composition known','Inferred negative production beyond uncertainty indicates model/data error','S:J/K;Qdot:W;T:K;Sdot:W/K','PHY-THERMO'),
('HYDRO','CONDITIONAL_POWER','P_hydraulic=rho*g*Qvol*H','incompressible pump/turbine useful hydraulic head','Head definition includes consistent boundary velocities and pressures','Measured energy balance exceeds applicable efficiency/loss model','rho:kg/m^3;g:m/s^2;Qvol:m^3/s;H:m;P:W','PHY-PUMP,PHY-THERMO'),
('PV','EMPIRICAL_MODEL','P_dc approx P_ref*(G/G_ref)*(1+gamma*(Tcell-Tref))','PV array near calibrated irradiance and temperature envelope','No clipping, mismatch or low-light extrapolation; DC operating point near MPP','Independent irradiance/temperature/IV data exceeds prediction interval','P:W;G:W/m^2;gamma:1/K;T:K','PHY-PV'),
('EFFICIENCY','ENGINEERING_ACCOUNTING','P_out=eta*P_in; 0<=eta<=1','single useful-energy output passive converter','Steady or storage-corrected averaging interval; other energy inputs excluded only when demonstrably absent; heat-pump COP distinct','Measured greater-than-one eta signals additional input or boundary error','P:W;eta:1','PHY-THERMO'),
('TRANSFORMER','CONDITIONAL_REDUCTION','V2/V1=N2/N1; P1=P2+P_copper+P_core+dE_field/dt','transformer in calibrated operating envelope','Ideal ratio is approximation; flux saturation and leakage qualified separately','Harmonics/saturation/leakage materially violate ideal relation','V:V;N:1;P:W;E_field:J;t:s','PHY-ELECTRIC'),
('SAG','CONDITIONAL_MECHANICS','sag approx w*L_span^2/(8*H_tension)','level-span parabolic conductor approximation','Uniform load; small sag/span; tension depends on temperature, creep and installed length','Catenary or unequal supports materially change clearance result','sag:m;w:N/m;L_span:m;H_tension:N','PHY-LINE-SAG'),
('CLEARANCE','ENGINEERING_CONSTRAINT','min_x(clearance(x,t))>=clearance_required','overhead line profile with terrain and crossing context','Required value from applicable asset/jurisdiction owner; value UNKNOWN here','Survey/model predicts or measures clearance below sourced requirement','clearance:m;t:s','PHY-LINE-SAG'),
('THERMAL_LIMIT','ENGINEERING_CONSTRAINT','max_x(T(x,t))<=T_limit(component,condition,duration)','asset operating envelope','Limit requires manufacturer/material/inspection basis; not inferred from average T','Hotspot exceeds limit or limit lacks applicable support','T:K;t:s','PHY-LINE'),
('SWITCH_ENERGY','CONDITIONAL_BALANCE','E_L=0.5*L*I^2; E_C=0.5*C_e*V^2','linear inductance/capacitance during switching','Magnetic saturation and nonlinear capacitance absent or represented','Transient energy/voltage cannot be accounted for within model','E:J;L:H;I:A;C_e:F;V:V','PHY-ELECTRIC'),
('STORAGE','ENGINEERING_ACCOUNTING','dE_store/dt=eta_c*P_charge-P_discharge/eta_d-P_self','bounded storage system','Efficiencies and self-discharge calibrated; energy definition fixed','Metered energy closure error beyond measurement tolerance','E_store:J;P:W;eta:1;t:s','PHY-ELECTRIC,PHY-THERMO'),
('BATTERY_CHARGE','CONDITIONAL_BALANCE','dSOC/dt=eta_coul*I/Q_cap','coulomb-counting battery state estimator','Current sign defined charging positive; usable capacity age/temperature dependent','Reference capacity measurement or side reactions invalidate estimator','SOC:1;I:A;Q_cap:C;t:s','PHY-ELECTRIC'),
('CAPACITY','ENGINEERING_CONSTRAINT','0<=E_store<=E_usable(condition); abs(P)<=P_limit(condition)','qualified storage operating domain','Age, temperature and SOC bounds from applicable data; no universal numeric limits','Observed/predicted state violates asset-qualified bound','E_store:J;P:W','PHY-ELECTRIC'),
('PUMP_SYSTEM','CONSTITUTIVE_SYSTEM_MODEL','H_pump(Qvol,N)=H_static+K*Qvol^2','steady pump and piping intersection','Single-phase; calibrated resistance; static head retained; NPSH checked separately','Measured operating point not explained by curves or cavitation occurs','H:m;Qvol:m^3/s;N:1/s;K:s^2/m^5','PHY-PUMP'),
('HEAT_RECOVERY','ENGINEERING_ACCOUNTING','Qdot_recovered<=Qdot_available; DeltaT_approach>0','passive heat exchanger without heat-pump work','Source/sink time, temperature, flow and fouling qualified','Claimed duty exceeds energy balance or violates temperature pinch','Qdot:W;DeltaT:K','PHY-HEAT,PHY-THERMO'),
('DEGRADATION','EMPIRICAL_MODEL','D(t)=integral(rate(T,stress,chemistry,history),dt)','damage state only within calibrated mechanism','Rate and accumulation rule must be externally identified; no universal Miner/Arrhenius validity','Held-out degradation or recovery invalidates rate/accumulation model','D:1;rate:1/s;t:s','PHY-LINE-AGE'),
('ISOLATION','SAFETY_REQUIREMENT','E_residual<=E_safe(context) and isolation_verified','maintenance/decommissioning effect boundary','Actual switching authority and lockout procedure outside research simulator; threshold UNKNOWN','Residual live source or stored energy defeats safe-state claim','E_residual:J;E_safe:J','PHY-ELECTRIC'),
('RECOVERY_MASS','ENGINEERING_ACCOUNTING','m_feed=m_products+m_rejects+m_emissions+Delta_m_process','recycling batch with moisture and reagents tracked','All material additions counted; composition balance separately required','Weighed/assayed mass balance fails beyond uncertainty','m:kg','PHY-THERMO'),
('MATERIAL_QUALITY','ENGINEERING_CONSTRAINT','composition_product in customer_spec and measured_properties in acceptance_set','recycled material reuse','No universal purity requirement assumed; specification and test values UNKNOWN','Product fails declared functional acceptance tests','composition:1;property:typed_per_property','PHY-THERMO'),
]

# Each field name is a physical quantity; units use SI or dimensionless state.
UNITS = {
'mass_flow':'kg/s','fuel_energy_density':'J/kg','fuel_moisture':'1','chemical_power':'W','process_power':'W','emissions_flow':'kg/s','heat_power':'W','heat_loss':'W','temperature':'K','ambient_temperature':'K','hotspot_temperature':'K','core_temperature':'K','surface_temperature':'K','pressure':'Pa','enthalpy':'J/kg','water_flow':'m^3/s','head':'m','shaft_power':'W','torque':'N*m','speed':'1/s','irradiance':'W/m^2','wind_speed':'m/s','wind_direction':'rad','air_density':'kg/m^3','solar_absorptivity':'1','emissivity':'1','dc_power':'W','ac_power':'W','active_power':'W','reactive_power':'var','voltage':'V','current':'A','frequency':'Hz','phase':'rad','resistance':'ohm','inductance':'H','capacitance':'F','flux':'Wb','harmonic_current':'A','impedance':'ohm','switch_state':'1','fault_current':'A','fault_duration':'s','protection_delay':'s','fault_energy':'J','line_temperature':'K','thermal_state':'K','thermal_capacity':'J/K','cooling_power':'W','span_length':'m','tension':'N','sag':'m','clearance':'m','creep_strain':'1','insulation_state':'1','damage_state':'1','mechanical_stress':'Pa','moisture':'1','particle_count':'1/m^3','contact_resistance':'ohm','state_of_charge':'1','usable_capacity':'J','stored_energy':'J','charge_capacity':'C','internal_resistance':'ohm','charge_current':'A','discharge_current':'A','cell_temperature':'K','efficiency':'1','power_limit':'W','load_demand':'W','delivered_service':'typed_service_unit/s','useful_work':'J','energy':'J','time':'s','flow_demand':'m^3/s','illuminance':'lx','light_power':'W','refrigeration_power':'W','service_temperature':'K','material_mass':'kg','recovered_mass':'kg','reject_mass':'kg','material_composition':'1','material_quality':'typed_property','remaining_life':'s','inspection_signal':'typed_signal','repair_state':'1','isolation_state':'1','residual_energy':'J','transformer_hotspot':'K','oil_temperature':'K','topology':'1','leakage_current':'A','synchronism':'1','inertia':'kg*m^2','rotor_angle':'rad','weather_history':'typed_timeseries','temperature_history':'typed_timeseries','current_history':'typed_timeseries','dispatch_horizon':'s','soil_temperature':'K','soil_moisture':'1','soil_thermal_resistivity':'m*K/W','coolant_flow':'kg/s','contaminant_fraction':'1','processing_temperature':'K','quality_signal':'typed_signal','dissolved_gas':'1','pressure_drop':'Pa','thermal_conductance':'W/K','health_estimate':'1','failure_probability':'1','repair_duration':'s','voltage_limit':'V',
}

# id|stage|branch|physical situation|inputs|outputs|persistent/required state|laws|assumptions|unresolved state
SITUATION_ROWS = r'''
E01|1|fuel|Extract and transport combustible feedstock|material_mass,process_power|mass_flow,fuel_moisture|fuel_energy_density,fuel_moisture|MASS,ENERGY|Material chain boundary includes transport energy|Feedstock moisture and grade variability
E02|1|fuel|Prepare and meter fuel at conversion boundary|mass_flow,fuel_moisture,process_power|chemical_power,mass_flow|fuel_energy_density,fuel_moisture|MASS,ENERGY|Chemical input is measured lower or higher heating value consistently|Fuel composition and moisture not interchangeable with mass
E03|1|hydro|Reservoir inflow and water release|water_flow,head|water_flow,head|stored_energy,head|MASS,ENERGY,HYDRO|Seasonal water balance and permissible flows externally provided|Reservoir geometry and competing flow requirements
E04|1|wind|Atmospheric wind reaches turbine rotor|wind_speed,air_density|wind_speed,air_density|weather_history,wind_direction|ENERGY|Rotor area and upstream/downstream boundary specified|Wake distribution and turbulence spectrum
E05|1|solar|Solar radiation reaches array plane|irradiance,ambient_temperature|irradiance|solar_absorptivity,material_quality|ENERGY,RAD|Plane-of-array irradiance distinct from horizontal weather observation|Spectral mismatch, soiling and shading pattern
E06|1|geothermal|Withdraw and return geothermal fluid|mass_flow,temperature,pressure|enthalpy,mass_flow|pressure,temperature|MASS,ENERGY|Reinjection stream tracked; no assumption of inexhaustible heat|Reservoir drawdown and scaling composition
E07|2|fuel|Convert chemical energy into hot fluid|chemical_power,mass_flow|heat_power,emissions_flow|temperature,material_composition|MASS,ENERGY,ENTROPY|Combustion or reactor-specific source term externally supplied|Reaction completion, excess air and spatial temperature
E08|2|thermal|Transfer heat to working fluid|heat_power,mass_flow|enthalpy,pressure,heat_loss|thermal_conductance,pressure_drop|ENERGY,HEAT,ENTROPY|Wall and fluid storage retained if transients material|Fouling and cross-stream temperature profiles
E09|2|thermal|Expand pressurized fluid through turbine|enthalpy,mass_flow,pressure|shaft_power,heat_loss|speed,mechanical_stress|ENERGY,SHAFT,ENTROPY|Working-fluid property model and exhaust state specified|Moisture erosion and part-load efficiency
E10|2|hydro|Convert hydraulic head into shaft power|water_flow,head|shaft_power,water_flow|speed,pressure|HYDRO,ENERGY|Efficiency map calibrated for actual head and flow|Cavitation margin and hydraulic transients
E11|2|wind|Aerodynamic rotor converts wind flux to torque|wind_speed,air_density|torque,shaft_power|speed,wind_direction,mechanical_stress|ENERGY,SHAFT|Rotor power coefficient is external aerodynamic model|Wake steering, gust loads and pitch response
E12|2|thermal|Condense exhaust and recirculate working fluid|enthalpy,mass_flow,cooling_power|heat_power,mass_flow|pressure,temperature|MASS,ENERGY,HEAT|Cooling source and pumping energy remain in system boundary|Ambient-limited back pressure
E13|3|rotating|Generator shaft accelerates under torque mismatch|torque,shaft_power|speed,rotor_angle|inertia,speed,rotor_angle|TORQUE,SHAFT|Rigid equivalent shaft only below torsional relevance|Multi-mass shaft and converter-coupled inertia
E14|3|rotating|Generator magnetic field induces terminal voltage|speed,flux|voltage,frequency|flux,temperature|FARADAY,ENERGY|Saturation and excitation represented by calibrated machine model|Rotor/stator spatial flux distribution
E15|3|rotating|Generator supplies load while winding losses heat insulation|voltage,current|ac_power,heat_loss|temperature,insulation_state|ACPOWER,JOULE,THERMAL|Balanced sinusoidal reduction conditional|Harmonic losses and end-winding hotspots
E16|3|solar|PV cell converts photons at electrical operating point|irradiance,cell_temperature,voltage|dc_power,current|cell_temperature,material_quality|PV,ENERGY|Linear PV formula only qualified operating envelope|Partial-shading mismatch and bypass-diode states
E17|3|solar|PV laminate heats and cools during irradiance change|irradiance,dc_power,ambient_temperature,wind_speed|cell_temperature,heat_loss|thermal_capacity,emissivity|THERMAL,RAD,HEAT|Electrical output subtracts from absorbed heat budget|Backsheet/cell gradients and mounting convection
E18|4|power_electronics|Inverter switches DC into grid-compatible AC|dc_power,voltage|ac_power,harmonic_current,heat_loss|switch_state,temperature|ENERGY,SWITCH_ENERGY,EFFICIENCY|Switching/loss model and control stability separately qualified|Device junction temperature and harmonic spectrum
E19|4|power_electronics|Filter attenuates inverter switching harmonics|harmonic_current,voltage|current,heat_loss|inductance,capacitance,temperature|CHARGE,SWITCH_ENERGY,JOULE|Filter parasitics and grid impedance included for resonance|Damping and grid-impedance variation
E20|4|transformer|Step-up transformer transfers voltage and current|ac_power,voltage,current|voltage,current,heat_loss|flux,temperature,insulation_state|TRANSFORMER,JOULE,ENERGY|Terminal ratio does not imply zero losses|Core saturation and winding hotspots
E21|4|control|Synchronize generating source before interconnection|voltage,frequency,phase|synchronism,switch_state|phase,frequency,rotor_angle|ENERGY,SWITCH_ENERGY|Closing limits require external protection/control settings|Measurement latency and angle uncertainty
E22|4|control|Maintain reactive support under voltage constraint|reactive_power,voltage,load_demand|voltage,reactive_power|power_limit,temperature|ACPOWER,THERMAL_LIMIT|Capability curve depends on voltage/current/temperature|Converter current allocation during disturbances
E23|5|transmission|AC branch redistributes current after topology change|voltage,impedance,topology|current,active_power,reactive_power|topology,phase|KCL,ACPOWER,ENERGY|Power-flow equations and branch impedances externally specified|Unbalanced/harmonic/transient modes outside AC load-flow
E24|5|transmission|Distributed conductor resistance produces heat|current,resistance|heat_power|line_temperature,current_history|JOULE,OHM|Frequency-dependent AC resistance where skin effects matter|Segment temperatures and joints versus average resistance
E25|5|transmission|Conductor exchanges heat with weather|heat_power,irradiance,wind_speed,wind_direction,ambient_temperature|line_temperature,cooling_power|core_temperature,surface_temperature,thermal_capacity|THERMAL,HEAT,RAD,THERMAL_LIMIT|Lumped state conditional; core/surface need separate states when material|Spatial weather coherence and time-varying boundary conditions
E26|5|transmission|Thermal expansion and creep alter tension|line_temperature,span_length,mechanical_stress|tension,creep_strain|temperature_history,creep_strain|ENERGY,DEGRADATION|Constitutive mechanics material-specific; creep not universally linear|Installed length, stress history and annealing
E27|5|transmission|Tension and terrain determine sag clearance|tension,span_length|sag,clearance|creep_strain,topology|SAG,CLEARANCE|Parabolic formula only level-span small-sag approximation|Terrain survey, ice/wind load and crossing requirement
E28|5|transmission|Connector contact resistance creates local hotspot|current,contact_resistance,ambient_temperature|hotspot_temperature,heat_loss|contact_resistance,damage_state|JOULE,THERMAL,THERMAL_LIMIT|Connector cooling distinct from bare span cooling|Contact pressure, corrosion and local thermal conductance
E29|5|transmission|Insulation withstands electric field and pollution|voltage,moisture,contaminant_fraction|leakage_current,insulation_state|insulation_state,temperature|CHARGE,ENERGY,THERMAL_LIMIT|Flashover model and withstand limits externally specified|Surface wetting, contamination and field enhancement
E30|5|transmission|Line fault drives electromagnetic transient|voltage,impedance,switch_state|fault_current,fault_energy|inductance,capacitance,topology|CHARGE,SWITCH_ENERGY,ENERGY|Transient model includes switching path and source contribution|Arc impedance and frequency-dependent network response
E31|5|transmission|Dispatch evaluates transient thermal headroom|current,line_temperature,weather_history|power_limit|dispatch_horizon,core_temperature,damage_state|THERMAL,THERMAL_LIMIT,CLEARANCE|Weather forecast and state uncertainty retained; no operational dispatch here|Component-specific weakest constraint and cumulative effects
E32|6|substation|Instrument transformers sense electrical state|voltage,current|voltage,current|temperature,phase|TRANSFORMER,ENERGY|Measurements retain timestamp, calibration and saturation qualification|Fault-time sensor saturation and timing skew
E33|6|substation|Protection classifies fault and times interruption|fault_current,voltage|protection_delay,switch_state|topology,insulation_state|THERMAL_LIMIT,SWITCH_ENERGY|Protection settings imported, not generated as permission|Coordination margins and inverter-limited fault current
E34|6|substation|Breaker interrupts fault and dissipates arc energy|fault_current,protection_delay|fault_energy,switch_state|damage_state,temperature|ENERGY,SWITCH_ENERGY|Interrupting capability must be equipment-qualified|Arc duration, contact wear and restrike
E35|6|substation|Busbar and disconnectors carry redistributed current|current,switch_state|current,heat_loss|contact_resistance,temperature|KCL,JOULE,THERMAL_LIMIT|Branch-current transfer respects topology; no switch-current equality assumption|Joint hotspots and nonuniform bus cooling
E36|6|substation|Power transformer heats oil and winding hotspots|current,voltage,ambient_temperature|voltage,oil_temperature,transformer_hotspot|temperature_history,insulation_state|TRANSFORMER,JOULE,THERMAL,THERMAL_LIMIT|Hotspot thermal network distinct from top-oil alone|Moisture-dependent dielectric/ageing effects
E37|6|substation|Restore network after fault isolation|switch_state,topology,load_demand|topology,current|temperature_history,damage_state|KCL,ENERGY,THERMAL_LIMIT|Restoration must re-evaluate equipment limits and cold-load pickup|Pre-fault heat and post-fault cumulative stress
E38|7|distribution|Feeder supplies unbalanced distributed loads|voltage,load_demand,topology|current,voltage,heat_loss|topology,impedance|KCL,JOULE,ENERGY|Full phase model required when imbalance material|Phase assignment and neutral current
E39|7|distribution|Tap changer regulates feeder voltage|voltage,load_demand|voltage,switch_state|damage_state,temperature|TRANSFORMER,SWITCH_ENERGY|Discrete tap bounds and delay externally specified|Mechanical wear and controller interactions
E40|7|distribution|Underground cable stores heat in soil|current,soil_temperature,soil_moisture|line_temperature,heat_loss|soil_thermal_resistivity,thermal_state|JOULE,HEAT,THERMAL_LIMIT|Soil dry-out and layered thermal response not universal constants|Moisture migration and neighboring-circuit heat
E41|7|distribution|Distributed solar reverses feeder power flow|dc_power,voltage,load_demand|active_power,voltage,current|topology,power_limit|KCL,ENERGY|Reverse-flow equipment capability separately verified|Protection directionality and voltage rise
E42|7|distribution|Service transformer converts to utilization voltage|voltage,current|voltage,current,heat_loss|transformer_hotspot,insulation_state|TRANSFORMER,JOULE,THERMAL_LIMIT|Local demand coincidence and ambient envelope needed|Coincident EV/heat-pump loading
E43|7|distribution|Meter records delivered electrical energy|voltage,current,time|energy|harmonic_current,phase|ENERGY,CHARGE|Meter bandwidth and synchronization define validity|Missing intervals and non-sinusoidal measurement error
E44|8|battery|Battery accepts charge into chemical state|voltage,charge_current|state_of_charge,heat_loss|charge_capacity,cell_temperature,internal_resistance|BATTERY_CHARGE,STORAGE,THERMAL|Side reactions and coulombic efficiency calibrated|Cell imbalance and lithium plating boundary
E45|8|battery|Battery discharges into converter demand|discharge_current,voltage|dc_power,state_of_charge,heat_loss|usable_capacity,internal_resistance,cell_temperature|BATTERY_CHARGE,STORAGE,CAPACITY|Discharge sign distinguished from charge convention|State/temperature-dependent voltage and power limits
E46|8|battery|Cooling loop equalizes storage cell temperatures|cell_temperature,coolant_flow|cell_temperature,cooling_power|thermal_state,thermal_conductance|ENERGY,HEAT,THERMAL_LIMIT|Cell and coolant spatial gradients included where consequential|Sensor placement and weakest-cell temperature
E47|8|hydro_storage|Pump water to upper storage reservoir|ac_power,water_flow|stored_energy,head,heat_loss|head,efficiency|HYDRO,STORAGE,ENERGY|Pump efficiency map and varying head retained|Evaporation, water leakage and hydraulic transients
E48|8|thermal_storage|Charge and discharge thermal store|heat_power,mass_flow|stored_energy,temperature|thermal_state,material_quality|ENERGY,STORAGE,ENTROPY|Temperature stratification/phase fraction retained if material|Mixing destroys recoverable heat quality
E49|8|storage_control|Allocate storage duty within condition-dependent limits|load_demand,state_of_charge,cell_temperature|power_limit,charge_current,discharge_current|usable_capacity,damage_state|STORAGE,CAPACITY,THERMAL_LIMIT|Action optimizer subordinate to qualified physical bounds|Forecast demand, degradation cost and capacity uncertainty
E50|9|motor|Electric motor produces torque at variable speed|voltage,current,frequency|torque,shaft_power,heat_loss|speed,temperature,insulation_state|ACPOWER,TORQUE,SHAFT,JOULE|Motor loss map and drive harmonics qualified|Bearing loss and part-load efficiency
E51|9|pump|Pump transfers shaft work into fluid head|shaft_power,water_flow|head,water_flow,heat_loss|speed,pressure|HYDRO,PUMP_SYSTEM,ENERGY|Operating point solved jointly with system curve|Cavitation, valve throttling and minimum flow
E52|9|heat_pump|Refrigeration cycle lifts heat to higher temperature|ac_power,temperature|heat_power,refrigeration_power|pressure,thermal_state|ENERGY,ENTROPY|Heat output may exceed electrical input because source heat included|Refrigerant charge, frosting and cycling loss
E53|9|lighting|LED driver and emitter deliver optical flux|ac_power,current|light_power,heat_loss|temperature,material_quality|ENERGY,JOULE,THERMAL|Spectral luminous efficacy needed to translate watts to illuminance|Junction temperature and spectral ageing
E54|9|compute|Power supply and electronic workload deliver computing service|ac_power,load_demand|heat_power,delivered_service|temperature,capacitance|ENERGY,SWITCH_ENERGY,THERMAL_LIMIT|Service quantity workload-specific, never generic intelligence unit|Timing errors, utilization and cooling overhead
E55|9|resistive_heat|Resistance heater transfers electricity to process heat|ac_power,current|heat_power,heat_loss|temperature,resistance|JOULE,ENERGY|Useful process boundary excludes uncontrolled heat leakage|Surface/process temperature gradient
E56|10|mechanical_service|Machine applies shaft work to useful task|shaft_power,torque,speed|useful_work,heat_loss|load_demand,mechanical_stress|SHAFT,ENERGY|Useful task and acceptance specification declared|Idle work versus accepted output
E57|10|fluid_service|Hydraulic network delivers required flow and pressure|water_flow,head|delivered_service,heat_loss|flow_demand,pressure|HYDRO,PUMP_SYSTEM,ENERGY|Service must meet minimum flow/pressure at actual demand nodes|Unequal branches and unnecessary throttling
E58|10|thermal_service|Building or process maintains temperature service|heat_power,refrigeration_power|service_temperature,delivered_service|thermal_state,temperature|ENERGY,HEAT|Occupancy/product requirement externally supplied; no invented human preference|Thermal mass and time-of-use constraints
E59|10|lighting_service|Optical system illuminates work plane|light_power|illuminance,delivered_service|material_quality|ENERGY|Geometry and spectrum needed; illuminance not conserved energy|Optical losses and functional lighting requirement
E60|11|rejection|Condenser releases low-grade heat to ambient|heat_power,ambient_temperature|heat_loss,temperature|thermal_conductance,coolant_flow|ENERGY,HEAT,ENTROPY|Fan/pump work included in net balance|Seasonal sink temperature and fouling
E61|11|recovery|Recover exhaust heat into matched demand stream|heat_power,temperature,mass_flow|heat_power,heat_loss|thermal_conductance,service_temperature|ENERGY,HEAT_RECOVERY,ENTROPY|Source/sink coincidence and approach temperature explicit|Variable demand, corrosion and heat quality
E62|11|recovery|Upgrade waste heat with heat-pump work|heat_power,ac_power|heat_power,heat_loss|pressure,temperature|ENERGY,ENTROPY|Electrical work explicitly charged against recovered service|COP across temperature lift and part-load
E63|11|environment|Disperse residual heat in receiving medium|heat_loss,mass_flow|temperature|ambient_temperature,thermal_state|ENERGY,HEAT|Receiving medium and thermal boundary defined|Environmental temperature constraints require local source
E64|12|conductor_ageing|Accumulate conductor creep and strength loss|line_temperature,mechanical_stress,time|creep_strain,damage_state|temperature_history,damage_state|DEGRADATION,SAG|Material-specific measured law; no universal damage threshold|Interaction of prior annealing and future emergency ratings
E65|12|insulation_ageing|Age transformer insulation under thermal and moisture exposure|transformer_hotspot,moisture,time|insulation_state,damage_state|temperature_history,material_quality|DEGRADATION,THERMAL_LIMIT|Rate calibration must match insulation chemistry and moisture|Oxygen, moisture transport and hotspot history
E66|12|battery_ageing|Battery cycling changes capacity and resistance|state_of_charge,cell_temperature,current,time|usable_capacity,internal_resistance,damage_state|temperature_history,current_history|DEGRADATION,STORAGE|Calendar/cycle pathways and reversibility separate|Spatial nonuniformity and chemistry-dependent mechanisms
E67|12|mechanical_ageing|Vibration and stress consume rotating-equipment margin|mechanical_stress,speed,time|damage_state,remaining_life|temperature,inspection_signal|DEGRADATION|Life is model estimate with uncertainty; load cycles retained|Lubrication, corrosion and interacting fatigue modes
E68|12|contamination|Deposits alter heat exchange and electrical leakage|mass_flow,contaminant_fraction,time|thermal_conductance,leakage_current|moisture,material_quality|MASS,HEAT,DEGRADATION|Deposit rate and geometry external; no universal fouling law|Nonuniform deposits and flow-regime dependence
E69|13|inspection|Measure equipment health before intervention|inspection_signal,temperature,voltage|health_estimate,failure_probability|damage_state,material_quality|THERMAL_LIMIT,DEGRADATION|Sensor model and calibration plus uncertainty explicit|Identifiability: distinct damage states can share signal
E70|13|isolation|Isolate electrical and stored-energy sources for maintenance|switch_state,stored_energy,topology|isolation_state,residual_energy|topology,voltage|ISOLATION,ENERGY,SWITCH_ENERGY|No physical work authorized by simulation; actual procedure owner required|Backfeed, capacitive energy and undocumented topology
E71|13|repair|Clean, repair or replace degraded component|isolation_state,material_mass,process_power|repair_state,material_mass|material_quality,damage_state|MASS,ENERGY,ISOLATION|Repair does not erase unaffected historical damage|Contact resistance after repair and altered geometry
E72|13|return_to_service|Verify condition and re-energize repaired asset|repair_state,voltage,current|switch_state,health_estimate|insulation_state,topology|THERMAL_LIMIT,ENERGY|Requalification bound to repaired asset and actual configuration|Commissioning test coverage and residual failure modes
E73|14|decommission|Disconnect asset and remove hazardous stored energy|switch_state,stored_energy,material_mass|residual_energy,material_mass|material_composition,isolation_state|ISOLATION,ENERGY,MASS|Hazards and jurisdiction-specific disposal obligations unresolved|Battery residual charge and oil contamination
E74|14|sorting|Separate components by composition and condition|material_mass,quality_signal|material_mass,material_composition|contaminant_fraction,material_quality|MASS,MATERIAL_QUALITY|Sorting accuracy and target product specification declared|Misclassification and spatial contamination
E75|14|reprocessing|Recover metals or active material by physical/chemical processing|material_mass,process_power,processing_temperature|recovered_mass,reject_mass,heat_loss|material_composition,contaminant_fraction|RECOVERY_MASS,ENERGY,ENTROPY|Reagents/emissions enter full balance; yield not assumed 100 percent|Recovery quality, energy demand and co-product allocation
E76|14|reuse|Qualify recovered material for new equipment|recovered_mass,material_composition,quality_signal|material_quality,material_mass|damage_state,contaminant_fraction|MATERIAL_QUALITY,MASS|Performance-based acceptance independent of origin label|Functional lifetime and impurity tolerance need experiments
E77|4|power_electronics|Battery charger rectifies grid power into controlled DC current|ac_power,voltage,current|voltage,charge_current,heat_loss|temperature,power_limit|ENERGY,EFFICIENCY,THERMAL_LIMIT|AC input and DC output are separate local ports even when quantity names match|Charge-voltage control, conversion losses and ripple
'''

# Curated edges include physically distinct branches, merges and feedback loops.
# Arrow order is process dependency, not a claim all events are sequential.
EDGE_ROWS = r'''
E01 E02 physical_flow mass_flow,fuel_moisture
E02 E07 physical_flow chemical_power,mass_flow
E03 E10 physical_flow water_flow,head
E04 E11 physical_flow wind_speed,air_density,weather_history
E05 E16 physical_flow irradiance
E05 E17 physical_flow irradiance
E06 E08 physical_flow mass_flow,enthalpy,temperature
E07 E08 physical_flow heat_power,mass_flow
E08 E09 physical_flow enthalpy,pressure,mass_flow
E09 E12 physical_flow enthalpy,mass_flow
E12 E08 feedback mass_flow,temperature,pressure
E09 E13 physical_flow shaft_power,speed
E10 E13 physical_flow shaft_power,speed
E11 E13 physical_flow shaft_power,torque,speed
E13 E14 physical_flow speed,rotor_angle
E14 E15 physical_flow voltage,frequency,flux
E15 E20 physical_flow ac_power,current,voltage
E16 E17 physical_flow dc_power
E17 E16 feedback cell_temperature
E16 E18 physical_flow dc_power,voltage,current
E18 E19 physical_flow harmonic_current,voltage
E19 E20 physical_flow current,voltage
E18 E22 information temperature,power_limit
E20 E21 physical_flow voltage
E21 E23 physical_flow synchronism,switch_state,phase,frequency
E22 E23 feedback voltage,reactive_power,power_limit
E23 E24 physical_flow current
E24 E25 physical_flow heat_power
E25 E24 feedback line_temperature
E25 E26 physical_flow line_temperature,temperature_history
E26 E27 physical_flow tension,creep_strain
E23 E28 physical_flow current
E23 E29 physical_flow voltage
E29 E30 physical_flow insulation_state,leakage_current
E30 E33 physical_flow fault_current
E25 E31 information line_temperature,core_temperature,weather_history
E27 E31 information clearance,sag,creep_strain
E28 E31 information hotspot_temperature,contact_resistance
E31 E23 feedback power_limit,dispatch_horizon
E23 E32 physical_flow current,voltage
E32 E33 information voltage,current,phase
E33 E34 physical_flow protection_delay,fault_current
E34 E35 physical_flow switch_state,damage_state
E35 E36 physical_flow current,voltage
E34 E37 lifecycle switch_state,damage_state,temperature
E37 E23 feedback topology
E36 E38 physical_flow voltage,current
E38 E39 information voltage,load_demand
E39 E38 feedback voltage,switch_state
E38 E40 physical_flow current
E40 E38 information line_temperature,soil_thermal_resistivity
E16 E41 physical_flow dc_power
E41 E38 physical_flow active_power,current,voltage
E38 E42 physical_flow voltage,current
E42 E43 physical_flow voltage,current
E42 E77 physical_flow ac_power,voltage,current
E77 E44 physical_flow voltage,charge_current
E43 E49 information energy
E44 E45 lifecycle state_of_charge,cell_temperature,usable_capacity
E45 E18 physical_flow dc_power,voltage
E44 E46 physical_flow cell_temperature,heat_loss
E45 E46 physical_flow cell_temperature,heat_loss
E46 E44 feedback cell_temperature
E46 E45 feedback cell_temperature
E38 E47 physical_flow ac_power
E47 E10 lifecycle stored_energy,head,water_flow
E61 E48 physical_flow heat_power
E48 E58 physical_flow stored_energy,temperature,heat_power
E44 E49 information state_of_charge,cell_temperature
E45 E49 information state_of_charge,usable_capacity
E49 E44 feedback charge_current,power_limit
E49 E45 feedback discharge_current,power_limit
E42 E50 physical_flow voltage,current
E50 E51 physical_flow shaft_power,speed
E42 E52 physical_flow ac_power
E42 E53 physical_flow ac_power,current
E42 E54 physical_flow ac_power
E42 E55 physical_flow ac_power,current
E50 E56 physical_flow shaft_power,torque,speed
E51 E57 physical_flow water_flow,head
E52 E58 physical_flow heat_power,refrigeration_power
E55 E58 physical_flow heat_power
E53 E59 physical_flow light_power
E12 E60 physical_flow heat_power,mass_flow
E54 E61 physical_flow heat_power,temperature
E55 E61 physical_flow heat_power,temperature
E60 E61 physical_flow heat_power,temperature
E61 E58 physical_flow heat_power,temperature
E61 E62 physical_flow heat_power,temperature
E62 E58 physical_flow heat_power
E60 E63 physical_flow heat_loss,mass_flow
E61 E63 physical_flow heat_loss,mass_flow
E25 E64 lifecycle line_temperature,temperature_history
E26 E64 lifecycle creep_strain,mechanical_stress
E64 E26 feedback damage_state,creep_strain
E64 E31 information damage_state,creep_strain
E36 E65 lifecycle transformer_hotspot,temperature_history
E65 E36 feedback insulation_state,damage_state
E44 E66 lifecycle state_of_charge,cell_temperature,current_history
E45 E66 lifecycle state_of_charge,cell_temperature,current_history
E66 E44 feedback usable_capacity,internal_resistance,damage_state
E66 E45 feedback usable_capacity,internal_resistance,damage_state
E66 E49 information usable_capacity,internal_resistance,damage_state
E50 E67 lifecycle speed,mechanical_stress,temperature
E67 E50 feedback damage_state,remaining_life
E08 E68 lifecycle mass_flow,temperature
E68 E08 feedback thermal_conductance,pressure_drop
E28 E69 information hotspot_temperature,contact_resistance,damage_state
E64 E69 information damage_state,creep_strain
E65 E69 information insulation_state,damage_state
E66 E69 information usable_capacity,internal_resistance,damage_state
E67 E69 information damage_state,remaining_life
E69 E70 information health_estimate,failure_probability
E70 E71 lifecycle isolation_state,residual_energy
E71 E72 lifecycle repair_state,material_quality,damage_state
E72 E23 lifecycle topology,switch_state,health_estimate
E72 E36 lifecycle repair_state,insulation_state,health_estimate
E69 E73 lifecycle health_estimate,damage_state
E70 E73 lifecycle isolation_state,residual_energy
E73 E74 physical_flow material_mass,material_composition
E74 E75 physical_flow material_mass,material_composition,contaminant_fraction
E75 E76 physical_flow recovered_mass,material_composition
E76 E71 physical_flow material_mass,material_quality
'''

# Parent regions express recursive process decomposition. Expansion is warranted
# by different state, boundary physics or decision constraints, never by a node
# quota. Unexpanded alternatives remain an explicit frontier.
PROCESS_GROUPS = [
 ('P-FUEL',1,'Fuel acquisition boundary',['E01','E02'],'Separate material quality and metered chemical energy; moisture changes conversion decisions.'),
 ('P-NATURAL',1,'Renewable and geothermal resource boundaries',['E03','E04','E05','E06'],'Distinct resource fluxes, time scales and extraction consequences require separate ports.'),
 ('P-THERMAL-CYCLE',2,'Thermal working-fluid cycle',['E07','E08','E09','E12'],'Heat transfer, expansion and condensation carry different thermodynamic state.'),
 ('P-FLUID-ROTOR',2,'Natural-flow mechanical conversion',['E10','E11'],'Hydraulic and aerodynamic conversion have distinct validity and uncertainty.'),
 ('P-GENERATOR',3,'Rotating generator conversion',['E13','E14','E15'],'Mechanical state, magnetic field and winding heat evolve on different time scales.'),
 ('P-PV',3,'Coupled photovoltaic and thermal response',['E16','E17'],'Bidirectional electrical/temperature dependency changes power prediction.'),
 ('P-CONDITIONING',4,'Power conversion and interconnection',['E18','E19','E20','E21','E22','E77'],'Switching, filtering, voltage ratio and grid connection preserve different constraints.'),
 ('P-TX-THERMOMECHANICAL',5,'Transmission electrothermal and clearance chain',['E24','E25','E26','E27','E28'],'Local heating, weather, installed mechanics and connector conditions can each constrain useful current.'),
 ('P-TX-NETWORK',5,'Transmission electrical and operating-envelope chain',['E23','E29','E30','E31'],'Network redistribution, insulation faults and dispatch horizons couple fast and slow state.'),
 ('P-SUB-PROTECTION',6,'Measurement through fault interruption',['E32','E33','E34'],'Latency and fault energy cross measurement, decision and physical interruption boundaries.'),
 ('P-SUB-TRANSFER',6,'Substation transfer and restoration',['E35','E36','E37'],'Component temperatures and damage survive topology restoration.'),
 ('P-DIST',7,'Distribution delivery and reverse flow',['E38','E39','E40','E41','E42','E43'],'Phase imbalance, soil heat, discrete taps and local generation need distinct context.'),
 ('P-BATTERY',8,'Battery energy and temperature cycling',['E44','E45','E46','E49'],'Charge, discharge, cooling and allocation share condition-dependent limits.'),
 ('P-NONBATTERY-STORAGE',8,'Hydraulic and thermal storage',['E47','E48'],'Stored energy retains head or temperature quality, not only quantity.'),
 ('P-ENDUSE',9,'Electrical conversion at final devices',['E50','E51','E52','E53','E54','E55'],'Different service mechanisms and heat ports require distinct science.'),
 ('P-SERVICE',10,'Accepted useful service',['E56','E57','E58','E59'],'Service equivalence depends on pressure, temperature, optical or mechanical acceptance conditions.'),
 ('P-HEAT-DESTINATION',11,'Residual heat and recovery',['E60','E61','E62','E63'],'Source-sink temperature and temporal coincidence determine recoverability.'),
 ('P-AGEING',12,'Condition histories across operation',['E64','E65','E66','E67','E68'],'Different degradation mechanisms have different state, falsifiers and recovery behavior.'),
 ('P-MAINTENANCE',13,'Observation through return to service',['E69','E70','E71','E72'],'Diagnosis, isolation, physical repair and requalification have separate evidence obligations.'),
 ('P-RECYCLE',14,'End-of-life material recovery',['E73','E74','E75','E76'],'Isolation, composition, recovery yield and functional acceptance preserve different constraints.'),
]
LAW_VARIABLES = {
 'MASS':['mass_flow','material_mass','time'],
 'ENERGY':['energy','time'],
 'CHARGE':['current','time'], 'KCL':['current','topology'],
 'OHM':['voltage','current','resistance','temperature'],
 'JOULE':['current','resistance'], 'ACPOWER':['voltage','current','phase'],
 'FARADAY':['flux','time'], 'TORQUE':['inertia','speed','torque','time'],
 'SHAFT':['torque','speed'], 'HEAT':['temperature','ambient_temperature','thermal_conductance'],
 'RAD':['temperature','ambient_temperature','emissivity'],
 'THERMAL':['temperature','thermal_capacity','heat_power','cooling_power','time'],
 'ENTROPY':['temperature','heat_power'], 'HYDRO':['water_flow','head'],
 'PV':['irradiance','cell_temperature'], 'EFFICIENCY':['efficiency'],
 'TRANSFORMER':['voltage','current','flux'], 'SAG':['span_length','tension'],
 'CLEARANCE':['clearance'], 'THERMAL_LIMIT':['temperature','time'],
 'SWITCH_ENERGY':['inductance','current','capacitance','voltage'],
 'STORAGE':['stored_energy','efficiency','time'],
 'BATTERY_CHARGE':['state_of_charge','charge_capacity','current','time'],
 'CAPACITY':['stored_energy','usable_capacity','power_limit'],
 'PUMP_SYSTEM':['water_flow','head','speed'],
 'HEAT_RECOVERY':['heat_power','temperature','service_temperature'],
 'DEGRADATION':['damage_state','time','temperature_history'],
 'ISOLATION':['residual_energy','isolation_state'],
 'RECOVERY_MASS':['material_mass','recovered_mass','reject_mass'],
 'MATERIAL_QUALITY':['material_composition','material_quality'],
}


# Reviewed physical-port refinements and directional state interfaces.
PORT_REFINEMENTS = r'''
E04||||weather_history|Resource observation retains time-resolved wind context at rotor location.
E06||temperature|||Withdrawn fluid carries temperature in addition to enthalpy; no equality of thermal and mechanical energy asserted.
E07||mass_flow|||Combustor outlet working-fluid mass carries products to exchanger.
E08|enthalpy,temperature|mass_flow,temperature|pressure,thermal_conductance,pressure_drop|pressure_drop|Heat exchanger transfers outlet mass and temperature; inlet state is branch-specific and pressure-drop state must be calibrated.
E09||enthalpy,mass_flow|speed|speed|Turbine exports exhaust fluid and shares speed with connected shaft; outlet enthalpy differs from inlet value.
E10||water_flow|speed,stored_energy|speed|Hydraulic turbine consumes reservoir energy/head and shares shaft speed; water flow is a physical outlet.
E11|||weather_history,speed|speed|Aerodynamic torque depends on local history and rotor speed; coupled shaft shares that kinematic state.
E12||temperature,pressure|||Condenser recirculates liquid state; return pressure is a distinct outlet port, not inlet equality.
E13|||speed||Shaft initial and coupled speed state is required to integrate torque balance.
E14|||rotor_angle|flux|Generator flux linkage and angle are machine states shared with terminal/load model.
E15|frequency|voltage,current|flux||Generator terminal voltage/current exported to transformer; internal flux enters qualified machine state.
E16||voltage|||PV operating-point voltage belongs to DC output terminal.
E18|current|voltage||temperature,power_limit|Inverter exports AC terminal voltage and device temperature/capability; input DC voltage is a separate local port.
E19||voltage|||Filter exports terminal voltage after frequency-dependent transfer.
E21||||phase,frequency|Synchronization conditions carry timestamped phase/frequency observations into interconnection.
E22|||temperature,power_limit|power_limit|Reactive allocation reports device-qualified capability state, not permission to dispatch.
E23||voltage|synchronism,switch_state,phase,frequency,reactive_power,power_limit,dispatch_horizon,health_estimate||Network model consumes connection/capability state; computed terminal voltage propagates to insulation and sensors.
E24|||line_temperature||Resistance depends on local conductor temperature received from heat balance.
E25||||core_temperature,weather_history,temperature_history|Conductor thermal model exports qualified core/history estimates and associated weather context; none are measured by default.
E26|||damage_state,creep_strain,temperature_history|mechanical_stress|Mechanical evolution consumes prior creep/damage and exports stress for ageing law.
E27|||creep_strain|creep_strain|Clearance calculation retains irreversible installed-length/creep contribution as a state dependency.
E28||||contact_resistance,damage_state|Connector model exports local resistance and condition estimates required by inspection/control.
E29|||||Leakage and insulation state are consumed at fault-transition boundary rather than mislabeled current conservation.
E30|||insulation_state,leakage_current||Fault model consumes the pre-fault insulation state and leakage signature; arc law remains unknown.
E31|||core_temperature,clearance,sag,creep_strain,hotspot_temperature,contact_resistance,damage_state|dispatch_horizon|Operating-envelope calculation jointly consumes component thermal/mechanical condition and retains decision horizon.
E32||||phase|Measurement subsystem exports timestamped phase alongside voltage/current; sensor-error model unknown.
E33|current|fault_current|phase||Protection receives measured current; fault_current is classified waveform forwarded for interruption energy accounting.
E34||||damage_state,temperature|Breaker interruption updates contact damage and temperature for restoration qualification.
E35||voltage|damage_state||Busbar terminal voltage is solved with circuit; equipment condition constrains allowable transfer.
E36||current|insulation_state,damage_state,repair_state,health_estimate|temperature_history|Transformer exports winding-current terminal and thermal history; repair/inspection state invalidates old capability.
E37|||damage_state,temperature||Restoration retains breaker thermal/damage state; topology is its physical decision output.
E38||load_demand,ac_power|current,switch_state,line_temperature,soil_thermal_resistivity,active_power||Distribution model receives boundary injection and cable state; branch terminal AC power follows local power balance.
E40||||soil_thermal_resistivity|Cable thermal profile exports soil parameter qualification; it is not measured soil condition without evidence.
E42||ac_power|||Service transformer exports terminal real power computed by waveform-aware power balance.
E44|||cell_temperature,usable_capacity,power_limit,internal_resistance,damage_state|cell_temperature,usable_capacity,current_history|Electrochemical charge consumes condition/capability and exports updated cell temperature, capacity assumption and current history.
E45||voltage|state_of_charge,cell_temperature,usable_capacity,power_limit,internal_resistance,damage_state|cell_temperature,usable_capacity,current_history|Discharge retains charge/ageing state, provides terminal voltage and heat/state histories; capacity remains externally qualified.
E46|heat_loss||||Cooling-loop heat inlet receives cell dissipation, distinct from externally supplied pump work.
E47||water_flow|||Pumped-storage reservoir state retains water transfer and head; turbine withdrawal is a later mode.
E48||heat_power|||Thermal storage discharge exports useful heat flux with temperature quality; cannot infer output duty from stored joules alone.
E49|||usable_capacity,internal_resistance,damage_state,energy||Allocator consumes condition plus metered delivered-energy observations; energy record is information, not a power port.
E50|||damage_state,remaining_life|speed,mechanical_stress,temperature|Motor shares shaft speed and exports stress/temperature condition for load and ageing models.
E51|||speed||Pump characteristic is conditioned on motor shaft speed.
E54||||temperature|Device heat-exhaust temperature conditions recoverability, independent of workload quantity.
E55||||temperature|Process heat supply and recoverable boundary temperature remain distinct from uncontrolled leakage.
E58|||stored_energy,temperature||Thermal service model consumes storage capacity and source temperature as state constraints.
E60|mass_flow|mass_flow,heat_power|||Condenser rejection stream may feed a selected heat-recovery branch; heat_power denotes that branch allocation, not duplicated heat.
E61||mass_flow,temperature|||Heat recovery exports outlet material state and temperature; recovered and residual heat branches need explicit energy allocation before simulation.
E62|||temperature||Heat-pump lift and efficiency depend on incoming waste-heat temperature.
E64|||temperature_history,creep_strain||Damage integral consumes thermal history and preexisting creep; no new history invented.
E65|||temperature_history||Insulation degradation integrates thermal history and moisture context.
E66|||current_history||Battery ageing integrates charge/discharge histories instead of only present current.
E67|||temperature||Fatigue and lubrication validity depend on thermal state in addition to mechanical load.
E68|||temperature|pressure_drop|Deposition model includes temperature and changes hydraulic resistance; constitutive relationship is uncalibrated.
E69|||hotspot_temperature,contact_resistance,damage_state,creep_strain,insulation_state,usable_capacity,internal_resistance,remaining_life|damage_state|Inspection combines observations into uncertain condition estimates; it does not create independent validation of input models.
E70|||health_estimate,failure_probability||Inspection outcomes motivate isolation priority but do not grant switching authority.
E71|||residual_energy,material_quality|material_quality,damage_state|Repair requires verified residual-energy state and qualified material; exports changed condition with unrepaired damage retained.
E72|||material_quality,damage_state|topology,repair_state,insulation_state|Return-to-service records actual configuration and condition; tests remain required.
E73|||health_estimate,damage_state,isolation_state,residual_energy|material_composition|Decommissioning carries inspection, residual-energy and composition records into actual safe dismantling boundary.
E74|||material_composition|contaminant_fraction|Sorting preserves composition and contamination information for separate material lots.
E75|||material_composition,contaminant_fraction|material_composition|Recovered-material composition is transformed by separation chemistry; process assay remains required.
'''

def _split(s):
    return [x.strip() for x in s.split(',') if x.strip()]

def _variables(s):
    return [{'name':n, 'unit':UNITS[n]} for n in _split(s)]

def _facets(stage, name):
    """All ten inspection surfaces, with scoped applicability rather than padding."""
    values = {
      'IdentityLifecycle':('APPLICABLE','Asset, material and state identities persist across '+name.lower()+'.'),
      'ScopeContext':('APPLICABLE','Operating regime, geometry and time scales bound the equations.'),
      'EpistemicsProvenance':('APPLICABLE','Physical sources, model assumptions and uncertainty remain explicit.'),
      'AuthorityHumanBoundary':('NOT_APPLICABLE','Descriptive offline physical model grants no actuation authority; deployment reopens human-effect review.'),
      'EffectsSafety':('APPLICABLE','Downstream thermal, electrical, mechanical or environmental effects must be retained.'),
      'DependencyValidity':('APPLICABLE','Material or model changes invalidate dependent predictions.'),
      'ResourceTermination':('APPLICABLE','Finite graph profile; unresolved detail remains outside coverage.'),
      'PrivacyRetention':('NOT_APPLICABLE','Seed contains no person-linked or operational customer data.'),
      'AuditExplanation':('APPLICABLE','Derived obligations cite law and transition witnesses.'),
      'RecoveryEvolution':('APPLICABLE' if stage>=12 else 'UNKNOWN','Material ageing and repair histories apply.' if stage>=12 else 'Reversibility is dimension-specific; detailed recovery not specified at this node.'),
    }
    if stage in (6,13,14):
        values['AuthorityHumanBoundary']=('UNKNOWN','Any real switching, maintenance or decommissioning requires separately grounded owner authority, safety and affected-human checks; absent in this simulator.')
    return {k:{'status':v[0],'reason':v[1]} for k,v in values.items()}

def _garden_source_records(repo_root):
    selections = [
      ('G-ABSTRACTION','design_deltas/v15.10/V15_10_ABSTRACTION_GCSC_DELTA.md',7,49),
      ('G-GCSC','design_deltas/v15.10/GSL_COMBINATORIAL_SEMANTIC_COVERAGE_v0.1.md',25,142),
      ('G-TREE-SUBSTRATE','design_deltas/v15.10/TREE_CORE_v0.8.1_2026-09-23.txt',85,215),
      ('G-TREE-TRUNK','design_deltas/v15.10/TREE_CORE_v0.8.1_2026-09-23.txt',236,335),
      ('G-TREE-OWNER','design_deltas/v15.10/TREE_CORE_v0.8.1_2026-09-23.txt',357,413),
      ('G-TECH-TYPES','design_deltas/v15.10/GARDEN_TECHNICAL_v15.10_FULL_DELTA.txt',90,274),
      ('G-TECH-EVIDENCE','design_deltas/v15.10/GARDEN_TECHNICAL_v15.10_FULL_DELTA.txt',353,409),
      ('G-TECH-THEORIES','design_deltas/v15.10/GARDEN_TECHNICAL_v15.10_FULL_DELTA.txt',534,707),
      ('G-SAL','design_deltas/v15.9.1/GCSC_SAL_SAC_DETAILED_SEMANTIC_PATCH.md',7,55),
      ('G-FUNCTIONS','design_deltas/v15.9.1/GCSC_FUNCTIONAL_CONTRACTS.md',1,29),
      ('G-GSK','design_deltas/v15.10/GENERATIVE_SEMANTIC_KERNEL_AND_DERIVED_GARDEN_CANDIDATE.md',42,132),
      ('G-RSDC','design_deltas/v15.10/RECURSIVE_SEMANTIC_DISCOVERY_COMPRESSION_RSDC_001.md',9,135),
      ('G-IDTD','design_deltas/v15.10/INVARIANT_DRIVEN_THEORY_DISCOVERY_IDTD_001.md',9,80),
    ]
    records=[]
    for sid,path,start,end in selections:
        p=Path(repo_root)/path
        if not p.exists():
            records.append({'id':sid,'path':path,'status':'SOURCE_UNAVAILABLE','line_start':start,'line_end':end})
            continue
        data=p.read_bytes(); lines=data.splitlines(keepends=True)
        if start < 1 or end < start or end > len(lines):
            records.append({'id':sid,'path':path,'status':'SOURCE_SPAN_UNAVAILABLE','line_start':start,'line_end':end,'available_lines':len(lines),'source_sha256':hashlib.sha256(data).hexdigest()})
            continue
        lo=sum(map(len,lines[:start-1])); hi=sum(map(len,lines[:end]))
        records.append({'id':sid,'path':path,'line_start':start,'line_end':end,'byte_start':lo,'byte_end':hi,
          'source_sha256':hashlib.sha256(data).hexdigest(),'span_sha256':hashlib.sha256(data[lo:hi]).hexdigest(),
          'status':'NONCANONICAL_SOURCE_BOUND','owner':path,'scope':'Research adapter architecture; not canonical admission','disposition':'RESEARCH','hash_meaning':'Exact bytes read for this build, not certification of unchanged historical baseline'})
    return records

def build_seed(repo_root=None):
    laws=[]
    for ident,typ,eq,domain,assumptions,falsifier,units,sources in LAW_ROWS:
        laws.append({'id':ident,'type':typ,'equation':eq,'domain':domain,'assumptions':[assumptions],
           'falsifier':falsifier,'units':units,'source_refs':_split(sources),
           'required_variables':LAW_VARIABLES[ident][:], 'scope':domain,
           'validity':'CONDITIONAL_ON_ASSUMPTIONS_AND_ASSET_QUALIFICATION',
           'operand_note':'Variables are observation/parameter obligations, not assumed supplied values. Balance ports depend on declared control volume; unbound coefficients and thresholds remain UNKNOWN.',
           'status':{'science':'ESTABLISHED_FRAMEWORK' if typ in ('EXACT_BALANCE','EXACT_FIELD_LAW','SECOND_LAW_CONSTRAINT') else 'SCOPED_MODEL_OR_CONSTRAINT',
                     'formula_review':'AUTHOR_FORMULATION_REQUIRES_DOMAIN_REVIEW','empirical':'NOT_VALIDATED_FOR_ASSET','admission':'NONCANONICAL_RESEARCH'},
           'owner':'external_domain_science:'+ident,'garden_source_refs':['G-TECH-THEORIES','G-IDTD']})
    law_by_id={x['id']:x for x in laws}; situations=[]
    parent_map={n:(gid,reason) for gid,stage,name,nodes,reason in PROCESS_GROUPS for n in nodes}
    for line in SITUATION_ROWS.strip().splitlines():
        ident,stage,branch,name,inputs,outputs,state,laws_s,assumption,unknown=line.split('|')
        stage=int(stage); c=_split(laws_s)
        objects=[{'id':ident+':asset','type':'THING','label':name},
                 {'id':ident+':event','type':'EVENT','label':name+' evolution'},
                 {'id':ident+':time','type':'TIME','label':'Resolved interval; duration unspecified'},
                 {'id':ident+':space','type':'SPACE','label':'Declared component/control volume'},
                 {'id':ident+':context','type':'CONTEXT','label':assumption}]
        relations=[{'relation':'contextualizes','source':ident+':context','target':ident+':event'},
                   {'relation':'dependsOn','source':ident+':event','target':ident+':asset','dependency_kind':'physical_state'}]
        for law in c:
            objects.append({'id':ident+':rule:'+law,'type':'RULE','label':law})
            relations.append({'relation':'obeys','source':ident+':asset','target':ident+':rule:'+law,'scope':'physical modelling obligation, not normative authority'})
        situations.append({'id':ident,'stage':stage,'branch':branch,'name':name,'objects':objects,'relations':relations,
          'parent_id':parent_map[ident][0],'depth':3,'expansion_reason':parent_map[ident][1],
          'control_volume':{'boundary':name+' component/interaction boundary; detailed geometry UNKNOWN',
             'kind':'OPEN_OR_COUPLED_SUBSYSTEM','boundary_ports':_variables(inputs)+_variables(outputs),
             'mass_ports':[v for v in _split(inputs)+_split(outputs) if v in ('mass_flow','water_flow','material_mass','recovered_mass','reject_mass','emissions_flow','coolant_flow')],
             'stored_state':_split(state),'environment_ports':['thermal exchange','mechanical/electrical/material exchange where applicable'],
             'closure_status':'UNKNOWN_PENDING_ASSET_BOUNDARY_AND_PORT_CALIBRATION',
             'energy_accounting':'No isolated-system energy constancy asserted; input-output balance includes storage, work, radiation, heat and material enthalpy as applicable.'},
          'scope':{'operating_domain':assumption,'validity':'CONDITIONAL; PARAMETERS_UNKNOWN','expansion_frontier':unknown},
          'forms':['CONSTRUCT','STATE','PROCESS','RULE','CONTRACT','RELATION','PROJECTION'],
          'inputs':_variables(inputs),'outputs':_variables(outputs),'state_required':_split(state),
          'constraints':c,'assumptions':[assumption],'unresolved_state':[unknown],
          'facets':_facets(stage,name),'source_refs':sorted({s for x in c for s in law_by_id[x]['source_refs']}),
          'garden_source_refs':['G-ABSTRACTION','G-SAL','G-TECH-THEORIES'],
          'status':{'structural':'RESEARCH_TYPED','completeness':'PARTIAL','join':'UNVERIFIED_RESEARCH_PROFILE',
                    'coherence':'REQUIRES_CONTEXT_CHECK','interpretation':'SCOPED_PHYSICAL_ADAPTER','admission':'NONCANONICAL'},
          'coverage_scope':'CURATED_REPRESENTATIVE; not exhaustive physical situations'})
    by_id={x['id']:x for x in situations}
    for row in PORT_REFINEMENTS.strip().splitlines():
        ident,pin,pout,sin,sout,reason=row.split('|'); node=by_id[ident]
        for key,names in [('inputs',pin),('outputs',pout)]:
            existing={v['name'] for v in node[key]}
            node[key].extend(v for v in _variables(names) if v['name'] not in existing)
        for direction,names in [('input',sin),('output',sout)]:
            node.setdefault('state_ports',[]).extend({'name':v['name'],'unit':v['unit'],'direction':direction,
                'role':'STATE_OBSERVATION_OR_QUALIFIED_PARAMETER','ownership_reason':reason,
                'value_status':'UNKNOWN_UNTIL_MEASURED_OR_MODEL_QUALIFIED'} for v in _variables(names))
        node['port_refinement_reason']=reason
    transitions=[]
    ids={x['id'] for x in situations}; by_id={x['id']:x for x in situations}
    for n,line in enumerate(EDGE_ROWS.strip().splitlines(),1):
        source,target,kind,vars_s=line.split(' ',3); names=_split(vars_s)
        assert source in ids and target in ids
        transitions.append({'id':f'T{n:03d}','source':source,'target':target,'kind':kind,
          'transfers':names,'required_transfers':names[:], 'transfer_units':{v:UNITS[v] for v in names},
          'constraints':sorted(set(by_id[source]['constraints']) & set(by_id[target]['constraints'])),
          'assumptions':['Ports may be conditioned/transformed; identity of variable name does not imply equality across components.','Temporal edges carry ordered dependency, feedback edges require joint iteration or dynamic states.'],
          'source_refs':sorted(set(by_id[source]['source_refs']+by_id[target]['source_refs'])),
          'garden_source_refs':['G-TECH-TYPES','G-SAL'],
          'status':'CURATED_INTERFACE_REQUIREMENT; not independently verified physical closure',
          'unresolved_state':['Asset-specific geometry, limits and uncertainty have not been calibrated.']})
    incoming={x['id']:[] for x in situations}
    for tr in transitions:
        incoming[tr['target']].append(tr)
    ambient={'ambient_temperature','irradiance','wind_speed','wind_direction','air_density','soil_temperature','soil_moisture','time','load_demand','flow_demand','cooling_power','coolant_flow','process_power','processing_temperature','contaminant_fraction','moisture','quality_signal','inspection_signal'}
    for node in situations:
        node['input_origins']=[]
        for inp in node['inputs']+[p for p in node.get('state_ports',[]) if p['direction']=='input']:
            name=inp['name']; edges=[x['id'] for x in incoming[node['id']] if name in x['transfers']]
            status='UPSTREAM_REQUIREMENT_UNVERIFIED' if edges else ('EXTERNAL_CONTEXT_REQUIRED' if name in ambient else ('LOCAL_STATE_REQUIRED' if name in node['state_required'] else 'UNKNOWN_INTERFACE_OR_EXTERNAL_PORT'))
            node['input_origins'].append({'variable':name,'unit':inp['unit'],'status':status,'transition_refs':edges,
              'value_status':'UNKNOWN; no asset measurement or numerical parameter supplied',
              'reason':'An incoming named requirement is not proof of measured availability, compatibility or equal value across ports.'})
        node['composite_motifs']=[{'kind':'multi_input_join','transition_refs':[t['id'] for t in incoming[node['id']]],
             'join_status':'UNKNOWN_UNTIL_SHARED_TIME_GEOMETRY_AND_MODEL_BINDINGS_VERIFIED'}] if len(incoming[node['id']])>1 else []
    if repo_root is not None:
        root=Path(repo_root)
    else:
        root=next((ancestor for ancestor in Path(__file__).resolve().parents
                   if (ancestor/'canonical/current/SOURCE_MANIFEST.json').exists()),
                  Path(__file__).resolve().parent/'garden-main')
    return {'schema':'GardenElectricityResearchSeed/v1','profile':{
      'status':'NONCANONICAL_RESEARCH_ADAPTER','scope':'77 curated situations in 14 stages; branching lifecycle with storage, maintenance and material feedback',
      'complete_gsl_compiler':False,'canonical_admission':False,'physical_coverage':'INCOMPLETE',
      'full_sal_registries':'UNAVAILABLE','tree_core_release_gates':'NOT_REASSESSED',
      'generation':'Curated reality-first seed and deterministic obligation binding; not blind autonomous discovery',
      'source_rule':'Domain science supplies physical laws; Garden supplies typed bookkeeping and qualification controls',
      'unexpanded_frontier':['nuclear criticality, fuel preparation and radioactive waste','HVDC converters/cables and grid-forming control','marine/tidal generation and hydrogen storage','multi-species chemistry and pollutant dispersion','asset-specific geometry, protection and operating standards','uncertainty-calibrated economic dispatch and field measurements'],
      'maximum_depth':4,'termination':'Single finite seed construction; optional bounded traversal handled by harness'},
      'core_objects':CORE_OBJECTS[:],'core_relations':CORE_RELATIONS[:],'forms':DESIGN_FORMS[:],'facets':FACETS[:],
      'decomposition':[{'id':'ELECTRICITY','parent_id':None,'depth':0,'name':'Bounded electricity lifecycle','expansion_reason':'Follow energy, material and equipment condition across conversion and service.'}] +
         [{'id':f'S{n:02d}','parent_id':'ELECTRICITY','depth':1,'name':name,'expansion_reason':'Distinct physical lifecycle boundary with material or economic consequences.'} for n,name in STAGES] +
         [{'id':gid,'parent_id':f'S{stage:02d}','depth':2,'name':name,'children':nodes,'expansion_reason':reason} for gid,stage,name,nodes,reason in PROCESS_GROUPS],
      'stages':[{'id':n,'name':name} for n,name in STAGES],'situations':situations,'transitions':transitions,
      'laws':laws,'sources':copy.deepcopy(SOURCES),'garden_sources':_garden_source_records(root)}

if __name__=='__main__':
    seed=build_seed()
    print(f"{len(seed['situations'])} situations; {len(seed['transitions'])} transitions; {len(seed['laws'])} laws; {len(seed['garden_sources'])} source spans")
