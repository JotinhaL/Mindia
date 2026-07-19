from pydantic import BaseModel
from app.domain.enums.department import DepartmentEnum
from app.api.schemas.question import QuestionResponse
from app.api.schemas.classification import classificationResponse
import datetime


class StartAssessmentRequest(BaseModel):
    department: DepartmentEnum
class StartAssessmentResponse(BaseModel):
    assessment_id: str
    question: QuestionResponse

class AnswerRequest(BaseModel):
    answer: str

class AnswerResponse(BaseModel):
    id: int
    next_question: str | None
    finished: bool
    depression: classificationResponse
    anxiety: classificationResponse
    stress: classificationResponse
    feedback: str
    created_at: datetime.datetime

