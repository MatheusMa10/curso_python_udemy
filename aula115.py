# Ambientes virtuais em Python (venv)
# Um ambiente virtual carrega toda a sua instalação
# do Python para uma pasta no caminho escolhido.
# Ao ativar um ambiente virtual, a instalação do
# ambiente virtual será usada.
# venv é o módulo que vamos usar para
# criar ambientes virtuais.
# Você pode dar o nome que preferir para um
# ambiente virtual, mas os mais comuns são:
# venv env .venv .env
# pip uninstall nome_pacote
# Congelar (ver pacotes)
# pip freeze
#
# Criando e usando um requirements.txt
# pip freeze > requirements.txt
# Instalando tudo do requirements.txt
# pip install -r requirements.txt


# pip install -r .\requirements.txt - comando para instalar um ambiente virtual venv com os mesmos pacotes e bibliotecas
# de um antigo ambiente virtual ou outro

# se você instala algo novo no seu ambiente virtual e queira atualizar o seu .\requeriments.txt voce pode usar o comando
# pip freeze > requeriments.txt

# caso voce queira atualizar o pip voce pode utilizar o comando
# pip install pip --upgrade  ou pode usar esse
# python -m pip install pip --upgrade