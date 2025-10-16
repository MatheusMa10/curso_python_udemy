# Enviando E-mails SMTP com Python
import os
from dotenv import load_dotenv
from pathlib import Path
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


load_dotenv()


# Caminho arquivo HTML
CAMINHO_HTML = Path(__file__).parent / 'aula185.html'


# Dados do remetente e destinatario
remetente = os.getenv('FROM_EMAIL', '')
destinatario = 'gg2018098@gmail.com'


# Configurações SMTP
smtp_server = 'smtp.gmail.com' # defindo o servidor que vai ser passado as informações que nesse caso é do gmail
smtp_port = 587 # passando a rota do servidor
smtp_username = os.getenv('FROM_EMAIL', '') # passando o email para conseguir logar no meu gmail
smtp_password = os.getenv('EMAIL_PASSWORD', '') # passando senha para conseguir entrar no meu gmail


# Mensagem de texto
with open(CAMINHO_HTML, 'r', encoding='utf-8') as arquivo:
    texto_arquivo =  arquivo.read() # lendo conteudo do arquivo e transformando em uma string
    template = Template(texto_arquivo) # instancia da classe Template para poder mudar as palavras chaves
    texto_email = template.substitute(nome='Matheus') # substituindo uma palavra chave no hard coder (sem criar variavel)


# Transformar nossa mensagem em MIMEMultipart
mime_multipart = MIMEMultipart() # instancia da classe onde passa os requisitos das informações que o gmail pede
mime_multipart['from'] = remetente
mime_multipart['to'] = destinatario
mime_multipart['subject'] = 'Este é o assunto do e-mail'

corpo_email = MIMEText(texto_email, 'html', 'utf-8') # instancia da classe MIMEText que cria o corpo do arquivo, passando como parametro a string que vai ter no email o formato que é HTML e a codificação
mime_multipart.attach(corpo_email) # metodo especifico para incluir partes expecificas do corpo da mensagem


# Envia o e-mail
with smtplib.SMTP(smtp_server, smtp_port) as server: # logando no servidor SMTP passando o servidor e a rota
    server.ehlo() # metodo usado para fazer a primeira comunicação entre o cliente e o servidor
    server.starttls() # faz a comunicação entre cliente e servidor serem seguras e proteger dados simples
    server.login(smtp_username, smtp_password) # faz login usando email e senha
    server.send_message(mime_multipart) # faz o envio da mensagem
    print('E-mail enviado com sucesso!')
