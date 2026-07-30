from uuid import uuid4

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.schemas.assessment import (
    AnswerRequest,
    AnswerResponse,
    StartAssessmentRequest,
    StartAssessmentResponse,
)
from app.database.config.config import get_db
from app.repositories.assessment import AssessmentRepository
from app.services.ai.ollama_service import OllamaService
from app.services.assessments.assessment_service import AssessmentService

router = APIRouter(
    prefix="/assessment",
    tags=["Assessment"],
)

#*TODO integrar o banco de dados
@router.post("/{session_id}/answer", response_model=AnswerResponse)
def answer_question(
    assessment_id: uuid4,
    request: AnswerRequest,
    db: Session = Depends(get_db)
):
    repository = AssessmentRepository(db)

    assessment = repository.get_by_id(assessment_id)

    service = AssessmentService(
        assessment=assessment,
        ollama_service=OllamaService()
    )

    service.answer_question(request.answer)

    repository.save(assessment)


def answer_question(session_id: uuid4, request: AnswerRequest):
    session_uuid = session_id
