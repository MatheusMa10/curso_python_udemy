"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.
Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]
=================== resultado
lista_soma  = [2, 4, 6, 8]
"""

# def somando_listas(lista1, lista2):
#     return [
#         lista1[indice] + lista2[indice] for indice in range(min(len(lista1), len(lista2)))
#     ]

# lista_a     = [1, 2, 3, 4, 5, 6, 7]
# lista_b     = [1, 2, 3, 4]

# lista_somada = somando_listas(lista_a, lista_b)
# print(lista_somada)
# print(list(zip(lista_a, lista_b)))


'''Fiz da forma acima mas poderia ter sido das formas abaixo'''

# lista_a     = [1, 2, 3, 4, 5, 6, 7]
# lista_b     = [1, 2, 3, 4]

# lista_somada = []
# # for indice in range( min(len(lista_a), len(lista_b))):
# #     lista_somada.append(lista_a[indice] + lista_b[indice])

# for indice, _ in enumerate(lista_b):
#     lista_somada.append(lista_a[indice] + lista_b[indice])

# print(lista_somada)


'''MAS A MELHOR FORMA DE FAZER ISSO É ESSA'''


from itertools import zip_longest

lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]

lista_soma = [x + y for x, y in zip(lista_a, lista_b)]
print(lista_soma)

lista_a = [10, 2, 3, 4, 5]
lista_b = [12, 2, 3, 6, 50, 60, 70]
 
lista_soma = [x + y for x, y in zip_longest(lista_a, lista_b, fillvalue=0)]
print(lista_soma)