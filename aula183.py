# string.Template para substituir variáveis em textos
# doc: https://docs.python.org/3/library/string.html#template-strings
# Métodos:
# substitute: substitui mas gera erros se faltar chaves
# safe_substitute: substitui sem gerar erros
# Você também pode trocar o delimitador e outras coisas criando uma subclasse
# de template.

import locale
from datetime import datetime
import json
import string
from pathlib import Path

CAMINHO_ARQUIVO = Path(__file__).parent / 'aula183.txt'

locale.setlocale(locale.LC_ALL, '')


def converte_para_brl(numero: float | int) -> str:
    brl = 'R$ ' + locale.currency(val=numero, symbol=False, grouping=True)
    return brl


data = datetime(2024, 4, 22)
dados = dict(
    nome='Matheus',
    valor=converte_para_brl(1_234_456),
    data=data.strftime('%d/%m/%Y'),
    empresa= 'M. M',
    telefone= '55 (11) 953980893',
)

print(json.dumps(dados, indent=2, ensure_ascii=False))

texto = '''
Prezado(a) $nome,

Informamos que sua mensalidade será cobrada no valor de ${valor} no dia $data. Caso deseje cancelar o serviço, entre em contato com a $empresa pelo $telefone.

Atenciosamente,

${empresa},
Abraços
'''

class MyTemplate(string.Template):
    delimiter = '%'

with open(CAMINHO_ARQUIVO, 'r', encoding='utf-8') as arquivo:
    texto = arquivo.read()
    template = MyTemplate(texto)
    print(template.safe_substitute(dados))
# print(template.substitute(dados))

################################################################################################################
# (locale.currency()): faz a conversão de moeda, ela tem um parametro (symbol=True) que define se tem ou não o simbolo da
# moeda e tem um parametro (grouping=True) que define os pontos e virgulas de um numero grande e os centavos
# (texto = arquivo.read()): le o arquivo e guarda o conteudo em uma variavel em formato string
# (string.Template): essa classe pega um arquivo/texto e se alguma palavra tiver o delimitador que assim com as 
# (fstring=f'') ele muda o valor delas assim como no arquivo 'aula183.py' do CAMINHO_ARQUIVO
# (substitute): metodo do template que substitui mas gera erros se faltar chaves
# (safe_substitute): metodo do template que substitui sem gerar erros
