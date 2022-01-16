# функция отрисовки текста, принимает на вход текст, размер, цвет, поле на котором отрисовывает, и координаты x y
import pygame


def draw_text(text, font_size, color, surface, x, y):
    font = pygame.font.Font('our_font.otf', font_size)
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
    return textobj.get_width()