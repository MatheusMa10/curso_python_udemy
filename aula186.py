import os
import shutil
from pathlib import Path
from zipfile import ZipFile

# Caminhos
CAMINHO_RAIZ = Path(__file__).parent
CAMINHO_ZIP_DIR = CAMINHO_RAIZ / 'aula186_diretorio_zip' # caminho para diretorio/pasta onde tera os arquivos zip
CAMINHO_COMPACTADO = CAMINHO_RAIZ / 'aula186_compactado.zip' # caminho do arquivo (.zip)
CAMINHO_DESCOMPACTADO = CAMINHO_RAIZ / 'aula186_descompactado' # caminho do diretorio/pasta dos arquivos (.txt)

shutil.rmtree(CAMINHO_ZIP_DIR, ignore_errors=True) # apagando diretorio/pasta dos arquivos zip
Path.unlink(CAMINHO_COMPACTADO, missing_ok=True) # apagando arquivos (.zip)
shutil.rmtree(str(CAMINHO_COMPACTADO).replace('.zip', ''), ignore_errors=True) # apagando arqiovos descompactados
shutil.rmtree(CAMINHO_DESCOMPACTADO, ignore_errors=True) # apagando diretorio/pasta dos arquivos (.txt)

# raise Exception()

# Cria o diretório para a aula
CAMINHO_ZIP_DIR.mkdir(exist_ok=True) # criando caminho do diretorio/pasta dos arquivos (.zip)

def criar_arquivos(qtd: int, zip_dir: Path):
    '''função que cria os arquivos (.txt) dentro do diretorio/pasta passado'''
    for i in range(qtd): # loop que passa pelo numeros de vezes passado no parametro da função
        texto = 'arquivo_%s' % i # variaveç que cria um arquivo com numeros diferentes a cada chamada do loop
        with open(zip_dir / f'{texto}.txt', 'w', encoding='utf-8') as arquivo: 
            '''Abrindo cada arquivo do diretorio/pasta e escrevendo seu nome'''
            arquivo.write(texto)

criar_arquivos(10, CAMINHO_ZIP_DIR) # chamando a função

# Criando um zio e adicionando arquivos
with ZipFile(CAMINHO_COMPACTADO, 'w') as zip:
    '''Cria arquivo zip e passa todos os arquivos criado anteriormente para esse arquivo (.zip)'''
    for root, dirs, files in os.walk(CAMINHO_ZIP_DIR):
        for file in files:
            # print(file)
            zip.write(os.path.join(root, file), file)

# Lendo arquivos de um zip
with ZipFile(CAMINHO_COMPACTADO, 'r') as zip:
    '''Lendo todo o arquivo (.zip) e vendo os arquivos que estão dentro'''
    for arquivo in zip.namelist(): # cria uma lista com todos os arquivos dentro do arquivo (.zip)
        print(arquivo)

# Extraindo arquivos de um zip
with ZipFile(CAMINHO_COMPACTADO, 'r') as zip:
    '''Extraindo os arquivos (.zip) e passando para o diretorio/pasta de arquivos descompactado'''
    zip.extractall(CAMINHO_DESCOMPACTADO) # metodo usado para extrair todos os arquivos dentro de um arquivo (.zip)
