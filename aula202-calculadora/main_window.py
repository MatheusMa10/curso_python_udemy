import sys
from PySide6.QtWidgets import  QMainWindow, QWidget, QVBoxLayout

class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

        # Configurando o layout básico
        self.central_widget = QWidget() # Definindo a widget central(como se fosse a margem do caderno de artes)
        self.vLayout = QVBoxLayout() # Definindo layout em formato vertical 
        self.central_widget.setLayout(self.vLayout) # Definindo que o layout criado acima é da widget central
        self.setCentralWidget(self.central_widget) # Definindo que a widget central acima é da classe MainWindow(como se fosse a tela de pintar em branco) 

        # Título da janela
        self.setWindowTitle("Calculadora") # Definindo o titulo do aplicativo 


    def adjustFixedSize(self):
        """Classe criada para definir um tamanho especifico do aplicativo"""
        # Última coisa a ser feita
        self.adjustSize() # Ajustando o tamanho certo com base nos elementos do aplicativo
        self.setFixedSize(self.width(), self.height()) # Faz com que não de para mudar o tamanho do aplicativo

    def addWidgetToLayout(self, widget: QWidget):
        """Como a instancia de QVBoxLayout foi criada dentro da classe quando quisermos definir uma nova widget a o aplicativo teriamos que caminhar pela classe até adicionar uma nova widget, então por boa pratica definimos esse metodo para fazer isso"""
        self.vLayout.addWidget(widget) # Adicionando nova widget ao layout do aplicativo