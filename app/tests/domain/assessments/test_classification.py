import pytest

from app.domain.assessments.assessment import Classification
from app.domain.assessments.score import Score


@pytest.fixture
def classification():
    return Classification(
        depression="",
        anxiety="",
        stress=""

    )

def test_classify(): 
    values = [0, 5, 10, 15, 20, 25, 30]
    index = 0
    category = ["Depression", "Anxiety", "Stress"]  # You can change this to "Anxiety" or "Stress" to test other categories
    if category[index] == "Depression":  # You can change this to "Anxiety" or "Stress" to test other categories
        for value in values:
            classification = Classification._classify(value, category[index])
            if value == 30:
                index += 1
    elif category[index] == "Anxiety":
        for value in values:
            classification = Classification._classify(value, category[index])
            if value == 30:
                index += 1
    elif category[index] == "Stress":
        for value in values:
            classification = Classification._classify(value, category[index])
    assert classification in ["Normal", "Mild", "Moderate", "Severe", "Extremely Severe"]

def test_from_score(classification):

    score = Score(depression=10, anxiety=15, stress=20)
    classification = Classification.from_score(score)

    assert classification.depression in ["Normal", "Mild", "Moderate", "Severe", "Extremely Severe"]
    assert classification.anxiety in ["Normal", "Mild", "Moderate", "Severe", "Extremely Severe"]
    assert classification.stress in ["Normal", "Mild", "Moderate", "Severe", "Extremely Severe"]

def test_classify_score_numbers(classification):
    depression_score = 1
    anxiety_score = 20
    stress_score = 33

    classification = Classification.classify_score(depression_score, anxiety_score, stress_score)

    assert classification.depression in ["Normal", "Mild", "Moderate", "Severe", "Extremely Severe"]
    assert classification.anxiety in ["Normal", "Mild", "Moderate", "Severe", "Extremely Severe"]
    assert classification.stress in ["Normal", "Mild", "Moderate", "Severe", "Extremely Severe"]