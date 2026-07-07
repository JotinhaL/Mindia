from dataclasses import dataclass


@dataclass(frozen=True)
class Question:
    id: int = 0
    content: str = ""
    category: str = ""

