# Importar streamlit, sqlite3 e OllamaLLM do langchain_ollama
# 1. Configurar a página do Streamlit com título "Meu Assistente de Rotina"

# 2. Criar uma função para conectar ao SQLite e buscar o histórico
# 3. Criar uma função para salvar novas anotações no SQLite

# 4. Criar a interface lateral (sidebar) com um campo de texto (text_area) 
#    para colar textos grandes e um botão "Salvar na Memória"

# 5. Criar o corpo principal: um chat (st.chat_message)
# 6. Usar st.chat_input para receber a dúvida do usuário
# 7. Quando o usuário enviar uma dúvida:
#    - Buscar histórico no banco
#    - Chamar o Ollama (llama3.2)
#    - Exibir a resposta na tela
