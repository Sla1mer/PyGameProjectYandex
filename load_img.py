import pygame
import os
import sys

# Загружает png изображение, не подходит для векторной графики!!


def load_image(name, flag=False):
    fullname = ""
    if flag:
        fullname = os.path.join(name)
    else:
        fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image
