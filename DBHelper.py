import sqlite3


def get_is_online(login):
    with sqlite3.connect('users.db') as db:
        cur = db.cursor()
        query = f"SELECT is_online FROM users WHERE login = '?'"
        cur.execute(query, (login,))

        print(cur.fetchall()[0])