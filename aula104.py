# Funções decoradoras e decoradores
# decorar = Adicionar/ Remover/ Restringir/ Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python
# Usar as funções decoradoras em outras funções.

def criate_function(func):
    def interna(*args, **kwargs):
        print('Vou te decorar')
        for arg in args:
            is_string(arg)
        resultado = func(*args, **kwargs)
        print(f'O seu resultado foi {resultado}')
        print('Ok, agora você foi decorada')
        return resultado
    return interna

@criate_function
def inverte_string(string):
    return string[::-1]

def is_string(param):
    if not isinstance(param, str):
        raise TypeError('param deve ser uma string')

# inverte_string_checando_parametro = criate_function(inverte_string)
invertida = inverte_string('123')
print(invertida)
