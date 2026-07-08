import re

from langchain_ollama import OllamaLLM
from app.agents.agente_logica import PROMPT_CLASSIFICADOR
from app.domain.assessments.assessment import Assessment


class OllamaService:
    def __init__(self):
        self.llm = OllamaLLM(model="llama3.2")

    def processar_conversa(self, pergunta: str, resposta: str) -> int | None:
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
        
        
