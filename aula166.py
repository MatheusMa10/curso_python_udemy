# Usando calendar para calendários e datas
# https://docs.python.org/3/library/calendar.html
# calendar é usado para coisas genéricas de calendários e datas.
# Com calendar, você pode saber coisas como:
# - Qual o último dia do mês (ex.: monthrange)
# - Qual o nome e número do dia de determinada data (ex.: weekday)
# - Criar um calendário em si (ex.: monthcalendar)
# - Trabalhar com coisas específicas de calendários (ex.: calendar, month)
# Por padrão dia da semana começa em 0 até 6
# 0 = segunda-feira | 6 = domingo
import calendar

# print(calendar.calendar(20240))
# print(calendar.month(2024, 4))
# numero_primeiro_dia, ultimo_dia = calendar.monthrange(2024, 4)
# print(list(enumerate(calendar.day_name)))
# print(calendar.day_name[numero_primeiro_dia])
# print(calendar.day_name[calendar.weekday(2024, 4, ultimo_dia)])
# print(calendar.monthcalendar(2024, 4))
# for week in calendar.monthcalendar(2024, 4):
#     print(list(enumerate(week)))
for week in calendar.monthcalendar(2024, 4):
    for days in week:
        if days == 0:
            continue
        print(days)

######################################################################################################################
# O modulo (calendar) tem a função (calendar) que retorna o calendario do ano que voce passar como parametro
# Tambem tem a função (month) que retorna o calendario do mes passando o ano e o mes como parametro
# Tambem tem a função (monthrange) que retorna o numero do dia da semana que representa do primeiro dia do mes e o ultimo # dia do mes passando como parametro o ano e o mes desejado
# Tambem tem o atributo (day_name) que retorna uma lista dos nomes de cada dia da semana
# Tambem tem a função (weekday) que retorna a posição do dia da semana na lista
# Tambem tem a função (minthcalendar) que cria um calendario e precisa dos parametros de ano e mes


