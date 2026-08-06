import datetime

from pydantic import BaseModel
from sqlalchemy import UUID

from app.api.schemas.classification import classificationResponse
from app.api.schemas.question import QuestionResponse
from app.domain.enums.department import DepartmentEnum


class StartAssessmentRequest(BaseModel):
    department: DepartmentEnum
class StartAssessmentResponse(BaseModel):
    session_id: UUID
    assessment_id: UUID
    question: QuestionResponse

class AnswerRequest(BaseModel):
    answer: str

class AnswerResponse(BaseModel):
    answer_id: int
    next_question: str | None
    finished: bool
    depression: classificationResponse | None
    anxiety: classificationResponse | None
    stress: classificationResponse | None
    feedback: str | None
    created_at: datetime.datetime

