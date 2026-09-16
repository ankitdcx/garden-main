"""Bounded local permission/recovery reference boundary.

Coordinator and reference target share one SQLite transaction.  This models an
atomic local boundary; it does not claim fencing or exactly-once behavior for a
distributed target that does not implement the same protocol.
"""
from __future__ import annotations

from contextlib import contextmanager
import json
import sqlite3

from .core import SemanticError


class PermissionRecoveryBoundary:
    def __init__(self, path, *, fixture_permission=True):
        """Create a reference boundary.

        ``fixture_permission`` is test-fixture state only.  It is not an
        external authority grant and this module is not production-wired.
        """
        if type(fixture_permission) is not bool:
            raise SemanticError("fixture_permission must be boolean")
        self.db = sqlite3.connect(path, isolation_level=None)
        self.db.row_factory = sqlite3.Row
        self.db.execute("PRAGMA synchronous=FULL")
        self.db.executescript("""
          CREATE TABLE IF NOT EXISTS meta(key TEXT PRIMARY KEY,value INTEGER NOT NULL);
          CREATE TABLE IF NOT EXISTS tasks(id TEXT PRIMARY KEY,effect TEXT NOT NULL,payload TEXT NOT NULL);
          CREATE TABLE IF NOT EXISTS attempts(id INTEGER PRIMARY KEY AUTOINCREMENT,task TEXT NOT NULL,
            worker TEXT NOT NULL,epoch INTEGER NOT NULL,state TEXT NOT NULL,permit_epoch INTEGER,result TEXT);
          CREATE TABLE IF NOT EXISTS effects(id TEXT PRIMARY KEY,payload TEXT NOT NULL,highest_epoch INTEGER NOT NULL,
            committed INTEGER NOT NULL DEFAULT 0,result TEXT);
          CREATE TABLE IF NOT EXISTS trace(seq INTEGER PRIMARY KEY AUTOINCREMENT,action TEXT NOT NULL,detail TEXT NOT NULL);
        """)
        with self.tx():
            self.db.execute("INSERT OR IGNORE INTO meta VALUES('issued_epoch',0)")
            self.db.execute("INSERT OR IGNORE INTO meta VALUES('permission',?)", (int(fixture_permission),))
            self.db.execute("INSERT OR IGNORE INTO meta VALUES('revoked',0)")
            self.db.execute("INSERT OR IGNORE INTO meta VALUES('fixture_authority',1)")

    @contextmanager
    def tx(self):
        self.db.execute("BEGIN IMMEDIATE")
        try:
            yield
            self.db.execute("COMMIT")
        except BaseException:
            self.db.execute("ROLLBACK")
            raise

    def _event(self, action, **detail):
        self.db.execute("INSERT INTO trace(action,detail) VALUES(?,?)", (action, json.dumps(detail, sort_keys=True)))

    def _meta(self, key):
        return self.db.execute("SELECT value FROM meta WHERE key=?", (key,)).fetchone()[0]

    def enqueue(self, task_id, effect_id, payload):
        if not all(isinstance(x, str) and x for x in (task_id, effect_id)):
            raise SemanticError("task and effect identity required")
        body = json.dumps(payload, sort_keys=True, separators=(",", ":"), allow_nan=False)
        with self.tx():
            old = self.db.execute("SELECT effect,payload FROM tasks WHERE id=?", (task_id,)).fetchone()
            if old:
                if (old[0], old[1]) != (effect_id, body):
                    raise SemanticError("idempotency identity rebound")
                return
            if self.db.execute("SELECT 1 FROM tasks WHERE effect=?", (effect_id,)).fetchone():
                raise SemanticError("effect identity already belongs to another task")
            self.db.execute("INSERT INTO tasks VALUES(?,?,?)", (task_id, effect_id, body))
            self.db.execute("INSERT OR IGNORE INTO effects(id,payload,highest_epoch) VALUES(?,?,0)", (effect_id, body))
            target = self.db.execute("SELECT payload FROM effects WHERE id=?", (effect_id,)).fetchone()[0]
            if target != body:
                raise SemanticError("effect identity rebound")
            self._event("Enqueue", task=task_id, effect=effect_id)

    def claim(self, task_id, worker):
        if not isinstance(worker, str) or not worker or worker != worker.strip():
            raise SemanticError("nonempty canonical worker identity required")
        with self.tx():
            if not self.db.execute("SELECT 1 FROM tasks WHERE id=?", (task_id,)).fetchone():
                raise SemanticError("unknown task")
            epoch = self._meta("issued_epoch") + 1
            self.db.execute("UPDATE meta SET value=? WHERE key='issued_epoch'", (epoch,))
            effect = self.db.execute("SELECT effect FROM tasks WHERE id=?", (task_id,)).fetchone()[0]
            self.db.execute("UPDATE effects SET highest_epoch=? WHERE id=? AND highest_epoch<?", (epoch, effect, epoch))
            cur = self.db.execute("INSERT INTO attempts(task,worker,epoch,state) VALUES(?,?,?,'Claimed')", (task_id, worker, epoch))
            attempt = cur.lastrowid
            self._event("Claim", attempt=attempt, worker=worker, epoch=epoch)
            return {"attempt": attempt, "epoch": epoch, "task": task_id, "worker": worker}

    def admit(self, claim):
        with self.tx():
            row = self._attempt(claim)
            if row["state"] != "Claimed" or not self._meta("permission") or self._meta("revoked"):
                raise SemanticError("permission unavailable")
            self.db.execute("UPDATE attempts SET state='Permitted',permit_epoch=? WHERE id=?", (row["epoch"], row["id"]))
            self._event("Admit", attempt=row["id"], epoch=row["epoch"])

    def revoke(self):
        with self.tx():
            self.db.execute("UPDATE meta SET value=0 WHERE key='permission'")
            self.db.execute("UPDATE meta SET value=1 WHERE key='revoked'")
            self._event("Revoke")

    def dispatch(self, claim, *, lose_ack=False):
        """Atomically recheck permission/fence and commit the idempotent effect."""
        if type(lose_ack) is not bool:
            raise SemanticError("lose_ack must be boolean")
        stale = None
        with self.tx():
            row = self._attempt(claim)
            if row["state"] != "Permitted":
                raise SemanticError("attempt is not dispatchable")
            task = self.db.execute("SELECT * FROM tasks WHERE id=?", (row["task"],)).fetchone()
            effect = self.db.execute("SELECT * FROM effects WHERE id=?", (task["effect"],)).fetchone()
            if not self._meta("permission") or self._meta("revoked"):
                raise SemanticError("permission revoked before commit")
            if row["epoch"] < effect["highest_epoch"]:
                self._event("RejectStaleFence", attempt=row["id"], epoch=row["epoch"], highest=effect["highest_epoch"])
                stale = True
            else:
                result = effect["result"]
                if not effect["committed"]:
                    result = json.dumps({"effect": effect["id"], "payload": json.loads(effect["payload"])}, sort_keys=True)
                    self.db.execute("UPDATE effects SET committed=1,result=? WHERE id=?", (result, effect["id"]))
                state = "Uncertain" if lose_ack else "Committed"
                self.db.execute("UPDATE attempts SET state=?,result=? WHERE id=?", (state, result, row["id"]))
                self._event("LostAck" if lose_ack else "Dispatch", attempt=row["id"], epoch=row["epoch"], idempotent=bool(effect["committed"]))
        if stale:
            raise SemanticError("stale fencing epoch")
        return json.loads(result)

    def acknowledge(self, claim):
        with self.tx():
            row = self._attempt(claim)
            if row["state"] != "Committed":
                raise SemanticError("no committed observation to acknowledge")
            self.db.execute("UPDATE attempts SET state='Done' WHERE id=?", (row["id"],))
            self._event("Ack", attempt=row["id"])

    def crash(self, claim):
        with self.tx():
            row = self._attempt(claim)
            if row["state"] not in {"Claimed", "Permitted", "Committed"}:
                raise SemanticError("attempt cannot crash from current state")
            self.db.execute("UPDATE attempts SET state='Uncertain' WHERE id=?", (row["id"],))
            self._event("Crash", attempt=row["id"], prior=row["state"])

    def reconcile(self, claim, *, authoritative_not_executed=False):
        if type(authoritative_not_executed) is not bool:
            raise SemanticError("authoritative_not_executed must be boolean")
        with self.tx():
            row = self._attempt(claim)
            if row["state"] != "Uncertain":
                raise SemanticError("only uncertain attempts reconcile")
            task = self.db.execute("SELECT effect FROM tasks WHERE id=?", (row["task"],)).fetchone()
            effect = self.db.execute("SELECT * FROM effects WHERE id=?", (task[0],)).fetchone()
            if effect["committed"]:
                state, result = "Done", effect["result"]
            elif authoritative_not_executed:
                state, result = "Idle", None
            else:
                raise SemanticError("authoritative reconciliation evidence required")
            self.db.execute("UPDATE attempts SET state=?,result=? WHERE id=?", (state, result, row["id"]))
            self._event("Reconcile", attempt=row["id"], state=state)
            return state

    def _attempt(self, claim):
        row = self.db.execute("SELECT * FROM attempts WHERE id=?", (claim.get("attempt"),)).fetchone()
        if (not row or row["epoch"] != claim.get("epoch") or row["worker"] != claim.get("worker")
                or row["task"] != claim.get("task")):
            raise SemanticError("unknown or rebound claim")
        return row

    def snapshot(self):
        effects = [dict(x) for x in self.db.execute("SELECT * FROM effects ORDER BY id")]
        attempts = [dict(x) for x in self.db.execute("SELECT * FROM attempts ORDER BY id")]
        trace = [{"action": x[0], **json.loads(x[1])} for x in self.db.execute("SELECT action,detail FROM trace ORDER BY seq")]
        return {"permission": bool(self._meta("permission")), "revoked": bool(self._meta("revoked")),
                "effects": effects, "attempts": attempts, "trace": trace}

    def close(self):
        self.db.close()
