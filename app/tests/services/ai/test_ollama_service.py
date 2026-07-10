import pytest
from app.services.ai.ollama_service import OllamaService
from unittest.mock import Mock
from app.dto.feedback import Feedback_DTO


@pytest.fixture
def llm_mock():
    return Mock()


@pytest.fixture
def ollama_service(llm_mock):
    return OllamaService(llm_mock)

@pytest.fixture
def feedback_dto():
    return Feedback_DTO(
        stress=10,
        anxiety=5,
        depression=2,
        answers=["Resposta 1", "Resposta 2", "Resposta 3"]
    )


#TESTE MOCKADO
def test_process_conversation_retorna_2(ollama_service, llm_mock):

    llm_mock.invoke.return_value = "2"

    resultado = ollama_service.process_conversation(
        "Nessa ultima semana, você teve dificuldade para se acalmar?",
        "Foi muito difícil.",
    )

    assert resultado == 2
    
#TESTE MOCKADO
def test_feedback_generation(ollama_service, llm_mock, feedback_dto):
    llm_mock.invoke.return_value = "Feedback empatico"


    feedback = ollama_service.generate_feedback(feedback_dto)

    assert feedback == "Feedback empatico"
