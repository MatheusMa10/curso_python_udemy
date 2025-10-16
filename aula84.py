# Introdução à List comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis.
# print(list(range(10)))
import pprint

def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)

lista = []
for numero in range(10):
    lista.append(numero)
# print(lista)

lista = [
    numero * 2
    for numero in range(10)
]
#print(lista)

# Mapeamento de dados em list comprehension
# Mapeamento é basicamente, eu ter uma lista e eu quero gerar uma lista talvez mudando os dados mas tendo o mesmo tamanho.
produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
]

#print(novos_produtos)
#print(*novos_produtos, sep='\n')
#p(novos_produtos)
#lista = [n for n in range(10) if n < 5]

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    # O que vem a esquerda do 'for' é mapeamento
    for produto in produtos
    # O que vem a direita do 'for' é filtro
    if produto['preco'] > 10
    ]
p(novos_produtos)
