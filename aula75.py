# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.
# def duplicar(numero):
#     return numero * 2


# def triplicar(numero):
#     return numero * 3


# def quadruplicar(numero):
#     return numero * 4
# def Criar_multiplicador(multiplicador):
#     def Multiplicar(numero):
#         return numero * multiplicador
#     return Multiplicar

# duplicar = Criar_multiplicador(2)
# triplicar = Criar_multiplicador(3)
# quadruplicar = Criar_multiplicador(4)

# print(duplicar(2))
# print(triplicar(2))
# print(quadruplicar(2))

def criar_expoente(x):
    def expoentado(y):
        return y ** x
    return expoentado

expoente_2 = criar_expoente(2)
expoente_3 = criar_expoente(3)
expoente_4 = criar_expoente(4)

for numero in [9, 10, 5, 2]:
    print(expoente_2(numero), expoente_3(numero), expoente_4(numero))