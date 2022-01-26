_is_login = False


def get_is_login():
    return _is_login


def set_is_login(arg):
    global _is_login
    _is_login = arg
