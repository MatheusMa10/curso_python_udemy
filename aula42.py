frase = 'O python é uma linguagem de programação multiparadigma Python foi criado por Guido van Rossum.'

i = 0

qtd_letras_que_apareceu = 0
letra_apareceu_mais_vezes = ''
while i < len(frase):
    letra_atual = frase[i]
    qtd_letras_que_apareceu_atual = frase.count(letra_atual)

    if letra_atual == ' ':
        i += 1
        continue
    
    if qtd_letras_que_apareceu < qtd_letras_que_apareceu_atual:
        qtd_letras_que_apareceu = qtd_letras_que_apareceu_atual
        letra_apareceu_mais_vezes = letra_atual
    i += 1
print(f'A letra que apareceu mais vezes foi {letra_apareceu_mais_vezes} e apareceu {qtd_letras_que_apareceu} vezes.')