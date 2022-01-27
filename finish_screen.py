import sys
import threading
import time

import pyautogui

from Settings import get_screen_mode
from load_img import load_image
from draw_text import draw_text

import pygame

FPS = 120

WIDTH, HEIGHT = pyautogui.size()
# Инициализация игрового поля
screen_size = (WIDTH, HEIGHT)
mainClock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption("Кардмастер")
if get_screen_mode():
    screen = pygame.display.set_mode(screen_size, pygame.FULLSCREEN)
else:
    screen = pygame.display.set_mode(screen_size)


def terminate():
    x = threading.Thread(target=finish_screen())
    x.start()

    pygame.quit()
    sys.exit()


def finish_screen():
    intro_text = ["КАРДМАСТЕР", "", "Спасибо герой за работу, ждём тебя ещё!"]

    background = pygame.transform.scale(load_image("background_finish_screen.jpg"), (WIDTH, HEIGHT))
    screen.blit(background, (0, 0))

    # Коэфициенты для координат текста
    koeff_wight = 0.3
    koeff_height = 0.55
    for line in intro_text:
        if line == "КАРДМАСТЕР":
            draw_text(line, round(screen_size[0] // 12.5), (255, 255, 255), screen, WIDTH * 0.29, HEIGHT * 0.35)
        else:
            draw_text(line, round(screen_size[0] // 50), (255, 255, 255), screen, WIDTH * koeff_wight,
                      HEIGHT * koeff_height)

    mainClock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()

    pygame.display.flip()
    time.sleep(5)
