# os + shutil - Copiando arquivos com Python
# Vamos copiar arquivos de uma pasta para outra.
# Copiar -> shutil.copy
import os
import shutil
from itertools import count

HOME = os.path.expanduser('~')
ONEDRIVE = os.path.join(HOME, 'OneDrive', 'Documentos')
PASTA_ORIGINAL = os.path.join(ONEDRIVE, 'EXEMPLO')
NOVA_PASTA = os.path.join(ONEDRIVE, 'NOVA_PASTA')
print(NOVA_PASTA)

os.makedirs(NOVA_PASTA, exist_ok=True)
counter = count()
for root, dirs, files in os.walk(PASTA_ORIGINAL):
    the_counter = next(counter)
    for dir_ in dirs:
        caminho_novo_diretorio = os.path.join(root.replace(PASTA_ORIGINAL, NOVA_PASTA), dir_)
        os.makedirs(caminho_novo_diretorio, exist_ok=True)
        print(the_counter,'diretorios',caminho_novo_diretorio)

    for file in files:
       caminho_arquivo = os.path.join(root, file)
       caminho_novo_arquivo = os.path.join(root.replace(PASTA_ORIGINAL, NOVA_PASTA), file)
       print(the_counter,'files',caminho_novo_arquivo)
       shutil.copy(caminho_arquivo, caminho_novo_arquivo)
       

#####################################################################################################
# (os.path.expanduser) é uma função que se tiver um ('~') como parametro retorna o home do usuario
# (os.makedirs) cria uma pasta/diretorio no python e recebe como parametro um caminho, e para não der erro ao tentar
# criar uma pasta que ja existe voce pode usar o parametro nomeado (exist_ok=) 
# O modulo (shutil) tem uma função (copy) que copia o arquivo passado como parametro
