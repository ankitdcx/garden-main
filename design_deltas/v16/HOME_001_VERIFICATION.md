# GARDEN-HOME-001 — Verification and admission checklist

**Scope:** v16 candidate `GARDEN-HOME-001`; **current state:** design arithmetic checked, physical/legal/patent evidence absent. Noncanonical, non-admitting.

## Invariants and test obligations

| ID | Test / evidence needed | Current status |
|---|---|---|
| HOME-T01 | Recompute `16×8=128` cells/floor; `16×4=64`/wing; `3×128=384` gross positions; `(15×8)+(16×7)=232` interior undirected edges/floor | PASS — nominal arithmetic only |
| HOME-T02 | For every eligible shared edge, verify configuration choices OPEN / THIN_PARTITION / THICK_MODULAR_WALL / OPENING_ONLY; each accepts compatible door kind or NONE; enumerate protected structural/fire/shaft edges and the impact of excluded interfaces | NOT EXECUTED |
| HOME-T03 | Produce feasible and accessible 100/150/175/200/300-sq-ft connected room layouts after partition thickness; reject insufficient daylight or floor area | NOT EXECUTED |
| HOME-T04 | Exchange a 25-sq-ft corridor cell and a room cell without losing occupied-room egress, accessibility or emergency response | NOT EXECUTED |
| HOME-T05 | Prototype a four-neighbour junction using open, lightweight partition, thick *removable non-load-bearing* panel, and allowed door types; verify anchor strength, weight, fire/acoustic continuity, accessibility and hardware clash | NOT EXECUTED |
| HOME-T06 | Reconcile gross/net area, open voids, garden, terrace, service spaces and actual permitted floor-area ratio | NOT EXECUTED |
| HOME-T07 | Validate shaft and wet-service connectivity, plumbing slopes, ventilation, electricity, fire compartment and maintenance access | NOT EXECUTED |
| HOME-T08 | Compare historical all-door, current interchangeable open/thin/thick/wall-with-door/wall-without-door, fixed-corridor, conventional masonry and other movable-partition baselines at matched usable area, repeat-change effort, safety, costs and labor | NOT EXECUTED |
| HOME-T09 | Independent novelty/inventive-step / prior-art claim chart for hardware, method and algorithmic directions | NOT EXECUTED — NOVELTY UNKNOWN |
| HOME-T10 | Record public-disclosure authorization, inventorship evidence and any filing decision without implying GitHub disclosure is a patent filing | USER AUTHORIZED REPO PUBLICATION; NO PATENT FILING |
| HOME-T11 | Structural-engineering feasibility of P0 + P1..P4 with load path, soil, lateral/wind/seismic stability, long spans; require explicit comparison to six-plus supports | NOT EXECUTED — DO NOT BUILD |
| HOME-T12 | Independently validate lift, stair, slide, landing, opening, fire/guarding and child-use constraints for multiple core shapes | NOT EXECUTED |
| HOME-T13 | Two legal alternate bedroom locations including eligible corners + at least two interior style profiles with fixed core; also cover wet-room relocation denial | NOT EXECUTED |
| HOME-T14 | Structural-edge accounting: `232` is theoretical; count fixed/protected versus freely reconfigurable edges, installed wall/door modes and edge-specific service/egress exceptions independently | NOT EXECUTED |
| HOME-T15 | Test design governance and no self-authorization; reject any unqualified layout despite a software pass | NOT EXECUTED |
| HOME-T16 | Representation escape: test square-lattice, other pitch, non-grid and simpler layouts; keep null/negative results | NOT EXECUTED |
| HOME-T17 | Safely remove and re-add a thin partition and an engineered thick non-load-bearing wall at the same edge repeatedly, with measured time, personnel, tools, damage, waste and cost; exclude structural and ordinary load-bearing masonry | NOT EXECUTED |
| HOME-T18 | Reject any optional solid no-door wall that destroys safe access/egress, fire compartment performance, maintenance access or ventilation, including during the construction transition | NOT EXECUTED |
| HOME-T19 | Validate door configurations NONE / hinged / sliding / pocket / folding / rated where compatible, including privacy, accessibility, clear opening, hinges, power and child safety | NOT EXECUTED |
| HOME-T20 | Show a three-stage *occupied-life* reconfiguration from open cells → solid thick wall without door → thin wall with door, while keeping five-support proposal unchanged and independently rechecking services, authority, fire and evacuation | NOT EXECUTED |

## Evidence rules

- Source/design specification does not prove implementation, testing, engineering adequacy, legal approval or patentability.
- Any failed safety-critical check means no 'buildable' status; UNKNOWN does not become PASS by a drawing, simulation, endorsement or successful arithmetic.
- **Latest requirement precedence (2026-11-23):** optional walls and optional doors supersede the historical all-neighbour installed-door mandate. Preserve both descriptions in provenance; do not silently enforce historical requirements as current.
- "Easily removable at any time" is an engineering/user-experience target, never permission to alter load-bearing/shear walls, protected shafts or rated fire separations or to skip required permits and inspection. A visually thick wall must still have a qualified nonstructural, lightweight/demountable construction.
- For egress test, consider doors locked at night, power failure, smoke, inaccessible lift and an occupant needing assisted evacuation.
- For physical proof, use independent structural/fire/accessibility professionals and relevant building authority approval; the five-principal-column design is **only a concept**.
- For rights/novelty, compare actual claim elements with substantive prior art; a patent-style title in GitHub does not create patent rights.
- Garden source/admission must preserve version epochs, source lineage, nonclaims, human authority and evidence provenance.

## Decision

**Preliminary result:** `RETAIN_AS_NONCANONICAL_V16_CANDIDATE`. No claim of Garden v16 canonical source admission, construction readiness or patent grant. Reassess only with independently collected evidence.
