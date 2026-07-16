from pydantic import BaseModel

class classificationResponse(BaseModel):
    score = int
    classification = str