from pathlib import Path
import csv

CAMINHO_CSV = Path(__file__).parent / 'aula180.csv'

lista_clientes = [
    {'Nome': 'Matheus', 'Endereço': 'Av. 1, 22'},
    {'Nome': 'Nubia', 'Endereço': 'Av. 2, 23'},
    {'Nome': 'Mendes', 'Endereço': 'Av. 3, 21'},
]

with open(CAMINHO_CSV, 'w', encoding='utf-8') as arquivo:
    nome_colunas = lista_clientes[0].keys()
    escritor = csv.DictWriter(
        arquivo,
        fieldnames= nome_colunas
    )

    escritor.writeheader()

    for cliente in lista_clientes:
        escritor.writerow(cliente)

# lista_clientes = [
#     ['Luiz Otávio', 'Av 1, 22'],
#     ['João Silva', 'R. 2, "1"'],
#     ['Maria Sol', 'Av B, 3A'],
# ]

# with open(CAMINHO_CSV, 'w', encoding='utf-8') as arquivo:
#     # nome_colunas = lista_clientes[0].keys()
#     nome_colunas = ['Nome', 'Endereço']
#     escritor = csv.writer(arquivo)

#     escritor.writerow(nome_colunas)

#     for cliente in lista_clientes:
#         escritor.writerow(cliente)


###################################################################################################################
# (csv.writer(arquivo)) cria um escritor
# (escritor.writerow(nome_colunas)) faz o escritor escrever uma linnha e recebe o conteudo a ser escrito como parametro
# (csv.DictWriter(arquivo,fieldnames= nome_colunas)) faz um escritor de dicionario
# (escritor.writeheader()) faz o escritor de dicionario escrever o topo da tabela/arquivo