import sqlite3 as sq
from  check_password import check_password


# Регистрация пользователя
def reg(login, password):
    if check_password(password)[0]:
        try:
            with sq.connect("users.db") as db:
                cur = db.cursor()
                cur.execute("INSERT INTO users (login, password) VALUES (?, ?)", (login, password))
                db.commit()
                return (True, None)
        except:
            return (False, 'Логин уже существует')
    else:
        check_password(password)

# Авторизация пользователя, возвращает True если удачна, False если нет
def autho(login, password):

    with sq.connect("users.db") as db:
        cur = db.cursor()
        query = 'SELECT password FROM USERS WHERE login = ? '
        cur.execute(query, (login.lower(),))
        try:
            if cur.fetchall()[0][0].lower() == password:
                print('ok')
                return True
        except IndexError:
            return False


