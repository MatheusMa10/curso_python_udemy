# Exercício solucionado: calculando as datas e parcelas de um empréstimo
# Maria pegou um empréstimo de 1.000.000
# para realizar o pagamento em 5 anos.
# A data em que ela pegou o empréstimo foi
# 20/12/2020 e o vencimento de cada parcela
# é no dia 20 de cada mês.
# - Crie a data do empréstimo
# - Crie a data do final do empréstimo
# - Mostre todas as datas de vencimento e o valor de cada parcela

"""Como eu fiz"""


"""
Nessa aula, tinhamos que fazer a conta de quanto alguem teria que pagar em parcelas com base na sua divida, entao eu criei uma variavel onde tinha o valor do emprestimo
criei uma variavel onde tinha a data e o formato usando o metodo(strptime) da classe (datetime)
criei uma variavel onde tinha a data de vencimento do emprestimo usando a variavel de cima mais a classe (relativedelta) com o parametro de anos para somar a data do inicio
criei uma variavel onde tinha a data em meses do tempo do emprestimo pegando uma data com o atributo (year) e subtriando da outra data tambem com o atributo (year) e multiplicando por 12 que daria o total de meses na diferença das datas

fiz um loop que passa por todos os meses, e cada vez que passa pelo loop a data inicial recebe ela mesma mais a classe (relativedelta) usando o parametro (months=1) para adicionar um mes todas as vezes e mostrei todas as saidas de pagamentos mes por mes e mostrei o valor pago usando a variavel do emprestimo dividido pelos meses 

"""

from datetime import datetime
from dateutil.relativedelta import relativedelta

emprestimo_maria = 1000000
data_pegou_emprestimo = datetime.strptime('20/12/2020', '%d/%m/%Y')
data_pagou_divida = data_pegou_emprestimo + relativedelta(years=5)
data_em_meses = (data_pagou_divida.year - data_pegou_emprestimo.year) * 12

for i, meses in enumerate(range(data_em_meses)):
    data_pegou_emprestimo += relativedelta(months=1)
    print(i, data_pegou_emprestimo, emprestimo_maria / data_em_meses)

"""Como o professor fez"""

# valor_total = 1_000_000
# data_emprestimo = datetime(2020, 12, 20)
# delta_anos = relativedelta(years=5)
# data_final = data_emprestimo + delta_anos

# data_parcelas = []
# data_parcela = data_emprestimo
# while data_parcela < data_final:
#     data_parcelas.append(data_parcela)
#     data_parcela += relativedelta(months=+1)

# numero_parcelas = len(data_parcelas)
# valor_parcela = valor_total / numero_parcelas

# for data in data_parcelas:
#     print(data.strftime('%d/%m/%Y'), f'R$ {valor_parcela:,.2f}')

# print()
# print(
#     f'Você pegou R$ {valor_total:,.2f} para pagar '
#     f'em {delta_anos.years} anos '
#     f'({numero_parcelas} meses) em parcelas de '
#     f'R$ {valor_parcela:,.2f}.'
# )
