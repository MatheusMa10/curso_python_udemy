# Herança simples - Relações entre classes
# Associação - usa, Agregação - tem
# Composição - É dono de, Herança - É um
#
# Herança vs Composição
#
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class
class Pessoa:
    cpf = '1234'
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def falar_nome_classe(self):
        print('CLASSE Pessoa')
        print(self.nome, self.sobrenome, self.__class__.__name__)

class Cliente(Pessoa):
    def falar_nome_classe(self):
        print('Eita, nem sai da classe Cliente')
        print(self.nome, self.sobrenome, self.__class__.__name__)

class Aluno(Pessoa):
    cpf = 'cpf aluno'

cliente1 = Cliente('Matheus', 'Matos')
print(cliente1.nome, cliente1.sobrenome)
cliente1.falar_nome_classe()
aluno1 = Aluno('Nubia', 'Santos')
print(aluno1.nome, aluno1.sobrenome)
aluno1.falar_nome_classe()
print(aluno1.cpf)
# help(Pessoa)
