# super() e a sobreposição de membros - Python Orientado a Objetos
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class
# class MinhaString(str):
#     def upper(self):
#         print('CHAMOU UPPER')
#         retorno = super(MinhaString, self).upper()
#         print('DEPOIS DO UPPER')
#         return retorno

# string = MinhaString('Luiz')
# print(string.upper())

class A:
    atributo_a = 'valor a'

    def __init__(self, atributo):
        self.atributo = atributo
        
    def metodo(self):
        print('A')

class B(A):
    atributo_b = 'valor b'

    def __init__(self, atributo, outra_coisa):
        super().__init__(atributo)
        self.outra_coisa = outra_coisa

    def metodo(self):
        print('B')

class C(B):
    atributo_c = 'valor c'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print('EI, burlei o sistema')

    def metodo(self):
        # super().metodo() # B
        # super(B, self).metodo() # A
        # super(A, self).metodo() # object
        A.metodo(self)
        B.metodo(self)
        print('C')

# print(C.mro())
# print(B.mro())
# print(A.mro())
c = C('atributo', 'Qualquer')
print(c.atributo)
print(c.outra_coisa)
# print(c.atributo_a)
# print(c.atributo_b)
# print(c.atributo_c)
c.metodo()

# AGORA VOU DEIXAR VARIOS EXEMPLOS DE COMO SE UTILIZAR A FUNÇÃO SUPER() EM PYTHON.

# 1. Inicialização de uma subclasse: Usar super() no método __init__() da subclasse para chamar o construtor da superclasse e garantir que todos os atributos da classe pai sejam inicializados corretamente.

# class Animal:
#     def __init__(self, nome):
#         self.nome = nome

# class Cachorro(Animal):
#     def __init__(self, nome, raca):
#         super().__init__(nome)
#         self.raca = raca

# cachorro = Cachorro("Rex", "Labrador")
# print(cachorro.nome)  # Saída: Rex
# print(cachorro.raca)  # Saída: Labrador


# 2. Chamada de métodos da superclasse: Em qualquer método de uma subclasse, você pode usar super() para chamar métodos da superclasse e estender seu comportamento. Isso é útil quando você quer adicionar funcionalidades à implementação da superclasse, sem precisar reescrever todo o método.

# class Animal:
#     def fazer_som(self):
#         return "Som genérico"

# class Cachorro(Animal):
#     def fazer_som(self):
#         som = super().fazer_som()  # Chamando o método da superclasse
#         return f"{som} - Au au!"

# cachorro = Cachorro()
# print(cachorro.fazer_som())  # Saída: Som genérico - Au au!


# AINDA DO EXEMPLO 2 MAS SEM GUARDAR O VALOR DA FUNÇÃO SUPER() EM UMA VARIAVEL

# class Animal:
#     def fazer_som(self):
#         return "Som genérico"

# class Cachorro(Animal):
#     def fazer_som(self):
#         return f"{super().fazer_som()} - Au au!"

# cachorro = Cachorro()
# print(cachorro.fazer_som())  # Saída: Som genérico - Au au!


# 3. Herança múltipla: Quando você está lidando com herança múltipla em Python, a função super() pode ser usada para garantir uma ordem coerente de chamadas de inicialização e métodos entre as superclasses.

# class A:
#     def __init__(self):
#         print("Inicializando A")

# class B:
#     def __init__(self):
#         print("Inicializando B")

# class C(A, B):
#     def __init__(self):
#         super().__init__()

# c = C()  # Saída: Inicializando A


# 4. Reescrita de métodos: Ao reescrever um método em uma subclasse, você pode querer chamar o método correspondente da superclasse dentro da implementação da subclasse para reutilizar parte da lógica da superclasse.

# class Animal:
#     def fazer_som(self):
#         return "Som genérico"

# class Cachorro(Animal):
#     def fazer_som(self):
#         som = super().fazer_som()  # Chamando o método da superclasse
#         return f"{som} - Au au!"

# class Gato(Animal):
#     def fazer_som(self):
#         som = super().fazer_som()  # Chamando o método da superclasse
#         return f"{som} - Miau!"

# cachorro = Cachorro()
# print(cachorro.fazer_som())  # Saída: Som genérico - Au au!

# gato = Gato()
# print(gato.fazer_som())      # Saída: Som genérico - Miau!


# AINDA DO EXEMPLO 4 MAS SEM GUARDAR O VALOR DA FUNÇÃO SUPER() EM UMA VARIAVEL.

# class Animal:
#     def fazer_som(self):
#         return "Som genérico"

# class Cachorro(Animal):
#     def fazer_som(self):
#         return f"{super().fazer_som()} - Au au!"

# class Gato(Animal):
#     def fazer_som(self):
#         return f"{super().fazer_som()} - Miau!"

# cachorro = Cachorro()
# print(cachorro.fazer_som())  # Saída: Som genérico - Au au!

# gato = Gato()
# print(gato.fazer_som())      # Saída: Som genérico - Miau!


# 5. Implementação de Mixins: Mixins são classes que fornecem funcionalidades adicionais a outras classes através de herança múltipla. A função super() é frequentemente usada ao trabalhar com mixins para chamar métodos de classes base sem precisar conhecer a hierarquia completa das classes.


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


# AINDA DO EXEMPLO 5 MAS SEM GUARDAR O VALOR DA FUNÇÃO SUPER() EM UMA VARIAVEL.


# class VoadorMixin:
#     def voar(self):
#         return "Estou voando!"

# class Animal:
#     def fazer_som(self):
#         return "Som genérico"

# class Pato(Animal, VoadorMixin):
#     def fazer_som(self):
#         return f"{super().fazer_som()} - Quack!"

# pato = Pato()
# print(pato.fazer_som())  # Saída: Som genérico - Quack!
# print(pato.voar())       # Saída: Estou voando!


# Esses exemplos ilustram diferentes maneiras de usar a função super() em Python para aproveitar a funcionalidade das superclasses e garantir uma estrutura de herança eficaz e modular.

# Em todos esses exemplos, super().fazer_som() é chamado diretamente no retorno do método, sem atribuição a uma variável intermediária. Isso funciona bem e é perfeitamente válido em Python. A escolha de usar ou não uma variável para armazenar super() depende da preferência pessoal e da legibilidade do código em questão.
