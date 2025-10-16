# raise - lançando exceções (erros)
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions

# print(123)
# raise ValueError('Deu erro')
# print(456)


# def divide(n, d):
#     try:
#         return n / d
#     except ZeroDivisionError:
#         print('____')
#         raise

# print(divide(8, 0))


def tratando_erro_nao_aceito_zero(d):
    if d == 0:
        raise ZeroDivisionError('Você esta tentando dividir por 0')
    return True

def tratando_erro_nao_aceito_string(n):
    tipo_n = type(n)
    if not isinstance(n, (float, int)):
        raise TypeError(f'{n} deve ser int ou float'
                        f'\t"{tipo_n.__name__}".enviado')
    return True

def divide(n, d):
    tratando_erro_nao_aceito_zero(d)
    tratando_erro_nao_aceito_string(d)
    tratando_erro_nao_aceito_string(n)
    return n / d

print(divide('8', 1))