from pydantic import BaseModel

class QuestionResponse(BaseModel):
    id: int
    content: str
    category: str