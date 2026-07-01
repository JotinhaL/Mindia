from dataclasses import dataclass
from app.domain.assesments.score import Score
from app.domain.assesments.classification import Classification

@dataclass
class Assessment:
    id: int
    field_of_work: str
    answers: list
    score: Score
    classification: Classification