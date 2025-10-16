# Funções recursivas e recursividade
# - funções que podem se chamar de volta
# - úteis p/ dividir problemas grandes em partes menores
# Toda função recursiva deve ter:
# - Um problema que possa ser dividido em partes menores
# - Um caso recursivo que resolve o pequeno problema
# - Um caso base que para a recursão
# - fatorial - n! = 5! = 5 * 4 * 3 * 2 * 1 = 120
# https://brasilescola.uol.com.br/matematica/fatorial.html

# import sys

# sys.setrecursionlimit(1004)

# def recursiva(inicio=0, fim=10):
#     # Caso base
#     if inicio >= fim:
#         return fim
#     print(inicio, fim)
#     # Caso recursivo
#     # contar até chegar no final
#     inicio += 1
#     return recursiva(inicio, fim)

# print(recursiva())

def factiorial(n):
    if n <= 1:
        return 1
    
    return n * factiorial(n-1)

print(factiorial(5))
print(factiorial(10))
print(factiorial(100))
# print(factiorial(1000))
# Função recusiva tem limite de 1000 execuções em python
