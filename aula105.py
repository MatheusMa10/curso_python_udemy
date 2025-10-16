# Decoradores com parâmetros
# def fabrica_de_decoradores(a, b, c): poderia ser assim para o exemplo mas para não ter que colocar parametros na hora da chamada definimos os parametros com valores padrões None
def fabrica_de_decoradores(a=None, b=None, c=None):
    def fabrica_de_funcoes(func):
        print('Decoradora 1')

        def aninhada(*args, **kwargs):
            print(f'Parâmetros do decorador {a, b, c}')
            print('Aninhada')
            resultado = func(*args, **kwargs)
            return resultado
        return aninhada
    return fabrica_de_funcoes

@fabrica_de_decoradores(1, 2, 3)
def soma(x, y):
    return x + y

decoradora = fabrica_de_decoradores()
multiplica = decoradora(lambda x, y: x * y)

# multiplica = fabrica_de_decoradores(1, 2, 3)(lambda x, y: x * y)

dez_mais_cinco = soma(10, 5)
print(dez_mais_cinco)

dez_vezes_cinco = multiplica(10, 5)
print(dez_vezes_cinco)
