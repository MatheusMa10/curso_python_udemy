# Problema dos parâmetros mutáveis em funções Python
# def adiciona_clientes(nome, lista=[]):
#     lista.append(nome)
#     return lista

# lista1= []
# cliente1 = adiciona_clientes('luiz',  lista1)
# adiciona_clientes('Joana', cliente1)
# print(cliente1)

# cliente2 = adiciona_clientes('Helena')
# adiciona_clientes('Maria', cliente2)
# print(cliente2)

'''O exemplo acima não é recomendado, porque quando se passa valores mutaveis como parametros padrões para uma função,
sempre que você executar essa função vai ser a mesma lista para todas as chamadas, mas no exemplo acima criamos uma variavel lista1 = [], que serve de parametro para a chamada,, ai vai sempre ser listas diferentes, no entanto ainda não é recomendado fazer isso'''

def adiciona_clientes(nome, lista=None):
    if lista == None:
        lista = []
    lista.append(nome)
    return lista

cliente1 = adiciona_clientes('luiz')
adiciona_clientes('Joana', cliente1)
adiciona_clientes('Fernando', cliente1)
cliente1.append('Edu')

cliente2 = adiciona_clientes('Helena')
adiciona_clientes('Maria', cliente2)

cliente3 = adiciona_clientes('Moreira')
adiciona_clientes('Vivi', cliente3)

print(cliente1)
print(cliente2)
print(cliente3)

'''Já nesse exemplo é melhor, pois o valor do parametro padrao da função recebe None e a função faz uma condicional que se a lista for igual a None a propria função cria uma lista'''