import os
import random
import sys

import pygame




# Изображение не получится загрузить
# без предварительной инициализации pygame
pygame.init()
size = width, height = 599, 300
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


class GameOver(pygame.sprite.Sprite):
    image = load_image("gameover.png", -1)

    def __init__(self, *group):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite. Это очень важно !!!
        super().__init__(*group)
        self.image = GameOver.image
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.rect = self.image.get_rect()
        self.rect.x = -600


        clock.tick(60)
        self.dx = 200 * clock.tick(60) / 1000
        print(self.dx)

    def update(self, *args):
        if self.rect.x > -12 :
            self.rect.x = -1
        else:
            self.rect.x += self.dx
        self.clock.tick(self.fps)


end = pygame.sprite.Group()

GameOver(end)

running = True
while running:
    end.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(pygame.Color("Blue"))


    end.draw(screen)
    clock.tick(60)
    pygame.display.flip()
pygame.quit()
