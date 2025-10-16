# Encapsulamento (modificadores de acesso: public, protected, private)
# Python NÃO TEM modificadores de acesso
# Mas podemos seguir as seguintes convenções
#   (sem underline) = public
#       pode ser usado em qualquer lugar
# _ (um underline) = protected
#       não DEVE ser usado fora da classe
#       ou suas subclasses.
# __ (dois underlines) = private
#       "name mangling" (desfiguração de nomes) em Python
#       _NomeClasse__nome_attr_ou_method
#       só DEVE ser usado na classe em que foi
#       declarado.
from functools import partial

class Foo:
    def __init__(self):
        self.public = 'isso é publico'
        self._protected = 'isso é protegido'
        self.__private = 'isso é privado'
    
    def metodo_publico(self):
        # self._metodo_protected()
        # print(self._protected)
        self.__metodo_private()
        print(self.__private)
        return 'metodo_publico'
    
    def _metodo_protected(self):
        print('_metodo_protected')
        return '_metodo_protected'
    
    def __metodo_private(self):
        print('__metodo_private')
        return '__metodo_private'
    
# Não podemos usar metodos nem atributos protected que são metodos e atributos que começam com underline('_'), mas podemos
# usar em qualquer lugar da classe e das subclasses assim como no exemplo acima
    
# O metodo e o atributo private eles sempre começam com dois underline('__') e eles só podem serem usados na classe não
# podem serem usados em subclasses nem fora delas

f = Foo()
# print(f._protected)
# print(f._metodo_protected())
# print(f.public)
print(f.metodo_publico())
# print(f._Foo__metodo_private()) # não recomendado porque um metodo private não é para ser chamado fora da classe
