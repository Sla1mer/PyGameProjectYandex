import sys

import pyautogui
import pygame

from Game_menu.draw_text import draw_text

width, height = 100, 100
# Инициализация игрового поля
screen_size = (width, height)
mainClock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption('Крутая карточная игра')
screen = pygame.display.set_mode(screen_size)


def error():
    while True:
        # выход из игры
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # подгружаю задний фон
        screen.fill((255, 255, 255))
        draw_text('Кардмастер', round(screen_size[0] // 12.5), (0, 170, 200), screen, width * 0.55, width * 0.05)

        pygame.display.update()
        mainClock.tick(60)
