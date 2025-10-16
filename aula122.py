# Entendendo self em classes Python
# Classe é o molde (sem dados)
# Instância da classe (objeto) - Tem os dados
# Uma classe pode gerar várias instâncias
# Na classe o self é a propria instância
class Carro:
    def __init__(self, nome):
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} esta acelerando...')


fusca = Carro('Fusca')
Carro.acelerar(fusca)
# print(fusca.nome)
fusca.acelerar()

celta = Carro('Celta')
Carro.acelerar(celta)
# print(celta.nome)
celta.acelerar()