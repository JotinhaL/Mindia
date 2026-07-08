import datetime
from app.domain.assessments.assessment import Assessment
from app.domain.chatMessages.chat_message import ChatMessage
from app.domain.answers.answer import Answer
from app.services.ai.ollama_service import OllamaService
class AssessmentService:
    def __init__(self, assessment: Assessment):
        self.assessment = assessment
        ollama_service = OllamaService()


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


    # *TODO implementar
    def answer_question(self, response: str):

        actual_question = self.assessment.current_question()
        
        actual_value = self.ollama_service.processar_conversa(actual_question.content, response)

        answer = Answer(
            id= actual_question.id,
            content= actual_question.content,
            value= actual_value,
            question= actual_question,
            created_at= datetime.datetime.now(datetime.timezone.utc),
        )
        
        self.assessment.answer_current_question(answer)
        self.assessment.next_question()


        
    
        
