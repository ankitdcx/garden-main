# GARDEN-HOME-001 — User-reconfigurable 5 × 5 ft Building Grid

**Artifact type:** Garden v16 applied human-systems invention-design candidate (NOT a filed patent)  
**Date:** 2026-11-23  
**Revision:** 1.4 — variable-column structural-cost optimization (2026-11-23), building on revision 1.3  
**Status:** `NONCANONICAL / NOVELTY_UNKNOWN / ENGINEERING_UNVALIDATED`  
**Source provenance:** User's November 20–23, 2026 home-design discussions and private HOME-001 rev 1.1; the user supplied the foundational grid, initial every-neighbour-door proposal, flexible room/path, earlier central-plus-four-support suggestion, central lift/stairs/slide, location and design freedom. The latest 2026-11-23 revisions require optional, easily replaceable nonstructural walls **and any feasible number, width and placement of columns that minimizes total construction cost**, superseding the mandatory-door and fixed-five-column starting concepts. Formal graph rules, alternatives, tests and safety qualifications are assistant elaborations.

## A. User-originated invariant / invention intent

1. **Universal 25-sq-ft lattice:** divide the **whole home** into regular **5 ft × 5 ft** planning cells, including zones that later become rooms, corridors, open spaces or service areas. Treat 10 × 10 ft / 100 sq ft as a four-cell macro-block, not the primitive unit.
2. **Universal neighbour-edge reconfiguration interface (latest requirement):** for any two cells sharing an eligible orthogonal 5-ft edge, the edge must support a compatible choice among **open connection/no wall; thin demountable partition; modular thick non-load-bearing wall; wall with door; wall with no door**, and permitted types of doorway/door, without modifying the permanent structural skeleton. The user's earlier *literal installed door on every available edge* is retained as a historical proposal **explicitly superseded by the latest optional-wall/optional-door requirement**, not silently erased. Boundary edges blocked by fixed structure, fire/shaft separation or legal limits remain exceptions.
3. **Role interchangeability:** a connected set of cells can become a room, path or shared area; cells can be reassigned to make larger, smaller, irregular, or relocated rooms over time, subject to building constraints.
4. **Variable columns for minimum feasible total construction cost (latest requirement):** optimize column count `N`, column width/depth/cross-section, material and position together with beams, slabs, foundations and lateral-resisting system. **Any engineering-feasible column count may be evaluated**; a thick central column and four other columns are no longer mandatory, but the historical five-column concept remains as one comparison candidate. Accept only designs meeting structural and legal requirements while retaining as much safe interior reconfigurability as practical.
5. **Central circulation/play space:** an appropriately sized flexible area **around** the centre is reserved for lift, stair and slide, with user choice of shapes and visual arrangement, subject to safe separate shafts, stairs/landings/clearances, emergency egress and accessibility. Slide is recreational, not an emergency exit.
6. **User-selectable everywhere else:** assign bedrooms or other functions in a preferred eligible corner/location; move and combine rooms; independently choose interior style, finish and furniture. Wet rooms, daylight, legal room sizes and utility availability still constrain the choice.
7. **Wall as replaceable component:** occupants may reconfigure eligible non-load-bearing walls **later**, not just during original construction: add, remove, relocate or swap a wall/partition/door assembly. A thick-looking wall is a specially engineered **non-load-bearing modular assembly**, not a license to remove masonry or an actual shear/load-bearing wall. Safety review, assembly handling, services and any required permits are prerequisites to physical changes.

**Purpose:** a reusable physical/digital building-design interface where the basic shell endures and room boundaries/paths change over a building's lifetime. It does not claim every possible arrangement is physically or legally feasible.

## B. User house / dimensional example

| Item | Nominal geometry | Lattice count |
|---|---:|---:|
| Primitive cell | 5 × 5 ft = 25 sq ft | 1 |
| Macro-block | 10 × 10 ft = 100 sq ft | 4 |
| Whole plot / planning level | 80 × 40 ft = 3,200 sq ft | 16 × 8 = 128 |
| Each longitudinal wing | 80 × 20 ft = 1,600 sq ft | 16 × 4 = 64 |
| Three gross levels | 9,600 sq ft | 384 cell positions |
| Garden example | 800 sq ft | 32 |
| Parking example | 900 sq ft | 36 |
| Guest room example | 200 sq ft | 8 |
| Bedroom options | 150 / 175 / 200 sq ft | 6 / 7 / 8 |
| Studio/services example | 300 sq ft | 12 |

**Geometry invariants:** on the unobstructed complete 16 × 8 grid the number of undirected interior orthogonal adjacency interfaces is `(16−1)×8 + 16×(8−1) = 232` per level. A 16 × 4 wing has `(16−1)×4 + 16×(4−1) = 108` edges; the 16 edges along the boundary between two wings bring the total to 232, assuming uninterrupted traversability. Across three unconstrained levels: `696` potential same-level edges, **not 696 mandatory doors or physically modifiable boundaries**.

The earlier 81-block idea depends on what 'block' means. In the 25-sq-ft scheme 81 cells = 2,025 sq ft; this exceeds one 1,600-sq-ft wing, while 64 cells exactly fill that wing's nominal footprint. A garden, open parking bay, terrace, lift, stair, structural member, void or shaft occupies nominal grid sites but is not necessarily habitable or door-traversable. Three levels × 3,200 sq ft gross is **not** a claim of 9,600 sq ft of enclosed or permitted floor area.

Historic project constraints include the frontage along the 40-ft road side, other three outside boundaries walled, left/right 80 × 20 ft wings, private home, service apartment/office, parking, garage, stairs/lift, guests, pooja, kitchen/dining, gym, terrace and gardens. Their complete simultaneous allocation has **not** been reconciled against the new central core; this remains a design test.

## C. Two overlays: permanent structure and reconfigurable space

**Permanent spatial constraints:** the structural support scheme is an *optimization variable*, not a five-column prescription. Enumerate and cost candidate counts, widths/depths, materials, positions and support schemes (including other lateral members or structural walls where required); retain only verified feasible designs. A central column is optional; a central lift/stair/slide core remains a functional allocation. An engineer must determine the foundation/soil, load path, spans, deflection, story drift, lateral seismic/wind resistance, fire robustness and applicable approvals. Every column, shear wall, shaft and protected element that interrupts a 5 × 5 ft planning cell or eligible wall edge must be registered as permanent, not falsely treated as moveable.

### HOME-OPT-001 — Structural cost-minimization contract

**Primary design objective:** choose the cheapest structurally and legally feasible combination of **number of columns × sizes/cross-sections × placements**, while preserving the adaptable 5 × 5 ft space layout and functioning central stair/lift/slide zone.

Column cost is **not** proportional to `N × width` alone: column width is a linear dimension, while material volumes depend on width × depth × story height; reinforcement, foundations, beam spans, slab thickness, shear system and labor also change when support positions/count change.

```text
StructuralCandidate {
  CandidateID, N, ColumnLocations[], CrossSections[], Materials[],
  ColumnHeightAndReinforcement[], FoundationDesign[], BeamDesign[],
  SlabDesign, LateralResistingDesign, FixedCoreAndProtectedElements,
  OccupiedCellsAndEdges[], StructuralEvidenceRefs[], CostEvidenceRefs[],
  SafetyStatus, DesignStatus
}

C_total = C_columns + C_foundations + C_beams_and_transfer_members
        + C_slabs + C_lateral_system + C_connections
        + C_reinforcement_formwork_and_labor + C_required_protections
        + C_structural_effects_on_services_and_fitout

Optimize:  min C_total(candidate)
Subject to: independently checked gravity/lateral loads, seismic/wind,
  soil/settlement, span/deflection/vibration, fire, robustness,
  code/permit, lift/stair/slide clearance, structural constructability
  and minimum usable room/circulation/function requirements.
```

- The 5-ft grid is a **planning lattice**, not a requirement to place columns at every 5-ft intersection; columns may occupy or obstruct cells/edges, which must be recorded.
- Compare fewer and more columns, narrower and wider cross-sections, and alternative layouts/materials. More columns may shorten spans and cheapen slabs/beams but cost more in footings and occupy floor area; fewer columns can make heavier/long-span systems costly.
- For every candidate, report bill of quantities, actual location-specific unit prices, buildability, blocked-cell count, net usable area, fire/egress impacts, and a breakdown of total cost. Cost per gross area and cost per **usable** area are both useful comparators.
- A proposed minimum is **minimum among evaluated feasible candidates** unless the optimizer has independently justified global coverage/bounds. If prices, soil or loads are missing, status is UNKNOWN, not 'cheapest'. No invented cost or optimal number is permitted.
- The earlier five-column arrangement is only one historical benchmark; it cannot be hardcoded as the preferred design. A qualified structural engineer/authority must verify the selected scheme before physical construction. Users may later move nonstructural partitions; **not structural columns**.

**Central region:** reserve `CENTRAL_CORE_ZONE` for `STAIR`, `LIFT`, `SLIDE`, landings and service passages, with a central column only if the optimized and engineered structure calls for one. Its shape can vary, but enforce dimensions, shafts, fire separation, guards, accessible entrances, child protections, permitted floor openings and safe crossings. Neither stair nor lift capacity is established by naming it.

**Flexible remainder:** non-load-bearing room partitions, engineered thick wall assemblies, open connections and compatible doors permit connected room groups and a movable corridor network. User selection changes `room-use`, `room shape`, `room location`, `edge mode`, `wall type`, `door type` and `interior style`; it may not change safety-critical fixed infrastructure without additional approval. Bathrooms and kitchens require service connections, sound control, and ventilation/drainage feasibility. Reconfiguration must be possible **after initial occupation** at eligible interfaces, without affecting the approved structure.

**Universal replaceable edge assembly:** a four-sided cell has up to four orthogonal neighbours. At each **eligible** internal edge, specify a reusable interface/anchoring/service-safe connection to accept these states:
- `OPEN` — no wall, free connection between cells.
- `THIN_PARTITION` — removable lightweight non-load-bearing panel; `door=NONE` or permitted door/portal.
- `THICK_MODULAR_WALL` — removable engineered non-load-bearing assembly, e.g. acoustic/fire-rated layered panels as qualified; `door=NONE` or permitted door/portal.
- `OPENING_ONLY` — partial wall/border/open doorway without a door leaf, where appropriate.
- `FIXED_PROTECTED` — shaft, egress, structural, fire or other boundary outside occupant reconfiguration.
**Door choice:** `NONE`, `HINGED`, `SLIDING`, `POCKET`, `FOLDING`, `RATED` or another qualified door assembly. A "thick wall" must meet load, handling, fixing, acoustic/fire and safe removal requirements; **ordinary thick masonry is not assumed easily removable**. Hinged-door swings, simultaneous openings, wall-joint air/acoustics, services, anchorage, accessibility and rated assemblies must each be validated. **Not all door types fit all 5-ft edges.**

**Reconfiguration protocol:** disconnect or isolate any services → secure the work site → confirm partition/nonstructural classification from an as-built register → remove or install approved wall/door modules without cutting structural members → inspect edge connections, fire/acoustic/service continuity and waste handling → independently recheck affected access, egress, privacy and accessibility → record a new version/approval before occupied use. User-requested "anytime easily" is a **design goal** (quick, low-disruption, reversible exchange), not unconditional permission to demolish walls or bypass inspection. An engineering prototype must establish whether repeated change is actually easy and affordable.

**Historical requirement transition:** the initial Nov 23 idea proposed doors on all permitted edges; the latest user input replaces it with **freely selectable wall-or-no-wall, door-or-no-door** at every eligible edge. Both remain in provenance for audit, but the latest rule controls this candidate.

**Edge-exception register:** every blocked or non-reconfigurable neighbour edge must record its reason (`COLUMN`, `SHAFT`, `FIRE_SEPARATION`, `BOUNDARY`, `STRUCTURAL`, `EGRESS`, `FIXED_SERVICES`, `OTHER`), evidence, effect on connectivity and reviewer status. A closed, intentionally solid removable partition is **not** an exception: it is an eligible edge in a `WALL_NO_DOOR` configuration. No silent exceptions.

## D. GSL-style formal representation (candidate profile, not a GSL syntax amendment)

Let `V` be the set of nominal cells and `E = {(u,v): u,v ∈ V, u and v share an internal full 5-ft orthogonal side}`. Declare any impediments explicitly.

```text
BuildingModel {
  SourceRef, DesignEpoch, Levels, GridPitch=5ft,
  PlotEnvelope, StructuralOptimizationRef, StructuralOverlay,
  CentralCoreZone, Perimeter, ServiceRoutes, ApplicableRuleRefs,
  GridCells[], NeighbourEdges[], Exceptions[], CostEvidenceRefs[], EvidenceRefs[], Status
}
Cell {
  CellID, Level, Row, Column, Bounds, FixedFlags[],
  Use: ROOM(RoomID) | CIRCULATION | SERVICE | GARDEN |
       PARKING | STAIR | LIFT | SLIDE | SHAFT | VOID | OPEN | UNRESOLVED
}
Edge {
  EdgeID, CellA, CellB, Reconfigurable: boolean, FixedExceptionRef?,
  AssemblyID?, WallState: OPEN | THIN_PARTITION |
             THICK_MODULAR_WALL | OPENING_ONLY | FIXED_PROTECTED,
  DoorKind: NONE | HINGED | SLIDING | POCKET | FOLDING |
            RATED | OTHER_QUALIFIED,
  PassageState: OPEN | CLOSED | LOCKED | NOT_APPLICABLE,
  StructuralInterferenceCheckRef, FireCheckRef, ServiceCheckRef
}
WallAssembly {
  AssemblyID, Version, StructuralClass=NON_LOAD_BEARING,
  Thickness, MassPerArea, Materials[], ConnectionSystem,
  RemovabilityProcedureRef, RequiredTools[], CrewPlan,
  FireAndAcousticRatings?, ServiceInterfaces[], CompatibilityRefs[],
  QualificationEvidenceRefs[], Status
}
StyleProfile { RoomID, FinishTheme, Fixtures, Lighting, Furnishing, Constraints }
ConfigurationReceipt {
  SourceEpoch, BuildingModelRef, LayoutID, AssignedCells[],
  RoomGroups[], AccessGraph, EdgeAssemblyStates[], StyleRefs[],
  SafetyCheckRefs[], ExceptionRefs[], RejectedAlternatives[],
  ApprovalRefs[], Status
}
ReconfigurationReceipt {
  FromLayoutID, ToLayoutID, ChangedEdges[], WallAssemblyVersions[],
  BeforeAfterAccessGraphs, ServiceIsolationRefs[],
  StructuralNonLoadBearingEvidenceRefs[], InspectionRefs[],
  MaterialHandlingRefs[], AuthorityRefs[], ResultStatus
}
```

Map these into existing GSL objects/relations/context through a frozen mapping profile; do **not** declare them new canonical GSL Core Objects. An unapproved plan is a candidate claim; drawing a column or connecting a door does not establish physical or legal feasibility.

A connected `ROOM(r)` assignment denotes a *grouping*, not a guarantee of habitable legal room dimensions. An admissible configuration must pass **area consistency; room/path connectivity after each optional wall/no-door change; qualified exit access; fire/shaft/structural limits; service routing; daylight/ventilation; mobility/accessibility; acoustic/privacy; demountable wall anchoring/weight/load; door hardware/clearance** before being labeled buildable. If any material check is unknown, emit `UNKNOWN` or `REJECTED`, not `PASS`.

Pseudo-process:

```text
freeze source evidence, floor geometry and safety requirements
vary column count, width/depth, position, materials, spans and support system
compute total feasible structure costs (columns, beams, slabs, foundations,
  lateral systems, connections and labor); reject unverified candidates
freeze selected engineer-approved structure and permanent elements
reserve central lift/stair/slide zone and lawful exit/service routes
map occupant's room sizes, preferred corners, functions and styles
generate connected sets of 25-sq-ft cells for rooms / pathway / shared uses
assign each eligible neighbour edge OPEN, THIN_PARTITION,
  THICK_MODULAR_WALL or OPENING_ONLY; select door kind or NONE
verify each selected removable wall module is engineered non-load-bearing
record fixed/protected exceptions, and why reconfiguration is forbidden
check structural + room-area + egress + access + fire + wet-service + privacy constraints
if unresolved: return UNKNOWN and alternatives; do not authorize construction
if valid: compare competing layouts and style profiles, retain versioned receipt
if occupant changes a layout: use safe install/remove protocol and
  revalidate the *whole affected access network* before occupied use
```

## E. Illustrative alternatives and falsification

Compare with a conventional column/beam frame and adjustable partitions; room-scale modular systems; alternate non-square pitch; permanent corridors; a no-slide conventional lift/stair core; fully installed all-door edges (historical) versus **optional modular wall/door interfaces** (current), traditional masonry versus qualified demountable thick panels; variable column count/size/placement/whole-frame cost, including the historical five-column comparator; and a non-grid bespoke layout. Match floor area, safety requirements, actual costs and usable room volume before claiming any benefit.

A graph layout that is geometrically valid but traps a bedroom after a corridor is converted is a negative test. A 5-ft cell whose proposed doors conflict with usable swing space is a negative test. Closing a previously open access edge with a solid wall, leaving an occupied room with no safe exit, is a negative test. A purported removable thick wall exceeding slab or handling loads is a negative test. A candidate of any column count failing seismic/span/load-path analysis is a negative test, even if its columns alone cost less. Compare feasible full-frame costs, not just support counts. A cheap modular system that performs better on practical change cost is evidence **against**, not for, HOME-001.

## F. Patent research directions — NOT patent claims

1. A physically specified four-neighbour interchangeable interface accepting no wall, thin panel, qualified removable thick non-load-bearing wall, doorless opening, and multiple compatible door types while respecting structural anchoring, sound, fire and accessibility constraints.
2. An approved repeated wall-removal/installation protocol for assigning connected cells between rooms and corridors while preserving an independently validated access network and service constraints.
3. A layered structural/core/flexible-cell construction method with jointly optimized support count, cross-sections and locations and a measured overall structural-cost improvement against comparable safe systems.
4. A versioned layout planning interface with retained safety/engineering evidence, change-impact receipts and separate occupant styling choices.

Prior work covers broad modular rooms and changing floor plans; **mere regular 5-ft cells, the idea of all-side access or movable partitions cannot currently be represented as proved novel**. Initial reference leads from the private draft: US20160145853A1; US20200320229A1; WO2024057004A1; US20220198080A1. These are **not** a completed prior-art search or claim chart. Patentability, inventor rights, filing/priority, patent subject-matter eligibility and freedom to operate remain **UNKNOWN**. The user expressly requested public GitHub publication on 2026-11-23; this repository record is a *public disclosure, not a patent application*, and may affect later patent rights.

## G. Garden compatibility, status and admission

- GSL / USM / KR: represent building, constraints, user choices, evidence and changes as source-bound context; no authority promotion through compilation.
- GSL-COMPARE / Reason / Proof: verify graph arithmetic, test alternatives, respect counterexamples; no structural proof or safety certificate inferred.
- REP / MCC / Human-Effect: challenge original representation and include people, neighbors, children, mobility, privacy, fire and lifecycle context.
- RCC / VEI / ActionGate: construction authorization, inspections and physical changes remain under legitimate human authorities; simulation receipts do not permit building.
- IDTD / RSDC: retain negative novelty comparisons; seek measurable physical improvement over competing techniques.

**Known nominal arithmetic:** PASS by inspection. **Universal optional-wall/optional-door interface:** CAPTURED AS NEWEST USER REQUIREMENT; PHYSICAL FEASIBILITY UNKNOWN. **Variable-column structural feasibility and optimum:** UNKNOWN; five columns retained only as a historical comparator. **Core lift/stair/slide legality:** UNKNOWN. **Actual flexible room feasibility, structural costs and global optimality:** UNKNOWN. **Patent novelty:** UNKNOWN. **Application filed:** NO. **Canonical admission:** NO.

**Validation plan:** [HOME_001_VERIFICATION.md](HOME_001_VERIFICATION.md).

**Source boundary:** Do not silently promote to canon, alter `LICENSE` or claim certification. This is an explicitly requested *v16 candidate*, not a completed new Garden release.
