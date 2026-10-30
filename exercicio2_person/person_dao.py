"""Exercício 2 - PersonDAO com a validação ``isValidToInclude()``."""

from __future__ import annotations

import re

from .person import Person

# Formato exigido: _____@____._____ (cada parte com ao menos 1 caractere).
# Não são permitidos espaços nem um segundo "@".
_PADRAO_EMAIL = re.compile(r"[^@\s]+@[^@\s]+\.[^@\s]+")

IDADE_MINIMA = 1
IDADE_MAXIMA = 200


class PersonDAO:
    """Persistência em memória de ``Person`` com validação de inclusão."""

    def __init__(self) -> None:
        self._pessoas: dict[int | None, Person] = {}

    def save(self, p: Person) -> None:
        """Salva a pessoa, recusando objetos inválidos.

        Raises:
            ValueError: com a lista de erros encontrada por
                :meth:`is_valid_to_include`.
        """
        erros = self.is_valid_to_include(p)
        if erros:
            raise ValueError("Pessoa inválida: " + " ".join(erros))
        self._pessoas[p.id] = p

    def is_valid_to_include(self, p: Person) -> list[str]:
        """Retorna a lista de erros de validação de ``p`` (vazia se válida)."""
        erros: list[str] = []
        erros.extend(self._validar_nome(p.name))
        erros.extend(self._validar_idade(p.age))
        erros.extend(self._validar_emails(p.emails))
        return erros

    @staticmethod
    def _validar_nome(nome: str) -> list[str]:
        erros: list[str] = []
        partes = (nome or "").split()

        if len(partes) < 2:
            erros.append("O nome deve ser composto por ao menos 2 partes.")

        if not partes or not all(parte.isalpha() for parte in partes):
            erros.append("O nome deve ser composto apenas por letras.")

        return erros

    @staticmethod
    def _validar_idade(idade: int) -> list[str]:
        if isinstance(idade, bool) or not isinstance(idade, int):
            return ["A idade deve ser um número inteiro."]
        if not IDADE_MINIMA <= idade <= IDADE_MAXIMA:
            return [
                f"A idade deve estar entre {IDADE_MINIMA} e {IDADE_MAXIMA}."
            ]
        return []

    @staticmethod
    def _validar_emails(emails: list) -> list[str]:
        if not emails:
            return ["O objeto Person deve ter pelo menos um Email associado."]

        erros: list[str] = []
        for email in emails:
            if not _PADRAO_EMAIL.fullmatch(email.name or ""):
                erros.append(
                    f"O nome do Email '{email.name}' deve estar no formato "
                    "'_____@____._____'."
                )
        return erros
