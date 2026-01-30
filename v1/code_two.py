from langchain_community.llms import Ollama
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferWindowMemory

# Inicializa o modelo que você baixou no Ollama
llm = Ollama(model="llama3")

# Criamos uma memória para que ela lembre do contexto da conversa atual
memoria = ConversationBufferWindowMemory(k=5) 

print("🤖 IA de Rotina Local Ativa! (Digite 'sair' para encerrar)")

while True:
    pergunta = input("Você: ")
    if pergunta.lower() == 'sair':
        break

    # Prompt simples para guiar a IA
    contexto = f"""
    Você é um assistente pessoal de rotina. 
    Seu objetivo é ajudar a organizar o dia a dia e tirar dúvidas sobre horários.
    Responda de forma curta e objetiva em Português.
    
    Pergunta: {pergunta}
    """

    resposta = llm.invoke(contexto)
    print(f"IA: {resposta}")
