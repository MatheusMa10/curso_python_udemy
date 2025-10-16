# json.dumps e json.loads com strings + typing.TypedDIct
# Ao converter de Python para JSON:
# Python        JSON
# dict          object
# list, tuple   array
# str           string
# int, float    number
# True          true
# False         false
# None          null
import json
from pprint import pprint
from typing import TypedDict

class Movie(TypedDict):
    title: str
    original_title: str
    is_movie: bool
    imdb_rating: float
    year: int
    characters: list[str]
    budget: None | float

string_json = '''
{
    "title": "O Senhor dos Anéis: A Sociedade do Anel",
    "original_title": "The Lord of the Rings: The Fellowship of the Ring",
    "is_movie": true,
    "imdb_rating": 8.8,
    "year": 2001,
    "characters": ["Frodo", "Sam", "Gandalf", "Legolas", "Boromir"],
    "budget": null
}'''

movie: Movie = json.loads(string_json)
# pprint(movie, width=40)
# print(movie['title'])
# print(movie['year'])
# print(movie['budget'])
# print(movie['original_title'])
# print(movie['is_movie'])
# print(movie['characters'][2])
# print(movie['imdb_rating'])
json_string = json.dumps(movie, ensure_ascii=False, indent=2)

#####################################################################################################################
# (pprint) é uma função do modulo (pprint) que é um print com configurações adicionais
# (json) é um modulo que voce consegue mexer com (arquivos.json) que neles voce pode guardar dados simples de python
# (json.loads) carrega uma string no formato json
# (json.dumps) guarda o conteudo da variavel que voce passar dentro de um arquivo.json
# O modulo (typing) tem a classe (TypedDict) que tipa uma variavel como um dicionario e vc cria uma classe que herda dessa classe e passa todas as chaves e tipagens dela