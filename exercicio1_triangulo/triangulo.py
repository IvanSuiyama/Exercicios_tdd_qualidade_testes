"""Exercício 1 - Classificação de triângulos.

Regra de existência: três valores inteiros formam um triângulo quando a soma
de dois lados quaisquer é maior que o terceiro lado.
"""

from __future__ import annotations


class Triangulo:
    """Classifica três lados inteiros em equilátero, isósceles ou escaleno."""

    EQUILATERO = "EQUILATERO"
    ISOSCELES = "ISOSCELES"
    ESCALENO = "ESCALENO"

    @classmethod
    def classificar(cls, lado_a: int, lado_b: int, lado_c: int) -> str:
        """Retorna o tipo do triângulo formado pelos lados informados.

        Raises:
            TypeError: se algum lado não for um número inteiro.
            ValueError: se algum lado for menor ou igual a zero ou se os
                lados não satisfizerem a desigualdade triangular.
        """
        cls._validar_inteiros(lado_a, lado_b, lado_c)
        cls._validar_positivos(lado_a, lado_b, lado_c)
        cls._validar_desigualdade_triangular(lado_a, lado_b, lado_c)

        lados_distintos = len({lado_a, lado_b, lado_c})
        if lados_distintos == 1:
            return cls.EQUILATERO
        if lados_distintos == 2:
            return cls.ISOSCELES
        return cls.ESCALENO

    @staticmethod
    def _validar_inteiros(*lados: int) -> None:
        for lado in lados:
            if isinstance(lado, bool) or not isinstance(lado, int):
                raise TypeError(f"O lado {lado!r} deve ser um número inteiro.")

    @staticmethod
    def _validar_positivos(*lados: int) -> None:
        for lado in lados:
            if lado <= 0:
                raise ValueError(f"O lado {lado} deve ser maior que zero.")

    @staticmethod
    def _validar_desigualdade_triangular(a: int, b: int, c: int) -> None:
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError(
                f"Os lados ({a}, {b}, {c}) não formam um triângulo: "
                "a soma de dois lados deve ser maior que o terceiro."
            )
