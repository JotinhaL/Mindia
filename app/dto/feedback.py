from dataclasses import dataclass

@dataclass
class Feedback_DTO:
    stress: int 
    anxiety: int 
    depression: int 
    answers: list[str]