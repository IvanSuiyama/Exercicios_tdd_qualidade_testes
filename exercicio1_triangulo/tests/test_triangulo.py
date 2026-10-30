"""Casos de teste do Exercício 1 - Triângulo."""

import pytest

from exercicio1_triangulo.triangulo import Triangulo


class TestTrianguloValido:
    """Itens 2.1 a 2.4 do enunciado."""

    def test_escaleno_valido(self):
        """2.1 - Triângulo escaleno válido."""
        assert Triangulo.classificar(3, 4, 5) == Triangulo.ESCALENO

    def test_isosceles_valido(self):
        """2.2 - Triângulo isósceles válido."""
        assert Triangulo.classificar(5, 5, 7) == Triangulo.ISOSCELES

    @pytest.mark.parametrize(
        "lado_a, lado_b, lado_c",
        [
            (3, 3, 4),
            (3, 4, 3),
            (4, 3, 3),
        ],
        ids=["a=b", "a=c", "b=c"],
    )
    def test_isosceles_valido_permutacoes(self, lado_a, lado_b, lado_c):
        """2.4 - Três CTs de isósceles válido com permutação dos valores."""
        assert Triangulo.classificar(lado_a, lado_b, lado_c) == Triangulo.ISOSCELES

    def test_equilatero_valido(self):
        """2.3 - Triângulo equilátero válido."""
        assert Triangulo.classificar(6, 6, 6) == Triangulo.EQUILATERO


class TestTrianguloInvalido:
    """Itens 2.5 a 2.11 do enunciado."""

    @pytest.mark.parametrize(
        "lado_a, lado_b, lado_c",
        [
            (0, 4, 5),
            (4, 0, 5),
            (4, 5, 0),
        ],
        ids=["a=0", "b=0", "c=0"],
    )
    def test_um_valor_zero(self, lado_a, lado_b, lado_c):
        """2.5 - Um valor zero."""
        with pytest.raises(ValueError, match="maior que zero"):
            Triangulo.classificar(lado_a, lado_b, lado_c)

    @pytest.mark.parametrize(
        "lado_a, lado_b, lado_c",
        [
            (-1, 4, 5),
            (4, -1, 5),
            (4, 5, -1),
        ],
        ids=["a<0", "b<0", "c<0"],
    )
    def test_um_valor_negativo(self, lado_a, lado_b, lado_c):
        """2.6 - Um valor negativo."""
        with pytest.raises(ValueError, match="maior que zero"):
            Triangulo.classificar(lado_a, lado_b, lado_c)

    @pytest.mark.parametrize(
        "lado_a, lado_b, lado_c",
        [
            (1, 2, 3),
            (1, 3, 2),
            (2, 1, 3),
            (2, 3, 1),
            (3, 1, 2),
            (3, 2, 1),
        ],
        ids=["abc", "acb", "bac", "bca", "cab", "cba"],
    )
    def test_soma_igual_ao_terceiro_lado(self, lado_a, lado_b, lado_c):
        """2.7 e 2.8 - Soma de dois lados igual ao terceiro, em todas as permutações."""
        with pytest.raises(ValueError, match="não formam um triângulo"):
            Triangulo.classificar(lado_a, lado_b, lado_c)

    @pytest.mark.parametrize(
        "lado_a, lado_b, lado_c",
        [
            (1, 2, 4),
            (1, 4, 2),
            (2, 1, 4),
            (2, 4, 1),
            (4, 1, 2),
            (4, 2, 1),
        ],
        ids=["abc", "acb", "bac", "bca", "cab", "cba"],
    )
    def test_soma_menor_que_o_terceiro_lado(self, lado_a, lado_b, lado_c):
        """2.9 e 2.10 - Soma de dois lados menor que o terceiro, em todas as permutações."""
        with pytest.raises(ValueError, match="não formam um triângulo"):
            Triangulo.classificar(lado_a, lado_b, lado_c)

    def test_tres_valores_iguais_a_zero(self):
        """2.11 - Os três valores iguais a zero."""
        with pytest.raises(ValueError, match="maior que zero"):
            Triangulo.classificar(0, 0, 0)


class TestTrianguloTipoInvalido:
    """Entrada que não seja número inteiro."""

    @pytest.mark.parametrize(
        "lado_invalido",
        ["3", 3.5, None, True],
        ids=["string", "float", "none", "bool"],
    )
    def test_lado_nao_inteiro(self, lado_invalido):
        with pytest.raises(TypeError, match="número inteiro"):
            Triangulo.classificar(3, 4, lado_invalido)
