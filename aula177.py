# json.dump e json.load com arquivos
import json
import os

NOME_ARQUIVO = 'aula177.json'
CAMINHO_ABSOLUTO_ARQUIVO = os.path.abspath(
    os.path.join(
            os.path.dirname(__file__), 
            NOME_ARQUIVO
    )
)
# print(os.path.abspath(__file__))
print(CAMINHO_ABSOLUTO_ARQUIVO)
filme = {
    "title": "O Senhor dos Anéis: A Sociedade do Anel",
    "original_title": "The Lord of the Rings: The Fellowship of the Ring",
    "is_movie": True,
    "imdb_rating": 8.8,
    "year": 2001,
    "characters": ["Frodo", "Sam", "Gandalf", "Legolas", "Boromir"],
    "budget": None
    }

with open(CAMINHO_ABSOLUTO_ARQUIVO, 'w', encoding='utf-8') as arquivo:
    json.dump(filme, arquivo, ensure_ascii=False, indent=2)

with open(CAMINHO_ABSOLUTO_ARQUIVO, 'r', encoding='utf-8') as arquivo:
    movie = json.load(arquivo)
    print(movie)

###################################################################################################################
# (os.path.abspath) retorna o caminho absoluto do arquivo passado
# (os.path.dirname(__file__)) retorna o nome do diretorio desde o começo ao fim sem retornar o nome do arquivo
# (json.dump) guarda dados em um arquivo '.json'
# (json.load) carrega o valor do arquivo/variavel passada no seu parametro



