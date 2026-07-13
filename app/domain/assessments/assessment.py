import datetime
import uuid
from dataclasses import dataclass, field
from typing import List, Optional

from app.domain.answers.answer import Answer
from app.domain.assessments.classification import Classification
from app.domain.assessments.score import Score
from app.domain.questions.dass_21_questions import DASS21_QUESTIONS
from app.domain.questions.question import Question

class InvalidSessionError(Exception):
    pass

class SessionNotFoundError(Exception):
    pass

@dataclass
class Assessment:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    actual_question_index: int = 0
    answers: List[Answer] = field(default_factory=list)
    questions: List[Question] = field(default_factory=list)
    classification: Optional[Classification] = None
    score: Optional[Score] = None
    created_at: datetime.datetime = field(default_factory=lambda: datetime.datetime.now(datetime.timezone.utc))
    updated_at: datetime.datetime = field(default_factory=lambda: datetime.datetime.now(datetime.timezone.utc))

    def __post_init__(self) -> None:
        if not self.questions:
            self.questions = list(DASS21_QUESTIONS)

    def restart(self) -> None:
        self.actual_question_index = 0
        self.answers = []
        self.score = None
        self.classification = None
        self.updated_at = datetime.datetime.now(datetime.timezone.utc)

    def finish(self) -> Score | None:
        if not self.answers:
            raise InvalidSessionError("Cannot finish assessment with no answers.")
        self.score = Score.from_answers(self.answers)
        #atencao a essa classificacao abaixo, ta dando tudo normal verificar
        self.classification = Classification.classify_score(
            self.score.depression,
            self.score.anxiety,
            self.score.stress,
        )
        self.updated_at = datetime.datetime.now(datetime.timezone.utc)
        return self.score

    def current_question(self) -> Optional[Question]:
        if self.actual_question_index < len(self.questions):
            return self.questions[self.actual_question_index]
        return None
    
    def send_question(self):
        return self.current_question()

    def next_question(self):
        self.actual_question_index += 1
    
    
    def answer_current_question(self, answer: Answer):
        if self.actual_question_index >= len(self.questions):
            raise InvalidSessionError("No more questions to answer.")
        
        self.answers.append(answer)
        self.updated_at = datetime.datetime.now(datetime.timezone.utc)


    @property
    def is_completed(self) -> bool:
        return self.actual_question_index >= len(self.questions)


