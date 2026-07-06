import datetime
import uuid
from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

from app.domain.assessments.assessment import Assessment


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
    assessment: Optional[Assessment] = None
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

    def finish(self) -> None:
        if self.status != SessionStatus.ACTIVE:
            raise InvalidSessionError("Only active sessions can be finished.")
        self.status = SessionStatus.CLOSED
        self.ended_at = datetime.datetime.now(datetime.timezone.utc)
        self.updated_at = datetime.datetime.now(datetime.timezone.utc)

    def reset(self) -> None:
        self.status = SessionStatus.PENDING
        self.assessment = None
        self.updated_at = datetime.datetime.now(datetime.timezone.utc)

    @property
    def is_active(self) -> bool:
        return self.status == SessionStatus.ACTIVE
    
    
