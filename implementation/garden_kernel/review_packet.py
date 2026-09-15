"""Bounded review-packet checks; completeness is relative to a trusted inventory.

The caller must mechanically derive the closure from the exact source. A supplied
object list or a model assertion cannot establish whole-source completeness.
"""
from __future__ import annotations

import re
from copy import deepcopy
from .core import SemanticError
from .completion_runner import digest, text


def packet(binding, objects, *, expected_objects, exclusions, closure_frontier):
    if not isinstance(objects, dict) or not isinstance(expected_objects, dict) or not expected_objects:
        raise SemanticError("nonempty mechanically derived closure required")
    if not isinstance(exclusions, dict) or set(objects) & set(exclusions):
        raise SemanticError("included/excluded objects overlap")
    if set(objects) | set(exclusions) != set(expected_objects):
        raise SemanticError("missing or extra closure objects")
    for key, value in objects.items():
        text(key)
        if not isinstance(value, str) or digest(value) != expected_objects[key]:
            raise SemanticError("object content differs from source inventory")
    for key, reason in exclusions.items():
        if reason not in {"OUTSIDE_DECLARED_SCOPE", "PRIVATE_NOT_FOR_PROVIDER"}:
            raise SemanticError("unexplained exclusion")
    if closure_frontier or exclusions:
        raise SemanticError("incomplete review packet; exclusions require a separately qualified projection")
    result = {"schema": "GardenReviewPacket/v1", "binding": {**binding.__dict__, "repo_heads": dict(binding.repo_heads)},
              "objects": objects, "closure_inventory_hash": digest(expected_objects),
              "closure_frontier": [], "exclusions": {}, "completeness_scope": "CALLER_DERIVED_INVENTORY"}
    return {**result, "packet_hash": digest(result)}


class ReviewSet:
    """Serializable blind findings, then cross-examination; no admission authority."""
    def __init__(self, review_packet, families, *, builder_family, min_families):
        self.packet = deepcopy(review_packet)
        claimed = review_packet.get("packet_hash")
        if claimed != digest({k: v for k, v in review_packet.items() if k != "packet_hash"}):
            raise SemanticError("invalid packet hash")
        if type(min_families) is not int or min_families < 2 or len(set(families)) < min_families:
            raise SemanticError("independent-family requirement unavailable")
        for family in families:
            text(family)
        self.families = frozenset(families)
        self.builder_family = text(builder_family)
        self.min_families = min_families
        self.blind = {}
        self.cross = {}

    def blind_input(self, family):
        if family not in self.families:
            raise SemanticError("unallocated family")
        # A detached copy prevents one reviewer from changing a peer's packet.
        import json
        return json.loads(json.dumps(self.packet))

    def record_blind(self, family, receipt):
        if family not in self.families or family in self.blind or self.cross:
            raise SemanticError("duplicate, unallocated or late blind review")
        self._bound(family, receipt)
        if receipt.get("phase") != "BLIND" or receipt.get("peer_findings_seen") is not False:
            raise SemanticError("blind-review boundary violated")
        self.blind[family] = deepcopy(receipt)

    def _bound(self, family, receipt):
        if receipt.get("family") != family or receipt.get("packet_hash") != self.packet["packet_hash"] or receipt.get("cycle_id") != self.packet["binding"]["cycle_id"]:
            raise SemanticError("wrong family, packet or cycle")
        if receipt.get("status") != "COMPLETE" or not receipt.get("findings"):
            raise SemanticError("incomplete reviewer output")
        text(receipt.get("provider_response_ref"))

    def cross_input(self):
        if set(self.blind) != set(self.families):
            raise SemanticError("all allocated blind reviews must finish first")
        import json
        return json.loads(json.dumps({"packet": self.packet, "blind": self.blind}))

    def record_cross(self, family, receipt):
        self.cross_input()
        if family not in self.families or family in self.cross:
            raise SemanticError("duplicate or unallocated cross-examiner")
        self._bound(family, receipt)
        if receipt.get("phase") != "CROSS_EXAM" or receipt.get("blind_set_hash") != digest(self.blind):
            raise SemanticError("cross-examination is not bound to complete blind set")
        self.cross[family] = deepcopy(receipt)

    def verified_closure(self, *, candidate_sha, verifier_family, evidence, verify):
        if set(self.cross) != set(self.families):
            raise SemanticError("cross-examination incomplete")
        if verifier_family == self.builder_family or verifier_family not in self.families:
            raise SemanticError("builder cannot independently verify its own fix")
        if not isinstance(candidate_sha, str) or not re.fullmatch("[0-9a-f]{40}", candidate_sha):
            raise SemanticError("exact candidate commit required")
        if evidence.get("candidate_sha") != candidate_sha or evidence.get("packet_hash") != self.packet["packet_hash"] or verify(evidence) is not True:
            raise SemanticError("independent post-fix evidence missing or stale")
        return {"schema": "FindingClosureReceipt/v1", "status": "VERIFIED_FIXED", "candidate_sha": candidate_sha,
                "packet_hash": self.packet["packet_hash"], "verifier_family": verifier_family,
                "evidence_hash": digest(evidence), "authorization_effect": "NONE"}
