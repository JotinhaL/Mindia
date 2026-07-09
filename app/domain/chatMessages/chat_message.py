import datetime
from dataclasses import dataclass , field
from enum import Enum



class Role(Enum):
    USER = "user"
    ASSISTANT = "assistant"
    SYSTEM = "system"

@dataclass(frozen=True)
class ChatMessage:
    role: Role 
    content: str
    created_at: datetime.datetime = field(default_factory=lambda: datetime.datetime.now(datetime.timezone.utc))

    @classmethod
    def assistant(cls, content: str):
        return cls(Role.ASSISTANT, content)

    @classmethod
    def user(cls, content: str):
        return cls(Role.USER, content)