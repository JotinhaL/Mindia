from pydantic import BaseModel


class AssessmentStartRequest(BaseModel):
    department: str

class AssessmentStartResponse(BaseModel):
    assessment_id: str
    question: str
    
class AnswerRequest(BaseModel):
    answer: str

class AnswerResponse(BaseModel):
    next_question: str | None
    finished: bool

