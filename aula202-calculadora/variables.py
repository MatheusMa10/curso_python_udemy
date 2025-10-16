"""Documento onde definimos variaveis que vamos usar e não vão ser mudadas, para não ficar tudo em um arquivo e perder a organização"""

from pathlib import Path

ROOT_DIR = Path(__file__).parent
FILES_DIR = ROOT_DIR / 'files'
ICON_PATH = FILES_DIR / 'icone.png'


# Sizing

BIG_FONT_SIZE = 40
MEDIUM_FONT_SIZE = 24
SMALL_FONT_SIZE = 18
TEXT_MARGIN = 15
MINIMUM_WIDTH = 600