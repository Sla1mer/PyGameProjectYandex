import json


def get_volume():
    with open("settings.json") as settings:
        data = json.load(settings)
        return data["volume"]


def get_screen_mode():
    with open("settings.json") as settings:
        data = json.load(settings)
        return data["full_screen"]


def set_volume(volume):
    with open("settings.json") as settings:
        data = json.load(settings)
        data["volume"] = volume

    with open("settings.json", "w", encoding='utf8') as settings:
        settings.write(json.dumps(data))


def set_screen_mode(flag):
    with open("settings.json") as settings:
        data = json.load(settings)
        data["full_screen"] = flag

    with open("settings.json", "w", encoding='utf8') as settings:
        settings.write(json.dumps(data))


def set_login(login):
    with open("settings.json") as settings:
        data = json.load(settings)
        data["login"] = login

    with open("settings.json", "w", encoding='utf8') as settings:
        settings.write(json.dumps(data))


def get_login():
    with open("settings.json") as settings:
        data = json.load(settings)
        return data["login"]
