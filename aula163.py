# datetime.timedelta e dateutil.relativetimedelta (calculando datas)
# Docs:
# https://dateutil.readthedocs.io/en/stable/relativedelta.html
# https://docs.python.org/3/library/datetime.html#timedelta-objects
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

fmt = '%d/%m/%Y %H:%M:%S'
data_inicio = datetime.strptime('20/04/1987 09:30:30', fmt)
data_fim = datetime.strptime('12/12/2022 08:20:20', fmt)
# delta = timedelta(days=10, hours=2)
delta = relativedelta(data_fim, data_inicio)
print(delta.days, delta.years)
print(data_fim)
# print(data_fim + relativedelta(seconds=60, minutes=10))
# print(data_fim - delta)
# delta = data_fim -data_inicio
# print(delta.days, delta.seconds, delta.microseconds)
# print(data_fim > data_inicio)
# print(data_fim < data_inicio)
# print(data_fim == data_inicio)

#########################################################################################################
# O modulo (datetime) também tem a classe (timedelta), que retorna a diferença em dias entre duas datas ou, voce pode
# criar um (timedelta) que recebe valores, para voce adicionar ou subtrair de outra data, com os parametros da classe
# O python tambem tem o modulo (dateutil.relativedelta), que tem a classe (relativedelta), que é igual a classe 
# (timedelta), mas é mais completo retornando e recebendo mais parametros nomeados como(years=, months=)