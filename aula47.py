palavra_secreta = 'perfume' # defini uma variavel para a palavra secreta
letra_acertada = '' # defini uma variavel vazia para as letras acertadas
cont = 0 # defini uma variavel contadora de tentativas
while True: # defini um loop infinito enquanto não acertar a palavra secreta
    letra_digitada = input('Digite uma letra: ').lower()[0] 
    cont += 1
    if letra_digitada in palavra_secreta: # defini uma condição testando se a palavra digitada está na palavra secreta
        letra_acertada += letra_digitada # se estiver, a palavra acertada recebe letra digitada
        
    palavra_formada = ''
    for letra in  palavra_secreta: # loop para testar letra por letra da palavra secreta
        if letra in letra_acertada: # teste condicional para saber se cada letra esta na  variavel letra_acertada
            palavra_formada += letra # se for True palavra_formada recebe ela mais letra
        else:
            palavra_formada += '*' # se for False palavra_formada recebe ela mais '*'
    print(palavra_formada)

    if palavra_formada == palavra_secreta:
        print('Você ganhou...')
        break
        
print(palavra_formada)
print(f'Você tentou {cont} vezes')