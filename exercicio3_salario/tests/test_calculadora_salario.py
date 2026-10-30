"""Casos de teste do Exercício 3 - Calculadora de salário."""

from decimal import Decimal

import pytest

from exercicio3_salario.calculadora_salario import CalculadoraSalario
from exercicio3_salario.cargo import Cargo
from exercicio3_salario.funcionario import Funcionario


def criar_funcionario(salario_base, cargo: Cargo = Cargo.DESENVOLVEDOR) -> Funcionario:
    return Funcionario(
        nome="Ivan Suiyama",
        email="ivan@fatec.br",
        salario_base=salario_base,
        cargo=cargo,
    )


@pytest.fixture
def calculadora() -> CalculadoraSalario:
    return CalculadoraSalario()


class TestDesenvolvedor:
    """DESENVOLVEDOR: 20% a partir de 3.000,00; 10% abaixo."""

    @pytest.mark.parametrize(
        "salario_base, esperado",
        [
            ("3000.00", "2400.00"),  # limite inferior da faixa de 20%
            ("5000.00", "4000.00"),
            ("2999.99", "2699.99"),  # um centavo abaixo do limite
            ("1000.00", "900.00"),
            ("0.00", "0.00"),
        ],
    )
    def test_calcula_salario_liquido(self, calculadora, salario_base, esperado):
        funcionario = criar_funcionario(salario_base, Cargo.DESENVOLVEDOR)
        assert calculadora.calcular_salario_liquido(funcionario) == Decimal(esperado)


class TestDba:
    """DBA: 25% a partir de 2.000,00; 15% abaixo."""

    @pytest.mark.parametrize(
        "salario_base, esperado",
        [
            ("2000.00", "1500.00"),
            ("4000.00", "3000.00"),
            ("1999.99", "1699.99"),
            ("1000.00", "850.00"),
        ],
    )
    def test_calcula_salario_liquido(self, calculadora, salario_base, esperado):
        funcionario = criar_funcionario(salario_base, Cargo.DBA)
        assert calculadora.calcular_salario_liquido(funcionario) == Decimal(esperado)


class TestTestador:
    """TESTADOR: 25% a partir de 2.000,00; 15% abaixo."""

    @pytest.mark.parametrize(
        "salario_base, esperado",
        [
            ("2000.00", "1500.00"),
            ("2500.00", "1875.00"),
            ("1999.99", "1699.99"),
            ("1000.00", "850.00"),
        ],
    )
    def test_calcula_salario_liquido(self, calculadora, salario_base, esperado):
        funcionario = criar_funcionario(salario_base, Cargo.TESTADOR)
        assert calculadora.calcular_salario_liquido(funcionario) == Decimal(esperado)


class TestGerente:
    """GERENTE: 30% a partir de 5.000,00; 20% abaixo."""

    @pytest.mark.parametrize(
        "salario_base, esperado",
        [
            ("5000.00", "3500.00"),
            ("8000.00", "5600.00"),
            ("4999.99", "3999.99"),
            ("1000.00", "800.00"),
        ],
    )
    def test_calcula_salario_liquido(self, calculadora, salario_base, esperado):
        funcionario = criar_funcionario(salario_base, Cargo.GERENTE)
        assert calculadora.calcular_salario_liquido(funcionario) == Decimal(esperado)


class TestConversaoENormalizacao:
    def test_aceita_float_como_salario_base(self, calculadora):
        funcionario = criar_funcionario(3000.0)
        assert calculadora.calcular_salario_liquido(funcionario) == Decimal("2400.00")

    def test_aceita_decimal_como_salario_base(self, calculadora):
        funcionario = criar_funcionario(Decimal("3000.00"))
        assert calculadora.calcular_salario_liquido(funcionario) == Decimal("2400.00")

    def test_resultado_arredondado_em_duas_casas(self, calculadora):
        # 1234.567 * 0,90 = 1111,1103 -> 1111,11
        funcionario = criar_funcionario("1234.567")
        assert calculadora.calcular_salario_liquido(funcionario) == Decimal("1111.11")

    def test_arredondamento_half_up(self, calculadora):
        # 1000.05 * 0,90 = 900,045 -> 900,05 (half-up; half-even daria 900,04)
        funcionario = criar_funcionario("1000.05")
        assert calculadora.calcular_salario_liquido(funcionario) == Decimal("900.05")


class TestEntradasInvalidas:
    def test_salario_base_negativo(self, calculadora):
        funcionario = criar_funcionario("-1.00")
        with pytest.raises(ValueError, match="não pode ser negativo"):
            calculadora.calcular_salario_liquido(funcionario)

    def test_cargo_sem_regra(self, calculadora):
        funcionario = criar_funcionario("3000.00")
        funcionario.cargo = "DESENVOLVEDOR"  # string em vez do enum
        with pytest.raises(ValueError, match="Cargo sem regra de desconto"):
            calculadora.calcular_salario_liquido(funcionario)

    def test_cargo_nao_hasheavel(self, calculadora):
        funcionario = criar_funcionario("3000.00")
        funcionario.cargo = ["DESENVOLVEDOR"]
        with pytest.raises(ValueError, match="Cargo sem regra de desconto"):
            calculadora.calcular_salario_liquido(funcionario)

    def test_parametro_que_nao_e_funcionario(self, calculadora):
        with pytest.raises(TypeError, match="deve ser um Funcionario"):
            calculadora.calcular_salario_liquido({"salario_base": 3000})
