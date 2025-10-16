# abstractmethod para qualquer método já decorado (@property e setter)
# É possível criar @property @property.setter @classmethod
# @staticmethod e métodos normais como abstratos, para isso
# use @abstractmethod como decorator mais interno.
# Foo - Bar são palavras usadas como placeholder
# para palavras que podem mudar na programação.
from abc import ABC, abstractmethod

class AbstractFoo(ABC):
    def __init__(self, name):
        self._name = False
        self.name = name

    @property
    @abstractmethod
    def name(self):...


class Foo(AbstractFoo):
    def __init__(self, name):
        super().__init__(name)
        # print('Sou inutil')

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name



foo = Foo('Bar')
print(foo.name)


# As classes abstratatas não podem ser implementadas, para implementalas você tera que criar outra classe que tenha 
# herança da classe abstrata e criar um metodo com o mesmo nome e os mesmos parametros do metodo abstrato.

# As vantagens de usar classes abstratas é que você pode reutilizar metodos dela em outras subclasses, sem precisar
# recrialas, e elas teram cada uma sua propria forma de executar os metodos, porque você chamou o metodo inicial da classe
# abstrata e na instancia você deu para cada chamada diferente um valor diferente.

# Não precisa ser apenas no metodo inicial para você colocar o @abstractmethod, você pode colocar em todos os metodos nos 
# quais você queira dar uma função diferente para cada subclasse que instanciar esse metodo abstrato.

# Ex:

# Claro! Vamos criar um exemplo um pouco mais elaborado para demonstrar como as classes abstratas podem ser usadas em um contexto mais complexo. Neste exemplo, vamos criar uma classe abstrata chamada Animal com métodos abstratos para representar comportamentos comuns a todos os animais. Em seguida, criaremos subclasses específicas, como Cachorro e Gato, que herdarão de Animal e implementarão esses comportamentos de maneira específica para cada tipo de animal.

# from abc import ABC, abstractmethod

# class Animal(ABC):
#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade
    
#     @abstractmethod
#     def fazer_som(self):
#         pass
    
#     @abstractmethod
#     def mover(self):
#         pass

# class Cachorro(Animal):
#     def fazer_som(self):
#         return "Au Au!"
    
#     def mover(self):
#         return f"{self.nome} está correndo atrás de uma bola."

# class Gato(Animal):
#     def fazer_som(self):
#         return "Miau!"
    
#     def mover(self):
#         return f"{self.nome} está pulando de um móvel para outro."

# # Criando instâncias de Cachorro e Gato
# meu_cachorro = Cachorro("Rex", 3)
# meu_gato = Gato("Whiskers", 2)

# # Chamando os métodos fazer_som() e mover() para cada animal
# print(f"Meu {meu_cachorro.__class__.__name__} faz: {meu_cachorro.fazer_som()}")
# print(meu_cachorro.mover())

# print(f"Meu {meu_gato.__class__.__name__} faz: {meu_gato.fazer_som()}")
# print(meu_gato.mover())


# Neste exemplo:

# Animal é uma classe abstrata que define dois métodos abstratos: fazer_som() e mover().
# Cachorro e Gato são subclasses de Animal que implementam esses métodos de acordo com o comportamento típico de cada animal.
# Ao criar instâncias de Cachorro e Gato e chamar os métodos fazer_som() e mover(), cada objeto retorna uma mensagem indicando o comportamento específico do animal, demonstrando o polimorfismo em ação.
