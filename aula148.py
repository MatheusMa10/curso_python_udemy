# __new__ e __init__ em classes Python
# __new__ é o método responsável por criar e
# retornar o novo objeto. Por isso, new recebe cls.
# __new__ ❗️DEVE retornar o novo objeto❗️
# __init__ é o método responsável por inicializar
# a instância. Por isso, init recebe self.
# __init__ ❗️NÃO DEVE retornar nada (None)❗️
# object é a super classe de uma classe
class A:
    # def __new__(cls):
    #     return object.__new__(A)

    def __new__(cls, *args, **kwargs):
        print('Antes de criar a instancia')
        instancia = super().__new__(cls)
        print('Depois de criar a instancia')
        instancia.x = 213
        return instancia

    def __init__(self, x):
        self.x = x
        print('Sou o init')

    def __repr__(self):
        return 'A()'

a = A(123)
print(a.x)


'''O __new__ é um metodo que cria e retorna uma classe, quase nunca você tera que utilizar, mas quando precisar é nessas horas que você está criando a instancia da classe, onde você queira que apareça algo junto como no codigo acima'''
    



'''Exemplo de como funciona quando você cria a instancia de uma classe'''

# Primeiro você chama o objeto object e atribui o dunder metodo new para criar um novo objeto e como parametro você passa 
# a classe que nesse caso é A, depois você guarda em uma variavel, então chama a variavel com o dunder metodo __init__()

# a = object.__new__(A)
# a.__init__()
# print(a)
