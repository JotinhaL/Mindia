from dataclasses import dataclass

@dataclass
class Feedback_DTO:
    stress: int = 0
    anxiety: int = 0
    depression: int = 0
    answers: list[str]