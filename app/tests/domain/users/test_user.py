import pytest

from datetime import datetime, timezone
from uuid import uuid4
from app.domain.users.user import User


@pytest.fixture
def user():
    return User(
        id=uuid4(),
        name="Lucas",
        email="lucas@example.com",
        field_of_work="Marketing",
        created_at=datetime.now(timezone.utc),
        active=True,
        last_evaluation_at=None,
    )


def test_user_deactivate_and_activate(user):
    # User começa com active=True
    assert user.active is True
    
    # Desativa
    user.deactivate()
    assert user.active is False
    
    # Ativa novamente
    user.activate()
    assert user.active is True

def test_user_update_email(user):
    new_email = "joao.com"
    with pytest.raises(ValueError):
        user.update_email(new_email)

    new_email_correct = "joao@ufu.com"
    user.update_email(new_email_correct)
    assert user.email == new_email_correct  

def test_user_update_field_of_work(user):
    new_field_of_work = ""
    with pytest.raises(ValueError):
        user.update_field_of_work(new_field_of_work)

    new_field_of_work_correct = "Engenharia"
    user.update_field_of_work(new_field_of_work_correct)
    assert user.field_of_work == new_field_of_work_correct

def test_user_record_evaluation(user):
    assert user.last_evaluation_at is None
    user.record_evaluation()
    print(f"Last evaluation recorded at: {user.last_evaluation_at}")
    assert user.last_evaluation_at is not None
