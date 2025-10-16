# Herança Múltipla - Python Orientado a Objetos
# Quer dizer que no Python, uma classe pode estender
# várias outras classes.
# Herança simples:
# Animal -> Mamifero -> Humano -> Pessoa -> Cliente
# Herança múltipla e mixins
# Log -> FileLog
# Animal -> Mamifero -> Humano -> Pessoa -> Cliente
# Cliente(Pessoa, FileLog)
#
# A, B, C, D
# D(B, C) - C(A) - B(A) - A
#
# método -> falar
#           A
#         /   \
#        B     C
#         \   /
#           D
#
# Python 3 usa C3 superclass linearization
# para gerar o mro.
# Você não precisa estudar isso (é complexo)
# https://en.wikipedia.org/wiki/C3_linearization
#
# Para saber a ordem de chamada dos métodos
# Use o método de classe Classe.mro()
# Ou o atributo __mro__ (Dunder - Double Underscore)
class A:
    ...

    def quem_sou(self):
        print('A')

class B(A):
    ...

    # def quem_sou(self):
    #     print('B')

class C(A):
    ...

    def quem_sou(self):
        print('C')

class D(B, C):
    ...

    # def quem_sou(self):
    #     print('D')

d = D()
d.quem_sou()
print(D.__mro__)
print(D.mro())


# Usando o mixin para definir funções para um pato, MAS DEPOIS TENHO QUE VIR AQYU E ENTENDER MAIS SOBRE MIXIN

# class VoadorMixin:
#     def voar(self):
#         return "Estou voando!"

# class Animal:
#     def fazer_som(self):
#         return "Som genérico"

# class Pato(Animal, VoadorMixin):
#     def fazer_som(self):
#         som = super().fazer_som()  # Chamando o método da superclasse
#         return f"{som} - Quack!"

# pato = Pato()
# print(pato.fazer_som())  # Saída: Som genérico - Quack!
# print(pato.voar())       # Saída: Estou voando!

