# Exercício - Adiando execução de funções
# def soma(x, y=5):
#     return x + y


# def multiplica(x, y=10):
#     return x * y


# def criar_funcao(funcao, *args):
#     return funcao(*args)


# soma_com_cinco = criar_funcao(soma, 23)
# multiplica_por_dez = criar_funcao(multiplica, 13)
# print(soma_com_cinco)
# print(multiplica_por_dez)


'''Fiz errado era pra fazer como esta abaixo'''


# # Exercício - Adiando execução de funções
# def soma(x, y):
#     return x + y


# def multiplica(x, y):
#     return x * y


# def criar_funcao(funcao, x):
#     def interna(y):
#         return funcao(x, y)
#     return interna


# soma_com_cinco = criar_funcao(soma, 5)
# multiplica_por_dez = criar_funcao(multiplica, 10)

# print(soma_com_cinco(10))
# print(multiplica_por_dez(10))


'''Treinando denovo'''

# Exercício - Adiando execução de funções
def soma(x, y):
    return x + y


def multiplica(x, y):
    return x * y


def criar_funcao(funcao, x):
    def somando(y):
        return funcao(x, y)
    return somando
    
soma_com_cinco = criar_funcao(soma, 5)
print(soma_com_cinco(15))
multiplica_por_dez = criar_funcao(multiplica, 10)
print(multiplica_por_dez(15))
