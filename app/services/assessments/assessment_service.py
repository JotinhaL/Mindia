from app.domain.assessments.assessment import Assessment
from app.domain.questions.question import Question

from app.domain.assessments.assessment import InvalidSessionError

class AssessmentService:
    def __init__(self, assessment: Assessment):
        self.assessment = assessment


    # *TODO implementar
    def answer_question(self):
        actual_question = self.assessment.current_question()
        content = actual_question.content 

        if actual_question is None:
            raise InvalidSessionError("Cannot answer question: no questions left")
        
        self.assessment.answer_current_question(content, value)
        
        
