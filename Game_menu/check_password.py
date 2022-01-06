# Функция удовлетворения пароля при регистрации
# Принимает на вход пароль
# Возвращает кортеж, True or False если удалось создать или нет, если нет то какая ошибка

def check_password(password):
    if len(password) < 8:
        return (False, "Длина пароля должна быть больше 8 символов")

    if not (password != password.lower() and password != password.upper()):
        return (False, "В пароле отсутсвуют присутствуют большие и маленькие буквы любого алфавита.")

    if not (any([x.isdigit() for x in password])):
        return (False, "Пароль должен содержать цифры")

    return (True, None)