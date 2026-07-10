from dataclasses import dataclass

@dataclass
class FeedbackDTO:
    stress: int 
    anxiety: int 
    depression: int 
    answers: list[str]