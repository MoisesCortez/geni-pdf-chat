import pypdf 

def extract_text_from_pdf(pdf_file):
    """
    Função para extrair o texto de um PDF carregando o Streamlit

    Parametros:
    pdf_file (UploadedFile):

    Retorno
    str: Texto extraido do PDF

    """
    reader = pypdf.PdfReader(pdf_file) #Cria o objeto para ler o PDF
    # Percorre todas as paginas e extrair
    text = "\n".join([page.extract_text()for page in reader.pages if page.extract_text()])
    return text # retona o texto extraido


    