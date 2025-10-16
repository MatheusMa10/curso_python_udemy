# argparse.ArgumentParser para argumentos mais complexos
# Tutorial Oficial:
# https://docs.python.org/pt-br/3/howto/argparse.html
from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument(
    '-b', '--basic',
    help='Mostra"Olá mundo" na tela',
    # type=str, # Tipo do argumento
    metavar='STRING',
    # default='Olá mundo!', # Valor padrão
    required=False,
    action='append' # Recebe o argumento mais de um valor
    # nargs='+' # Recebe mais de um valor
)

parser.add_argument( # Método que recebe valores e adiciona eles
    '-v', '--verbose', # Argumentos passados
    help='Mostra logs', # Fala oque função esta fazendo
    action='store_true' # Essa ação, diferente da de cima que vai atribuindo valores e cria uma lista, essa retorna um valor bool se tiver ou não passado um valor a ele
)
args = parser.parse_args()

if args.basic is None:
    print('Você não passou o valor de basic.')
    print(args.basic)
else:
    print('O valor de basic:', args.basic)
    
print(args.verbose)
