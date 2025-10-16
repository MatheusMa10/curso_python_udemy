# @property - um getter no modo Pythônico
# getter - um método para obter um atributo
# cor -> get_cor()
# modo pythônico - modo do Python de fazer coisas
# @property é uma propriedade do objeto, ela
# é um método que se comporta como um
# atributo 🤯 🤯 🤯
# Geralmente é usada nas seguintes situações:
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Código cliente - é o código que usa seu código
class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor

    @property
    def cor(self):
        print('PROPERTY')
        return self.cor_tinta
    
    @property
    def cor_tampa(self):
        return 123456


#####################################

caneta = Caneta('Azul')
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor_tampa)

# GETTER É UM METODO QUE EVITA A QUEBRA DE CODIGO POR MUDANÇA DE CODIGO, COMO NO EXEMPLO ACIMA USAMOS @PROPERTY PARA FAZER
# O METODO COR E O METODO COR_TAMPA SEREM TRATADOS PELO USUARIO COMO UM ATRIBUTO NÃO UM METODO, ENTÃO SEMPRE QUE FOR
# CHAMADO OS METODOS NAO VÃO PRECISAR SEREM CHAMADOS ELES SIMPLESMENTE RETORNAM UM VALOR IGUAL OS ATRIBUTOS DE CLASSE


# class Caneta:
#     def __init__(self, cor):
#         self.cor_tinta = cor

#     def get_cor(self):
#         print('GET COR')
#         return self.cor_tinta

# #####################################

# caneta = Caneta('Azul')
# print(caneta.get_cor())
# print(caneta.get_cor())
# print(caneta.get_cor())
# print(caneta.get_cor())
# print(caneta.get_cor())