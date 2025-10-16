# secrets gera números aleatórios seguros
import secrets
# import string as s # modulo string que tem varias funções diferentes de objetos string
# from secrets import SystemRandom as Sr

# print(s.ascii_letters, s.digits, s.punctuation) # pega todos os caracteres que existem em python

# print(''.join(Sr().choices(s.ascii_letters + s.digits + s.punctuation, k=64))) # gerando senha aleatoria segura

random =  secrets.SystemRandom() # classe do modulo secrets que faz as mesmas coisas que o modulo random mas gerando numeros mais seguros e guardando dentro de uma variavel, assim criando um objeto da classe com todas as suas funções 

# print(secrets.randbelow(100)) # gera de forma mais segura que o random um numero aleatorio abaixo do valor dado
# print(secrets.choice([10, 11, 12])) # gera de forma mais segura que o random um valor aleatorio da lista passada


# Funções:
# seed
#   -> Inicializa o gerador de random (por isso "números pseudoaleatórios")
# random.seed(time.time())
# print(time.time())
# random.seed(0)

# random.randrange(início, fim, passo)
#   -> Gera um número inteiro aleatório dentro de um intervalo específico
r_range = random.randrange(10, 20, 2)
# print(r_range)

# random.randint(início, fim)
#   -> Gera um número inteiro aleatório dentro de um intervalo "sem passo"
r_int = random.randint(10, 20)
# print(r_int)

# random.uniform(início, fim)
#   -> Gera um número flutuante aleatório dentro de um intervalo "sem passo"
r_uniform = random.uniform(10, 20)
# print(r_uniform)

# random.shuffle(SequenciaMutável) -> Embaralha a lista original
nomes = ['Luiz', 'Maria', 'Helena', 'Joana']
# random.shuffle(nomes)
# print(nomes)

# random.sample(Iterável, k=N)
#   -> Escolhe elementos do iterável e retorna outro iterável (não repete)
novos_nomes = random.sample(nomes, k=3)
# print(nomes)
# print(novos_nomes)

# random.choices(Iterável, k=N)
#   -> Escolhe elementos do iterável e retorna outro iterável (repete valores)
novos_nomes = random.choices(nomes, k=3)
print(nomes)
print(novos_nomes)

# random.choice(Iterável) -> Escolhe um elemento do iterável
print(random.choice(nomes))