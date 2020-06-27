import sqlite3


def connect_to_db(path_to_db):
    connection = None
    if (path_to_db):
        try:
            connection = sqlite3.connect(
                'file:' + path_to_db + '?mode=rw', uri=True)
            # connection = sqlite3.connect(path_to_db)
        except:
            return None
        else:
            c = connection.cursor()
            return {"conn": connection, "cursor": c}

    return connection


def wrapper():
    # он должен в себе содержать:
    # ввод с клавиатуры или получения из другого источника логина и пароля
    print("Login: ")
    log = input()
    print("Password: ")
    pwd = input()
    table = 'users'
    # получение из БД пользователя с тем логином, который был введен
    # сверка пароля введенного пользователем с паролем, хранящемся в БД
    users = get_users_from_table(conn, table)
    for user in users:
      if user[0] == log and user[1] == pwd:
        private_zone_area()
        return
    # если успех и аутентификация прошла успешно, показываем private_zone_area
    else:
        print("No such user")
    # если нет, то показать надпись пользователю о том, пользователя с таким паролем - нет
    


def private_zone_area():
    print("private_zone_area")

    return "private_zone_area"


def get_users_from_table(conn, table):
    sql_query = "SELECT * FROM " + str(table)
    cursor = conn.cursor()
    res = cursor.execute(sql_query)
    users_lst = res.fetchall()

    # print(users_lst) to test with a user

    return users_lst


conn_dict = connect_to_db('example.db')
conn, cur = conn_dict["conn"], conn_dict["cursor"]
wrapper()

