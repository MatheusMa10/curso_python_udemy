# QWidget e QLayout de PySide6.QtWidgets
# QWidget -> genérico
# QLayout -> Um widget de layout que recebe outros widgets
import sys

from PySide6.QtWidgets import QApplication, QPushButton, QGridLayout, QWidget

app = QApplication(sys.argv)

botao = QPushButton('Texto do botão') # Cria o botão e passa o texto do botão
botao.setStyleSheet('font-size: 80px; color: red;') # Método que define as caracteristicas do botão com CSS

botao2 = QPushButton('Botão 2') # Cria o botão e passa o texto do botão
botao2.setStyleSheet('font-size: 40px; color: blue;') # Método que define as caracteristicas do botão com CSS

botao3 = QPushButton('Botão 3') # Cria o botão e passa o texto do botão
botao3.setStyleSheet('font-size: 40px; color: blue;') # Método que define as caracteristicas do botão com CSS

central_widget = QWidget() # Cria um Widget genérico

layout = QGridLayout() # Cria um layout que recebe outros widget no mesmo layut
central_widget.setLayout(layout) # Atribuindo o layout criado a widget genérica

layout.addWidget(botao, 1, 1, 1, 1) # Adicionando Widget(ferramenta) ao layout do widget genérico
layout.addWidget(botao2, 1, 2, 1 , 1) # Adicionando Widget(ferramenta) ao layout do widget genérico
layout.addWidget(botao3, 2, 1, 1 , 2) # Adicionando Widget(ferramenta) ao layout do widget genérico

central_widget.show() # Mostrando o widget genérico
app.exec() # O loop da aplicação
