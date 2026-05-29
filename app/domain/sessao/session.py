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


class SessionRepository(Protocol):
    def save(self, session: SessaoDASS21) -> SessaoDASS21:
        ...

    def find_by_id(self, session_id: str) -> Optional[SessaoDASS21]:
        ...

    def list_all(self) -> List[SessaoDASS21]:
        ...

    def delete(self, session_id: str) -> None:
        ...


class SessionService:
    def __init__(self, repository: SessionRepository):
        self._repository = repository

    def create_session(self, questions: List) -> SessaoDASS21:
        session = SessaoDASS21(questions=questions)
        return self._repository.save(session)

    def get_session(self, session_id: str) -> SessaoDASS21:
        session = self._repository.find_by_id(session_id)
        if session is None:
            raise SessionNotFoundError(f"Session with id '{session_id}' not found.")
        return session

    def start_session(self, session_id: str) -> SessaoDASS21:
        session = self.get_session(session_id)
        session.start()
        return self._repository.save(session)

    def close_session(self, session_id: str) -> SessaoDASS21:
        session = self.get_session(session_id)
        session.close()
        return self._repository.save(session)

    def add_response(self, session_id: str, response: int) -> SessaoDASS21:
        session = self.get_session(session_id)
        session.answers.append(response)
        return self._repository.save(session)

    def list_sessions(self) -> List[SessaoDASS21]:
        return self._repository.list_all()
