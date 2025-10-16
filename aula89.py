# dir, hasattr e getattr em python
#dir() vai mostrar todos os metodos dentro da sua variavel
string = 'Luiz carlos'
metodo = 'title'

if hasattr(string, 'upper'):
    print('Existe upper')
    print(string.upper())

if hasattr(string, metodo):
    print('Existe upper')
    print(getattr(string, metodo)())
else:
    print('Não existe o metodo', metodo)