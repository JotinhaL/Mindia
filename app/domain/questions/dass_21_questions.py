from typing import ClassVar, List
from .question import Question

class DASS21Questions:
    _questions: ClassVar[List[Question]] = [
        Question(1, "Pensando na última semana, você sentiu dificuldade para se acalmar? Conte como foi.", "Estresse"),
        Question(2, "Pensando na última semana, você percebeu sua boca seca em algum momento? Conte como foi.", "Ansiedade"),
        Question(3, "Pensando na última semana, você conseguiu vivenciar sentimentos positivos? Conte como foi sua experiência.", "Depressão"),
        Question(4, "Pensando na última semana, você teve dificuldade para respirar em algum momento, como falta de ar ou respiração ofegante sem esforço físico? Conte como foi.", "Ansiedade"),
        Question(5, "Pensando na última semana, você teve dificuldade para tomar iniciativa e fazer as coisas? Conte como foi.", "Depressão"),
        Question(6, "Pensando na última semana, você percebeu que reagiu de forma exagerada a alguma situação? Conte como foi.", "Estresse"),
        Question(7, "Pensando na última semana, você sentiu tremores, como nas mãos? Conte como foi.", "Ansiedade"),
        Question(8, "Pensando na última semana, você se sentiu nervoso(a) com frequência? Conte como foi.", "Estresse"),
        Question(9, "Pensando na última semana, você se preocupou com a possibilidade de entrar em pânico ou passar vergonha? Conte como foi.", "Ansiedade"),
        Question(10, "Pensando na última semana, você sentiu que não tinha nada pelo que desejar ou esperar? Conte como foi.", "Depressão"),
        Question(11, "Pensando na última semana, você se sentiu agitado(a)? Conte como foi.", "Estresse"),
        Question(12, "Pensando na última semana, você teve dificuldade para relaxar? Conte como foi.", "Estresse"),
        Question(13, "Pensando na última semana, você se sentiu deprimido(a) ou sem ânimo? Conte como foi.", "Depressão"),
        Question(14, "Pensando na última semana, você percebeu que ficou intolerante ou irritado(a) com situações que interrompiam o que estava fazendo? Conte como foi.", "Estresse"),
        Question(15, "Pensando na última semana, você sentiu que poderia entrar em pânico? Conte como foi.", "Ansiedade"),
        Question(16, "Pensando na última semana, você teve dificuldade para se entusiasmar com alguma coisa? Conte como foi.", "Depressão"),
        Question(17, "Pensando na última semana, você sentiu que não tinha valor como pessoa? Conte como foi.", "Depressão"),
        Question(18, "Pensando na última semana, você percebeu que estava mais emotivo(a) ou sensível do que o habitual? Conte como foi.", "Estresse"),
        Question(19, "Pensando na última semana, você percebeu seu coração acelerado ou alterado mesmo sem esforço físico? Conte como foi.", "Ansiedade"),
        Question(20, "Pensando na última semana, você sentiu medo sem um motivo claro? Conte como foi.", "Ansiedade"),
        Question(21, "Pensando na última semana, você sentiu que a vida não tinha sentido? Conte como foi.", "Depressão"),

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