from pathlib import Path
import shutil

caminho_projeto = Path()
print(caminho_projeto.absolute())

caminho_arquivo = Path(__file__)
print(caminho_arquivo)

print(caminho_arquivo.parent.parent)

ideias =  caminho_arquivo.parent / 'ideias'
print(ideias / 'arquivo.txt')

# arquivo = Path.home() / 'OneDrive' / 'arquivo.txt'
# arquivo.touch()
# print(arquivo)
# arquivo.write_text('Olá, Mundo!')
# arquivo.write_text('Olá, Denovo!')
# print(arquivo.read_text())
# arquivo.unlink()

# caminho_arquivo = Path.home() / 'OneDrive' / 'arquivo.txt'
# # with caminho_arquivo.open('a+') as arquivo:
# with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
#     arquivo.write('Uma linha\n')
#     arquivo.write('Outra linha\n')

# print(caminho_arquivo.read_text())

caminho_arquivo = Path.home() / 'OneDrive' / 'arquivo.txt'
caminho_arquivo.touch()
caminho_arquivo.write_text('Olá, Mundo!')
caminho_arquivo.unlink()

caminho_pasta = Path.home() / 'OneDrive' / 'Python é legal'
caminho_pasta.mkdir(exist_ok=True)

subpasta = caminho_pasta / 'Subpasta'
subpasta.mkdir(exist_ok=True)

outro_arquivo = subpasta / 'arquivo.txt'
outro_arquivo.touch()
outro_arquivo.write_text('Oi')

mais_arquivo = caminho_pasta / 'arquivo.txt'
mais_arquivo.touch()
mais_arquivo.write_text('Oi')

# caminho_pasta.rmdir()

files = caminho_pasta / 'files'
files.mkdir(exist_ok=True)

for i in range(10):
    file = files / f'file_{i}.txt'
    file.touch()

    if file.exists():
        file.unlink()
    else:
        file.touch()

    with file.open('a+') as text_file:
        text_file.write('Olá, Mundo\n')
        text_file.write(f'file_{i}.txt')

# shutil.rmtree(caminho_pasta)
def rmtree(root: Path, remove_root=True):
    for file in root.glob('*'):
        if file.is_dir():
            print('DIR: ', file)
            rmtree(file, False)
            file.rmdir()
        else:
            print('FILE: ', file)
            file.unlink()
            
    if remove_root:
        root.rmdir()

rmtree(caminho_pasta)

#########################################################################################################################
# (Path()) é uma classe do pathlib que precisa de uma (string que tenha um caminho) e retorna esse caminho
# (caminho_projeto.absolute()) retorna o caminho absoluto do caminho passado
# (caminho_projeto.parent) atributo da classe que retorna o diretorio pai do arquivo passado
# (caminho_projeto.touch()) é uma função que cria um caminho
# (caminho_arquivo.write_text('Olá, Mundo!')) escreve oque for passado no arquivo
# (caminho_arquivo.unlink()) apaga o arquivo/diretorio
# (Path.home()) retorna o comeco do diretorio
# (caminho_pasta.mkdir(exist_ok=True)) cria uma pasta/arquivo
