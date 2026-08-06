import datetime

from app.api.schemas.assessment import AnswerResponse
from app.domain.answers.answer import Answer
from app.domain.assessments.assessment import Assessment
from app.domain.assessments.score import Score
from app.domain.chatMessages.chat_message import ChatMessage
from app.domain.questions.question import Question
from app.dto.feedback import FeedbackDTO
from app.services.ai.ollama_service import OllamaService


class AssessmentService:
    def __init__(self, assessment: Assessment, ollama_service: OllamaService):
        self.assessment = assessment
        self.ollama_service = ollama_service


    def greeting(self):
        return [
            ChatMessage.assistant("Olá! 👋 Seja bem-vindo(a) à avaliação de bem-estar."),
            ChatMessage.assistant("Antes de começarmos, gostaria de explicar rapidamente como esta avaliação funciona."),
            ChatMessage.assistant("Sua participação é totalmente anônima. Nenhum dado que permita identificar você será associado às suas respostas."),
            ChatMessage.assistant("Para fins estatísticos, apenas informações gerais, como a área ou departamento em que você trabalha, poderão ser utilizadas para análises coletivas."),
            ChatMessage.assistant("Não existem respostas certas ou erradas. O mais importante é responder com sinceridade, de acordo com como você realmente tem se sentido nos ultimos dias."),
            ChatMessage.assistant("Responda as perguntas em apenas um bloco de texto, pois você pode acabar passando a próxima pergunta antes de terminar a resposta."),
            ChatMessage.assistant("Estou pronto para começar. Vamos para a primeira pergunta?")
        ]

    #*TODO refatorar essa funcao para separar responsabilidades, pois ela esta fazendo muita coisa
    def send_question(self):
        return self.assessment.send_question()

    def _create_answer(self, question: Question, response: str):
        actual_value = self.ollama_service.process_conversation(question, response)
        
        answer = Answer(
            #* ESSE ID SERA GERADO PELO BANCO DE DADOS
            id= 0,
            content= response,
            value= actual_value,
            question= question,
            created_at= datetime.datetime.now(datetime.timezone.utc),
        )

        return answer

    def _create_answer_response_not_finished_dto(self, answer: Answer):
        next_question = self.assessment.current_question()

        return AnswerResponse(
            id= answer.id,
            next_question= next_question,
            finished= False,
            depression= None,
            anxiety= None,
            stress= None,
            feedback= None,
            created_at= datetime.datetime.now(datetime.timezone.utc)
        )

    def _finish_assessment(self, last_answer: Answer, score: Score):
        feedback = self.ollama_service.generate_feedback(score)
        return AnswerResponse(
                id= last_answer.id,
                next_question= None,
                finished= True,
                depression= score.depression,
                anxiety= score.anxiety,
                stress= score.stress,
                feedback= feedback,
                created_at= datetime.datetime.now(datetime.timezone.utc)
        )

    def answer_question(self, response: str):

        current_question = self.assessment.current_question()

        answer = self._create_answer(current_question, response)
        
        self.assessment.answer_current_question(answer)

        self.assessment.next_question()

        if self.assessment.is_completed:
            score = self.assessment.finish()
            return self._finish_assessment(answer, score)


        #renomear essa funcao pq ela n cria dto ela ja finaliza o assessment
        return self._create_answer_response_not_finished_dto(answer)
        
        


        
    
        
