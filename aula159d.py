# dataclasses - O que são dataclasses?
# O módulo dataclasses fornece um decorador e funções para criar métodos como
# __init__(), __repr__(), __eq__() (entre outros) em classes definidas pelo usuario
# Em resumo: dataclasses são syntax sugar para criar classes normais.
# Foi descrito na PEP 557 e adicionado na versão 3.7 do Python.
# doc: https://docs.pyhton.org/3/library/dataclasses.html


"""Aprendendo configurações do decorador dataclass"""

from dataclasses import dataclass


# @dataclass(frozen=True, repr=False, order=True)
@dataclass(order=True)
class Pessoa:
    nome: str
    sobrenome: str


if __name__ == '__main__':
    lista_pessoas = [Pessoa('a', 'z'), Pessoa('b', 'y'), Pessoa('c', 'x')]
    lista_pessoas_ordenada = sorted(lista_pessoas, key= lambda pessoa: pessoa.sobrenome)
    print(lista_pessoas)
    print(lista_pessoas_ordenada)