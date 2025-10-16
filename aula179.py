# csv.reader e csv.DictReader
# csv.reader lê o CSV em formato de lista
# csv.DictReader lê o CSV em formato de dicionário
from pathlib import Path
import csv

CAMINHO_ARQUIVO = Path(__file__).parent / 'aula179.csv'
print(CAMINHO_ARQUIVO)

# with open(CAMINHO_ARQUIVO, 'w', encoding='utf-8') as arquivo:
#     arquivo.write('Nome, Idade, Endereço\n')
#     arquivo.write(f'Matheus, {21}, "Rua João Lanhoso, 49"\n')
#     arquivo.write(f'Nubia, {25}, "Av. Do Taboão, 2000"')

with open(CAMINHO_ARQUIVO, 'r', encoding='utf-8')as arquivo:
    # leitor = csv.reader(arquivo)
    leitor = csv.DictReader(arquivo)

    for linha in leitor:
        print(linha)
        print(linha['Nome'], linha['Idade'], linha['Endereço'])

# with open(CAMINHO_ARQUIVO, 'r', encoding='utf-8')as arquivo:
#     leitor = csv.reader(arquivo)

#     for linha in leitor:
#         print(linha)

########################################################################################################
# (csv.reader(arquivo)) le o arquivo .csv e retorna uma lista das linhas do arquivo
# (csv.DictReader(arquivo)) assim como o csv.reader ele le mas nao retorna uma linha ele retorna um dicionario com a primeira linha sendo as chaves dele
