import pytest

from app.domain.sessions.session import SessaoDASS21
from app.domain.answers.answer import Answer
from app.domain.questions.question import Question
from app.domain.sessions.session import SessionStatus
from datetime import datetime, timezone
from uuid import uuid4

@pytest.fixture
def session():
    return SessaoDASS21(
        id = uuid4(),
        status = SessionStatus.PENDING,
        actual_question_index = 0,
        answers = [],
        questions = [],
        classification = None,
        score = None,
        started_at = datetime.now(timezone.utc),
        ended_at = datetime.now(timezone.utc),
        created_at = datetime.now(timezone.utc),
        updated_at = datetime.now(timezone.utc)
    )

answer = Answer(
    id=1,
    question=Question(id=1, content="Qual é a sua idade?", category="demographic"),
    content="Minha resposta",
    created_at=datetime.now(timezone.utc)
)


def test_handle_session_lifecycle(session):
    session.start()
    assert session.status == SessionStatus.ACTIVE

    session.finish()
    assert session.status == SessionStatus.CLOSED

    session.reset()
    assert session.status == SessionStatus.PENDING

def test_answer_current_question_invalid_state(session):
    with pytest.raises(Exception):
        session.answer_current_question("Minha resposta")  

def test_answer_current_question(session):
    session.start()
    session.answer_current_question("Minha resposta")
    session.answer_current_question("Outra resposta")

    assert len(session.answers) == 2
    assert session.answers[0].content == "Minha resposta"
    assert session.answers[1].content == "Outra resposta"

def test_answer_current_question_no_more_questions(session):
    session.start()
    session.questions = [Question(id=1, content="Pergunta 1", category="demographic")]
    session.answer_current_question("Resposta 1")

    with pytest.raises(Exception):
        session.answer_current_question("Resposta 2")

def test_is_active(session):
    assert session.is_active() is False

    session.start()
    assert session.is_active() is True

    session.finish()
    assert session.is_active() is False



    

