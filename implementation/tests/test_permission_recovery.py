import tempfile
import unittest
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor

from garden_kernel.core import SemanticError
from garden_kernel.permission_recovery import PermissionRecoveryBoundary


class PermissionRecoveryTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(); self.addCleanup(self.tmp.cleanup)
        self.path = Path(self.tmp.name) / "boundary.sqlite"
        self.b = PermissionRecoveryBoundary(self.path, fixture_permission=True); self.addCleanup(self.b.close)
        self.b.enqueue("t", "effect-1", {"value": 1})

    def permitted(self, worker="w1"):
        c = self.b.claim("t", worker); self.b.admit(c); return c

    def test_dispatch_ack_commit(self):
        c=self.permitted(); self.b.dispatch(c); self.b.acknowledge(c)
        s=self.b.snapshot(); self.assertEqual(s["attempts"][0]["state"],"Done"); self.assertEqual(s["effects"][0]["committed"],1)

    def test_revoke_before_commit_blocks(self):
        c=self.permitted(); self.b.revoke()
        with self.assertRaisesRegex(SemanticError,"revoked"): self.b.dispatch(c)
        self.assertEqual(self.b.snapshot()["effects"][0]["committed"],0)

    def test_revoke_after_commit_does_not_erase_effect(self):
        c=self.permitted(); self.b.dispatch(c,lose_ack=True); self.b.revoke()
        self.assertEqual(self.b.reconcile(c),"Done"); self.assertEqual(self.b.snapshot()["effects"][0]["committed"],1)

    def test_lost_ack_is_unknown_then_reconciled(self):
        c=self.permitted(); self.b.dispatch(c,lose_ack=True)
        self.assertEqual(self.b.snapshot()["attempts"][0]["state"],"Uncertain"); self.assertEqual(self.b.reconcile(c),"Done")

    def test_crash_before_dispatch_requires_authoritative_nonexecution(self):
        c=self.permitted(); self.b.crash(c)
        with self.assertRaisesRegex(SemanticError,"evidence"): self.b.reconcile(c)
        self.assertEqual(self.b.reconcile(c,authoritative_not_executed=True),"Idle")

    def test_stale_concurrent_worker_rejected(self):
        old=self.permitted("w1"); new=self.permitted("w2")
        with self.assertRaisesRegex(SemanticError,"stale fencing"): self.b.dispatch(old)
        state=self.b.snapshot(); self.assertEqual(state["effects"][0]["highest_epoch"],new["epoch"])
        self.assertEqual(state["effects"][0]["committed"],0)
        self.assertIn("RejectStaleFence",[x["action"] for x in state["trace"]])
        self.b.dispatch(new)

    def test_effect_identity_is_idempotent(self):
        a=self.permitted("w1"); r1=self.b.dispatch(a)
        b=self.permitted("w2"); r2=self.b.dispatch(b)
        self.assertEqual(r1,r2); self.assertEqual(len(self.b.snapshot()["effects"]),1)

    def test_restart_preserves_unknown_and_fence(self):
        c=self.permitted(); self.b.dispatch(c,lose_ack=True); self.b.close()
        self.b=PermissionRecoveryBoundary(self.path, fixture_permission=True)
        self.assertEqual(self.b.reconcile(c),"Done")
        later=self.b.claim("t","w2"); self.assertGreater(later["epoch"],c["epoch"])

    def test_identity_rebinding_rejected(self):
        with self.assertRaisesRegex(SemanticError,"rebound"): self.b.enqueue("t","effect-1",{"value":2})

    def test_duplicate_effect_different_task_is_typed(self):
        with self.assertRaisesRegex(SemanticError,"another task"): self.b.enqueue("other","effect-1",{"value":1})

    def test_claim_task_field_cannot_be_rebound(self):
        c=self.permitted(); c["task"]="other"
        with self.assertRaisesRegex(SemanticError,"rebound"): self.b.dispatch(c)

    def test_uncertain_never_dispatches_without_reconciliation(self):
        c=self.permitted(); self.b.crash(c)
        with self.assertRaisesRegex(SemanticError,"not dispatchable"): self.b.dispatch(c)

    def test_two_connections_issue_unique_ordered_epochs(self):
        def take(worker):
            x=PermissionRecoveryBoundary(self.path,fixture_permission=True)
            try:return x.claim("t",worker)
            finally:x.close()
        with ThreadPoolExecutor(2) as pool:
            claims=list(pool.map(take,("w1","w2")))
        self.assertEqual(sorted(x["epoch"] for x in claims),[1,2])

    def test_fixture_permission_can_start_denied(self):
        other=PermissionRecoveryBoundary(Path(self.tmp.name)/"denied.sqlite",fixture_permission=False)
        try:
            other.enqueue("x","effect-x",{}); claim=other.claim("x","w")
            with self.assertRaisesRegex(SemanticError,"permission unavailable"): other.admit(claim)
        finally: other.close()

    def test_worker_identity_is_enforced(self):
        for worker in (None,""," w "):
            with self.subTest(worker=worker), self.assertRaisesRegex(SemanticError,"worker identity"):
                self.b.claim("t",worker)

    def test_boolean_controls_are_strict_and_state_unchanged(self):
        c=self.permitted();before=self.b.snapshot()
        with self.assertRaisesRegex(SemanticError,"lose_ack"):self.b.dispatch(c,lose_ack="yes")
        self.assertEqual(self.b.snapshot(),before)
        self.b.crash(c);before=self.b.snapshot()
        with self.assertRaisesRegex(SemanticError,"authoritative_not_executed"):self.b.reconcile(c,authoritative_not_executed="unknown")
        self.assertEqual(self.b.snapshot(),before)


if __name__ == "__main__": unittest.main()
