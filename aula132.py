# @property + @setter - getter e setter no modo Pythônico
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Atributos que começar com um ou dois underlines
# não devem ser usados fora da classe.
#  🐍🤓🤯🤯🤯🤯

class Caneta:
    def __init__(self, cor):
        self.cor = cor
        self._cor_tampa = None

# Se o atributo ou o metodo começarem com underline('_') o python esta falando que não é para usalo fora da classe

    @property
    def cor(self):
        print('ESTOU NO GETTER')
        # print('PROPERTY')
        return self._cor
    
    @cor.setter
    def cor(self, valor):
        print('ESTOU NO SETTER')
        # if valor == 'Rosa':
        #     raise ValueError('Não aceitamos esse valor')
        self._cor = valor

    @property
    def cor_tampa(self):
        return self._cor_tampa

    @cor_tampa.setter
    def cor_tampa(self, valor):
        self._cor_tampa = valor

# O METODO SETTER DEFINI UM VALOR VOCE PODE CRIAR OUTRO METODO COM O MESMO NOME APENAS PARA PODER ATRIBUIR UM NOVO VALOR
# USANDO O DECORADOR (@'NOME_DO_METODO_GETTER'.SETTER) E A FUNÇÃO SETTER ALEM DO SELF TEM QUE TER UM PARAMETRO PARA O 
# USARIO PODER DEFINIR OUTRO VALOR AO METODO GETTER ASSIM COMO UM ATRIBUTO NORMAL ONDE VOCE TROCA O VALOR PARA ELE  

# def mostrar(caneta):
#     return caneta.cor
    
caneta = Caneta('Azul')
caneta.cor = 'Rosa'
caneta.cor_tampa = 'Preto'
print(caneta.cor)
print(caneta.cor_tampa)
# print(mostrar(caneta))
