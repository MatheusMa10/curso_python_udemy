lista = []

for x in range(3):
    for y in range(3):
        lista.append((x, y))
#print(lista)

lista = [
    (x, y)
    for x in range(3)
    for y in range(3)
    if x != 0 and y != 0
]

lista2 = [
    lis
    for lis in lista
    if lis != (2, 1)
]
print(lista)
print(lista2)