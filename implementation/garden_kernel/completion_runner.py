"""Completion-driven execution substrate; no scheduler, provider or authority built in.

All workers must use ONE persistent database. SQLite transactions arbitrate claims;
the external call happens only after its reservation commits. An interrupted call
is UNKNOWN and is never retried automatically. Hash chains detect corruption, not
hostile database replacement: deployments must retain an external checkpoint.
"""
from __future__ import annotations

from contextlib import contextmanager
from dataclasses import dataclass
from datetime import datetime, timezone
from hashlib import sha256
import json
import math
import sqlite3
from typing import Callable
from uuid import uuid4

from .core import SemanticError
from .process_engine import CycleBinding, ProcessFactory, ProcessState


def encoded(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)


def digest(value):
    return sha256(encoded(value).encode()).hexdigest()


def text(value):
    if not isinstance(value, str) or not value or value != value.strip():
        raise SemanticError("nonempty canonical string required")
    return value


def integer(value, minimum=0):
    if type(value) is not int or value < minimum:
        raise SemanticError("bounded integer required")
    return value


def timestamp(value):
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value) or value < 0:
        raise SemanticError("finite nonnegative UTC timestamp required")
    return value


@dataclass(frozen=True)
class Limits:
    # Integer microdollars avoid floating-point accounting errors.
    daily_micro_usd: int = 1_000_000
    free_daily: int = 48
    free_hourly: int = 2
    max_attempts: int = 3
    lease_seconds: int = 300
    cooldown_seconds: int = 60
    max_steps_per_wake: int = 32

    def __post_init__(self):
        for field in self.__dataclass_fields__:
            integer(getattr(self, field), 1)


class CompletionStore:
    def __init__(self, path, limits=Limits()):
        self.limits = limits
        self.db = sqlite3.connect(path, timeout=30, isolation_level=None)
        self.db.row_factory = sqlite3.Row
        self.db.execute("PRAGMA foreign_keys=ON")
        self.db.execute("PRAGMA synchronous=FULL")
        self.db.executescript("""
            CREATE TABLE IF NOT EXISTS meta (key TEXT PRIMARY KEY, value TEXT NOT NULL);
            CREATE TABLE IF NOT EXISTS cycles (id TEXT PRIMARY KEY, record TEXT NOT NULL);
            CREATE TABLE IF NOT EXISTS tasks (
                id TEXT PRIMARY KEY, cycle TEXT NOT NULL REFERENCES cycles(id),
                spec TEXT NOT NULL, state TEXT NOT NULL, token TEXT,
                lease REAL, attempts INTEGER NOT NULL DEFAULT 0, result TEXT);
            CREATE TABLE IF NOT EXISTS calls (
                token TEXT PRIMARY KEY, task TEXT NOT NULL REFERENCES tasks(id),
                started REAL NOT NULL, pool TEXT NOT NULL, reserved INTEGER NOT NULL,
                charged INTEGER, state TEXT NOT NULL);
            CREATE TABLE IF NOT EXISTS events (
                seq INTEGER PRIMARY KEY, previous TEXT NOT NULL, record TEXT NOT NULL,
                hash TEXT NOT NULL UNIQUE);
        """)
        with self.transaction():
            policy = encoded(limits.__dict__)
            old = self.get_meta("limits")
            if old is not None and old != policy:
                raise SemanticError("shared store limits mismatch; explicit migration required")
            if old is None:
                self.put_meta("limits", policy)
                self.put_meta("paused", True)
                self.put_meta("cooldown", 0)
                self.put_meta("last_time", 0)

    @contextmanager
    def transaction(self):
        self.db.execute("BEGIN IMMEDIATE")
        try:
            yield
            self.db.execute("COMMIT")
        except BaseException:
            self.db.execute("ROLLBACK")
            raise

    def close(self):
        self.db.close()

    def get_meta(self, key):
        row = self.db.execute("SELECT value FROM meta WHERE key=?", (key,)).fetchone()
        return json.loads(row[0]) if row else None

    def put_meta(self, key, value):
        self.db.execute("INSERT OR REPLACE INTO meta VALUES (?,?)", (key, encoded(value)))

    def event(self, kind, payload):
        last = self.db.execute("SELECT hash FROM events ORDER BY seq DESC LIMIT 1").fetchone()
        previous = last[0] if last else "0" * 64
        record = encoded({"kind": kind, "payload": payload})
        hashed = digest({"previous": previous, "record": record})
        self.db.execute("INSERT INTO events(previous,record,hash) VALUES (?,?,?)", (previous, record, hashed))
        return hashed

    def verify_chain(self, expected_head=None):
        previous = "0" * 64
        for row in self.db.execute("SELECT * FROM events ORDER BY seq"):
            if row["previous"] != previous or row["hash"] != digest({"previous": previous, "record": row["record"]}):
                raise SemanticError("execution event chain corrupt")
            previous = row["hash"]
        if expected_head is not None and previous != expected_head:
            raise SemanticError("execution checkpoint mismatch")
        return previous

    def configure(self, *, paused, pool_remaining=None, reconciliation_ref=None):
        if type(paused) is not bool:
            raise SemanticError("paused must be boolean")
        with self.transaction():
            if pool_remaining is not None:
                if self.db.execute("SELECT 1 FROM calls LIMIT 1").fetchone():
                    raise SemanticError("cannot reset balances after calls; reconcile individual attempts")
                text(reconciliation_ref)
                if not pool_remaining or set(pool_remaining) - {"routine", "challenger", "escalation", "emergency_reserve"}:
                    raise SemanticError("unknown or empty budget pools")
                for amount in pool_remaining.values():
                    integer(amount)
                self.put_meta("pools", pool_remaining)
            self.put_meta("paused", paused)
            self.event("CONFIGURE", {"paused": paused, "pool_remaining": pool_remaining, "reconciliation_ref": reconciliation_ref})

    def create_cycle(self, binding, work_id, route, profile):
        process = ProcessFactory.create(route, binding=binding, work_id=work_id)
        record = {"binding": {**binding.__dict__, "repo_heads": dict(binding.repo_heads)},
                  "work_id": work_id, "route": process.route_receipt(),
                  "transitions": [], "profile_hash": digest(profile)}
        with self.transaction():
            row = self.db.execute("SELECT record FROM cycles WHERE id=?", (binding.cycle_id,)).fetchone()
            if row:
                if row[0] != encoded(record):
                    raise SemanticError("cycle already exists; cannot rebind or erase progress")
                return
            self.db.execute("INSERT INTO cycles VALUES (?,?)", (binding.cycle_id, encoded(record)))
            self.event("CYCLE_CREATED", record)

    def restore(self, cycle_id, observed_binding, profile):
        row = self.db.execute("SELECT record FROM cycles WHERE id=?", (cycle_id,)).fetchone()
        if not row:
            raise SemanticError("unknown cycle")
        record = json.loads(row[0])
        if record["binding"] != {**observed_binding.__dict__, "repo_heads": dict(observed_binding.repo_heads)} or record["profile_hash"] != digest(profile):
            raise SemanticError("stale cycle or algebra profile")
        return record, ProcessFactory.restore(record["route"], record["transitions"], binding=observed_binding,
                                               work_id=record["work_id"], algebra_profile=profile)

    def advance(self, cycle_id, binding, profile, target, evidence, verify_gate, source_refs):
        # The verifier is a trusted adapter, never a model-supplied callable.
        with self.transaction():
            record, process = self.restore(cycle_id, binding, profile)
            required = process.required_gates(target)
            if any(gate not in evidence or verify_gate(gate, evidence[gate], binding) is not True for gate in required):
                raise SemanticError("missing, stale or unverified gate evidence")
            receipt = process.advance(target, satisfied_gates=sorted(required), algebra_profile=profile, source_obligation_refs=source_refs)
            record["transitions"].append(receipt)
            self.db.execute("UPDATE cycles SET record=? WHERE id=?", (encoded(record), cycle_id))
            self.event("PROCESS_TRANSITION", {"receipt": receipt, "gate_evidence_hash": digest(evidence)})
            return receipt

    def enqueue(self, task_id, cycle_id, *, handler, dependencies=(), external=False,
                pool="routine", max_cost_micro_usd=0, priority=0, packet_hash=None):
        text(task_id); text(handler); integer(priority)
        integer(max_cost_micro_usd)
        if type(external) is not bool or (not external and max_cost_micro_usd):
            raise SemanticError("invalid external-call specification")
        if pool not in {"routine", "challenger", "escalation", "emergency_reserve"}:
            raise SemanticError("invalid budget pool")
        deps = list(dependencies)
        if len(set(deps)) != len(deps) or task_id in deps:
            raise SemanticError("duplicate or self dependency")
        for dep in deps:
            text(dep)
        spec = dict(handler=handler, dependencies=deps, external=external, pool=pool,
                    max_cost_micro_usd=max_cost_micro_usd, priority=priority, packet_hash=packet_hash)
        with self.transaction():
            old = self.db.execute("SELECT cycle,spec FROM tasks WHERE id=?", (task_id,)).fetchone()
            if old:
                if old[0] != cycle_id or old[1] != encoded(spec):
                    raise SemanticError("idempotency key rebound")
                return
            for dep in deps:
                row = self.db.execute("SELECT cycle FROM tasks WHERE id=?", (dep,)).fetchone()
                if not row or row[0] != cycle_id:
                    raise SemanticError("dependency must already exist in the same cycle")
            self.db.execute("INSERT INTO tasks(id,cycle,spec,state) VALUES (?,?,?,'READY')", (task_id, cycle_id, encoded(spec)))
            self.event("TASK_ENQUEUED", {"task_id": task_id, "cycle_id": cycle_id, "spec": spec})

    def _time(self, now):
        timestamp(now)
        if now < self.get_meta("last_time"):
            raise SemanticError("clock moved backwards; reconciliation required")
        self.put_meta("last_time", now)

    def claim(self, now, observed_bindings, profile):
        with self.transaction():
            self._time(now)
            self.verify_chain()
            running = self.db.execute("SELECT * FROM tasks WHERE state='RUNNING'").fetchone()
            if running:
                if running["lease"] <= now:
                    self.db.execute("UPDATE tasks SET state='UNKNOWN' WHERE id=?", (running["id"],))
                    self.db.execute("UPDATE calls SET state='UNKNOWN' WHERE token=?", (running["token"],))
                    self.event("INTERRUPTED_UNKNOWN", {"task_id": running["id"], "token": running["token"]})
                return None
            if self.get_meta("paused") or now < self.get_meta("cooldown"):
                return None
            # An ambiguous external effect blocks the entire shared executor.
            if self.db.execute("SELECT 1 FROM tasks WHERE state='UNKNOWN' LIMIT 1").fetchone():
                return None
            ready = list(self.db.execute("SELECT rowid,* FROM tasks WHERE state='READY' ORDER BY rowid"))
            ready.sort(key=lambda r: -json.loads(r["spec"])["priority"])
            for row in ready:
                spec = json.loads(row["spec"])
                if row["cycle"] not in observed_bindings:
                    continue
                self.restore(row["cycle"], observed_bindings[row["cycle"]], profile)
                if any(self.db.execute("SELECT state FROM tasks WHERE id=?", (dep,)).fetchone()[0] != "SUCCEEDED" for dep in spec["dependencies"]):
                    continue
                if row["attempts"] >= self.limits.max_attempts:
                    continue
                cost = spec["max_cost_micro_usd"]
                if spec["external"]:
                    calls = list(self.db.execute("SELECT * FROM calls"))
                    today = datetime.fromtimestamp(now, timezone.utc).date()
                    day_calls = [c for c in calls if datetime.fromtimestamp(c["started"], timezone.utc).date() == today]
                    amount = lambda c: c["charged"] if c["charged"] is not None else c["reserved"]
                    if sum(amount(c) for c in day_calls) + cost > self.limits.daily_micro_usd:
                        continue
                    if cost:
                        pools = self.get_meta("pools")
                        if pools is None or spec["pool"] not in pools:
                            continue
                        if sum(amount(c) for c in calls if c["pool"] == spec["pool"]) + cost > pools[spec["pool"]]:
                            continue
                    else:
                        free = [c for c in calls if c["reserved"] == 0]
                        if sum(c["started"] > now - 86400 for c in free) >= self.limits.free_daily or sum(c["started"] > now - 3600 for c in free) >= self.limits.free_hourly:
                            continue
                token = uuid4().hex
                self.db.execute("UPDATE tasks SET state='RUNNING',token=?,lease=?,attempts=attempts+1 WHERE id=?", (token, now + self.limits.lease_seconds, row["id"]))
                if spec["external"]:
                    self.db.execute("INSERT INTO calls VALUES (?,?,?,?,?,NULL,'RESERVED')", (token, row["id"], now, spec["pool"], cost))
                claim = {"task_id": row["id"], "cycle_id": row["cycle"], "token": token, "spec": spec}
                self.event("TASK_CLAIMED", claim)
                return claim
            return None

    def finish(self, claim, *, now, status, result, actual_micro_usd=None, retry_after_seconds=None):
        if status not in {"SUCCEEDED", "RATE_LIMITED", "FAILED", "UNKNOWN"}:
            raise SemanticError("invalid task result")
        if actual_micro_usd is not None:
            integer(actual_micro_usd)
        if retry_after_seconds is not None:
            integer(retry_after_seconds)
        encoded(result)
        with self.transaction():
            self._time(now)
            row = self.db.execute("SELECT * FROM tasks WHERE id=?", (claim["task_id"],)).fetchone()
            if not row or row["state"] != "RUNNING" or row["token"] != claim["token"] or row["lease"] <= now:
                raise SemanticError("stale completion token or expired lease")
            spec = json.loads(row["spec"])
            if spec["external"] and (actual_micro_usd is None or actual_micro_usd > spec["max_cost_micro_usd"]):
                status = "UNKNOWN"
            state = status
            if status == "RATE_LIMITED":
                delay = max(retry_after_seconds or 0, self.limits.cooldown_seconds * 2 ** (row["attempts"] - 1))
                self.put_meta("cooldown", max(self.get_meta("cooldown"), now + delay))
                state = "READY" if row["attempts"] < self.limits.max_attempts else "FAILED"
            self.db.execute("UPDATE tasks SET state=?,result=? WHERE id=?", (state, encoded(result), row["id"]))
            self.db.execute("UPDATE calls SET state=?,charged=? WHERE token=?", (status, actual_micro_usd, claim["token"]))
            self.event("TASK_FINISHED", {"task_id": row["id"], "token": claim["token"], "status": status, "state": state, "result": result, "actual_micro_usd": actual_micro_usd})
            return state

    def reconcile(self, task_id, *, resolution, actual_micro_usd, evidence_ref):
        """Trusted operator/provider reconciliation only; never infer non-execution."""
        text(evidence_ref)
        integer(actual_micro_usd)
        if resolution not in {"SUCCEEDED", "FAILED", "NOT_EXECUTED"}:
            raise SemanticError("invalid reconciliation")
        with self.transaction():
            row = self.db.execute("SELECT * FROM tasks WHERE id=?", (task_id,)).fetchone()
            if not row or row["state"] != "UNKNOWN":
                raise SemanticError("only UNKNOWN attempts require reconciliation")
            state = "READY" if resolution == "NOT_EXECUTED" and row["attempts"] < self.limits.max_attempts else ("FAILED" if resolution == "NOT_EXECUTED" else resolution)
            self.db.execute("UPDATE tasks SET state=? WHERE id=?", (state, task_id))
            self.db.execute("UPDATE calls SET charged=?,state=? WHERE token=?", (actual_micro_usd, resolution, row["token"]))
            self.event("RECONCILED", {"task_id": task_id, "resolution": resolution, "actual_micro_usd": actual_micro_usd, "evidence_ref": evidence_ref})


class CompletionWorker:
    def __init__(self, store, handlers: dict[str, Callable], clock: Callable):
        self.store, self.handlers, self.clock = store, handlers, clock

    def run_ready(self, observe_bindings, profile):
        """Continue immediately after success; stop on quota, cooldown or failure.

        observe_bindings refreshes actual repository/source bindings BEFORE each
        item. Handlers are trusted code, return one result and make at most ONE
        provider call. Unknown exceptions preserve reservations and halt.
        """
        completed = []
        for _ in range(self.store.limits.max_steps_per_wake):
            claim = self.store.claim(self.clock(), observe_bindings(), profile)
            if claim is None:
                break
            try:
                response = self.handlers[claim["spec"]["handler"]](claim)
                state = self.store.finish(claim, now=self.clock(), **response)
            except Exception as exc:
                try:
                    self.store.finish(claim, now=self.clock(), status="UNKNOWN", result={"error_type": type(exc).__name__})
                except SemanticError:
                    # Expired lease remains RUNNING and becomes UNKNOWN on observation.
                    pass
                break
            completed.append({"task_id": claim["task_id"], "state": state})
            if state != "SUCCEEDED":
                break
        return completed
