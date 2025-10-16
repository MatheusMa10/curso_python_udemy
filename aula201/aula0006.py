# Trabalhando com classes e herança no PySide6
import sys

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QApplication, QPushButton, QGridLayout, QWidget, QMainWindow
# Assim como em programação seguimos uma logica computacional, no pyside6 seguimos um padrão de como construir uma janela
# Esse padrao segue com a criação do app

class MyWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        # A classe QWidget() é um widget que dentro da tela vc define como widget central, é como se fosse a margem q fazia na aula de artes
        self.central_widget = QWidget() # Cria um Widget genérico
        self.setCentralWidget(self.central_widget) # Atribuindo o widget genérico como o centro da tela
        self.setWindowTitle('Meu Titulo') # Definindo titulo do app
        

        # Elementos da janela
        self.botao1 = self.make_button('Botão 1') # Cria o botão e passa o texto do botão
        self.botao1.clicked.connect(self.segunda_acao_marcada) # Usando o atributo clicked que faz algo sempre que algo for clicado

        self.botao2 = QPushButton('Botão 2') # Cria o botão e passa o texto do botão
        self.botao2.setStyleSheet('font-size: 40px; color: blue; background-color: green; font-weight: bold;') # Método que define as caracteristicas do botão com CSS

        self.botao3 = QPushButton('Botão 3') # Cria o botão e passa o texto do botão
        self.botao3.setStyleSheet('font-size: 40px; color: green; background-color: yellow; font-weight: bold;') # Método que define as caracteristicas do botão com CSS

        # window.setStyleSheet('background-color: rgba(0,0,0, 0.1);')

        self.grid_layout = QGridLayout() # Cria um layout que recebe outros widget no mesmo layut
        self.central_widget.setLayout(self.grid_layout) # Atribuindo o layout criado a widget genérica

        self.grid_layout.addWidget(self.botao1, 1, 1, 1, 1) # Adicionando Widget(ferramenta) ao layout do widget genérico
        self.grid_layout.addWidget(self.botao2, 1, 2, 1 , 1) # Adicionando Widget(ferramenta) ao layout do widget genérico
        self.grid_layout.addWidget(self.botao3, 2, 1, 1 , 2) # Adicionando Widget(ferramenta) ao layout do widget genérico

        # statusBar
        self.status_bar = self.statusBar() # Criando sua barra de status
        self.status_bar.showMessage('Mostrar mensagem na barra') # Atribuindo o texto da barra de status

        # menuBar
        self.menu = self.menuBar() # Criando Barra de menu
        self.primeiro_menu = self.menu.addMenu('Qualquer coisa') # Adicionando um botão na barra de menu
        self.primeira_acao = self.primeiro_menu.addAction('Primeira ação') # Adicionando uma ação ao menu
        self.primeira_acao.triggered.connect(self.muda_mensagem_da_status_bar) # type: ignore # Aqui atribuimos uma função a ação e passamos em uma variavel não nomeada para atrasar a função

        self.segunda_acao = self.primeiro_menu.addAction('Segunda ação') # Adicionando uma ação ao menu
        self.segunda_acao.setCheckable(True)
        self.segunda_acao.toggled.connect(self.segunda_acao_marcada) # type: ignore # Aqui atribuimos uma função a ação e passamos em uma variavel não nomeada para atrasar a função
        self.segunda_acao.hovered.connect(self.segunda_acao_marcada) # Usando o atributo hovered que faz algo sempre que passar o mause por cima, nesse caso da segunda ação do menu
        
    @Slot()
    def muda_mensagem_da_status_bar(self):
        self.status_bar.showMessage('Mostrar mensagem na barra2')

    @Slot()
    def segunda_acao_marcada(self):
        print('Está marcado?', self.segunda_acao.isChecked())

    def make_button(self, text):
        btn = QPushButton(text)
        btn.setStyleSheet('font-size: 40px; color: yellow; background-color: blue; font-weight: bold;')
        return btn

    
# Agora vem a criação da parte da pagina onde vai ter o conteudo da aplicação, a classe QApplication() é como se fosse a # estrutura de madeira de um painel de pintura, ja a classe QMainWindow() é como se fosse a tela onde voce pinta
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec() # O loop da aplicação
