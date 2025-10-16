# os.walk para navegar de caminhos de forma recursiva
# os.walk é uma função que permite percorrer uma estrutura de diretórios de
# maneira recursiva. Ela gera uma sequência de tuplas, onde cada tupla possui
# três elementos: o diretório atual (root), uma lista de subdiretórios (dirs)
# e uma lista dos arquivos do diretório atual (files).
import os
from itertools import count

caminho = os.path.join('\\Users', 'Matheus', 'OneDrive', 'Documentos', 'EXEMPLO')
counter = count()

for root, dirs, files in os.walk(caminho):
    the_counter = next(counter)  
    print(the_counter, 'Pasta atual', root)

    for dir_ in dirs:
        print('    ', the_counter, dir_)
        
        
    for file_ in files:
        caminho_completo_pasta = os.path.join(root, file_)
        print('aaaaaaaaaaaaa', caminho_completo_pasta)
        print('    ', the_counter, caminho_completo_pasta)

        # NÃO FAÇA ISSO, (VAI APAGAR TUDO DA PASTA)
        # os.unlink(caminho_completo_pasta)

# print(list(os.walk(caminho)))

#####################################################################################################################
# (os.walk) é uma função que assim como o (listdir) retorna todos os items dentro da pasta, mas diferente do (listdir) o 
# (walk) mostra todos os arquivos que estao dentro de pastas dentro de outras pastas
# (os.unlink) é uma função que exclui toda a pasta e oque estiver dentro
