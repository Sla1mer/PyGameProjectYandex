from Settings import get_login
import sqlite3 as sq


def get_statistic(screen, screen_size):
    with sq.connect('users.db') as db:
        cur = db.cursor()
        query = """SELECT * FROM all_user_games WHERE login = ? """
        cur.execute(query, (get_login(),))
        for id, result, date, username in cur.fetchall():
            print(result)
    #     to_parse = cur.fetchall()[0]
    #     id = to_parse[0]
    #     result = to_parse[1]
    #     date = to_parse[2]
    #     name = to_parse[3]
    # print(id, result, date, name)

get_statistic(123, 123)