from __future__ import annotations

import hashlib
import json
from pathlib import Path
import unittest

from garden_kernel.evolution_epoch import (
    EvolutionArtifactBinding,
    EvolutionArtifactKind,
    validate_evolution_binding,
)

ROOT = Path(__file__).resolve().parents[2]
VECTOR_PATH = ROOT / "gsl" / "SHARED_CONFORMANCE_VECTORS.json"


def _canonical_hash(value) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    ).hexdigest()


class SharedConformanceVectorTests(unittest.TestCase):
    def test_private_kernel_matches_shared_design_epoch_vectors(self):
        payload = json.loads(VECTOR_PATH.read_text(encoding="utf-8"))
        vectors = payload["vectors"]
        self.assertEqual(_canonical_hash(vectors), payload["vector_set_sha256"])
        self.assertFalse(payload["semantic_compliance_proved"])
        self.assertEqual(payload["implementations"]["scep"], "FRONTIER")

        for row in vectors:
            with self.subTest(vector=row["vector_id"]):
                i = row["input"]
                expected = row["expected"]
                required = i.get("required_dependencies")
                result = validate_evolution_binding(
                    EvolutionArtifactBinding(
                        artifact_id=row["vector_id"],
                        kind=EvolutionArtifactKind.FINDING,
                        design_epoch=i["binding_epoch"],
                        dependencies=i["bound_dependencies"],
                        required_dependencies=None if required is None else frozenset(required),
                    ),
                    current_design_epoch=i["current_epoch"],
                    current_dependencies=i["current_dependencies"],
                )
                self.assertEqual(result.status.value, expected["status"])
                for prefix in expected["reason_prefixes"]:
                    self.assertTrue(any(reason.startswith(prefix) for reason in result.reasons))


if __name__ == "__main__":
    unittest.main()
