from dataclasses import dataclass

from app.domain.answers.answer import Answer


@dataclass(frozen=True)
class Score:
    depression: int
    anxiety: int
    stress: int

    def __post_init__(self):
        if self.depression < 0 or self.anxiety < 0 or self.stress < 0:
            raise ValueError("Scores cannot be negative")

    @classmethod
    def from_answers(cls, answers: list[Answer]) -> "Score":
        depression = 0
        anxiety = 0
        stress = 0

        for answer in answers:
            if answer.question.category == "Depressão":
                depression += answer.value
            elif answer.question.category == "Ansiedade":
                anxiety += answer.value
            elif answer.question.category == "Estresse":
                stress += answer.value

        return cls(
            depression=depression * 2,
            anxiety=anxiety * 2,
            stress=stress * 2,
        )