# Enum -> Enumerações
# Enumerações na programação, são usadas em ocasiões onde temos um determinado numero de coisas.
# Enums têm membros e seus valores são constantes.
# Enums em python:
#   - são um conjunto de nomes simbólicos (membros) ligados e valores unicos
#   - podem ser iterados para retornar seus membros canônicos na ordem de definição
# enum.Enum é a superclasse para suas enumerações. Mas também pode ser usada
#   diretamente (mesmo assim, Enums não são classes normais em Python).
# Você poderá usar seu Enum com type annotations, com isinstance e
# outras coisas relacionadas com tipo.
# Para obter dados:
# chave = Classe.chave.name, Classe(valor), Classe['chave']
# valor = Classe.chave.value

import enum

# Direcoes = enum.Enum('Direcoes', ['ESQUERDA', 'DIREITA', 'ACIMA', 'ABAIXO'])
class Direcoes(enum.Enum):
    ESQUERDA = enum.auto()
    DIREITA = enum.auto()
    ACIMA = enum.auto()
    ABAIXO = enum.auto()
    

print(Direcoes(1), Direcoes['ESQUERDA'], Direcoes.ESQUERDA)
print(Direcoes(1).value, Direcoes['ESQUERDA'].name, Direcoes.ESQUERDA.value)


def mover(direcao: Direcoes):
    if not isinstance(direcao, Direcoes):
        raise ValueError('Direção não encontrada')
    print(f'Movendo para {direcao.value}- {direcao.name}')

mover(Direcoes.ESQUERDA)
mover(Direcoes.DIREITA)
mover(Direcoes.ACIMA)
mover(Direcoes.ABAIXO)
# mover('lado')