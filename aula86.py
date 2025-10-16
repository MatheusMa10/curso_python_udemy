produto = {
    'nome': 'Caneta Azul',
    'preço': 2.5,
    'categoria': 'Escritorio'
}

dc = {
    # chave: valor.upper()
    # if isinstance(valor, str) else valor
    chave: valor 
    if isinstance(valor, (int, float)) else valor.upper()
    for chave, valor
    in produto.items() 
    if chave != 'categoria'
}

lista = [
    ('a', 'valor a'),
    ('b', 'valor b'),
    ('c', 'valor c'),
]

dc = {
    chave: valor
    for chave, valor in lista
}

s1 = {2 ** i for i in range(10)}
print(s1)

# print(set(range(10)))
# print(dict(lista))