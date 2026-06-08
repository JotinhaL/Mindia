from dataclasses import dataclass
from datetime import datetime


@dataclass
class Answer:
    question_id: int
    content: str
    created_at: datetime

    def __post_init__(self):
        if not self.content.strip():
            raise ValueError("Answer cannot be empty")