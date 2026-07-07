import pytest
import datetime

from app.domain.assessments.assessment import Score
from app.domain.questions.question import Question
from app.domain.answers.answer import Answer

@pytest.fixture
def score():
    return Score(
        depression=0,
        anxiety=0,
        stress=0
    )

def test_from_answers(score):
    answers = [
        Answer(1, Question(1, "Achei difícil me acalmar", "Estresse"), "Nao estou bem", 2, datetime.datetime.now(datetime.timezone.utc)),
        Answer(2, Question(2, "Senti minha boca seca", "Ansiedade"), "Nao estou bem", 3, datetime.datetime.now(datetime.timezone.utc)),
        Answer(3, Question(3, "Não consegui vivenciar nenhum sentimento positivo", "Depressão"), "Nao estou bem", 1, datetime.datetime.now(datetime.timezone.utc))
    ]

    score = Score.from_answers(answers)


    assert score.depression == answers[2].value * 2
    assert score.anxiety == answers[1].value * 2
    assert score.stress == answers[0].value * 2

