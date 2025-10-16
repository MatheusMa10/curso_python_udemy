# Relações entre classes: associação, agregação e composição
# Agregação é uma forma mais especializada de associação
# entre dois ou mais objetos. Cada objeto terá
# seu ciclo de vida independente.
# Geralmente é uma relação de um para muitos, onde um
# objeto tem um ou muitos objetos.
# Os objetos podem viver separadamente, mas pode
# se tratar de uma relação onde um objeto precisa de
# outro para fazer determinada tarefa.
# (existem controvérsias sobre as definições de agregação).
class Carrinho:
    def __init__(self):
        self._produtos = []

    def total(self):
        return sum([p.preco for p in self._produtos])
    
    def inserir_produtos(self, *produtos):
        # self._produtos.extend(produtos)
        # self._produtos += produtos
        for produto in produtos:
            self._produtos.append(produto)
    
    def listar_produtos(self):
        for produto in self._produtos:
            print(produto.nome, produto.preco)
        print()


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

carrinho = Carrinho()
produto1, produto2 = Produto('Caneta', 1.20), Produto('Camiseta', 20)
carrinho.inserir_produtos(produto1, produto2)
carrinho.listar_produtos()
print(carrinho.total())

# A diferenlça de associação e agregação é que da forma mais simples a associação associa um objeto a outro sem qualquer
# regra então basicamente cada objeto funciona sozinho sem depender do outro
# 
# Ja a agregação ele fala que um objeto tem outro objeto, como no exemplo acima onde os Carrinhos tem Produtos, mas mesmo
# assim cada objeto funciona independentemente, mas a diferença é que um não faz muita coisa sem o outro (PENSA)
