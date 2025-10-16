# Empacotamento e desempacotamento de dicionarios
a, b = 1, 2
a, b = b, a
#print(a, b)

#a, b = pessoa.values()
#print(a, b)

#a, b = pessoa.items()
#print(a, b)

#(a1, a2), (b1, b2) = pessoa.items()
#print(a1, a2)
#print(b1, b2)

#for chave, valor in pessoa.items():
#    print(chave, valor)

pessoa = {
    'nome': 'Aline',
    'Sobrenome': 'Souza',
}

dados_pessoa = {
    'idade': 16,
    'altura': 1.6,
}

#pessoa_completa = {**pessoa, 'chave': 1}
#pessoa_completa = {**pessoa, 'nome': 1}
pessoa_completa = {**pessoa, **dados_pessoa}
print(pessoa)
# args e kwargs
# args (ja vimos)
# kwargs - keyword arguments (argumentos nomeados)
def mostro_argumentos_nomeados(*args, **kWargs):
    print('NÃO NOMEADOS:',  args)

    for chave, valor in kWargs.items():
        print(chave, valor)

#mostro_argumentos_nomeados(1, 2, nome='Joana', qlq=123)
#mostro_argumentos_nomeados(**pessoa_comleta)

configuracoes = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
    'arg4': 4,
}
mostro_argumentos_nomeados(1, 2, **configuracoes)
