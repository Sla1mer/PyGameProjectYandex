from win32api import GetMonitorInfo, MonitorFromPoint

from animation_test import open_chest
from load_img import load_image
from test_gameplay import play
import pygame
import sys
import os, platform
from particle_class import all_parcticles, create_particles
import pyautogui
from play_sound import play_sound, change_volume, game_volume
from button_class import Button
from draw_text import draw_text
from Settings import get_screen_mode

# не используемые импорты не трогать они работают на самом деле!!!!!
from open_doc import open_documentation
from autho_and_reg import autho, reg
import time
import random
import os
from test_settings import options
import webbrowser

width, height = pyautogui.size()
# Инициализация игрового поля
screen_size = (width, height)
mainClock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption('Крутая карточная игра')
if platform.system() == 'Windows':  # Windows
    monitor_info = GetMonitorInfo(MonitorFromPoint((0, 0)))
    monitor_area = monitor_info.get("Monitor")
    work_area = monitor_info.get("Work")

    if get_screen_mode():
        screen = pygame.display.set_mode((screen_size[0], screen_size[1] - (monitor_area[3] - work_area[3])), pygame.FULLSCREEN)
    else:
        screen = pygame.display.set_mode((screen_size[0], screen_size[1] - (monitor_area[3] - work_area[3])))
else:
    if get_screen_mode():
        screen = pygame.display.set_mode(screen_size, pygame.FULLSCREEN)
    else:
        screen = pygame.display.set_mode(screen_size)


# класс масок ввода пароля и логина
class InputBox:

    def __init__(self, x, y, size, text=''):
        self.rect = pygame.Rect(x, y, size[0], size[1])
        self.color = (212, 175, 55)
        self.text = text
        self.active = False
        self.text_color = (255, 255, 255)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
                self.text = self.text.replace("|", "")
                self.text += "|"
            else:
                self.text = self.text.replace("|", "")
                self.active = False

        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]

                else:
                    if draw_text(self.text, 20, self.text_color, screen, self.rect.x + 5, self.rect.y + 5) + 10 \
                            < box_size[0] - 10:
                        self.text = self.text.replace("|", "")
                        self.text += event.unicode + "|"
                    else:
                        draw_text(self.text, 20, self.text_color, screen, self.rect.x + 5, self.rect.y + 5)

    def update(self):
        draw_text(self.text, 20, self.text_color, screen, self.rect.x + 5, self.rect.y + 5) + 10

        pygame.draw.rect(screen, self.color, self.rect, 2, 3)

    def give_text(self):
        return self.text


# Создаю кнопки и поля ввода, все расчеты делал на глаз так чтобы выглядело красиво
box_size = screen_size[0] // 4, screen_size[1] // 16
login = InputBox(screen_size[0] - screen_size[0] // 3, screen_size[1] - box_size[1] * 5 - box_size[1] // 2, box_size)
password = InputBox(screen_size[0] - screen_size[0] // 3, screen_size[1] - box_size[1] * 4, box_size)
input_boxes = [login, password]
button_size = screen_size[0] // 7.2, screen_size[1] // 9
auth_button_size = screen_size[0] // 7.2 - box_size[0] // 13.7, screen_size[1] // 10

all_buttons = pygame.sprite.Group()
menu_button_pos_x = screen_size[0] // 14.4
menu_button_pos_y = screen_size[1] // 9

all_buttons.add(Button(menu_button_pos_x, menu_button_pos_y * 2,
                       "play(screen, screen_size)", 'button_start_game.png', button_size))

all_buttons.add(Button(menu_button_pos_x, menu_button_pos_y * 3,
                       "open_chest(screen, screen_size)", 'button_change_deck.png', button_size))

all_buttons.add(Button(menu_button_pos_x, menu_button_pos_y * 4,
                       "open_documentation('data.txt')", 'button_help.png', button_size))

all_buttons.add(Button(menu_button_pos_x, menu_button_pos_y * 5,
                       "options(screen_size, screen)", 'button_settings.png', button_size))

all_buttons.add(Button(menu_button_pos_x, menu_button_pos_y * 6,
                       "print('сделать')", 'button_stats.png', button_size))

all_buttons.add(Button(screen_size[0] - screen_size[0] // 3,
                       screen_size[1] - auth_button_size[1] * 4.2 - auth_button_size[1] // 4,
                       "autho(login.give_text(), password.give_text())", 'button_login.png', auth_button_size))

all_buttons.add(Button(screen_size[0] - screen_size[0] // 3 - screen_size[1] // 16 + box_size[0] - box_size[0] // 4,
                       screen_size[1] - auth_button_size[1] * 4.2 - auth_button_size[1] // 4,
                       "reg(login.give_text(), password.give_text(), screen, width, height)", 'button_reg.png',
                       auth_button_size))

all_buttons.add(Button(width - 60, 10, "webbrowser.open('https://github.com/Sla1mer/PyGameProjectYandex',new=2)",
                       'github_logo.png', (50, 50)))

# Задний фон
bg = pygame.transform.scale(load_image('background.jpg'), (width, height))

def main_menu():
    while True:
        # выход из игры
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for button in all_buttons:
                    if button.rect.collidepoint(event.pos):
                        # при нажатии на кнопку проигрываю звук, создаю партикл и ивалю ее функцию
                        play_sound('button_click.wav')
                        create_particles(pygame.mouse.get_pos())
                        eval(button.update())

            for box in input_boxes:
                box.handle_event(event)

        # подгружаю задний фон
        screen.blit(bg, (0, 0))
        draw_text('Кардмастер', round(screen_size[0] // 12.5), (255, 255, 255), screen, width * 0.53, width * 0.05)

        all_buttons.draw(screen)

        for box in input_boxes:
            box.update()

        all_parcticles.draw(screen)
        all_parcticles.update()

        pygame.display.update()
        mainClock.tick(60)


if __name__ == '__main__':
    main_menu()
