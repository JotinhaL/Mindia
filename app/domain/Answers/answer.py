from dataclasses import dataclass
from datetime import datetime


@dataclass
class Answer:
    question_id: int
    content: str
    created_at: datetime

    def __post_init__(self):
        if self.question_id <= 0:
            raise ValueError("Invalid question id")

        if not self.content.strip():
            raise ValueError("Answer cannot be empty")