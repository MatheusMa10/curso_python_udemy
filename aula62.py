cpf_enviado_pelo_usuario = '35525780801'
nove_digitos = cpf_enviado_pelo_usuario[:9]
multiplicador_decrescente = 10
resultado = 0

for digito in nove_digitos:
    resultado += int(digito) * multiplicador_decrescente
    multiplicador_decrescente -= 1
digito_1 = resultado * 10 % 11
digito_1 = digito_1 if digito_1 <= 9 else 0
print(digito_1)


dez_digitos = nove_digitos + str(digito_1)
multiplicador_decrescente2 = 11
resultado2 = 0

for digito in dez_digitos:
    resultado2 += int(digito) * multiplicador_decrescente2
    multiplicador_decrescente2 -= 1
digito_2 = resultado2 * 10 % 11
digito_2 = digito_2 if digito_2 <= 9 else 0
print(digito_2)

cpf_gerado_pelo_calculo = f'{dez_digitos}{digito_2}'

if cpf_enviado_pelo_usuario == cpf_gerado_pelo_calculo:
    print(f'{cpf_gerado_pelo_calculo} é valido')
else:
    print('CPF invalido')