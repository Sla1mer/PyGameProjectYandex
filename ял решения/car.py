import os
import random
import sys

import pygame

# Изображение не получится загрузить
# без предварительной инициализации pygame
pygame.init()
size = width, height = 600, 95
screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class Hero(pygame.sprite.Sprite):
    image = load_image("car.png", -1)

    def __init__(self, *group):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite. Это очень важно !!!
        super().__init__(*group)
        self.image = Hero.image
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.rect = self.image.get_rect()


        clock.tick(60)
        self.dx = 200 * 60 / 1000

    def update(self, *args):
        self.rect.x += self.dx
        if self.rect.x > 450 or self.rect.x < 0:
            self.image = pygame.transform.flip(self.image, True, False)
            self.dx *= -1
        self.clock.tick(self.fps)


car = pygame.sprite.Group()

Hero(car)

running = True
while running:
    car.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



    screen.fill(pygame.Color("white"))
    clock.tick(60)

    car.draw(screen)
    pygame.display.flip()
