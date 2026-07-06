import pytest

from app.domain.assessments.assessment import Assessment
from app.domain.questions.question import Question
from datetime import datetime, timezone
from uuid import uuid4

@pytest.fixture
def assessment():
    return Assessment(
        id = uuid4(),
        actual_question_index = 0,
        answers = [],
        questions = [],
        classification = None,
        score = None,
        created_at = datetime.now(timezone.utc),
        updated_at = datetime.now(timezone.utc)
    )



def test_handle_session_lifecycle(assessment):    
    assert assessment.questions != []
    assert assessment.answers == []

    assessment.answer_current_question("Minha resposta", 0)
    assessment.finish()

    assert assessment.score is not None
    assert assessment.classification is not None
 

def test_answer_current_question(assessment):
    assessment.answer_current_question("Minha resposta", 2)
    assessment.answer_current_question("Outra resposta", 3)

    assert len(assessment.answers) == 2
    assert assessment.answers[0].content == "Minha resposta"
    assert assessment.answers[0].value == 2
    assert assessment.answers[1].content == "Outra resposta"
    assert assessment.answers[1].value == 3

def test_answer_current_question_no_more_questions(assessment):
    assessment.questions = [Question(id=1, content="Pergunta 1", category="demographic")]
    assessment.answer_current_question("Resposta 1", 2)

    with pytest.raises(Exception):
        assessment.answer_current_question("Resposta 2", 3)

def test_restart_assessment(assessment):
    assessment.answer_current_question("Minha resposta", 2)
    assessment.finish()

    assert assessment.score is not None
    assert assessment.classification is not None


    assessment.restart()

    assert assessment.actual_question_index == 0
    assert assessment.answers == []
    assert assessment.score is None
    assert assessment.classification is None





    

