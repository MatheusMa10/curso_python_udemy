# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela
class Carro:
    def __init__(self, nome):
        self.nome = nome
        self.motor = None
        self.fabricante = None

    def inserir_motor(self, motor):
        if self.motor != None:
            return
        self.motor = Motor(motor)

    def inserir_fabricante(self, fabricante):
        if self.fabricante != None:
            return
        self.fabricante = Fabricante(fabricante)
    
    def mostrar_motor(self):
        print(self.motor.nome)

    def mostrar_fabricante(self):
        print(self.fabricante.nome)


class Motor:
    def __init__(self, nome):
        self.nome = nome


class Fabricante:
    def __init__(self, nome):
        self.nome = nome

carro1 = Carro('fox')
print(carro1.nome)
carro1.inserir_motor('V8')
carro1.mostrar_motor()
carro1.inserir_fabricante('Volkswagen')
carro1.mostrar_fabricante()

print()

carro2 = Carro('civic')
print(carro2.nome)
carro2.inserir_motor('4.0')
carro2.mostrar_motor()
carro2.inserir_fabricante('chevrolet')
carro2.mostrar_fabricante()