# dataclasses - O que são dataclasses?
# O módulo dataclasses fornece um decorador e funções para criar métodos como
# __init__(), __repr__(), __eq__() (entre outros) em classes definidas pelo usuario
# Em resumo: dataclasses são syntax sugar para criar classes normais.
# Foi descrito na PEP 557 e adicionado na versão 3.7 do Python.
# doc: https://docs.pyhton.org/3/library/dataclasses.html


"""Aprendendo dataclass"""

from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    idade: int

if __name__ == '__main__':
    p1 = Pessoa('Matheus', 21)
    p2 = Pessoa('Matheus', 21)
    print(p1 == p2)