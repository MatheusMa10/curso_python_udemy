import sqlite3
from main import DB_FILE, TABLE_NAME

connection = sqlite3.connect(DB_FILE) # Conectando o arquivo que vai ser trabalhado com sqlite3
cursor = connection.cursor() # É quem vai executar as consultas na base de dados

# SQL
cursor.execute(f'SELECT * FROM {TABLE_NAME}')

for row in cursor.fetchall():
    _id = row[0]
    name = row[1]
    weight = row[2]
    # _id, name, weight = row
    print(_id, name, weight)

cursor.execute(f'SELECT * FROM {TABLE_NAME} WHERE id = "2"')

row = cursor.fetchone()
_id, name, weight = row
print('\n', _id, name, weight)

cursor.close() # Vai fechar o cursor
connection.close() # Vai fechar a base de dados