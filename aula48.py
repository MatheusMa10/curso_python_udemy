lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
lista_a.extend(lista_b)
print(lista_a)
print(lista_c)

# Exemplo de copia com duas variaveis oculpando o mesmo espaço na memoria, entao se mudar um muda o outro
lista_d = lista_c

lista_c.append('matheus')
print(lista_c)
print(lista_d)

# Exemplo contrario, quando mudo uma variavel copiada ela não altera a outra
lista_d = lista_c.copy()

lista_d.append("{'nome': matheus,}")
print(lista_c)
print(lista_d)
print(lista_d[-1][2])