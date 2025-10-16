# # PyPDF2 para manipular arquivos PDF (Instalação)
# PyPDF2 é uma biblioteca de manipulação de arquivos PDF feita em Python puro,
# gratuita e de código aberto. Ela é capaz de ler, manipular, escrever e unir
# dados de arquivos PDF, assim como adicionar anotações, transformar páginas,
# extrair texto e imagens, manipular metadados, e mais.
# A documentação contém todas as informações necessárias para usar PyPDF2.
# Link: https://pypdf2.readthedocs.io/en/3.0.0/
# Ative seu ambiente virtual
# pip install pypdf2
from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter, PdfMerger


PASTA_RAIZ = Path(__file__).parent

PASTA_ORIGINAIS = PASTA_RAIZ / 'pdfs_originais'
PASTA_NOVA = PASTA_RAIZ / 'arquivos_novos'

RELATORIO_BACEN = PASTA_ORIGINAIS / 'R20240510.pdf'
PASTA_NOVA.mkdir(exist_ok=True)

# Classe que é o leitor de um arquivo(.pdf), e como parametro você passa o arquivo(.pdf) que vai ser lido
reader = PdfReader(RELATORIO_BACEN) 
# print(len(reader.pages))
# for page in reader.pages:
#     print(page)
#     print()
#     print(page.images)

page0 = reader.pages[0] # Atributo da classe PdfReader que mostra as paginas do arquivo
# imagem0 = page0.images[0] # Atributo da classe PdfReader que mostra as imagens do arquivo

# print(page0.extract_text()) # Método que mostra oque esta escrito em cada pagina
# with open(PASTA_NOVA / f'{imagem0.name}.jpeg', 'wb') as fp:
#     fp.write(imagem0.data)


"""NÃO CONSEGUI ABRIR A IMAGEM POR ESTAR EM FORMATO PNG AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"""


#                                            PRIMEIRA FORMA


# writer = PdfWriter() # Classe que é o escritor de arquivos(.pdf)
# writer.add_page(page0) 
# Método que adiciona uma nova pagina ao arquivo e como parametro foi passado a pagina de um pdf ja existente

# with open(PASTA_NOVA / 'page0.pdf', 'wb') as arquivo:
#     writer.write(arquivo) # Método do PdfWriter que fala para escrever os dados que foram recebidas no método add_page()


#                                            SEGUNDA FORMA


# writer = PdfWriter()

# with open(PASTA_NOVA / 'NOVO_PDF.pdf', 'wb') as arquivo:
#     for page in reader.pages:
#         writer.add_page(page)
#     writer.write(arquivo)


#                                           TERCEIRA FORMA


# for i, page in enumerate(reader.pages):
#     writer = PdfWriter()

#     with open(PASTA_NOVA / f'page{i}.pdf', 'wb') as arquivo:
#         writer.add_page(page)
#         writer.write(arquivo)


files = [
    PASTA_NOVA / f'page1.pdf',
    PASTA_NOVA / f'page0.pdf',
]

merger = PdfMerger() # Classe que junta arquivos(.pdf) separados
for file in files:
    merger.append(file) # Método que recebe arquivos(.pdf) que voce queira juntar

with open(PASTA_NOVA / 'MERGERD.pdf', 'wb') as arquivo:
    merger.write(arquivo) # Método que recebe os dados do método append() e junta todos arquivos(.pdf) que foram passados
