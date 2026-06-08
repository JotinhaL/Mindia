import datetime
import uuid
from domain.questions.questions import DASS21_QUESTIONS
from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional, Protocol


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
    answers: List[int] = field(default_factory=list)
    questions: List = field(default_factory=list)
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

    def close(self) -> None:
        if self.status != SessionStatus.ACTIVE:
            raise InvalidSessionError("Only active sessions can be closed.")
        self.status = SessionStatus.CLOSED
        self.ended_at = datetime.datetime.now(datetime.timezone.utc)
        self.updated_at = datetime.datetime.now(datetime.timezone.utc)

    def reset(self) -> None:
        self.status = SessionStatus.PENDING
        self.actual_question_index = 0
        self.answers = []
        self.updated_at = datetime.datetime.now(datetime.timezone.utc)

    def answer_current_question(self, answer: int) -> None:
        if self.status != SessionStatus.ACTIVE:
            raise InvalidSessionError("Only active sessions can be answered.")
        if self.actual_question_index >= len(self.questions):
            raise InvalidSessionError("No more questions to answer.")
        self.answers.append(answer)
        self.actual_question_index += 1
        self.updated_at = datetime.datetime.now(datetime.timezone.utc)


