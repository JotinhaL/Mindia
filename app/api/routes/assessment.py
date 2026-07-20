from fastapi import APIRouter
from app.services.assessments.assessment_service import AssessmentService
from uuid import uuid4

from app.api.schemas.assessment import (
    AnswerRequest,
    AnswerResponse,
    StartAssessmentRequest,
    StartAssessmentResponse
)

router = APIRouter(
    prefix="/assessment",
    tags=["Assessment"],
)

#*TODO integrar o banco de dados
@router.post(
    "/{session_id}/answer",
    response_model=AnswerResponse,
)


def answer_question(session_id: uuid4, request: AnswerRequest):
    session_uuid = session_id
