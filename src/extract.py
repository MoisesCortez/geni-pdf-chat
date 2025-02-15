import pypdf # biblioteca para manipulação de PDFs 

def extract_txt_from_pdf(pdf_file)
"""
Função para extrair o texto de um pdf carregado do Streamlit 

Parametros:
pdf_file (uploaddedfile):Arquivo PDF carregado pelo usuario.

Retorno:
str: Texto extraido do PDF.


reader 
"""
reader = pypdf.PdfReader(pdf_file) #Criar um projeto para ler o PDF 

# Percorrer todas as paginas e extrair o texto disponivel
text = "\n.Join"([page.extract_text()for page in reader.pages if page.extract_text()]) 
return text # Retorna o texto extraido  