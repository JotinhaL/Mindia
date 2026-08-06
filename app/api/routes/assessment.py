import datetime
from uuid import UUID, uuid4

from fastapi import APIRouter, Depends, HTTPException
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

@router.post("/{session_id}/answer", response_model=AnswerResponse)
def answer_question(
    assessment_id: UUID,
    request: AnswerRequest,
    db: Session = Depends(get_db)
):
    assessment_repository = AssessmentRepository(db)
    assessment = assessment_repository.get_by_id(assessment_id)

    if not assessment:
        raise HTTPException(
            status_code=404,
            detail="Assessment not found"
        )

    service = AssessmentService(
        assessment=assessment,
        ollama_service=OllamaService()
    )



    response = service.answer_question(request.answer)
    assessment_repository.save(assessment)

    return response

