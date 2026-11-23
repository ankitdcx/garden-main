# GARDEN-HOME-001 — Verification and admission checklist

**Scope:** v16 candidate `GARDEN-HOME-001`; **current state:** design arithmetic checked, physical/legal/patent evidence absent. Noncanonical, non-admitting.

## Invariants and test obligations

| ID | Test / evidence needed | Current status |
|---|---|---|
| HOME-T01 | Recompute 80×40 ft / 4×4 ft as `20×10=200` cells/full floor; an 80×20 ft wing as `20×5=100`; 3 full levels `600` sites and 3 above + 1 basement `800`; horizontal edges `19×10+20×9=370` per full level; wing `19×5+20×4=175` | PASS — nominal arithmetic only |
| HOME-T02 | For every eligible shared edge, verify configuration choices OPEN / THIN_PARTITION / THICK_MODULAR_WALL / OPENING_ONLY; each accepts compatible door kind or NONE; enumerate protected structural/fire/shaft edges and the impact of excluded interfaces | NOT EXECUTED |
| HOME-T03 | Show connected 4×4 cell groups nearest to requested 100/150/175/200/300 sq ft and disclose area quantization (multiples of 16), usable wall losses, access/ventilation failures; never assert exact 150 or 200 sq ft from whole cells | NOT EXECUTED |
| HOME-T04 | Exchange a 25-sq-ft corridor cell and a room cell without losing occupied-room egress, accessibility or emergency response | NOT EXECUTED |
| HOME-T05 | Prototype a four-neighbour junction using open, lightweight partition, thick *removable non-load-bearing* panel, and allowed door types; verify anchor strength, weight, fire/acoustic continuity, accessibility and hardware clash | NOT EXECUTED |
| HOME-T06 | Reconcile gross/net area, open voids, garden, terrace, service spaces and actual permitted floor-area ratio | NOT EXECUTED |
| HOME-T07 | Validate shaft and wet-service connectivity, plumbing slopes, ventilation, electricity, fire compartment and maintenance access | NOT EXECUTED |
| HOME-T08 | Compare historical all-door, current interchangeable open/thin/thick/wall-with-door/wall-without-door, fixed-corridor, conventional masonry and other movable-partition baselines at matched usable area, repeat-change effort, safety, costs and labor | NOT EXECUTED |
| HOME-T09 | Independent novelty/inventive-step / prior-art claim chart for hardware, method and algorithmic directions | NOT EXECUTED — NOVELTY UNKNOWN |
| HOME-T10 | Record public-disclosure authorization, inventorship evidence and any filing decision without implying GitHub disclosure is a patent filing | USER AUTHORIZED REPO PUBLICATION; NO PATENT FILING |
| HOME-T11 | Engineer-check **variable number and sizes of columns** and full structural schemes, including fewer and more than five supports; validate load paths, soil, lateral/wind/seismic stability, long spans and independent comparison to the historical five-column design | NOT EXECUTED — DO NOT BUILD |
| HOME-T12 | Independently validate lift, stair, slide, landing, opening, fire/guarding and child-use constraints for multiple core shapes | NOT EXECUTED |
| HOME-T13 | Two legal alternate bedroom locations including eligible corners + at least two interior style profiles with fixed core; also cover wet-room relocation denial | NOT EXECUTED |
| HOME-T14 | Structural-edge accounting: `370` is a theoretical unobstructed 20×10 grid level, not a promise of doors; count blocked/protected vs free edges, door/wall modes, service/egress exceptions and per-level variability | NOT EXECUTED |
| HOME-T15 | Test design governance and no self-authorization; reject any unqualified layout despite a software pass | NOT EXECUTED |
| HOME-T16 | Representation escape: test square-lattice, other pitch, non-grid and simpler layouts; keep null/negative results | NOT EXECUTED |
| HOME-T17 | Safely remove and re-add a thin partition and an engineered thick non-load-bearing wall at the same edge repeatedly, with measured time, personnel, tools, damage, waste and cost; exclude structural and ordinary load-bearing masonry | NOT EXECUTED |
| HOME-T18 | Reject any optional solid no-door wall that destroys safe access/egress, fire compartment performance, maintenance access or ventilation, including during the construction transition | NOT EXECUTED |
| HOME-T19 | Validate door configurations NONE / hinged / sliding / pocket / folding / rated where compatible, including privacy, accessibility, clear opening, hinges, power and child safety | NOT EXECUTED |
| HOME-T20 | Show a three-stage *occupied-life* reconfiguration from open cells → solid thick wall without door → thin wall with door, while keeping the **engineer-approved selected structural scheme** unchanged and independently rechecking services, authority, fire and evacuation | NOT EXECUTED |
| HOME-T21 | Compare a scoped set of feasible column counts (including fewer than five, five and more than five), variable cross-sections, locations and structural systems with full foundation/beam/slab/lateral cost and independent design verification | NOT EXECUTED — NO COST OPTIMUM CLAIM |
| HOME-T22 | Recompute quantity takeoffs and compare matched local prices for columns, foundations, beams, slabs, lateral bracing, connections, reinforcement, labor and structural effects on services/fit-out; quantify usable-area impact | NOT EXECUTED |
| HOME-T23 | Falsify cheapest-column-only metrics: test cases where more narrow columns increase foundation cost or fewer wide columns increase slab/beam spans; reject cost wins that fail engineering feasibility | NOT EXECUTED |
| HOME-T24 | Demonstrate that the algorithm does not hard-code a center column or five columns; document finite search coverage, uncertainty, globality limits and all blocked cells/door interfaces | NOT EXECUTED |
| HOME-T25 | Verify 4×4 ft pitch propagates to all candidate schemas, graph neighbors, counts, wall interfaces and cost quantities; old 5×5 ft pitch remains provenance only | NOT EXECUTED |
| HOME-T26 | Form connected and disconnected unions from adjoining 4×4 planning cells; detect overlap/double-count, land boundaries, easements and denied legal subdivision/lot-merger rights | NOT EXECUTED |
| HOME-T27 | Count `sum_l |S_l|` for varying above-ground/basement footprints and setbacks; reject `|S|×(A+B)` when footprints are partial and distinguish usable vs gross vs open space | NOT EXECUTED |
| HOME-T28 | Validate level access as stairs/lifts or genuinely approved portals only; closing/reconfiguring floor cells must not create unsupported vertical passage or unsafe egress | NOT EXECUTED |
| HOME-T29 | Compare B=0,1,2+ requests under groundwater, excavation depth, retention walls, adjacent foundations, waterproofing, emergency access and cost; reject infeasible basements | NOT EXECUTED |
| HOME-T30 | Compare A=1,3,10+ requests against land-use/zoning/height permissions, evacuation/lift/core requirements, loads, drift and lifecycle cost; more floors does not imply more columns automatically | NOT EXECUTED |
| HOME-T31 | Test a 4-ft edge with hinging/sliding doors and walls including thick panels; reject required clearances or accessible routes that cannot physically fit | NOT EXECUTED |

## Evidence rules

- Source/design specification does not prove implementation, testing, engineering adequacy, legal approval or patentability.
- Any failed safety-critical check means no 'buildable' status; UNKNOWN does not become PASS by a drawing, simulation, endorsement or successful arithmetic.
- **Latest requirement precedence (2026-11-23):** optional walls and optional doors supersede the historical all-neighbour installed-door mandate. Preserve both descriptions in provenance; do not silently enforce historical requirements as current.
- "Easily removable at any time" is an engineering/user-experience target, never permission to alter load-bearing/shear walls, protected shafts or rated fire separations or to skip required permits and inspection. A visually thick wall must still have a qualified nonstructural, lightweight/demountable construction.
- For egress test, consider doors locked at night, power failure, smoke, inaccessible lift and an occupant needing assisted evacuation.
- For physical proof, use independent structural/fire/accessibility professionals and relevant building authority approval; the **number, size and placement of supports remain unengineered**. The earlier five-column concept is merely a historical comparator.
- **Latest user requirement precedence (2026-11-23):** 4×4 ft cells, adjoining land-cell assembly and arbitrary *requested* floor/basement counts supersede 5×5 ft as the active design. Variable column count/width/position and removable wall rules remain current. Minimum `N × width` alone is not proof of minimum total cost.
- A 4×4 ft cell is a conceptual planning site, not an independently verified legal land plot. Unlimited vertical levels are user-request input options, **not an engineering or regulatory entitlement**.
- For rights/novelty, compare actual claim elements with substantive prior art; a patent-style title in GitHub does not create patent rights.
- Garden source/admission must preserve version epochs, source lineage, nonclaims, human authority and evidence provenance.

## Decision

**Preliminary result:** `RETAIN_AS_NONCANONICAL_V16_CANDIDATE`. No claim of Garden v16 canonical source admission, construction readiness or patent grant. Reassess only with independently collected evidence.
