# os.listdir para navegar em caminhos
# /Users/luizotavio/Desktop/EXEMPLO
# C:\Users\luizotavio\Desktop\EXEMPLO
# caminho = r'C:\\Users\\luizotavio\\Desktop\\EXEMPLO'
# C:
import os
caminho = os.path.join('\\Users', 'Matheus', 'OneDrive', 'Documentos', 'EXEMPLO')

for pasta in os.listdir(caminho):
    caminho_completo_pasta = os.path.join(caminho, pasta)
    print(pasta)
    if not os.path.isdir(caminho_completo_pasta):
        continue

    for item in os.listdir(caminho_completo_pasta):
        print('  ', item)

# print(os.listdir(caminho))


################################################################################################################
# (os.isdir) é uma função que retorna se é ou não é um diretorio
# (os.listdir) é uma função que retorna todos os items do caminho, mas só a primeira camada, entao se tiver outra pasta
# teria que passar por ela tambem com um loop dentro de outro loop
