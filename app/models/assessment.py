# *TODO MODELS E REPOSITORiES
from dataclasses import field
from datetime import datetime
from uuid import uuid4

from sqlalchemy import DateTime, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql.sqltypes import String

from app.database.config import Base


class AssessmentModel(Base):
    __tablename__ = "assessments"

    id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid4
    )

    session_id: Mapped[UUID | None] = mapped_column(
        UUID(as_uuid=True),
        nullable=True,
    )

    actual_question_index: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=0
    )

    status: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
        default="PENDING"
    )

    depression_score: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True
    )
    anxiety_score: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True
    )
    stress_score: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True
    )

    depression_classification: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True
    )
    anxiety_classification: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True
    )
    stress_classification: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        default=datetime.utcnow
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        default= field(default_factory=lambda: datetime.datetime.now(datetime.timezone.utc)),
        onupdate=field(default_factory=lambda: datetime.datetime.now(datetime.timezone.utc)),
    )