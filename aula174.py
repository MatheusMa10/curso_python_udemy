# os + shutil - Apagando, copiando, movendo e renomeando pastas com Python
# Vamos copiar arquivos de uma pasta para outra.
# Copiar -> shutil.copy
# Copiar Árvore recursivamente -> shutil.copytree
# Apagar Árvore recursivamente -> shutil.rmtree
# Apagar arquivos -> os.unlink
# Renomear/Mover -> shutil.move ou os.rename
import os
import shutil

HOME = os.path.expanduser('~')
ONEDRIVE = os.path.join(HOME, 'OneDrive', 'Documentos')
PASTA_ORIGINAL = os.path.join(ONEDRIVE, 'EXEMPLO')
NOVA_PASTA = os.path.join(ONEDRIVE, 'NOVA_PASTA')

shutil.rmtree(NOVA_PASTA, ignore_errors=True)
shutil.copytree(PASTA_ORIGINAL, NOVA_PASTA)
shutil.move(NOVA_PASTA, NOVA_PASTA + '_EITA')

# os.makedirs(NOVA_PASTA, exist_ok=True)

# for root, dirs, files in os.walk(PASTA_ORIGINAL):
#     for dir_ in dirs:
#         caminho_novo_diretorio = os.path.join(root.replace(PASTA_ORIGINAL, NOVA_PASTA), dir_)
#         os.makedirs(caminho_novo_diretorio, exist_ok=True)

#     for file in files:
#        caminho_arquivo = os.path.join(root, file)
#        caminho_novo_arquivo = os.path.join(root.replace(PASTA_ORIGINAL, NOVA_PASTA), file)
#        print(caminho_novo_arquivo)
#        shutil.copy(caminho_arquivo, caminho_novo_arquivo)

##########################################################################################################
# (shutil.rmtree) é uma função que apaga toda a arvore da pasta/arquivo escolhido
# (shutil.move) é uma função que permite mudar o caminho da pasta/arquivo ou mudar o nome da pasta/arquivo passando no primeiro parametro a pasta atual e no segundo a mudança
# (shutil.copytree) é uma função em python que copia toda a arvore da primeira pasta passada no parametro e manda para a pasta que esta no segundo parametro