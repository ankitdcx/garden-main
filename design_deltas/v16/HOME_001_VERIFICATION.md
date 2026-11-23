# GARDEN-HOME-001 — Verification and admission checklist

**Scope:** v16 candidate `GARDEN-HOME-001`; **current state:** design arithmetic checked, physical/legal/patent evidence absent. Noncanonical, non-admitting.

## Invariants and test obligations

| ID | Test / evidence needed | Current status |
|---|---|---|
| HOME-T01 | Recompute `16×8=128` cells/floor; `16×4=64`/wing; `3×128=384` gross positions; `(15×8)+(16×7)=232` interior undirected edges/floor | PASS — nominal arithmetic only |
| HOME-T02 | Map every allowed orthogonal shared edge to an *installed* door under literal user baseline; enumerate blocked structural/fire/shaft edges and consequence | NOT EXECUTED |
| HOME-T03 | Produce feasible and accessible 100/150/175/200/300-sq-ft connected room layouts after partition thickness; reject insufficient daylight or floor area | NOT EXECUTED |
| HOME-T04 | Exchange a 25-sq-ft corridor cell and a room cell without losing occupied-room egress, accessibility or emergency response | NOT EXECUTED |
| HOME-T05 | Prototype four-door junction and any full-edge hardware under fire, acoustic, clearance, disability and hardware clash checks | NOT EXECUTED |
| HOME-T06 | Reconcile gross/net area, open voids, garden, terrace, service spaces and actual permitted floor-area ratio | NOT EXECUTED |
| HOME-T07 | Validate shaft and wet-service connectivity, plumbing slopes, ventilation, electricity, fire compartment and maintenance access | NOT EXECUTED |
| HOME-T08 | Compare full-door, door-ready, fixed-corridor and movable-partition baselines with matched usable area, engineering constraints, lifecycle costs and labor | NOT EXECUTED |
| HOME-T09 | Independent novelty/inventive-step / prior-art claim chart for hardware, method and algorithmic directions | NOT EXECUTED — NOVELTY UNKNOWN |
| HOME-T10 | Record public-disclosure authorization, inventorship evidence and any filing decision without implying GitHub disclosure is a patent filing | USER AUTHORIZED REPO PUBLICATION; NO PATENT FILING |
| HOME-T11 | Structural-engineering feasibility of P0 + P1..P4 with load path, soil, lateral/wind/seismic stability, long spans; require explicit comparison to six-plus supports | NOT EXECUTED — DO NOT BUILD |
| HOME-T12 | Independently validate lift, stair, slide, landing, opening, fire/guarding and child-use constraints for multiple core shapes | NOT EXECUTED |
| HOME-T13 | Two legal alternate bedroom locations including eligible corners + at least two interior style profiles with fixed core; also cover wet-room relocation denial | NOT EXECUTED |
| HOME-T14 | Structural-edge accounting: `232` is theoretical; count forbidden, door-fitted and door-ready edges independently | NOT EXECUTED |
| HOME-T15 | Test design governance and no self-authorization; reject any unqualified layout despite a software pass | NOT EXECUTED |
| HOME-T16 | Representation escape: test square-lattice, other pitch, non-grid and simpler layouts; keep null/negative results | NOT EXECUTED |

## Evidence rules

- Source/design specification does not prove implementation, testing, engineering adequacy, legal approval or patentability.
- Any failed safety-critical check means no 'buildable' status; UNKNOWN does not become PASS by a drawing, simulation, endorsement or successful arithmetic.
- For egress test, consider doors locked at night, power failure, smoke, inaccessible lift and an occupant needing assisted evacuation.
- For physical proof, use independent structural/fire/accessibility professionals and relevant building authority approval; the five-principal-column design is **only a concept**.
- For rights/novelty, compare actual claim elements with substantive prior art; a patent-style title in GitHub does not create patent rights.
- Garden source/admission must preserve version epochs, source lineage, nonclaims, human authority and evidence provenance.

## Decision

**Preliminary result:** `RETAIN_AS_NONCANONICAL_V16_CANDIDATE`. No claim of Garden v16 canonical source admission, construction readiness or patent grant. Reassess only with independently collected evidence.
