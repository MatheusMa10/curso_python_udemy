import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'customers'

connection = sqlite3.connect(DB_FILE) # Conectando o arquivo que vai ser trabalhado com sqlite3
cursor = connection.cursor() # É quem vai executar as consultas na base de dados

# SQL

# CUIDADO: fazendo delete sem where
cursor.execute(
    f'DELETE FROM {TABLE_NAME}'
)

cursor.execute(
    f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"'
)
connection.commit()

# Cria a tabela
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,' # Não é uma sequencia de coisas, é um indentificador que é autoincrementado
    'name TEXT,'
    'weight REAL'
    ')'
)

connection.commit()

#  Registrar valores nas colunas da tabela
# CUIDADO: sql injection quando o usuario estiver digitando
sql = (
    f'INSERT INTO {TABLE_NAME} (name, weight) '
    'VALUES' 
    '(:nome, :peso)'
)
# cursor.execute(sql, ['Matheus', 1.65])
# cursor.executemany(sql, [['Matheus', 1.65], ['Nubia', 1.59]])
cursor.execute(sql, {'nome': 'Matheus', 'peso': 56})
cursor.executemany(sql, ({'nome': 'Matheus', 'peso': 56}, {'nome': 'Nubia', 'peso': 55}))
connection.commit()
print(sql)

cursor.close() # Vai fechar o cursor
connection.close() # Vai fechar a base de dados
