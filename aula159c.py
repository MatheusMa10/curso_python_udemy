# dataclasses - O que são dataclasses?
# O módulo dataclasses fornece um decorador e funções para criar métodos como
# __init__(), __repr__(), __eq__() (entre outros) em classes definidas pelo usuario
# Em resumo: dataclasses são syntax sugar para criar classes normais.
# Foi descrito na PEP 557 e adicionado na versão 3.7 do Python.
# doc: https://docs.pyhton.org/3/library/dataclasses.html


"""Aprendendo sobre o metodo __post_init__ e __init__"""

from dataclasses import dataclass

@dataclass(init=False)
class Pessoa:
    nome: str
    sobrenome: str

    def __init__(self, nome: str, sobrenome: str):
        self.nome = nome
        self.sobrenome = sobrenome
        self.nome_completo = f'{self.nome} {self.sobrenome}'

    def __post_init__(self):
        print('POST INIT')
        self.nome_completo = f'{self.nome} {self.sobrenome}'

#     @property
#     def nome_completo(self):
#         return f'{self.nome} {self.sobrenome}'
    
#     @nome_completo.setter
#     def nome_completo(self, valor: str):
#         nome, *sobrenome = valor.split()
#         self.nome = nome
#         self.sobrenome = ' '.join(sobrenome)

if __name__ == '__main__':
    p1 = Pessoa('Matheus', 'Matos')
    print(p1)
    print(p1.nome_completo)