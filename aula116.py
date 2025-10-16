# Criando arquivos com Python + Context Manager with
# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita), x (para criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load
# caminho = 'aula116.txt' # caso voce queira criar um arquivo.txt na mesma pasta onde esse arquivo esta
caminho_arquivo = 'C:\\Users\\Matheus\\OneDrive\\Documentos\\udemy-python\\'
caminho_arquivo += 'aula116.txt'

'''Primeira parte da aula:'''

# arquivo = open(caminho_arquivo, 'w')
# # 
# arquivo.close()

# with open(caminho_arquivo, 'w') as arquivo:
#     print('Olá mundo')
#     print('Arquivo vai ser fechado')

'''Segunda parte da aula:'''

# with open(caminho_arquivo, 'w') as arquivo:
#     arquivo.write('Linha 1\n')
#     arquivo.write('Linha 2')

# with open(caminho_arquivo, 'w+') as arquivo:
#     print(type(arquivo))
#     arquivo.write('Linha 1\n')
#     arquivo.write('Linha 2\n')
#     arquivo.writelines(
#         ('Linha 3\n', 'Linha 4\n')
#     )
#     arquivo.seek(0, 0)
#     print(arquivo.read())
#     print('Lendo')
#     arquivo.seek(0, 0)
#     print(arquivo.readline(), end='')
#     print(arquivo.readline().strip())
#     print(arquivo.readline().strip())
#     print(arquivo.readline()) # o readline é como se fosse o next() ele le linha por linha cada vez que é chamado

#     print('READLINES')
#     arquivo.seek(0, 0)
#     for linha in arquivo.readlines():
#         print(linha.strip())

# print('#' * 40)

# with open(caminho_arquivo, 'r') as arquivo:
#     print(arquivo.read())

'''Terceira parte da aula:'''

import os

with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
    print(type(arquivo))
    arquivo.write('Atenção\n')
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.writelines(
        ('Linha 3\n', 'Linha 4\n')
    )

# os.unlink(caminho_arquivo)
# os.remove(caminho_arquivo)
# os.rename(caminho_arquivo, 'aula116-2.txt')

# a diferença entre o 'w' e o 'a' é que o 'w' sempre que ele é executado ele apaga tudo do arquivo e escreve oque vc pede
# e o 'a' escreve no final do arquivo sem apagar nada 
    