# Formatando datas do datetime
# datetime.strftime('DATA', 'FORMATO')
# https://docs.python.org/3/library/datetime.html
from datetime import datetime

fmt = 'd/%m/%Y'
# data = datetime(2022, 12, 13, 7, 59, 23)
data = datetime.strptime('2022-12-13 07:59:23', '%Y-%m-%d %H:%M:%S')
print(data.strftime('%d/%m/%Y'))
print(data.strftime('%d/%m/%Y %H:%M'))
print(data.strftime('%d/%m/%Y %H:%M:%S'))
print(data.strftime('%Y'), data.year)
print(data.strftime('%d'), data.day)
print(data.strftime('%m'), data.month)
print(data.strftime('%H'), data.hour)
print(data.strftime('%M'), data.second)
print(data.strftime('%S'), data.minute)

###################################################################################################################
# A classe (datetime) tambem tem o metodo(strftime), que recebe o formato e faz a saida sair assim como voce passou e
# é usado assim como esta acima onde voce cria um (objeto) da classe (datetime) e chama o metodo (strftime) passando o
# formato que voce desejar
