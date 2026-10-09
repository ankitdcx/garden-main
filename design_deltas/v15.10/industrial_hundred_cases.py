#!/usr/bin/env python3
"""Garden v15.10 bounded industrial research adapter: N001-N100.

NONCANONICAL. Numerical replay is not field validation, scientific novelty,
measured savings, canonical GSL encoding or full GCSC admission. All prices,
improvement targets and facility scales are scenario assumptions.

Usage: python industrial_hundred_cases.py
       python industrial_hundred_cases.py --case N072
       python industrial_hundred_cases.py --details
Standard library only; no network, plant control, external source files or writes.
Do not use Python -O: the source-role physical checks contain assertions.

Source-role modules are statically embedded in isolated functions below.
Integration removes their report-writing functions and main blocks, adds an
outer function scope, and adds graph, financial and uncertainty audits.
Original hashes identify inputs; they do not certify external-source truth.
"""
import argparse
import collections
import hashlib
import json
import math

BASE_COMMIT = '512b7cbefa8d3bac9736f0bce7efa87db1bf50e0'
CRF = .08 / (1 - 1.08 ** -10)


# Source SHA256: cfe897a2d6887f9d17155ef5a1e41f813ff431cfa1ad441e0d9fdb31b0240f11
def workstream_separations():
    """N001-N020 bounded Garden research adapter; all scenarios ASSUMED, not observed."""
    import math
    CRF=.08/(1-(1.08)**-10)
    CASES=[]
    def add(i,title,nodes,cross,constraints,equation,q,gain,price,opex,capex,unit,physical,operators,baseline,status,sources,source_note,falsifier):
        gross=q*gain*price
        CASES.append(dict(id=f'N{i:03d}',title=title,nodes=nodes.split('|'),edges=[(j,j+1) for j in range(1,len(nodes.split('|')))]+cross,constraints=[dict(type=t,scope=s,statement=x) for t,s,x in constraints],equation=equation,inputs=dict(assumption_status='ALL ASSUMED; neither plant measurement nor current market quote',annual_activity=q,improvement=gain,unit_value_usd=price,activity_and_improvement_units=unit,opex_usd_y=opex,capex_usd=capex,capital_recovery_factor=CRF),physical_prediction=physical,financial=dict(gross=gross,opex=opex,capex=capex,annualized_capex=capex*CRF,net=gross-opex-capex*CRF,break_even=opex+capex*CRF,break_even_improvement=(opex+capex*CRF)/(q*price) if q*price else None,units='gross/opex/net/break_even USD/year; capex USD once',increment_vs_best_baseline_usd_y=None),operators=dict(zip(['Projection-Loss','Necessity-Challenge','Decision-Sufficiency'],operators)),baseline=baseline,novelty=status,status=status,sources=sources,source_note=source_note,falsifier=falsifier))
    add(1,'Distillation cut routing constrained by final receiver purity',
    'Charge batch|Establish reflux|Condense first cut|Route transition cut|Collect main cut|Mix qualified receiver|Recycle remaining offcut',[(3,6),(5,4),(7,1)],
    [('CONSERVATION','1-7','Each species entering equals sold plus recycled plus waste plus inventory change.'),('ENGINEERING','4-6','Blending is allowed only when every contaminant limit and receiver mixing requirement holds.'),('CONSTITUTIVE','2-3','Vapor-liquid equilibrium and column holdup depend on pressure and composition.')],
    'M_accept <= M_good*(c_limit-c_good)/(c_off-c_limit), for c_off>c_limit>c_good; kg times dimensionless ratios gives kg.',500,500,.4,20000,200000,'batches/year; kg avoided redistillation/batch; USD/kg marginal redistillation cost',
    'ASSUMED 10000 kg main cut at impurity0.001, offcut0.021 and limit0.002 admit at most526.316kg; target500kg gives mixed impurity0.00195238. No product-sales credit.',
    ['Equal instantaneous overhead purity but different receiver inventory gives different admissible cut routing.','A cut need not individually meet a batch-average specification when blending is permitted.','Assay and valve timing earn value only through avoided reprocessing after same final quality.'],
    'Compare against published cumulative-purity receiver/offcut recycling and full batch-distillation campaign optimization; historical intervention already exists.','KNOWN',
    ['https://patents.google.com/patent/US6638397B1/en','https://pubs.acs.org/iecred/article/45/26/8998/3471739/Multicomponent-Batch-Distillations-Campaign'],
    'Patent full text inspected: cumulative collected purity and transition tanks. ACS search record retrieved, full page403. Neither establishes our costs.',
    'An unmeasured impurity, receiver stratification or an individual-cut specification invalidates routing; contemporary campaign optimizer may already save all500kg.')
    add(2,'Wet-cake solvent exchange endpoint accounts for inaccessible pore liquor',
    'Crystallize|Drain free mother liquor|Measure retained liquid|Wash accessible pores|Hold for diffusion|Displace again|Dry accepted cake',[(3,6),(5,4),(4,7)],
    [('CONSERVATION','2-7','Initial solvent equals wash filtrate plus remaining cake plus captured dryer solvent.'),('CONSTITUTIVE','4-6','Two-zone exchange coefficients require tracer calibration; slow pores cannot be assumed clean.'),('ENGINEERING','7','Residual solvent and impurity limits hold throughout accepted product.')],
    'R(n)=(1-f)*exp(-n)+f*exp(-k*n); n wash-pore-volumes, f trapped fraction and k relative exchange rate dimensionless.',400,1500,.25,30000,300000,'batches/year; kg wash solvent avoided/batch; USD/kg net recovery duty',
    'ASSUMED f0.1,k0.05,n5 gives residual0.083944; a single well-mixed model predicts0.006738. A hold improving exchange must be measured;1500kg saving is target, not inferred from this discrepancy.',
    ['Same drained cake mass may retain different inaccessible mother liquor.','Continuous high-volume washing is not necessary if diffusion hold plus displacement meets residual limits.','Additional pore-liquor assay matters only if it safely reduces solvent and drying duty.'],
    'Two-zone diffusion/displacement models, solvent exchange and countercurrent wash are established; compare with validated process analytical endpoint control.','OVERLAP',
    ['https://patents.google.com/patent/US3433816A/en','https://pmc.ncbi.nlm.nih.gov/articles/PMC8787817/'],
    'Patent inspected: intermediate solvent displacement and recovery. Constant-rate washing paper abstract retrieved; PMC full retrieval blocked.',
    'If hold time reduces annual accepted output or diffusion does not improve enough, net benefit falls; negative solvent balance invalidates claimed saving.')
    add(3,'Centrifuge wash distribution adjusted before cake channels form',
    'Form cake|Compact cake|Measure wash resistance|Distribute wash|Sample filtrate|Measure cake impurity|Discharge',[(2,4),(5,3),(6,4)],
    [('CONSERVATION','4-6','Solute washed out plus retained equals prewash solute.'),('CONSTITUTIVE','2-4','Permeability distribution controls channel bypass; Darcy relation applies only in stated laminar regime.'),('ENGINEERING','6-7','Worst sampled cake impurity and mechanical speed limits govern acceptance.')],
    'Effective wash n_eff=(1-b)*Vw/Vp; ideal mixed-pore residual exp(-n_eff). Holding residual fixed gives Vnew/Vold=(1-bold)/(1-bnew).',600,800,.2,18000,180000,'batches/year; kg wash solvent avoided/batch; USD/kg recovery cost',
    'ASSUMED bypass falls0.30to0.10; same modeled residual needs77.778% of prior wash. At3600kg/batch this is800kg; channel-removal target unmeasured.',
    ['Same total wash volume hides bypassed cake regions.','Uniform constant-speed washing is not necessary; controlled distribution may meet cake quality.','Resistance/impurity sampling must change distribution decisions enough to cover costs.'],
    'Basket centrifuge optimization already links cake mass, impurity, permeability and wash ratio; compare with optimized spray and cake-churning systems.','KNOWN',
    ['https://patents.google.com/patent/US6328897B1/en','https://patents.google.com/patent/US5948256A/en'],
    'First patent full text inspected; second retrieved search record. Both describe established wash-control mechanisms.',
    'If reduced bypass is not observed or worst cake region fails purity, claimed800kg saving is rejected; reslurrying may consume more energy than credited.')
    add(4,'Recover crystallizer fines without returning their impurity-rich liquor',
    'Feed crystallizer|Grow crystals|Classify fines|Separate liquor|Wash recovered fines|Return solid seed|Purge impurity liquor',[(6,2),(7,1),(4,2)],
    [('CONSERVATION','1-7','Steady impurity input equals purge plus product impurity; internal recycling is not removal.'),('ENGINEERING','2,7','Liquor impurity stays below solubility and product-contamination limits.'),('CONSTITUTIVE','3-5','Classification and wash selectivity determine product recovery versus impurity entrainment.')],
    'Pmin=Iin/Cmax; Iin kg/h, Cmax kg/m3, Pmin m3/h. Net clean-solid recovery=solid_capture*(1-impurity_rejection_loss), separately measured.',8000,40,1,50000,600000,'operating h/year; kg additionally accepted fines/h; USD/kg marginal product value',
    'ASSUMED impurity input100kg/h and limit20kg/m3 require at least5m3/h purge if product impurity negligible. Returning all liquor at2m3/h implies50kg/m3 and fails. Fortykg/h clean solids is a test target.',
    ['Equal solids recycle flow does not imply equal impurity return.','Discarding fines with purge is not necessary if a separate clean solid stream can be proved.','Particle/solute assays must raise accepted recovery without shifting impurities into product.'],
    'Fines classification, mother-liquor impurity purge and soda-value recovery already published; financial comparator already maintains the compliant5m3/h purge. The2m3/h example is only an invalid counterexample. USD1/kg is net accepted-product value; added wash, separation and waste handling are included in assumed OPEX50000/year.','KNOWN',
    ['https://patents.google.com/patent/EP2566815B1/en','https://patents.google.com/patent/FR2881360A1/en'],
    'EP full text inspected: impurity buildup, purge and solid recovery. FR search record describes fines and mother-liquor recycle classification.',
    'At equal annual terminal impurity inventory, no net purge reduction is possible without an additional impurity exit; altered crystal habit can erase recovery.')
    add(5,'Ion-exchange regenerant fractions reused with sodium-to-hardness ledger',
    'Load resin|Displace service water|Regenerate resin|Split early and late fractions|Assay sodium and hardness|Reuse qualified brine|Purge rejected ions',[(5,3),(6,3),(7,1)],
    [('CONSERVATION','1-7','Charge equivalents and each ion mass close over repeated regeneration cycles.'),('CONSTITUTIVE','3,6','Exchange selectivity depends on activities and resin loading, not conductivity alone.'),('ENGINEERING','5-6','Restored capacity and downstream hardness leakage must match reference.')],
    'Ehard=2*nCa+2*nMg in mol charge; usable regenerant requires measured Na/hardness activity ratio. Avoided NaCl=q*delta_salt; no savings from storing hardness.',1000,1000,.15,25000,200000,'regenerations/year; kg virgin NaCl avoided/regeneration; USD/kg NaCl',
    'ASSUMED1000kg fresh-salt displacement each regeneration; conductivity-matched brines with different Ca fractions are not equivalent. Performance must be proved at periodic resin and tank state.',
    ['Equal conductivity hides ion selectivity and divalent-ion return.','All spent brine need not be discarded if reusable fractions preserve regeneration capacity.','Ion-specific assay is useful only if it changes fraction cutoff and saves net salt.'],
    'US9776137B2 explicitly separates recovered brine by NaCl concentration and Na/Ca ratio and uses lowest-quality fractions first; broad idea already anticipated.','KNOWN',
    ['https://patents.google.com/patent/US9776137B2/en'],
    'Full text inspected, including quality-segregated tanks and recovery endpoint options; not evidence for assumed1000kg gain.',
    'Hardness accumulation, lower resin capacity or extra wastewater/energy exceeding savings falsifies the scenario.')
    def run():
        return [dict(x) for x in CASES]
    add(6,'EDR reversal routing constrained by a locked batch-tank salt budget',
    'Produce diluate|Reverse stack polarity|Displace concentrated holdup|Measure outlet salt|Route to locked tank or reject|Mix entire batch|Release accepted process water|Complete tank drawdown',[(3,6),(4,5),(8,1)],
    [('CONSERVATION','1-8','Salt and water close across stack, tank, rejection and delivered batch; inventory cannot fund recurring benefit.'),('CONSTITUTIVE','3','Illustrative stack/manifold holdup is a CSTR; residence-time tails and sensor delay require independent identification.'),('ENGINEERING','5-8','No withdrawal before mixing; all specified species and product concentration limits must hold, not salinity alone.')],
    'c(t)=ci+(c0-ci)*exp(-Q*t/Vh); Mexcess=Vh*(c0-ci)*(1-exp(-Q*T/Vh)); final c=(Vb*cb+Q*T*ci+Mexcess)/(Vb+Q*T). Concentration mg/L=g/m3, volume m3.',1320,100,2.5,25000,300000,'reversal/batch events/year; m3 reject plus replacement avoided/event; USD/m3 combined marginal cost',
    'ASSUMED Vh40m3,Q20m3/min,c03000,ci=cb100mg/L,Vb200m3,T10min: final locked400m3 batch388.05mg/L<500. Fixed5min diversion rejects100m3 then replaces it with100m3 fresh water. Both deliver400m3. Full drawdown and200m3 normal replenishment precede each event; no persistent clean-tank headroom loan.',
    ['Same outlet salt history produces different acceptability with different batch inventory.','Every transient parcel need not meet final industrial batch spec if permitted whole-batch mixing is proven.','Tank inventory and assay can reduce diversion only when they alter safe routing; all additional analysis/valving costs counted.'],
    'Published conductivity/time/flow reversal routing already exists. Compare against those plus standard batch inventory-aware control; equipped-control equality establishes no Garden advantage, while patents independently establish broad overlap.','OVERLAP',
    ['https://patents.google.com/patent/US8142633B2/en','https://patents.google.com/patent/US9227857B2/en'],
    'First full text inspected. Second independently inspected by referee: reversal product-tank protection and conductivity endpoint. Integrated batch budget is a narrow implementation question, not a novel conservation law.',
    'If required quality is instantaneous, buffer is too small, an unmeasured ion is hazardous, or downstream reuse accumulates salt, routing fails. Periodic all-stream balance and equal delivered service are required.')
    add(7,'Recover filter backwash water while enforcing a solids purge',
    'Filter incoming water|Backwash retained solids|Collect dirty water|Settle solids|Withdraw sludge|Return qualified supernatant|Refilter recovered water',[(7,1),(3,5),(6,2)],
    [('CONSERVATION','1-7','Solids input must leave in sludge/waste or accepted outlet; recycling cannot remove solids.'),('ENGINEERING','4-7','Hydraulic capacity, source-specific contaminants and filtration integrity remain bounded.'),('EMPIRICAL','4-6','Settling capture must be determined on actual solids, not inferred from water recovery.')],
    'Mnext=(1-r)*(M+Min) for fraction r of combined solids removed each cycle. At steady M=(1-r)*Min/r; r=0 yields unbounded accumulation.',10000000,.02,2,100000,2000000,'m3 treated/year; additional recovered m3/m3 treated; USD/m3 marginal water and discharge cost',
    'ASSUMED Min100kg/cycle,r0.8 gives25kg residual periodic solids; r0 has no bounded steady state. Additional2% water recovery must retain that solids exit and all quality barriers.',
    ['Equal recycled volume does not preserve total accumulated solids.','Discarding every backwash stream is not necessary if sludge removal and treatment remain effective.','Solids and hydraulic measurements matter only if qualified supernatant return reduces actual purchased water.'],
    'EPA backwash recycling guidance explicitly covers solids removal, equalization and treatment capacity; no new broad relationship. This is an industrial process-water scenario, not authorization for potable reuse.','KNOWN',
    ['https://nepis.epa.gov/Exe/ZyPURL.cgi?Dockey=200025V5.TXT'],
    'Full technical guidance inspected; used for engineering prior art, not a claim about current jurisdictional requirements.',
    'Recycle without a demonstrated contaminant exit, or any degraded downstream water specification, invalidates the2% recovery and may increase cost.')
    add(8,'DAF recycle setpoint based on delivered microbubble mass',
    'Condition wastewater|Pressurize recycle|Dissolve air|Release pressure|Contact bubbles and flocs|Float solids|Return clarified recycle',[(7,2),(3,5),(1,5)],
    [('CONSERVATION','2-5','Dissolved air entering minus gas retained/vented equals released gas; pressure alone is not gas mass.'),('CONSTITUTIVE','3','Cout=Ceq*(1-exp(-kLa*t)) only for a well-mixed batch/contact parcel or plug-flow residence approximation; not a continuous CSTR.'),('ENGINEERING','5-6','Same solids capture and bubble-size distribution must be maintained; large gas bubbles are not equivalent.')],
    'Cout=H(T)*p*(1-exp(-kLa(T)*t)); mg/L if H in mg/(L bar),p bar,t s,kLa1/s. Pump energy=q*deltaP/(3.6e6*eta), q m3 and deltaP Pa.',8000000,.02,.1,12000,150000,'m3 feed/year; kWh/m3 target electric saving; USD/kWh',
    'ASSUMED equilibrium gas capacities100and80mg/L, kLa*t0.3and0.6 give25.92and36.10mg/L actually dissolved. Warmer water can deliver more gas despite lower equilibrium solubility. Target0.02kWh/m3 remains unmeasured.',
    ['Equal pressure and recycle flow conceal unequal gas transfer at different temperatures.','A higher pressure after warming is not always necessary if kinetics improve.','Measure released gas and capture quality before lowering pressure or recycle flow.'],
    '2012 and2019 experiments already optimize saturation pressure, temperature and mass transfer; compare with calibrated DAF gas-transfer and collision models.','REJECTED',
    ['https://repository.lsu.edu/bio_engineering_pubs/528/','https://ro.ecu.edu.au/ecuworkspost2013/7333/'],
    'Both author-institution abstracts inspected.2019 explicitly reports equilibrium/non-equilibrium temperature differences; physical mechanism known. This cost screen is negative.',
    'If bubbles enlarge, capture falls, or measured electric saving is below break-even, no economic benefit; temperature control energy cannot be omitted.')
    add(9,'Capture dissolved methane before aerobic polishing',
    'Anaerobic conversion|Separate suspended solids|Measure dissolved methane|Degas through contactor|Collect qualified fuel gas|Aerobically polish water|Use recovered gas',[(3,4),(5,7),(4,6)],
    [('CONSERVATION','1-7','Methane produced equals headspace gas plus recovered dissolved gas plus oxidized/emitted methane plus inventory.'),('CONSTITUTIVE','4','Removal fraction1-exp(-kLa*t) assumes negligible gas-side methane and calibrated transfer.'),('ENGINEERING','5,7','Recoverable heating value requires actual gas composition and compatible combustion; losses and auxiliary loads counted.')],
    'mCH4=Q*C*eta; C kg/m3,Q m3/year. Euse=mCH4*13.9*eta_use kWh/year with13.9kWh/kg ASSUMED methane lower heating value.',10000000,.018*.75*13.9*.8,.05,55000,2000000,'m3 wastewater/year; useful thermal kWh/m3; USD/kWh displaced heat',
    'ASSUMED18mg/L methane,75% capture,80% useful-heat efficiency yield1,501,200kWh/year. Electricity-generation value is not added to the same fuel. With these costs the opportunity is negative.',
    ['Equal headspace biogas yield hides methane leaving in liquid.','Aerobic oxidation is not necessary for all dissolved methane if capture meets effluent quality.','Dissolved-gas assay changes recovery operation only when marginal recovered energy exceeds auxiliaries.'],
    'Published membrane-contactor experiments and net-energy optimization already address this interface; compare with tuned vacuum/sweep-gas recovery and direct biological oxidation.','REJECTED',
    ['https://www.sciencedirect.com/science/article/pii/S0376738815303847','https://pubmed.ncbi.nlm.nih.gov/31244075/'],
    'Targeted primary research abstracts retrieved in search; full article access failed. Do not infer a complete current-frontier review or import their efficiencies into this assumed scenario.',
    'Wet membranes, low methane concentration, unrecoverable diluted gas or high vacuum power erase benefit. No carbon-credit value has been assumed.')
    add(10,'Remove CO2 before ammonia recovery with an alkalinity ledger',
    'Characterize digester liquor|Strip carbon dioxide|Capture any co-stripped ammonia|Measure DIC TAN and alkalinity|Add required caustic|Recover ammonia in acid trap|Release qualified residual liquid',[(2,4),(3,6),(4,5)],
    [('CONSERVATION','1-7','Total nitrogen, inorganic carbon and charge equivalents close across liquid, gas and acid trap.'),('CONSTITUTIVE','2-5','CO2-only transfer conserves total alkalinity; NH3 transfer, precipitation and chemical dosing do not.'),('ENGINEERING','6-7','Equal recovered TAN and qualified residual liquid are required; lower pH-dose cost alone is insufficient.')],
    'A=CT*(alpha1+2*alpha2)+TN*fNH3+[OH]-[H]; mol-equivalent/L. For common INITIAL feed alkalinity A0 and TAN, actual avoided NaOH=40*[max(0,A_target(CT0)-A0)-max(0,A_target(CT1)-A0)] kg/m3. At targetpH10,TN0.04mol/L,A0.04eq/L both demands positive, giving40*(CT0-CT1)*(alpha1+2alpha2). CO2-only transfer preserves initial A; final target A differs with CT. Include any NH3-loss correction.',800000,.5,.5,56000,500000,'m3 liquor/year; kg NaOH/m3 avoided TARGET; USD/kg NaOH',
    'ASSUMED targetpH10,pKa16.35,pKa210.33,CT0.06to0.02mol/L give2.11kg/m3 ideal CO2-only caustic difference. Economic target0.5kg/m3 is not a prediction of an actual stripper. NH3 co-loss and carbon outputs must be measured; zero CO2 removal gives zero difference.',
    ['Equal pH hides different titratable alkalinity and inorganic-carbon inventories.','Caustic-first alkalization is not necessary when selective CO2 removal reaches the same nitrogen-recovery outcome.','DIC/TAN/alkalinity assays matter only if they change dosing beyond ordinary titration and cover stripping cost.'],
    'CO2 removal before ammonia stripping already appears in US7811455B2 and a2025 membrane-contactor pilot study. Compare equal-TAN integrated stripper/acid-capture process, including carbonate solids and all gas losses.','KNOWN',
    ['https://patents.google.com/patent/US7811455B2/en','https://www.mdpi.com/2077-0375/15/2/62'],
    'Patent full text inspected.2025 study search abstract retrieved; MDPI full retrieval failed, referee independently inspected PMC11857175. Published measured23% is NOT our target or input.',
    'If co-stripped ammonia is not recovered, alkalinity changes are ignored, or final carbon accumulation differs between repeated runs, caustic saving cannot be credited.')
    add(11,'RO brine softening with an explicit crystal carryover barrier',
    'Pressurize feed|Produce permeate and brine|Grow scale on seed crystals|Retain crystals by microfiltration|Check dissolved saturation and particle carryover|Recycle conditioned brine|Purge solids and nonprecipitating ions',[(6,1),(7,3),(4,3),(5,1)],
    [('CONSERVATION','1-7','Calcium and carbonate removed from water must appear in solids or purge; nonprecipitating salt cannot disappear.'),('CONSTITUTIVE','3,5','Ion activity product and nucleation/growth kinetics govern precipitation; saturation index is not itself a rate.'),('ENGINEERING','4-6','RO particulate limit and all scale-forming species remain controlled at higher recovery.')],
    'Solid CaCO3 kg/h=100.09*deltaCa kmol/h. RO additional water=Q*(Rnew-Rold); residual nonprecipitating salt concentration scales approximately1/(1-R).',8000000,.05,2,250000,2000000,'m3 RO feed/year; additional permeate m3/m3 feed TARGET; USD/m3 marginal water/disposal value',
    'ASSUMED recovery0.75to0.80 yields400000m3/year; nonprecipitating salt concentration factor rises4to5. Precipitating1kmolCa/h creates100.09kg/h dry CaCO3 requiring separation. Higher recovery is not free concentration capacity.',
    ['Equal dissolved hardness at recycle inlet can hide different seed carryover and nonprecipitating salt.','Discarding all RO concentrate is not necessary if controlled precipitation and solids separation preserve membrane limits.','Particle plus ion assays must change recycle decisions enough to justify added unit operations.'],
    'US7077962B2 already joins seeded concentrate precipitation, MF separation, pH cycling and RO recovery control. Compare complete high-recovery RO/softening process, not untreated brine discard.','KNOWN',
    ['https://patents.google.com/patent/US7077962B2/en'],
    'Full patent inspected, including operating-sequence and barrier descriptions. Its claims are prior art, not validation of our5percentage-point target.',
    'Seed leakage, silica/sulfate limits, pressure growth or sludge disposal can erase the target. Equal membrane life and accepted permeate must be maintained.')
    add(12,'Ozone dose coordinated with downstream biofilter carbon and oxygen capacity',
    'Characterize effluent|Apply ozone|Form biodegradable oxidation products|Transfer to biofilter|Supply oxygen|Remove carbon and biomass|Verify reuse quality',[(3,5),(6,2),(4,7)],
    [('CONSERVATION','1-7','Carbon appears in residual dissolved species, biomass, CO2 or removed solids; UV absorbance loss is not destruction.'),('CONSTITUTIVE','4-6','Reaction and adsorption kinetics depend on substrate identity; oxygen/DOC ratio is not universal.'),('ENGINEERING','2,7','Disinfection/micropollutant/byproduct limits and biological stability remain unchanged.')],
    'For a specified carbohydrate surrogate CH2O+O2->CO2+H2O, complete oxidation needs32/12 kgO2/kgC; this is not a universal NOM invariant. Ozone energy avoided=Q*deltaDose*eO3.',20000000,.001,2,15000,200000,'m3/year; kg O3/m3 avoided TARGET; USD/kg marginal ozone generation and oxygen cost',
    'ASSUMED reduce ozone1mg/L=0.001kg/m3;20000kg/year avoided. Carbon-to-oxygen bound applies only to the stated surrogate. Reduced dose must independently retain contaminant and byproduct outcomes; scenario net is negative.',
    ['Same UV reduction can leave different biodegradable carbon and biofilter demand.','Maximal oxidation before biofiltration need not be necessary when the biological step meets the same final specification.','BDOC/oxygen/target-contaminant measurements must change dose jointly; extra assay alone earns no value.'],
    'Existing ozonation-biofiltration experiments and multispecies biofilm/adsorption models already retain this handoff; compare optimized dose and contact time.','REJECTED',
    ['https://dwes.copernicus.org/preprints/3/107/2010/dwesd-3-107-2010.pdf','https://pubmed.ncbi.nlm.nih.gov/38141435/'],
    'Primary2010 discussion paper full text inspected; it reports nonuniversal DOC/oxygen relations and multiple competing processes.2024 biofilter study abstract retrieved; full page unrendered. Neither provides our savings.',
    'Any loss of required oxidation or water stability invalidates dose reduction. Adsorption inventory depletion cannot be counted as repeated biological removal.')
    add(13,'VOC adsorber regeneration fractions routed before wet and dry solvent mix',
    'Adsorb VOC mixture|Isolate loaded bed|Desorb early wet fraction|Change regeneration conditions|Desorb solvent-rich fraction|Condense separate receivers|Qualify recycle solvent|Regenerate bed to reference state',[(3,6),(5,6),(7,1),(8,1)],
    [('CONSERVATION','1-8','Each VOC and water balance includes residual bed loading and vent capture.'),('CONSTITUTIVE','3-5','Competitive adsorption and desorption rates determine fraction purity; volatility alone is insufficient.'),('ENGINEERING','6-8','Recycled solvent specification, stack emissions and restored adsorption capacity remain identical.')],
    'm_qualified=sum_j m_j*1[all species limits satisfied]; separate fractions cannot exceed total condensed solvent. Avoided purification cost=q*delta_m*price.',1000,500,.6,50000,800000,'regenerations/year; kg solvent directly reused instead of repurified/regeneration TARGET; USD/kg net purification cost',
    'ASSUMED percycle1000kg wet fraction with10%water and2000kg rich fraction with0.1%water: mixing gives3.4%water; rich fraction alone meets0.5%limit. Economic target500kg additional direct reuse, without solvent-sales double credit.',
    ['Equal total solvent recovery masks when water and different VOC species emerged.','All regeneration condensate need not enter one purification tank.','Fraction assays create value only if routing avoids real purification duty while bed capacity and emissions are unchanged.'],
    'US5958109A explicitly stages water removal before solvent recovery. Compare multicomponent staged desorption/condensation with individual qualified receivers.','KNOWN',
    ['https://patents.google.com/patent/US5958109A/en','https://patents.google.com/patent/EP0453588A1/en'],
    'First full text inspected: two heating steps and water removal before recovered solvent. Second search record describes fraction separation. Narrow composition scheduling remains unverified, not novel by absence.',
    'Azeotropy, desorption overlap, extra regeneration heat or residual bed loading can remove benefit; reject any inventory depletion masquerading as recurring recovery.')
    add(14,'Hydrogen PSA equalization stops on impurity inventory as well as pressure',
    'Adsorb feed impurities|Deliver hydrogen|Start bed equalization|Track impurity front and transfer line|Stop transfer before breakthrough|Regenerate donor bed|Repressurize receiving bed|Verify next-cycle product',[(4,8),(5,7),(6,1),(8,1)],
    [('CONSERVATION','1-8','Hydrogen and each impurity close over the full periodic cycle including tailgas and adsorbate inventory.'),('CONSTITUTIVE','1,4','Competitive isotherms, temperature and mass-transfer fronts require identified parameters.'),('ENGINEERING','3-8','Equalization pressure is not sufficient to guarantee next-cycle CO or other impurity specification.')],
    'n_transfer approximately deltaP*V/(R*T), ideal gas with Pa,m3,J/(mol K),K. Impurity introduced=integral y_i*dn. Extra accepted H2=feed_H2*(recovery_new-recovery_old).',30000000,.005,1.5,40000,500000,'kg feed hydrogen/year; absolute recovery fraction gain TARGET; USD/kg net hydrogen value after foregone tailgas fuel credit',
    'ASSUMED0.5percentage-point recovery improvement creates150000kg/year additional accepted hydrogen. Equal transferred moles with different impurity fractions are not equivalent for next cycle. No extra credit for the same hydrogen as fuel.',
    ['Equal bed pressure hides impurity in lines and receiver adsorbent.','Equalization to a fixed pressure endpoint is not always necessary for highest qualified recovery.','Predictive impurity measurement must outperform conventional front tracking and cover sensor/control cost.'],
    'Predictive methane/CO sensing and purity-aware PSA control already patented; compare modern validated cyclic adsorption optimization. Broad mechanism known; a fitted optimizer tie alone would not prove historical prior art.','KNOWN',
    ['https://patents.google.com/patent/US20140352531A1/en','https://patents.google.com/patent/US4693730A/en'],
    'First full text inspected: earlier impurity feedback used to increase recovery without exceeding CO limit. Second targeted search record covers purity control.',
    'If next-cycle trace-impurity peak rises or tailgas replacement fuel consumes the added value, the0.5point target fails; residual adsorbate cannot be borrowed across cycles.')
    add(15,'Vacuum distillation condenser and noncondensable removal jointly controlled',
    'Boil feed under vacuum|Condense overhead|Accumulate noncondensables|Measure partial-pressure state|Adjust coolant and gas removal|Collect qualified distillate|Track solvent entrainment',[(3,1),(5,2),(7,5),(2,4)],
    [('CONSERVATION','1-7','Vapor species balances include noncondensables, product condensate and vent entrainment.'),('CONSTITUTIVE','2-4','Total pressure equals vapor saturation contribution plus noncondensable partial pressure only under stated local equilibrium.'),('ENGINEERING','1,5','Boiling temperature, pressure stability and condenser duty limits are retained.')],
    'Ptotal=Pcond(T,x)+nNC*R*T/V; ideal-gas NC inventory. Psat(T) replaces Pcond only for a pure condensable or fixed-composition surrogate. Avoided steam=q_hours*delta_msteam*price; additional coolant/vacuum electricity included in OPEX.',8000,300,.03,15000,400000,'operating h/year; kg motive steam/h reduction TARGET; USD/kg marginal steam cost',
    'ASSUMED300kg/h motive-steam reduction gives2.4millionkg/year. At fixedT, increasing noncondensable inventory raises pressure without increasing useful condensing duty. This scenario does not cover annualized implementation cost.',
    ['Equal total pressure can arise from different condensible/noncondensable mixtures, requiring different actions.','Continuous full ejector steam is not universally necessary if gas removal and condensation remain adequate.','Partial-pressure diagnostics help only if they change utility dispatch without product or vacuum losses.'],
    'US20110240525A1 already coordinates condensation pressure and discontinuous noncondensable evacuation; compare modern vacuum system design/control and leak repair.','REJECTED',
    ['https://patents.google.com/patent/US20110240525A1/en'],
    'Full patent inspected, including continuous versus discontinuous ejector operation. Assumed steam reduction is not taken from its example.',
    'Air leakage repair may dominate; extra cooling energy, entrained solvent loss or vacuum excursions invalidate the reduction.')
    add(16,'Amine reclaimer endpoint closes amine and heat-stable-salt balances',
    'Absorb acid gas|Strip reusable amine|Send contaminated slipstream to reclaimer|Control steam and water|Recover amine vapor|Purge nonvolatile residue|Return qualified amine',[(7,1),(4,5),(6,3)],
    [('CONSERVATION','1-7','Amine and each heat-stable salt balance includes thermal degradation and waste; high recovery cannot eliminate nonvolatile residue.'),('CONSTITUTIVE','3-5','Volatility and degradation kinetics depend on temperature, water and composition.'),('ENGINEERING','4-7','Minimum liquid level, thermal limit, returned solvent quality and gas treatment performance hold.')],
    'At steady state residue purge P>=G_HSS/x_HSS,max where G kg/year,x mass fraction; recovered amine=purge_feed*delta_recovery after correcting new degradation.',500000,.2,2,50000,500000,'kg reclaimer feed/year; extra recovered amine kg/kg feed TARGET; USD/kg net usable amine value',
    'ASSUMED heat-stable-salt formation10000kg/year and permitted residue fraction0.20 require50000kg/year residue purge.20percentage-point additional amine recovery is a test target; no avoided purge credit.',
    ['Equal reclaimer level or temperature does not reveal amine versus salt inventory.','Fixed steam input and fixed-duration endpoint are not necessary when coupled level/composition control meets recovery.','Amine/salt measurements must improve net recovery beyond existing coordinated control.'],
    'US11819777B2 already couples variable steam with water/amine inputs to reduce degradation and increase recovery; compare modern thermal and membrane/ion-exchange reclaiming as applicable.','KNOWN',
    ['https://patents.google.com/patent/US11819777B2/en','https://patents.google.com/patent/US9994512B2/en'],
    'First full text inspected, including residue disposal after each cycle and joint controller. Second primary search record describes recovery endpoint and water/steam use.',
    'Any increased degradation, gas-treatment shortfall or hidden salt accumulation cancels recovery credit. Trial ends at matched periodic solvent composition.')
    add(17,'Recover entrained loaded solvent from raffinate before returning water',
    'Contact leach liquor and organic|Settle bulk phases|Measure raffinate droplets|Coalesce residual organic|Return recovered organic to extraction|Send raffinate to leach|Strip and account recovered metal',[(4,5),(5,1),(6,1),(5,7)],
    [('CONSERVATION','1-7','Organic solvent and metal partition close through raffinate, recovered droplets and stripping; recovered metal cannot be credited twice.'),('CONSTITUTIVE','3-4','Stokes settling v=delta_rho*g*d^2/(18*mu) only for isolated small droplets with low Reynolds number.'),('ENGINEERING','5-7','Recovered phase purity and downstream extraction chemistry must remain qualified.')],
    'm_saved=Q*deltaC where Q m3/year and deltaC kg/m3; Stokes droplet speed scales d^2 under stated conditions. Price includes net replacement benefit only.',50000000,.01,3,300000,3000000,'m3 raffinate/year; kg organic loss/m3 additionally avoided TARGET; USD/kg net solvent replacement value',
    'ASSUMED entrainment reduction10mg/L=0.01kg/m3 yields500000kg/year solvent. Increasing droplet diameter20to80micrometres gives16x Stokes speed, conditional on dilute isolated drops; not a prediction of separator recovery.',
    ['Equal raffinate dissolved-metal assay hides organic droplets carrying solvent and metal.','All entrained organic need not be replaced as fresh solvent if qualified coalescence returns it.','Droplet monitoring is useful only if it improves recovered solvent beyond existing separator operation.'],
    'US6350354B1 already explicitly includes raffinate and loaded-organic coalescers. Compare sized/coalescer-optimized solvent extraction, not deliberately omitted equipment.','KNOWN',
    ['https://patents.google.com/patent/US6350354B1/en'],
    'Full text inspected: separate raffinate/loaded-organic coalescence and return paths. No demonstrated10mg/L incremental gain over modern equipment.',
    'Surfactant-stabilized emulsions, contaminated recovered organic or higher shear may prevent recovery. Do not add recovered-metal sales if included in solvent marginal value.')
    add(18,'Filter wash solvent selected against both product dissolution and impurity precipitation',
    'Crystallize product|Drain mother liquor|Map wash-mixture solubilities|Apply staged wash|Remove displaced liquor|Dry crystal cake|Verify purity and particle form',[(3,4),(4,7),(5,3)],
    [('CONSERVATION','1-7','Product and impurity masses include dissolution, reprecipitation, wash effluent and final cake.'),('CONSTITUTIVE','3-4','Solubility surfaces and nucleation delay depend on temperature and mixed-solvent composition.'),('ENGINEERING','6-7','Same impurity limit, polymorph and particle specifications are retained; apparent yield from impurity precipitation is rejected.')],
    'Potential product dissolution <=Vwash*max(0,S_product-C_product,in); impurity precipitation=max(0,mI_liquid-Vliquid*S_I,mix). S kg/m3,V m3.',1000,20,10,30000,200000,'batches/year; kg additionally accepted product/batch TARGET; USD/kg marginal value after wash/recovery costs',
    'ASSUMED2m3 wash, original solubility15kg/m3 and selected5kg/m3 lower dissolution upper bound30to10kg, difference20kg. Impurity precipitation constraint can invalidate this apparent saving; all values hypothetical.',
    ['Equal wash volume or residual mother-liquor ratio does not preserve dissolved product and precipitated impurity.','An extremely poor product solvent is not necessarily a suitable wash solvent.','Binary-solvent assays matter if they change mixture choice and accepted yield after impurity testing.'],
    '2021 primary work explicitly maps anti-solvent precipitation versus dissolution during API washing. Distinct from N002 diffusion and N003 bypass, but benefits cannot be added for the same loss.','KNOWN',
    ['https://strathprints.strath.ac.uk/75622/'],
    'Author-institution full abstract inspected, including wash-composition boundaries and product/impurity precipitation. The20kg financial target is ours, not a reported result.',
    'If impurity precipitation, polymorph conversion, agglomeration or saturated wash preparation consumes the saved product, accepted-yield benefit is zero or negative.')
    add(19,'Nitrite-bearing sidestream return matched to mainstream nitrogen capacity',
    'Treat concentrated centrate|Partially oxidize ammonium|Measure ammonium and nitrite|Meter sidestream to mainstream|Carry out anammox and polishing|Measure nitrogen gas and residual species|Return biomass and close cycle',[(3,4),(6,1),(7,5),(2,5)],
    [('CONSERVATION','1-7','Total nitrogen includes ammonia, nitrite, nitrate, N2, N2O and biomass; disappearance from water is not automatically benign N2.'),('CONSTITUTIVE','5','Illustrative anammox demand1.32kg nitrite-N/kg ammonium-N is an empirical stoichiometric approximation, not universal invariant.'),('ENGINEERING','4-6','Same effluent total nitrogen, nitrite toxicity and emissions constraints; temperature and biomass activity remain valid.')],
    'N_NH4_used <=min(NH4_available,NO2_available/1.32,active_capacity); kgN/time throughout. External carbon avoided=q_N*delta_COD, all rates measured at same removal.',500000,.4,.8,50000,500000,'kg nitrogen treated/year; kg external COD/kgN additionally avoided TARGET; USD/kg marginal purchased COD',
    'ASSUMED100kgNH4-N/day plus66kgNO2-N/day can support at most50kgNH4-N/day under1.32ratio before activity limit. Economic target0.4kg externalCOD/kgN is unmeasured; no simultaneous electric-saving credit.',
    ['Equal total nitrogen loading masks ammonium/nitrite ratio and biologically available capacity.','Separate full treatment of every centrate stream is not universally necessary if integrated treatment meets all outputs.','Speciated nitrogen and activity assays create value only if return timing changes needed carbon beyond established integrated control.'],
    'TUM Sidestream Enhanced Mainstream Anammox process and2022 primary publication already integrate sidestream nitrite with mainstream treatment; compare seasonal biological models and validated equalization control.','KNOWN',
    ['https://www.cee.ed.tum.de/en/sww/research/finished-projects/energy-efficient-anammox/','https://pubs.acs.org/doi/10.1021/acs.est.2c03256'],
    'Author project page inspected with mass-balance integration; ACS abstract/search retrieved, full retrieval403. Do not transfer their assumed feasibility to this site.',
    'N2O increase, low-temperature loss of activity, nitrite breakthrough or carbon shifted to downstream polishing invalidates the0.4target.')
    add(20,'Grow flocs after the last damaging pump before membrane filtration',
    'Measure raw water|Dose coagulant|Pass high-shear feed pump|Provide controlled floc-growth residence|Filter through ceramic membrane|Backwash or purge solids|Measure permeate and recovered cycle',[(3,4),(6,2),(7,1)],
    [('CONSERVATION','1-7','Solids and coagulant leave as sludge or permitted residual; larger flocs do not destroy contaminant mass.'),('CONSTITUTIVE','3-5','Breakage/aggregation kinetics and cake resistance require calibration; floc size alone does not determine permeability.'),('ENGINEERING','4-7','Same flux, rejection, pressure limit and membrane life; residence volume and pumping head counted.')],
    'Darcy J=deltaP/[mu*(Rm+Rc)]; floc-conditioning benefit requires measured smaller Rc at equal rejected solids. Chemical saving=q_water*delta_dose, dose kg/m3.',5000000,.01,.5,5000,100000,'m3 water/year; kg coagulant/m3 additionally avoided TARGET; USD/kg coagulant',
    'ASSUMED reducing coagulant by10mg/L=0.01kg/m3 saves50000kg/year if filtration quality remains equal. Pump relocation alone does not predict that result; zero change in cake resistance/quality is a null.',
    ['Equal tank floc size does not guarantee equal floc state after transport through a pump.','Raising chemical dose before damaging shear is not always necessary; growth after shear may suffice.','Post-pump particle and resistance measurements must justify lower dose beyond optimized existing design.'],
    'EP2687487B1 explicitly grows flocs downstream of the pump to preserve membrane performance without more coagulant; compare modern coagulation/membrane recirculation design.','KNOWN',
    ['https://patents.google.com/patent/EP2687487B1/en','https://www.mdpi.com/2077-0375/15/8/225'],
    'Patent full text inspected with downstream growth and recirculation.2025 research abstract retrieved; fullpaper retrieval blocked. Broad intervention directly anticipated.',
    'Smaller, denser flocs can sometimes foul less; if lower dose worsens permeate or increases membrane cleaning/replacement, net saving fails.')
    # Graph edges are physical chronological/transfer dependencies, not additions to GSL relations.
    for c in CASES:
        c['edges']=list(dict.fromkeys(c['edges']))
        c['prior_art_class']='KNOWN' if c['status']=='REJECTED' else c['status']
        c['equation_contract']={'units':'Stated in each equation and inputs; monetary values USD/year unless explicitly capital USD.','domain':'Only the declared process, assumptions and equal accepted-service constraints. Empirical coefficients are scenario assumptions.','limiting_case':'Zero physically achieved improvement gives negative implementation cost; no conservation law creates economic gain.','falsifier':c['falsifier']}
        c['mapping']={'objects':['TIME','SPACE','THING','EVENT','ACTION','RULE','VALUE','CONTEXT','CLAIM'],'agency':'Only plant operator/controller implementation; no physical matter is assigned authority.','forms':['CONSTRUCT','CONTRACT','STATE','RELATION','PROCESS','RULE','PROJECTION'],'relations':'CLAIM derivedFrom source/equation; RULE governs operating contract; measurement supports CLAIM; dependencies are owner-qualified. Complete SAL type/signature certification remains UNKNOWN.','facets':'IdentityLifecycle, ScopeContext, EpistemicsProvenance, EffectsSafety, DependencyValidity, ResourceTermination, AuditExplanation, RecoveryEvolution apply; AuthorityHumanBoundary applies to any future deployment; PrivacyRetention only to future sensitive plant data.'}

    def deep_tests():
        """Actual bounded numerical/null tests, not a blinded discovery benchmark."""
        checks=0
        def check(ok):
            nonlocal checks
            assert ok
            checks+=1
        def edr(buffer=200,c0=3000,cb=100,divert=0,dt=.002):
            Q,V,ci,T=20.,40.,100.,10.
            c=c0; tank_mass=buffer*cb; tank_volume=buffer
            rejected=0.; out_mass=0.
            steps=round(T/dt)
            for j in range(steps):
                f=math.exp(-Q*dt/V)
                mass=ci*Q*dt+(c-ci)*V*(1-f)
                c=ci+(c-ci)*f
                out_mass+=mass
                if j*dt < divert-1e-9:
                    rejected+=Q*dt
                else:
                    tank_mass+=mass; tank_volume+=Q*dt
            tank_mass+=rejected*ci; tank_volume+=rejected
            balance_error=V*c0+Q*T*ci-V*c-out_mass
            return dict(final_concentration=tank_mass/tank_volume,volume=tank_volume,rejected_m3=rejected,stack_final_concentration=c,balance_error_g=balance_error)
        candidate=edr(); timer=edr(divert=5)
        # Comparator uses ordinary, independently specified batch-inventory feasibility.
        Q,V,T,ci,c0=20.,40.,10.,100.,3000.
        mex=V*(c0-ci)*(1-math.exp(-Q*T/V))
        classic_inventory=(200*100+Q*T*ci+mex)/(200+Q*T)
        check(abs(candidate['final_concentration']-classic_inventory)<1e-7)
        check(candidate['final_concentration']<500 and timer['final_concentration']<500)
        check(abs(candidate['volume']-timer['volume'])<1e-7)
        check(abs(candidate['stack_final_concentration']-timer['stack_final_concentration'])<1e-8)
        check(abs(candidate['balance_error_g'])<1e-6)
        check(abs(timer['rejected_m3']-100)<1e-7)
        low_buffer=edr(buffer=50)
        check(low_buffer['final_concentration']>500)
        null=edr(c0=100)
        check(abs(null['final_concentration']-100)<1e-7)
        robust=edr(c0=3500,cb=150)
        check(robust['final_concentration']<500)
        concentration_endpoint_time=V/Q*math.log((c0-ci)/(500-ci))
        check(0<concentration_endpoint_time<5)
        def alk(ct,tn,pH):
            h=10**(-pH); k1=10**-6.35;k2=10**-10.33
            den=h*h+k1*h+k1*k2
            a1=k1*h/den; a2=k1*k2/den
            fn=1/(1+10**(9.25-pH))
            return ct*(a1+2*a2)+tn*fn+1e-14/h-h
        def demand(ct,tn=.04,a0=.04,pH=10):
            return 40*max(0,alk(ct,tn,pH)-a0)
        old,new=demand(.06),demand(.02)
        check(old>new>0)
        check(abs((old-new)-40*(alk(.06,.04,10)-alk(.02,.04,10)))<1e-10)
        check(abs(demand(.06)-demand(.06))<1e-12)
        # Strong conventional equilibrium titration predicts exactly the same signed/base-clipped result.
        conventional_delta=40*(max(0,alk(.06,.04,10)-.04)-max(0,alk(.02,.04,10)-.04))
        check(abs(conventional_delta-(old-new))<1e-10)
        high_alk_saved=demand(.06,a0=.15)-demand(.02,a0=.15)
        check(high_alk_saved==0)
        # Co-stripped NH3 lowers TAN AND total alkalinity by its molar transfer.
        tn_after=.035; a_after=.035
        co_strip_demand=demand(.02,tn=tn_after,a0=a_after)
        check(co_strip_demand>new)
        def solve_pH(ct,tn,targetA):
            lo,hi=2.,14.
            for _ in range(100):
                mid=(lo+hi)/2
                if alk(ct,tn,mid)<targetA:lo=mid
                else:hi=mid
            return (lo+hi)/2
        pH0=solve_pH(.06,.04,.04);pH1=solve_pH(.02,.04,.04)
        check(pH1>pH0)
        check(abs(alk(.02,.04,pH1)-.04)<1e-12)
        for c in CASES:
            check(len(c['nodes'])>=5 and len(c['nodes'])<=9)
            check(len(c['edges'])==len(set(c['edges'])))
            check(all(1<=a<=len(c['nodes']) and 1<=b<=len(c['nodes']) for a,b in c['edges']))
            f=c['financial'];i=c['inputs']
            check(abs(f['gross']-i['annual_activity']*i['improvement']*i['unit_value_usd'])<1e-7)
            check(abs(f['net']-(f['gross']-f['opex']-CRF*f['capex']))<1e-7)
        return dict(checks=checks,N006={'candidate':candidate,'timer_baseline':timer,'modern_inventory_concentration':classic_inventory,'modern_conductivity_divert_minutes':concentration_endpoint_time,'low_buffer_rejected':low_buffer,'null':null,'bounded_uncertainty':robust,'finding':'Numerical mass balance and final batch quality verified under toy assumptions; classical inventory-aware control ties. Published endpoint control is known; exact deployment advantage remains unmeasured.'},N010={'old_NaOH_kg_m3':old,'after_CO2_NaOH_kg_m3':new,'ideal_avoided_kg_m3':old-new,'high_initial_alkalinity_null_saved':high_alk_saved,'co_stripped_NH3_corrected_demand':co_strip_demand,'initial_pH':pH0,'CO2_only_pH':pH1,'finding':'Common initial alkalinity and TAN retained. CO2 removal raises pH without consuming alkalinity; co-stripped NH3 requires a separate nitrogen/alkalinity exit. Conventional equilibrium titration gives same result; equipment performance not simulated.'})

    return run(), deep_tests()



# Source SHA256: b13e1f6558235be467ced342eb42e48fba5d596111ce0d8a4b512a9aacc1244a
def workstream_materials():
    """Twenty noncanonical materials interface screens; standard-library replay.
    All numerical parameters are assumptions, except arithmetic and quoted stoichiometry.
    Search-informed models, not blind discovery. No field saving or frontier novelty established.
    Source: actual Garden v15.10/GCSC/TREE_CORE; bounded manual adapter only.
    """
    import math

    CRF = .08 * 1.08**10 / (1.08**10 - 1)

    def financial(quantity, improvement, value, opex, capex, unit, note=''):
        gross = quantity * improvement * value
        return dict(gross=gross, opex=opex, capex=capex, annualized_capex=CRF*capex,
                    net=gross-opex-CRF*capex,
                    break_even=(opex+CRF*capex)/(quantity*value),
                    break_even_unit=unit, quantity_per_year=quantity,
                    assumed_improvement=improvement, assumed_unit_value=value,
                    assumption_note=note, modern_baseline_increment=None)

    def cake_cost(p, response=True):
        """USD/t dry cake; P in bar. Synthetic response, not fitted plant model."""
        w=.12+.08*math.exp(-(p-1)/2) if response else .20
        e=4+.3*(p-1)**2
        return .10*e+1000*(w-.08)*2.5/.75*.01

    def deep_tests():
        # Analytic derivative root, bounded to the frozen physical interval.
        lo,hi=1.,9.
        for _ in range(80):
            p=(lo+hi)/2
            d=.06*(p-1)-(4/3)*math.exp(-(p-1)/2)
            if d>0: hi=p
            else: lo=p
        optimum=(lo+hi)/2
        # Independent exhaustive numerical optimizer, same information/actions.
        grid=min((1+i*.0001 for i in range(80001)), key=cake_cost)
        assert abs(optimum-grid)<.0001
        assert abs(cake_cost(optimum)-cake_cost(grid))<1e-8
        assert min((1+i*.01 for i in range(801)),key=lambda p:cake_cost(p,False))==1
        assert cake_cost(optimum)<cake_cost(3)
        # CaO + CO2 -> CaCO3. Other Ca phases can absorb the remaining CO2.
        residual=[10-a*6*56/44 for a in [1,.2]]
        assert residual[0]<5<residual[1]
        assert all(0<=x<=10 for x in residual)
        assert abs((10-residual[0])*44/56-6)<1e-12
        assert abs((10-residual[1])*44/56-1.2)<1e-12
        assert 10-0*6*56/44==10
        # Null: if both alpha and initial fCaO are known, total uptake is sufficient.
        assert 10-1*6*56/44==residual[0]
        shell_unreacted=(1-1/5)**3
        assert abs(shell_unreacted-.512)<1e-12
        return dict(cake_pressure_bar=optimum, grid_pressure_bar=grid,
                    cake_cost_3bar=cake_cost(3), cake_cost_9bar=cake_cost(9),
                    cake_cost_optimum=cake_cost(optimum),
                    cake_saving_vs_3bar=cake_cost(3)-cake_cost(optimum),
                    cake_saving_vs_9bar=cake_cost(9)-cake_cost(optimum),
                    cake_modern_increment_before_extra_cost=0.,
                    slag_residual_free_CaO_kg_t=residual,
                    slag_same_total_CO2_kg_t=6.,
                    slag_unreacted_core_volume_fraction=shell_unreacted,
                    checks=11)

    def run():
        cases=[]
        # Manually scoped bindings: each row gives nodes for constraints1..4.
        bindings={
          21:[[1,2,3,4,5,6,7],[2,3,4],[1,2,3,4,5,6],[5,6,7]],
          22:[[1,2,3,4,5,6,7],[2,3,4,5,6],[2,3,5],[6,7]],
          23:[[1,2,3,4,5,6,7],[2,3,4,5],[2,3,5],[3,4,7]],
          24:[[4,5,6],[1,2,3,4,7],[1,3,4,5],[5,6]],
          25:[[1,2,3,4,5,7],[1,2,3,4],[2,3,5,6,7],[4,5,7]],
          26:[[1,2,3,4,5,6,7],[3,4,5,6],[2,3,4,5],[1,6,7]],
          27:[[1,2,3,4,5,6,7],[2,4,5,6],[1,2,3,6,7],[2,3,7]],
          28:[[1,2,3],[2,3,4,5,6,7],[2,3,4,5],[5,6,7]],
          29:[[3,4,5,6],[1,2,3,4,5],[2,3,4,5],[3,6,7]],
          30:[[1,2,3,4,5],[1,2,3,4,5],[2,4,5],[5,6,7]],
          31:[[1,2,3,4,5,6,7],[3,4,5],[4,5,6],[3,6,7]],
          32:[[2,3,4,5,6,7],[1,2,3,6,7],[1,2,3,4,5,6],[2,4,5,6,7]],
          33:[[1,3,4,5,6],[1,2,3,4,5],[2,3,4,5],[5,6,7]],
          34:[[1,2,3,4,5,6,7],[1,2,3,4,5],[3,4,5],[5,6,7]],
          35:[[1,2,3,4,5,6,7],[1,2,3,4,5],[3,5,6],[5,6,7]],
          36:[[1,2,3,4,5,6,7],[1,2,3,4,5],[4,5,6],[5,6,7]],
          37:[[1,2,3,4,5],[1,2,3,4,5,7],[1,2,3,5,6],[5,6,7]],
          38:[[1,2,3,4,5,7],[1,3,4,5,7],[2,3,4,5],[5,6,7]],
          39:[[1,2,3,4,5,6,7],[3,4,5,6],[3,4,5,6,7],[5,6,7]],
          40:[[1,2,3,4,5,6,7],[2,3,4,5,6],[1,3,4,5],[4,5,6,7]]}
        def add(i,title,nodes,cross,constraints,gap,operators,equation,inputs,prediction,
                fin,baseline,novelty,sources,support,falsifier,limits):
            n=nodes.split(' | ')
            edges=[(j,j+1) for j in range(1,len(n))]+cross
            assert 5<=len(n)<=9 and len(set(edges))==len(edges)
            assert all(1<=a<=len(n) and 1<=b<=len(n) for a,b in edges)
            c=dict(id=f'N{i:03d}',title=title,nodes=n,edges=edges,
                   cross_edges=cross,constraints=constraints,gap=gap,
                   operators=operators,equation=equation,inputs=inputs,
                   physical_prediction=prediction,financial=fin,baseline=baseline,
                   novelty=novelty,status='NONCANONICAL; CONDITIONAL SCREEN; FIELD UNKNOWN',
                   sources=sources,source_support=support,falsifier=falsifier,
                   limiting_case=limits)
            c['transfer_audit']=gap
            c['garden_binding']={'objects':['TIME','SPACE','THING','EVENT','ACTION','RULE','VALUE','CONTEXT','CLAIM'],
                 'agency':'Plant owner/operator only for any later consequential action; no agency assigned to matter.',
                 'relations':['partOf','dependsOn','causes','frames','references','derivedFrom','hasHypothesis','supports','contradicts'],
                 'relation_scope':'Chronological and transfer edges are domain fields. Core relation typing is a manual projection; unresolved SAL rules are UNKNOWN.',
                 'forms':['CONSTRUCT','CONTRACT','STATE','RELATION','PROCESS','RULE','PROJECTION']}
            c['constraint_bindings']=[{'constraint':j+1,'nodes':nn} for j,nn in enumerate(bindings[i])]
            assert all(any(node in b['nodes'] for b in c['constraint_bindings']) for node in range(1,len(n)+1))
            c['economic_screen']='POSITIVE_CONDITIONAL' if fin['net']>0 else 'NEGATIVE_CONDITIONAL'
            c['verification']={'arithmetic':'REPLAYED','prior_art':'SCOPED_CHECK','frontier_novelty':'NOT_ESTABLISHED','field':'UNKNOWN','measured_economic_value':'UNKNOWN'}
            cases.append(c)
        add(21,'Retain fines provenance when changing an ore-sorter cut',
            'Blast mineralized rock | Crush and classify by size | Assay bypass fines | Sensor-sort coarse particles | Merge accepted coarse and fines | Grind and recover metal | Reconcile saleable metal and rejects',
            [(2,5),(3,7),(4,7)],
            ['EXACT MASS: feed metal equals accepted, rejected and retained-inventory metal over a closed campaign.',
             'ENGINEERING: sub-sensor-size fines cannot inherit coarse-particle classification confidence.',
             'CONSTITUTIVE: reject grade and liberation depend on size/mineral texture; measured curves required.',
             'QUALITY: equal recovered payable metal or explicit lost-metal opportunity cost is required.'],
            'The coarse reject rate can improve while the untracked fines carry more metal. Retain size-by-grade lot identity through both paths; choose a cut on the whole-feed payable-metal balance, with a separate fines assay.',
            'Projection-Loss: same coarse sorter accuracy, different fines grade. Necessity-Challenge: do all fines require milling? Only assay-supported barren fractions can bypass. Decision-Sufficiency: assay only if changed routing exceeds acquisition and lost-metal costs.',
            'Gross before implementation = M*dr*(c_process-g_reject*v_metal); g_reject=.0001 tCu/t extra reject in this scenario. USD/y = t/y * fraction * USD/t. Total recovered-metal change includes both coarse and fines paths, never coarse recovery alone.',
            {'M_t_y':5e6,'extra_reject_fraction':.02,'process_USD_t':5,'lost_metal_t_per_feed_t':.000002,'metal_USD_t':6000},
            {'extra_reject_t_y':100000,'lost_metal_t_y':10},
            financial(5e6,.02,4.4,90000,1e6,'additional rejected feed fraction','5 USD/t process saving less0.6 USD/t lost-Cu margin gives4.4 USD/t extra reject. Metal penalty scales with reject mass in the break-even calculation. No throughput-revenue credit.'),
            'Modern geometallurgical size-by-grade balance, sensor sortability curves and sensor-fusion ore sorting. Conventional optimizer can use identical fines assays.','KNOWN',
            ['https://pmc.ncbi.nlm.nih.gov/articles/PMC12788257/','https://www.mdpi.com/2075-163X/12/5/630'],
            'Primary studies already assess grade/recovery and particle sortability; neither supports this assumed 2% extra reject target.',
            'Reject if a held-out campaign loses more payable metal than budgeted, or a conventional size-resolved optimizer matches the outcome.',
            'Zero added rejection gives zero gross benefit; completely liberated uniform-grade ore removes the proposed projection distinction.')
        add(22,'Carry recycled-water redox into sulfide flotation conditioning',
            'Collect tailings water | Aerate or hold recycled water | Mix water with fresh ore | Grind exposed sulfide surfaces | Dose collector and frother | Float concentrate | Recycle water and audit metal recovery',
            [(2,5),(3,6),(6,1)],
            ['EXACT ELEMENT BALANCE: Cu and S leave in concentrate, tailings or inventory, not by redox bookkeeping.',
             'CONSTITUTIVE: oxidation-reduction potential, dissolved oxygen and ion concentrations affect surface species within mineral-specific domains.',
             'ENGINEERING: Eh cannot be inferred from conductivity alone.',
             'QUALITY: recovery comparison must hold concentrate grade and contaminant penalties fixed.'],
            'Conductivity/pH summaries can erase oxidation state between the pond and collector dosing. Test a lot-specific redox/DO carryover measurement and preconditioning schedule before adding extra collector.',
            'Projection-Loss: equal salinity/pH can differ in Eh and surface adsorption. Necessity-Challenge: challenge extra-collector prerequisite using water conditioning. Decision-Sufficiency: measure Eh only when the route or dose changes expected net recovery.',
            'Extra payable Cu = M*g*dR (t/y); gross=M*g*dR*v. Scenario is a required target, not a flotation kinetic prediction.',
            {'ore_t_y':5e6,'Cu_grade':.005,'recovery_gain':.0025,'net_Cu_USD_t':6000},
            {'required_additional_Cu_t_y':62.5},
            financial(25000,.0025,6000,120000,500000,'absolute metal recovery fraction','No gain is credited for poorer concentrate grade or greater reagent discharge.'),
            'Electrochemical flotation modelling with water chemistry, Eh/DO control and bench mineral tests; same information and reagent budget.','KNOWN',
            ['https://open.uct.ac.za/items/be309311-d2ef-428e-9a85-29c0dce203f4','https://www.sciencedirect.com/science/article/pii/S0892687512002671'],
            'Primary work directly studies recycled-water chemistry and flotation response; assumed recovery gain is not sourced.',
            'Reject if grade-matched randomised runs show no positive recovery increment over current Eh-aware practice.',
            'If ore surfaces and water reach the same equilibrium before flotation, extra inlet Eh information may have no decision value.')
        add(23,'Limit heap irrigation using precipitation-dependent permeability',
            'Crush and agglomerate ore | Stack lift under self-weight | Irrigate reactive leach solution | Precipitate or dissolve pore minerals | Drain pregnant solution | Recover copper | Return liquor with changed chemistry',
            [(2,5),(4,3),(7,3)],
            ['EXACT BALANCE: solute and water accumulation must be included over the full leach cycle.',
             'CONSTITUTIVE: Darcy flux q = k*dp/(mu*L) for a saturated approximation; unsaturated heaps need retention relations.',
             'ENGINEERING: ponding, slope and liner limits bound irrigation regardless of nominal recovery gain.',
             'CHEMICAL: precipitation changes pore space and solution speciation; equal inflow does not imply equal contact.'],
            'A fixed irrigation rate may ignore declining pore permeability caused by recycled-liquor chemistry. Test chemistry-triggered irrigation/rest scheduling using both drainage balance and mineral saturation, rather than adding flow.',
            'Projection-Loss: identical surface flux with different pore-blockage histories. Necessity-Challenge: continuous full-rate irrigation may not be necessary for equal copper recovery. Decision-Sufficiency: monitoring is useful only if additional metal exceeds slower-cycle and treatment costs.',
            'Q2/Q1=k2/k1 at fixed gradient, viscosity and geometry. Copper benefit=M*g*dR*v. Saturated reduction is a local diagnostic, not a complete heap model.',
            {'permeability_ratio':.6,'ore_t_y':2e6,'Cu_grade':.005,'recovery_gain':.003,'Cu_USD_t':6000},
            {'fixed_gradient_flow_ratio':.6,'required_additional_Cu_t_y':30},
            financial(10000,.003,6000,80000,800000,'absolute copper recovery fraction','Time to recovery and retained copper inventory must be matched; assumed costs make this screen negative.'),
            'Reactive unsaturated dual-phase heap models, tracer tests and irrigation scheduling already preserve permeability and chemistry.','KNOWN',
            ['https://www.sciencedirect.com/science/article/pii/S0304386X2200175X','https://pmc.ncbi.nlm.nih.gov/articles/PMC9491881/'],
            'Primary studies treat heap hydraulic properties and permeability evolution; no new chemical-hydraulic law claimed.',
            'Reject if reduced irrigation only delays recovery, causes ponding, or fails against a calibrated reactive-transport controller.',
            'With stable permeability and no precipitation, extra chemistry-based scheduling can add cost without physical benefit.')
        add(24,'Count thickener polymer carryover in electrowinning additive control',
            'Dose flocculant to slurry | Settle solids | Clarify copper liquor | Transfer organic species to electrolyte | Plate copper at controlled current | Strip and grade cathodes | Purge or return electrolyte',
            [(1,4),(3,5),(7,4)],
            ['EXACT CHARGE: m_Cu=eta*I*t*M_Cu/(2F), with current efficiency eta measured.',
             'SPECIES BALANCE: upstream polymer and intentionally dosed smoothing agent both enter the electrolyte inventory.',
             'CONSTITUTIVE: molecular weight, charge and degradation alter adsorption; total organic carbon alone is not a universal predictor.',
             'QUALITY: cathode roughness, impurities and cell shorting must be held to the same specification.'],
            'Additive dosing can count only the intentional tank dose while ignoring carried-over polymer. Test a joint upstream-polymer/cell-response balance to reduce over-dosing or energy loss; do not assume every flocculant is harmful.',
            'Projection-Loss: equal TOC can contain polymers with different adsorption. Necessity-Challenge: a fixed downstream dose may be unnecessary when beneficial upstream polymer survives. Decision-Sufficiency: use cell-response sensing only if it changes a dose or purge decision.',
            'Energy saving=M_Cu*de (kWh/y); gross=M_Cu*de*p_e. At fixed current, eta change must be accounted separately from cell-voltage change.',
            {'Cu_t_y':100000,'target_kWh_per_t_reduction':15,'electricity_USD_kWh':.1},
            {'required_energy_reduction_kWh_y':1500000},
            financial(100000,15,.1,25000,400000,'kWh/t copper','No separate cathode-yield credit;15 kWh/t reduction is unmeasured.'),
            'Published polymer molecular-property/electrodeposition models and existing EW additive optimisation.','KNOWN',
            ['https://www.sciencedirect.com/science/article/pii/S0304386X06002052','https://doi.org/10.1016/j.hydromet.2020.105407'],
            'Primary research explicitly describes upstream PAM plus intentional smoothing additives and molecular-weight effects.',
            'Reject if removing carryover worsens deposits, or a current-efficiency and morphology matched comparator has equal net cost.',
            'At zero polymer carryover the upstream handoff adds no downstream information.')
        d=deep_tests()
        add(25,'Stop cake dewatering where downstream drying makes further pressure uneconomic',
            'Characterise slurry pore water | Filter cake at pressure P | Displace capillary water | Discharge cake with retained moisture | Thermally dry to target | Meter electricity and fuel | Match final dry mass and moisture',
            [(1,3),(3,5),(2,6),(4,7)],
            ['EXACT WATER BALANCE: removed liquid plus evaporated water plus terminal water equals initial water.',
             'CONSTITUTIVE: capillary entry pressure scales as2*gamma*cos(theta)/r for ideal pores; compressible cakes need measured curves.',
             'ENERGY: dryer duty includes latent heat, sensible heat and losses; the toy curve isolates a fixed latent term.',
             'ENGINEERING: cake handling and final moisture limits may exclude the unconstrained monetary optimum.'],
            'A filtration target expressed only as maximum dryness can overspend electricity, while minimum filter power can transfer excessive duty to the dryer. Optimise the shared pressure-to-moisture-to-drying contract at equal final product.',
            'Projection-Loss: equal dry solids throughput loses retained water and marginal press work. Necessity-Challenge: maximum cake dryness is not necessary for minimum total cost. Decision-Sufficiency: buy moisture information only if it changes the joint optimum.',
            'w(P)=.12+.08exp[-(P-1)/2] kg/kg dry; E(P)=4+.3(P-1)^2 kWh/t dry. C=.1E+1000(w-.08)*2.5/.75*.01 USD/t. P in[1,9]bar; derivative .06(P-1)-(4/3)exp[-(P-1)/2]=0.',
            {'dry_t_y':200000,'baseline_bar':3,'final_moisture_kg_kg':.08,'all_response_coefficients':'SYNTHETIC, not measured'},
            {'optimum_bar':d['cake_pressure_bar'],'USD_per_t_gain_vs_3bar':d['cake_saving_vs_3bar'],'modern_optimizer_difference_USD_t':0},
            financial(200000,d['cake_saving_vs_3bar'],1,50000,500000,'USD/t net operating saving','Baseline3bar is reported;9bar gives a larger weak-baseline gain. Modern joint optimizer ties exactly before added costs.'),
            'Conventional joint dewatering/drying optimisation with the same calibrated cake and dryer maps; independent grid optimizer implemented.','KNOWN',
            ['https://cris.vtt.fi/en/publications/specific-energy-consumption-of-cake-dewatering-with-vacuum-filter/','https://patents.google.com/patent/AU633505B2/en'],
            'Primary work and patent already join cake dryness, energy and downstream drying. Our exponential and quadratic curves are independent synthetic assumptions.',
            'Reject superiority if a conventional optimizer matches cost; it does in this replay. Field applicability also fails if measured cake response differs.',
            'Null test with pressure-independent moisture picks minimum pressure; maximum dryness is not a universally valid proxy for minimum cost.')
        add(26,'Schedule copper converter blows against the acid-plant gas envelope',
            'Smelt matte continuously | Charge batch converters | Blow oxygen and evolve SO2 | Mix converter and smelter gases | Clean and cool gases | Convert SO2 to acid | Audit sulfur capture and auxiliary heat',
            [(2,4),(3,6),(1,4)],
            ['EXACT SULFUR: feed sulfur equals acid sulfur, emitted sulfur and changing inventories.',
             'ENERGY: catalyst beds have minimum heat balance and maximum allowable temperature.',
             'ENGINEERING: blower, hood capture and pressure limits apply jointly to simultaneous converter events.',
             'QUALITY: equal copper production and sulfur capture prevent fictitious fuel savings by throttling production.'],
            'Independent converter schedules can create gas pulses outside the acid-plant thermal and flow envelope. Test sulfur-flow-aware blow staggering while preserving each furnace metallurgy and hood capture.',
            'Projection-Loss: same daily SO2 production can have different hourly concentration/heat-release profiles. Necessity-Challenge: extra support fuel may be avoidable through scheduling. Decision-Sufficiency: upstream event timing matters only if the acid-plant controller cannot already absorb the pulse.',
            'Fuel saving=DeltaP_support*h (kWh/y); gross=DeltaP_support*h*p_fuel. Sulfur-flow constraint sum(mdot_S,i) <= admitted plant envelope at each time.',
            {'avoided_support_kW':300,'hours_y':8000,'fuel_USD_kWh':.04},
            {'required_support_energy_reduction_kWh_y':2400000},
            financial(8000,300,.04,30000,300000,'average avoided support-fuel kW','No acid-sales and copper-throughput credits; support fuel reduction is a target.'),
            'Integrated smelter/acid-plant scheduling and pressure controls, including modern centralised/hierarchical optimisation.','KNOWN',
            ['https://doi.org/10.1016/j.compchemeng.2022.107864','https://patents.google.com/patent/US4281821A/en'],
            'Primary scheduling study and historical control patent already couple these units.',
            'Reject if scheduling worsens sulfur emissions, shifts production, or gives no gain against integrated scheduling.',
            'A plant with no auxiliary fuel and adequate buffer capacity has no saving under this channel.')
        add(27,'Allocate copper-bearing scrap to product tolerance before melting',
            'Receive scrap lots | Assay attached and dissolved copper | Blend charge against product specification | Melt and refine steel | Oxidise during reheat | Hot-work with surface copper enrichment | Grade product and account dilution',
            [(2,5),(3,7),(2,7)],
            ['EXACT COPPER BALANCE: ordinary steel refining does not justify silently deleting incoming Cu.',
             'CONSTITUTIVE: selective oxidation can enrich Cu at the steel-scale interface; alloy and thermal history matter.',
             'ENGINEERING: grade-specific residual limits and rolling quality are hard boundaries.',
             'ECONOMIC: dilution saving must net assay, sorting and lost flexibility; no universal Cu threshold assumed.'],
            'An average scrap category can lose copper identity before grade scheduling. Test assay-informed allocation to already qualified copper-tolerant grades, reducing low-residual virgin dilution without inventing melt removal.',
            'Projection-Loss: same scrap mass and average purchase grade hide lot-level residuals. Necessity-Challenge: dilution with low-Cu iron may not be necessary for every product. Decision-Sufficiency: value assays by avoided premium dilution under all grade constraints.',
            'c_mix=sum(m_i*c_i)/sum(m_i); benefit=M*df*p_premium. Units: mass fractions, t/y and USD/t premium.',
            {'steel_t_y':200000,'avoided_premium_iron_fraction':.015,'premium_USD_t':50},
            {'required_avoided_premium_iron_t_y':3000},
            financial(200000,.015,50,30000,500000,'avoided premium charge fraction','No benefit is assumed from exceeding product residual limits;1.5% charge change is a target.'),
            'Scrap blending optimisers with residual constraints and modern Cu-aware steel alloy/product allocation.','KNOWN',
            ['https://link.springer.com/article/10.1007/s11663-019-01537-9','https://www.jstage.jst.go.jp/article/jsas1989/13/3/13_3_260/_article/-char/en'],
            'Primary physical analysis and experiments establish residual copper/hot-shortness and existing separation options.',
            'Reject if lower dilution creates surface cracking or if an incumbent grade-aware blender chooses the same allocation.',
            'Uniform Cu content across all lots leaves no information benefit from lot separation.')
        add(28,'Close the nitride-to-ammonia balance across aluminium salt-dross leaching',
            'Characterise salt dross | Wet and leach salts | Hydrolyse aluminium nitride | Collect mixed offgas | Separate or scrub ammonia | Recover salts and alumina residue | Close nitrogen and gas-treatment inventory',
            [(1,4),(3,7),(5,7)],
            ['EXACT STOICHIOMETRY: AlN+3H2O -> Al(OH)3+NH3;17/41 kg NH3 per kg AlN using rounded molar masses.',
             'SPECIES: NH3 may dissolve or escape; gas-only readings do not close nitrogen balance.',
             'SAFETY: hydrogen, methane and possible hazardous trace gases require a qualified offgas system.',
             'QUALITY: recovered solution has a qualified use; avoided reagent value cannot be assumed from crude gas mass.'],
            'Leach salt yield can be optimised while nitrogen transfers unnoticed into brine and offgas. Test coordinated pH/temperature and gas/liquid capture accounting, using usable recovered ammonia to displace purchased reagent.',
            'Projection-Loss: equal salt yield hides dissolved versus vented NH3. Necessity-Challenge: destruction of all recovered nitrogen is not always required if a qualified reuse exists. Decision-Sufficiency: measure phase partition before choosing capture settings.',
            'NH3potential=M_dross*f_AlN*(17/41); additional usable NH3=potential*dcapture. Gross=t_NH3/y*USD/t displaced reagent.',
            {'dross_t_y':20000,'AlN_fraction':.04,'incremental_usable_capture_fraction':.15,'net_reagent_USD_t':300},
            {'potential_NH3_t_y':20000*.04*17/41,'additional_usable_NH3_t_y':20000*.04*17/41*.15},
            financial(20000*.04*17/41,.15,300,10000,100000,'additional usable ammonia capture fraction','Required gas treatment already exists. Extra capture benefits cannot excuse emissions; price is assumed avoided reagent cost.'),
            'Established staged dross leaching and ammonia recovery, including nitrogen-product recovery patents.','KNOWN',
            ['https://patents.google.com/patent/US5227143A/en','https://patents.google.com/patent/WO1991009978A1/fr'],
            'Patents directly describe nitride hydrolysis and collecting ammonia or converting it to salts.',
            'Reject if ammonia cannot meet the receiving process specification or the complete nitrogen/cost balance is negative.',
            'At zero AlN or no incremental usable capture, this benefit channel is zero.')
        add(29,'Bind foundry core gas-release timing to the vent path during filling',
            'Store binder-containing cores | Assemble mold and vents | Pour metal around changing exposed surfaces | Heat and decompose binder | Vent gas through remaining paths | Solidify casting | Inspect gas defects and reconcile yield',
            [(1,4),(3,5),(4,6)],
            ['EXACT GAS BALANCE: generated gas equals vented gas plus compressed/dissolved inventory.',
             'CONSTITUTIVE: Darcy vent flow depends on permeability, gas viscosity and open path; moving metal changes the boundary.',
             'ENGINEERING: gas pressure must remain below a qualified defect/metal-entry envelope.',
             'QUALITY: slower filling cannot compromise cold-shut or inclusion specifications.'],
            'A room-temperature permeability certificate can miss the gas peak after molten metal closes a vent. Test time-resolved core storage/moisture data in the fill simulation and adjust vent geometry or qualified pour sequence.',
            'Projection-Loss: identical room permeability but different gas-generation timing. Necessity-Challenge: more binder may not be needed if core handling is improved. Decision-Sufficiency: use gas-release measurements only when they alter the admitted vent/pour design.',
            'For fixed path, Q=k*A*DeltaP/(mu*L); halve open A and required DeltaP doubles at fixed gas generation. Gross=N_castings*dscrap*net_margin.',
            {'castings_y':200000,'target_absolute_scrap_reduction':.01,'net_margin_USD_casting':30},
            {'pressure_ratio_for_halved_open_area':2,'required_additional_good_castings_y':2000},
            financial(200000,.01,30,10000,200000,'absolute scrap fraction','30 USD is net recoverable marginal value after scrap salvage; no gross sales credit.'),
            'Modern casting multiphysics models with moving fill fronts, measured binder gas curves and vent permeability.','KNOWN',
            ['https://link.springer.com/article/10.1007/s40962-023-01090-x','https://link.springer.com/article/10.1007/s40962-023-01180-w'],
            'Primary experiments already bind gas release, storage, binder and permeability to casting models.',
            'Reject if equal-quality trials show no scrap advantage over measured-gas modern simulation.',
            'With negligible gas generation or ample unchanged vents, extra schedule adaptation has no predicted benefit.')
        add(30,'Transfer strip oxide state from annealing into galvanizing control',
            'Identify steel alloy lot | Anneal in controlled H2/water atmosphere | Form selective surface oxides | Transfer strip to zinc bath | Wet and form coating interface | Cool and inspect coating | Reconcile rework and gas use',
            [(1,3),(2,5),(3,6)],
            ['EXACT ELEMENT BALANCE: surface oxygen is transferred to oxide or removed through qualified reduction reactions.',
             'CONSTITUTIVE: oxide morphology and alloy chemistry determine wetting; dew point is not a universal scalar quality guarantee.',
             'ENGINEERING: hydrogen atmosphere and bath controls retain plant safety limits.',
             'QUALITY: coating adhesion, bare spots and alloy mechanical properties must all remain qualified.'],
            'A single furnace dew-point setting can lose alloy-specific oxide morphology at the zinc handoff. Test alloy/oxide-qualified dew-point recipes and transfer-time tracking against actual coating adhesion, not dew point alone.',
            'Projection-Loss: equal dew point can yield different oxides for different alloys. Necessity-Challenge: universally stronger reduction may be unnecessary or ineffective. Decision-Sufficiency: surface-state measurement matters only when the qualified atmosphere/bath recipe changes.',
            'Young wetting relation cos(theta)=(gamma_SV-gamma_SL)/gamma_LV applies to ideal equilibrium surfaces; reactive wetting needs kinetic qualification. Required benefit=M*dreject*v_rework.',
            {'strip_t_y':300000,'target_absolute_reject_reduction':.002,'net_rework_USD_t':200},
            {'required_avoided_reject_t_y':600},
            financial(300000,.002,200,20000,300000,'absolute reject fraction','No claimed universal dew point or directly predicted scrap rate.'),
            'Alloy-specific selective-oxidation/reactive-wetting modelling and galvanizing simulator recipes.','KNOWN',
            ['https://onlinelibrary.wiley.com/doi/10.1002/srin.202300678','https://www.sciencedirect.com/science/article/pii/S0010938X14002054'],
            'Primary experiments directly vary dew point and observe oxidation and zinc wetting.',
            'Reject if atmosphere changes improve visible coating but reduce adhesion or mechanical qualification, or incumbent recipes match.',
            'If all lots share the same oxide response and transfer history, the additional classification has no value.')
        add(31,'Use cullet carbon balance when dosing glass fining sulfate',
            'Receive recycled cullet | Measure organic and reduced contaminants | Blend with sulfate-bearing batch | Heat and change melt redox | Generate fining gas and foam | Refine and form glass | Inspect bubbles and colour',
            [(2,4),(3,6),(4,7)],
            ['EXACT REDOX/ELEMENT: carbon, sulfur and oxygen balances must include furnace atmosphere and offgas.',
             'CONSTITUTIVE: sulfate decomposition and gas solubility vary with redox and temperature.',
             'ENGINEERING: bubble removal requires adequate residence and viscosity; reducing sulfate is not universally beneficial.',
             'QUALITY: colour, bubbles, emissions and melt throughput are held fixed.'],
            'A mass-only cullet substitution recipe loses its reducing carbon load. Test incoming-lot organic-carbon adjustment of fining sulfate/oxidant within an existing qualified redox model.',
            'Projection-Loss: equal cullet fraction with different residual carbon. Necessity-Challenge: a fixed sulfate excess may be avoidable. Decision-Sufficiency: assay only if it changes batch recipe enough to offset test cost and false correction.',
            'O2 equivalent for complete C oxidation=(32/12)*m_C. An added0.1 kgC/t batch requires0.2667 kgO2/t in this stoichiometric bound; no fixed sulfate substitution ratio is inferred.',
            {'glass_t_y':200000,'extra_carbon_kg_t':.1,'target_absolute_reject_reduction':.002,'net_rework_USD_t':150},
            {'extra_O2_equivalent_kg_t':32/12*.1,'required_avoided_reject_t_y':400},
            financial(200000,.002,150,20000,400000,'absolute reject fraction','Illustrative cost screen is negative; no further fuel credit or sulfate revenue.'),
            'Published cullet-organic/redox/fining models and batch redox control already address this interface.','KNOWN',
            ['https://repository.tno.nl/SingleDoc?docId=73059','https://repository.tno.nl/SingleDoc?docId=61001'],
            'Primary glass research directly treats organic contamination, sulfur reactions and fining.',
            'Reject if batch correction merely trades bubbles for colour or SOx, or an established redox controller is equivalent.',
            'At constant cullet reducing load, extra carbon assay cannot improve an already calibrated recipe.')
        add(32,'Include salt deposition in glass-regenerator reversal decisions',
            'Evolve sodium sulfate and dust in melting | Carry exhaust into checker brick | Condense salt in cooler passages | Restrict gas flow and alter heat exchange | Reverse to combustion-air preheat | Reheat or clear deposited regions | Audit fuel, pressure drop and refractory condition',
            [(1,3),(3,5),(6,4)],
            ['EXACT ENERGY: compare complete heating/cooling cycles with equal brick terminal heat inventory.',
             'SPECIES BALANCE: salt removal moves material to a collection path; it does not annihilate sulfur/sodium.',
             'CONSTITUTIVE: deposit temperature and phase govern adhesion/melting; gas composition and local temperatures are necessary.',
             'ENGINEERING: refractory/support temperatures and emissions constrain cycle extension or local heating.'],
            'Pure heat-recovery optimisation can miss deposit accumulation. Test a deposit-aware reversal or selective-clearing schedule with spatial temperature and pressure-drop constraints. Independent review found a patent already connecting cycle length, salt plugging and overheating.',
            'Projection-Loss: equal mean checker temperature hides cold plugged zones. Necessity-Challenge: whole-regenerator heating may be unnecessary when local clearing suffices. Decision-Sufficiency: spatial sensing only has value if the incumbent deposit-aware policy makes a different decision.',
            'Recovered annual fuel value=M*e_fuel*df*p_fuel. Dimensions: t/y*GJ/t*fraction*USD/GJ. Actual deposit dynamics and allowable cycle changes remain unidentified.',
            {'glass_t_y':200000,'fuel_GJ_t':5,'target_fuel_reduction_fraction':.01,'fuel_USD_GJ':10},
            {'required_avoided_fuel_GJ_y':10000},
            financial(1e6,.01,10,15000,200000,'fuel reduction fraction','All cycle endpoints must have equal checker heat inventory; local burner fuel is included in extra OPEX.'),
            'Deposit-aware regenerator control including US5840093A local heating and cycle-length/deposit tradeoffs.','KNOWN',
            ['https://patents.google.com/patent/US5840093A/en','https://pure.tue.nl/ws/files/1742411/255404.pdf'],
            'The patent explicitly discusses cycle duration, local salt condensation and support overheating. No novel joint-control claim survives.',
            'Reject if net firing rises, refractory damage increases, or existing deposit-aware control achieves the same outcome.',
            'With clean passages, reversal optimisation reduces to known thermal-cycle control; no deposit-specific benefit remains.')
        add(33,'Set ceramic debinding ramps from gas transport and shrinking green strength',
            'Form binder-containing green body | Characterise thickness and pore paths | Heat into binder decomposition | Generate and transport vapor | Lose binder-supported green strength | Complete burnout and sinter | Inspect cracking and density',
            [(2,4),(3,5),(4,6)],
            ['EXACT MASS: binder removed equals evolved species plus residual carbon and condensate.',
             'CONSTITUTIVE: vapor generation and transport depend on temperature, pore connectivity and body size.',
             'ENGINEERING: internal stress must remain below evolving green strength, not only final ceramic strength.',
             'QUALITY: equal burnout/carbon residue and final density are required when changing ramp time.'],
            'A furnace temperature recipe can erase body thickness and the temporary strength trough during burnout. Test thickness/permeability-conditioned ramp holds that preserve the gas-pressure/green-strength margin.',
            'Projection-Loss: identical oven temperature, different core gas pressure. Necessity-Challenge: a universally slow ramp may be unnecessary for thin/permeable parts. Decision-Sufficiency: characterise transport only when ramp scheduling changes enough to reduce defects/cycle cost.',
            'Diffusive transport time tau=L^2/D_eff (s); doubling half-thickness gives4*tau at constant D. Pressure/strength margin requires coupled reaction-transport modelling.',
            {'body_half_thickness_ratio':2,'parts_y':1e6,'target_absolute_scrap_reduction':.003,'net_margin_USD_part':20},
            {'transport_time_ratio':4,'required_avoided_scrap_parts_y':3000},
            financial(1e6,.003,20,10000,100000,'absolute scrap fraction','No cycle-time capacity credit; final burnout is matched.'),
            'Existing thermal debinding pressure/stress/strength models and geometry-aware transport-network design.','KNOWN',
            ['https://www.kci.go.kr/kciportal/landing/article.kci?arti_id=ART001628139','https://www.sciencedirect.com/science/article/pii/S0272884223042359'],
            'Primary models already couple green strength, gas pressure, geometry and thermal history.',
            'Reject if the modified ramp leaves carbon, reduces density or fails against a calibrated debinding model.',
            'For transport much faster than generation, pressure-limited holds may not be needed, though chemical burnout still is.')
        add(34,'Carry spray-granule shell strength into ceramic pressing pressure',
            'Disperse ceramic slurry | Atomise and dry droplets | Form binder-rich shell or hollow granules | Fill pressing die | Crush or deform granules | Sinter inherited pore structure | Grade tile strength and appearance',
            [(1,3),(3,6),(4,7)],
            ['EXACT MASS: ceramic and binder mass are conserved through drying apart from specified volatilisation.',
             'CONSTITUTIVE: granule morphology and binder distribution determine crush pressure, not particle size alone.',
             'ENGINEERING: pressing load must compact granules without unacceptable tooling or lamination damage.',
             'QUALITY: sintered strength/porosity and dimensional tolerance bind any pressure or slurry change.'],
            'Powder with equal nominal size and moisture may retain different hard shells. Test shell-strength-conditioned slurry/atomisation settings and pressing recipes, instead of increasing press pressure blindly.',
            'Projection-Loss: equal sieve distribution, different hollow-shell population. Necessity-Challenge: higher pressure is not always required if shell formation is corrected upstream. Decision-Sufficiency: morphology sampling matters only when it changes a process setting.',
            'Ideal thin spherical shell pressure p_cr = 2E/sqrt(3(1-nu^2))*(t/R)^2. Halving t/R reduces this elastic-buckling scale by4; real irregular wet granules require measured crush curves.',
            {'shell_thickness_radius_ratio_factor':.5,'tile_m2_y':5e6,'target_absolute_reject_reduction':.002,'net_margin_USD_m2':5},
            {'ideal_buckling_pressure_ratio':.25,'required_additional_good_m2_y':10000},
            financial(5e6,.002,5,10000,200000,'absolute reject fraction','Thin-shell equation is a conditional physical analogy, not a validated ceramic process predictor.'),
            'Modern granule compaction/microstructure characterisation and slurry-dispersion control.','KNOWN',
            ['https://www.sciencedirect.com/science/article/pii/S027288421933737X','https://doi.org/10.1111/j.1151-2916.1999.tb01990.x'],
            'Primary work directly links binder distribution, slurry rheology and hollow granules to compaction.',
            'Reject if changed drying worsens flow/die filling or strength, or standard morphology-aware pressing achieves the same result.',
            'When all granules collapse well below normal pressing pressure, a more detailed shell model may not change the decision.')
        add(35,'Use sulfate-release timing when qualifying cement superplasticizer dose',
            'Blend cement and sulfate carriers | Store at varying temperature | Contact mix water | Dissolve sulfate and hydrate C3A | Adsorb polycarboxylate dispersant | Place concrete at target workability | Verify set and hardened strength',
            [(1,4),(2,5),(4,6)],
            ['EXACT SPECIES: sulfate and polymer are partitioned among solution, adsorption and solid products.',
             'CONSTITUTIVE: competitive adsorption and sulfate-carrier dissolution depend on chemistry and temperature.',
             'ENGINEERING: water/binder ratio, placement window and setting time remain within a qualified mix contract.',
             'QUALITY: reduced admixture cannot trade away strength, durability or slump retention.'],
            'Total SO3 and total admixture dose can hide sulfate release during the placement window. Test a short dissolution/adsorption qualification per cement lot and choose an already allowed dose/sequence.',
            'Projection-Loss: equal bulk SO3, different carrier dissolution. Necessity-Challenge: extra PCE may not be necessary after correcting mixing sequence. Decision-Sufficiency: a release assay is useful only when dose savings exceed testing cost at equal performance.',
            'PCE saving = concrete_volume*cement_t_m3*dPCE_kg_t/1000 (t/y). Gross=saved_PCE_t*p_PCE.',
            {'concrete_m3_y':200000,'cement_t_m3':.3,'target_PCE_kg_t_reduction':.2,'PCE_USD_t':2000},
            {'required_PCE_reduction_t_y':12},
            financial(60000,.2,2,10000,100000,'kg PCE/t cement','Cost screen is negative at the assumed target; no extra water or cement reduction credit.'),
            'Current sulfate/PCE competitive-adsorption and temperature-aware compatibility testing.','KNOWN',
            ['https://doi.org/10.1016/J.CONBUILDMAT.2020.119428','https://www.sciencedirect.com/science/article/pii/S0008884600005032'],
            'Primary experiments already test sulfate/PCE coupling; dose gain is a hypothetical target.',
            'Reject if lower dose changes slump retention, set, strength or durability, or ordinary compatibility testing matches.',
            'With invariant sulfate release across lots, repeated assays have no incremental decision value.')
        add(36,'Stop calcined-clay grinding when reactivity no longer pays for energy',
            'Identify clay mineral assemblage | Calcine within an activation window | Cool without uncontrolled rehydration | Grind and mechanically activate | Measure reactive fraction and water demand | Blend qualified cement | Test strength and total processing cost',
            [(1,4),(2,5),(4,7)],
            ['EXACT MATERIAL: mineral mass plus released structural water closes the calciner balance.',
             'CONSTITUTIVE: thermal dehydroxylation and mechanical activation are mineral-dependent; fineness alone does not equal reactivity.',
             'ENGINEERING: grinding wear contamination and water demand may increase even when surface area rises.',
             'QUALITY: matched strength, workability and durability are mandatory before claiming energy benefit.'],
            'A universal fineness target can overgrind already reactive clay or under-activate another mineral assemblage. Test mineral/reactivity-qualified grinding stop rules jointly with calcination history.',
            'Projection-Loss: equal Blaine area, different structural disorder and reactive fraction. Necessity-Challenge: all clay need not receive the same milling energy. Decision-Sufficiency: reactivity testing pays only if it safely changes grinding allocation.',
            'Saved energy=M*de (kWh/y); gross=M*de*p_e. The prediction is conditional on equal independently tested cement performance; no reactivity equation is invented.',
            {'clay_t_y':200000,'target_kWh_t_reduction':10,'power_USD_kWh':.1},
            {'required_energy_saving_kWh_y':2000000},
            financial(200000,10,.1,20000,500000,'kWh/t clay','Calciner fuel and clinker substitution benefits are excluded to avoid overlapping credits.'),
            'Mineral-specific thermal/mechanical activation optimisation with R3/Chapelle tests, particle size and cement performance.','KNOWN',
            ['https://www.research-collection.ethz.ch/entities/publication/af9bfba2-9f5f-4e5f-a35d-87d4387126b1','https://discovery.ucl.ac.uk/id/eprint/10220362/','https://pubmed.ncbi.nlm.nih.gov/39336392/'],
            'Primary work already evaluates overcalcination, hybrid activation and energy/wear tradeoffs.',
            'Reject if avoided milling increases clinker demand or water demand enough to erase the benefit, or modern mineral-aware control matches.',
            'If all incoming clay has identical activation response, lot-specific testing cannot improve a calibrated fixed grind.')
        add(37,'Separate water and suspended solids when reusing concrete wash slurry',
            'Wash mixer and collect slurry | Settle or agitate reclaimed tank | Measure liquid and solids fractions | Meter reclaimed slurry into new batch | Correct fresh water and qualified solids contribution | Place and cure concrete | Verify workability and durability',
            [(2,5),(3,6),(1,7)],
            ['EXACT WATER: slurry mass equals liquid water plus solids; solids must not be counted as mixing water.',
             'EXACT SOLIDS: hydrated old cement is not automatically equivalent to fresh binder.',
             'CONSTITUTIVE: fines age, alkalinity and residual admixture can change rheology and hydration.',
             'QUALITY: required strength, chloride/alkali limits and setting behavior remain qualified.'],
            'A volume-only reclaimed-water meter can lose suspended solids and effective water. Test density/solids measurement and batch correction while explicitly classifying old hydrated solids as filler unless separately qualified.',
            'Projection-Loss: equal slurry volume can deliver different free water and fines. Necessity-Challenge: all slurry need not be disposed when correctly dosed. Decision-Sufficiency: extra measurement has value only if it raises qualified reuse relative to existing solids-aware batching.',
            'For mass S and dry solids fraction s, free water W=S(1-s), retained solids=Ss. A1000kg batch at5% solids gives950kg water, not1000kg.',
            {'concrete_m3_y':200000,'additional_qualified_reuse_m3_per_concrete_m3':.05,'combined_avoided_water_disposal_USD_m3':4},
            {'water_from_1000kg_5pct_slurry_kg':950,'extra_reuse_m3_y':10000},
            financial(200000,.05,4,10000,100000,'m3 slurry reuse per m3 concrete','Combined4 USD/m3 is a single assumed avoided water/disposal cost; no cement replacement credit.'),
            'Established reclaimed-wash-water qualification and solids-corrected batching, including treated/carbonated water options.','KNOWN',
            ['https://www.sciencedirect.com/science/article/pii/S0008884600004683','https://pmc.ncbi.nlm.nih.gov/articles/PMC11990545/'],
            'Primary studies already assess fines, actual water/cement ratio and strength response.',
            'Reject if corrected reuse changes durability or requires extra cement that outweighs disposal/water saving.',
            'At zero suspended solids, volume/mass water correction collapses to ordinary clear-water dosing.')
        add(38,'Qualify carbonated slag by residual reactive lime rather than CO2 uptake alone',
            'Characterise free lime and slag mineral phases | Crush and size aggregate | Expose moist slag to CO2 | Form carbonated shell and react calcium phases | Sample residual core and free lime | Run expansion and product qualification | Sell only qualified aggregate and close carbon balance',
            [(1,5),(3,6),(4,7)],
            ['EXACT STOICHIOMETRY: CaO+CO2 -> CaCO3,44/56 mass CO2/CaO using rounded molar masses.',
             'SPECIES: CO2 uptake into other Ca/Mg phases does not prove free-CaO removal.',
             'CONSTITUTIVE: reaction-front transport can leave an unreacted core; fixed penetration depth is a model assumption.',
             'QUALITY: expansion qualification must cover the actual aggregate/product, final replacement fraction and exposure; no invented safe fCaO standard.'],
            'Total CO2 uptake can be mistaken for complete stabilisation. Test a release gate retaining initial mineral phase, particle size and residual free-CaO/soundness evidence; further-treat only failing fractions. Existing soundness testing already addresses the main risk.',
            'Projection-Loss: same 6 kg CO2/t, different fraction reacting with free lime. Necessity-Challenge: uniform longer carbonation may be unnecessary when only selected fractions fail. Decision-Sufficiency: residual assay only adds value beyond incumbent soundness testing if it changes treatment economically.',
            'Residual fCaO=c0-alpha*u*56/44 kg/t,0<=alpha<=1, consumption<=c0. Unreacted spherical core fraction=(1-delta/R)^3 for0<=delta<=R. No expansion law is inferred from these balances.',
            {'initial_free_CaO_kg_t':10,'uptake_CO2_kg_t':6,'alpha_cases':[1,.2],'illustrative_threshold_kg_t':5,'radius_mm':5,'reacted_depth_mm':1},
            {'residual_free_CaO_kg_t':d['slag_residual_free_CaO_kg_t'],'unreacted_volume_fraction':d['slag_unreacted_core_volume_fraction'],'same_CO2_uptake_but_different_gate':True},
            financial(100000,.10,12,30000,500000,'additional independently qualified saleable fraction','100000 t/year slag; assumed additional qualified fraction10%;12 USD/t net outlet spread. No carbon credits; gate itself does not prove10% gain.'),
            'Phase-resolved carbonation models plus residual-free-lime and accelerated soundness/expansion tests already in literature. Same assays make conventional decisions identical.','OVERLAP',
            ['https://pmc.ncbi.nlm.nih.gov/articles/PMC10488658/','https://pmc.ncbi.nlm.nih.gov/articles/PMC11243214/','https://orca.cardiff.ac.uk/id/eprint/133474/'],
            'Primary tests examine residual lime, carbonation, expansion and carbonate-layer effects. Narrow assay-economics superiority remains unresolved.',
            'Reject if released aggregate fails independently applicable expansion/durability tests, or a conventional soundness gate gives equal net value.',
            'If alpha and c0 are already known exactly, uptake determines the residual in this toy model; no projection gap remains. If delta>=R, geometric unreacted core is zero.')
        add(39,'Track soluble salts from recycled gypsum into the paper-bonding front',
            'Receive recycled gypsum | Remove paper and coarse contaminants | Measure soluble salts and moisture | Wash qualified fractions if necessary | Recalcine and form board slurry | Dry with salt migration to paper interface | Qualify bond and recycle off-spec board',
            [(3,6),(4,7),(5,7)],
            ['EXACT SALT: chloride removed in wash appears in wastewater; dryer does not eliminate dissolved salt.',
             'EXACT WATER/ENERGY: washing adds water that must be recovered or evaporated before fair energy comparison.',
             'CONSTITUTIVE: salt migration during drying changes the paper-core interface; total recycled fraction is not sufficient.',
             'QUALITY: paper adhesion, set and board properties constrain recycled feed qualification.'],
            'A recycled-gypsum percentage can omit soluble salt loading and its interface concentration after drying. Test salt-stratified blending/washing with explicit wastewater and redrying costs, avoiding automatic rejection of all recycled feed.',
            'Projection-Loss: equal gypsum purity by bulk mineral assay can hide dissolved chloride. Necessity-Challenge: universal virgin gypsum use may be unnecessary for clean recycled lots. Decision-Sufficiency: assay pays only when it changes washing/blending without greater drying cost.',
            'Salt after ideal washing m_s,out=m_s,in*(1-r_remove); extra drying Q=m_addedwater*L/eta. Benefit=M*df*v_qualified_feed; all wash/redry costs charged to OPEX.',
            {'board_gypsum_t_y':100000,'extra_qualified_recycled_fraction':.10,'net_feed_spread_USD_t':15,'ideal_salt_removal_fraction':.8},
            {'remaining_salt_fraction':.2,'extra_recycled_gypsum_t_y':10000},
            financial(100000,.10,15,100000,500000,'additional qualified recycled feed fraction','OPEX100000 includes assumed washing, wastewater and redrying. Target scenario is negative.'),
            'Published acid-leaching purification and soluble-impurity qualification for post-consumer gypsum.','KNOWN',
            ['https://pmc.ncbi.nlm.nih.gov/articles/PMC10873547/','https://www.mdpi.com/2071-1050/16/1/425'],
            'Primary studies directly identify soluble salts, migration to paper interface and purification routes.',
            'Reject if additional water/redrying/wastewater cost exceeds feed saving or paper bond is not equivalent.',
            'With salt-free recycled material, purification has no salt-removal benefit and may only add cost.')
        add(40,'Dry reclaimed asphalt without spending the binder thermal-aging budget',
            'Receive and cover RAP stockpile | Measure moisture and binder condition | Pre-dry or separate wet fines | Heat aggregate and RAP along qualified route | Blend activated aged binder and fresh components | Compact pavement material | Test cracking, rutting and moisture resistance',
            [(1,4),(2,5),(4,7)],
            ['EXACT WATER/ENERGY: removal of moisture requires latent and sensible heat; inventory-drying effects are not free.',
             'CONSTITUTIVE: oxidative aging depends on temperature, oxygen and time; binder activation/blending also requires heat.',
             'ENGINEERING: staged heating cannot compromise moisture removal, emissions or plant throughput.',
             'QUALITY: cracking, rutting and moisture susceptibility are jointly qualified; rejuvenation is not assumed complete.'],
            'An outlet aggregate temperature can hide binder exposure during removal of wet RAP moisture. Test moisture-qualified feed separation/covered storage and staged heating while tracking a calibrated binder aging integral.',
            'Projection-Loss: same final mix temperature, different RAP time-temperature-oxygen exposure. Necessity-Challenge: superheating all virgin aggregate may not be necessary with drier RAP. Decision-Sufficiency: moisture/binder sensing pays only if the safe thermal route changes.',
            'Avoided evaporation fuel=M_RAP*1000*dw*L/eta MJ/y. WithL=2.5MJ/kg,eta=.7,dw=.01, avoided fuel35.714MJ/t RAP. Aging damage integral requires independently fitted kinetics.',
            {'RAP_t_y':100000,'target_moisture_reduction_kg_kg':.01,'latent_MJ_kg':2.5,'dryer_efficiency':.7,'fuel_USD_GJ':10},
            {'avoided_fuel_GJ_y':100000*1000*.01*2.5/.7/1000},
            financial(100000,.01,1000*2.5/.7/1000*10,15000,200000,'kg water/kg RAP','No pavement-life monetary credit; covering/pre-drying cost is annualized. Assumed screen is negative.'),
            'Modern RAP moisture management, separate/staged drying and binder aging/activation qualification.','KNOWN',
            ['https://www.sciencedirect.com/science/article/abs/pii/S0959652623009381','https://www.sciencedirect.com/science/article/abs/pii/S095006182034191X'],
            'Primary tests establish preheating/aging and recycling tradeoffs; the1% moisture reduction is an assumed target.',
            'Reject if fuel use just shifts to pre-drying, equal binder activation is not met, or modern moisture-aware practice ties.',
            'Already dry RAP gives no moisture-removal saving. Zero heat can also fail binder blending, so colder is not universally better.')
        assert len(cases)==20 and len({c['id'] for c in cases})==20
        for c in cases:
            f=c['financial']
            assert abs(f['gross']-f['opex']-f['annualized_capex']-f['net'])<1e-8
            assert f['modern_baseline_increment'] is None
        return cases

    return run(), deep_tests()



# Source SHA256: edcbc315d5093c987a2095c94d1828498d3689c83c678d16715a0d2e9c6475d5
def workstream_manufacturing():
    """N041-N060 bounded physical research screens, 2026-10-09.
    Standard library only. No measured savings, novel certification, plant action,
    or Garden canonical admission. run() returns twenty traceable records.
    """
    import math
    from pathlib import Path

    SOURCE_MANIFEST = [('V15_10_ABSTRACTION_GCSC_DELTA.md', '90a58c337bc87c2e445eb56d6197cddea845f74485339e074b0818d70dae8479', 'whole'), ('GSL_COMBINATORIAL_SEMANTIC_COVERAGE_v0.1.md', '27428feebc2fe8f2a4a9a5dd8fc5d680d36fb18623575ef19235427f9021e3b1', 'whole'), ('INVARIANT_DRIVEN_THEORY_DISCOVERY_IDTD_001.md', '14bf4fdced0cccebeb5cb22a0cec3b7aff765e57efa25230626ddcf3b24bfdf4', 'whole'), ('TREE_CORE_v0.8.1_2026-09-23.txt', '4af3a2c4c8d8577909735fb61c42e0f43324dc0147d8b24146b4561ee56511fa', 'lines 95-170, 275-327, 352-390'), ('GARDEN_TECHNICAL_v15.10_FULL_DELTA.txt', 'f61bc8e4f12418498f114f586c2d4e58b1ca575a788e0e5194430088a0f8f18f', 'lines 140-278, 830-887')]

    CRF = .08*(1.08**10)/(1.08**10-1)


    def record(i,title,nodes,extra,constraints,equation,inputs,prediction,gross,opex,capex,driver,driver_unit,baseline,novelty,sources,falsifier,projection,necessity,decision,intervention,source_scope,status='KNOWN'):
        nodes=nodes.split(' | ')
        edges=[(j,j+1) for j in range(1,len(nodes))]+extra
        annual=opex+CRF*capex
        financial={'gross':gross,'opex':opex,'capex':capex,'net':None if gross is None else gross-annual,'break_even':None if gross is None or gross<=0 else driver*annual/gross,'break_even_unit':driver_unit,'currency_scope':'ASSUMED USD per facility/year','increment_vs_strongest':None}
        return dict(id=f'N{i:03d}',title=title,nodes=nodes,edges=edges,constraints=constraints,equation=equation,inputs=inputs,physical_prediction=prediction,financial=financial,baseline=baseline,novelty=novelty,status=status,sources=sources,source_scope=source_scope,falsifier=falsifier,operators={'Projection-Loss':projection,'Necessity-Challenge':necessity,'Decision-Sufficiency':decision},intervention=intervention,admission='NONCANONICAL_CANDIDATE',empirical_validation='NOT_RUN')


    def run():
        c=[]
        c.append(record(41,'Qualify component bake termination from package moisture, not elapsed oven time',
          'Dry package received | Bag opened and humidity exposure | Moisture diffuses into package | Sealed qualified bake | Moisture endpoint estimated | Component solder reflow | Delamination and electrical acceptance',[(2,5),(3,6),(5,7)],
          ['EXACT species balance: absorbed water equals input minus desorption, nodes 2-5.', 'CONSTITUTIVE: slab diffusion with constant D is an approximation, nodes 3-5.', 'ENGINEERING: supplier bake temperature, floor-life and oxidation limits remain binding, nodes 4-7.'],
          'First-mode remaining fraction m(t)/m0=(8/pi^2)*exp(-pi^2*D*t/(4*L^2)); t[s], D[m^2/s], half-thickness L[m]. Valid late-time Fickian plane slab; not a supplier qualification.',
          {'D_m2_s':1e-11,'L_m':.001,'target_fraction':.01,'batches_y':1000,'bake_kW':20,'assumed_hours_avoided_batch':4,'electricity_USD_kWh':.12},
          {'target_hours':4*.001**2/(math.pi**2*1e-11)*math.log(8/(math.pi**2*.01))/3600},9600,2000,12000,4,'hours of bake avoided per batch',
          'Qualified IPC/JEDEC and supplier moisture-aware drying, floor-life tracking and dry storage. Financial screen compares unnecessary four-hour repeat bake only; no gain against compliant modern handling established.',
          'Package moisture diffusion and conditional baking are known. Narrow instrument endpoint still needs package-specific validation; not admitted as novel.',
          ['https://www.ti.com/lit/an/snoa300a/snoa300a.pdf','https://www.ti.com/quality-reliability/faqs.html'],
          'Any endpoint-passed package violates supplier handling or has excess reflow delamination versus prescribed bake.',
          'Equal exposure hours can yield different internal moisture at different humidity or thickness.',
          'Test whether an extra fixed bake is necessary once qualified moisture state is already below limit.',
          'Additional endpoint measurement pays only if avoided compliant bake energy exceeds annual sensor cost.',
          'Retain qualified exposure and diffusion state through the storage-to-reflow interface; stop only under independently qualified endpoint.',
          'TI application guidance and FAQs explicitly bind moisture sensitivity, exposure and baking to standards; source does not support our assumed four hours saved.'))
        c.append(record(42,'Use a jointly qualified oven recipe to reduce reflow changeover idle time',
          'Board and component limits registered | Existing oven thermal state | New board enters convection zones | Joint temperatures evolve | Conveyor speed selected | Solder liquidus exposure | Cooling and acceptance | Next board recipe change',[(1,5),(2,4),(4,7)],
          ['ENERGY balance: C*dT/dt=hA*(Ta-T), nodes 3-4, lumped body approximation.', 'ENGINEERING: every joint meets peak and time-above-liquidus windows, nodes 1,4,6,7.', 'DEPENDENCY: product identity, oven drift and loading invalidate old recipe, nodes 1,2,8.'],
          'T(t)=Ta+(T0-Ta)*exp(-t/tau), tau=C/(hA)[s]; heating time t=tau*ln((Ta-T0)/(Ta-Ttarget)). Different board taus require intersecting feasible speed intervals.',
          {'Ta_C':250,'T0_C':25,'Ttarget_C':217,'tau_fast_s':25,'tau_slow_s':55,'changeovers_y':1200,'assumed_minutes_avoided':10,'bottleneck_marginal_USD_h':200},
          {'fast_heat_s':25*math.log(225/33),'slow_heat_s':55*math.log(225/33)},40000,4000,40000,10,'minutes of qualified idle avoided per changeover',
          'KIC common-recipe/profile-prediction optimization already changes conveyor speed while maintaining component windows. Do not compare only with manual retuning.',
          'Direct commercial prior art; an implementation adoption opportunity, not a new mechanism.',
          ['https://kicthermal.com/article-paper/110-developing-common-reflow-oven-recipes-for-mixed-production-lines-using-the-kic-navigator-3/','https://kicthermal.com/wp-content/uploads/2016/08/The-Science-Behind-Conveyor-Oven-Profiling-R0610B.pdf'],
          'No common recipe exists, or any joint peak/TAL/cooling bound fails; assumed idle value disappears off bottleneck.',
          'Same oven setpoints do not imply same joint temperature on boards with different thermal mass.',
          'Test whether all zone setpoints must change for every board identity.',
          'Product-specific profile information enables speed-only changeovers only where feasible intervals intersect.',
          'Find and validate common oven settings with board-specific speeds, carry joint constraints into every transition.',
          'KIC explicitly describes common oven settings and conveyor-speed-only product changeovers; it supplies no evidence for our 10-minute or financial assumptions.'))
        c.append(record(43,'Meter selective-solder nitrogen from local oxygen exposure',
          'Nitrogen supplied | Gas shroud around nozzle | Air entrained by board motion | Solder wave contacts pad | Oxide and flux reaction | Joint and dross acceptance',[(2,5),(3,5),(1,4)],
          ['EXACT gas-species balance under steady well-mixed approximation, nodes 1-3.', 'ENGINEERING: local oxygen bound and wetting quality cannot be relaxed, nodes 4-6.', 'ECONOMIC: gas saving excludes any unmeasured dross or quality credit.'],
          'cO2=0.21*qa/(qN+qa), volume fraction, q in common reference Nm3/h; qN>=qa*(0.21/clim-1). Spatial jet entrainment makes a single mixed estimate nonconservative.',
          {'qN_old_Nm3_h':10,'qN_new_Nm3_h':7,'qa_Nm3_h':.01,'hours_y':6000,'gas_USD_Nm3':.25},
          {'oxygen_ppm_new':1e6*.21*.01/(7+.01)},4500,1500,25000,3,'Nm3/h nitrogen reduction',
          'Modern nozzle-local inerting, calibrated oxygen measurement and gas flow recipes; compare same local oxygen and joint yield.',
          'Nozzle-local nitrogen is established. Sensor-conditioned flow is not shown novel; declared economic screen is negative.',
          ['https://support.itweae.com/support/solutions/articles/42000072360-use-of-nitrogen-in-the-selective-soldering-machines','https://patents.google.com/patent/US20090224028A1/en'],
          'Local pad oxygen exceeds bound despite average estimate, or nitrogen reduction increases defects; negative net already rejects these costs.',
          'Same bottle flow can produce different local oxygen when shroud leakage changes.',
          'Challenge fixed maximum nitrogen flow while preserving validated local inertness.',
          'Measurement must avoid more than its annualized cost; present 3 Nm3/h reduction does not.',
          'Gate lower nitrogen flow on local oxygen and wetting validation rather than nominal supply flow alone.',
          'ITW describes nitrogen around the nozzle and its oxide-suppression role; patent describes nearby nitrogen outlet. No measured gas reduction supplied.',status='REJECTED'))
        c.append(record(44,'Reorder laser cuts to preserve heat-escape paths until narrow parts are complete',
          'Sheet clamped on bed | Nest and cut paths planned | First slots isolate ligaments | Heat enters remaining struts | Thermoelastic bow changes geometry | Later contour cut | Released part inspected',[(2,4),(3,5),(1,7)],
          ['ENERGY balance: heat input, conduction and losses, nodes 3-5.', 'CONSTITUTIVE: deltaL=alpha*L*deltaT only free uniform bar; restrained strut needs mechanics, nodes 4-5.', 'ENGINEERING: kerf, collision, part retention and final tolerance all preserved, nodes 2,6,7.'],
          'Free thermal movement deltaL=alpha*L*deltaT [m]; alpha[1/K], L[m], deltaT[K]. It is a materiality bound, not a cutting-error prediction.',
          {'alpha_per_K':12e-6,'strut_L_m':.2,'deltaT_K':100,'parts_y':600000,'assumed_absolute_scrap_reduction':.005,'marginal_USD_part':12,'extra_s_part':.1,'machine_USD_h':120},
          {'free_thermal_motion_mm':12e-6*.2*100*1000},36000,6000,60000,.005,'absolute scrap fraction reduction',
          'Thermomechanical nesting/cut-sequence optimization with strut heat isolation already modeled; strongest comparator retains evolving cut topology.',
          'Direct patent coverage of cut sequence, trapped strut heat and bowing; novel claim rejected.',
          ['https://patents.google.com/patent/US12059751B2/en','https://patents.google.com/patent/EP4126445B1/en'],
          'Reordering fails tolerance or raises total marginal cost including longer travel; 0.5 percentage-point scrap reduction is unmeasured.',
          'Identical total laser energy and final nest can have different transient conductive topology.',
          'Challenge shortest travel order as a necessary economic optimum.',
          'Predicting ligament state has value only if it changes a feasible sequence and net accepted-part cost.',
          'Keep neighboring heat-escape ligaments intact until sensitive contours finish, under full cut-plan constraints.',
          'Patents explicitly identify thermal trapping in narrow struts and sequence changes to reduce bowing.'))
        c.append(record(45,'Qualify sieved titanium powder reuse by chemistry and useful yield',
          'Powder lot loaded | Melt-adjacent powder exposed | Unmelted powder recovered | Oversize sieve rejects removed | Chemistry and size fractions sampled | Qualified blend made | Recoating and build | Mechanical acceptance',[(2,5),(4,6),(5,8),(6,8)],
          ['EXACT oxygen and metal mass balances through mixing, nodes 2-6.', 'CONSTITUTIVE: oxygen uptake and particle-size correlations require measurement, nodes 2,5.', 'ENGINEERING: chemistry, flow, packing and final properties remain bounded, nodes 5-8.'],
          'cblend=f*cv+(1-f)*cr; f_min=(cr-clim)/(cr-cv) for cv<clim<cr. Concentrations mass fractions; sieving alone cannot reduce uniformly dissolved oxygen.',
          {'virgin_O_wtpercent':.08,'reused_O_wtpercent':.14,'qualified_limit_wtpercent':.13,'powder_kg_y':20000,'assumed_additional_reuse_fraction':.1,'virgin_minus_salvage_USD_kg':60},
          {'minimum_virgin_mass_fraction':(.14-.13)/(.14-.08)},120000,25000,150000,.1,'additional qualified reuse fraction',
          'NIST powder-reuse and oxidation-aware mass-balance models, multi-property certification and qualified blending; no advantage versus those shown.',
          'Oxygen and particle size heterogeneity are measured prior art. Financial target is an adoption scenario, not discovery.',
          ['https://www.nist.gov/publications/additive-manufacturing-titanium-powder-oxygen-variation-within-single-powder-bed-due','https://www.nist.gov/publications/simple-numerical-model-lpbf-am-powder-reuse-and-experimental-design-model-verification'],
          'Accepted reuse fails property limits or sample misses localized oxidation; recovery displaces no virgin material.',
          'Same sieve pass fraction can conceal different chemistry and therefore permitted blend fractions.',
          'Challenge rejection after fixed reuse count when qualified chemistry and performance permit reuse.',
          'Additional fraction-resolved assay pays only if it raises safe usable powder beyond current best practice.',
          'Carry recovered powder chemistry and size-conditioned evidence through sieve and blending decisions.',
          'NIST reports oxygen variation by powder size and explicit reuse modeling; numeric plant chemistry and reuse gain here are assumed.'))
        c.append(record(46,'Delay final machining datum until AM support stress release is resolved',
          'AM part attached to plate | Stress-relief treatment | Initial datum measured | Support paths removed | Residual stress redistributes | Free geometry remeasured | Finish allowance machined | Final tolerance accepted',[(1,4),(2,5),(3,7),(5,7)],
          ['MECHANICAL equilibrium and compatibility before/after changing constraints, nodes 1-6.', 'CONSTITUTIVE: linear spring release estimate only elastic regime, nodes 4-5.', 'ENGINEERING: machining cannot restore removed stock; collision and minimum wall constraints persist, nodes 6-8.'],
          'u=Fres/k [m] for a one-mode elastic release; Fres[N], k[N/m]. Required stock allowance a>=abs(u)+measurement margin.',
          {'Fres_N':100,'k_N_m':2e6,'parts_y':5000,'assumed_absolute_scrap_reduction':.015,'marginal_USD_part':500},
          {'release_um':100/2e6*1e6},37500,12000,80000,.015,'absolute scrap fraction reduction',
          'Process-chain finite-element stress relief/support removal plus post-release probing and finish machining, not fixed clamped datum. Distinct process from prior two-preload fixture estimation.',
          'Stress release on AM support removal and datum-aware removal are known. Whole-chain implementation overlap; frontier novelty unsupported.',
          ['https://scholarsmine.mst.edu/mec_aereng_facwork/5188/','https://patents.google.com/patent/EP3152519A1/en','https://patents.google.com/patent/US10589353B2/en'],
          'Release displacement exceeds reserved stock, inelastic warping invalidates one-mode estimate, or existing process already re-datums.',
          'Identical clamped coordinates need not imply identical free geometry after support removal.',
          'Challenge final datum establishment before the final constraint release.',
          'Release-aware planning pays only for additional avoided scrap after paying probing, stock and machining cost.',
          'Reserve finishing allowance and re-establish the datum after planned support release, using validated process-chain mechanics.',
          'Experiment documents stress and distortion changes after removal; patent models distortion and another provides AM removal datum structures.',status='OVERLAP'))
        c.append(record(47,'Separate tramp-oil signal before coolant concentrate replenishment',
          'Coolant emulsified | Cutting consumes and evaporates fluid | Hydraulic oil leaks into sump | Refractometer sample read | Tramp oil separately estimated | Concentrate and water dosed | Tool life and finish accepted',[(2,4),(3,6),(5,7)],
          ['EXACT component inventory: water, formulated coolant and tramp oil tracked separately, nodes 1-6.', 'MEASUREMENT model: R=a*c+b*t not a universal calibration, nodes 4-5.', 'ENGINEERING: concentration, microbial/pH and tool finish limits remain, node 7.'],
          'R=a*c+b*t; corrected c=(R-b*t)/a. R and c,t expressed in consistent calibrated percentage points; b and a dimensionless empirical sensitivities.',
          {'R_pct':6,'a':1,'tramp_pct':2,'b':.5,'annual_makeup_L':1000000,'additional_concentrate_cost_USD_y':None,'concentrate_USD_L':5},
          {'corrected_concentration_pct':(6-.5*2),'control_direction':'Positive tramp-oil bias makes actual formulation lower than indicated; correction toward the same target requires more concentrate, not less.'},None,5000,30000,1,'USD/year of independently demonstrated avoided quality or replacement loss',
          'Supplier titration/separation confirmation, skimming and calibrated coolant management; not raw Brix alone. Direction of dosing benefit depends on site errors.',
          'Tramp-oil interference and routine separation are known; particular dual calibration unvalidated. Independent review rejected the assumed $25,000 concentrate-saving gross because the displayed positive optical bias implies correction adds concentrate. Avoided quality or replacement loss remains UNKNOWN.',
          ['https://blaser.com/measuring-the-coolant-concentration/','https://blaser.com/cutting-and-grinding-fluid-tests-what-needs-to-be-considered-in-cutting-and-grinding-fluid-management/'],
          'Two-sensor model is not identifiable, or avoided quality/replacement loss fails to exceed annual sensor costs plus additional concentrate cost. No positive direct concentrate-saving claim survives.',
          'Same optical reading can represent formulated lubricant or contaminant oil with different cutting performance.',
          'Challenge replacing all coolant solely because a blurred optical line appears, while preserving chemistry and hygiene.',
          'Separating signals is useful only when avoided quality/replacement loss exceeds $9,470.88/year plus any additional concentrate cost; neither avoided loss nor added formulation cost has been measured.',
          'Confirm true formulation concentration with independent separation/titration before automated dosing; remove leak source.',
          'Blaser describes diffuse refractometer lines under unstable emulsion or tramp oil and formulation-specific factors; no dollar benefit is sourced.',status='OVERLAP'))
        c.append(record(48,'Release sealed solder paste only when both temperature and condensation bounds hold',
          'Paste jar refrigerated | Sealed jar scheduled for warming | Exterior warms | Paste core and rheology equilibrate | Jar opened in room humidity | Paste transferred through stencil | Deposit volume and solder quality inspected',[(2,4),(3,5),(4,6),(5,7)],
          ['ENERGY balance in jar and paste, nodes 2-4; lumped model only if justified.', 'PHASE boundary: exposed surface temperature must exceed local dewpoint with margin, nodes 3-5.', 'ENGINEERING: supplier conditioning and rheology/storage restrictions still apply, nodes 4-7.'],
          'Tcore=Tamb-(Tamb-T0)*exp(-t/tau); tmin=tau*ln((Tamb-T0)/(Tamb-Tqualified)) [min]. Dewpoint alone is insufficient for printing qualification.',
          {'Tamb_C':25,'T0_C':5,'Tqualified_C':20,'tau_min':30,'jars_y':4000,'kg_jar':.5,'assumed_absolute_discard_reduction':.02,'paste_USD_kg':80},
          {'thermal_screen_min':30*math.log(4)},3200,1000,6000,.02,'absolute paste discard fraction reduction',
          'Supplier sealed warmup and validated conditioning workflow; actual thermometry cannot override material instructions.',
          'Sealed warmup and condensation prevention directly known. Narrow earlier release by core measurement remains unvalidated and no novelty demonstrated.',
          ['https://www.indium.com/blog/stencil-printing-for-success-solder-paste-handling-and-storage/','https://documents.indium.com/qdynamo/download.php?docid=2703'],
          'Core rheology/deposit repeatability is unacceptable despite dewpoint pass; no discard reduction versus scheduled standard handling.',
          'Equal exterior temperature can conceal different core temperature and viscosity.',
          'Challenge arbitrary extra waiting only after all supplier thermal/rheological limits are met.',
          'Sensor information must reduce actual discard; it does not justify valuing every waiting hour as production.',
          'Use sealed, scheduled conditioning with core-temperature evidence and qualified stencil transfer acceptance.',
          'Indium handling instructions directly require sealed warming and discuss condensation; no proof of 41.6-minute release or 2% discard reduction.',status='OVERLAP'))
        water_saved_t=200000*(1/.45-1/.46)
        c.append(record(49,'Close press-felt water inventory through nip, suction box and next nip',
          'Wet web enters press | Felt accepts expressed water | Nip exit separates web | Felt retains liquid | Suction box conditions felt | Felt returns to next nip | Dryer evaporates residual web water | Sheet quality accepted',[(2,4),(3,7),(5,7),(6,1)],
          ['EXACT water balance across web, felt and drainage, nodes 1-7.', 'CONSTITUTIVE: capillary rewetting and felt permeability depend on age/compaction, nodes 2-6.', 'ENGINEERING: web crush, profile, vibration and sheet strength constraints cannot be traded away.'],
          'Delta_water=Qdry*(1/xold-1/xnew) [t/y]; x=dry-solids mass fraction. Fuel saving=Delta_water*h_evap/eta [GJ/y]. No double credit for steam and fuel.',
          {'dry_paper_t_y':200000,'xold':.45,'xnew_target':.46,'effective_evap_GJ_t':2.6,'steam_system_eta':.85,'fuel_USD_GJ':8},
          {'water_evaporation_avoided_t_y':water_saved_t},water_saved_t*2.6/.85*8,50000,600000,.01,'absolute press-exit solids fraction gain',
          'Moisture/permeability-profile controlled press fabric conditioning and nip/Uhle optimization already sold commercially.',
          'Whole felt water pathway and rewetting are established. Proposed inventory-aware setting is an adoption hypothesis.',
          ['https://www.valmet.com/insights/articles/up-and-running/performance/FRPressFabMon/','https://www.valmet.com/insights/articles/all-articles/save-costs-by-optimizing-water-removal/'],
          'Extra suction energy or press damage exceeds steam savings, or gain vanishes at equal paper quality and speed.',
          'Same suction pressure does not identify felt saturation/permeability or next-nip capacity.',
          'Challenge maximum continuous suction as necessary for minimum dryer duty.',
          'Felt-state measurement pays only for additional net dewatering improvement over present profile controls.',
          'Schedule suction and conditioning from measured felt water/permeability, preserve next-nip and final-sheet constraints.',
          'Valmet describes the complete nip/felt/Uhle paths, moisture scans and rewetting prevention; 45-to-46% solids is an assumed target.'))
        c.append(record(50,'Meter coated-broke release against wet-end charge demand capacity',
          'Coated broke repulped | Dissolved anionic load released | Broke tank blended | Wet-end cationic additive dosed | Fibers fines and binder associate | Forming wire retains solids | Whitewater recirculates | Strength and deposits checked',[(1,3),(2,4),(3,5),(7,4)],
          ['EXACT polymer, fines and ion inventories include whitewater recirculation, nodes 1-7.', 'CONSTITUTIVE: effective charge demand is an assay-dependent empirical property, nodes 2-5.', 'ENGINEERING: retention, strength and pitch deposition limits persist through scheduled feed.'],
          'Charge-load rate J=q_b*c_b [equivalent/h]; required polymer mdot=J/(z*eta_bind) [kg/h], z[equivalent/kg]. Mixing/adsorption kinetics make instantaneous equality insufficient.',
          {'paper_t_y':150000,'assumed_additive_kg_saved_t':.2,'additive_USD_kg':3,'example_J_eq_h':20,'z_eq_kg':5,'eta_bind':.8},
          {'polymer_equivalent_requirement_kg_h':20/(5*.8)},90000,15000,120000,.2,'kg additive avoided per tonne accepted paper',
          'Feed-forward charge-demand control, isolated broke pretreatment and established coated-broke coagulant/retention systems. Compare the best complete wet-end control.',
          'Coated-broke charge and treatment overlap directly with published processes; narrow scheduling implementation unresolved, not a novel scientific relation.',
          ['https://patents.google.com/patent/WO2001063050A1/en','https://patents.google.com/patent/EP2157237A1/en'],
          'Lower dosing or pulsed broke release violates retention/strength/deposit thresholds; tank inventory shifted to next period rather than reduced.',
          'Same tonnes of broke conceal different soluble charge demand and delayed whitewater return.',
          'Challenge fixed maximum coagulant dose if staged known-demand feed can meet the same retained-paper specification.',
          'Useful upstream assay must change a feed/dose decision beyond existing charge control and pay for itself.',
          'Carry assayed broke charge and recirculating demand into a bounded release/dose schedule.',
          'Patents cover coated-broke pretreatment, polyelectrolyte interactions and raw-material-specific cationic addition; exact dynamic schedule was not established by this bounded search.',status='OVERLAP'))
        c.append(record(51,'Balance liner moisture strain before corrugator bond locks warp',
          'Liner rolls unwrapped | Preheaters add heat | Moisture and tension profiles differ | Adhesive applied | Double facer bonds layers | Board cools and equilibrates | Cross-direction warp measured',[(1,3),(2,4),(3,5),(3,6),(5,7)],
          ['EXACT heat/water balances across each liner, nodes 1-6.', 'CONSTITUTIVE: curvature responds to differential free strain and laminate stiffness, nodes 3-7.', 'ENGINEERING: bond gelatinization, crush resistance, moisture and tensile strength bounds remain.'],
          'Screen kappa≈Delta_epsilon/h [1/m], Delta_epsilon=beta*Delta_m+Delta_alpha*DeltaT; beta[1/(kg/kg)], h[m]. Full orthotropic laminate model required for prediction.',
          {'Delta_epsilon':.001,'h_m':.003,'area_m2_y':80000000,'assumed_absolute_reject_reduction':.005,'marginal_USD_m2':.35},
          {'curvature_screen_per_m':.001/.003},140000,15000,150000,.005,'absolute rejected area fraction reduction',
          'BHS Warp Control System with moisture/temperature/tension control and HydroBar; screen versus manual settings only.',
          'Commercial multi-state warp control already preserves central interface; no incremental Garden effect shown.',
          ['https://www.bhs-world.com/en/corrugators/corrugated-4','https://www.bhs-world.com/en/corrugators/individual-machines/preheater'],
          'Predicted flattening breaks bond quality, transfers warp downstream, or performs no better than existing WCS.',
          'Same bulk board temperature can hide opposing liner moisture strains.',
          'Challenge equal heating of both liners as necessary for flat board.',
          'Per-liner state matters only if it enables a lower-cost qualified moisture/heat/tension action.',
          'Use liner-specific moisture-strain estimates to qualify wet-end settings before the bond fixes relative length.',
          'BHS explicitly markets wet-end temperature warp control and correction for across-width moisture inhomogeneity.'))
        c.append(record(52,'Carry residual-solvent state from gravure dryer through cooling and winding',
          'Ink deposited on web | Solvent evaporates in dryer | Web leaves with residual solvent | Vapor boundary layer follows web | Chill roll contacts web | Winding traps layers | Blocking and residual-solvent acceptance',[(2,4),(3,5),(3,6),(5,7)],
          ['EXACT solvent inventory in ink, exhaust, web and recovered liquid, nodes 1-7.', 'CONSTITUTIVE: diffusion/desorption and vapor-boundary transport are distinct, nodes 2-5.', 'ENGINEERING: solvent exposure, flammability, coating quality and final residual limits remain binding.'],
          'A first-mode residual fraction r=exp(-k*t), k[1/s], t[s]; required dwell ln(rin/rlim)/k. Winding closure changes boundary condition and cannot inherit a free-web k blindly.',
          {'k_per_s':.1,'rin':1,'rlim':.01,'area_m2_y':30000000,'assumed_absolute_block_reject_reduction':.003,'marginal_USD_m2':.6,'incremental_energy_USD_y':20000},
          {'open_web_dwell_s':math.log(100)/.1},54000,25000,100000,.003,'absolute rejected area fraction reduction',
          'Modern residual-solvent-aware drying plus boundary-layer extraction and controlled chilling/winding. Match line speed, coating and finished limits.',
          'Patents already connect residual solvent, downstream boundary layer, chilling and blocking. No novel mechanism.',
          ['https://patents.google.com/patent/US4462169A/en','https://patents.google.com/patent/US20250001769A1/en'],
          'Intervention meets outlet temperature but increases retained solvent after winding or costs exceed avoided marginal rejects.',
          'Same dryer exit temperature can hide different residual solvent and downstream vapor boundary layer.',
          'Challenge more dryer heat as the only way to prevent winding block when downstream vapor extraction is the limiting interface.',
          'The extra measurement/action is valuable only compared with solvent-aware dryer and chill-roll control.',
          'Qualify extraction/chilling/winding using residual-solvent and boundary-layer state, not web temperature alone.',
          '1984 patent discusses vapor-layer condensation at chill rolls and blocking; 2025 filing relates residual-solvent level to winding blocking.'))
        heat=20000*1000*4.18*30/3600/.85*.04
        c.append(record(53,'End reactive-dye rinsing only after dye and salt constraints both clear',
          'Dye fixation ends | Hydrolyzed dye remains on fibers | Bath drained with retained liquor | Fresh rinse contacts fabric | Dye desorbs and salt dissolves | Color and conductivity sampled | Fastness and final salt accepted',[(2,5),(3,5),(5,7),(6,4)],
          ['EXACT separate dye and salt species balances, nodes 1-7.', 'CONSTITUTIVE: dye desorption and salt mixing have different rates, nodes 4-5.', 'ENGINEERING: fastness, shade and final chemical residues preserved; color alone is insufficient.'],
          'Ideal dilution after n exchanges: cj,n=cj,0*(Vr/(Vr+Vadd))^n; j indexes species. Bound dye additionally by measured fabric desorption; no equivalence from conductivity alone.',
          {'batches_y':1000,'assumed_water_saved_m3_batch':20,'water_plus_treatment_USD_m3':3,'heated_fraction':1,'deltaT_K':30,'heat_eta':.85,'fuel_USD_kWh':.04,'Vr_L':1000,'Vadd_L':4000},
          {'ideal_solute_fraction_after_3_exchanges':(.2)**3,'heat_cost_avoided_USD_y':heat},60000+heat,8000,100000,20,'m3 qualified rinse water avoided per batch',
          'Color/conductivity endpoint washing, countercurrent rinsing and supplier fastness tests; not fixed rinse count.',
          'Color-based dye-machine rinse termination already patented; multi-species quality control is known. Exact site saving unmeasured.',
          ['https://patents.google.com/patent/WO2014179930A1/en','https://patents.google.com/patent/US9689101B2/en'],
          'Fabric releases dye during later washing despite clear bath, conductivity misses nonionic contaminants, or energy was never purchased.',
          'Same conductivity can hide different hydrolyzed dye, and same color can hide different salt.',
          'Challenge a fixed rinse count while requiring both chemical endpoints and fabric fastness.',
          'Two signals pay only if they safely shorten a rinse relative to strongest existing endpoint control.',
          'Bind optical and ionic endpoints to fabric fastness; independently qualify lower water exchange and same delivered textile.',
          'Patent explicitly ends dye-machine rinse from measured RGB indices; second patent covers optical or conductivity dye sensing.'))
        c.append(record(54,'Express concentrated mercerization liquor before dilution, retaining fabric tension',
          'Cotton absorbs caustic under tension | Reaction dwell completes | Concentrated liquor mechanically expressed | Fabric remains dimensionally restrained | Countercurrent washing dilutes remaining liquor | Recovery evaporator concentrates weak liquor | Neutralized fabric accepted',[(1,4),(3,6),(4,7),(5,7)],
          ['EXACT caustic and water balances through return and evaporation, nodes 1-6.', 'ENGINEERING: mercerization dwell, tension, dimensional and alkali limits remain, nodes 1-7.', 'ECONOMIC: only caustic otherwise lost is incremental when baseline already recovers most.'],
          'Delta_solution=Qfabric*(pold-pnew) [kg/y]; avoided chemical loss=Delta_solution*cNaOH*(1-rbaseline). Avoided evaporation is UNKNOWN without a washwater/feed/product concentration ledger; water carried with recovered caustic is not automatically evaporated.',
          {'fabric_kg_y':10000000,'pold':.8,'pnew':.65,'cNaOH':.25,'baseline_recovery_fraction':.9,'caustic_USD_kg':.5,'water_evap_MJ_kg':2.4,'eta':.8,'fuel_USD_GJ':8},
          {'solution_kg_y':1500000,'incremental_caustic_kg_y':37500,'evap_water_kg_y':None},18750,10000,100000,.15,'kg solution expressed additionally per kg fabric',
          'Modern tension-controlled mercerizer squeeze, countercurrent washing and caustic recovery; full caustic value cannot be credited again.',
          'Concentrated expression and caustic recovery established; no new chemistry or machine principle. Independent review rejected a $27,000 evaporation credit because equal final concentration and unchanged washwater do not support it; corrected net is negative.',
          ['https://patents.google.com/patent/WO2014020503A1/en','https://patents.google.com/patent/EP0052302A1/en','https://benningergroup.com/fileadmin/user_upload/Textile_Finishing/Mercerizing_Solutions/Broschuere_Mercerizing_EN_2024.pdf'],
          'Extra nip changes fabric dimensions/luster or expressed caustic cannot be returned; evaporator baseline must use real marginal duty.',
          'Same total recovered caustic can hide large differences in dilution water and evaporation duty.',
          'Challenge dilution before all mechanically removable concentrated liquor has been recovered.',
          'Additional expression pays only for incremental losses and evaporator duty beyond current recovery.',
          'Preserve dwell and tension while reducing liquor carryover into the dilution/recovery interface.',
          'WO2014020503 describes known squeezing of excess solution before further washing; EP0052302 expressly recovers strong lye without washwater dilution. Benninger brochure search excerpt supports integrated washing/recovery, but full-PDF retrieval timed out. No vendor savings claim used.',status='REJECTED'))
        c.append(record(55,'Drain electroplating racks over the mother bath before rinse transfer',
          'Rack plates in process bath | Rack withdrawn | Liquid film and pockets drain | Angled rack held over bath | Residual dragout enters rinse | Rinse and wastewater treated | Coating quality accepted',[(1,3),(2,4),(3,5),(4,7)],
          ['EXACT bath-chemical mass balance through dragout, return and rinse, nodes 1-6.', 'CONSTITUTIVE: draining film h depends on withdrawal speed, viscosity and geometry, nodes 2-4.', 'ENGINEERING: extra dwell must not stain, oxidize or lose bottleneck output, nodes 4-7.'],
          'Chemical saving=N*(Vold-Vnew)*c*p [USD/y]; N[racks/y], V[L/rack], c[kg/L], p[USD/kg]. Add separately marginal treatment cost per L, subtract added bottleneck dwell.',
          {'racks_y':100000,'Vold_L':.5,'Vnew_L':.35,'c_kg_L':.2,'chemical_USD_kg':3,'marginal_treatment_USD_L':2,'extra_dwell_s':5,'bottleneck_USD_h':40},
          {'dragout_L_y_avoided':15000,'chemical_kg_y_avoided':3000},39000,5000+100000*5/3600*40,40000,.15,'L dragout avoided per rack',
          'EPA-documented slow withdrawal, angled orientation and drain boards already standard pollution prevention; use same throughput and finish.',
          'Direct longstanding prior art, not a novel idea.',
          ['https://www.epa.gov/sites/default/files/2013-12/documents/pwb_pollution_prevention_control_survey_results.pdf','https://nepis.epa.gov/Exe/ZyPURL.cgi?Dockey=20000VPB.TXT'],
          'Drain dwell causes surface defects or lost contribution larger than solution savings; actual treatment marginal cost may be near zero.',
          'Same rack area conceals trapped pockets and orientation-dependent retained solution.',
          'Challenge immediate transfer to rinse as necessary for finish quality; validate maximum safe dwell.',
          'Geometry-aware dwell pays only when real dragout reduction exceeds dwell opportunity cost.',
          'Select draining orientation and dwell with explicit finish/throughput bounds before fresh rinse dilution.',
          'EPA reports angular rack orientation, slow withdrawal and drainage as dragout-reduction methods; no current legal limit inferred.'))
        c.append(record(56,'Bind wafer rinse endpoint to in-feature residues rather than only bulk outlet purity',
          'Patterned wafer leaves chemical clean | Ultrapure water supplied | Bulk bath contamination flushes | Deep-feature residue desorbs | In-feature surrogate sensor responds | Rinse stops and drying begins | Electrical and surface acceptance',[(1,4),(3,5),(4,6),(5,7)],
          ['EXACT ion inventory in bulk plus adsorbed/feature compartments, nodes 1-6.', 'CONSTITUTIVE: desorption and diffusion limitations are surface-specific, nodes 3-5.', 'ENGINEERING: corrosion, charging, particles and surface residue bounds persist, nodes 6-7.'],
          'Mfeature(t)=M0*exp(-kd*t); kd[1/s]. Bulk c≈kd*Mfeature/q if quasisteady, so increasing q lowers measured outlet concentration without proportionally clearing feature inventory.',
          {'M0_ug':100,'kd_per_s':.01,'q_L_s':1,'t_s':60,'batches_y':20000,'flow_L_min':20,'assumed_minutes_avoided':2,'UPW_marginal_USD_m3':8},
          {'feature_remaining_ug_after60s':100*math.exp(-.6),'bulk_concentration_ug_L':.01*100*math.exp(-.6)},6400,5000,75000,2,'minutes of qualified rinse avoided per batch',
          'Published electrochemical residue sensors in patterned microfeatures optimize rinse flow/temperature/time; compare same surface and device quality.',
          'Exact core distinction and sensor approach covered by US8120368B2. Present water-only economics negative.',
          ['https://patents.google.com/patent/US8120368B2/en'],
          'Surrogate feature is unrepresentative or endpoint leaves residue; water savings cannot fund assumed instrumentation.',
          'Identical outlet resistivity can accompany different deeply retained residue after changes of rinse flow.',
          'Challenge long fixed rinse only after the physically relevant surface endpoint is validated.',
          'Added surface observability must produce incremental avoided water or yield beyond established endpoint methods.',
          'Qualify surface-representative endpoint before stopping rinse, preserving corrosion and electrostatic constraints.',
          'Patent explicitly measures microfeature residues, rinse endpoint and low-resource flow/temperature selection.',status='REJECTED'))
        c.append(record(57,'Vent cold vacuum workpieces only inside a qualified dewpoint transfer envelope',
          'Workpiece cooled in vacuum | Loadlock isolated | Dry vent gas introduced | Workpiece warms and moisture mixes | Door approaches ambient boundary | Workpiece transferred | Surface contamination accepted',[(1,4),(3,5),(4,6),(5,7)],
          ['EXACT water-vapor mixing and heat balance, nodes 1-5.', 'PHASE constraint: local surface T exceeds local dewpoint with margin whenever exposed, nodes 4-6.', 'ENGINEERING: vent particles, static charge, mechanical stress and downstream temperature preserved.'],
          'For well-mixed purge moisture y=y0*exp(-n), n=Qt/V. Surface acceptance requires psat(Tsurface)>y*P, not only a low source-gas dewpoint.',
          {'initial_water_ppm':10000,'target_water_ppm':100,'purge_volume_changes':math.log(100),'cycles_y':100000,'assumed_safe_seconds_avoided':10,'bottleneck_marginal_USD_h':150},
          {'required_ideal_volume_changes':math.log(100)},100000*10/3600*150,10000,100000,10,'seconds of qualified transfer wait avoided per cycle',
          'Active dewpoint sensing and loadlock vent/warming controls already patented; need full humidity/temperature/mixing and particle limits.',
          'Exact active dewpoint gating is published; no novel relationship.',
          ['https://patents.google.com/patent/US20110291030A1/en','https://patents.google.com/patent/US6750155B2/en'],
          'Local cold spot condenses despite mixed sensor, purge introduces particles, or throughput was not constrained by wait.',
          'Same loadlock pressure and source-gas specification can hide different coldest-surface moisture exposure.',
          'Challenge fixed long warmup when a measured dry transfer envelope already permits release.',
          'State knowledge pays only through additional safe throughput relative to active conventional gating.',
          'Transfer within qualified local dewpoint margin and thermal state, retaining dry-gas protection through door opening.',
          'US20110291030 directly concerns active dewpoint sensing and cold-workpiece vent/transfer; older patent controls condensation with nitrogen placement.'))
        c.append(record(58,'Balance component line pressure before adhesive dispensing restarts',
          'A and B metering pumps stop | Elastic lines retain different pressure | Idle viscosity and cure evolve | Dispense valves reopen | Component transient reaches mixer | Off-ratio material diverted | Bond cured and tested',[(1,3),(2,4),(3,5),(4,6),(5,7)],
          ['EXACT separate component mass inventory includes elastic line storage and diverted material, nodes 1-6.', 'CONSTITUTIVE: first-order hydraulic response is a linear approximation, nodes 2-5.', 'ENGINEERING: local mix ratio, pot life, mixer quality and bonded strength preserved, nodes 5-7.'],
          'qj=qj_inf*(1-exp(-t/tauj)); integral_0^T qj dt=qj_inf*(T-tauj*(1-exp(-T/tauj))). q in g/s, t in s, integral in g. Equal pump set ratios do not fix local transient ratio.',
          {'qA_inf_g_s':2,'qB_inf_g_s':1,'tauA_s':.2,'tauB_s':1,'starts_y':100000,'assumed_purge_reduction_g_start':1.5,'material_USD_kg':20},
          {'deep_test':'See deep_tests(): ratio, null and strong pressure-prebalance comparator.'},3000,3000,50000,1.5,'g qualified purge reduction per restart',
          'Known off-pressure/viscosity compensation and compressibility balancing of two-component systems; same bond ratio and pot life.',
          'Direct prior art covers precisely ratio transients after reopening and compliance; present material-only economics negative.',
          ['https://patents.google.com/patent/EP0494453B1/en','https://patents.google.com/patent/US5332125A/en','https://patents.google.com/patent/US5027981A/en'],
          'Pressure prebalance does not preserve local ratio or mixed age; even assumed purge gain fails annualized cost screen.',
          'Identical metering pump command ratio can produce different first-shot ratio because line storage differs.',
          'Challenge a fixed large purge when prebalanced hydraulic state can deliver qualified ratio sooner.',
          'Extra pressure sensing/control pays only for incremental accepted-bond cost beyond established compensation.',
          'Qualify component pressures/idle state before restart and divert until local mix is within bounds.',
          'EP0494453 and US5332125 explicitly target transient ratio errors on restart; US5027981 covers component compressibility balance.',status='REJECTED'))
        c.append(record(59,'Close composite resin bleed inventory into final fiber fraction and void limits',
          'Prepreg layup and resin mass recorded | Bag breather and bleeder assembled | Heat reduces resin viscosity | Pressure compacts fiber bed | Resin exits into bleeder | Gelation freezes geometry | Fiber fraction voids and thickness accepted',[(1,4),(2,5),(3,5),(4,6),(5,7)],
          ['EXACT resin and fiber mass/volume balances including bleed and volatiles, nodes 1-7.', 'CONSTITUTIVE: Darcy flow and cure-dependent viscosity, nodes 3-5.', 'ENGINEERING: final fiber fraction, void content, cure and thickness all constrained, nodes 6-7.'],
          'Vf=(mf/rhof)/(mf/rhof+(mr0-mbleed)/rhor) for zero voids; masses[kg], densities[kg/m3]. Allowing voids adds Vvoid to denominator; high Vf alone is not success.',
          {'mf_kg':6,'mr0_kg':4,'mbleed_kg':1,'rhof_kg_m3':1800,'rhor_kg_m3':1200,'laminate_kg_y':10000,'assumed_resin_kg_saved_kg_laminate':.03,'resin_USD_kg':60},
          {'zero_void_fiber_volume_fraction':(6/1800)/(6/1800+3/1200)},18000,10000,150000,.03,'kg resin saved per kg accepted laminate',
          'Coupled cure, resin flow, bleeder and fiber-compaction models such as NASA/COMPRO plus inspection; not temperature-only cure control.',
          'Integrated resin bleed/fiber fraction modeling is established since at least 1985; no new invariant. Declared resin-only economics negative.',
          ['https://ntrs.nasa.gov/citations/19860006800','https://ntrs.nasa.gov/citations/20160012030'],
          'Reducing bleed raises voids or shifts fiber fraction/thickness out of bounds; fiber fraction gain cannot excuse porosity.',
          'Same cure temperature/pressure can leave different resin loss and thickness when bleeder or permeability changes.',
          'Challenge a fixed excess-resin allowance only with full mass balance and property acceptance.',
          'Bleed-state measurement needs incremental accepted-material savings beyond coupled conventional models.',
          'Bind bleeder inventory and permeability to cure/compaction schedule before attempting less resin or shorter process.',
          'NASA models explicitly include laminate/bleeder/breather resin flow, fiber compaction and final fiber volume fraction.',status='REJECTED'))
        c.append(record(60,'Keep laminate deairing channels open until trapped gas meets the seal criterion',
          'Glass and conditioned PVB stacked | Vacuum ring establishes exhaust path | Air flows along embossed interface | Heat softens PVB channels | Edge seal progresses | Autoclave pressure bonds plies | Bubbles adhesion and optical quality accepted',[(1,3),(2,5),(3,5),(4,6),(5,7)],
          ['EXACT gas inventory and exhaust balance before seal, nodes 1-5.', 'CONSTITUTIVE: pneumatic conductance depends strongly on channel geometry/temperature, nodes 3-4.', 'ENGINEERING: interlayer moisture, adhesion, edge seal, optical and bubble limits persist, nodes 5-7.'],
          'dn/dt=-k(t)*n with k=C(t)/V [1/s]. Residual n/n0=exp(-integral k dt); a sealed edge makes C≈0 and freezes residual inventory in this ideal model.',
          {'k_before_seal_per_s':.05,'weak_early_seal_s':30,'qualified_target_fraction':.01,'panels_y':100000,'assumed_absolute_reject_reduction':.004,'marginal_USD_panel':150,'extra_deair_s_per_100panel_batch':math.log(100)/.05-30,'bottleneck_USD_h':100},
          {'fraction_at_early_seal':math.exp(-.05*30),'ideal_target_time_s':math.log(100)/.05,'deep_test':'See deep_tests(): conductance loss, null and strong baseline.'},60000,5000+100000/100*(math.log(100)/.05-30)/3600*100,80000,.004,'absolute rejected panel fraction reduction',
          'Supplier-qualified deairing before edge sealing plus temperature/vacuum control and known no-autoclave deair/heat/seal sequences.',
          'Sequence and mechanism directly known; simple conductance model does not establish a new control method. Financial dwell is tied to the modeled 62.1034-second extension rather than a rounded 60 seconds.',
          ['https://www.trosifol.com/fileadmin/user_upload/tools/downloads/technical_information/kuraray-technical-manual-architecture-web.pdf','https://patents.google.com/patent/US5536347A/en'],
          'Seal occurs before gas target, dissolved water creates bubbles despite gas removal, or adhesion/optical quality fails; existing baseline already closes interface.',
          'Same final vacuum reading can conceal trapped gas when interface channels have sealed.',
          'Challenge heating immediately to bonding temperature before sufficient deairing.',
          'Gas/temperature tracking is worth paying for only if it beats the already qualified deair/seal recipe at equal quality.',
          'Carry interfacial conductance and remaining gas into the heating/seal decision; preserve interlayer conditioning.',
          'Kuraray warns trapped interfacial air can cause later defects; US5536347 expressly deairs then heats to seal edges.'))
        c[6]['financial']['required_avoided_loss_usd_y_excluding_unknown_additional_concentrate']=5000+CRF*30000
        c[6]['financial']['break_even_note']='Avoided quality/replacement loss must exceed this threshold PLUS any additional concentrate cost; benefit and added concentrate cost UNKNOWN.'
        # Exact nonlinear break-even for the press-solids response, holding all
        # other assumptions fixed; linearizing in solids fraction would bias it.
        press=c[8]
        annual=press['financial']['opex']+CRF*press['financial']['capex']
        needed_water=annual/(2.6/.85*8)
        xbreak=1/(1/.45-needed_water/200000)
        press['financial']['break_even']=xbreak-.45
        assert len(c)==20 and len({x['id'] for x in c})==20
        for x in c:
            assert 5<=len(x['nodes'])<=9
            assert len(set(x['edges']))==len(x['edges'])
            assert all(1<=a<=len(x['nodes']) and 1<=b<=len(x['nodes']) and a!=b for a,b in x['edges'])
            assert x['sources'] and set(x['operators'])=={'Projection-Loss','Necessity-Challenge','Decision-Sufficiency'}
        return c


    def deep_tests():
        # N058: distinct hydraulic time constants; composition is delivered mass,
        # not the metering-pump command. No reaction or mixing quality is inferred.
        def mass(q,tau,t):return q*(t-tau*(-math.expm1(-t/tau)))
        ma,mb=mass(2,.2,1),mass(1,1,1)
        ratio=ma/mb
        # Same time constants is a true physical null for transient ratio error.
        null=mass(2,.2,1)/mass(1,.2,1)
        # Established pressure/compressibility balancing gives same response times.
        strong=mass(2,.2,1)/mass(1,.2,1)
        candidate=strong
        # At steady state finite shot average approaches desired ratio.
        longratio=mass(2,.2,10000)/mass(1,1,10000)
        assert ratio>4 and abs(null-2)<1e-12 and candidate==strong
        assert abs(longratio-2)<.001
        # Mass reconciliation is analytic and checked against trapezoid integration.
        n=20000; dt=1/n
        na=sum((2*(1-math.exp(-(i*dt)/.2))+2*(1-math.exp(-((i+1)*dt)/.2)))*dt/2 for i in range(n))
        nb=sum(((1-math.exp(-i*dt))+(1-math.exp(-(i+1)*dt)))*dt/2 for i in range(n))
        assert abs(na-ma)<1e-7 and abs(nb-mb)<1e-7
        # N060: pressure at pump can remain low after channels shut, yet gas remains.
        k=.05; target=.01
        early=math.exp(-k*30)
        required=math.log(1/target)/k
        delayed=math.exp(-k*required)
        known=math.exp(-k*required)
        zero_conductance=math.exp(0)
        assert early>.22 and abs(delayed-target)<1e-12 and delayed==known
        assert zero_conductance==1
        # Counterexample: a perfect gas-removal result still says nothing about
        # independent water vapor released later from PVB.
        return {'N058':{'first_second_A_g':ma,'first_second_B_g':mb,'delivered_A_B_ratio':ratio,'target_ratio':2,'null_equal_time_constants_ratio':null,'known_prebalance_ratio':strong,'candidate_vs_known_ratio_difference':candidate-strong,'claim':'Known transient compensation ties candidate; material-only net negative.'},'N060':{'early_seal_remaining_fraction':early,'qualified_ideal_deair_seconds':required,'candidate_remaining_fraction':delayed,'known_recipe_remaining_fraction':known,'sealed_before_deair_null_fraction':zero_conductance,'claim':'Known deair-before-seal protocol ties candidate; real channel and moisture parameters unmeasured.'}}

    return run(), deep_tests()



# Source SHA256: 82dc3e9ac6348e72472db64cf5b7e926b545347b6581591f88c155980126ec66
def workstream_electricity():
    #!/usr/bin/env python3
    """N061-N080: bounded, noncanonical Garden electricity interface investigations.

    Standard library only. All prices, scales, and intervention improvements below
    are explicit scenarios, not plant data. No record is an admitted discovery.
    run() returns twenty self-contained records; detailed_tests() adds two bounded
    physical-model comparisons and null cases. This is not a complete SAL compiler.
    """
    import math
    import cmath

    CRF = .08 * 1.08**10 / (1.08**10 - 1)


    def constraint(kind, nodes, text):
        return {"type": kind, "nodes": nodes, "statement": text}


    def money(gross, opex, capex, break_even, basis):
        return dict(gross=gross, opex=opex, capex=capex,
                    annual_capital=CRF*capex,
                    net=None if gross is None else gross-opex-CRF*capex,
                    break_even=break_even, basis=basis,
                    currency="USD/facility/year", measured=False,
                    incremental_vs_strong_baseline=None)


    def record(n, title, nodes, edges, constraints, gap, operators, equation,
               inputs, prediction, financial, baseline, novelty, status, sources,
               source_scope, falsifier):
        return dict(id=f"N{n:03}", title=title, nodes=nodes, edges=edges,
                    constraints=constraints, gap=gap, operators=operators,
                    equation=equation, inputs=inputs, physical_prediction=prediction,
                    financial=financial, baseline=baseline, novelty=novelty,
                    status=status, sources=sources, source_scope=source_scope,
                    falsifier=falsifier, admission="NONCANONICAL_CANDIDATE",
                    empirical_status="NOT_TESTED", frontier_novelty="UNRESOLVED",
                    owner=f"research.N{n:03}.electricity.2026-10-09")


    def sheath_service_case(total0=2500., limit=1600., rc=.01, rs=.1,
                            k1=.05, k2=.10, voltage=10000.):
        """Two independently controlled feeder converters, same delivered real W.

        This control freedom does NOT exist in uncontrolled parallel cables.
        Identical ideal converter efficiencies are assumed, and all core/sheath
        losses are charged to input power. Voltage is an aggregate single-phase
        RMS equivalent, not a claim about an installed three-phase cable.
        """
        def loss(x,total):
            return rc*(x*x+(total-x)**2)+(k1*x-k2*(total-x))**2/rs
        def allocation(total):
            s=k1+k2
            uncon=(rc*total+s*k2*total/rs)/(2*rc+s*s/rs)
            return max(total-limit,min(limit,uncon))
        base_loss=loss(total0/2,total0)
        delivered=voltage*total0-base_loss
        lo,hi=delivered/voltage,total0
        for _ in range(90):
            total=(lo+hi)/2
            x=allocation(total)
            if voltage*total-loss(x,total)<delivered:
                lo=total
            else:
                hi=total
        total=(lo+hi)/2
        x=allocation(total)
        new_loss=loss(x,total)
        assert abs(voltage*total-new_loss-delivered)<1e-6
        assert 0<=x<=limit and 0<=total-x<=limit
        return dict(total0_A=total0,total_A=total,x_A=x,other_A=total-x,
                    delivered_W=delivered,baseline_loss_W=base_loss,
                    candidate_loss_W=new_loss,
                    saved_input_W=voltage*(total0-total),
                    voltage_V=voltage)


    def run():
        c = constraint
        out = []
        out.append(record(61, "Clipped-PV fault diagnosis with a bounded headroom probe",
          ["Photons and cell temperature", "Series cells and bypass diode", "DC operating point",
           "Inverter AC clipping", "Short diagnostic voltage sweep", "Fault diagnosis and repair", "Subsequent unclipped export"],
          [(1,2),(2,3),(3,4),(3,5),(5,6),(6,7),(1,7),(4,6),(2,7)],
          [c("EXACT",[2,3,4],"DC input equals AC output plus conversion loss and stored-energy rate."),
           c("CONSTITUTIVE",[1,2,3,5],"Qualified diode I-V model and bypass switching determine operating points."),
           c("ENGINEERING",[4,5],"Probe must preserve inverter voltage/current, grid export and thermal limits."),
           c("EVIDENCE",[1,5,6],"Clouds, irradiance error and MPPT disturbances can mimic faults."),
           c("ECONOMIC",[4,6,7],"Recoverable energy must occur outside clipping or displace a real loss; suppressed DC potential is not sold AC energy.")],
          "Clipped AC watts lose information about DC array health. Test whether a brief headroom interval adds decision value beyond existing DC-V/I diagnosis.",
          {"projection_loss":"P_ac=min(eta*P_dc,P_limit): 1.1 and 1.3 MW DC can give identical 1 MW AC.",
           "necessity_challenge":"Additional module sensors may be unnecessary if existing DC V/I and a qualified sweep identify the fault; this is already explored in published diagnosis.",
           "decision_sufficiency":"Repair only if future recoverable export and avoided damage exceed diagnosis, repair and probe costs."},
          "P_ac=min(eta*P_dc,P_limit) [W]; deltaE=integral(P_ac,repaired-P_ac,faulty)dt [Wh]. eta dimensionless. Assumes stable irradiance over probe; dynamic PV and inverter constraints remain required.",
          dict(annual_unclipped_kWh=30_000_000,additional_recoverable_fraction=.01,price=.06,probe_kWh=1000),
          dict(equal_clipped_AC_kW=1000,assumed_recovered_kWh=300_000,probe_loss_kWh=1000),
          money(300_000*.06,3000+1000*.06,20_000,(3000+60+CRF*20_000)/(.06*30_000_000),"Versus AC-only clip-blind monitoring; break-even is additional recoverable fraction of 30 GWh/year."),
          "Kohno et al. diagnosis using existing inverter DC V/I under MPPT AND clipping; full I-V sweep and thermography comparator. No demonstrated gain over these.",
          "OVERLAP: clipped-operation diagnosis and bypass fault classification already published; narrow lowest-cost probe timing unverified.","OVERLAP",
          ["https://ieeexplore.ieee.org/document/8681125/","https://eprints.whiterose.ac.uk/id/eprint/177705/"],
          "Targeted primary-paper search: IEEE 2019 abstract/search excerpt supports clipping diagnosis; direct IEEE open blocked by robot wall. Author-repository bypass-diode algorithm abstract supports I-V comparator, not this probe's superiority.",
          "Reject incremental claim if existing DC telemetry detects the same faults, if irradiance changes cause false alarms, or repair cannot increase saleable output."))
        out.append(record(62, "Bifacial PV clearing that retains useful ground snow",
          ["Snowfall on modules and ground", "Front occlusion", "Rear albedo irradiance", "Selective module clearing", "Meltwater and refreezing", "Net export and maintenance"],
          [(1,2),(1,3),(2,4),(3,6),(4,2),(4,3),(4,5),(5,2),(2,6)],
          [c("EXACT",[2,3,6],"Both faces contribute to one electrical output; front and rear credits cannot exceed measured total."),
           c("CONSTITUTIVE",[1,3],"Albedo, view factors and spectral response determine rear gain."),
           c("ENGINEERING",[4,5],"Robot load, glass abrasion, runoff icing and access limits remain unchanged."),
           c("EMPIRICAL",[2,4,5],"Snow shedding and refreezing depend on module tilt, temperature and local weather."),
           c("ECONOMIC",[3,4,6],"Incremental clearing cost is compared with retained front-plus-rear energy over the same weather sequence.")],
          "A front-only cleaning schedule can remove or dirty reflective ground snow and erase rear yield. Keep useful ground snow when access and drainage permit.",
          {"projection_loss":"Same front cover ratio, different ground albedo => different net clearing value.","necessity_challenge":"Clearing the entire ground apron is not physically necessary for every module-clearing operation; access/safety may nevertheless require it.","decision_sufficiency":"Clear when front recovery minus rear loss, refreeze loss and cost is positive."},
          "deltaE=E_front,recovered - E_rear,lost - E_refreeze [kWh]. Bidirectional irradiance and identical snow-free reference required; no universal albedo-to-energy constant.",
          dict(front_recovered_kWh=100_000,rear_loss_kWh=20_000,price=.08),
          dict(net_energy_kWh=80_000),
          money(80_000*.08,2000,20_000,(2000+CRF*20_000)/.08,"Versus no additional module clearing; break-even net recovered kWh/year. Strong snow-aware clearing is not shown inferior."),
          "Empirical bifacial snow-loss and albedo models plus selective snow-clearing optimization.",
          "OVERLAP: coupling between snow, albedo and clearing is known. Exact deployment sequence not established novel.","OVERLAP",
          ["https://digitalcommons.mtu.edu/michigantech-p/15981/","https://www.mdpi.com/2071-1050/17/14/6350"],
          "2022 primary author-repository abstract opened: hourly energy, albedo and image-derived snow data; 2025 primary modelling search explicitly excludes removal cost. Neither supplies this scenario's 100/20 MWh inputs.",
          "Reject if refreezing, access work or lost rear irradiance eliminates net recovery versus a snow-aware baseline."))
        out.append(record(63, "Dew-timed PV washing before soluble dust cements",
          ["Dust mineral deposition", "Nocturnal radiative cooling", "Dew film formation", "Solute dissolution", "Timed soft cleaning", "Drying and recrystallization", "Transmission and export"],
          [(1,3),(2,3),(3,4),(4,5),(4,6),(5,6),(6,7),(1,7),(5,7)],
          [c("EXACT",[3,4,5,6],"Water and soluble-solid masses close across runoff and drying."),
           c("CONSTITUTIVE",[1,4,6],"Mineral solubility, crystal precipitation and adhesion are material-specific."),
           c("ENGINEERING",[5,7],"Equal cleaning quality and abrasion limits; water saving cannot trade for permanent haze."),
           c("EMPIRICAL",[2,3,5],"A sufficient usable dew window is unmeasured, not a guaranteed daily resource."),
           c("ECONOMIC",[5,7],"Separate avoided water cost from incremental export; no duplicated cleaning benefit.")],
          "Exploit a measured dew-prewet interval only before cementation; a dry optical-loss metric omits the chemical state that changes cleaning work.",
          {"projection_loss":"Same optical loss can be loose dust or cemented dust with different required washing.","necessity_challenge":"Some fresh-water prewetting may be unnecessary when safe natural wetting already exists.","decision_sufficiency":"Choose dew cleaning only if saved water/labour and export exceed night operation, damage and sensing costs."},
          "Water reduction deltaW=W_baseline-W_dew [m3]; value=deltaW*cW+deltaE*cE [USD/year]. A material-specific cementation-rate model, not dew presence alone, must determine the window.",
          dict(assumed_water_saved_m3=5000,water_price=2,additional_kWh=100_000,electricity_price=.06),
          dict(conditional_water_m3=5000,conditional_energy_kWh=100_000),
          money(5000*2+100_000*.06,2000,50_000,(2000+CRF*50_000-100_000*.06)/2,"Assumed 100 MW site; versus fixed dry-time washing. Break-even water m3/year conditional on the assumed 100 MWh export gain."),
          "Site/mineral-specific soiling and humidity models, optimized robotic wet cleaning; published dew-induced cementation experiments.",
          "OVERLAP: dew can cement dust rather than help. Exact timing benefit remains untested.","OVERLAP",
          ["https://elmi.hbku.edu.qa/en/publications/comprehensive-analysis-of-soiling-and-cementation-processes-on-pv/","https://onlinelibrary.wiley.com/doi/10.1002/solr.202500792"],
          "2018 primary abstract opened: mineral-specific dew cementation and inhibition by heating. 2026 primary research search supports site-specific cleaning protocols. Neither measures this intervention's savings.",
          "Reject if wetting accelerates cementation, coating wear rises, or equal cleanliness needs equal/more water."))
        out.append(record(64, "Joint carrier-phase choice for bearing stress and circulating losses",
          ["Shared DC supply", "Parallel PWM carriers", "Phase-leg common-mode voltage", "Motor parasitic capacitance", "Shaft and bearing discharge", "Inter-inverter circulating loop", "Copper heat", "Qualified phase controller"],
          [(1,2),(2,3),(3,4),(4,5),(2,6),(6,7),(7,8),(5,8),(8,2)],
          [c("EXACT",[3,4],"Displacement current i=C*dv/dt; common-mode and differential paths are separate."),
           c("EXACT",[6,7],"Loop loss is I_rms^2 R; canceled terminal ripple does not imply zero internal loss."),
           c("CONSTITUTIVE",[4,5],"Bearing lubricant breakdown and capacitance vary with speed and temperature."),
           c("ENGINEERING",[2,8],"Current sharing, torque ripple and semiconductor ratings constrain phase choice."),
           c("ECONOMIC",[5,7,8],"Do not price a bearing-life extension without measured event-rate change.")],
          "A carrier phase that cancels common-mode voltage may increase intermodule current. Carry both burdens into the same modulation choice.",
          {"projection_loss":"Equal motor torque and output THD can hide different bearing and circulating currents.","necessity_challenge":"An added bearing-isolation component may be avoidable only if control demonstrably meets the same reliability requirement.","decision_sufficiency":"Minimum bearing current is not the minimum total-cost operating point."},
          "For two ideal carrier harmonics, |Vcm|=V*|cos(phi/2)| and |Vdiff|=2V*|sin(phi/2)| [V]; L=a*cos(phi/2)^2+b*sin(phi/2)^2 [W]. This harmonic surrogate does not predict bearing lifetime.",
          dict(assumed_loss_reduction_kW=2,hours=6000,price=.10,unmeasured_bearing_value=None),
          dict(energy_saved_kWh=12_000,phase_tradeoff="CM zero at pi while differential harmonic is maximal"),
          money(1200,500,20_000,(500+CRF*20_000)/(.1*6000),"Energy-only versus poorly phased modules; break-even measured kW reduction. Bearing value UNKNOWN."),
          "Carrier-phase common-mode/shaft-voltage suppression plus circulating-current control already published; multiobjective modulation comparator.",
          "KNOWN components; joint implementation overlap, no quantitative superiority established.","OVERLAP",
          ["https://www.mdpi.com/1996-1073/14/21/6924","https://www.mdpi.com/1996-1073/15/5/1949"],
          "Primary search abstracts: 2021 shaft voltage reduction by carrier shift; 2022 carrier-error circulating-current suppression. MDPI direct opening returned 429; no full-paper claim.",
          "Reject if reduced common-mode stress increases loop heating, torque ripple or faults; no energy advantage versus joint modulation baseline."))
        out.append(record(65, "Residual-flux uncertainty carried from opening to controlled reclosing",
          ["Loaded transformer flux", "Breaker opening", "Voltage decay measurement", "Remanent flux and uncertainty", "Closing phase selection", "First-cycle magnetization", "Protection and restored service"],
          [(1,2),(2,3),(3,4),(4,5),(5,6),(6,7),(1,4),(4,6),(7,2)],
          [c("EXACT",[1,3,4,6],"Faraday law v=N*dPhi/dt; switching retains a remanent initial condition."),
           c("CONSTITUTIVE",[4,6],"Hysteresis and saturation require qualified B-H data for current prediction."),
           c("ENGINEERING",[5,6,7],"Breaker scatter and voltage-measurement errors bound achieved closure; protection settings remain authoritative."),
           c("EVIDENCE",[3,4,5],"Instrument dead bands and lost samples create a residual-flux interval, not a measured point."),
           c("ECONOMIC",[5,7],"Reduced peak flux is not a measured reduction in trip frequency or asset damage.")],
          "Retain an interval for residual flux through deenergization; choose closing phase robust to that interval instead of assuming the core resets.",
          {"projection_loss":"Both transformers read zero terminal volts while residual flux is +0.8 or -0.8 pu; their optimal closing phases differ.","necessity_challenge":"Separate demagnetization need not be required when controlled closure is independently qualified.","decision_sufficiency":"Use residual flux only when avoided interruption/damage exceeds monitoring and breaker-control cost."},
          "Phi(t)=Phi_r+Phi_hat*(cos(theta)-cos(omega*t+theta)) [Wb]; max absolute normalized flux=1+|r+cos(theta)|. Single phase, ideal applied voltage, first cycle; current and 3-phase coupling require nonlinear EMT. theta*=acos(-r) for |r|<=1.",
          dict(r_values=[-.8,0,.8],closing_error_deg=3,residual_interval_halfwidth=.05),
          dict(fixed_quartercycle_peak_pu=1.8,perfect_control_peak_pu=1.0,robust_upper_bound_pu=1+.05+math.radians(3)),
          money(None,3000,50_000,3000+CRF*50_000,"Required additional avoided loss USD/year; no invented outage probability."),
          "Existing residual-flux-aware controlled switching, including closing-scatter and residual-measurement-uncertainty studies; nonlinear EMT comparator needed for actual current.",
          "KNOWN; replay exactly ties conventional point-on-wave physics. Dead-band implementation novelty not established.","KNOWN",
          ["https://www.ipstconf.org/papers/Proc_IPST2023/23IPST014.pdf","https://citeseerx.ist.psu.edu/document?doi=38c97aef4d8b4eab47c2a91579abc7fdf2137e5c&repid=rep1&type=pdf"],
          "2023 primary conference full text opened, equations 4-7 and laboratory apparatus; prior uncertainty-paper search identifies already-known closing scatter and residual error treatment.",
          "Reject any new-method claim if established controlled closing achieves equal flux; reject safety inference if hysteresis, voltage or breaker error exceeds the qualified envelope."))
        cap_kWh=.5*.1*(1000**2-60**2)/3_600_000
        out.append(record(66, "Recover isolated DC-link energy before maintenance discharge",
          ["Charged converter capacitor", "Source isolation", "Isolated recovery converter", "Auxiliary battery acceptance", "Verified low voltage", "Maintenance access"],
          [(1,2),(2,3),(3,4),(3,5),(5,6),(4,3),(1,5)],
          [c("EXACT",[1,3,4,5],"Capacitor energy decrease bounds all recovered energy."),
           c("ENGINEERING",[2,3,5,6],"Proven source isolation, backfeed prevention and discharge deadline remain mandatory."),
           c("ENGINEERING",[4],"Battery SOC, current and temperature must permit acceptance; fallback dissipative discharge is retained."),
           c("EVIDENCE",[5,6],"A controller status bit does not verify touch-safe voltage."),
           c("ECONOMIC",[1,4],"Only pre-existing stored energy counts; charging merely to recover energy creates no saving.")],
          "A shutdown treats DC-link energy as waste while station storage exists; recover it through a qualified isolated path, subject to an energy upper bound.",
          {"projection_loss":"Equal shutdown count hides capacitance and initial voltage, which determine available energy.","necessity_challenge":"Resistive dissipation is not the only way to achieve discharge, but recovery cannot weaken isolation.","decision_sufficiency":"Reject retrofit when even complete energy recovery cannot pay its annual cost."},
          "E_rec<=eta*C*(V_i^2-V_f^2)/2 [J]; divide by 3.6e6 for kWh. C[F], V[V], 0<=eta<=1, V_i>=V_f. Ideal fixed capacitor; parasitic and standby consumption only reduce value.",
          dict(capacitance_F=.1,initial_V=1000,final_V=60,efficiency=.8,bays=10,shutdowns_per_bay_year=1000,price=.1),
          dict(kWh_per_discharge_before_recovery=cap_kWh,recovered_kWh_year=cap_kWh*.8*10*1000),
          money(cap_kWh*.8*10*1000*.1,500,10_000,(500+CRF*10_000)/(cap_kWh*.8*.1),"Break-even total annual discharge events across the facility; energy-only upper-bound screen."),
          "Existing active-discharge/flyback conversion and regenerative DC buses. The retrieved patent supports controlled discharge, not this exact battery recovery topology.",
          "REJECTED economic screen; exact topology search inconclusive, adjacent circuitry known.","REJECTED",
          ["https://patents.google.com/patent/US9656556B2/en","https://www.astesj.com/v05/i02/p08/"],
          "Targeted primary patent search documents charge transfer between capacitors then inverter discharge; primary EV recovery paper documents battery acceptance limitations. Not evidence of novel station-storage recovery.",
          "The annualized hardware/standby cost exceeds the recoverable-energy upper bound for the assumed facility; a changed scale must be declared as a different scenario."))
        out.append(record(67, "Cold switchgear heating tied to gas condensation state",
          ["Ambient cold front", "Tank wall temperature", "Insulating gas mixture phase equilibrium", "Gas density and dielectric margin", "Distributed heater control", "Qualified switching readiness"],
          [(1,2),(2,3),(3,4),(4,5),(5,2),(4,6),(2,6)],
          [c("EXACT",[2,3,5],"Gas and tank energy balances include latent heat and local heat loss."),
           c("CONSTITUTIVE",[3,4],"Mixture vapor pressure and composition determine gaseous density; ideal-gas correction alone fails at condensation."),
           c("ENGINEERING",[4,5,6],"Dielectric and interrupting qualification must hold at the coldest relevant surface, not average air temperature."),
           c("EVIDENCE",[2,3],"Sensor placement and mixture identity are dependencies; missing phase data yields UNKNOWN."),
           c("ECONOMIC",[5,6],"Avoided heater electricity cannot be credited when readiness or insulation margin is reduced.")],
          "A cabinet thermostat may miss a cold internal gas surface. Use measured mixture-specific phase margin to allocate heating, preserving readiness.",
          {"projection_loss":"Same cabinet air temperature can coexist with a cold wall causing local condensation.","necessity_challenge":"Continuous full heater power might be unnecessary when local phase margin is sufficient.","decision_sufficiency":"Only qualified lower heater duty has value; no value assigned to unproven dielectric risk reduction."},
          "C_th*dT/dt=P_heater-UA*(T-T_a)+L*dm_cond/dt [W]. Boundary contains gas and tank; m_cond is accumulated condensed mass and L>0, so condensation releases latent heat and evaporation removes it. Gas-phase amount and dielectric strength require mixture data. Economic deltaE=n*P_heater*h*reduction [kWh].",
          dict(bays=50,heater_kW=.2,hours=3000,assumed_duty_reduction=.4,price=.12),
          dict(conditional_kWh_saved=12_000),
          money(12_000*.12,500,10_000,(500+CRF*10_000)/(.12*50*.2*3000),"Versus fixed winter heat; break-even heater-duty reduction fraction."),
          "Gas-condensation prevention heating with internal fluid circulation already patented; qualified local-temperature control.",
          "KNOWN broad mechanism; energy-only retrofit negative at declared scale.","KNOWN",
          ["https://patents.google.com/patent/US10999897B2/en","https://patents.google.com/patent/RU2563575C1/en"],
          "US patent full record opened; direct low-temperature insulation-fluid condensation prevention. RU patent search also describes local circulation and heating.",
          "Reject if cold spots, gas fraction or interruption performance worsen, or heater saving is below break-even."))
        out.append(record(68, "Electrolyser pressure-ramp contract across low-load operation",
          ["Variable electricity request", "Stack current", "Hydrogen and oxygen generation", "Dissolved and crossover gas", "Separator headspace inventory", "Pressure/flow adjustment", "Product compression", "Qualified delivered hydrogen"],
          [(1,2),(2,3),(3,4),(4,5),(5,6),(6,4),(6,7),(7,8),(3,8),(1,6)],
          [c("EXACT",[2,3],"Faraday stoichiometry relates charge to generated hydrogen and oxygen."),
           c("EXACT",[4,5,6],"Crossed gas accumulates and leaves via purge/outflow; concentration does not reset when current changes."),
           c("CONSTITUTIVE",[4,6],"Permeation and dissolution depend on pressure, temperature, separator and membrane chemistry."),
           c("ENGINEERING",[5,6,8],"Independently approved impurity, differential-pressure and ramp limits remain hard gates."),
           c("ECONOMIC",[6,7,8],"Extra hydrogen must include depressurization loss, recompression, wear and electricity opportunity cost.")],
          "An electrical minimum-load rule can discard safe operating windows or miss crossover accumulation. Carry gas inventories and pressure into the dispatch contract.",
          {"projection_loss":"Same current can have different headspace impurity because of prior pressure and dwell time.","necessity_challenge":"A fixed high-pressure minimum-load floor is not necessary under every qualified pressure schedule; literature already establishes this.","decision_sufficiency":"Additional operation is worthwhile only after product margin covers pressure cycling and control cost."},
          "dn_H2,cross/dt=J_cross*A-y*ndot_out [mol/s]; y=n_H2,cross/n_gas. H2 generation eta_F*I/(2F) [mol/s]; qualified pressure-dependent J required. Delivered kg=eligible_kWh/(kWh/kg), with purge/compression already netted.",
          dict(plant_MW=10,additional_full_power_equivalent_hours=200,additional_eligible_MWh=2000,specific_kWh_per_kg=55,net_margin_USD_per_kg=1),
          dict(assumed_additional_kg=2_000_000/55),
          money(2_000_000/55,10_000,100_000,(10_000+CRF*100_000)*55/1000,"Break-even additional eligible MWh/year; 2000 MWh is an unmeasured target equivalent to 200 full-power hours, NOT 200 clock hours of low-load operation. $1/kg contribution margin ASSUMED net of electricity, water, purge, compression and variable degradation."),
          "Pressure/impurity MPC for alkaline electrolysers (2021), coupled transient PEM crossover models; technology-specific comparison required.",
          "KNOWN pressure/load coupling; no additional Garden advantage. Alkaline and PEM parameters cannot be interchanged.","KNOWN",
          ["https://doi.org/10.1016/j.ijhydene.2021.08.069","https://arxiv.org/html/2501.14576v1","https://www.sciencedirect.com/science/article/pii/S0378775326014229"],
          "Primary searches identify established dynamic impurity and pressure-control strategies. 2025 multi-stack author manuscript supplies modern comparison. 2026 PEM search result is provisional metadata only; not necessary to the known-status conclusion.",
          "Reject if purity/pressure limits are violated or extra hydrogen margin disappears after recompression, purge and wear; compare on delivered hydrogen, not electrical uptake."))
        out.append(record(69, "Flow-battery standby circulation with restart and shunt closure",
          ["Charge ends", "Electrolyte retained in stack", "Crossover and shunt self-discharge", "Standby pump/washing decision", "Stack temperature", "Restart composition front", "Delivered next-cycle energy"],
          [(1,2),(2,3),(3,5),(5,4),(4,2),(4,6),(6,7),(3,7),(1,7)],
          [c("EXACT",[2,3,6,7],"Species/charge inventories close over standby and next discharge."),
           c("EXACT",[3,4,5],"Shunt heat and pump work are counted in the same energy balance."),
           c("CONSTITUTIVE",[2,3,5],"Crossover, shunt conductance and precipitation depend on temperature and SOC."),
           c("ENGINEERING",[4,5,6],"No unsafe temperature or precipitation; restart delay and demanded power preserved."),
           c("ECONOMIC",[4,7],"Reduced pump electricity and reduced stored-energy loss are distinct only with the same inventory endpoints.")],
          "Zero terminal power does not mean zero internal electrochemical loss. Schedule intermittent washing using both thermal/self-discharge and restart constraints.",
          {"projection_loss":"Same terminal zero current and tank SOC can hide a hot, self-discharged stack.","necessity_challenge":"Continuous standby pumping is not always required; exact smart intermittent washing is prior art.","decision_sufficiency":"Minimize standby plus restart energy at equal ready-power availability."},
          "deltaE=(P_pump,b-P_pump,c)*h+deltaE_selfdischarge-deltaE_restart [kWh]; dU/dt=Q_shunt+Q_cross-Q_cooling. Requires same final SOC and qualified chemistry.",
          dict(pump_baseline_kW=2,pump_candidate_kW=.4,hours=4000,assumed_selfdischarge_saved_kWh=4000,price=.1),
          dict(conditional_kWh_saved=10400),
          money(1040,500,10_000,(500+CRF*10_000)/.1,"Favorable upper bound versus continuous/fixed periodic washing: zero additional restart energy ASSUMED, although the physical contract requires measuring it. Break-even whole-cycle kWh/year. Negative even before an added restart penalty."),
          "Experimentally tested smart intermittent standby washing; validated standby model with crossover/shunt effects.",
          "KNOWN exact broad intervention; negative retrofit screen at this size.","KNOWN",
          ["https://www.sciencedirect.com/science/article/pii/S0196890420310414","https://www.sciencedirect.com/science/article/pii/S0306261919303642"],
          "Primary search abstracts explicitly report the standby strategy and experimental validation. Direct repository fetch failed; abstract-level prior art receipt.",
          "Reject if next-cycle lost energy or restart readiness offsets the apparent pump saving; no new claim against published smart standby."))
        out.append(record(70, "High-temperature sodium-sulfur standby versus scheduled reheating",
          ["End of battery dispatch", "Stored electrochemical state", "Insulated vessel heat loss", "Qualified standby temperature", "Scheduled reheat", "Thermal stress and phase state", "Restored power service"],
          [(1,2),(2,3),(3,4),(4,5),(5,6),(6,7),(2,7),(4,6),(1,5)],
          [c("EXACT",[3,4,5],"Heat saved while cooler must be netted against reheating to the same endpoint."),
           c("CONSTITUTIVE",[2,4,6],"Electrolyte conductivity, phase changes and seal stress depend on temperature."),
           c("ENGINEERING",[4,5,6,7],"OEM-approved temperatures/ramp rates and immediate reserve requirements constrain any cooldown."),
           c("EMPIRICAL",[6],"Cycle-induced damage cost is UNKNOWN without qualification; it cannot be assigned zero."),
           c("ECONOMIC",[3,5,7],"Equal reserve availability and final temperature; no borrowing stored heat as a saving.")],
          "A dispatch plan ending at zero electrical demand can still require expensive hot readiness. Compare a qualified lower-temperature interval with reheat and lost readiness.",
          {"projection_loss":"Same SOC and next-day energy schedule can hide very different thermal readiness.","necessity_challenge":"Full-temperature standby may be unnecessary during a firmly unavailable maintenance interval, but not during contracted fast reserve.","decision_sufficiency":"Cooldown duration must exceed the full reheating, wear and unavailable-service break-even."},
          "deltaE=deltaP_hold*h-E_reheat [kWh]; E_reheat includes integral(C(T)dT)+latent terms and heater losses. Simplified energy screen only; no permission to cool a real battery.",
          dict(holding_kW=25,hours=3000,assumed_heat_reduction=.3,reheat_kWh=10000,price=.12),
          dict(conditional_net_kWh=12500),
          money(1500,1000,20_000,(1000+CRF*20_000)/.12,"Break-even net kWh/year AFTER reheat; unpriced wear/availability would further reduce value."),
          "Distributed dynamic NaS thermal-electrochemical scheduling and thermal-management models.",
          "OVERLAP known thermal scheduling; negative optimistic energy screen, actual operating admissibility UNKNOWN.","REJECTED",
          ["https://www.osti.gov/servlets/purl/1977190","https://www.sciencedirect.com/science/article/pii/S2352152X24047030"],
          "Primary paper searches show distributed and lumped coupled thermal-electrical models. OSTI full-text fetch returned 502; no model-parameter extraction claimed.",
          "Reject if approved lower-temperature state does not exist, reheat/thermal wear erases savings, or equal reserve response cannot be maintained."))
        out.append(record(71, "HVDC polarity reversal qualified by residual space charge",
          ["Cable loaded at DC polarity", "Thermal gradient and charge injection", "Voltage removed", "Charge relaxation", "Opposite-polarity ramp", "Local dielectric field peak", "Restored transfer"],
          [(1,2),(2,3),(3,4),(4,5),(5,6),(2,6),(6,7),(4,6),(7,1)],
          [c("EXACT",[2,4,6],"Poisson charge-field relation and charge continuity must hold."),
           c("CONSTITUTIVE",[2,4],"Trap/detrap mobility and conductivity depend on material and temperature."),
           c("ENGINEERING",[5,6,7],"Qualified local field/ramp and dielectric ageing limits survive dispatch optimization."),
           c("EVIDENCE",[2,4,6],"A scalar residual-charge decay is only a proxy; full radial field and uncertainty are required for real cable qualification."),
           c("ECONOMIC",[4,7],"Shorter waiting has value only if power has a real alternate-use margin and reliability is preserved.")],
          "A fixed dead time can omit actual retained charge and thermal gradients. Test qualified waiting/ramp schedules instead of declaring voltage zero to mean electrical reset.",
          {"projection_loss":"Same terminal voltage zero, different charge profiles => different reversal fields.","necessity_challenge":"The longest fixed waiting interval need not be necessary for every qualified state.","decision_sufficiency":"Release earlier only when avoided transfer constraint exceeds sensing, modelling and added risk cost."},
          "Proxy E_peak=E_applied+E_charge,0*exp(-t/tau) [kV/mm]; t_min=tau*ln(E_charge,0/(E_limit-E_applied)) if positive. Space-dependent transport supersedes this scalar model; tau[T] must be measured.",
          dict(E_applied_kV_per_mm=20,E_charge0_kV_per_mm=10,E_limit_kV_per_mm=25,tau_s=1000,assumed_hours_recovered=12,MW=500,margin_USD_per_MWh=5),
          dict(proxy_wait_s=1000*math.log(2)),
          money(12*500*5,25_000,250_000,(25_000+CRF*250_000)/(500*5),"Break-even qualified extra-transfer hours/year at assumed $5/MWh margin; not current market price."),
          "Bipolar charge transport, temperature-gradient and reversal-life models, with cable-type-specific testing.",
          "KNOWN charge/reversal coupling; negative economic screen and no qualified reduction in wait demonstrated.","KNOWN",
          ["https://www.mdpi.com/1996-1073/15/3/985","https://www.mdpi.com/1996-1073/17/13/3182"],
          "Primary search abstracts explicitly address residual space charge, temperature gradient, reversal period and lifetime. Direct 2024 full text returned 429.",
          "Reject if local field exceeds qualification, scalar relaxation misses polarity-dependent peaks, or avoided transfer is displaced to another hour with no net value."))
        # N072: derive and implement the two-port reduction of a coupled sheath circuit.
        total, limit, rc, rs, k1, k2 = 2500.,1600.,.01,.1,.05,.10
        sc=sheath_service_case(total,limit,rc,rs,k1,k2)
        x=sc['x_A']
        old_loss,new_loss=sc['baseline_loss_W'],sc['candidate_loss_W']
        saved_kW=sc['saved_input_W']/1000
        out.append(record(72, "Feeder dispatch preserving shared-ground sheath-loop loss",
          ["Two independently controlled feeder converters", "Core currents and mutual induction", "Cross-bonded sheath loops", "Shared grounding return", "Loop heat plus core heat", "Ampacity/service constraints", "Whole-network allocation", "Same delivered real power"],
          [(1,2),(2,3),(3,4),(4,3),(3,5),(2,5),(5,6),(6,7),(7,1),(1,8),(4,6)],
          [c("EXACT",[2,3,4],"Kirchhoff equations apply to shared grounding and sheath paths; earth bonding is not removed to save energy."),
           c("EXACT",[2,3,5],"Passive circuit real power dissipates as sum(I_rms^2 R); internal transfers do not create energy."),
           c("CONSTITUTIVE",[2,3,4],"Frequency-specific mutual impedance and loop impedance depend on actual topology and geometry."),
           c("ENGINEERING",[1,6,7,8],"Only electrically realizable transfers preserving power, voltage, protection and ampacity are eligible."),
           c("ECONOMIC",[5,7,8],"Include core-loss increase, control hardware and switching wear; capacity credits are excluded."),
           c("EVIDENCE",[2,4,7],"A changed earth/link-box state invalidates the loss kernel; uncertain impedance needs bounded robust dispatch.")],
          "A deliberately specified core-only benchmark omits a shared sheath return. Add that independently identified circuit only where independently controlled feeder converters or documented discrete load transfers actually exist. Passive parallel cables do not allow arbitrary current splitting. No inspected commercial implementation is claimed to omit this effect.",
          {"projection_loss":"Same total supplied current and individual RMS limits can hide unequal induced loop voltages and loss.","necessity_challenge":"Equal feeder loading is not always necessary for minimum total loss; it minimizes only symmetric core losses.","decision_sufficiency":"Include sheath state only if changed feasible allocation saves more than telemetry/control cost; a full-circuit optimizer is the comparator."},
          "Reduced resistive phasor-aligned model: L(x,I)=Rc*[x^2+(I-x)^2]+[k1*x-k2*(I-x)]^2/Rs [W]. x,I[A], Rc,Rs[ohm], k[V/A]. x in [I-Imax,Imax]. At fixed I, x*=clip{[Rc I+(k1+k2)k2 I/Rs]/[2Rc+(k1+k2)^2/Rs]}. Then solve V*I-L(x*,I)=Pdelivered to compare identical load service. Independently controlled converter inputs, identical ideal conversion efficiency and a 10kV aggregate RMS equivalent are ASSUMED. It is a passive two-port circuit surrogate, not a complete 3-phase cable model.",
          dict(initial_total_A=total,max_each_A=limit,Rcore_ohm=rc,Rloop_ohm=rs,k1_V_per_A=k1,k2_V_per_A=k2,hours=6000,price=.08,voltage_equivalent_V=10000,actuator="two independently controlled converter inputs; no added converter hardware included"),
          dict(equal_split_A=total/2,coupled_optimum_A=x,other_current_A=sc['other_A'],baseline_loss_W=old_loss,candidate_loss_W=new_loss,reduction_kW=saved_kW,identical_delivered_W=sc['delivered_W']),
          money(saved_kW*6000*.08,3000,50_000,(3000+CRF*50_000)/(.08*6000),"Versus equal-load/core-only allocation; break-even whole-system kW reduction. Toy result ties full coupled circuit optimization; field parameters and feasible actuator UNKNOWN."),
          "Published shared-ground multiloop models (Li et al., first published 2024), explicit cable-model software plus constrained circuit-aware optimization. Full coupled optimizer equals the proposed solution in this reduced model.",
          "OVERLAP with adverse novelty lead: field relation and electrical-thermal cable/load-transfer integration already published. Root reviewer located secondary summaries of CN122712765A apparently optimizing load allocation with sheath-current/thermal constraints, but primary access failed. Exact scope unresolved; no positive novelty conclusion.","OVERLAP",
          ["https://ietresearch.onlinelibrary.wiley.com/doi/full/10.1049/hve2.12503","https://www.digsilent.de/en/faq-reader-powerfactory/how-do-you-model-cross-bonding-in-cable-systems.html","https://patents.google.com/patent/CN109167362A/en","https://patents.google.com/patent/CN122712765A/en"],
          "Primary full paper opened: equations 1-13 model shared grounding, division and mutual coupling. Primary 2019 CN109167362A opened: shield/armor impedance, thermal load flow and load-transfer example. Official software search documents explicit bonding. CN122712765A is an UNVERIFIED ADVERSE LEAD: primary URL inaccessible; no claim its full scope was read. No universal software omission established.",
          "Reject if measured coupled loss is absent, no feasible load-transfer control exists, robust margins erase saving, or an established detailed network optimizer attains equal/better total cost."))
        out[-1]["financial"]["incremental_vs_strong_baseline"]=0.0
        out.append(record(73, "Station-DC ground-fault localization preserving capacitive transients",
          ["DC battery supplies protection", "Cable capacitance and leakage", "First insulation fault", "Bounded diagnostic injection", "Branch phase-sensitive sensing", "Isolation diagnosis", "Authorized repair", "Protection readiness"],
          [(1,2),(2,3),(3,4),(4,5),(2,5),(5,6),(6,7),(7,8),(1,8),(4,8)],
          [c("EXACT",[2,4,5],"Diagnostic admittance Y=G+j*omega*C separates resistive leakage from charging current."),
           c("ENGINEERING",[1,4,8],"Injection must not actuate or desensitize trips; DC supply remains available."),
           c("ENGINEERING",[3,7,8],"First-fault localization cannot imply permission to continue with dangerous second-fault combinations."),
           c("EVIDENCE",[5,6],"Sensor phase error and branch topology bound identifiability; ambiguous branches remain UNKNOWN."),
           c("ECONOMIC",[6,7],"Outage avoidance is counted only from measured improvement over current insulation monitors.")],
          "An amplitude-only injected-current detector mistakes distributed capacitance for a resistive fault. Preserve phase and topology through branch diagnosis.",
          {"projection_loss":"Equal current amplitude can arise from leakage or healthy capacitance, demanding different repair actions.","necessity_challenge":"Disconnecting each live protection feeder may be unnecessary when qualified online localization exists.","decision_sufficiency":"Additional sensing pays only if avoidable diagnosis/outage cost exceeds its annual burden."},
          "I=V*(G+j*2*pi*f*C) [A]. With V=10 V,f=1 Hz,C=10 uF,G=1/100kohm: resistive 100 uA, capacitive 628.3 uA. Linear small-signal model; protective-circuit interactions excluded pending qualification.",
          dict(V=10,f_Hz=1,C_F=10e-6,R_ohm=100_000),
          dict(resistive_uA=100,capacitive_uA=10*2*math.pi*10e-6*1e6),
          money(None,1000,10_000,1000+CRF*10_000,"Required incremental avoided diagnosis/outage loss USD/year; event rate and loss severity unmeasured."),
          "Modern continuous DC insulation monitors and low-frequency/phase-sensitive injection localization; topology-aware methods already studied.",
          "KNOWN family; new integration superiority unshown.","KNOWN",
          ["https://link.springer.com/article/10.1186/s42162-025-00470-3","https://www.sciencedirect.com/science/article/pii/S0378779625007977"],
          "2025 primary substation paper opened; separate primary low-frequency injection verification search. These establish existing diagnosis families, not safety of arbitrary injection parameters.",
          "Reject if a healthy capacitive branch is flagged, injection affects protection, or established monitors match accuracy and diagnosis cost."))
        battery_kWh=5000*10/3600
        out.append(record(74, "Hydro fast-response split that preserves penstock pressure",
          ["Grid requests fast power", "Electrical torque changes", "Governor gate motion", "Water-column acceleration", "Penstock pressure wave", "Battery bridge power", "Water flow reaches target", "Battery recharge and restored reserve"],
          [(1,2),(1,6),(2,3),(3,4),(4,5),(5,3),(6,2),(4,7),(7,8),(6,8),(8,1)],
          [c("EXACT",[3,4,5],"Water momentum and compressibility couple flow change to pressure; sudden-change Joukowsky bound is delta p=rho*a*delta v."),
           c("EXACT",[2,6,7,8],"Hydro plus battery power meets the request; recharge returns battery SOC before comparing service."),
           c("ENGINEERING",[3,5,7],"Water hammer, gate-rate, turbine instability and cavitation limits remain binding."),
           c("ENGINEERING",[6,8],"Battery power, usable energy and reserve recovery constrain the bridge."),
           c("ECONOMIC",[6,8],"Count service contribution after recharge loss and cycle wear, not bridge energy as free generation.")],
          "A fast electrical dispatch omits water-column lag. Supply the shortfall from an existing qualified buffer while hydro moves within hydraulic limits.",
          {"projection_loss":"Same hydro MW rating but different penstock momentum gives different safe ramp capability.","necessity_challenge":"Fast governor opening need not be the only path to a fast net electrical response.","decision_sufficiency":"A buffer is worthwhile only if extra service value exceeds power electronics, recharge and battery wear."},
          "For first-order hydraulic surrogate P_h=Pstep*(1-exp(-t/tau)), P_b=Pstep*exp(-t/tau); E_b=Pstep*tau/3600 [kWh], Pstep[kW],tau[s]. Water-hammer EMT/CFD qualification required; this does not predict pressure compliance.",
          dict(step_kW=5000,tau_s=10,events_year=1000,assumed_service_MW=5,service_hours=500,contribution_USD_per_MW_h=5,wear_USD_per_kWh=.02),
          dict(min_bridge_kWh=battery_kWh,recharge_required=True),
          money(5*500*5,3000+battery_kWh*1000*.02,100_000,(3000+battery_kWh*1000*.02+CRF*100_000)/(5*500),"Break-even service contribution USD/MW/h; contribution assumed net of recharge energy, wear separately charged. Power hardware costs scenario only."),
          "Hydroelectric-battery coordinated frequency control with refined water-hammer models already published.",
          "KNOWN exact broad coordination; negative assumed retrofit economics.","KNOWN",
          ["https://www.sciencedirect.com/science/article/pii/S0142061525008543","https://www.mdpi.com/1996-1073/18/19/5249"],
          "Primary research search identifies anti-regulation/water-hammer battery compensation and refined hydropower/BESS control. Direct publisher fetch failed; abstracts only.",
          "Reject if response is not equivalent, pressure exceeds its certified boundary, SOC is depleted, or baseline coordination yields the same net service."))
        dh=(4247-1228)/(1000*9.81)
        out.append(record(75, "Pumped-storage intake temperature carried into cavitation scheduling",
          ["Reservoir level and thermal profile", "Intake withdrawal depth", "Suction pressure and losses", "Vapor pressure at inlet", "Cavitation and efficiency", "Pump timing or intake choice", "Equal stored water/head"],
          [(1,2),(2,3),(2,4),(3,5),(4,5),(5,6),(6,2),(6,7),(1,7)],
          [c("EXACT",[1,2,7],"Same net water transfer and reservoir endpoint; stratification is not an energy source."),
           c("CONSTITUTIVE",[3,4,5],"NPSH available depends on absolute pressure, temperature-dependent vapor pressure, elevation and loss."),
           c("ENGINEERING",[5,6],"Qualified NPSH margin and pump operating map constrain intake and flow."),
           c("ENGINEERING",[2,6],"Environmental mixing, intake hardware and permitted water operation must remain feasible."),
           c("ECONOMIC",[5,6,7],"Any timing change includes changed price, head and water opportunity cost.")],
          "A level-only intake rule omits seasonal temperature and may miss a cavitation-margin crossover. Choose a feasible intake/time using both temperature and level.",
          {"projection_loss":"Same lower-reservoir level, different inlet temperature changes available suction margin.","necessity_challenge":"Reducing flow is not always necessary if an existing intake can supply cooler water without other penalties.","decision_sufficiency":"A small hydraulic margin has economic value only if it changes a feasible operating action."},
          "NPSHa=(p_abs-p_v(T))/(rho*g)+z-h_loss [m]. With assumed p_v(10 C)=1228 Pa and p_v(30 C)=4247 Pa, margin difference=.308 m. These are rounded scenario water properties, not an actual pump requirement.",
          dict(pv_cold_Pa=1228,pv_warm_Pa=4247,rho=1000,g=9.81,plant_kW=100_000,hours=2000,assumed_energy_fraction=.002,price=.08),
          dict(NPSH_difference_m=dh,assumed_saved_kWh=400_000),
          money(400_000*.08,5000,80_000,(5000+CRF*80_000)/(.08*100_000*2000),"Break-even saved energy fraction for same pumping service; .2% assumed, NOT derived from the .308 m NPSH difference."),
          "Temperature-aware NPSH assessment, cavitating pump-turbine CFD and plant scheduling with physical operating envelopes.",
          "OVERLAP: no new NPSH law; narrow thermal-stratification scheduling benefit unresolved.","OVERLAP",
          ["https://research.chalmers.se/en/publication/543489","https://www.sciencedirect.com/science/article/pii/S0196890424013116"],
          "2024 primary author page opened for cavitating pump/turbine performance; primary cavitation-scale paper search. They support the strong comparator, not the assumed .2% site saving.",
          "Reject if intake temperature cannot be changed, actual NPSH remains safely nonbinding, or energy/quality benefit vanishes against temperature-aware scheduling."))
        rail_kWh=4000*10/3600*.9*10_000
        out.append(record(76, "Rail dwell scheduling with actual regenerative-network receptivity",
          ["Train braking event", "DC regenerative injection", "Network resistance and substation topology", "Other train acceleration", "Station auxiliary or grid acceptance", "Voltage clamp and braking resistor", "Feasible dwell adjustment", "Passenger service and meter total"],
          [(1,2),(2,3),(3,4),(3,5),(3,6),(4,7),(7,1),(7,4),(6,8),(5,8),(7,8)],
          [c("EXACT",[2,3,4,5,6],"Braking energy divides into useful absorption, network loss, resistor heat and storage change."),
           c("CONSTITUTIVE",[3,6],"Network voltage and resistance bound absorption; overlap time alone is insufficient."),
           c("ENGINEERING",[7,8],"Headway, passenger dwell, journey time and punctuality constraints are preserved."),
           c("ENGINEERING",[3,5],"Substation reverse-power permissions and equipment limits must be known."),
           c("ECONOMIC",[5,6,8],"Do not add the same kWh as train saving, station saving and exported energy.")],
          "Acceleration/braking time overlap loses the electrical location and receptive path. Optimize small existing timetable slack using actual network absorption.",
          {"projection_loss":"Same braking/traction overlap, different electrical sections or voltage headroom => different recovered energy.","necessity_challenge":"New storage is not necessarily needed if existing timetable slack and receptive loads suffice.","decision_sufficiency":"Use only schedule changes with positive metered energy value after equivalent passenger service."},
          "E_used=integral min(P_brake,P_receptive,P_networklimit)dt * eta_path [kWh]. Toy pulses: 4 MW, extra overlap 10 s, eta=.9 =>10 kWh/event. Full nonlinear DC load flow is required for field predictions.",
          dict(brake_kW=4000,extra_overlap_s=10,efficiency=.9,eligible_events_year=10_000,price=.12),
          dict(conditional_kWh_recovered=rail_kWh),
          money(rail_kWh*.12,2000,30_000,(2000+CRF*30_000)/(.12*10),"Break-even eligible events/year at 10 kWh/event; compared with a fixed less-coordinated timetable."),
          "2025 speed-profile/dwell optimization with dynamic power network; cross-substation energy optimization (2023) and power-flow timetabling (2012).",
          "KNOWN exact class; no gain over modern timetable-plus-load-flow optimizer shown.","KNOWN",
          ["https://livrepository.liverpool.ac.uk/3193208/","https://www.sciencedirect.com/science/article/pii/S0360835223004722","https://journals.sagepub.com/doi/10.1177/0954409711429411"],
          "Primary publisher and author-repository search abstracts explicitly address dynamic power flow, dwell and cross-substation energy. Repository open failed; no underlying timetable reused.",
          "Reject if the extra overlap is infeasible, energy is already absorbed/exported, or the modern constrained timetable model matches the result."))
        ups_saved=1000*8760*(1/.96-1/.99)*.7
        out.append(record(77, "UPS economical bypass qualified by phase and hold-up reserve",
          ["Utility waveform", "Bypass eligibility decision", "Static-switch phase relationship", "DC-link stored energy", "Disturbance detected", "Inverter resumes supply", "Critical-load continuity"],
          [(1,2),(2,3),(3,7),(1,5),(5,6),(4,6),(6,7),(3,6),(7,2)],
          [c("EXACT",[4,6,7],"Load hold-up energy cannot exceed capacitor/battery usable energy."),
           c("ENGINEERING",[1,3,5,6,7],"Transfer phase, waveform quality, detection delay and critical-load tolerance must all be qualified."),
           c("CONSTITUTIVE",[2,6],"Efficiency and losses are load- and mode-dependent, not constant nameplate values."),
           c("EVIDENCE",[1,2],"Normal recent utility history is not proof the next transfer will succeed."),
           c("ECONOMIC",[2,7],"No energy saving can be valued without unchanged required availability; outage-loss change UNKNOWN.")],
          "A utility-good flag omits phase alignment and energy needed until inverter recovery. Bind these before admitting more high-efficiency operation.",
          {"projection_loss":"Identical utility RMS voltage can have different phase jumps and transfer outcomes.","necessity_challenge":"Continuous double conversion is unnecessary for some qualified loads/utility conditions, already commercialized.","decision_sufficiency":"Bypass only within independently validated continuity boundaries; compare total lifecycle cost, not efficiency alone."},
          "E_hold=.5*C*(V_hi^2-V_lo^2) [J]>=P_load*t_transfer. For 1 MW,10 ms,400->350 V, C>=.5333 F in an ideal capacitor-only proxy. deltaE=P_load*h*(1/eta_base-1/eta_eco)*eligible [kWh].",
          dict(load_kW=1000,hours=8760,eta_base=.96,eta_eco=.99,eligible=.7,price=.1),
          dict(conditional_saved_kWh=ups_saved,ideal_hold_C_F=2*1e6*.01/(400**2-350**2)),
          money(ups_saved*.1,3000,50_000,(3000+CRF*50_000)/(.1*1000*8760*(1/.96-1/.99)),"Break-even eligible time fraction; hypothetical 1 MW site versus continuous double conversion."),
          "Commercial advanced ECO/multimode UPS and phase-synchronized static transfer with load-compatibility qualification.",
          "KNOWN class; no novel control or equal-reliability improvement proved.","KNOWN",
          ["https://www.eaton.com/content/dam/eaton/products/backup-power-ups-surge-it-power-distribution/backup-power-ups/eaton-93pr/eaton-93pr25-1200kw-ups-whitepaper-en-us-east-asia.pdf","https://patents.justia.com/patent/20140361624"],
          "Official manufacturer whitepaper and primary patent search describe high-efficiency bypass and load-quality control. Manufacturer performance assertions are not independent validation of this scenario.",
          "Reject if transfer/quality requirements fail, recent-grid signals add no information beyond existing ECO control, or availability-adjusted cost increases."))
        ev_kWh=16*.08*(1000-200)
        out.append(record(78, "EV cable cooling run-on from stored heat and next-session readiness",
          ["High-current charging", "Cable and connector heat inventory", "Charge disconnect", "Coolant circulation continues", "Surface/internal cooling", "Pump stopping decision", "Next charging session"],
          [(1,2),(2,3),(3,4),(4,5),(5,6),(6,7),(2,5),(7,1),(7,6)],
          [c("EXACT",[1,2,4,5],"Joule heat and cooling/storage energy balance must close after current stops."),
           c("CONSTITUTIVE",[2,5],"Internal hotspot and measured coolant temperature can differ; calibrated thermal model needed."),
           c("ENGINEERING",[5,6,7],"Touch limits, hose/material limits and promised next-session power remain unchanged."),
           c("ENGINEERING",[4,7],"Coolant viscosity, pressure and cold-start limits may invalidate a cooling-only model."),
           c("ECONOMIC",[4,6],"Pump run-on energy is usually small; do not imply a large charging-energy percentage.")],
          "A fixed after-run interval ignores stored heat and arriving demand. Stop after qualified temperature/readiness criteria, not automatically at unplugging.",
          {"projection_loss":"Equal last-session kWh can hide different current histories and connector heat.","necessity_challenge":"A fixed long run-on is not always necessary; an already-published temperature stop exists.","decision_sufficiency":"Pump saving must exceed sensing, control and support cost at unchanged turnaround."},
          "C_th*dT/dt=I^2R-UA(u)*(T-Ta) [W]; after unplug I=0. Equal endpoint temperatures and next-session readiness. deltaE=n_ports*P_pump*(h_base-h_candidate) [kWh].",
          dict(ports=16,pump_kW=.08,base_runon_h=1000,candidate_runon_h=200,price=.15),
          dict(conditional_saved_kWh=ev_kWh),
          money(ev_kWh*.15,500,16_000,(500+CRF*16_000)/(.15*16*.08),"Break-even avoided run-on hours per port/year; candidate hours hypothetical."),
          "Temperature-threshold post-session cooling (EP4653248A1) and qualified liquid-cable cold-start control.",
          "KNOWN exact broad stopping criterion; negative energy-only retrofit screen.","KNOWN",
          ["https://patents.google.com/patent/EP4653248A1/en","https://patents.google.com/patent/WO2018200552A1/en"],
          "Primary EP patent opened; explicitly continues cooling after session until temperature threshold. WO patent describes cold-start pressure/flow constraints.",
          "Reject if internal temperature rebounds above limit, next session derates, or old controller already uses a valid temperature stop."))
        out.append(record(79, "Coastal electrical-insulator cleaning using dry salt and wetting state",
          ["Marine aerosol deposited", "Dry nonconducting salt layer", "Fog or dew wetting", "Conductive leakage path", "Surface heating/flashover risk", "Qualified cleaning window", "Safe energized availability"],
          [(1,2),(2,3),(3,4),(4,5),(5,6),(6,2),(5,7),(3,6),(1,6)],
          [c("EXACT",[1,2,6],"Salt mass balance includes deposition, rain wash and deliberate cleaning."),
           c("CONSTITUTIVE",[2,3,4],"Film conductivity depends on salt loading, water, material hydrophobicity and geometry."),
           c("ENGINEERING",[4,5,6,7],"Certified insulation and safe work/weather boundaries remain hard constraints."),
           c("EVIDENCE",[2,4],"Low dry leakage does not prove clean insulation; independent dry contamination measurement is needed."),
           c("ECONOMIC",[6,7],"Count avoided actual visits only; no invented flashover event probabilities or simultaneous duplicated availability credit.")],
          "Leakage-current-only maintenance can regard a dry salt deposit as harmless until wetting. Combine dry contamination and wetting forecasts before selecting a cleaning window.",
          {"projection_loss":"Zero dry leakage can mean clean or heavily salted insulation with opposite wet-weather risk.","necessity_challenge":"Fixed-calendar cleaning need not be necessary if a qualified contamination/wetting assessment supports the same risk limit.","decision_sufficiency":"The assessment has value only if it changes a safe visit decision and costs less than the avoided visit."},
          "I_leak=V*G_film(m_salt,water,T,geometry) [A]; G is empirical, nonlinear and cannot be inferred from dry I alone. Annual direct value=N_avoided_visits*c_visit [USD/year].",
          dict(assumed_avoided_visits=4,cost_per_visit=15_000),
          dict(measured_failure_reduction=None,conditional_avoided_visits=4),
          money(60_000,10_000,100_000,(10_000+CRF*100_000)/15_000,"Break-even safely avoided visits/year at assumed $15k offshore/coastal campaign cost; site eligibility unmeasured."),
          "Dry-condition microwave reflectometry and meteorology/leakage-based contamination monitoring already published; compare condition-based maintenance with equivalent qualification.",
          "OVERLAP; no novel sensing principle or measured reduction in visits.","OVERLAP",
          ["https://orca.cardiff.ac.uk/id/eprint/94369/","https://researchportal.hw.ac.uk/en/publications/the-effects-of-salt-contamination-deposition-on-hv-insulators-und/","https://www.mdpi.com/2076-3417/14/4/1506"],
          "Primary author-repository search explicitly identifies the dry-condition blind spot and microwave method; separate salt-deposition study and condition-monitoring research support wetting coupling.",
          "Reject if dry-salt measurement adds no decision information, forecast errors increase risk, or existing condition-based maintenance already avoids these visits."))
        q=100.; a,b=.1,.2
        q1=b*q/(a+b)
        old=a*(q/2)**2+b*(q/2)**2
        new=a*q1*q1+b*(q-q1)**2
        out.append(record(80, "Synchronous-condenser VAr sharing with whole-plant loss curves",
          ["Grid reactive-power request", "Two online condenser fields", "Stator and field copper loss", "Cooling auxiliaries", "Rotor thermal limits", "Required fault strength and inertia", "Constrained VAr allocation", "Voltage service plus metered real power"],
          [(1,2),(2,3),(3,4),(3,5),(5,7),(6,7),(7,2),(2,8),(4,8),(6,8)],
          [c("EXACT",[1,2,8],"Reactive power sum meets the same grid demand; real power drawn supplies machine and auxiliary losses."),
           c("CONSTITUTIVE",[2,3,4,5],"Loss curves and field/thermal limits depend on machine condition and ambient state."),
           c("ENGINEERING",[6,7,8],"Required online inertia/fault contribution is preserved; machines cannot be switched off merely because VAr can be supplied elsewhere."),
           c("ENGINEERING",[2,7],"Capability curves, excitation response and reserve headroom constrain dispatch."),
           c("ECONOMIC",[3,4,8],"Both machines stay online; fixed windage/core losses cancel and cannot be claimed as saved.")],
          "Equal VAr sharing ignores unequal marginal copper/cooling loss. Allocate within complete capabilities while preserving required synchronous support.",
          {"projection_loss":"Same total MVAr and equal nameplate sizes can have different marginal real-power losses.","necessity_challenge":"Equal VAr loading is not required for equal grid support when both online machines retain qualified margins.","decision_sufficiency":"Shift VAr only when total metered real-power reduction exceeds controller cost and preserves dynamic service."},
          "L=Lfixed+a*Q1^2+b*Q2^2 [kW], Q[MVAr], a,b[kW/MVAr^2], Q1+Q2=Qtotal; Q1*=b*Qtotal/(a+b), clipped to capability constraints. Static quadratic surrogate; dynamic stability separately qualified.",
          dict(total_MVAr=q,a=a,b=b,hours=8000,price=.08,both_machines_online=True),
          dict(optimal_Q1_MVAr=q1,baseline_variable_loss_kW=old,optimal_variable_loss_kW=new,reduction_kW=old-new),
          money((old-new)*8000*.08,5000,100_000,(5000+CRF*100_000)/(.08*8000),"Break-even measured kW saving versus equal VAr sharing. Existing full-loss optimal dispatch ties, not an incremental Garden saving."),
          "Constrained optimal reactive dispatch, AC-excitation condenser loss optimization and whole-plant active-energy metering.",
          "KNOWN optimization class; no new theorem, equipment effect or advantage over loss-aware dispatch.","KNOWN",
          ["https://ieeexplore.ieee.org/document/10913876/","https://cse.cigre.org/cse-n040/active-energy-metering-in-synchronous-condensers.html"],
          "Primary IEEE title/abstract search explicitly covers condenser loss optimization under multiple constraints; CIGRE primary engineering paper includes auxiliary and fixed-loss metering boundaries.",
          "Reject if real capability curves prohibit the shift, extra cooling/field loss reverses it, or loss-aware conventional dispatch already uses the same optimum."))
        for r in out:
            assert all(1<=u<=len(r['nodes']) and 1<=v<=len(r['nodes']) for u,v in r['edges'])
            assert all(all(1<=n<=len(r['nodes']) for n in con['nodes']) for con in r['constraints'])
            if r['financial']['gross'] is not None:
                assert math.isfinite(r['financial']['net'])
        assert [r['id'] for r in out]==[f'N{n:03}' for n in range(61,81)]
        return out


    def detailed_tests():
        """Numerical physical comparisons, explicit assumptions; not plant validation."""
        checks=0
        # Faraday-law normalized first-cycle flux: integrate dphi/dt=sin(t+theta).
        # Numerical trapezoidal trajectory independently compares analytic endpoint.
        worst=0.; worst_error=0.
        for r in [-.8,-.4,0,.4,.8]:
            theta=math.acos(-r)
            steps=20000
            dt=2*math.pi/steps
            flux=r
            peak=abs(flux)
            for j in range(steps):
                t=j*dt
                flux+=.5*dt*(math.sin(t+theta)+math.sin(t+dt+theta))
                expected=r+math.cos(theta)-math.cos(t+dt+theta)
                worst_error=max(worst_error,abs(flux-expected))
                peak=max(peak,abs(flux))
            assert abs(peak-1)<1e-7
            assert abs(flux-r)<1e-10
            # Fixed 90-degree closing is optimal only for zero remanence.
            assert 1+abs(r+math.cos(math.pi/2)) >= peak-1e-7
            checks+=3
            for error in [-.05,0,.05]:
                for jitter in [-math.radians(3),0,math.radians(3)]:
                    observed=1+abs(r+error+math.cos(theta+jitter))
                    assert observed<=1+.05+math.radians(3)+1e-12
                    worst=max(worst,observed)
                    checks+=1
        # Large-error null demonstrates the toy safety margin is not universal.
        large_error_peak=1+abs(.8+.1+math.cos(math.acos(-.8)+math.radians(-15)))
        assert large_error_peak>1.2
        checks+=1
        # N072 compare derivative-derived allocation with a conventional scalar
        # optimizer. Both close SAME DELIVERED POWER and see the same actual control
        # freedom (independent ideal feeder converters); passive cable splitting is
        # explicitly excluded. The comparator solves for the second current from
        # the quadratic power balance, then uses a golden-section search.
        def loss(x,total,rc,rs,k1,k2):
            return rc*(x*x+(total-x)**2)+(k1*x-k2*(total-x))**2/rs
        scenarios=[(2500.,1600.,.01,.1,.05,.1),
                   (2500.,1600.,.01,.1,.05,.05), # symmetric null
                   (1000.,800.,.01,.1,0.,0.), # no coupling null
                   (2500.,1250.,.01,.1,.05,.1), # no dispatch freedom
                   (1000.,800.,.05,.2,.02,.05)]
        results=[]
        for total,lim,rc,rs,k1,k2 in scenarios:
            service=sheath_service_case(total,lim,rc,rs,k1,k2)
            target=service['delivered_W']
            voltage=service['voltage_V']
            def other_current(x,ka,kb):
                aa=rc+kb*kb/rs
                bb=voltage+2*ka*kb*x/rs
                cc=(rc+ka*ka/rs)*x*x-voltage*x+target
                disc=bb*bb-4*aa*cc
                assert disc>=0
                return 2*cc/(bb+math.sqrt(disc))
            lower=max(0.,other_current(lim,k2,k1))
            upper=lim
            def required_input(x):
                return voltage*(x+other_current(x,k1,k2))
            gl,gh=lower,upper
            ratio=(math.sqrt(5)-1)/2
            for _ in range(150):
                left=gh-ratio*(gh-gl)
                right=gl+ratio*(gh-gl)
                if required_input(left)<required_input(right):
                    gh=right
                else:
                    gl=left
            choices=[lower,upper,gl,gh,(gl+gh)/2]
            strongest_input=min(required_input(t) for t in choices)
            strongest=strongest_input-target
            x=service['x_A']
            total_new=service['total_A']
            proposed=service['candidate_loss_W']
            fixed=service['baseline_loss_W']
            assert abs(proposed-strongest)<1e-5
            assert proposed<=fixed+1e-7
            # Circuit conservation: induced source drop powers the resistive loop.
            emf=k1*x-k2*(total_new-x)
            loop_current=emf/rs
            assert abs(emf*loop_current-loop_current**2*rs)<1e-7
            checks+=3
            results.append(dict(initial_total_A=total,new_total_A=total_new,x_A=x,
                                delivered_W=target,weak_loss_W=fixed,
                                candidate_loss_W=proposed,strong_loss_W=strongest,
                                gain_vs_strong_W=strongest-proposed))
        assert abs(results[1]['weak_loss_W']-results[1]['candidate_loss_W'])<1e-7
        assert abs(results[2]['weak_loss_W']-results[2]['candidate_loss_W'])<1e-7
        assert abs(results[3]['weak_loss_W']-results[3]['candidate_loss_W'])<1e-7
        checks+=3
        return dict(assertions=checks,flux_numerical_max_error=worst_error,
                    flux_bounded_error_peak=worst,flux_large_error_counterexample=large_error_peak,
                    sheath_comparisons=results,empirical_tests=0,
                    blind_benchmark=False,physical_model_scope="single-phase ideal Faraday law; reduced two-feeder sheath circuit")

    return run(), detailed_tests()



# Source SHA256: e635ee8c44ec2bd120a2f56cc9151c4548e52e7d99e3c0d0e29bd51658c23f60
def workstream_food_bio():
    """N081-N100: bounded, noncanonical industrial research screens.
    Standard library; all numerical plant parameters and prices are assumptions.
    Not a food safety validator, SAL compiler, novelty certificate, or deployment tool.
    """
    import math

    SOURCE_MANIFEST = {'V15_10_ABSTRACTION_GCSC_DELTA.md': '90a58c337bc87c2e445eb56d6197cddea845f74485339e074b0818d70dae8479', 'GSL_COMBINATORIAL_SEMANTIC_COVERAGE_v0.1.md': '27428feebc2fe8f2a4a9a5dd8fc5d680d36fb18623575ef19235427f9021e3b1', 'INVARIANT_DRIVEN_THEORY_DISCOVERY_IDTD_001.md': '14bf4fdced0cccebeb5cb22a0cec3b7aff765e57efa25230626ddcf3b24bfdf4', 'TREE_CORE_v0.8.1_2026-09-23.txt': '4af3a2c4c8d8577909735fb61c42e0f43324dc0147d8b24146b4561ee56511fa', 'GARDEN_TECHNICAL_v15.10_FULL_DELTA.txt': 'f61bc8e4f12418498f114f586c2d4e58b1ca575a788e0e5194430088a0f8f18f'}

    CRF = .08 * 1.08**10 / (1.08**10 - 1)


    def case(i, title, nodes, cross, constraints, gap, intervention, operators, equation,
             inputs, quantity, unit_value, opex, capex, break_unit, baseline, status,
             novelty, sources, falsifier, limit, prediction):
        n = nodes.split(' | ')
        q = quantity
        gross = None if q is None else q * unit_value
        return dict(id=f'N{i:03d}', title=title, nodes=n,
            edges=[(j,j+1) for j in range(1,len(n))]+cross,
            constraints=constraints, gap=gap, intervention=intervention,
            operators=dict(zip(('Projection-Loss','Necessity-Challenge','Decision-Sufficiency'), operators)),
            equation=equation, inputs=inputs, physical_prediction=prediction,
            financial=dict(gross=gross,opex=opex,capex=capex,
                net=None if gross is None else gross-opex-CRF*capex,
                break_even=(opex+CRF*capex)/unit_value if unit_value else None,
                break_even_unit=break_unit, currency='USD per facility-year',
                basis='ASSUMED scenario versus specified weak/local baseline; incremental value versus strongest baseline UNKNOWN'),
            baseline=baseline,novelty=novelty,status=status,sources=sources,
            falsifier=falsifier,limiting_case=limit,
            evidence=dict(derivation='bounded algebra checked',simulation='not field validation',
                          empirical='UNKNOWN',historical_novelty='not demonstrated',economic='unmeasured',admission='NONCANONICAL'))


    def run():
        c=[]
        c.append(case(81,'Press spent brewery grain before thermal drying, retaining dissolved solids accounting',
          'Lauter discharge | Wet grain buffer | Mechanical press | Press liquor assay | Cake dryer | Dry feed quality | Effluent treatment',
          [(3,5),(4,7),(4,6)],
          ['EXACT mass: dry solids and water close across press cake and liquor (nodes 2-5,7).',
           'CONSTITUTIVE: evaporative duty q per kg removed valid only at declared dryer efficiency (5).',
           'ENGINEERING: feed nutritional and microbial endpoints unchanged; reject fines/nutrient loss (6).',
           'ECONOMIC: displaced evaporation minus electricity, liquor treatment and lost feed value (3-7).'],
          'A dryer feed mass total erases whether water could leave mechanically and whether valuable solids leave with it.',
          'Qualify extra press duty using water and dry-solids balances before reducing thermal drying.',
          ['Same wet mass and moisture can have different pressability and liquor-solids export.',
           'Evaporation is not necessary for all free water; dry-feed specification still holds.',
           'Press only if avoided fuel exceeds press work, solids loss and effluent cost.'],
          'D=M(1-x0); W_removed=M-D/(1-x1); E_avoided=W_removed*q. M,D,W kg; x wet-basis fractions; q kWh/kg.',
          dict(wet_feed_kg_y=50e6,x0=.8,x1=.7,q_kWh_kg=.75,heat_USD_kWh=.04,
               extra_press_kWh_per_kg_water=.025,electric_USD_kWh=.12,other_cost_USD_y=33000),
          (50e6-10e6/.3)*.75,.04,(50e6-10e6/.3)*.025*.12+33000,300000,'avoided thermal kWh/y',
          'Optimized filter/screw press plus low-temperature dryer, already incorporating liquor treatment; no demonstrated gain over it.',
          'KNOWN','Broad two-stage mechanical/thermal dewatering is directly disclosed; no novel claim.',
          ['https://patents.google.com/patent/US20120005916A1/en','https://onlinelibrary.wiley.com/doi/full/10.1002/jib.697'],
          'Lower dry-feed yield, extra treatment burden or best existing press already reaching x1 eliminates the claim.',
          'x1=x0 gives zero displaced evaporation; x1>x0 invalid.',
          'Assumed moisture change 80% to 70% removes 16.667 million kg/y water mechanically; quality and pressability untested.'))
        c.append(case(82,'Stop grain-bin aeration only after a qualified cooling front completes',
          'Ambient air qualification | Fan start | Bottom grain cooled | Moving cooling front | Top outlet response | Fan stop | Storage moisture check',
          [(1,4),(4,7),(5,7)],
          ['EXACT energy: air enthalpy removal equals grain cooling plus losses (2-5).',
           'CONSTITUTIVE: interstitial airflow and heat transfer determine front travel (3-5).',
           'ENGINEERING: the warmest retained grain and moisture redistribution qualify stop, not mean temperature alone (5-7).',
           'ENGINEERING: roof ventilation and condensation constraints persist (2-7).'],
          'Mean bin temperature loses the incomplete top front; fixed extra fan hours waste power after it has completed.',
          'Use outlet/front and humidity checks to terminate only redundant aeration hours.',
          ['Equal mean temperature can hide a warm top versus a uniformly cool bin.',
           'Fixed long fan operation is unnecessary after a verified front, but early stopping is inadmissible.',
           'A front check matters only if its avoided overrun exceeds sensor and maintenance cost.'],
          'E_saved=P_fan*Delta_t; P kW, Delta_t h/y, E kWh/y. Front bound M*c_p*Delta_T <= integral(m_air*Delta_h dt).',
          dict(fan_kW=100,redundant_hours_y=200,electric_USD_kWh=.12),
          100*200,.12,2000,50000,'avoided fan kWh/y',
          'Existing outlet-temperature/humidity aeration management and distributed temperature control; candidate adds no physical capability.',
          'KNOWN','Completion of the cooling front is explicit existing extension guidance; assumed small site fails financial screen.',
          ['https://extension.okstate.edu/fact-sheets/aeration-management-knowing-when-to-run-aeration-fans',
           'https://cropwatch.unl.edu/grain-drying-tips-and-reminders/'],
          'Stopping before top cooling or permitting condensation invalidates energy credit.',
          'Zero redundant hours means zero gross saving; a larger motor alone does not establish redundant duty.',
          'Conditional avoided electricity 20,000 kWh/y; no avoided spoilage value claimed.'))
        c.append(case(83,'Bind rice tempering completion to subsequent milling fracture loss',
          'Rice dryer exit | Kernel moisture profile | Insulated tempering | Moisture equalization | Milling stress | Whole and broken separation | Saleable grade',
          [(2,5),(3,7),(5,7)],
          ['EXACT water: mean kernel water stays constant during sealed tempering (2-4).',
           'CONSTITUTIVE: diffusion and glass-transition/stress laws are cultivar/temperature dependent (2-5).',
           'EMPIRICAL: fissure-to-head-rice-yield relation requires calibration (5-7).',
           'ENGINEERING: moisture, food safety, throughput and milling degree unchanged (3-7).'],
          'Dryer mean moisture can be acceptable while a remaining radial gradient damages rice in milling.',
          'Release tempered batches on a validated profile/stress bound rather than mean moisture alone.',
          ['Equal mean moisture with unequal radial gradient yields different fracture risk.',
           'Immediate milling after mean moisture passes is not necessary; excessive tempering is also not required.',
           'Extra head-rice premium must cover tempering inventory, handling and monitoring.'],
          'dX/dt=D_eff*Laplacian(X) with no-flux tempering boundary; Delta_V=M*Delta_h*p. X kg water/kg dry solid; D m2/s; M t/y; Delta_h dimensionless.',
          dict(rice_t_y=100000,additional_head_fraction=.005,premium_USD_t=150),
          100000*.005,150,15000,200000,'additional head rice t/y',
          'Finite-element kernel moisture/glass-transition models and optimized intermittent drying/tempering already couple milling yield.',
          'KNOWN','Cross-situation moisture-to-milling relation directly studied; no new law or measured cultivar improvement.',
          ['https://www.sciencedirect.com/science/article/pii/S0260877409005032',
           'https://doi.org/10.1016/S1537-5110(03)00091-6'],
          'Matched milling at equal degree and moisture shows no additional head rice or tempering creates throughput loss exceeding value.',
          'Uniform initial X leaves no profile-relaxation benefit.',
          'The assumed 0.5 percentage point gain would add 500 t/y head rice; this is a target, not predicted from calibrated diffusion.'))
        c.append(case(84,'Recover ice-carried mother liquor with measured wash-front displacement',
          'Juice crystallizer | Ice and entrained liquor | Wash-column bed | Meltwater displacement | Concentrate return | Ice melt outlet | Refrigeration balance',
          [(2,6),(4,5),(4,7),(5,1)],
          ['EXACT solute: mother-liquor sugar enters concentrate return or melt outlet; inventory is explicit (1-6).',
           'EXACT water/energy: added wash melt increases water/refrigeration or reconcentration duty (3-7).',
           'CONSTITUTIVE: exp(-N) wash model assumes well mixed retained pore liquid, no occluded inaccessible pockets (2-4).',
           'ENGINEERING: concentrate quality and final solids content unchanged (5).'],
          'Counting clean ice tonnes omits retained solute and the washwater dilution returned to concentration.',
          'Assay both outlet solute streams and qualify a wash-front setpoint on net recovery after dilution cost.',
          ['Equal ice throughput can carry different trapped liquor fractions.',
           'Discarding entrained liquor is unnecessary; unlimited washing is not free.',
           'Continue washing only while marginal recovered-solute value exceeds added removal duty and costs.'],
          'm_s0=M_ice*e*c; m_s_remaining=m_s0*exp(-N); r=1-exp(-N). N=W/L, L retained liquor kg, W clean wash kg. Economic delta uses r_new-r_base.',
          dict(ice_kg_y=20e6,entrained_liquor_kg_per_kg_ice=.05,solute_mass_fraction=.4,r_base=.5,r_new=.9,
               solute_USD_kg=1.5,extra_wash_water_kg_y=(math.log(10)-math.log(2))*50*20000,removal_kWh_kg=.7,electric_USD_kWh=.10,other_opex=50000),
          20e6*.05*.4*(.9-.5),1.5,50000+(math.log(10)-math.log(2))*50*20000*.7*.1,400000,'extra recovered solute kg/y',
          'Known countercurrent gradient/wash columns with solute and washwater balances, including US4830645A. Strong baseline matches this scalar model.',
          'KNOWN','Mother-liquor displacement and recycle are old prior art; a site sensor integration is not a discovery.',
          ['https://patents.google.com/patent/US4830645A/en','https://patents.google.com/patent/EP0360876B1/en'],
          'Inaccessible occlusion, lower purity, lost refrigeration capacity or existing wash efficiency of 90% erases incremental value.',
          'e=0, c=0 or r_new=r_base gives zero product recovery; N→infinity approaches but never exceeds initial trapped solute.',
          'Conditional extra recovery 160,000 kg/y versus 50% wash recovery; against a 90% modern column, extra recovery is zero.'))
        c.append(case(85,'Route spray-dryer fines into the qualified agglomeration zone',
          'Atomized droplets | Drying trajectory | Cyclone fines | Fines return injection | Sticky collision zone | Finished powder | Wall deposits and cleaning',
          [(2,5),(3,7),(4,7),(5,7)],
          ['EXACT solids: feed equals product, deposits, exhaust loss and inventory (1-7).',
           'CONSTITUTIVE: glass-transition temperature and water activity set sticking window (2,5).',
           'ENGINEERING: powder size, solubility, moisture and hygienic endpoints preserved (6).',
           'ECONOMIC: recovered product and avoided cleaning cannot both count the same saleable batch twice.'],
          'Returning all fines without their moisture/temperature collision state can convert recoverable solids to wall deposits.',
          'Choose return position and gas condition using measured stickiness and product properties.',
          ['Equal fines mass at different moisture and injection locations does not imply equal agglomeration.',
           'Maximum dryer temperature is not necessary for stable powder production.',
           'The changed return is useful only if net saleable powder gain beats blower, cleaning and capital costs.'],
          'Delta_m=M_powder*Delta_y; sticking proxy T_particle-Tg(X) must remain within calibrated zone. Delta_m kg/y; Delta_y dimensionless.',
          dict(powder_kg_y=50e6,additional_saleable_fraction=.002,net_product_USD_kg=3),
          50e6*.002,3,60000,400000,'extra saleable powder kg/y',
          'CFD agglomeration plus measured glass-transition-based fines return optimization; modern installations may already preserve this interface.',
          'KNOWN','Injection position, sticky state and energy economy directly covered by patents and experiments.',
          ['https://patents.google.com/patent/EP0729383A1/en','https://www.sciencedirect.com/science/article/pii/S0032591010004328'],
          'No saleable gain at matched powder quality or additional recirculation/deposits offset it.',
          'No fines/deposit loss or equal optimized return gives zero increment.',
          'Target gain 100,000 kg/y; no calibrated deposition model predicts that gain here.'))
        c.append(case(86,'Route dairy membrane permeate by downstream ionic and hygiene duty',
          'Dairy NF permeate | RO separation | Dissolved-species assay | Water duty allocation | Qualified utility use | Concentrate disposition | Hygiene requalification',
          [(2,6),(3,6),(4,7),(7,5)],
          ['EXACT species: salts, lactose and water separately close across RO (1-3,6).',
           'CONSTITUTIVE: membrane rejection depends on species, age and pressure (2).',
           'ENGINEERING: each receiving duty retains microbial/chemical criteria; conductivity alone cannot certify reuse (3-7).',
           'ECONOMIC: avoid water disposal and purchase only once; retentate disposal remains charged (6).'],
          'Bulk conductivity can hide organic contamination or unsuitable ion ratios when permeate is handed to a reuse decision.',
          'Allocate only independently qualified streams to matching utility duties, preserving retentate costs.',
          ['Equal conductivity can contain different lactose and ion species.',
           'Potable fresh water is not essential for every isolated utility duty; unrestricted food-contact reuse is not inferred.',
           'Saved purchased water must exceed treatment, assays and disposal cost.'],
          'm_i,feed=m_i,perm+m_i,ret; V_reuse=V*eligible. V m3/y; m_i kg/y; eligible dimensionless. Each duty has independent c_i limits.',
          dict(permeate_m3_y=200000,eligible_fraction=.6,avoided_water_USD_m3=2.5),
          200000*.6,2.5,120000,400000,'qualified reused water m3/y',
          'Dairy process-water RO plus multicomponent chemical/microbial qualification; current recovery studies already evaluate water and mineral streams.',
          'OVERLAP','Species-qualified water reuse is established; exact site allocation may be useful but is not proven novel.',
          ['https://pubmed.ncbi.nlm.nih.gov/29055547/','https://www.sciencedirect.com/science/article/pii/S2949824426001217'],
          'Any required duty fails chemical or hygienic qualification, or strongest existing allocation achieves the same reuse.',
          'Eligible fraction zero gives no saving; reject rather than blend away a forbidden contamination state.',
          '120,000 m3/y qualifying reuse is an assumed target, not an established safe volume.'))
        c.append(case(87,'Capture whey curd fines before they enter membrane clarification',
          'Cheese vat draining | Whey and curd fines | Gentle screen separation | Recovered curd disposition | Clarified whey membrane feed | Product qualification | Waste mass closure',
          [(2,5),(3,5),(4,6),(3,7)],
          ['EXACT protein/fat: captured solids cannot also be credited as downstream whey protein (1-7).',
           'CONSTITUTIVE: size-dependent capture and shear fragmentation require measured curves (2-3).',
           'ENGINEERING: curd use, sanitation and membrane feed quality remain qualified (4-6).',
           'ECONOMIC: price is marginal value versus existing fines use, not whole cheese selling price.'],
          'A clarified-liquid specification can hide valuable fines sent downstream or to waste and double-count them as recovered protein.',
          'Separate and assay fines before membrane feed, accounting for alternate use value and downstream yield.',
          ['Equal whey turbidity can represent different curd sizes and saleable recovery.',
           'All whey solids need not be sent through the membrane.',
           'Screen only if additional marginal curd value exceeds sanitation and pumping costs.'],
          'Delta_m=V*c_fines*Delta_eta; V m3/y, c kg/m3, eta dimensionless. Protein balance includes downstream decrease.',
          dict(whey_m3_y=2e6,fines_kg_m3=.2,additional_capture=.5,marginal_USD_kg=2),
          2e6*.2*.5,2,70000,600000,'additional qualifying fines kg/y',
          'Commercial fine-saving screens and centrifugal clarification before membrane processing.',
          'KNOWN','Curd-fines screens and recovery are disclosed decades ago.',
          ['https://patents.google.com/patent/CA1144083A/en','https://patents.justia.com/patent/5167807'],
          'Captured protein merely displaces equally valued downstream product or recovered fines fail use qualification.',
          'Delta_eta=0 or fines concentration zero eliminates benefit.',
          'Target additional 200,000 kg/y qualifying fines; downstream value loss must already be included in $2/kg.'))
        c.append(case(88,'Segregate fermentation CO2 by oxygen-front and impurity qualification',
          'Fermenter air displacement | CO2 generation | Startup gas diversion | Gas composition qualification | Recovery purification | CO2 storage | Beverage reuse',
          [(1,4),(3,5),(4,7),(5,7)],
          ['EXACT gas species: CO2, O2, nitrogen, volatiles and moisture close through all vents/storage (1-7).',
           'CONSTITUTIVE: purification performance changes with inlet impurity burden (4-5).',
           'ENGINEERING: beverage-grade acceptance is independent of CO2 percentage alone (7).',
           'ECONOMIC: recovered gas credited only when it displaces actual purchased gas, net of purification.'],
          'A timer-based recovery handoff may reject usable gas or admit an impurity front.',
          'Qualify composition-dependent diversion and purification within existing gas standards.',
          ['Equal CO2 flow can have different oxygen and volatile contamination.',
           'Discarding an entire fixed startup duration is not inherently necessary.',
           'Measured qualifying gas displacing purchase determines value, not total fermentation CO2.'],
          'm_usable=m_vent*f_qual*eta; kg/y. Headspace ideal flushing y_O2=y0*exp(-V_CO2/V_head) assumes perfect mixing, no O2 source.',
          dict(vent_CO2_t_y=1000,additional_qualified_recovery_fraction=.6,CO2_USD_t=300),
          1000*.6,300,60000,700000,'additional purchased CO2 displaced t/y',
          'Modern oxygen-monitored recovery with stripping/purification and composition-based collection.',
          'KNOWN','Initial air exclusion and impurity-aware brewery CO2 recovery are explicitly prior art.',
          ['https://patents.google.com/patent/WO1999013049A2/en','https://patents.google.com/patent/US20160003532A1/en'],
          'Other contaminants fail qualification, no purchased-gas demand coincides, or optimized recovery already collects it.',
          'f_qual=0 or no displaced purchase gives no economic value.',
          '600 t/y additional qualified recovery is assumed; not a measured recovery yield.'))
        c.append(case(89,'Recover ethanol carried from fermentation into the vent condenser',
          'Broth fermentation | Ethanol-water vapor loading | Vent gas conduit | Chilled condenser | Collected ethanol solution | Recovery distillation | Clean gas discharge',
          [(2,7),(4,7),(5,1),(4,6)],
          ['EXACT ethanol/water: condensed and vented components close the fermenter balance (1-7).',
           'EXACT energy: latent and sensible loads enter condenser work and downstream distillation (4-6).',
           'CONSTITUTIVE: VLE and mass-transfer limits replace ideal complete capture (2-4).',
           'ENGINEERING: fermenter pressure, sterile boundary, emissions and product quality remain controlled.'],
          'Broth yield alone omits ethanol leaving in CO2 and the energy needed to recover its dilute condensate.',
          'Qualify vent condensation versus water scrubbing on whole-process ethanol and energy balances.',
          ['Equal broth ethanol can have different offgas losses.',
           'Venting all noncondensable gas need not vent all ethanol.',
           'Condense only when net recovered-ethanol contribution exceeds refrigeration and reconcentration.'],
          'Delta_m=m_ethanol,vent*eta; Q=m_cond*h_fg+Q_sensible; W=Q/COP. m kg/y; h_fg kJ/kg; Q kJ/y.',
          dict(vent_ethanol_t_y=300,additional_capture=.7,net_ethanol_USD_t=700),
          300*.7,700,40000,500000,'additional net ethanol recovered t/y',
          'Optimized vent scrubber/condenser with distillation integration; site VLE required.',
          'KNOWN','Fermentation headspace condenser recovery directly disclosed.',
          ['https://patents.google.com/patent/US20160244704A1/en','https://patents.google.com/patent/US9221735B2/en'],
          'Extra water condensation/reboiling or pressure impact outweighs product; existing scrubber already captures it.',
          'Zero ethanol vapor or equal existing capture produces zero increment.',
          '210 t/y extra ethanol is an assumed recoverable stream; all downstream energy must fit $40,000/y OPEX.'))
        c.append(case(90,'Return foam-breaker liquid while preserving cell and product inventories',
          'Aerobic broth | Rising foam | Mechanical foam collapse | Liquid and cell separation | Qualified broth return | Offgas release | Product harvest',
          [(3,6),(4,7),(5,1),(4,6)],
          ['EXACT liquid/cell/product: foam collapse redistributes mass; it does not create product (1-7).',
           'CONSTITUTIVE: foam drainage, shear survival and product partition depend on culture (2-5).',
           'ENGINEERING: sterile return and oxygen transfer must stay within validated domain (5).',
           'ECONOMIC: harvestable product alone has credit; biomass returned but later lost cannot be valued twice.'],
          'Foam volume understates liquid/product export and omits return-line cell damage.',
          'Assay collapsed liquid and cells, then return only qualified fractions or collect usable product.',
          ['Equal foam height can carry different liquid and product masses.',
           'Discarding all foam or adding more antifoam is not universally necessary.',
           'Recovery must outperform an optimized conventional foam breaker after shear and sanitation costs.'],
          'Delta_m=V_foam_liquid*c_product*Delta_eta; V L/y, c kg/L, eta dimensionless.',
          dict(entrained_liquid_L_y=100000,product_kg_L=.02,additional_capture=.7,net_USD_kg=50),
          100000*.02*.7,50,30000,200000,'additional qualifying product kg/y',
          'Mechanical foam breakers with broth recycle or cell harvest, plus culture-specific shear/sterility validation.',
          'KNOWN','Phase-separated foam liquid return/harvest is directly disclosed.',
          ['https://patents.google.com/patent/US4340677A/en','https://patents.google.com/patent/US4373024A/en'],
          'Returned cells lose viability or harvested product is already credited in final batch yield.',
          'No entrained product means no product benefit even if visible foam disappears.',
          '1,400 kg/y extra qualifying product is an assumed target; not a fermentation yield forecast.'))
        c.append(case(91,'Separate sugar-centrifuge wash tails from impurity-rich mother liquor',
          'Massecuite feed | Centrifugal mother-liquor discharge | Crystal wash | Time-resolved runoff assay | Clean wash-tail return | Impurity purge | Sugar quality',
          [(2,6),(4,6),(5,1),(3,7)],
          ['EXACT sucrose/non-sugar: both species close around recycle and purge (1-7).',
           'CONSTITUTIVE: wash dissolves sucrose as it removes syrup; purity is not Brix alone (3-4).',
           'ENGINEERING: final crystal color/purity and crystallizer capacity unchanged (5-7).',
           'ECONOMIC: reprocessing and displaced molasses value subtract from recovered sugar.'],
          'Combining low-purity mother liquor with higher-purity later wash can export sucrose unnecessarily or recycle impurities.',
          'Switch runoff destination on verified sucrose/impurity purity, with complete recycle cost.',
          ['Equal runoff Brix can contain different sucrose/non-sugar proportions.',
           'All centrifuge runoff need not share one destination.',
           'A split is useful only when extra crystallizable sucrose exceeds reheating and evaporation costs.'],
          'Delta_m=M_sugar*f_dissolved*Delta_recovery; kg/y. Impurity steady state requires input=purge+product, never unlimited recycle.',
          dict(sugar_t_y=500000,wash_dissolution_fraction=.0025,additional_recovery=.5,net_USD_t=500),
          500000*.0025*.5,500,70000,700000,'extra sugar equivalent t/y',
          'Purity-controlled green/white runoff segregation in modern centrifugals.',
          'KNOWN','Timed and assay-guided runoff segregation are explicitly prior art.',
          ['https://patents.google.com/patent/US2347157A/en','https://patents.google.com/patent/US20240173726A1/en'],
          'Impurity accumulation or evaporation load offsets gain; optimized existing separator already splits correctly.',
          'Zero dissolved sugar or equal baseline split gives zero recovery gain.',
          '625 t/y additional crystallizable sugar is assumed, net of existing molasses credit.'))
        c.append(case(92,'Reuse vegetable blanch water across qualified temperature and species stages',
          'Clean cooling water | Cooked-product cooling | Water composition check | Earlier blanch stage | Raw-product preheat | Bleed and treatment | Product enzyme/quality check',
          [(2,7),(3,7),(4,7),(5,6)],
          ['EXACT energy: recovered heat equals hot-stream loss after exchanger/mixing losses (1-5).',
           'EXACT species: nutrients, allergens, soil and chemicals remain separately conserved or explicitly reacted (2-6).',
           'ENGINEERING: required enzyme inactivation, microbial controls and product separation remain intact (7).',
           'ECONOMIC: water and heat have distinct avoided purchases; do not double-count avoided wastewater heating.'],
          'Temperature-only reuse can preserve heat while transferring an inadmissible food species or contaminant.',
          'Route countercurrent water only within qualified product campaigns and maintain explicit species bleed.',
          ['Equal water temperature and clarity do not establish equal chemical or microbial suitability.',
           'Fresh water at every upstream stage is not always necessary; validated hygiene remains necessary.',
           'Reuse value depends on accepted campaigns, bleed and treatment costs.'],
          'Q=V*rho*c_p*Delta_T; kJ/y with V m3/y,rho kg/m3,c_p kJ/kg/K. Gross=V*p_water+Q/1000*p_heat where p_heat USD/MJ.',
          dict(reused_water_m3_y=50000,water_USD_m3=3,Delta_T_K=40,rho=1000,cp=4.18,heat_USD_MJ=.015),
          1,50000*3+50000*1000*4.18*40/1000*.015,40000,500000,'fractions of stated annual reuse target',
          'Existing countercurrent integrated blancher/cooler plus validated water-hygiene controls.',
          'OVERLAP','Heat/water cascade is old; species-qualified switching needs site validation, no new preservation claim.',
          ['https://patents.google.com/patent/US4702161','https://patents.google.com/patent/FR2674100A1/en'],
          'Cross-product carryover, inadequate inactivation or treatment cost removes admissibility/value.',
          'No concurrent eligible stage or Delta_T=0 eliminates the respective recovery term.',
          'Assumed 50,000 m3/y reuse and 8.36 TJ/y useful heat displaced, without changing processing endpoints.'))
        c.append(case(93,'Close both oxygen and carbon-dioxide balances in produce package selection',
          'Harvested produce lot | Respiration characterization | Film/perforation choice | Sealed headspace | Temperature excursion | Gas and quality check | Shelf-life disposition',
          [(2,5),(3,6),(5,6),(6,3)],
          ['EXACT species: O2 and CO2 transfer/respiration and unchanged N2 determine total pressure and mole fractions in the declared rigid test volume (2-6).',
           'CONSTITUTIVE: respiration and film permeance depend on temperature/composition (2-5).',
           'ENGINEERING: oxygen lower and CO2 upper limits are commodity-specific; neither inferred from the other (6).',
           'EVIDENCE: gas-target satisfaction alone is not microbial safety or shelf-life validation (7).'],
          'An oxygen-only package match can satisfy O2 while accumulating damaging CO2 after a temperature change.',
          'Choose gas-selective film/perforation using jointly constrained balances and validate commodity quality.',
          ['Same O2 reading can coexist with different CO2 because permeance ratios differ.',
           'A single oxygen-optimal film is not sufficient or universally necessary.',
           'Extra film/testing expense needs independently measured additional avoided saleable loss.'],
          'B*dpO/dt=GO*(pO_air-pO)-R; B*dpC/dt=GC*(pC_air-pC)+RQ*R. Isothermal rigid 1 L test headspace, B=1 reference-L/atm; G reference-L/(h atm), R reference-L O2/h. pN=.7896 atm initially ambient and has zero driving force. P=pO+pC+pN; mole fractions yi=pi/P. Constant R is local; flexible-package/constant-pressure use is outside this contract.',
          dict(rigid_test_headspace_L=1,GO_refL_h_atm=.0625,R_refL_h=.01,RQ=1,pO_air_atm=.21,pCO2_air_atm=.0004,pN_atm=.7896,
               alpha_base=2,alpha_new=4,yO_min=.03,yCO2_max=.05,packages_y=1e6,extra_film_USD=.005,QA_USD_y=5000),
          None,1,10000,100000,'additional avoided loss USD/y',
          'Multigas respiration-transport MAP models from Renault 1994 onward already impose both species. Strong model predicts exactly the same result.',
          'KNOWN','Coupled multigas MAP is established; no predictive gain over modern models demonstrated.',
          ['https://academic.oup.com/ijfst/article/29/4/365/7867625','https://www.sciencedirect.com/science/article/pii/S0925521408001907'],
          'Flexible volume, imposed constant pressure, oxygen-limited respiration, condensation, leaks or microbial outcomes invalidate extrapolation of the rigid constant-R test model.',
          'R=0 approaches ambient pressure/composition; alpha→infinity suppresses CO2 partial-pressure buildup but total pressure and mole fractions must still be recomputed.',
          'At fixed R and GO, steady oxygen partial pressure=.05 atm; alpha=2 gives total P=.92 atm and O2=5.435%, CO2=8.739%; alpha=4 gives P=.88 atm and O2=5.682%, CO2=4.591%. Both pass the assumed 3% O2 floor, only alpha=4 passes 5% CO2 ceiling. A rigid test vessel must tolerate this pressure; no flexible-pack or shelf-life saving is inferred.'))
        c.append(case(94,'Regenerate ethylene adsorbent without sending a humidity/ethylene pulse back to fruit',
          'Humid fruit-store air | Side-stream contactor | Competitive adsorption | Bed isolation | Qualified dry regeneration | Rehumidified clean return | Fruit-quality check',
          [(3,6),(5,1),(4,6),(6,7)],
          ['EXACT ethylene/water: captured species leave in regeneration exhaust or remain stored (2-6).',
           'CONSTITUTIVE: competitive adsorption capacity depends on RH and co-adsorbates (2-3).',
           'ENGINEERING: fruit RH and ethylene bounds preserved, including reconnect transient (6-7).',
           'ECONOMIC: longer sorbent life must exceed drying, regeneration and makeup humidity cost.'],
          'A dry-gas sorbent capacity certificate can fail in a humid store; reconnecting a bed can desorb stored ethylene.',
          'Test a separately isolated regeneration/conditioning loop and verify reconnect gas before return.',
          ['Equal dry sorbent mass can have different available capacity after humid exposure.',
           'Whole-store dehumidification is not required just to regenerate an isolated bed.',
           'Avoided replacement cost, not assumed avoided spoilage, defines the screened value.'],
          'qE=qmax*bE*pE/(1+bE*pE+bW*pW); kg/kg with b inverse pressure. Savings=C_sorbent*f_life_gain minus annualized regeneration costs.',
          dict(annual_sorbent_replacement_USD=200000,replacement_cost_reduction=.5),
          200000*.5,1,40000,300000,'avoided sorbent purchase USD/y',
          'Humidity-resistant ethylene sorbents and EP0709122A1 isolated regeneration/conditioning cycle, plus breakthrough-qualified reconnect; no superiority over these established methods shown.',
          'OVERLAP','Independent referee found EP0709122A1 (1996): isolated fruit-container flow, external ethylene desorption, drying stage and humidity/temperature coupling. Cyclic arrangement strongly overlaps. The patent permits the drying stream to be container air; it does not establish a fully isolated pre-reconnect sensor guard. That exact guard remains UNRESOLVED and has no demonstrated benefit.',
          ['https://patents.google.com/patent/EP0709122A1/en','https://www.sciencedirect.com/science/article/pii/S0925521422000497','https://www.sciencedirect.com/science/article/abs/pii/S138358662401373X','https://patents.google.com/patent/CN101578978A/en'],
          'Regeneration emits an ethylene pulse, dries fruit, damages sorbent or costs more than a humidity-resistant conventional bed.',
          'pW=0 removes competitive-water penalty; no reversible capacity loss gives no regeneration gain.',
          '50% replacement-cost reduction is an unmeasured target; no spoilage reduction monetized.'))
        c.append(case(95,'Terminate vacuum cooling using both product enthalpy and saleable water loss',
          'Warm leafy produce | Chamber evacuation | Flash evaporation | Product temperature field | Qualified endpoint | Repressure and hydration check | Saleable quality',
          [(3,6),(4,7),(5,7),(2,5)],
          ['EXACT energy: product sensible cooling supplies evaporation plus parasitic heat (1-5).',
           'EXACT water: evaporated mass cannot remain in product inventory (3,6).',
           'ENGINEERING: warmest product, shelf life and acceptable water condition unchanged (4-7).',
           'ECONOMIC: only genuine retained saleable product valued, not arbitrary added water.'],
          'A pressure or average-temperature endpoint can continue removing water after useful cooling is complete.',
          'Use qualified spatial temperature and condensate/water balances to avoid overcooling; compare with optimized standard endpoint control.',
          ['Equal pressure can conceal warm interiors and unequal dehydration.',
           'A fixed extra vacuum dwell is not necessary after complete qualified cooling.',
           'Retained saleable yield must cover sensing and cycle changes; faster cycles are not assumed.'],
          'm_evap≈M*c_p*Delta_T/hfg for adiabatic cooling; M kg,c_p kJ/kg/K,hfg kJ/kg. Incremental water retention is not derivable from this bound alone.',
          dict(produce_kg_y=10e6,additional_saleable_fraction=.005,net_USD_kg=1),
          10e6*.005,1,20000,250000,'additional genuine saleable produce kg/y',
          'Coupled heat/mass/deformation vacuum-cooling models with optimization of time, temperature uniformity and weight loss.',
          'KNOWN','Endpoint and water-loss optimization already actively modeled; assumed site economics are negative.',
          ['https://www.sciencedirect.com/science/article/pii/S0260877426000609','https://www.sciencedirect.com/science/article/abs/pii/S0196890408001532'],
          'Retained water is gained at the expense of required cooling or disappears before sale.',
          'Delta_T=0 removes required sensible cooling; parasitic loads may still evaporate water.',
          'Target 50,000 kg/y genuinely retained saleable produce; not established by simulation or field observation.'))
        c.append(case(96,'Recover retort cooling-water heat without changing package pressure and lethality',
          'Validated retort hold | Controlled cooling onset | Segregated heat exchanger | Recovery tank | Next-batch preheat | Pressure-controlled final cool | Package integrity release',
          [(1,7),(2,6),(3,6),(4,5)],
          ['EXACT energy: recovered heat ≤ donor enthalpy and eligible next-batch demand (2-5).',
           'ENGINEERING: validated lethality/cooling schedule and container differential pressure unchanged (1,6,7).',
           'ENGINEERING: hygienic water segregation and package seal integrity preserved (3-7).',
           'ECONOMIC: storage losses and batch overlap charged; no shortened sterilization credit.'],
          'Cooling duty is often valued separately from next-batch heating, while recovering heat can disrupt pressure or timing.',
          'Use a segregated water/heat recovery store sized to matched eligible batches under the unchanged validated process.',
          ['Equal rejected heat totals can have different temperature/time availability and pressure obligations.',
           'Rejecting all cooling heat is not necessary; reducing validated treatment is not permitted by this model.',
           'Recovered useful heat after storage losses must pay for exchanger/store and operation.'],
          'Q_y=N*Mwater*c_p*Delta_T*epsilon; kJ/y. Q_use=min(Q_y,Q_demand); water kg, c_p kJ/kg/K.',
          dict(batches_y=5000,water_kg_batch=5000,Delta_T_K=80,cp=4.18,recovery=.5,heat_USD_MJ=.015),
          5000*5000*4.18*80*.5/1000,.015,15000,400000,'useful recovered heat MJ/y',
          'Regenerative/cascade retorts with water recovery and heat-exchanger integration.',
          'KNOWN','Direct prior art covers linked retort heat/water recovery; assumed retrofit is not economical.',
          ['https://patents.google.com/patent/EP4470390A1/en','https://patents.google.com/patent/US20110180232A1/en'],
          'No simultaneous/storage-compatible heat demand, altered schedule, package damage or hygiene failure rejects credit.',
          'epsilon=0 or no eligible sink gives zero recovery.',
          'Assumed useful heat recovery 4.18 TJ/y; no sterilization or throughput improvement claimed.'))
        c.append(case(97,'Recuperate carton sterilant-drying air only across a qualified residue boundary',
          'Carton sterilant application | Required contact | Hot-air residue removal | Exhaust heat exchanger | Fresh aseptic air preheat | Residue verification | Fill and seal',
          [(2,6),(3,6),(4,5),(5,3)],
          ['EXACT energy: sensible exhaust heat recovery bounded by source/sink heat capacities (3-5).',
           'EXACT species: peroxide and water vapor cannot be assumed absent after heat exchange (3-6).',
           'ENGINEERING: required sterilant treatment, residue and aseptic-air conditions unchanged (2,6,7).',
           'ENGINEERING: fouling/leak detection and pressure ordering belong to independent equipment qualification.'],
          'Energy recovery can transfer residual sterilant or contaminate clean drying air if only temperature is tracked.',
          'Assess isolated recuperation with independently qualified leak/residue controls, not direct dirty-air recirculation.',
          ['Equal exhaust temperature can hide different peroxide loading and admissibility.',
           'New heat for all drying air is not necessary when isolated recovery is feasible.',
           'Small air heat duty must exceed exchanger and verification costs.'],
          'Qdot=epsilon*m_air*c_p*(T_hot-T_cold); kW with kg/s,kJ/kg/K,K. E=Qdot*h, kWh/y.',
          dict(air_kg_s=1,cp=1,Delta_T_K=80,epsilon=.6,h_y=5000,heat_USD_kWh=.10),
          .6*1*1*80*5000,.10,5000,150000,'useful recovered kWh/y',
          'Aseptic air/peroxide recovery systems and heat exchangers already qualified for residue and hygiene.',
          'OVERLAP','Peroxide removal/recovery loops are old; exact isolated heat integration unresolved but this cost scenario fails.',
          ['https://patents.google.com/patent/EP0502645B1/en','https://patents.google.com/patent/EP3895998B1/en'],
          'Residue/sterility endpoint changes, dirty-to-clean leak or retrofit costs exceed heat value.',
          'Equal inlet/exhaust temperatures give zero recuperation regardless of exchanger area.',
          'Assumed recoverable 48 kW or 240,000 kWh/y; no release or safety certification follows.'))
        c.append(case(98,'Recover desolventizer vapor heat while preserving solvent and meal-quality closure',
          'Solvent-wet oilseed meal | Desolventizer heating | Mixed steam-solvent vapor | Dust removal | Qualified vapor reuse | Final meal solvent/toast check | Condensed solvent return',
          [(3,7),(4,7),(5,2),(5,6)],
          ['EXACT solvent/water: reuse, product residue, recovered liquid and vent inventories close (1-7).',
           'EXACT energy: reused vapor replaces only actually displaced steam; compression/ejector work charged (2-5).',
           'ENGINEERING: residual solvent and meal protein/toasting criteria unchanged (6).',
           'ENGINEERING: flammability/pressure and dust handling remain installation-qualified.'],
          'Vapor heat and solvent recovery evaluated separately can overstate steam savings or return unwanted solvent to dry meal.',
          'Qualify vapor routing jointly with final residual solvent and meal treatment, comparing existing vapor-recovery trays.',
          ['Equal vapor enthalpy can have different solvent fraction and reuse suitability.',
           'Fresh steam need not supply all heat; solvent removal remains necessary.',
           'Incremental steam displacement after compression and solvent penalties drives value.'],
          'Delta_msteam=M_meal*delta_s; M t/y,delta_s kg/t. Gross=Delta_msteam*psteam. Full enthalpy and component balances qualify delta_s.',
          dict(meal_t_y=1e6,additional_steam_displacement_kg_t=20,steam_USD_kg=.03),
          1e6*20,.03,100000,2e6,'additional steam displaced kg/y',
          'Modern desolventizer-toaster vapor recycle/scavenger systems with solvent and meal-quality control.',
          'KNOWN','Solvent/steam vapor recycling and heat recovery directly disclosed.',
          ['https://patents.google.com/patent/US9250013B2/en','https://patents.google.com/patent/US9683778B2/en'],
          'Final solvent or meal quality worsens, recycled vapor substitutes no fresh steam, or best existing recovery already achieves it.',
          'No additional steam displacement means no fuel credit even with a large circulating vapor flow.',
          '20 million kg/y extra displaced steam is assumed; no validated plant energy balance establishes it.'))
        c.append(case(99,'Control potato steam-peel exposure to loosen skin without sacrificing edible tissue',
          'Potato size/skin lot | Pressurized steam pulse | Skin softening front | Rapid decompression | Peel removal | Edible yield sorting | Downstream texture check',
          [(1,3),(2,7),(3,6),(4,6)],
          ['EXACT edible solids: removed peel plus retained edible tissue close; water changes are separate (1-6).',
           'CONSTITUTIVE: thermal diffusion and skin weakening depend on size, cultivar and age (2-4).',
           'ENGINEERING: residual skin, texture, throughput and food controls unchanged (5-7).',
           'ECONOMIC: avoided edible loss valued against existing byproduct destination, not full retail value.'],
          'Successful skin removal can conceal excessive subskin cooking and edible loss downstream.',
          'Use size/skin-qualified pulse and decompression timing with downstream usable-solid yield as endpoint.',
          ['Equal skin removal can hide different cooked-layer depths and edible yield.',
           'Longer uniform steam treatment is not necessary for every lot.',
           'Only extra usable potato at equal peel quality and throughput generates value.'],
          'Thermal depth scales ell~sqrt(alpha*t); alpha m2/s,t s. Value=M*Delta_y*p; M t/y,p USD/t. Scaling is not a peeling law.',
          dict(potatoes_t_y=200000,additional_usable_fraction=.003,net_USD_t=400),
          200000*.003,400,30000,700000,'additional usable potatoes t/y',
          'Calibrated steam-peeling heat penetration, cyclic treatment and optical peel/yield control.',
          'KNOWN','Exposure/cycle versus heat penetration and yield was experimentally studied long before this pass.',
          ['https://www.sciencedirect.com/science/article/pii/S0260877400000327','https://www.sciencedirect.com/science/article/abs/pii/S0023643896901917'],
          'Yield increase represents residual skin/water rather than usable tissue, or texture/throughput deteriorates.',
          't→0 reduces heat penetration but may fail peeling entirely; zero-loss optimal baseline leaves no gain.',
          '600 t/y extra usable potato is an assumed target; heat-depth scaling does not establish it.'))
        c.append(case(100,'Recover controlled-atmosphere storage gas while removing respiratory CO2',
          'Fruit respiration | Store CO2 buildup | Side-stream compression | Selective CO2 separation | Nitrogen-rich return | Gas and pressure makeup | Fruit atmosphere qualification',
          [(1,7),(4,6),(5,1),(6,7)],
          ['EXACT gas species/pressure: CO2 removed and O2 consumed require independently balanced makeup (1-7).',
           'CONSTITUTIVE: membrane selectivity changes with pressure, humidity and gas mixture (3-4).',
           'ENGINEERING: fruit-specific O2/CO2/RH bounds preserved, including transients (7).',
           'ECONOMIC: nitrogen returned counts only as displaced purchased/generated nitrogen after compression cost.'],
          'Bulk purge to control CO2 also rejects conditioned nitrogen and can induce oxygen makeup errors.',
          'Compare selective gas recovery and return with optimized scrubbers, including all gas components and pressure.',
          ['Equal store CO2 can occur with unequal O2 and nitrogen losses.',
           'Whole-atmosphere purge is not necessary to remove CO2 selectively.',
           'Gas purchase avoided must outweigh compression and equipment; low purge sites fail.'],
          'Delta_VN=VN_purge*recovery; Nm3/y at the same declared reference state. n_i,in+generation-consumption=n_i,out+Delta_n_i.',
          dict(eligible_N2_purge_Nm3_y=200000,recovery=.5,N2_USD_Nm3=.2),
          200000*.5,.2,15000,200000,'purchased nitrogen displaced Nm3/y',
          'Integrated membrane return/makeup and low-oxygen scrubber regeneration recovery, published decades ago.',
          'KNOWN','Direct disclosure US5120329A matches selective CO2 removal with nitrogen/oxygen recycle.',
          ['https://patents.google.com/patent/US5120329','https://patents.google.com/patent/US8551215B2/en'],
          'Compressor cost, membrane losses or gas-quality changes exceed benefit; best existing scrubber already preserves gas.',
          'No purge or no displaced nitrogen purchase gives zero gross credit.',
          'Assumed 100,000 Nm3/y nitrogen displacement; financial screen is negative.'))
        # Explicit topology: branches are not forced into a linear chronology.
        graphs={
          81:[(1,2),(2,3),(3,4),(3,5),(5,6),(4,7),(4,6)],
          82:[(1,2),(2,3),(3,4),(4,5),(5,6),(6,7),(1,4),(4,7),(5,7)],
          83:[(1,2),(2,3),(3,4),(4,5),(5,6),(6,7),(2,5),(3,7),(5,7)],
          84:[(1,2),(2,3),(3,4),(4,5),(4,6),(2,6),(4,7),(6,7),(5,1)],
          85:[(1,2),(2,3),(3,4),(4,5),(2,5),(5,6),(2,7),(5,7)],
          86:[(1,2),(2,3),(3,4),(4,5),(2,6),(3,6),(4,7),(7,5)],
          87:[(1,2),(2,3),(3,4),(3,5),(4,6),(5,6),(3,7),(4,7),(5,7)],
          88:[(2,1),(1,3),(2,3),(3,4),(4,5),(5,6),(6,7),(4,7)],
          89:[(1,2),(2,3),(3,4),(4,5),(5,6),(4,7),(5,1),(4,6)],
          90:[(1,2),(2,3),(3,4),(4,5),(5,1),(3,6),(4,7),(4,6)],
          91:[(1,2),(1,3),(3,4),(4,5),(5,1),(2,6),(4,6),(3,7)],
          92:[(1,2),(2,3),(3,4),(4,5),(5,6),(2,7),(3,7),(4,7)],
          93:[(1,2),(2,3),(3,4),(4,5),(5,6),(6,7),(2,5),(3,6),(6,3)],
          94:[(1,2),(2,3),(3,4),(4,5),(5,6),(6,7),(3,6),(4,6),(6,1)],
          95:[(1,2),(2,3),(3,4),(4,5),(5,6),(6,7),(3,6),(4,7),(5,7),(2,5)],
          96:[(1,2),(2,3),(3,4),(4,5),(2,6),(6,7),(1,7),(3,6)],
          97:[(1,2),(2,3),(3,6),(6,7),(3,4),(4,5),(5,3),(2,6)],
          98:[(1,2),(2,3),(3,4),(4,5),(5,2),(2,6),(3,7),(4,7),(5,6)],
          99:[(1,2),(2,3),(3,4),(4,5),(5,6),(6,7),(1,3),(2,7),(3,6),(4,6)],
          100:[(1,2),(2,3),(3,4),(4,5),(5,1),(4,6),(6,7),(1,7),(5,7)]}
        for a in c:
            a['edges']=graphs[int(a['id'][1:])]
            a['edge_contract']='Directed physical sequence, branch, recycle or downstream constraint dependency; domain flow/precedence fields are not invented Core Relation types. Source-to-target effects are constrained by the numbered-node invariant scopes.'
        return c


    def deep_tests():
        # N084: whole solute balance, diminishing returns, wash cost and modern baseline.
        m0=1000*.05*.4  # 20 kg solute in liquor on a 1000 kg ice batch.
        L=50.0
        recovery=lambda N: m0*(1-math.exp(-N))
        N50=math.log(2); N90=math.log(10)
        assert abs(recovery(N50)-10)<1e-12
        assert abs(recovery(N90)-18)<1e-12
        assert abs(recovery(N90)+m0*math.exp(-N90)-m0)<1e-12
        assert recovery(0)==0 and recovery(10)<m0
        # A fixed 400,000 kg/y extra wash-water assumption is NOT consistent with
        # this well-mixed model's L=50 kg/batch and 20,000 batches/year.
        # Enforce measured/required water accounting instead of silently retaining it.
        extra_wash=(N90-N50)*L*20000
        extra_cost=extra_wash*.7*.1
        modeled_net=160000*1.5 - 50000 - extra_cost - CRF*400000
        assert extra_wash>400000
        # Best existing wash column uses same model and endpoint -> zero physical increment.
        strong_delta=recovery(N90)-recovery(N90)
        assert strong_delta==0
        # Optimum of per-batch solute revenue minus water-removal cost.
        value_kg=1.5; water_cost_kg=.7*.1
        Nopt=max(0,math.log(m0*value_kg/(L*water_cost_kg)))
        deriv=lambda n: m0*value_kg*math.exp(-n)-L*water_cost_kg
        assert abs(deriv(Nopt))<1e-12
        assert deriv(Nopt-.1)>0 and deriv(Nopt+.1)<0
        # N093: closed-form species balances versus numerical integration.
        V=1.; KO=.0625; R=.01; yoa=.21; yca=.0004
        def exact(t,alpha):
            ysO=yoa-R/KO; ysC=yca+R/(alpha*KO)
            return (ysO+(yoa-ysO)*math.exp(-KO*t/V),ysC+(yca-ysC)*math.exp(-alpha*KO*t/V))
        def numerical(t,alpha):
            yO,yC=yoa,yca; dt=.001
            for _ in range(round(t/dt)):
                yO+=dt*(KO*(yoa-yO)-R)/V
                yC+=dt*(alpha*KO*(yca-yC)+R)/V
            return yO,yC
        for alpha in (2.,4.):
            ex=exact(96,alpha); nu=numerical(96,alpha)
            assert max(abs(a-b) for a,b in zip(ex,nu))<2e-6
        base=exact(96,2); candidate=exact(96,4)
        pN=.7896
        total_base=sum(base)+pN; total_candidate=sum(candidate)+pN
        base_y=tuple(p/total_base for p in base)
        candidate_y=tuple(p/total_candidate for p in candidate)
        assert base_y[0]>=.03 and candidate_y[0]>=.03
        assert base_y[1]>.05 and candidate_y[1]<.05
        assert .8<total_candidate<total_base<1.0
        assert abs(sum(base_y)+pN/total_base-1)<1e-12
        assert abs(sum(candidate_y)+pN/total_candidate-1)<1e-12
        # Null: modern multigas baseline at same alpha exactly predicts candidate.
        assert candidate==exact(96,4)
        # Temperature excursion doubles R without matched permeance increase:
        # constant-R equilibrium O2 becomes negative, marking the model/domain invalid.
        invalid_hot_O2=yoa-2*R/KO
        assert invalid_hot_O2<0
        cases=run()
        corrected=next(a for a in cases if a['id']=='N084')
        assert abs(corrected['financial']['net']-modeled_net)<1e-8
        assert abs(corrected['inputs']['extra_wash_water_kg_y']-extra_wash)<1e-8
        assert len(cases)==20 and len({a['id'] for a in cases})==20
        for a in cases:
            assert 5<=len(a['nodes'])<=9
            assert all(1<=x<=len(a['nodes']) and 1<=y<=len(a['nodes']) for x,y in a['edges'])
            assert len(set(a['edges']))==len(a['edges'])
            f=a['financial']
            if f['gross'] is not None:
                assert abs(f['net']-(f['gross']-f['opex']-CRF*f['capex']))<1e-8
        return dict(N084=dict(entrained_solute_kg_batch=m0,baseline_recovery_kg=10,candidate_recovery_kg=18,
                 required_extra_wash_kg_y=extra_wash,extra_water_removal_cost=extra_cost,
                 modeled_net_USD_y=modeled_net,optimal_wash_pore_volumes=Nopt,
                 strongest_baseline_increment_kg=strong_delta,
                 interpretation='Simple economic target understates wash duty; corrected mixed-wash model is the admissible modeled scenario.'),
               N093=dict(base_partial_pressures_atm_96h=base,candidate_partial_pressures_atm_96h=candidate,
                 base_total_atm=total_base,candidate_total_atm=total_candidate,
                 base_mole_fractions_96h=base_y,candidate_mole_fractions_96h=candidate_y,
                 steady_O2_partial_atm=.05,base_steady_CO2_partial_atm=.0804,candidate_steady_CO2_partial_atm=.0404,
                 hot_constant_R_equilibrium=invalid_hot_O2,
                 interpretation='Multigas baseline ties. Negative hot equilibrium is DOMAIN_FAILURE, not negative physical oxygen or proof of shelf life.'))

    return run(), deep_tests()



EXPECTED = {1: 500 * 500 * 0.4, 2: 400 * 1500 * 0.25, 3: 600 * 3600 * (1 - (1 - 0.3) / (1 - 0.1)) * 0.2, 4: 8000 * 40 * 1, 5: 1000 * 1000 * 0.15, 6: 1320 * (20 * 5) * 2.5, 7: 10000000.0 * 0.02 * 2, 8: 8000000.0 * 0.02 * 0.1, 9: 10000000.0 * 0.018 * 0.75 * 13.9 * 0.8 * 0.05, 10: 800000 * 0.5 * 0.5, 11: 8000000.0 * (0.8 - 0.75) * 2, 12: 20000000.0 * 0.001 * 2, 13: 1000 * 500 * 0.6, 14: 30000000.0 * 0.005 * 1.5, 15: 8000 * 300 * 0.03, 16: 500000 * 0.2 * 2, 17: 50000000.0 * (10 / 1000) * 3, 18: 1000 * 2 * (15 - 5) * 10, 19: 500000 * 0.4 * 0.8, 20: 5000000.0 * (10 / 1000) * 0.5, 61: 30000000.0 * 0.01 * 0.06, 62: (100000 - 20000) * 0.08, 63: 5000 * 2 + 100000 * 0.06, 64: 2 * 6000 * 0.1, 65: None, 66: 0.8 * 0.1 * (1000 ** 2 - 60 ** 2) / 2 / 3600000.0 * 10 * 1000 * 0.1, 67: 50 * 0.2 * 3000 * 0.4 * 0.12, 68: 10 * 1000 * 200 / 55 * 1, 69: ((2 - 0.4) * 4000 + 4000) * 0.1, 70: (25 * 3000 * 0.3 - 10000) * 0.12, 71: 12 * 500 * 5, 72: (2500 - 2 * 25556887.5 / (10512 + math.sqrt(10512 ** 2 - 4 * 0.11 * 25556887.5))) * 10000 / 1000 * 6000 * 0.08, 73: None, 74: 5 * 500 * 5, 75: 100000 * 2000 * 0.002 * 0.08, 76: 4000 * 10 / 3600 * 0.9 * 10000 * 0.12, 77: 1000 * 8760 * (1 / 0.96 - 1 / 0.99) * 0.7 * 0.1, 78: 16 * 0.08 * (1000 - 200) * 0.15, 79: 4 * 15000, 80: (0.1 * 50 ** 2 + 0.2 * 50 ** 2 - (0.1 * (0.2 * 100 / 0.3) ** 2 + 0.2 * (0.1 * 100 / 0.3) ** 2)) * 8000 * 0.08, 21: 5000000.0 * 0.02 * (5 - 0.0001 * 6000), 22: 5000000.0 * 0.005 * 0.0025 * 6000, 23: 2000000.0 * 0.005 * 0.003 * 6000, 24: 100000 * 15 * 0.1, 25: 200000 * (0.1 * (4 + 0.3 * 2 ** 2) + 1000 * (0.12 + 0.08 * math.exp(-1) - 0.08) * 2.5 / 0.75 * 0.01 - (0.1 * (4 + 0.3 * (4.625951890040168 - 1) ** 2) + 1000 * (0.12 + 0.08 * math.exp(-(4.625951890040168 - 1) / 2) - 0.08) * 2.5 / 0.75 * 0.01)), 26: 300 * 8000 * 0.04, 27: 200000 * 0.015 * 50, 28: 20000 * 0.04 * 17 / 41 * 0.15 * 300, 29: 200000 * 0.01 * 30, 30: 300000 * 0.002 * 200, 31: 200000 * 0.002 * 150, 32: 200000 * 5 * 0.01 * 10, 33: 1000000.0 * 0.003 * 20, 34: 5000000.0 * 0.002 * 5, 35: 200000 * 0.3 * 0.2 / 1000 * 2000, 36: 200000 * 10 * 0.1, 37: 200000 * 0.05 * 4, 38: 100000 * 0.1 * 12, 39: 100000 * 0.1 * 15, 40: 100000 * 1000 * 0.01 * 2.5 / 0.7 / 1000 * 10, 41: 1000 * 20 * 4 * 0.12, 42: 1200 * 10 / 60 * 200, 43: 3 * 6000 * 0.25, 44: 600000 * 0.005 * 12, 45: 20000 * 0.1 * 60, 46: 5000 * 0.015 * 500, 47: None, 48: 4000 * 0.5 * 0.02 * 80, 49: 200000 * (1 / 0.45 - 1 / 0.46) * 2.6 / 0.85 * 8, 50: 150000 * 0.2 * 3, 51: 80000000 * 0.005 * 0.35, 52: 30000000 * 0.003 * 0.6, 53: 1000 * 20 * 3 + 1000 * 20 * 1000 * 4.18 * 30 / 3600 / 0.85 * 0.04, 54: 10000000 * (0.8 - 0.65) * 0.25 * (1 - 0.9) * 0.5, 55: 100000 * (0.5 - 0.35) * (0.2 * 3 + 2), 56: 20000 * 20 * 2 / 1000 * 8, 57: 100000 * 10 / 3600 * 150, 58: 100000 * 1.5 / 1000 * 20, 59: 10000 * 0.03 * 60, 60: 100000 * 0.004 * 150, 81: (50000000.0 - 50000000.0 * (1 - 0.8) / (1 - 0.7)) * 0.75 * 0.04, 82: 100 * 200 * 0.12, 83: 100000 * 0.005 * 150, 84: 20000000.0 * 0.05 * 0.4 * (0.9 - 0.5) * 1.5, 85: 50000000.0 * 0.002 * 3, 86: 200000 * 0.6 * 2.5, 87: 2000000.0 * 0.2 * 0.5 * 2, 88: 1000 * 0.6 * 300, 89: 300 * 0.7 * 700, 90: 100000 * 0.02 * 0.7 * 50, 91: 500000 * 0.0025 * 0.5 * 500, 92: 50000 * 3 + 50000 * 1000 * 4.18 * 40 / 1000 * 0.015, 93: None, 94: 200000 * 0.5, 95: 10000000.0 * 0.005 * 1, 96: 5000 * 5000 * 4.18 * 80 * 0.5 / 1000 * 0.015, 97: 0.6 * 1 * 1 * 80 * 5000 * 0.1, 98: 1000000.0 * 20 * 0.03, 99: 200000 * 0.003 * 400, 100: 200000 * 0.5 * 0.2}

EXPECTED_VARIABLE_OPEX = {81: (50000000.0 - 50000000.0 * (1 - 0.8) / (1 - 0.7)) * 0.025 * 0.12 + 33000, 84: 20000000.0 * 0.05 * math.log(5) * 0.7 * 0.1 + 50000, 55: 5000 + 100000 * 5 / 3600 * 40, 60: 5000 + 100000 / 100 * (math.log(100) / 0.05 - 30) / 3600 * 100, 74: 3000 + 5000 * 10 / 3600 * 1000 * 0.02}

def independent_financial_check(records):
    numeric, unknown, max_delta, variable_opex_checks = 0, 0, 0.0, 0
    for case in records:
        index = int(case['id'][1:])
        require(index in EXPECTED, f"Independent arithmetic missing {case['id']}")
        gross = EXPECTED[index]
        f = case['financial']
        if gross is None:
            require(f['gross'] is None and f['net'] is None, 'Unknown became numeric')
            unknown += 1
            continue
        delta = abs(gross-f['gross'])
        max_delta = max(max_delta,delta)
        require(delta < 1e-6, f"Independent gross mismatch {case['id']}")
        if index in EXPECTED_VARIABLE_OPEX:
            require(abs(EXPECTED_VARIABLE_OPEX[index]-f['opex']) < 1e-6,
                    f"Independent variable OPEX mismatch {case['id']}")
            variable_opex_checks += 1
        require(abs(gross-f['opex']-CRF*f['capex']-f['net']) < 1e-6,
                f"Independent net mismatch {case['id']}")
        numeric += 1
    return {'numeric_cases':numeric,'unquantified_cases':unknown,
            'maximum_gross_residual_USD_y':max_delta,
            'variable_OPEX_crosschecks':variable_opex_checks,
            'scope':'Scenario equations only; assumptions and field outcomes unverified'}

SOURCE_ROLE_SHA256 = {'separations': 'cfe897a2d6887f9d17155ef5a1e41f813ff431cfa1ad441e0d9fdb31b0240f11', 'materials': 'b13e1f6558235be467ced342eb42e48fba5d596111ce0d8a4b512a9aacc1244a', 'manufacturing': 'edcbc315d5093c987a2095c94d1828498d3689c83c678d16715a0d2e9c6475d5', 'electricity': '82dc3e9ac6348e72472db64cf5b7e926b545347b6581591f88c155980126ec66', 'food_bio': 'e635ee8c44ec2bd120a2f56cc9151c4548e52e7d99e3c0d0e29bd51658c23f60', 'independent_referee': '152a1bdbbf066fa28415d5a21dbd0ce527413d4073dd846ff767aca0e0db23e4'}

WORKSTREAMS = [
    ('separations', workstream_separations),
    ('materials', workstream_materials),
    ('manufacturing', workstream_manufacturing),
    ('electricity', workstream_electricity),
    ('food_bio', workstream_food_bio),
]

def prior_art_class(case):
    # Economic rejection is an independent axis, never a novelty category.
    ident = case['id']
    if case.get('prior_art_class') in {'KNOWN','OVERLAP','UNRESOLVED'}:
        return case['prior_art_class']
    if ident in {'N008','N009','N043','N054','N056','N058','N059'}:
        return 'KNOWN'
    if ident in {'N066','N070'}:
        return 'OVERLAP'
    if 'N021' <= ident <= 'N040':
        return case['novelty']
    status = case.get('status', 'UNKNOWN')
    return status if status in {'KNOWN','OVERLAP','UNRESOLVED'} else 'UNKNOWN'


def require(condition, message):
    if not condition:
        raise ValueError(message)


def audit(records):
    require([r['id'] for r in records] == [f'N{i:03}' for i in range(1,101)],
            'Expected exactly N001-N100 in order')
    totals = collections.Counter()
    art = collections.Counter()
    branch_totals = {}
    for r in records:
        ident = r['id']
        for field in ('title','nodes','edges','constraints','operators','equation',
                      'inputs','financial','baseline','sources','falsifier'):
            require(bool(r.get(field)), f'{ident}: missing {field}')
        require(len(r['nodes']) == len(set(r['nodes'])), f'{ident}: duplicate nodes')
        n = len(r['nodes'])
        seen = set()
        neighbors = {i:set() for i in range(1,n+1)}
        for edge in r['edges']:
            require(len(edge) == 2, f'{ident}: malformed edge')
            a,b = edge
            require(a in neighbors and b in neighbors and a != b,
                    f'{ident}: invalid endpoint {edge}')
            require((a,b) not in seen, f'{ident}: duplicate edge {edge}')
            seen.add((a,b)); neighbors[a].add(b); neighbors[b].add(a)
        reached, pending = set(), [1]
        while pending:
            node = pending.pop()
            if node not in reached:
                reached.add(node); pending.extend(neighbors[node]-reached)
        require(len(reached) == n, f'{ident}: disconnected case graph')
        for binding in r.get('constraint_bindings', []):
            require(1 <= binding['constraint'] <= len(r['constraints']),
                    f'{ident}: invalid constraint binding')
            require(all(i in neighbors for i in binding['nodes']),
                    f'{ident}: invalid constraint node')
        for constraint in r['constraints']:
            if isinstance(constraint, dict):
                require(bool(constraint.get('type')), f'{ident}: missing constraint type')
                require(all(i in neighbors for i in constraint.get('nodes',[])),
                        f'{ident}: invalid constraint scope')
        require(all(isinstance(s,str) and s.startswith('https://') for s in r['sources']),
                f'{ident}: malformed source reference')
        f = r['financial']
        if f.get('net') is None:
            require(f.get('gross') is None, f'{ident}: ambiguous unknown economics')
            totals['unquantified_economic_scenarios'] += 1
        else:
            for key in ('gross','opex','capex','net'):
                require(isinstance(f[key],(int,float)) and math.isfinite(f[key]),
                        f'{ident}: nonfinite financial {key}')
            require(f['opex'] >= 0 and f['capex'] >= 0, f'{ident}: negative implementation cost')
            expected = f['gross'] - f['opex'] - CRF*f['capex']
            require(math.isclose(expected,f['net'],abs_tol=1e-6),
                    f'{ident}: net arithmetic mismatch')
            totals['positive_conditional_scenarios' if f['net'] > 0 else
                   'negative_or_zero_conditional_scenarios'] += 1
        r['review_status'] = {
            'prior_art_class': prior_art_class(r),
            'canonical_admission': 'NONE',
            'formal_SAL_GCSC_typing': 'UNKNOWN',
            'field_validation': 'NOT_RUN',
            'measured_savings_USD_y': None,
            'measured_increment_vs_strongest_baseline_USD_y': None,
            'historical_novelty_demonstrated': False,
            'frontier_novelty_established': False,
            'economic_inputs': 'ASSUMED_PER_FACILITY',
        }
        totals['case_graphs'] += 1
        totals['situation_nodes'] += n
        totals['directed_edges'] += len(r['edges'])
        totals['constraint_records'] += len(r['constraints'])
        totals['operator_applications'] += 3
        art[prior_art_class(r)] += 1
        branch = r['source_role']
        b = branch_totals.setdefault(branch, collections.Counter())
        b.update(cases=1,nodes=n,edges=len(r['edges']),constraints=len(r['constraints']))
    # No denominator for all industrial reality or GCSC VALID_* classes exists.
    return {'counts':dict(totals), 'prior_art_classes':dict(art),
            'workstreams':{k:dict(v) for k,v in branch_totals.items()},
            'coverage_percentage':None, 'verified_novel_discoveries':0,
            'measured_economic_successes':0, 'independent_field_experiments':0,
            'formal_GCSC_coverage':'UNKNOWN',
            'TREE_CORE_build_integrity_debt':'NOT_RETESTED',
            'blind_matched_budget_benchmark':'NOT_RUN'}


def run_all():
    require(__debug__, 'Run without -O; physical assertions must remain enabled')
    records, physical = [], {}
    for name, func in WORKSTREAMS:
        cases, tests = func()
        for case in cases:
            case['source_role'] = name
        records.extend(cases)
        physical[name] = tests
    records.sort(key=lambda r:r['id'])
    summary = audit(records)
    independent = independent_financial_check(records)
    sealed = {'records':records,'physical':physical,'summary':summary,
              'independent_financial_review':independent}
    # Deterministic scientific adapter serialization, explicitly NOT GSL v3.
    payload = json.dumps(sealed,sort_keys=True,ensure_ascii=False,
                         separators=(',',':'),allow_nan=False).encode()
    sealed['research_output_sha256'] = hashlib.sha256(payload).hexdigest()
    return sealed


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--case', help='Print the full case contract, e.g. N072')
    parser.add_argument('--details',action='store_true',help='Print physical comparisons')
    args = parser.parse_args()
    result = run_all()
    if args.case:
        matches = [r for r in result['records'] if r['id']==args.case.upper()]
        if not matches:
            parser.error('Case must be N001 through N100')
        print(json.dumps(matches[0],indent=2,ensure_ascii=False,allow_nan=False))
        return
    print('NONCANONICAL RESEARCH — 100 investigations, not 100 novel discoveries')
    print('ASSUMED USD/facility/year; incremental field value versus strong methods UNKNOWN')
    print(json.dumps(result['summary'],indent=2,ensure_ascii=False))
    print('ID | prior-art class | conditional annual net | interface')
    for r in result['records']:
        net = r['financial']['net']
        money = 'UNKNOWN' if net is None else f'{net:,.2f}'
        print(f"{r['id']} | {prior_art_class(r)} | {money} | {r['title']}")
    print('INDEPENDENT ARITHMETIC REVIEW',result['independent_financial_review'])
    print('OUTPUT IDENTITY',result['research_output_sha256'])
    if args.details:
        print(json.dumps(result['physical'],indent=2,ensure_ascii=False,allow_nan=False))


if __name__ == '__main__':
    main()
