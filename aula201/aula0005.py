# QMainWindow e centralWidget
# -> QApplication (app)
#   -> QMainWindow (window->setCentralWidget)
#       -> CentralWidget (central_widget)
#           -> Layout (layout)
#               -> Widget 1 (botao1)
#               -> Widget 2 (botao2)
#               -> Widget 3 (botao3)
#   -> show
# -> exec
import sys

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QApplication, QPushButton, QGridLayout, QWidget, QMainWindow
# Assim como em programação seguimos uma logica computacional, no pyside6 seguimos um padrão de como construir uma janela
# Esse padrao segue com a criação do app
app = QApplication(sys.argv)

# Agora vem a criação da parte da pagina onde vai ter o conteudo da aplicação, a classe QApplication() é como se fosse a # estrutura de madeira de um painel de pintura, ja a classe QMainWindow() é como se fosse a tela onde voce pinta
window = QMainWindow()

# A classe QWidget() é um widget que dentro da tela vc define como widget central, é como se fosse a margem q fazia na aula de artes
central_widget = QWidget() # Cria um Widget genérico
window.setCentralWidget(central_widget) # Atribuindo o widget genérico como o centro da tela
window.setWindowTitle('Meu Titulo') # Definindo titulo do app

botao = QPushButton('Texto do botão') # Cria o botão e passa o texto do botão
botao.setStyleSheet('font-size: 80px; color: red; background-color: rgba(5,120,50, 0.9)') # Método que define as caracteristicas do botão com CSS

botao2 = QPushButton('Botão 2') # Cria o botão e passa o texto do botão
botao2.setStyleSheet('font-size: 40px; color: blue; background-color: rgba(125,0,0, 0.9)') # Método que define as caracteristicas do botão com CSS

botao3 = QPushButton('Botão 3') # Cria o botão e passa o texto do botão
botao3.setStyleSheet('font-size: 40px; color: blue; background-color: rgba(121,0,0, 0.9)') # Método que define as caracteristicas do botão com CSS

# window.setStyleSheet('background-color: rgba(0,0,0, 0.1);')

layout = QGridLayout() # Cria um layout que recebe outros widget no mesmo layut
central_widget.setLayout(layout) # Atribuindo o layout criado a widget genérica

layout.addWidget(botao, 1, 1, 1, 1) # Adicionando Widget(ferramenta) ao layout do widget genérico
layout.addWidget(botao2, 1, 2, 1 , 1) # Adicionando Widget(ferramenta) ao layout do widget genérico
layout.addWidget(botao3, 2, 1, 1 , 2) # Adicionando Widget(ferramenta) ao layout do widget genérico

@Slot()
def slot_example(status_bar):
    def interna():
        status_bar.showMessage('Mostrar mensagem na barra2')
    return interna

@Slot()
def outro_slot(checked):
    print('Está marcado?', checked)

@Slot()
def terceiro_slot(action):
    def interna():
        outro_slot(action.isChecked())
    return interna

# statusBar
status_bar = window.statusBar() # Criando sua barra de status
status_bar.showMessage('Mostrar mensagem na barra') # Atribuindo o texto da barra de status

# menuBar
menu = window.menuBar() # Criando Barra de menu
primeiro_menu = menu.addMenu('Qualquer coisa') # Adicionando um botão na barra de menu
primeira_acao = primeiro_menu.addAction('Primeira ação') # Adicionando uma ação ao menu
primeira_acao.triggered.connect(slot_example(status_bar)) # type: ignore # Aqui atribuimos uma função a ação e passamos em uma variavel não nomeada para atrasar a função

segunda_acao = primeiro_menu.addAction('Segunda ação') # Adicionando uma ação ao menu
segunda_acao.setCheckable(True)
segunda_acao.toggled.connect(outro_slot) # type: ignore # Aqui atribuimos uma função a ação e passamos em uma variavel não nomeada para atrasar a função
segunda_acao.hovered.connect(terceiro_slot(segunda_acao)) # Usando o atributo hovered que faz algo sempre que passar o mause por cima, nesse caso da segunda ação do menu

botao.clicked.connect(terceiro_slot(segunda_acao)) # Usando o atributo clicked que faz algo sempre que algo for clicado

window.show()
app.exec() # O loop da aplicação