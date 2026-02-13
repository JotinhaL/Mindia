# Lista extraída do site MedRio (DASS-21)
QUESTOES_DASS21 = [
    {"id": 1, "texto": "Achei difícil me acalmar", "categoria": "Estresse"},
    {"id": 2, "texto": "Senti minha boca seca", "categoria": "Ansiedade"},
    {"id": 3, "texto": "Não consegui vivenciar nenhum sentimento positivo", "categoria": "Depressão"},
    {"id": 4, "texto": "Tive dificuldade em respirar em alguns momentos (ex. respiração ofegante, falta de ar, sem ter feito nenhum esforço físico)", "categoria": "Ansiedade"},
    {"id": 5, "texto": "Achei difícil ter iniciativa para fazer as coisas", "categoria": "Depressão"},
    {"id": 6, "texto": "Tive a tendência de reagir de forma exagerada às situações", "categoria": "Estresse"},
    {"id": 7, "texto": "Senti tremores (ex. nas mãos)", "categoria": "Ansiedade"},
    {"id": 8, "texto": "Senti que estava sempre nervoso", "categoria": "Estresse"},
    {"id": 9, "texto": "Preocupei-me com situações em que eu pudesse entrar em pânico e parecesse ridículo(a)", "categoria": "Ansiedade"},
    {"id": 10, "texto": "Senti que não tinha nada a desejar", "categoria": "Depressão"},
    {"id": 11, "texto": "Senti-me agitado", "categoria": "Estresse"},
    {"id": 12, "texto": "Achei difícil relaxar", "categoria": "Estresse"},
    {"id": 13, "texto": "Senti-me depressivo(a) e sem ânimo", "categoria": "Depressão"},
    {"id": 14, "texto": "Fui intolerante com as coisas que me impediam de continuar o que eu estava fazendo", "categoria": "Estresse"},
    {"id": 15, "texto": "Senti que ia entrar em pânico", "categoria": "Ansiedade"},
    {"id": 16, "texto": "Não consegui me entusiasmar com nada", "categoria": "Depressão"},
    {"id": 17, "texto": "Senti que não tinha valor como pessoa", "categoria": "Depressão"},
    {"id": 18, "texto": "Senti que estava um pouco emotivo/sensível demais", "categoria": "Estresse"},
    {"id": 19, "texto": "Sabia que meu coração estava alterado mesmo não tendo feito nenhum esforço físico (ex. aumento da frequência cardíaca)", "categoria": "Ansiedade"},
    {"id": 20, "texto": "Senti medo sem motivo", "categoria": "Ansiedade"},
    {"id": 21, "texto": "Senti que a vida não tinha sentido", "categoria": "Depressão"}
]

# Escala de valores
ESCALA_VALORES = {
    "Não se aplicou de maneira alguma": 0,
    "Aplicou-se em algum grau, ou por pouco de tempo": 1,
    "Aplicou-se em um grau considerável, ou por uma boa parte do tempo": 2,
    "Aplicou-se muito, ou na maioria do tempo": 3
}

class SessaoDASS21:
    def __init__(self):
        self.indice_pergunta_atual = 0
        self.respostas_coletadas = []
        self.questoes = QUESTOES_DASS21 

    def obter_pergunta_atual(self):
        if self.indice_pergunta_atual < len(self.questoes):
            return self.questoes[self.indice_pergunta_atual]["texto"]
        return None

    def registrar_resposta(self, valor_numérico):
        # Guarda a resposta com a categoria para o cálculo final
        pergunta = self.questoes[self.indice_pergunta_atual]
        self.respostas_coletadas.append({
            "categoria": pergunta["categoria"],
            "valor": valor_numérico
        })
        self.indice_pergunta_atual += 1

    def teste_finalizado(self):
        return self.indice_pergunta_atual >= len(self.questoes)