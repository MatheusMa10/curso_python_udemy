# os.path trabalha com caminhos em Windows, Linux e Mac
# Doc: https://docs.python.org/3/library/os.path.html#module-os.path
# os.path é um módulo que fornece funções para trabalhar com caminhos de
# arquivos em Windows, Mac ou Linux sem precisar se preocupar com as diferenças
# entre esses sistemas.
# Exemplos do os.path:
# os.path.join: junta strings em um único caminho. Desse modo,
# os.path.join('pasta1', 'pasta2', 'arquivo.txt') retornaria
# 'pasta1/pasta2/arquivo.txt' no Linux ou Mac, e
# 'pasta1\pasta2\arquivo.txt' no Windows.
# os.path.split: divide um caminho uma tupla (diretório, arquivo).
# Por exemplo, os.path.split('/home/user/arquivo.txt')
# retornaria ('/home/user', 'arquivo.txt').
# os.path.exists: verifica se um caminho especificado existe.
# os.path só trabalha com caminhos de arquivos e não faz nenhuma
# operação de entrada/saída (I/O) com arquivos em si.
import os

caminho = os.path.join('Desktop', 'curso', 'arquivo.txt')
print(caminho)
diretorio, arquivo = os.path.split(caminho)
print(arquivo)
nome_arquivo, extencao_arquivo = os.path.splitext(arquivo)
# print(extencao_arquivo)
# print(os.path.exists('\\Users\\Matheus\\OneDrive\\Documentos\\udemy-python'))
# print(os.path.abspath('.'))
print(os.path.basename(caminho))
print(os.path.basename(diretorio))
print(os.path.dirname(caminho))

######################################################################################################################
# (os.path) mexe com caminhos de arquivos
# (os.path.join) é uma função que voce pode passar o caminho do arquivo que ele vai juntando
# (os.path.split) é uma função que divide o seu caminho em duas partes sendo a primeira no diretorio e a segunda o arquivo
# (os.path.splitext) pega o arquivo e divide o nome da extenção do arquivo
# (os.path.exists) é uma função que retorna se o caminho do arquivo existe ou não
# (os.path.abspath) é uma função que se voce passar como parametro ('.') ela retorna o caminho absoluto desse arquivo
# (os.path.basename) é uma função que retorna o final do seu caminho
# (os.path.dirname) é uma função que retorna o diretorio do caminho
