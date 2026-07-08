from dataclasses import dataclass


@dataclass(frozen=True)
class Question:
    id: int 
    content: str 
    category: str 

