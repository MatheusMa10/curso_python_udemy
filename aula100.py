# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
# from copy import deepcopy

# def aumeto_preco_porcentagem(preco):
#      return f'{preco + preco / 100 * 10:5.2f}'
    


# produtos = [
#     {'nome': 'Produto 5', 'preco': 10.00},
#     {'nome': 'Produto 1', 'preco': 22.32},
#     {'nome': 'Produto 3', 'preco': 10.11},
#     {'nome': 'Produto 2', 'preco': 105.87},
#     {'nome': 'Produto 4', 'preco': 69.90},
# ]

# novos_produtos = deepcopy(produtos)

# for preco in novos_produtos:
#     preco['preco'] = aumeto_preco_porcentagem(preco['preco'])

# print(produtos)
# print(novos_produtos)


# # Ordene os produtos por nome decrescente (do maior para menor)
# c = sorted(produtos, key=lambda item: item['nome'], reverse=True)
# print(c)
# # Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
# d = deepcopy(c)
# d = sorted(d, key=lambda items: items['nome'])
# print(d)
# # Ordene os produtos por preco crescente (do menor para maior)
# produtos = sorted(produtos, key=lambda item: item['preco'])
# print(produtos)
# # Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
# produtos_ordenados_por_preco = deepcopy(produtos)
# print(produtos_ordenados_por_preco)






'''Poderia ter feito assim'''




# import copy

# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)

# novos_produtos = [
#     {**p, 'preco': round(p['preco'] * 1.1, 2)}
#     for p in copy.deepcopy(produtos)
# ]

# print(*produtos, sep='\n')
# print()
# print(*novos_produtos, sep='\n')

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
# produtos_ordenados_por_nome = sorted(
#     copy.deepcopy(produtos),
#     key=lambda p: p['nome'],
#     reverse=True
# )
# print(*produtos, sep='\n')
# print()
# print(*produtos_ordenados_por_nome, sep='\n')


# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
# produtos_ordenados_por_preco = sorted(
#     copy.deepcopy(produtos),
#     key=lambda p: p['preco']
# )

# # FINAL

# print(*produtos, sep='\n')
# print()
# print(*novos_produtos, sep='\n')
# print()
# print(*produtos_ordenados_por_nome, sep='\n')
# print()
# print(*produtos_ordenados_por_preco, sep='\n')


'''Treinando denovo'''

# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)

from copy import deepcopy
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

novos_produtos = deepcopy(produtos)

for preco in novos_produtos:
    novo_preco = round(preco['preco'] *1.1, 2)
    preco['preco'] = novo_preco
# print(*produtos, sep='\n')
# print()
# print(*novos_produtos, sep='\n')

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

novos_produtos = sorted(novos_produtos, key=lambda produto: produto['nome'], reverse=True)

produtos_ordenados_por_nome = sorted(deepcopy(novos_produtos), key=lambda produto: produto['nome'])
# print(*produtos, sep='\n')
# print()
# print(*produtos_ordenados_por_nome, sep='\n')

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

novos_produtos = sorted(novos_produtos, key=lambda produto: produto['preco'])
produtos_ordenados_por_preco = deepcopy(novos_produtos)
# produtos_ordenados_por_preco = sorted(deepcopy(produtos), key=lambda produto: produto['preco'])
print(*produtos, sep='\n')
print()
print(*produtos_ordenados_por_preco, sep='\n')
