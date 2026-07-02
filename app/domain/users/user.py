from dataclasses import dataclass, field
from datetime import datetime, timezone
from uuid import UUID, uuid4
from zoneinfo import ZoneInfo


@dataclass
class User:
    name: str
    email: str
    field_of_work: str
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    active: bool = True
    last_evaluation_at: datetime | None = None
    id: UUID = field(default_factory=uuid4)


    def deactivate(self):
        if not self.active:
            raise Exception("User is already deactivated")

        self.active = False

    def activate(self):
        if self.active:
            raise Exception("User is already active")

        self.active = True

    def update_email(self, new_email: str):
        if "@" not in new_email:
            raise ValueError("Invalid email")

        self.email = new_email

    def update_field_of_work(self, new_field_of_work: str):
        if not new_field_of_work:
            raise ValueError("Field of work cannot be empty")

        self.field_of_work = new_field_of_work

    def record_evaluation(self):
        self.last_evaluation_at = datetime.now(ZoneInfo("America/Sao_Paulo"))


    