# Atributos de classe
class Pessoa:
    ano_atual = 2024

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        # self.ano_atual = 100

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade
    
pessoa1 = Pessoa('Matheus', 21)
pessoa2 = Pessoa('Helena', 14)

print(Pessoa.ano_atual)
# Pessoa.ano_atual = 1

print(pessoa1.get_ano_nascimento())
print(pessoa2.get_ano_nascimento())