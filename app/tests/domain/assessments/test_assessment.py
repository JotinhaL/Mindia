import pytest

from app.domain.assessments.assessment import Assessment
from app.domain.answers.answer import Answer
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

answer = Answer(
    id=1,
    question=Question(id=1, content="Qual é a sua idade?", category="Estresse"),
    content="Minha resposta",
    created_at=datetime.now(timezone.utc)
)


def test_handle_session_lifecycle(assessment):    
    assessment.start()
    assert assessment.questions != []
    assert assessment.answers == []

    assessment.answer_current_question("Minha resposta")
    assessment.finish()

    assert assessment.score is not None
    assert assessment.classification is not None
 

def test_answer_current_question(assessment):
    assessment.start()
    assessment.answer_current_question("Minha resposta")
    assessment.answer_current_question("Outra resposta")

    assert len(assessment.answers) == 2
    assert assessment.answers[0].content == "Minha resposta"
    assert assessment.answers[1].content == "Outra resposta"

def test_answer_current_question_no_more_questions(assessment):
    assessment.start()
    assessment.questions = [Question(id=1, content="Pergunta 1", category="demographic")]
    assessment.answer_current_question("Resposta 1")

    with pytest.raises(Exception):
        assessment.answer_current_question("Resposta 2")





    

