import pytest

from app.domain.questions.dass_21_questions import DASS21_QUESTIONS

@pytest.fixture
def dass_21_questions():
    return DASS21_QUESTIONS

def test_dass_21_questions_length(dass_21_questions):
    assert len(dass_21_questions) == 21

def test_get_question_by_id(dass_21_questions):
    question_id = 5
    question = next((q for q in dass_21_questions if q.id == question_id), None)
    assert question is not None
    assert question.id == question_id
    assert question.content == "Pensando na última semana, você teve dificuldade para tomar iniciativa e fazer as coisas? Conte como foi."

def test_get_questions_by_category(dass_21_questions):
    category = "Ansiedade"
    questions = [q for q in dass_21_questions if q.category == category]
    assert len(questions) == 7
    for question in questions:
        assert question.category == category