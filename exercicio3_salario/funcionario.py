"""Exercício 3 - Entidade Funcionario."""

from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

from .cargo import Cargo


def _para_decimal(valor) -> Decimal:
    """Converte int/float/str em ``Decimal`` sem herdar o erro do float."""
    if isinstance(valor, Decimal):
        return valor
    if isinstance(valor, float):
        return Decimal(str(valor))
    return Decimal(valor)


@dataclass
class Funcionario:
    """Funcionário com nome, email, salário-base e cargo."""

    nome: str
    email: str
    salario_base: Decimal
    cargo: Cargo = field(default=Cargo.DESENVOLVEDOR)

    def __post_init__(self) -> None:
        self.salario_base = _para_decimal(self.salario_base)
