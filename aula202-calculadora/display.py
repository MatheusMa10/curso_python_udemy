from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLineEdit
from variables import BIG_FONT_SIZE, TEXT_MARGIN, MINIMUM_WIDTH

class Display(QLineEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle() # faz a instancia do metodo de configurações para assim que tiver uma instancia da classe as configurações virem juntas


    def configStyle(self):
        margins = [TEXT_MARGIN for _ in range(4)] # uma lista compreenshion para escrever 4 vzs o conteudo da variavel
        self.setStyleSheet(f'font-size: {BIG_FONT_SIZE}px;') # Passando as configuracoes do layout do aplicativo
        self.setMinimumHeight(BIG_FONT_SIZE * 2) # Definindo tamanho minimo de altura do display
        self.setMinimumWidth(MINIMUM_WIDTH) # Definindo tamanho minimo da largura do display
        self.setAlignment(Qt.AlignmentFlag.AlignRight) # Definindo o alinhamento do display, onde vai ficar oque for escrito, nesse caso fica alinhado na direita do display
        self.setTextMargins(*margins) # Definindo a margem do texto e como tem que passar quatro o tamanho dos 4 lados ja pega os valores da compreenshion