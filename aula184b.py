# Variáveis de ambiente com Python
# Para variáveis de ambiente
# Windows PS: $env:VARIAVEL="VALOR" | dir env:
# Linux e Mac: export NOME_VARIAVEL="VALOR" | echo $VARIAVEL
# Para obter o valor das variáveis de ambiente
# os.getenv ou os.environ['VARIAVEL']
# Para configurar variáveis de ambiente
# os.environ['VARIAVEL'] = 'valor'
# Ou usando python-dotenv e o arquivo .env
# pip install python-dotenv
# from dotenv import load_dotenv
# load_dotenv()
# https://pypi.org/project/python-dotenv/
# OBS.: sempre lembre-se de criar um .env-example
from dotenv import load_dotenv #type: ignore
import os

load_dotenv() # carrega o ambiente do sistema operacional

# print(os.environ) # Nostra todas as variaveis do sistema operacional
user = os.getenv('BD_USER')
print(user, os.getenv('BD_PASSWORD')) # mostra o valor da variavel do ambiente operacional, que nesse caso é 'BD_PASSWORD'

###################################################################################################################

# python-dotenv é uma biblioteca Python que permite que você faça uso de arquivos de configuração para armazenar e acessar as suas variáveis de ambiente de forma mais fácil e segura em seus projetos.

# As variáveis de ambiente são valores que podem ser usados em seu código e que podem variar dependendo do ambiente em que o seu código está sendo executado (por exemplo, o ambiente de produção ou o ambiente de desenvolvimento).
