def Mult(*args):
    '''Função que multiplica todos os numeros'''
    total = 0
    cont = 1
    for arg in args:
        if cont == 1:
            total = 1
        print(total)
        cont += 1
        total *= arg
    return total

def Parouimpar(num):
    if num % 2 == 0:
        return f'O numero {num} é par'
    else:
        return f'O numero {num} é impar'
    
poi = Parouimpar(2)
print(poi)

calc = Mult(2, 3, 45, 5)

print(calc)