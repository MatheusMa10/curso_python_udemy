# locale para internacionalização (tradução)
# https://docs.python.org/3/library/locale.html
# https://learn.microsoft.com/fr-fr/powershell/module/international/get-winsystemlocale?view=windowsserver2022-ps&viewFallbackFrom=win10-ps
import calendar
import locale

# locale.setlocale(locale.LC_ALL, '')
# locale.setlocale(locale.LC_ALL, 'pt_BR')
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

print(calendar.calendar(2024))
print(locale.getlocale())


#####################################################################################################################
# O modulo locale tem a função (setlocale) que recebe os parametros (locais que quer mudar no seu sistema, e a linguagem)
# Tambem tem a função (getlocale) que mostra em qual linguagem seu codigo esta trabalhando
