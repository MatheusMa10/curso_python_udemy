# Decoradores com parâmetros
# def fabrica_de_decoradores(a, b, c): poderia ser assim para o exemplo mas para não ter que colocar parametros na hora da chamada definimos os parametros com valores padrões None
def parametros_decorador(name):
    def fabrica_de_funcoes(func):
        print('Decorador:', name)

        def sua_nova_funcao(*args, **kwargs):
            resultado = func(*args, **kwargs)
            final = f'{resultado} {name}'
            return final
        return sua_nova_funcao
    return fabrica_de_funcoes

@parametros_decorador('5')
@parametros_decorador('4')
@parametros_decorador('3')
@parametros_decorador('2')
@parametros_decorador('1')
def soma(x, y):
    return x + y

dez_mais_cinco = soma(10, 5)
print(dez_mais_cinco)

