# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']

# import os

# def func_listar(tarefas):
#     print('\nTAREFAS:')
#     print(*tarefas, sep='\n')

# tarefas = []
# desfeito = []
# while True:
#     print('\nComandos: listar, desfazer e refazer')
#     tarefa_comando = str(input('Digite uma tarefa ou comando: ')).lower()

#     if tarefa_comando == 'listar': 
#         func_listar(tarefas)

#     elif tarefa_comando == 'desfazer':
#         try:
#             des = tarefas.pop()
#             desfeito.append(des)
#         except:
#             pass
#         func_listar(tarefas)

#     elif tarefa_comando == 'refazer':
#         try:
#             ref = desfeito.pop()
#             tarefas.append(ref)
#         except:
#             pass
#         func_listar(tarefas)

#     elif tarefa_comando == 'clear':
#         os.system('cls')

#     else:
#         tarefas.append(tarefa_comando)
#         func_listar(tarefas)

'''Poderia fazer como no codigo abaixo'''

# import os


# def listar(tarefas):
#     print()
#     if not tarefas:
#         print('Nenhuma tarefa para listar')
#         return

#     print('Tarefas:')
#     for tarefa in tarefas:
#         print(f'\t{tarefa}')
#     print()


# def desfazer(tarefas, tarefas_refazer):
#     print()
#     if not tarefas:
#         print('Nenhuma tarefa para desfazer')
#         return

#     tarefa = tarefas.pop()
#     print(f'{tarefa=} removida da lista de tarefas.')
#     tarefas_refazer.append(tarefa)
#     print()


# def refazer(tarefas, tarefas_refazer):
#     print()
#     if not tarefas_refazer:
#         print('Nenhuma tarefa para refazer')
#         return

#     tarefa = tarefas_refazer.pop()
#     print(f'{tarefa=} adicionada na lista de tarefas.')
#     tarefas.append(tarefa)
#     print()


# def adicionar(tarefa, tarefas):
#     print()
#     tarefa = tarefa.strip()
#     if not tarefa:
#         print('Você não digitou uma tarefa.')
#         return
#     print(f'{tarefa=} adicionada na lista de tarefas.')
#     tarefas.append(tarefa)
#     print()


# tarefas = []
# tarefas_refazer = []

# while True:
#     print('Comandos: listar, desfazer e refazer')
#     tarefa = input('Digite uma tarefa ou comando: ')

#     if tarefa == 'listar':
#         listar(tarefas)
#         continue
#     elif tarefa == 'desfazer':
#         desfazer(tarefas, tarefas_refazer)
#         listar(tarefas)
#         continue
#     elif tarefa == 'refazer':
#         refazer(tarefas, tarefas_refazer)
#         listar(tarefas)
#         continue
#     elif tarefa == 'clear':
#         os.system('clear')
#         continue
#     else:
#         adicionar(tarefa, tarefas)
#         listar(tarefas)
#         continue


'''E tambem existe esse jeito sem colocar muitos if, sempre que pudermos escrever o codigo com menos if é melhor, mas esse codigo pode estar mais complexo de se entender, oque é algo ruim'''

import os


def listar(tarefas):
    print()
    if not tarefas:
        print('Nenhuma tarefa para listar')
        return

    print('Tarefas:')
    for tarefa in tarefas:
        print(f'\t{tarefa}')
    print()


def desfazer(tarefas, tarefas_refazer):
    print()
    if not tarefas:
        print('Nenhuma tarefa para desfazer')
        return

    tarefa = tarefas.pop()
    print(f'{tarefa=} removida da lista de tarefas.')
    tarefas_refazer.append(tarefa)
    print()
    listar(tarefas)


def refazer(tarefas, tarefas_refazer):
    print()
    if not tarefas_refazer:
        print('Nenhuma tarefa para refazer')
        return

    tarefa = tarefas_refazer.pop()
    print(f'{tarefa=} adicionada na lista de tarefas.')
    tarefas.append(tarefa)
    print()
    listar(tarefas)


def adicionar(tarefa, tarefas):
    print()
    tarefa = tarefa.strip()
    if not tarefa:
        print('Você não digitou uma tarefa.')
        return
    print(f'{tarefa=} adicionada na lista de tarefas.')
    tarefas.append(tarefa)
    print()
    listar(tarefas)


tarefas = []
tarefas_refazer = []

while True:
    print('Comandos: listar, desfazer e refazer')
    tarefa = input('Digite uma tarefa ou comando: ')

    comandos = {
        'listar': lambda: listar(tarefas),
        'desfazer': lambda: desfazer(tarefas, tarefas_refazer),
        'refazer': lambda: refazer(tarefas, tarefas_refazer),
        'clear': lambda: os.system('cls'),
        'adicionar': lambda: adicionar(tarefa, tarefas),
    }
    comando = comandos.get(tarefa) if comandos.get(tarefa) is not None else comandos['adicionar']
    comando()

    # if tarefa == 'listar':
    #     listar(tarefas)
    #     continue
    # elif tarefa == 'desfazer':
    #     desfazer(tarefas, tarefas_refazer)
    #     listar(tarefas)
    #     continue
    # elif tarefa == 'refazer':
    #     refazer(tarefas, tarefas_refazer)
    #     listar(tarefas)
    #     continue
    # elif tarefa == 'clear':
    #     os.system('clear')
    #     continue
    # else:
    #     adicionar(tarefa, tarefas)
    #     listar(tarefas)
    #     continue