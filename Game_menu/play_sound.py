import os, pygame
from Settings import get_volume

game_volume = get_volume()

# файл отвечает за весь звук в игре, пока это только звуки тыканья по кнопкам
# функция играет звук


def play_sound(filename):
    path = os.path.join('sound', filename)
    button_click = pygame.mixer.Sound(path)
    button_click.set_volume(game_volume)
    button_click.play()


# функция меняет громкость


def change_volume(volume):
    global game_volume
    game_volume += volume
    if game_volume >= 1:
        game_volume = 1
    if game_volume <= 0:
        game_volume = 0
    print(game_volume)


# возвращает текущую громкость


def get_volume():
    return game_volume
