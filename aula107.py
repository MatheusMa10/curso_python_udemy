# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

# def unir_listas(estados, siglas):
#     estados_completos = []
#     n = 0
#     for estado in estados:
#         junto = estado, siglas[n]
#         estados_completos.append(junto)
#         n += 1
#     return estados_completos

# estados = ['Salvador', 'Ubatuba', 'Belo Horizonte']
# siglas_dos_estados = ['BA', 'SP', 'MG', 'RJ']

# lista = unir_listas(estados, siglas_dos_estados)
# print(lista)


'''Fiz como esta acima mas poderia ter feito como esta abaixo'''


# def zipper(lista1, lista2):
#     intervalo = min(len(lista1), len(lista2))
#     return [
#         (lista1[lista], lista2[lista]) for lista in range(intervalo)
#     ]

# lista_1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
# lista_2 = ['BA', 'SP', 'MG', 'RJ']

# print(zipper(lista_1, lista_2))


'''Mas no pyhton tem uma função que ja faz isso'''


# lista_1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
# lista_2 = ['BA', 'SP', 'MG', 'RJ']

# print(list(zip(lista_1,lista_2)))


'''Mas tambem tem outro modulo com uma função que faz a mesma coisa com o parametro maior'''


from itertools import zip_longest

lista_1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
lista_2 = ['BA', 'SP', 'MG', 'RJ']

print(list(zip(lista_1,lista_2)))
print()
# print(list(zip_longest(lista_1, lista_2)))
print(list(zip_longest(lista_1, lista_2, fillvalue='SEM CIDADE')))
