from dataclasses import dataclass


@dataclass(frozen=True)
class Question:
    id: int
    texto: str
    categoria: str

