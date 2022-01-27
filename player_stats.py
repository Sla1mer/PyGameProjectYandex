import sys

from Settings import get_login
import sqlite3 as sq
import pygame
from load_img import load_image
from draw_text import draw_text


def get_statistic(screen, screen_size):
    all_games = {}
    with sq.connect('users.db') as db:
        cur = db.cursor()
        query = """SELECT * FROM all_user_games WHERE login = ? """
        cur.execute(query, (get_login(),))
        for index, (id, result, date, username) in enumerate(cur.fetchall()):
            if index < 9:
                all_games[index] = (result, date, username)
    print(all_games)
    running = True
    text_size = screen_size[0] * 0.07, screen_size[1] * 0.1

    bg = pygame.transform.scale(load_image('board/background.png'), (screen_size[0], screen_size[1]))
    mainClock = pygame.time.Clock()
    while running:
        screen.blit(bg, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        # pygame.draw.rect(screen, (255, 0, 255), (1, 1, text_size[0] * 2, text_size[1] * 2), -1)

        draw_text(f'результаты последних игр ', screen_size[0] // 30, (255, 255, 255),
                  screen, screen_size[0] // 2 - screen_size[0] // 4, screen_size[1] * 0.02)

        draw_text(f'Результат    дата    имя игрока', screen_size[0] // 40, (255, 255, 255), screen,
                  text_size[0], text_size[1])

        for id, games in enumerate(all_games.values()):
            if id < 8:
                to_show = str(games).strip("(").strip(")").replace(",", " ").replace("'", " ").split()
                if to_show[0] == 'win':
                    temp = draw_text(f'''{str(games).strip("(").strip(")").replace(",", " ").replace("'", " ")}''',
                                     screen_size[0] // 30, (255, 255, 255), screen, text_size[0],
                                     screen_size[1] * 0.1 + text_size[1] + text_size[1] * id)
                    pygame.draw.rect(screen, (142, 196, 250), (
                    text_size[0], screen_size[1] * 0.1 + text_size[1] + text_size[1] * id, temp, text_size[1]), 0)
                    draw_text(f'''{str(games).strip("(").strip(")").replace(",", " ").replace("'", " ")}''',
                              screen_size[0] // 30, (255, 255, 255), screen, text_size[0],
                              screen_size[1] * 0.1 + text_size[1] + text_size[1] * id)
                else:
                    temp = draw_text(f'''{str(games).strip("(").strip(")").replace(",", " ").replace("'", " ")}''',
                                     screen_size[0] // 30, (255, 255, 255), screen, text_size[0],
                                     screen_size[1] * 0.1 + text_size[1] + text_size[1] * id)
                    pygame.draw.rect(screen, (241, 201, 81), (
                        text_size[0], screen_size[1] * 0.1 + text_size[1] + text_size[1] * id, temp, text_size[1]), 0)
                    draw_text(f'''{str(games).strip("(").strip(")").replace(",", " ").replace("'", " ")}''',
                              screen_size[0] // 30, (255, 255, 255), screen, text_size[0],
                              screen_size[1] * 0.1 + text_size[1] + text_size[1] * id)

        pygame.display.update()
        mainClock.tick(60)
