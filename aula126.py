# __dict__ e vars para atributos de instância
class Pessoa:
    ano_atual = 2024

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        # self.ano_atual = 100

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade
    
dados = {'nome':'Matheus', 'idade': 21}
pessoa1 = Pessoa(**dados)
# pessoa1.nome = 'sla'
# del pessoa1.nome
# print(pessoa1.nome)
# pessoa1.__dict__['outra'] = 'coisa'
# pessoa1.__dict__['nome'] = 'eita'
# del pessoa1.__dict__['nome']
# print(pessoa1.__dict__)
# print(vars(pessoa1))
# print(pessoa1.outra)
print(vars(pessoa1))
print(pessoa1.nome)
