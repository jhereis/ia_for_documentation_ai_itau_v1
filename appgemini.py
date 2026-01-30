import sqlite3
from langchain_community.llms import Ollama

# 1. Configuração do Banco de Dados (Memória Permanente)
conn = sqlite3.connect('memoria_ia.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS rotina 
                  (id INTEGER PRIMARY KEY, informacao TEXT)''')
conn.commit()

# 2. Inicialização do Modelo Local
llm = Ollama(model="llama3")

def salvar_informacao(texto):
    cursor.execute("INSERT INTO rotina (informacao) VALUES (?)", (texto,))
    conn.commit()
    return "✅ Informação guardada na minha memória local."

def buscar_memoria():
    cursor.execute("SELECT informacao FROM rotina")
    rows = cursor.fetchall()
    return "\n".join([r[0] for r in rows])

print("🤖 IA de Rotina Local: On! (Comandos: 'anote: [texto]' ou apenas sua dúvida)")

while True:
    user_input = input("\nVocê: ")
    
    if user_input.lower() in ['sair', 'exit']: break

    if user_input.lower().startswith("anote:"):
        info = user_input.replace("anote:", "").strip()
        print(f"IA: {salvar_informacao(info)}")
    else:
        # Recupera tudo que a IA sabe para ela ter contexto
        contexto_memoria = buscar_memoria()
        
        prompt = f"""
        Você é um assistente de rotina. Abaixo estão os fatos que você sabe sobre mim:
        {contexto_memoria}
        
        Responda à seguinte dúvida baseando-se apenas nesses fatos: {user_input}
        Se não souber a resposta, diga que ainda não tem essa informação anotada.
        """
        
        resposta = llm.invoke(prompt)
        print(f"IA: {resposta}")