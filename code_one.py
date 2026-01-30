#O Primeiro Código (Protótipo em Python)
import json

class AssistenteRotina:
    def __init__(self, nome_arquivo="minha_rotina.json"):
        self.nome_arquivo = nome_arquivo
        self.carregar_dados()

    def carregar_dados(self):
        try:
            with open(self.nome_arquivo, "r") as f:
                self.dados = json.load(f)
        except FileNotFoundError:
            self.dados = {}

    def salvar_dados(self):
        with open(self.nome_arquivo, "w") as f:
            json.dump(self.dados, f, indent=4)

    def guardar_rotina(self, dia, atividade):
        if dia not in self.dados:
            self.dados[dia] = []
        self.dados[dia].append(atividade)
        self.salvar_dados()
        return f"Entendido! Anotei '{atividade}' para {dia}."

    def consultar_dia(self, dia):
        atividades = self.dados.get(dia, [])
        if not atividades:
            return f"Você não tem nada agendado para {dia}."
        return f"Sua rotina para {dia}: " + ", ".join(atividades)

# Exemplo de uso:
ia = AssistenteRotina()
print(ia.guardar_rotina("Segunda", "Reunião de Data Science no Itaú"))
print(ia.consultar_dia("Segunda"))
