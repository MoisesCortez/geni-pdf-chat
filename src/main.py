import sys # importar e utilizar ferramentas do sistema 
import os # importar e ter acesso ao sistema operacional 

# direcionamento de caminhos e acesso a diretorios do projeto 

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as streamlit 
from src.extract import extract_txt_from_pdf 
from src.gemini_api import ask_gemini 

# Titulo da aplicação 
st.title("cht do gemini") 

# Upload do arquivo PDF 
upload_file =st.file_upload("Faça upload de um PDF",type=Pdf) 

# se um arquivo for carregado ,extrai o textyo e armazena na sessão 
if upload-file is not Nome:
    text = extract _text_from_pdf(upload_file) 
    st.session_state ["context"] = text 

    # campo de entrada para a pergunta do usuario 
    question = st.text_imput("Digite uma pergunta 😊") 

    # Se houver uma pergunta e um contexto carregado,chama a API do GEMINI! 
    if question and "context" in st.session_state: 
        response = ask_gemini("question, st.session_state ["context]") 
        st.write("### resposta:") 
        st.wit(response) # Exibe a resposta gerada pelo GEMINI! 
        