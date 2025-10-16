import sys
# Generator expression, Iterables e Iterators em Python
iterable = ['Eu', 'Tenho', '__iter__']
# iterator = iterable.__iter__() #tem __iter__ e __next__
iterator =  iter(iterable)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
lista = [n for n in range(100)]
generator = (n for n in range(100))
print(sys.getsizeof(lista)) 
# Lista salva todos os valores na memoria
print(sys.getsizeof(generator))
# Generator não grava todos os valores ele grava um por vez

print(generator)

# for i in generator:
#     print(i)

#GENERATOR É UM INTERAVEL MAS UM INTERAVEL NÃO É UM GENERATOR