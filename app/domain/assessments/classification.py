from dataclasses import dataclass

from app.domain.assessments.score import Score


@dataclass(frozen=True)
class Classification:
    depression: str
    anxiety: str
    stress: str

    @classmethod
    def from_score(cls, score: Score) -> "Classification":
        return cls.classify_score(score.depression, score.anxiety, score.stress)

    @classmethod
    def classify_score(cls, depression: int, anxiety: int, stress: int) -> "Classification":
        return cls(
            depression=cls._classify(depression, "Depression"),
            anxiety=cls._classify(anxiety, "Anxiety"),
            stress=cls._classify(stress, "Stress"),
        )

    @staticmethod
    def _classify(value: int, category: str) -> str:
        thresholds = {
            "Depression": (9, 13, 20, 27),
            "Anxiety": (7, 9, 14, 19),
            "Stress": (14, 18, 25, 33),
        }

        normal, mild, moderate, severe = thresholds[category]

        if value <= normal:
            return "Normal"
        if value <= mild:
            return "Mild"
        if value <= moderate:
            return "Moderate"
        if value <= severe:
            return "Severe"

        return "Extremely Severe"