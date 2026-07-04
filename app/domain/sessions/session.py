import datetime
import uuid
from app.domain.assesments.classification import Classification
from app.domain.assesments.score import Score
from app.domain.questions.dass_21_questions import DASS21_QUESTIONS
from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
from app.domain.answers.answer import Answer
from app.domain.questions.question import Question


class SessionStatus(Enum):
    PENDING = "pending"
    ACTIVE = "active"
    CLOSED = "closed"


class SessionError(Exception):
    pass


class SessionNotFoundError(SessionError):
    pass


class InvalidSessionError(SessionError):
    pass


@dataclass
class SessaoDASS21:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    status: SessionStatus = SessionStatus.PENDING
    actual_question_index: int = 0
    answers: List[Answer] = field(default_factory=list)
    questions: List[Question] = field(default_factory=list)
    classification: Classification | None = None
    score: Score | None = None
    started_at: Optional[datetime.datetime] = None
    ended_at: Optional[datetime.datetime] = None
    created_at: datetime.datetime = field(default_factory=datetime.datetime.now(datetime.timezone.utc))
    updated_at: datetime.datetime = field(default_factory=datetime.datetime.now(datetime.timezone.utc))

    def start(self) -> None:
        if self.status != SessionStatus.PENDING:
            raise InvalidSessionError("Only pending sessions can be started.")
        self.status = SessionStatus.ACTIVE
        self.started_at = datetime.datetime.now(datetime.timezone.utc)
        self.updated_at = datetime.datetime.now(datetime.timezone.utc)
        self.questions = DASS21_QUESTIONS

    def finish(self) -> None:
        if self.status != SessionStatus.ACTIVE:
            raise InvalidSessionError("Only active sessions can be finished.")
        self.status = SessionStatus.CLOSED
        self.ended_at = datetime.datetime.now(datetime.timezone.utc)
        self.updated_at = datetime.datetime.now(datetime.timezone.utc)

    def reset(self) -> None:
        self.status = SessionStatus.PENDING
        self.actual_question_index = 0
        self.answers = []
        self.updated_at = datetime.datetime.now(datetime.timezone.utc)

    def next_question(self) -> None:
        self.actual_question_index += 1

    def answer_current_question(self, content: str) -> None:
        if self.status != SessionStatus.ACTIVE:
            raise InvalidSessionError("Only active sessions can be answered.")
        if self.actual_question_index >= len(self.questions):
            raise InvalidSessionError("No more questions to answer.")
        
        answer = Answer(
            id=self.questions[self.actual_question_index].id,
            content=content,
            question=self.questions[self.actual_question_index],
            created_at=datetime.datetime.now(datetime.timezone.utc)
        )
        self.answers.append(answer)
        self.next_question()
        self.updated_at = datetime.datetime.now(datetime.timezone.utc)

    def is_active(self) -> bool:
        return self.status == SessionStatus.ACTIVE
    
    
