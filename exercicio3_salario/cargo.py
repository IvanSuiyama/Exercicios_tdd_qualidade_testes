"""Exercício 3 - Cargos de funcionário."""

from enum import Enum


class Cargo(Enum):
    """Cargos previstos na regra de cálculo do salário líquido."""

    DESENVOLVEDOR = "DESENVOLVEDOR"
    DBA = "DBA"
    TESTADOR = "TESTADOR"
    GERENTE = "GERENTE"
