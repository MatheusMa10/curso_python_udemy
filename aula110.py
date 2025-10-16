# groupby - agrupando valores (itertools)

from itertools import groupby

alunos = [
    {'nome':'Luiz', 'nota': 'A'},
    {'nome':'Leticia', 'nota': 'B'},
    {'nome': 'Fabricio', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
]

def ordena(aluno):
    return aluno['nota']

alunos_agrupados = sorted(alunos, key= ordena)

grupos = groupby(alunos_agrupados, key= ordena)

for chave, grupo in grupos:
    print(chave)
    for aluno in grupo:
        print(aluno)

# alunos = ['a', 'a', 'a', 'a', 'a', 'b', 'c', 'a',]
# grupos = groupby(sorted(alunos))

# for chave, grupo in grupos:
#     print(chave)
#     print(list(grupo))