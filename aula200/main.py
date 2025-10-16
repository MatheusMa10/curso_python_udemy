# Pillow: redimensionando imagens com Python
# Essa biblioteca é o Photoshop do Python 😂

from PIL import Image
from pathlib import Path

ROOT_FOLDER = Path(__file__).parent
ORIGINAL = ROOT_FOLDER / 'original.jpeg'
NEW_IMAGE = ROOT_FOLDER / 'new.jpeg'

pil_image = Image.open(ORIGINAL) # Abrindo imagem original que vai ser redimencionada, e vendo seus dados
width, height = pil_image.size # Atributo que mostra uma tupla com valores de largura e altura(nessa ordem)
exif = pil_image.info['exif'] # Exif são todas as informações da foto

# width     new_width
# height    new_height
new_width = 640
new_height = round(height * new_width / width) # Calculo para definir o redimensionamento da altura com base na largura

# print(width, height)
# print(new_width, new_height)

new_image = pil_image.resize(size=(new_width, new_height)) # Método que redimenciona a imagem original para uma nova, salvando suas informações na memoria interna do pc

new_image.save(
    NEW_IMAGE,
    optimize=True,
    quality=70,
    exif=exif, 
) # Assim como nos arquivos xlsx voce salva e cria os dados da sua imagem/arquivo
