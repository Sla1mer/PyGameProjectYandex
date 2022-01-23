import sys

import pyautogui

from Settings import get_screen_mode
from load_img import load_image
from draw_text import draw_text
from test_menu import main_menu

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
    pygame.quit()
    sys.exit()


def start_screen():
    intro_text = ["КАРДМАСТЕР", "", "Нажмите любую кнопку, что бы продолжить"]

    background = pygame.transform.scale(load_image("start_screen_background.jpg"), (WIDTH, HEIGHT))
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

    while True:
        mainClock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                main_menu()

        pygame.display.flip()


if __name__ == '__main__':
    start_screen()
