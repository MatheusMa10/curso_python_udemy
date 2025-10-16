# Relações entre classes: associação, agregação e composição
# Composição é uma especialização da agregação.
# Mas nela, quando o objeto "pai" for apagado, todas
# as referências dos objetos filhos também são
# apagadas.
class Cliente:
    def __init__(self, nome):
        self.nome =  nome
        self.enderecos = []

    def inserir_endereco(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero))

    def inserir_endereco_externo(self, endereco):
        self.enderecos.append(endereco)

    def listar_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero)
    
    def __del__(self):
        print('APAGANDO', self.nome)


class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero

    def __del__(self):
        print('APAGANDO', self.rua, self.numero)

cliente1 =  Cliente('Maria')
cliente1.inserir_endereco('João Lanhoso', 49)
cliente1.inserir_endereco('Any', 224)
endereco_externo = Endereco('Av Brasil', 123123)
cliente1.inserir_endereco_externo(endereco_externo)
cliente1.listar_enderecos()

del cliente1

print(endereco_externo.rua, endereco_externo.numero)
print('AQUI TERMINA MEU CODIGO')

# A composição diferente da associação e agregação, ela realmente une as duas classes, como no exemplo acima onde a classe
# Cliente recebe uma instancia de Endereço dentro do metodo onde cria um endereço, então se eu apagar a instania cliente1
# da classe Cliente com o metodo __del__ a instancia de endereço também é apagada junto, porque a instancia de Endereco
# foi criada dentro da classe cliente
