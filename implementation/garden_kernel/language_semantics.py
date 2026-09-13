from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

from .core import SemanticError


class LetForm(str, Enum):
    EXPRESSION = "EXPRESSION"
    STATEMENT = "STATEMENT"


@dataclass(frozen=True)
class LetBinding:
    name: str
    bound_expression_ref: str
    form: LetForm
    body_expression_ref: str | None = None
    enclosing_scope_ref: str | None = None

    def __post_init__(self) -> None:
        if not self.name.strip() or not self.bound_expression_ref.strip():
            raise SemanticError("let binding requires name and bound expression")
        if self.form is LetForm.EXPRESSION:
            if not self.body_expression_ref:
                raise SemanticError("LetExpr requires an explicit `in` body expression")
            if self.enclosing_scope_ref is not None:
                raise SemanticError("LetExpr body defines its lexical scope; enclosing statement scope is not used")
        elif self.form is LetForm.STATEMENT:
            if not self.enclosing_scope_ref:
                raise SemanticError("LetStmt requires an enclosing lexical scope")
            if self.body_expression_ref is not None:
                raise SemanticError("LetStmt cannot carry an `in` body")

    @property
    def result_type(self) -> str:
        return "BODY_EXPRESSION_TYPE" if self.form is LetForm.EXPRESSION else "Unit"


class QueryDestinationKind(str, Enum):
    LOCAL_BINDING = "LOCAL_BINDING"
    DECLARED_OUTPUT = "DECLARED_OUTPUT"


@dataclass(frozen=True)
class QueryResultBinding:
    query_ref: str
    destination_kind: QueryDestinationKind
    destination_ref: str
    function_contract_ref: str | None = None
    scope_ref: str | None = None

    def __post_init__(self) -> None:
        if not self.query_ref.strip() or not self.destination_ref.strip():
            raise SemanticError("query result binding requires query and destination")
        if self.destination_kind is QueryDestinationKind.LOCAL_BINDING:
            if not self.scope_ref:
                raise SemanticError("query `into ID` requires an enclosing lexical scope")
        elif self.destination_kind is QueryDestinationKind.DECLARED_OUTPUT:
            if not self.function_contract_ref:
                raise SemanticError(
                    "query without `into` requires a declared FunctionContract output sink"
                )


def bind_query_result(
    *,
    query_ref: str,
    into_id: str | None,
    scope_ref: str | None,
    declared_output_ref: str | None,
    function_contract_ref: str | None,
) -> QueryResultBinding:
    if into_id:
        return QueryResultBinding(
            query_ref=query_ref,
            destination_kind=QueryDestinationKind.LOCAL_BINDING,
            destination_ref=into_id,
            scope_ref=scope_ref,
        )
    if declared_output_ref:
        return QueryResultBinding(
            query_ref=query_ref,
            destination_kind=QueryDestinationKind.DECLARED_OUTPUT,
            destination_ref=declared_output_ref,
            function_contract_ref=function_contract_ref,
        )
    raise SemanticError("QUERY_RESULT_UNCONSUMED")
