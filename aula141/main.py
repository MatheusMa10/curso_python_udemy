# from log import LogPrintMixin, LogFileMixin

# log_print = LogPrintMixin()
# log_print.log_error('Qualquer coisa')
# log_print.log_success('Que legal')
# log_file = LogFileMixin()
# log_file.log_error('Qualquer coisa')
# log_file.log_success('Que legal')

from eletronico import Smartphone

galaxy_s = Smartphone('Galaxy S')
iphone = Smartphone('iPhone')

galaxy_s.ligar()
iphone.desligar()

