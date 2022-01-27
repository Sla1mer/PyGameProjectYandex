import hashlib
import sqlite3 as sq

import pyautogui
import pygame

import test_menu
from check_password import check_password
from draw_text import draw_text
from threading import Thread
from disable_button_auth import set_is_login, get_is_login
from Settings import set_login


# Регистрация пользователя
def reg(login, password, screen, width, height):
    if check_password(password)[0]:
        try:
            with sq.connect("users.db") as db:
                cur = db.cursor()
                cur.execute("INSERT INTO users (login, password) VALUES (?, ?)",
                            (login, hashlib.sha256(password.lower().encode("utf-8")).hexdigest()))
                db.commit()
                set_is_login(not get_is_login())
                set_login(login)
                # Здесь происходит двойной щелчок по левой кнопке мышки, что бы очистить группу спрайтов от ненужных
                # кнопок
                pyautogui.click(pygame.mouse.get_pos())
                pyautogui.click(pygame.mouse.get_pos())
                return (True, None)
        except:
            return (False, 'Логин уже существует')
    else:
        print(check_password(password)[1])


# Авторизация пользователя, возвращает True если удачна, False если нет
def autho(login, password):
    with sq.connect("users.db") as db:
        cur = db.cursor()
        query = 'SELECT password FROM USERS WHERE login = ? '
        cur.execute(query, (login.lower(),))
        try:
            if cur.fetchall()[0][0] == \
                    hashlib.sha256(password.lower().encode("utf-8")).hexdigest():
                print('ok')
                set_login(login)
                if not get_is_login():
                    set_is_login(not get_is_login())
                # Здесь происходит двойной щелчок по левой кнопке мышки, что бы очистить группу спрайтов от ненужных
                # кнопок
                pyautogui.click(pygame.mouse.get_pos())
                pyautogui.click(pygame.mouse.get_pos())
                return True
        except IndexError:
            return False
