import pytest

from app.domain.sessions.session import SessaoDASS21
from app.domain.sessions.session import SessionStatus
from datetime import datetime, timezone
from uuid import uuid4

@pytest.fixture
def session():
    return SessaoDASS21(
        id = uuid4(),
        status = SessionStatus.PENDING,
        started_at = datetime.now(timezone.utc),
        ended_at = datetime.now(timezone.utc),
        created_at = datetime.now(timezone.utc),
        updated_at = datetime.now(timezone.utc)
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





    

