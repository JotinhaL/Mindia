# *TODO MODELS E REPOSITORiES

from datetime import datetime
from uuid import uuid4

from sqlalchemy import DateTime, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.database.config import Base


class AssessmentModel(Base):
    __tablename__ = "assessments"

    id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid4,
    )

    actual_question_index: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=0,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        default=datetime.utcnow,
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
    )