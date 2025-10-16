# PyMySQL - um cliente MySQL feito em Python Puro
# Doc: https://pymysql.readthedocs.io/en/latest/
# Pypy: https://pypi.org/project/pymysql/
# GitHub: https://github.com/PyMySQL/PyMySQL
import pymysql
import dotenv
import os
import pymysql.cursors

dotenv.load_dotenv()


connection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE'],
    cursorclass=pymysql.cursors.DictCursor,  
)

TABLE_NAME = 'customers'

with connection:
    with connection.cursor() as cursor:
        # SQL
        cursor.execute(
            F'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ('
            'id INT NOT NULL AUTO_INCREMENT, '
            'nome VARCHAR(50) NOT NULL, '
            'idade INT NOT NULL, '
            'PRIMARY KEY (id)'
            ')'
        )
        # CUIDADO: ISSO LIMPA A TABELA
        cursor.execute(f'TRUNCATE TABLE {TABLE_NAME}')
    connection.commit()
    
    # Começo a manipular dados a partir daqui

    # Inserindo um valor usando placeholder e um iterável
    with connection.cursor() as cursor:
        # cursor.execute(
        #     f'INSERT INTO {TABLE_NAME} '
        #     '(nome, idade) '
        #     'VALUES '
        #     '("Matheus", 22) '
        # )

        sql =(
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade)'
            'VALUES '
            '(%s, %s) '
        )

        data = ('Matheus', 22)

        result = cursor.execute(sql, data)
        # print(sql, data)
        # print(result)
    connection.commit()


    # Inserindo um valor usando placeholder e um dicionário
    with connection.cursor() as cursor:

        sql =(
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade)'
            'VALUES '
            '(%(nome)s, %(idade)s) '
        )

        data2 = {
            "nome": "Le",
            "idade": 27,
        }

        result = cursor.execute(sql, data2)
        # print(sql)
        # print(data2)
        # print(result)
    connection.commit()


    # Inserindo vários valores usando placeholder e uma tupla de dicionários
    with connection.cursor() as cursor:

        sql =(
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade)'
            'VALUES '
            '(%(nome)s, %(idade)s) '
        )

        data3 = (
            {"nome": "Le", "idade": 27},
            {"nome": "Matheus", "idade": 22},
            {"nome": "Rose", "idade": 19},
        )

        result = cursor.executemany(sql, data3)
        # print(sql)
        # print(data3)
        # print(result)
    connection.commit()
    

    # Inseriondo vários valores usando placeholder e uma tupla de tuplas
    with connection.cursor() as cursor:

        sql =(
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade)'
            'VALUES '
            '(%s, %s) '
        )

        data4 = (
            ("Siri", 27),
            ("Helena", 23)
        )

        result = cursor.executemany(sql, data4)
        # print(sql)
        # print(data4)
        # print(result)
    connection.commit()


    # Lendo os valores com SELECT
    with connection.cursor() as cursor:
        # menor_id = int(input('Digite o menor id: '))
        # maior_id = int(input('Digite o maior id: '))
        menor_id = 2
        maior_id = 4
        sql = (
            f'SELECT * FROM {TABLE_NAME} '
            'WHERE id BETWEEN %s AND %s '
        )
        result = cursor.execute(sql, (menor_id, maior_id))
        # print(cursor.mogrify(sql, (menor_id, maior_id)))
        data5 = cursor.fetchall()
        # for row in data5:
        #     print(row)
            
    connection.commit()
    

    # Apagando com DELETE, WHERE e placeholders no PyMySQL
    with connection.cursor() as cursor:
        sql = (
            f'DELETE FROM {TABLE_NAME} '
            'WHERE id = %s'
        )
        cursor.execute(sql, (2))
        connection.commit()
        
        cursor.execute(f'SELECT * FROM {TABLE_NAME} ')

        # for row in cursor.fetchall():
        #     print(row)
            
    # # Editando com UPDATE, WHERE e placeholders no PyMySQL
    # with connection.cursor() as cursor:
    #     sql = (
    #         f'UPDATE {TABLE_NAME} '
    #         'SET nome = %s, idade = %s '
    #         'WHERE id = %s'
    #     )
    #     cursor.execute(sql, ('Linguiça', 32, 4))
    #     cursor.execute(f'SELECT * FROM {TABLE_NAME} ')

    #     # for row in cursor.fetchall():
    #     #     _id, nome, idade = row
    #     #     print(_id, nome, idade)

    #     # data6 = cursor.fetchall()

    #     print('For 1:')
    #     for row in cursor.fetchall_unbuffered(): # Um generator de dicionarios
    #         print(row)

    #         if row['id'] >= 5:
    #             break

    #     print()
    #     print('For 2:')
    #     # cursor.scroll(-2)
    #     # cursor.scroll(1, 'absolute') # Mostra os dados apartir do numero dado
    #     for row in cursor.fetchall_unbuffered():
    #         print(row)

    # connection.commit()
            
    # Editando com UPDATE, WHERE e placeholders no PyMySQL
    with connection.cursor() as cursor:
        sql = (
            f'UPDATE {TABLE_NAME} '
            'SET nome = %s, idade = %s '
            'WHERE id = %s'
        )
        cursor.execute(sql, ('Linguiça', 32, 4))
        cursor.execute(
            f'SELECT id from {TABLE_NAME} ORDER BY id DESC LIMIT 1'
        )

        last_id_from_select = cursor.fetchone()

        result_from_select = cursor.execute(f'SELECT * FROM {TABLE_NAME} ')

        data6 = cursor.fetchall()

        for row in cursor.fetchall():
            print(row)


        print('Result from select ', result_from_select)
        print('len(data6)', len(data6))
        print('rowcount', cursor.rowcount)
        print('lastrowid', cursor.lastrowid)
        print('lastrowid na mão', last_id_from_select['id']) # type: ignore
        print('rownumber', cursor.rownumber)

        cursor.scroll(-2)
        print('rownumber', cursor.rownumber)

    connection.commit()
            