# Classes decoradoras (Decorator classes)

# class Multiplicar:
#     def __init__(self, func):
#         self.func = func
#         self.multiplicador = 10

#     def __call__(self, *args, **kwargs):
#         resultado = self.func(*args, **kwargs)
#         return resultado * self.multiplicador


# @Multiplicar
# def soma(x, y):
#     return x * y


# dois_mais_dois = soma(2, 2)
# print(dois_mais_dois)


#################################################################
class Multiplicar:
    def __init__(self, multiplicador):
        self.multiplicador = multiplicador

    def __call__(self, func):
        def interno(*args, **kwargs):
            resultado = func(*args, **kwargs)
            return resultado * self.multiplicador
        return interno


@Multiplicar(10)
def soma(x, y):
    return x * y


dois_mais_dois = soma(2, 2)
print(dois_mais_dois)
