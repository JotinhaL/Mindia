import datetime
from dataclasses import dataclass, field

from app.domain.questions.question import Question


@dataclass
class Answer:
    id: int = 0
    question: Question | None = None
    content: str = ""
    value: int = 0
    created_at: datetime.datetime = field(default_factory=lambda: datetime.datetime.now(datetime.timezone.utc))

    def __post_init__(self):
        if self.id < 0:
            raise ValueError("Invalid answer id")

        if not self.content.strip():
            raise ValueError("Answer cannot be empty")

        if self.value is not None and self.value not in (0, 1, 2, 3):
            raise ValueError("Answer value must be between 0 and 3")
        
