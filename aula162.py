# Criando datas com módulo datetime
# datetime(ano, mês, dia)
# datetime(ano, mês, dia, horas, minutos, segundos)
# datetime.strptime('DATA', 'FORMATO')
# datetime.now()
# https://pt.wikipedia.org/wiki/Era_Unix
# datetime.fromtimestamp(Unix Timestamp)
# https://docs.python.org/3/library/datetime.html
# Para timezones
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# Instalando o pytz
# pip install pytz types-pytz
from datetime import datetime

# from pytz import timezone

# data = datetime.now(timezone('Asia/Tokyo'))

data = datetime.now()
print(data.timestamp()) # Isso estaria na base de dados
print(data.fromtimestamp(1712742951.206616))
# data_str_data = '2022-04-20 07:49:23'
# data_str_fmt = '%Y-%m-%d %H:%M:%S'

# data = datetime(2022, 4, 20, 7, 49, 23, tzinfo=timezone('Asia/Tokyo'))
# print(data)
# data = datetime.strptime(data_str_data, data_str_fmt)


###############################################################################################
# O modulo datetime é um modulo que retorna uma data e uma hora, assim como o nome diz
# Você pode passar a data, apenas chamando a classe datetime e passando a data desejada
# A classe datetime tem o metodo strptime, que recebe a data e o formato no qual você quer que apareça
###############################################################################################
# E também tem o metodo (now), que retorna o horario atual do seu computador
# O modulo (pytz) tem uma função chamada (timezone), que recebe uma localização e retorna o horario da localização passada
# e qual a diferença de horas da localização normal, e a que foi passada. E a função (timezone) pode ser passada como 
# parametro para o metodo (now) ou do metodo (datetime), usando o parametro nomeado (tzinfo=).
# A classe (datetime) tambem tem o metodo (timestamp), que retorna o tempo atual em segundos e é usado muito em banco de 
# dados, voce pode pegar o valor que ela retorna e passar como parametro para o metodo (fromtimestamp) que ira retornar a
# data atual
