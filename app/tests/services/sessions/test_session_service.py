from app.domain.sessions.session import SessionStatus
from app.services.sessions.session_service import SessionService
import pytest

@pytest.fixture
def session_service():
    return SessionService()

def test_session_service_create_session(session_service):
    session = session_service.create_session()

    assert session.status == SessionStatus.ACTIVE
    assert session.assessment is not None
    assert session.assessment.questions is not None