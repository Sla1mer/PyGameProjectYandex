import os
import sys

import pygame

# Изображение не получится загрузить
# без предварительной инициализации pygame
pygame.init()
size = width, height = 600
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
    image = load_image("creature.png", -1)

    def __init__(self, *group):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite. Это очень важно !!!
        super().__init__(*group)
        self.image = Hero.image
        self.rect = self.image.get_rect()

    def update(self, *args):
        if args:
            if args[0] == pygame.K_LEFT:
                self.rect.x -= 10
            if args[0] == pygame.K_RIGHT:
                self.rect.x += 10
            if args[0] == pygame.K_UP:
                self.rect.y -= 10
            if args[0] == pygame.K_DOWN:
                self.rect.y += 10


all_sprites = pygame.sprite.Group()

Hero(all_sprites)

running = True
while running:
    clock.tick(60)
    all_sprites.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_LEFT]:
            all_sprites.update(pygame.K_LEFT)
        if keys_pressed[pygame.K_RIGHT]:
            all_sprites.update(pygame.K_RIGHT)
        if keys_pressed[pygame.K_UP]:
            all_sprites.update(pygame.K_UP)
        if keys_pressed[pygame.K_DOWN]:
            all_sprites.update(pygame.K_DOWN)

    screen.fill(pygame.Color("white"))
    all_sprites.draw(screen)
    pygame.display.flip()
