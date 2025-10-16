import sqlite3
from pathlib import Path
from bindings import sql

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
cursor.execute(
    f'INSERT INTO {TABLE_NAME} (id, name, weight)'
    'VALUES' 
    '(NULL, "Matheus Matos", 1.65),'
    '(NULL, "Nubia Silva", 1.59),'
    '(NULL, "Mendes", 1.80)'
)

connection.commit()

if __name__ == '__main__':
    print(sql)

    cursor.execute(
        f'SELECT * FROM {TABLE_NAME}'
    )

    for row in cursor.fetchall():
        _id, name, weight = row
        print(_id, name, weight)

    cursor.execute(f'DELETE FROM {TABLE_NAME} WHERE id = "2"')

    cursor.execute(f'UPDATE {TABLE_NAME} SET name = "QUALQUER" WHERE id = "3"')
    
    connection.commit()

    cursor.close() # Vai fechar o cursor
    connection.close() # Vai fechar a base de dados
