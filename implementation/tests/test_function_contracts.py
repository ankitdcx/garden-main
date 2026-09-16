from __future__ import annotations

from pathlib import Path
import tempfile
import unittest

from garden_kernel.function_contracts import (
    FunctionContractBinding,
    FunctionContractRegistry,
    enumerate_scoped_public_functions,
)


class PublicMethodEnumerationTests(unittest.TestCase):
    def test_declared_and_frontier_public_methods_are_visible_but_private_nested_are_excluded(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "sample.py").write_text(
                """
class Visible:
    def declared(self, value: int) -> int:
        return value
    def unbound(self) -> None:
        return None
    def _private_method(self) -> None:
        return None

class _PrivateClass:
    def visible_name_but_private_class(self) -> None:
        return None

def outer() -> None:
    def nested() -> None:
        return None
    return None
""",
                encoding="utf-8",
            )
            binding = FunctionContractBinding(
                contract_id="FC-DECLARED-METHOD-v1",
                path="sample.py",
                function="Visible.declared",
                affects=("TEST",),
                input_semantics="Integer fixture input.",
                output_semantics="Returns fixture input.",
                error_semantics="No fixture error path.",
                unknown_semantics="No authority or unknown resolution is implied.",
                effect_semantics="No external effect.",
                proof_obligations=("fixture-method-visible",),
                test_refs=("sample.py",),
            )
            registry = FunctionContractRegistry(
                registry_id="TEST-METHOD-ENUMERATION",
                design_epoch="v15.5",
                canonical_source_root_sha256="a" * 64,
                scope_globs=("sample.py",),
                contracts=(binding,),
            )
            records = {record.identity: record for record in enumerate_scoped_public_functions(root, registry)}

        self.assertEqual(records["sample.py::Visible.declared"].coverage_state, "DECLARED_REFERENCE")
        self.assertEqual(records["sample.py::Visible.unbound"].coverage_state, "FRONTIER")
        self.assertEqual(records["sample.py::outer"].coverage_state, "FRONTIER")
        self.assertNotIn("sample.py::Visible._private_method", records)
        self.assertNotIn("sample.py::_PrivateClass.visible_name_but_private_class", records)
        self.assertNotIn("sample.py::outer.nested", records)


if __name__ == "__main__":
    unittest.main()
