perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opições': ['1', '2', '3', '4', '5'],
        'Resposta': '4',
    },

    {
        'Pergunta': 'Quanto é 5*5?',
        'Opições': ['25', '55', '10', '51'],
        'Resposta': '25',
    },

    {
        'Pergunta': 'Quanto é 10/2?',
        'Opições': ['4', '5', '6', '7'],
        'Resposta': '5'
    }
]
certas = 0

for pergunta in perguntas:
    print(pergunta['Pergunta'])
    certa = pergunta['Resposta']

    for chave, valor in enumerate(pergunta['Opições']):
        print(f'{chave}) {valor}')

    resposta = input('Digite o valor: ')
    if resposta == certa:
        print('Acertou')
        certas += 1
    else:
        print('Errou')
    print()

print(f'Você acertou {certas} de 3 perguntas.')

'''qtd_acertos = 0
for pergunta in perguntas:
    print('Pergunta:', pergunta['Pergunta'])
    print()

    opcoes = pergunta['Opções']
    for i, opcao in enumerate(opcoes):
        print(f'{i})', opcao)
    print()

    escolha = input('Escolha uma opção: ')

    acertou = False
    escolha_int = None
    qtd_opcoes = len(opcoes)

    if escolha.isdigit():
        escolha_int = int(escolha)

    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qtd_opcoes:
            if opcoes[escolha_int] == pergunta['Resposta']:
                acertou = True

    print()
    if acertou:
        qtd_acertos += 1
        print('Acertou 👍')
    else:
        print('Errou ❌')

    print()


print('Você acertou', qtd_acertos)
print('de', len(perguntas), 'perguntas.')'''   