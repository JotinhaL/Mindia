from uuid import uuid4

from fastapi import APIRouter

from app.api.schemas.assessment import (
    AnswerRequest,
    AnswerResponse,
    StartAssessmentRequest,
    StartAssessmentResponse,
)
from app.services.assessments.assessment_service import AssessmentService

router = APIRouter(
    prefix="/assessment",
    tags=["Assessment"],
)

#*TODO integrar o banco de dados
@router.post(
    "/{session_id}/answer",
    response_model=AnswerResponse,
    status_code=201
)


def answer_question(session_id: uuid4, request: AnswerRequest):
    session_uuid = session_id
