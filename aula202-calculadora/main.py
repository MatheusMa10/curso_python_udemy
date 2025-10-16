import sys

from variables import ICON_PATH
from info import Info
from main_window import MainWindow
from display import Display
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QLabel
import qdarktheme

def temp_label(texto):
    """Função criada para criar labels de forma mais facil onde so precisa passar oque vai estar escrito nela e depois ela retorna uma label com formato padrão"""
    label1 = QLabel(texto)
    label1.setStyleSheet('font-size: 150px;')
    return label1

if __name__ == '__main__':
    # snake_case
    # PascalCase
    # camelCase

    # Cria aplicação
    app = QApplication(sys.argv) # Criando aplicativo( como se fosse o apoio de madeira do quadro)
    window = MainWindow() # Criando a widget principal(como se fosse o quadro em branco)

    # define o icone
    icone = QIcon(str(ICON_PATH)) # Criando o icone
    window.setWindowIcon(icone) # Definindo icone como icone da widget principal
    app.setWindowIcon(icone) # Definindo icone como icone do aplicativo
    
    # Info
    info = Info('2.0 ^ 10.9 = 1024')
    window.addWidgetToLayout(info)

    # Display
    display = Display('Texto Inicial') # Criando display e passando oque vai estar escrito nele por padrao
    # display.setPlaceholderText('Digite alguma coisa')
    window.addWidgetToLayout(display) # colocando o display no layout do aplicativo
    # window.addWidgetToLayout(Display('Display 2')) # colocando o display no layout do aplicativo
    # window.addWidgetToLayout(Display('Display 3')) # colocando o display no layout do aplicativo

    # Executa tudo
    window.adjustFixedSize() 
    window.show()
    app.exec()