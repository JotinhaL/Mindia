from langchain_ollama import OllamaLLM
from agente_logica import SessaoDASS21, PROMPT_CLASSIFICADOR, calcular_resultados, QUESTOES_DASS21

# 1. Inicializa a IA
llm = OllamaLLM(model="deepseek-r1:1.5b") 

# 2. Inicializa a sessão do DASS-21
sessao = SessaoDASS21()
print(f"DEBUG: Quantidade de perguntas carregadas: {len(sessao.questoes)}")

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
    
print("Mindia: Olá! Vamos iniciar a avaliação.")

# Este loop é o coração do seu agente
while not sessao.teste_finalizado():
    pergunta = sessao.obter_pergunta_atual()
    
    # 1. O Python para aqui e espera você digitar
    texto_da_sua_resposta = input(f"\nAssistente: {pergunta}\nVocê: ")
    
    # 2. Aqui você CHAMA a função que você me mandou
    feedback = processar_conversa(texto_da_sua_resposta)
    
    # 3. Mostra o que a função retornou ("Entendido" ou "Não entendi")
    print(f"Mindia: {feedback}")
    
print("\n" + "="*30)
print("PROCESSANDO RESULTADOS...")

# Aqui você passa a lista completa para a função de cálculo
meus_resultados = calcular_resultados(sessao.respostas_coletadas)

print(f"Resultados Finais (Escala 0-42):")
print(f"Depressão: {meus_resultados['Depressão']}")
print(f"Ansiedade: {meus_resultados['Ansiedade']}")
print(f"Estresse: {meus_resultados['Estresse']}")
print("="*30)