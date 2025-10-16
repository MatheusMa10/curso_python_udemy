# dataclasses - O que são dataclasses?
# O módulo dataclasses fornece um decorador e funções para criar métodos como
# __init__(), __repr__(), __eq__() (entre outros) em classes definidas pelo usuario
# Em resumo: dataclasses são syntax sugar para criar classes normais.
# Foi descrito na PEP 557 e adicionado na versão 3.7 do Python.
# doc: https://docs.pyhton.org/3/library/dataclasses.html


"""Aprendendo valores padroes, field, fields"""

"""Dataclasses são uma forma mais curta e simples de fazer classes porque elas ja tem algumas configurações proprias como por exemplo ja tem um método __repr__ imbutido dentro delas etc..."""

from dataclasses import dataclass, field, fields

@dataclass
class Pessoa:
    nome: str = field(default='Matheus', repr=False)
    sobrenome: str = 'Matos'
    idade: int = '21'
    enderecos: list[str] = field(default_factory=list)

if __name__ == '__main__':
    p1 = Pessoa()
    print(fields(p1))
    print(p1)