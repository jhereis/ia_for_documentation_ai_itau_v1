# Assistente de Rotina Local usando Ollama e SQLite
# Objetivo: Guardar eventos de rotina e responder dúvidas do usuário
# Bibliotecas: langchain_community, sqlite3

import sqlite3
from langchain_community.llms import Ollama

class AssistenteIA:
    def __init__(self):
        # Aqui o Copilot deve sugerir a conexão com o banco 'rotina.db'
        self.conn = sqlite3.connect('rotina.db')
        self.criar_tabela()
        self.llm = Ollama(model="llama3")

    def criar_tabela(self):
        # Digite 'self.cursor' e deixe o Copilot sugerir o CREATE TABLE
        pass

    def salvar_evento(self, texto):
        # Sugira ao Copilot salvar o texto na tabela de rotina
        pass

    def consultar_memoria(self):
        # Peça para o Copilot buscar todos os registros e retornar uma string única
        pass
