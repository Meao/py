import sqlite3
"""
https://repl.it/@MarinaKrvtsn/sem4-t1-lr3#main.py containts db

Разработать фрагмент программы, сериализующей вводимые пользователем данные, в базе данных sqlite (использовать модуль sqlite3) с использованием расширенного синтаксиса исключений."""
# Рефакторинг добавления данных (insert_param_data)
# Добавить код, который реализует: 
# параметризованное удаление данных (DELETE),
# обновление (изменение) данных (UPDATE), 
# выборку (извлечение) данных из таблицы stocks (SELECT)
# Добавить обработку исключительных ситуаций

def connect_to_db(path_to_db):

    connection = None
    if (path_to_db):
        try:
            # connection = sqlite3.connect(
                # 'file:' + path_to_db + '?mode=rw', uri=True)
            connection = sqlite3.connect(path_to_db)
        except:
            return None
        else:
            c = connection.cursor()
            return {"conn": connection, "cursor": c}

    return connection


def create_table(table_name, domens_lst, conn):
    # проверяем есть ли conn
    # если нет, падаем / возвращаем None
    # если есть соединение, проверить есть ли таблица, если есть, то все ок и создавать не надо
    # если нет, то создадим и вернем какой-то код, если все хорошо

    # проверить есть ли таблица: попытаться создать таблицу и проанализировать ответ, если он "table 'table_name' already exists".
    try:
      sql_query = '''CREATE TABLE stocks
                (date text, trans text, symbol text, qty real, price real)'''
      
      cur.execute(sql_query)

    except sqlite3.OperationalError as e:
      e_str = str(e)

      if ("already exists" in e_str):
        sql_query_lst = sql_query.split()
        print(f' NOTICE: {e}. CONTINUE ')
    finally:
      pass
      # добавляем первоначальные данные, если таблица 
