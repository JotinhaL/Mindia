from dataclasses import dataclass
from typing import ClassVar, List
from .questions import Question

class DASS21Questions:
    _questions: ClassVar[List[Question]] = [
        Question(1, "Achei difícil me acalmar", "Estresse"),
        Question(2, "Senti minha boca seca", "Ansiedade"),
        Question(3, "Não consegui vivenciar nenhum sentimento positivo", "Depressão"),
        Question(4, "Tive dificuldade em respirar em alguns momentos (ex. respiração ofegante, falta de ar, sem ter feito nenhum esforço físico)", "Ansiedade"),
        Question(5, "Achei difícil ter iniciativa para fazer as coisas", "Depressão"),
        Question(6, "Tive a tendência de reagir de forma exagerada às situações", "Estresse"),
        Question(7, "Senti tremores (ex. nas mãos)", "Ansiedade"),
        Question(8, "Senti que estava sempre nervoso", "Estresse"),
        Question(9, "Preocupei-me com situações em que eu pudesse entrar em pânico e parecesse ridículo(a)", "Ansiedade"),
        Question(10, "Senti que não tinha nada a desejar", "Depressão"),
        Question(11, "Senti-me agitado", "Estresse"),
        Question(12, "Achei difícil relaxar", "Estresse"),
        Question(13, "Senti-me depressivo(a) e sem ânimo", "Depressão"),
        Question(14, "Fui intolerante com as coisas que me impediam de continuar o que eu estava fazendo", "Estresse"),
        Question(15, "Senti que ia entrar em pânico", "Ansiedade"),
        Question(16, "Não consegui me entusiasmar com nada", "Depressão"),
        Question(17, "Senti que não tinha valor como pessoa", "Depressão"),
        Question(18, "Senti que estava um pouco emotivo/sensível demais", "Estresse"),
        Question(19, "Sabia que meu coração estava alterado mesmo não tendo feito nenhum esforço físico (ex. aumento da frequência cardíaca)", "Ansiedade"),
        Question(20, "Senti medo sem motivo", "Ansiedade"),
        Question(21, "Senti que a vida não tinha sentido", "Depressão")
    ]


    @classmethod
    def get_all(cls) -> List[Question]:
        return cls._questions
    
    @classmethod
    def get_question_by_id(cls, question_id: int) -> Question:
        for question in cls._questions:
            if question.id == question_id:
                return question
        raise ValueError(f"Question with id {question_id} not found")
    
    @classmethod
    def get_questions_by_category(cls, category: str) -> List[Question]:
        return [question for question in cls._questions if question.categoria == category]
    

    
DASS21_QUESTIONS = DASS21Questions.get_all()