from langchain_community.llms import Ollama
from agente_logica import SessaoDASS21, PROMPT_CLASSIFICADOR

# 1. Inicializa a IA
llm = Ollama(model="deepseek-r1:8b") 

# 2. Inicializa a sessão do DASS-21
sessao = SessaoDASS21()

def processar_conversa(texto_usuario):
    pergunta_atual = sessao.obter_pergunta_atual()
    
    # Criamos o prompt específico para esta rodada
    prompt_final = f"""
    {PROMPT_CLASSIFICADOR}
    Pergunta: {pergunta_atual}
    Resposta do Usuário: {texto_usuario}
    """
    
    # A comunicação real com o Ollama acontece aqui:
    resposta_ia = llm.invoke(prompt_final)
    
    # Limpeza: A IA as vezes fala demais, pegamos apenas o primeiro número que aparecer
    import re
    numero = re.search(r'\d', resposta_ia) # Busca o primeiro dígito (0-3)
    
    if numero:
        valor = int(numero.group())
        sessao.registrar_resposta(valor)
        return f"Entendido. Vamos para a próxima?"
    else:
        return "Não entendi bem. Pode repetir de outra forma?"