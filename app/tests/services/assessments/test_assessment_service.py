import pytest
from app.services.assessments.assessment_service import AssessmentService
from app.domain.assessments.assessment import Assessment
from app.domain.questions.question import Question
from uuid import uuid4
from datetime import datetime, timezone
from unittest.mock import Mock

@pytest.fixture
def assessment():
    return Assessment(
        id = uuid4(),
        actual_question_index = 0,
        answers = [],
        questions = [
                    Question(1, "Pensando na última semana, você sentiu dificuldade para se acalmar? Conte como foi.", "Estresse"),
                    Question(2, "Pensando na última semana, você percebeu sua boca seca em algum momento? Conte como foi.", "Ansiedade"),
        ],
        classification = None,
        score = None,
        created_at = datetime.now(timezone.utc),
        updated_at = datetime.now(timezone.utc)
    )

@pytest.fixture
def ollama_service():
    service = Mock()
    service.process_conversation.return_value = 2
    return service

@pytest.fixture
def assessment_service(assessment, ollama_service):
    return AssessmentService(assessment, ollama_service)


def test_assessment_service_greeting(assessment_service):
    greeting = assessment_service.greeting()
    assert len(greeting) == 7

#TESTE DE RESPONDER A QUESTÃO E PASSAR PRA A PROXIMA
#TESTE COM MOCK DE OLLAMA
def test_assessment_service_answer_question(assessment, assessment_service, ollama_service):
    assessment_service.answer_question("Resposta do usuário")
    assessment_service.answer_question("Resposta do usuário 2")

    assert len(assessment_service.assessment.answers) == 2
    assert assessment_service.assessment.answers[0].content == "Resposta do usuário"
    assert assessment.actual_question_index == 2

    ollama_service.generate_feedback.assert_called_once()
    ollama_service.process_conversation.assert_called()


def test_assessment_service_many_answers(assessment, assessment_service):
    while assessment_service.assessment.actual_question_index < assessment.questions.__len__():
        assessment_service.answer_question("Resposta do usuário")

    assert len(assessment_service.assessment.answers) == assessment.questions.__len__()
    assessment_service.assessment.actual_question_index += 1

    with pytest.raises(Exception):
        assessment.send_question(assessment.questions[assessment_service.assessment.actual_question_index])
        

