import re

from langchain_ollama import OllamaLLM
from app.agents.agente_logica import PROMPT_CLASSIFICADOR, PROMPT_FEEDBACK
from app.dto.feedback import FeedbackDTO



class OllamaService:
    def __init__(self, llm = None):
        self.llm = llm or OllamaLLM(model="llama3.2")

    def process_conversation(self, pergunta: str, resposta: str) -> int | None:
        prompt_final = f"""
        {PROMPT_CLASSIFICADOR}

        Pergunta: {pergunta}
        Resposta do Usuário: {resposta}
        """

        resposta_ia = self.llm.invoke(prompt_final)

        numero = re.search(r"\d", resposta_ia)

        if numero:
            valor = int(numero.group())
            if valor in {0, 1, 2, 3}:
                return valor

        return None
    

    def generate_feedback(self, FeedbackDTO: FeedbackDTO) -> str:
        prompt_final = f"""
        {PROMPT_FEEDBACK}

        {FeedbackDTO.stress}
        {FeedbackDTO.anxiety}
        {FeedbackDTO.depression}
        {FeedbackDTO.answers}
        """

        resposta_ia = self.llm.invoke(prompt_final)

        return resposta_ia
        
        
