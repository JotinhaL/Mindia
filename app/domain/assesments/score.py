from dataclasses import dataclass
from dataclasses import field

@dataclass
class Score:
    depression: int
    anxiety: int
    stress: int
    sum_depressiion: list[int] = field(default_factory=list)
    sum_anxiety: list[int] = field(default_factory=list)
    sum_stress: list[int] = field(default_factory=list)

    def __post_init__(self):
            if self.depression < 0 or self.anxiety < 0 or self.stress < 0:
                raise ValueError("Scores cannot be negative")
            
    def depression_score(self, value: int) -> int:
            sum_depression.append(value)
            return sum(self.depression) * 2

    def anxiety_score(self) -> int:
            return sum(self.anxiety) * 2

    def stress_score(self) -> int:
            return sum(self.stress) * 2

    def total_score(self) -> int:
            return self.depression_score() + self.anxiety_score() + self.stress_score()