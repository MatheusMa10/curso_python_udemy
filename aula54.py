print('Selecione uma opção')
lista_compras = []

while True:     
    opição = input('[i]nserir, [a]pagar, [l]istar: ').lower().strip()[0]
    if opição == 'i':
        colocando = input('Oque vc deseja inserir? ')
        lista_compras.append(colocando)
    elif opição == 'a':
        indice = int(input('Escolha o indice para apagar: '))
        if indice not in range(0,len(lista_compras)):
            print('Não tem esse indice')
            continue
        else:
            del lista_compras[indice]
    elif opição == 'l':
        for indice, item in enumerate(lista_compras):
            print(indice, item)
    else:
        print('Não temos essa opição tente denovo!')

# Eu poderia ter usado esse código abaixo no lugar do if dentro da opição 'a' ele lidaria com qualquer erro
"""
try:
            indice_ex = int(indice)
            del lista[indice]
        except ValueError:
            print('Por favor digite número int.')
        except IndexError:
            print('Índice não existe na lista')
        except Exception:
            print('Erro desconhecido')
"""
