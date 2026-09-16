------------------------- MODULE Recovery -------------------------
EXTENDS Naturals, FiniteSets, TLC

(***************************************************************************
Finite safety model for one idempotent consequential effect.  A durably
issued claim immediately advances the target fencing epoch.  Dispatch is the target commit point; an
acknowledgement is deliberately separate.  EnforceFence is FALSE only for
the negative control run.
***************************************************************************)

CONSTANTS Workers, MaxEpoch, EnforceFence

VARIABLES pc, epoch, issued, targetFence, effectDone, attemptEffect,
          permission, revoked, staleAccepted, unauthorizedEffect

vars == <<pc, epoch, issued, targetFence, effectDone, attemptEffect,
          permission, revoked, staleAccepted, unauthorizedEffect>>

States == {"Idle", "Claimed", "Permitted", "Uncertain", "Committed", "Done"}
Max2(a, b) == IF a >= b THEN a ELSE b

Init ==
  /\ pc = [w \in Workers |-> "Idle"]
  /\ epoch = [w \in Workers |-> 0]
  /\ issued = 0
  /\ targetFence = 0
  /\ effectDone = FALSE
  /\ attemptEffect = [w \in Workers |-> FALSE]
  /\ permission = TRUE
  /\ revoked = FALSE
  /\ staleAccepted = FALSE
  /\ unauthorizedEffect = FALSE

Claim(w) ==
  /\ pc[w] = "Idle"
  /\ issued < MaxEpoch
  /\ pc' = [pc EXCEPT ![w] = "Claimed"]
  /\ epoch' = [epoch EXCEPT ![w] = issued + 1]
  /\ issued' = issued + 1
  /\ targetFence' = issued + 1
  /\ UNCHANGED <<effectDone, attemptEffect, permission, revoked,
                  staleAccepted, unauthorizedEffect>>

Admit(w) ==
  /\ pc[w] = "Claimed"
  /\ permission /\ ~revoked
  /\ pc' = [pc EXCEPT ![w] = "Permitted"]
  /\ UNCHANGED <<epoch, issued, targetFence, effectDone, attemptEffect,
                  permission, revoked, staleAccepted, unauthorizedEffect>>

Revoke ==
  /\ ~revoked
  /\ revoked' = TRUE
  /\ permission' = FALSE
  /\ UNCHANGED <<pc, epoch, issued, targetFence, effectDone, attemptEffect,
                  staleAccepted, unauthorizedEffect>>

Acceptable(w) == permission /\ ~revoked /\ (~EnforceFence \/ epoch[w] >= targetFence)

Dispatch(w) ==
  /\ pc[w] = "Permitted"
  /\ Acceptable(w)
  /\ pc' = [pc EXCEPT ![w] = "Committed"]
  /\ targetFence' = Max2(targetFence, epoch[w])
  /\ effectDone' = TRUE
  /\ attemptEffect' = [attemptEffect EXCEPT ![w] = TRUE]
  /\ staleAccepted' = (staleAccepted \/ epoch[w] < targetFence)
  /\ unauthorizedEffect' = (unauthorizedEffect \/ ~permission \/ revoked)
  /\ UNCHANGED <<epoch, issued, permission, revoked>>

Ack(w) ==
  /\ pc[w] = "Committed"
  /\ pc' = [pc EXCEPT ![w] = "Done"]
  /\ UNCHANGED <<epoch, issued, targetFence, effectDone, attemptEffect,
                  permission, revoked, staleAccepted, unauthorizedEffect>>

LostAck(w) ==
  /\ pc[w] = "Committed"
  /\ pc' = [pc EXCEPT ![w] = "Uncertain"]
  /\ UNCHANGED <<epoch, issued, targetFence, effectDone, attemptEffect,
                  permission, revoked, staleAccepted, unauthorizedEffect>>

Crash(w) ==
  /\ pc[w] \in {"Claimed", "Permitted", "Committed"}
  /\ pc' = [pc EXCEPT ![w] = "Uncertain"]
  /\ UNCHANGED <<epoch, issued, targetFence, effectDone, attemptEffect,
                  permission, revoked, staleAccepted, unauthorizedEffect>>

(***************************************************************************
A stale process can still arrive at the boundary after local crash.  The
target must reject it by epoch.  With fencing disabled this is the intended
negative-control counterexample even though effect identity remains idempotent.
***************************************************************************)
LateDispatch(w) ==
  /\ pc[w] = "Uncertain"
  /\ ~attemptEffect[w]
  /\ Acceptable(w)
  /\ pc' = [pc EXCEPT ![w] = "Committed"]
  /\ targetFence' = Max2(targetFence, epoch[w])
  /\ effectDone' = TRUE
  /\ attemptEffect' = [attemptEffect EXCEPT ![w] = TRUE]
  /\ staleAccepted' = (staleAccepted \/ epoch[w] < targetFence)
  /\ unauthorizedEffect' = (unauthorizedEffect \/ ~permission \/ revoked)
  /\ UNCHANGED <<epoch, issued, permission, revoked>>

Reconcile(w) ==
  /\ pc[w] = "Uncertain"
  /\ IF attemptEffect[w]
        THEN pc' = [pc EXCEPT ![w] = "Done"]
        ELSE pc' = [pc EXCEPT ![w] = "Idle"]
  /\ UNCHANGED <<epoch, issued, targetFence, effectDone, attemptEffect,
                  permission, revoked, staleAccepted, unauthorizedEffect>>

Next ==
  \/ Revoke
  \/ \E w \in Workers : Claim(w) \/ Admit(w) \/ Dispatch(w) \/ Ack(w)
                         \/ LostAck(w) \/ Crash(w) \/ LateDispatch(w)
                         \/ Reconcile(w)

Spec == Init /\ [][Next]_vars /\ WF_vars(\E w \in Workers : Reconcile(w))

TypeOK ==
  /\ pc \in [Workers -> States]
  /\ epoch \in [Workers -> 0..MaxEpoch]
  /\ issued \in 0..MaxEpoch
  /\ targetFence \in 0..MaxEpoch
  /\ attemptEffect \in [Workers -> BOOLEAN]
  /\ effectDone \in BOOLEAN
  /\ permission \in BOOLEAN /\ revoked \in BOOLEAN
  /\ staleAccepted \in BOOLEAN /\ unauthorizedEffect \in BOOLEAN

EpochsIssuedMonotonically == \A w \in Workers : epoch[w] <= issued
FenceTracksLatestIssuedClaim == targetFence = issued
CommittedHasEffect == \A w \in Workers : pc[w] \in {"Committed", "Done"} => attemptEffect[w]
NoUnauthorizedEffect == ~unauthorizedEffect
NoStaleFenceAccepted == ~staleAccepted
IdempotentBoundary == effectDone = (\E w \in Workers : attemptEffect[w])

=============================================================================
