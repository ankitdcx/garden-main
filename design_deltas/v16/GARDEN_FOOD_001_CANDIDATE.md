# GARDEN-FOOD-001 — Modular Food Outlet and Replicable Chain Operating System

**Candidate:** G16-BP-FOOD-001 / GARDEN-FOOD-001. **Date:** 2026-11-24. **Revision:** 1.0.
**Status:** NONCANONICAL BUSINESS-PROCESS DESIGN; ECONOMICS UNVALIDATED; NOVELTY UNKNOWN.
**Provenance:** User-originated Shop project discussions November 23–24, 2026: small low-capital outlet, whole-wheat pizza, uniform ₹50 modular prices, low inventory, short preparation, trial before scale and ₹100/hour wage rising to ₹200 when profitable. Latest recovered Shop assistant summaries at 10:13, 10:36, 10:40 and 10:42 IST on Nov 24 supply the working recipes and operating estimates; earlier menus are superseded. Some detailed recipes were not recoverable. Assistant-added equations, safety gates and scale criteria are proposals, not user-approved facts. Research/design only; no commercial deployment or canon admission authorized by this document. Preserve existing Garden deployment restrictions and LICENSE.

## 1. Business invariant

A minimal, repeatable outlet combines a standard base, individually selectable toppings and a narrow rotating selection of sides/drinks/sweets, each sold in a single price quantum. Prepare shared components in advance, assemble to order, measure all costs and waste, and replicate only proven units. Generalize the reference pizza model to other cuisines only when safety, preparation and unit economics remain valid. Neither the generic modular menu nor the generic franchise concept is asserted novel.

### Reference menu (latest working version)

All customer prices are tax-inclusive ₹50 per module; 5 × 5 inches = 25 sq in per pizza portion. No maida. Vegetarian reference.

| Module | Portion | Gross customer price INR | Estimated direct cost INR |
|---|---|---:|---:|
| Atta-ghee-malai base | 1 (60 g dry atta) | 50 | 20 |
| Cheese | 20 g | 50 | 15 |
| Paneer | 40 g | 50 | 16 |
| Vegetables | 100 g | 50 | 15 |
| Mango lassi | 200 ml | 50 | 20 |
| Five-fruit drink | 200 ml | 50 | 20 |
| Chocolate dessert | 50 g | 50 | 20 |
| Royal Crunch Shrikhand | 56 g | 50 | 19.80 |
| Ghee potatoes | 125 g | 50 | 20 |
| Corn-kala chana chaat | 100 g | 50 | 20 |

Water allowance ₹5 per pizza order, counted once per qualifying order (not once per topping). Vegetable module: cauliflower, bhindi, baby corn, French beans 25 g each. Paneer ₹400/kg implies ₹16; cheese ₹500/kg implies ₹10 raw plus ₹5 unresolved allowance (do not assume it is measured packaging or waste). Verify vegetable ₹15/100 g and all other estimates against actual invoices/yield. Full ingredient recipes for base sauce/ghee/malai, five fruits, drinks, chocolate and sides are pending source recovery/recipe tests. No silent invented recipe. Two drinks, two desserts, two sides can rotate under a versioned recipe/price/allergen contract. Earlier chaas, ice cream, other veg and chicken options are historical, not current menu.

Royal Crunch Shrikhand: 50 g premium shrikhand ₹12.50; 3 g almond flakes ₹3.60; 1 g pistachio ₹1.60; 2 g roasted coconut ₹0.60; cup/spoon ₹1.50; total 56 g edible and ₹19.80. Milk/nut allergens disclosed.

For base + optional cheese, paneer, veg there are 2^3 = 8 combinations. With price 50(1+C+P+V) and cost 20+15C+16P+15V, gross price/direct cost pairs: basic 50/20, cheese 100/35, paneer 100/36, veg 100/35, cheese+paneer 150/51, cheese+veg 150/50, paneer+veg 150/51, all 200/66. Add water allowance and all missing variable costs before margin. Prices not profit.

## 2. Physical micro-outlet and operating configuration

200 sq ft trial takeaway; rent ₹20–25k/month; used reliable oven/fridge/freezer, food-safe counter, scales, utensils, sink/handwashing, potable water, exhaust, fire safety, simple billing, minimal decoration; buy fresh ingredients frequently. Earlier equipment budget ₹59.5–64.5k; bargain startup ₹1.09–1.25 lakh; ₹2 lakh conservative working capital target, all estimates. Refundable deposit (prior ₹50k assumption), advance rent, equipment, fitout/permits and reserve separately tracked; no double-counting. No mixer initially if measured hand-knead capacity sufficient. Clothing expansion excluded from food pilot; physically separate if later tested.

Trial: 4 service hours/day, 20 days, one month, one trained service worker where demonstrated adequate. 10 customers/hour target. Later 12 hours/day × 30 days, staffed in lawful shifts with relief, not one continuous 12h worker. ₹100/hour initial labor assumption, ₹200 if sustained economics allow. All prep/closing/cleaning/receiving and breaks/relief paid or imputed. Online orders optional and separately costed; delivery commissions/discounts/packaging and capacity included.

## 3. Standard process

Forecast demand by module -> procure approved suppliers -> receiving checks/lot and yield -> batch prep -> portion, label, safe hold -> accept order and compute module price -> assemble and bake -> serve drinks/sides/desserts -> bill and dispatch -> reconcile cash, ingredient inventory, time, waste and complaints -> revise next batch. Never serve expired/unsafe ingredients to protect margin. Can pre/par-bake tested bases, then final bake ~3–5 min target, handoff ~1 min; prior 5–8 min order-to-serve target is unvalidated. 10 customers/hr = one arrival per 6 minutes on average; actual simultaneous work, batch size, oven recovery, payment/packing, burst queues and cleaning must be timed.

Morning active prep estimate (minutes): dough 10–15; sauce/ghee/malai 5; roast vegetables 15–20; portion cheese/paneer 5–10; potatoes/corn/chana 5–10; drinks 5; chocolate dessert 10; shrikhand/nuts 5; organize 5 = 65–85. Passive proofing, cooking, cooling, sanitation, procurement and cleanup separate; scale to volume and measure; 65–85 is not a promise at 150 portions. Refrigerate perishables safely; use batch-sized replenishment, no all-day ambient holding.

Dough: 60 g dry atta per slice; 60% hydration. 40/80/120 portions need 2.4/4.8/7.2 kg flour; at one pizza per customer and 10 customers/hr this equals 4/8/12 service hours. 150 portions with buffer: 9 kg atta + 5.4 L water (approx 5.4 kg) + 160 g salt + 90 g sugar + 30 g yeast = 14.68 kg dough, ~97.9 g/portion before losses. 40 portions at proportional recipe ~3.915 kg (flour+water alone 3.84 kg); 120 ~11.744 kg (flour+water alone 11.52 kg). Buffer based on demand and safe holding, not compulsory production. Forecast actual pizza portions per customer separately from drinks/toppings and online demand.

## 4. Unit economics and proof obligations

For outlet i and day t: gross sales S=sum(price_j * paid units_j), net revenue R=S/(1+g) when applicable inclusive GST rate g, variable cost V=sum(actual used ingredient cost + packaging + water + waste + payment/delivery channel costs), labor L=sum(paid hours * wage), fixed expense F=rent+utilities+maintenance+insurance+admin etc, operating surplus O=R-V-L-F. Include spoilage only once (inventory reconciliation); track capex and refundable deposit separately, depreciation/financing and taxes for accounting profit. Contribution margin=(R-V)/R. Target >=50% after actual variable costs, not guaranteed. Cash flow separate from profit.

Latest Shop hourly estimate: 10 customers × ₹125 basket=₹1,250 gross, ₹500 direct cost, ₹750 gross contribution, ₹100 service labor, ₹102 allocated overhead, ₹548 operating surplus/hr before further tax/prep/etc; ₹448 at ₹200. ₹125 basket means 2.5 ₹50 modules on average, not necessarily 2.5 pizza slices. If 5% GST applies, net revenue ₹1,190.48/hr and surplus ₹488.48/₹388.48 under same cost assumptions. Treat ₹500/h as all-direct-cost scenario only if water/waste/packaging included; otherwise deduct missing amounts. ₹102/hour implies ₹36,720 overhead across 360 service hours/month; do not reuse at 80 hours without recalculating.

Illustrative 4h×20d: 800 customers, ₹100k gross, ₹40k variable, ₹8k service wages at ₹100, 1.25h prep/day ₹2.5k, ₹32k fixed (25k rent + illustrative 7k others), ₹17.5k surplus before GST/extra expenses; if 5% applies ₹12,738. At 12h×30d: ₹450k gross, ₹180k variable, ₹36k service wage, ₹3.75k prep (1.25h/day; likely insufficient at volume), ₹36,720 overhead, ₹193,530 before GST/extra shifts/closing/depreciation; at ₹200, ₹153,780. These are scenario calculations not forecasts. 4h scenario break-even before GST at ₹75/customer contribution, (32k+8k+2.5k)/(80*75)=7.0833 customers/hr; with 5% GST ₹69.0476/customer -> 7.6940/hr. No double counting fixed overhead. Payback = nonrefundable invested capital / sustainable post-cost free cash flow, not revenue.

## 5. Food safety and compliance (hard gates)

Before sale, obtain applicable FSSAI registration/license, local shop/trade/fire/electrical permissions, potable water, safe food-contact surfaces, staff hygiene and training, cleaning/pest controls and FSMS as applicable. Verify current thresholds and GST applicability per entity/channel/location. FSSAI hygiene checks include cold holding around <=5°C, hot holding >=65°C, validated cooling/reheating and frozen storage requirements; actual recipe-specific conditions and shelf lives require qualified verification. Maintain lot traceability, expiry/discard, thermometer calibration, allergen declarations (wheat/gluten, dairy, almond/pistachio etc), cross-contact prevention, illness exclusion, recall/complaint procedure, incident stop and disposal. No safety shortcuts for one-hour prep or low cost. Online delivery adds temperature, packaging and traceability gates.

Official references checked Nov 24: https://fssai.gov.in/inspection/hygiene-requirements ; https://hygiene.fssai.gov.in/auditDetails.php?mid=3 ; https://foscos.fssai.gov.in/ ; https://cbic-gst.gov.in/hindi/gst-goods-services-rates.html (ordinary restaurant service 5% without ITC where applicable). Applicability not certified.

## 6. Chain design and controlled replication

Stage 0 recipe/oven/food safety qualification; Stage 1 one outlet 30-day bounded experiment with measured daily data; Stage 2 repeat at independent location with trained operator, compare results against baseline; Stage 3 replicate in batches only when food safety, economics, demand, staffing and supply quality remain robust. No automatic expansion, real-world authorization or use of Garden granted here. Central chain: recipe registry and bill of materials, supplier qualification, outlet equipment and layout kit, training and audit checklist, POS and inventory standard, pricing quantum with local affordability and tax variants, anonymized aggregated performance, issue/recall escalation, versioned changes and rollback. Local outlet retains lawful human responsibility, procurement where quality validated, staffing, customer service. Do not collect unnecessary customer/employee data. Each outlet has independent P&L; cross-subsidy and franchise fees explicitly recorded if any; no invented franchise economics.

Test hypotheses: modular menu reduces ingredients/prep/waste versus conventional matched local takeaway; affordability and quality drive repeat demand; 10/hr capacity maintained without harm; sustained >=50% direct margin; full-cost positive cash flow, adequate worker compensation and safety. Suggested admission evidence: 30 days reliable measured data including peak/quiet days, all safety gates pass, positive fully loaded operating surplus and realistic sensitivity under demand -30%, input +20%, wage doubling, downtime and delivery fees; independent second-site replication before chain claim. Thresholds proposed not approved. If low sales close/rework, do not scale; if food safety incident stop affected production and remedy. Compare independent representations (per customer, per module, per kg, per staff-hour, per outlet), matched conventional small takeaway; avoid bias from selected profitable hours. Prior art: build-your-own pizza and standardized assembly lines already exist (https://franchise.yourpie.com/our-concept/ ; https://www.rectizza.com/ ; https://picnic.demosurface.com/picnic-pizza-station/). No claim of novelty or superior outcome without broad search and tested evidence. India Patents Act §3(k) excludes business methods; this is a business-process candidate, NOT a patent filing or grant. A separately demonstrated new technical invention would require separate patentability and disclosure review. https://ipindia.gov.in/acts/patent-act-1970/section-3 ; publication is public disclosure. No license change.

## 7. Garden GSL representation and cross-module review

Conceptual GSL/KR mapping (not executable or a new GSL syntax): entities = outlet, worker, recipe, ingredient lot, equipment, customer order, supplier, batch, expense, observation and authorization; qualified relations = composition, temporal sequence, dependency, provenance, quantities, costs, constraints, alternatives, responsibility and evidence. Represent measured vs estimated facts separately; use current GSL v45.1 owners, not new core object/relations/forms. Record version, unit, source, scope, assumptions, confidence, invalidation and exceptions; changes never automatically authorize actions.

| Existing owner/candidate | Review obligation/result |
|---|---|
| GSL/KR/USM | Recipe/order and inventory mapping conceptual; exact executable encoding not run. Missing ingredient details unknown. |
| Reason/GSL-COMPARE/REP/QSE | Compare menu, service hours, baseline, independent representations and alternative cost models; demand and savings not demonstrated. |
| Proof/Algebra | Arithmetic enumerated: eight combinations; 56 g ₹19.80 shrikhand; 14.68 kg batch; scenario reconciliation. Conditional arithmetic only. |
| Materiality/MCC/Human-Effect | Include safety, allergens, accessibility, worker wage/shift, environmental waste, affordability and privacy. |
| RSDC/IDTD/GCSC | Prior-art screen identifies existing custom pizza/assembly models; no novelty pass; real comparative experiment needed. |
| RCC/VEI/ActionGate | Legal food approval, owner/worker consent, capital and expansion gates separate from design; no real actions approved. |
| Transition/audit/assurance | Source versions, batch lineage, financial evidence, incident and rollback records; no unseen evidence credited. |
| Production | Throughput/oven/pacing tests and second-site validation UNKNOWN. |

Checks: 2^3=8, price/cost sum, dough mass conservation before losses, tax-inclusive revenue formula, nonnegative ingredient inventory, batch traceability, allergens and expiry checks, labor and overhead not double counted. Counterexamples: 4h overhead dilution failure; every customer buys only one ₹50 item; high delivery commissions; 20% ingredient inflation; cold-chain failure; allergen cross-contact; burst orders overwhelm oven; staffing absence; seasonal price shock; second outlet has no demand. Tests require actual records; conceptual checks PASS arithmetic only, safety/market/novelty/production/independent module execution UNKNOWN. No canonical modification, no license change.
