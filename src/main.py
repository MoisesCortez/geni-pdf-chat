import sys # imprtar e utilizar ferramenta do sistema
import os # importar e

#direcionamento de caminhos e acesso a diretorios do projeto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))

import streamlit as st
from src.extract import extract_text_from_pdf
from src.gemini_api import ask_gemini

# Titulo do aplicação
st.title("Chat do Gemini")

# Upload do arquivo PDF

uploaded_file =st.file_uploader("Faça upload do PDF",type = {"pdf"})

# Se um arquivo for carregado, extrai o texto e armazena na sessão
if uploaded_file is not None:
    text = extract_text_from_pdf(uploaded_file)
    st.session_state["context"] = text

# Campo de entrada para a pergunta do usuário
question = st.text_input("Digite uma pergunta😁👍")

# Se houver uma pergunta e um contexto carregado, chama a API do GEMINI
if question and "context" in st.session_state:
    response = ask_gemini(question,st.session_state["context"])
    st.write("### resposta:")
    st.write(response) # exibe a resposta gerada pelo GEMINI
    