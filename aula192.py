# + Web Scraping com Python usando requests e bs4 BeautifulSoup
# - Web Scraping é o ato de "raspar a web" buscando informações de forma
# automatizada, com determinada linguagem de programação, para uso posterior.
# - O módulo requests consegue carregar dados da Internet para dentro do seu
# código. Já o bs4.BeautifulSoup é responsável por interpretar os dados HTML
# em formato de objetos Python para facilitar a vida do desenvolvedor.
# - Doc: https://www.crummy.com/software/BeautifulSoup/bs4/doc.ptbr/
# + Instalação
# - pip install requests types-requests bs4
# python -m http.server -d aula190_site/ 3333

import requests
import re
from bs4 import BeautifulSoup

url = 'http://localhost:3333/'
response = requests.get(url) # Faz a leitura da url passada como parametro
raw_html = response.text # Mostra o conteudo da url (seu codigo)
parsed_html = BeautifulSoup(raw_html, 'html.parser') # Classe que recebe um documento HTML ou XML e faz com que eu possa chamar os argumentos ou metodos desses documentos como se fosse atributos Python

# Essa classe faz Web Scraping que basicamente faz a raspagem do conteudo de paginas html

# print(parsed_html)
print(parsed_html.title) # Pega a tag html title que foi transformada para um atributo Python com a classe BeautifulSoup

# if parsed_html.title is not None:
#     print(parsed_html.title.text)

top_jobs_heading = parsed_html.select_one('#intro > div > div > article > h2') # Metodo utilizado para selecionar um unico elemento do arquivo HTML

if top_jobs_heading is not None:
    article = top_jobs_heading.parent # Pegando a tag pai 
    if article is not None:
        for p in article.select('p'): # Selecionando todos os paragrafos do article com o metodo select para selecionar apenas as tags 'p' em vez de pegar todas as tags dentro do article
            # print(p)
            # print(p.text)
            print(re.sub(r'\s{1,}', ' ', p.text).strip())
