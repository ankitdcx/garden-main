# Appointment-reminder composition fixture

**Status** Bounded candidate integration example. The [reference tests](../../verification/test_design_cases.py) exercise a synthetic state machine. Their outcomes apply to this fixture.

| Stage | Existing owner | Frozen behavior |
|---|---|---|
| Map | USM | Bind an immutable request to an appointment, recipient, purpose, permission reference and logical time. |
| Expand | MCC / DSC | Visit the registered obligations in a stable order. A logical work limit emits INCOMPLETE and the unvisited frontier. Wall-clock interruption is operational. Resume at the last committed logical checkpoint. |
| Authorize and apply | Authority / VEI | At the simulated effect, check the current scoped grant, freshness, expiry and revocation, and verify the recipient and purpose. Bind the effect to the exact appointment request. |
| Record | Transition / VEI | Keep the responsible holder, effect identity and outcome. Repeating a completed request cannot create a second effect in the fixture. |

When two runs reach the same logical checkpoint under the same frozen facts, their semantic results must agree. If the relevant permission changes while work is paused, the resumed run must check current permission before applying an effect. An unrelated evidence revision cannot revoke a valid grant. A missing delegation qualifier keeps the action unresolved. A denied or unfinished run sends zero reminders. A valid positive control sends exactly one. The model assumes one process and an atomic in-memory final check and effect. Distributed fencing, durable recovery, delivery to external targets and actual Garden implementations require separate qualification.
