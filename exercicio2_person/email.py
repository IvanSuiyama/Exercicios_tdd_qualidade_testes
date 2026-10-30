"""Exercício 2 - Entidade Email do diagrama de classes."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Email:
    """Representa um e-mail associado a uma ``Person``."""

    id: int | None = None
    name: str = ""
