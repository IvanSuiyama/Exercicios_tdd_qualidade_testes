"""Exercício 3 - Cálculo do salário líquido por cargo."""

from __future__ import annotations

from decimal import ROUND_HALF_UP, Decimal

from .cargo import Cargo
from .funcionario import Funcionario

_CENTAVOS = Decimal("0.01")


class CalculadoraSalario:
    """Aplica o desconto do cargo sobre o salário-base do funcionário."""

    # Cargo -> (piso salarial, desconto a partir do piso, desconto abaixo dele)
    _REGRAS: dict[Cargo, tuple[Decimal, Decimal, Decimal]] = {
        Cargo.DESENVOLVEDOR: (
            Decimal("3000.00"),
            Decimal("0.20"),
            Decimal("0.10"),
        ),
        Cargo.DBA: (
            Decimal("2000.00"),
            Decimal("0.25"),
            Decimal("0.15"),
        ),
        Cargo.TESTADOR: (
            Decimal("2000.00"),
            Decimal("0.25"),
            Decimal("0.15"),
        ),
        Cargo.GERENTE: (
            Decimal("5000.00"),
            Decimal("0.30"),
            Decimal("0.20"),
        ),
    }

    def calcular_salario_liquido(self, funcionario: Funcionario) -> Decimal:
        """Retorna o salário-base menos o desconto do cargo (2 casas).

        Raises:
            TypeError: se ``funcionario`` não for um ``Funcionario``.
            ValueError: se o salário-base for negativo ou se o cargo não
                possuir regra cadastrada.
        """
        if not isinstance(funcionario, Funcionario):
            raise TypeError("O parâmetro deve ser um Funcionario.")

        salario_base = funcionario.salario_base
        if salario_base < 0:
            raise ValueError("O salário-base não pode ser negativo.")

        desconto = self._obter_desconto(funcionario.cargo, salario_base)
        salario_liquido = salario_base * (Decimal("1") - desconto)
        return salario_liquido.quantize(_CENTAVOS, rounding=ROUND_HALF_UP)

    def _obter_desconto(self, cargo: Cargo, salario_base: Decimal) -> Decimal:
        try:
            piso, desconto_acima, desconto_abaixo = self._REGRAS[cargo]
        except (KeyError, TypeError) as erro:
            raise ValueError(f"Cargo sem regra de desconto: {cargo!r}") from erro

        return desconto_acima if salario_base >= piso else desconto_abaixo
