from fastapi import APIRouter

from app.api.schemas.assessment import (
    AnswerRequest,
    AnswerResponse,
)

router = APIRouter(
    prefix="/assessment",
    tags=["Assessment"],
)


@router.post(
    "/answer",
    response_model=AnswerResponse,
)
def answer_question(request: AnswerRequest):
    # Aqui normalmente você chamaria o AssessmentService
    # service = AssessmentService()
    # next_question = service.answer_question(request.answer)

    return AnswerResponse(
        next_question="Como você está dormindo ultimamente?",
        finished=False,
    )