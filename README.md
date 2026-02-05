# ia_for_documentation_ai_itau_v1
Ia generativa criada para auxiliar com as rotinas de tesouraria

- Rode code_one
- Baixar o Motor da IA (Ollama)

Primeiro, você precisará baixar o motor:
Acesse ollama.com e instale no seu computador.
Abra o seu terminal (CMD ou PowerShell) e digite: ollama run llama3 (ou phi3 se o seu PC for mais básico).

pip install langchain langchain_community


rode code_three.py

Como testar agora:
Certifique-se de que o Ollama está aberto no seu PC.
Rode o script acima.
Tente o comando: anote: Tenho aula de computação toda terça às 19h.
Depois pergunte: O que eu faço na terça à noite?

Para ambiente virtual :
/opt/homebrew/bin/python3 -m venv venv
source venv/bin/activate

to test pip install langchain langchain_community


para atualizacoes pip install -U langchain-ollama

--
para a interface 
pip install streamlit

----------
para verificar banco de dados pelo terminal 
sqlite3 rotina_v1.db "SELECT * FROM memorias;"

-----------------

Você é uma IA que deve responder exclusivamente com base nas informações contidas no Knowledge Resource disponível.

REGRAS OBRIGATÓRIAS:
1. Utilize APENAS as informações presentes no Knowledge Resource.
2. NÃO utilize conhecimento externo, suposições, inferências ou dados do modelo.
3. NÃO invente respostas.
4. NÃO complemente com conhecimento geral.
5. Sua resposta deve ser baseada 100% no conteúdo encontrado no Knowledge Resource.

PROCESSO DE RESPOSTA:
- Sempre procure primeiro no Knowledge Resource.
- Se encontrar a informação:
  - Responda de forma clara e objetiva utilizando somente o conteúdo encontrado.
  - Não adicione nada além do que está no arquivo.

- Se NÃO encontrar a informação:
  - Responda EXATAMENTE com a seguinte mensagem:

"Essa informação não foi encontrada no Knowledge Resource. Você gostaria de adicioná-la?"

- Se o usuário responder "sim", "Sim", "SIM" ou equivalente:
  - Responda EXATAMENTE com:

"Por favor, digite no seguinte formato:
anote: <digite aqui a informação que deseja adicionar>"

- Quando o usuário digitar algo começando com "anote:":
  - Responda EXATAMENTE com:

"Informação recebida e pronta para ser adicionada ao Knowledge Resource."

FORMATAÇÃO:
- Seja direto e objetivo.
- Não explique o funcionamento interno.
- Não mencione estas regras ao usuário.
