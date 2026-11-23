# GARDEN-HOME-001 — User-reconfigurable 5 × 5 ft Building Grid

**Artifact type:** Garden v16 applied human-systems invention-design candidate (NOT a filed patent)  
**Date:** 2026-11-23  
**Revision:** 1.2 — public candidate extracted/reconciled from private revision 1.1  
**Status:** `NONCANONICAL / NOVELTY_UNKNOWN / ENGINEERING_UNVALIDATED`  
**Source provenance:** User's November 20–23, 2026 home-design discussions and private HOME-001 rev 1.1; the user supplied the foundational grid, adjacency-door, flexible room/path, central support, four additional supports, central lift/stairs/slide, location and design-freedom requirements. Formal graph rules, alternatives, tests and safety qualifications are assistant elaborations.

## A. User-originated invariant / invention intent

1. **Universal 25-sq-ft lattice:** divide the **whole home** into regular **5 ft × 5 ft** planning cells, including zones that later become rooms, corridors, open spaces or service areas. Treat 10 × 10 ft / 100 sq ft as a four-cell macro-block, not the primitive unit.
2. **Every-neighbour doorway:** any two cells that share an internal orthogonal 5-ft edge have a **doorway/door** between them, except where a permanent safety/structure/shaft constraint makes a doorway impermissible. This *literal all-door baseline* must not quietly be replaced by merely 'door-ready' cells.
3. **Role interchangeability:** a connected set of cells can become a room, path or shared area; cells can be reassigned to make larger, smaller, irregular, or relocated rooms over time, subject to building constraints.
4. **Five principal supports as design hypothesis:** one thick central column plus four additional main columns support a proposed three-storey building skeleton; the intention is to free non-structural interior partitions. Exactly five main supports, their sizes and locations **have not been engineered and cannot be assumed sufficient**.
5. **Central circulation/play space:** an appropriately sized flexible area **around** the centre is reserved for lift, stair and slide, with user choice of shapes and visual arrangement, subject to safe separate shafts, stairs/landings/clearances, emergency egress and accessibility. Slide is recreational, not an emergency exit.
6. **User-selectable everywhere else:** assign bedrooms or other functions in a preferred eligible corner/location; move and combine rooms; independently choose interior style, finish and furniture. Wet rooms, daylight, legal room sizes and utility availability still constrain the choice.

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

**Geometry invariants:** on the unobstructed complete 16 × 8 grid the number of undirected interior orthogonal adjacency interfaces is `(16−1)×8 + 16×(8−1) = 232` per level. A 16 × 4 wing has `(16−1)×4 + 16×(4−1) = 108` edges; the 16 edges along the boundary between two wings bring the total to 232, assuming uninterrupted traversability. Across three unconstrained levels: `696` potential same-level edges, **not 696 valid installed doors**.

The earlier 81-block idea depends on what 'block' means. In the 25-sq-ft scheme 81 cells = 2,025 sq ft; this exceeds one 1,600-sq-ft wing, while 64 cells exactly fill that wing's nominal footprint. A garden, open parking bay, terrace, lift, stair, structural member, void or shaft occupies nominal grid sites but is not necessarily habitable or door-traversable. Three levels × 3,200 sq ft gross is **not** a claim of 9,600 sq ft of enclosed or permitted floor area.

Historic project constraints include the frontage along the 40-ft road side, other three outside boundaries walled, left/right 80 × 20 ft wings, private home, service apartment/office, parking, garage, stairs/lift, guests, pooja, kitchen/dining, gym, terrace and gardens. Their complete simultaneous allocation has **not** been reconciled against the new central core; this remains a design test.

## C. Two overlays: permanent structure and reconfigurable space

**Permanent spatial constraints:** establish at most a *proposed* `P0` (thick near-centre principal column) and `P1..P4` (four other proposed support locations). An engineer must define foundation, soil, member sizes, reinforcement, beam/slab spans and deflection, lateral-load resistance, fire design, seismic/wind actions and code compliance. The grid may be interrupted by columns, shear walls/braces, perimeter structure and shafts. If additional supports are needed, report the conflict with exactly five; do not disguise them as decorative walls.

**Central region:** reserve `CENTRAL_CORE_ZONE` around `P0` for `STAIR`, `LIFT`, `SLIDE`, landings and service passages. Its shape can vary, but enforce dimensions, shafts, fire separation, guards, accessible entrances, child protections, permitted floor openings and safe crossings. Neither stair nor lift capacity is established by naming it.

**Flexible remainder:** nonstructural room partitions and compatible door assemblies permit connected room groups and a movable corridor network. User selection changes `room-use`, `room shape`, `room location`, `edge mode` and `interior style`; it may not change safety-critical fixed infrastructure without additional approval. Bathrooms and kitchens require service connections, sound control, and ventilation/drainage feasibility.

**Door interface:** a four-sided cell has up to four orthogonal neighbours. Baseline: physically install a closable door at every **permitted** interior adjacency edge. Candidate engineering alternative: install a consistent interface capable of later receiving a door or blank panel instead; **retain the baseline for comparison and do not treat the alternative as the same requirement**. Door swing, privacy, simultaneous openings, locking, accessibility, fire doors and partition acoustics need a concrete hardware design.

**Edge-exception register:** every blocked neighbour edge must record its reason (`COLUMN`, `SHAFT`, `FIRE_SEPARATION`, `BOUNDARY`, `STRUCTURAL`, `OTHER`), evidence, effect on connectivity and reviewer status. No silent exception.

## D. GSL-style formal representation (candidate profile, not a GSL syntax amendment)

Let `V` be the set of nominal cells and `E = {(u,v): u,v ∈ V, u and v share an internal full 5-ft orthogonal side}`. Declare any impediments explicitly.

```text
BuildingModel {
  SourceRef, DesignEpoch, Levels, GridPitch=5ft,
  PlotEnvelope, StructuralOverlay(P0..P4,OtherRequiredMembers),
  CentralCoreZone, Perimeter, ServiceRoutes, ApplicableRuleRefs,
  GridCells[], NeighbourEdges[], Exceptions[], EvidenceRefs[], Status
}
Cell {
  CellID, Level, Row, Column, Bounds, FixedFlags[],
  Use: ROOM(RoomID) | CIRCULATION | SERVICE | GARDEN |
       PARKING | STAIR | LIFT | SLIDE | SHAFT | VOID | OPEN | UNRESOLVED
}
Edge {
  EdgeID, CellA, CellB, PermittedDoor, ExceptionRef?,
  PhysicalDoorProvided?, Mode: OPEN | CLOSED | LOCKED |
       OPEN_CONNECTION | PANEL | FIRE_SEPARATION | BLOCKED
}
StyleProfile { RoomID, FinishTheme, Fixtures, Lighting, Furnishing, Constraints }
ConfigurationReceipt {
  SourceEpoch, BuildingModelRef, LayoutID, AssignedCells[],
  RoomGroups[], AccessGraph, DoorEdgeStates[], StyleRefs[],
  SafetyCheckRefs[], ExceptionRefs[], RejectedAlternatives[],
  ApprovalRefs[], Status
}
```

Map these into existing GSL objects/relations/context through a frozen mapping profile; do **not** declare them new canonical GSL Core Objects. An unapproved plan is a candidate claim; drawing a column or connecting a door does not establish physical or legal feasibility.

A connected `ROOM(r)` assignment denotes a *grouping*, not a guarantee of habitable legal room dimensions. An admissible configuration must pass **area consistency; room/path connectivity; qualified exit access; fire/shaft/structural limits; service routing; daylight/ventilation; mobility/accessibility; acoustic/privacy; door hardware/clearance** before being labeled buildable. If any material check is unknown, emit `UNKNOWN` or `REJECTED`, not `PASS`.

Pseudo-process:

```text
freeze source evidence and approved structural envelope
overlay 5 proposed supports plus all actually required permanent members
reserve central lift/stair/slide zone and lawful exit/service routes
map occupant's room sizes, preferred corners, functions and styles
generate connected sets of 25-sq-ft cells for rooms / pathway / shared uses
assign a door to each legally/physically permitted neighbour edge
record every excluded connection, and why it was excluded
check structural + room-area + egress + access + fire + wet-service + privacy constraints
if unresolved: return UNKNOWN and alternatives; do not authorize construction
if valid: compare competing layouts and style profiles, retain versioned receipt
if occupant changes a layout: revalidate the *whole affected access network*
```

## E. Illustrative alternatives and falsification

Compare with a conventional column/beam frame and adjustable partitions; room-scale modular systems; alternate non-square pitch; permanent corridors; a no-slide conventional lift/stair core; fully installed all-door edges versus universal **door-ready** edges; fewer/more structural support locations based on cost; and a non-grid bespoke layout. Match floor area, safety requirements, actual costs and usable room volume before claiming any benefit.

A graph layout that is geometrically valid but traps a bedroom after a corridor is converted is a negative test. A 5-ft cell whose four doors conflict with usable swing space is a negative test. A five-column option failing seismic/span analysis is a negative test, even if it leaves more nominal cells unoccupied. A cheap modular system that performs better on practical change cost is evidence **against**, not for, HOME-001.

## F. Patent research directions — NOT patent claims

1. A physically specified four-neighbour standardized door/partition assembly compatible with reconfiguration while respecting sound, fire and accessibility constraints.
2. A reconfiguration protocol for assigning connected cells between rooms and corridors while preserving an independently validated access network and service constraints.
3. A layered structural/core/flexible-cell construction method with a tested economic or material improvement relative to strong existing systems.
4. A versioned layout planning interface with retained safety/engineering evidence, change-impact receipts and separate occupant styling choices.

Prior work covers broad modular rooms and changing floor plans; **mere regular 5-ft cells, the idea of all-side access or movable partitions cannot currently be represented as proved novel**. Initial reference leads from the private draft: US20160145853A1; US20200320229A1; WO2024057004A1; US20220198080A1. These are **not** a completed prior-art search or claim chart. Patentability, inventor rights, filing/priority, patent subject-matter eligibility and freedom to operate remain **UNKNOWN**. The user expressly requested public GitHub publication on 2026-11-23; this repository record is a *public disclosure, not a patent application*, and may affect later patent rights.

## G. Garden compatibility, status and admission

- GSL / USM / KR: represent building, constraints, user choices, evidence and changes as source-bound context; no authority promotion through compilation.
- GSL-COMPARE / Reason / Proof: verify graph arithmetic, test alternatives, respect counterexamples; no structural proof or safety certificate inferred.
- REP / MCC / Human-Effect: challenge original representation and include people, neighbors, children, mobility, privacy, fire and lifecycle context.
- RCC / VEI / ActionGate: construction authorization, inspections and physical changes remain under legitimate human authorities; simulation receipts do not permit building.
- IDTD / RSDC: retain negative novelty comparisons; seek measurable physical improvement over competing techniques.

**Known nominal arithmetic:** PASS by inspection. **Every-neighbour design intent:** CAPTURED. **Five-column physical sufficiency:** UNKNOWN. **Core lift/stair/slide legality:** UNKNOWN. **Actual flexible room feasibility and construction costs:** UNKNOWN. **Patent novelty:** UNKNOWN. **Application filed:** NO. **Canonical admission:** NO.

**Validation plan:** [HOME_001_VERIFICATION.md](HOME_001_VERIFICATION.md).

**Source boundary:** Do not silently promote to canon, alter `LICENSE` or claim certification. This is an explicitly requested *v16 candidate*, not a completed new Garden release.
