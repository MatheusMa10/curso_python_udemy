# Abstração
# Herança - é um
from pathlib import Path
LOG_FILE = Path(__file__).parent / 'log.txt'
class Log:
    def _log(self, msg):
        raise NotImplementedError('Implemente o método log')
    
    def log_error(self, msg):
        self._log(f'Error: {msg}')

    def log_success(self, msg):
        self._log(f'Success: {msg}')

class LogFileMixin(Log):
    def _log(self, msg):
        msg_formatada = f'{msg} ({self.__class__.__name__})'
        print(f'Salvando no Log {msg}')
        with open(LOG_FILE, 'a', encoding='utf8') as arquivo:
            arquivo.write(msg_formatada)
            arquivo.write('\n')


class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')

if __name__ == '__main__':
    log_print = LogPrintMixin()
    log_print.log_error('Qualquer coisa')
    log_print.log_success('Que legal')
    log_file = LogFileMixin()
    log_file.log_error('Qualquer coisa')
    log_file.log_success('Que legal')
    print(LOG_FILE)
