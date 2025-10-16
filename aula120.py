# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de
# classes.
# string = 'Luiz'  # str
# print(string.upper())
# print(isinstance(string, str))
class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome


p1 = Pessoa('Matheus', 'Matos')
# p1.nome = 'Luiz'
# p1.sobrenome = 'Otavio'

p2 = Pessoa('Luiz', 'Otavio')
# p2.nome = 'Luiz'
# p2.sobrenome = 'Otavio'

print(p1.nome)
print(p1.sobrenome)

print(p2.nome)
print(p2.sobrenome)

# Self é como se fosse a instancia da classe, a instancia da classe de cima é o p1 e p p2
