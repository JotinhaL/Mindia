import pytest

from app.domain.assessments.assessment import Assessment
from app.domain.questions.question import Question
from datetime import datetime, timezone
from app.domain.answers.answer import Answer
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

answer = [Answer(
            id=1,
            content="Nao estou me sentindo bem",
            value= 3,
            question=Question(id=1, content="Pergunta 1", category="Estresse"),
            created_at=datetime.now(timezone.utc),
        ),
        Answer(
            id=2,
            content="Estou bem",
            value= 0,
            question=Question(id=2, content="Pergunta 2", category="Anxiety"),
            created_at=datetime.now(timezone.utc),
        )
]

def test_handle_session_lifecycle(assessment):    
    assert assessment.questions != []
    assert assessment.answers == []

    assessment.answer_current_question(answer[0])

    assert len(assessment.answers) == 1
    assert assessment.answers[0].content == "Nao estou me sentindo bem"
    assert assessment.answers[0].value == 3

    assessment.next_question()

    assert assessment.actual_question_index == 1

    assessment.finish()

    assert assessment.score is not None
    assert assessment.classification is not None
 

def test_answer_current_question(assessment):
    assessment.answer_current_question(answer[0])
    assessment.next_question()
    assessment.answer_current_question(answer[1])
    assessment.next_question()


    assert len(assessment.answers) == 2
    assert assessment.answers[0].content == "Nao estou me sentindo bem"
    assert assessment.answers[0].value == 3
    assert assessment.answers[1].content == "Estou bem"
    assert assessment.answers[1].value == 0

def test_answer_current_question_no_more_questions(assessment):
    assessment.questions = [Question(id=1, content="Pergunta 1", category="demographic")]
    assessment.answer_current_question(answer[0])
    assessment.next_question()


    with pytest.raises(Exception):
        assessment.answer_current_question(answer[1])

def test_restart_assessment(assessment):
    assessment.answer_current_question(answer[0])
    assessment.finish()

    assert assessment.score is not None
    assert assessment.classification is not None


    assessment.restart()

    assert assessment.actual_question_index == 0
    assert assessment.answers == []
    assert assessment.score is None
    assert assessment.classification is None





    

