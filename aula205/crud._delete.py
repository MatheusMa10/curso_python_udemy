import sqlite3
from main import DB_FILE, TABLE_NAME

connention = sqlite3.connect(DB_FILE)
cursor = connention.cursor()

# CRUD - Create Read Update Delete
# SQL - INSERT SELECT UPDATE DELETE

# CUIDADO: fazendo delete sem where
cursor.execute(f'DELETE FROM {TABLE_NAME}')

# DELETE mais cuidadoso
cursor.execute(f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"')
connention.commit()

cursor.close()
connention.close()