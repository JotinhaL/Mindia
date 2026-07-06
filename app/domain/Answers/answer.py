from dataclasses import dataclass
from datetime import datetime

from app.domain.questions.question import Question


@dataclass
class Answer:
    id: int
    question: Question
    content: str
    created_at: datetime
    value: int = 0

    def __post_init__(self):
        if self.id <= 0:
            raise ValueError("Invalid answer id")

        if not self.content.strip():
            raise ValueError("Answer cannot be empty")

        if self.value not in (0, 1, 2, 3):
            raise ValueError("Answer value must be between 0 and 3")