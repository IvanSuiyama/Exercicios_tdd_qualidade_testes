"""Exercício 2 - Entidade Person do diagrama de classes."""

from __future__ import annotations

from dataclasses import dataclass, field

from .email import Email


@dataclass
class Person:
    """Pessoa do diagrama: 1 Person possui 1..* Email."""

    id: int | None = None
    name: str = ""
    age: int = 0
    emails: list[Email] = field(default_factory=list)
