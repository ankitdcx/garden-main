"""Synthetic numerical and appointment controls; run directly with Python 3."""
from dataclasses import dataclass, replace
from math import sqrt
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from check_design import ROOT, verify_receipt, verify_release


def paired_errors(both, first_only, second_only, neither):
    counts = (both, first_only, second_only, neither)
    if any(type(value) is not int or value < 0 for value in counts):
        raise ValueError("expected four nonnegative integer counts")
    total = sum(counts)
    product = (both + first_only) * (second_only + neither) * (both + second_only) * (first_only + neither)
    joint = both / total if total else None
    phi = (both * neither - first_only * second_only) / sqrt(product) if product else None
    return joint, phi


@dataclass(frozen=True)
class Reminder:
    appointment: str = "demo-7"
    recipient: str = "person-a"
    purpose: str = "appointment-reminder"
    grant_id: str = "grant-1"


@dataclass(frozen=True)
class Grant:
    identity: str = "grant-1"
    recipient: str = "person-a"
    purpose: str = "appointment-reminder"
    valid_from: int = 1
    expires: int = 10
    revoked: bool = False


# A checkpoint belongs to this immutable request and frozen obligation order.
OBLIGATIONS = ("recipient", "purpose", "grant_id")


@dataclass(frozen=True)
class Checkpoint:
    request: Reminder
    visited: int = 0

    @property
    def frontier(self):
        return OBLIGATIONS[self.visited:]

    def advance(self, steps):
        if steps < 0:
            raise ValueError("negative work budget")
        return replace(self, visited=min(len(OBLIGATIONS), self.visited + steps))


class ReminderCase:
    def __init__(self):
        self.grants = {"grant-1": Grant()}
        self.unrelated_evidence_revision = 0
        self.effects = set()

    def apply(self, checkpoint, now):
        req = checkpoint.request
        if req in self.effects:
            outcome = "ALREADY_RECORDED"
        elif checkpoint.frontier:
            outcome = "INCOMPLETE"
        elif not all(getattr(req, key) for key in OBLIGATIONS) or req.grant_id not in self.grants:
            outcome = "UNRESOLVED"
        else:
            grant = self.grants[req.grant_id]
            scoped = (req.grant_id, req.recipient, req.purpose) == (grant.identity, grant.recipient, grant.purpose)
            if not all((grant.identity, grant.recipient, grant.purpose)) or None in (grant.valid_from, grant.expires, grant.revoked, now):
                outcome = "UNRESOLVED"
            elif grant.revoked or not scoped or not (grant.valid_from <= now < grant.expires):
                outcome = "BLOCKED"
            else:
                self.effects.add(req)
                outcome = "RECORDED"
        return {"outcome": outcome, "request": req, "holder": "demo-reminder-desk"}


class DesignCases(unittest.TestCase):
    def test_sct_counts(self):
        self.assertEqual(paired_errors(1, 9, 9, 81), (0.01, 0.0))
        joint, phi = paired_errors(1, 0, 0, 99)
        self.assertEqual((joint, phi), (0.01, 1.0))
        self.assertEqual(2 / (1 + phi), 1.0)
        self.assertEqual(paired_errors(0, 0, 10, 90), (0, None))
        self.assertEqual(paired_errors(0, 0, 0, 0), (None, None))
        with self.assertRaises(ValueError):
            paired_errors(-1, 2, 3, 4)

    def test_failed_verdict(self):
        with self.assertRaisesRegex(ValueError, "did not return PASS"):
            verify_receipt({"status": "FAIL"}, {"status": "FAIL"})

    def test_each_missing_role(self):
        source = ROOT / "canonical/current"
        for omit in source.glob("Garden_*.txt"):
            with self.subTest(omit=omit.name), TemporaryDirectory() as folder:
                target = Path(folder)
                for p in source.iterdir():
                    if p != omit:
                        (target / p.name).symlink_to(p)
                with self.assertRaisesRegex(ValueError, "source file set"):
                    verify_release(target)

    def test_progress_and_retry(self):
        state = ReminderCase()
        start = Checkpoint(Reminder())
        partial = start.advance(1)
        self.assertEqual(partial.frontier, ("purpose", "grant_id"))
        self.assertEqual(state.apply(partial, 2)["outcome"], "INCOMPLETE")
        self.assertFalse(state.effects)
        state.unrelated_evidence_revision += 1
        completed = partial.advance(2)
        self.assertEqual(completed, start.advance(3))
        self.assertEqual(state.apply(completed, 4)["outcome"], "RECORDED")
        self.assertEqual(state.apply(completed, 5)["outcome"], "ALREADY_RECORDED")
        self.assertEqual(state.effects, {start.request})

    def test_worker_speed_and_resume(self):
        outcomes = []
        for cost_per_step in (1, 3):
            # A six-tick interruption lets the faster worker finish three obligations.
            state = ReminderCase()
            checkpoint = Checkpoint(Reminder()).advance(6 // cost_per_step)
            if checkpoint.frontier:
                self.assertEqual(state.apply(checkpoint, 3)["outcome"], "INCOMPLETE")
            completed = checkpoint.advance(len(checkpoint.frontier))
            outcomes.append((completed, state.apply(completed, 4), state.effects))
        self.assertEqual(outcomes[0], outcomes[1])
        self.assertEqual(outcomes[0][1]["outcome"], "RECORDED")

    def test_current_permission(self):
        for grant, now in ((Grant(revoked=True), 3), (Grant(), 10), (Grant(), 0),
                           (Grant(recipient="person-b"), 3), (Grant(purpose="marketing"), 3)):
            with self.subTest(grant=grant, now=now):
                state = ReminderCase()
                planned = Checkpoint(Reminder()).advance(2)
                state.grants["grant-1"] = grant
                receipt = state.apply(planned.advance(1), now)
                self.assertEqual((receipt["outcome"], receipt["holder"]), ("BLOCKED", "demo-reminder-desk"))
                self.assertFalse(state.effects)

    def test_incomplete_grant(self):
        state = ReminderCase()
        state.grants["grant-1"] = Grant(purpose="")
        self.assertEqual(state.apply(Checkpoint(Reminder()).advance(3), 3)["outcome"], "UNRESOLVED")
        self.assertFalse(state.effects)

    def test_missing_qualifier(self):
        for request in (Reminder(grant_id=""), Reminder(purpose=""), Reminder(grant_id="missing")):
            state = ReminderCase()
            self.assertEqual(state.apply(Checkpoint(request).advance(3), 4)["outcome"], "UNRESOLVED")
            self.assertFalse(state.effects)


if __name__ == "__main__":
    unittest.main()
