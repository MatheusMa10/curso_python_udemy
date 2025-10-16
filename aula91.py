# def generator(n=0):
#     yield 1 # Pausar
#     print('Continuando...')
#     yield 2 # Pausar
#     print('Mais uma...')
#     yield 3
#     print('Vou terminar')
#     return 'ACABOU'

# gen = generator()

# for  n in gen:
#     print(n)
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))


def generator(n=0, maximum=10):
    while True:
        yield n
        if n >= maximum:
            return
        n+= 1

gen = generator()

for n in gen:
    print(n)