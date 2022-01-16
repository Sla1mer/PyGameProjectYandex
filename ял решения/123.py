import os
import sys

import pygame

# Изображение не получится загрузить
# без предварительной инициализации pygame
pygame.init()
size = width, height = 600, 600
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



class Card(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(load_image('button_help.png'), (100, 50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x = self.rect.x
        self.y = self.rect.y


    def update(self, *args):
        self.rect.x += args[0][0]
        self.rect.y += args[0][1]


all_card = pygame.sprite.Group()
all_card.add(Card(100, 100))
all_card.add(Card(200, 200))

def main(screen):
    pygame.display.set_caption('Перетаскивание')
    state = False

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for card in all_card:
                    if card.rect.collidepoint(event.pos):
                        state = True

            if event.type == pygame.MOUSEMOTION:
                if state:
                    for card in all_card:
                        if card.rect.collidepoint(event.pos):
                            card.update(event.rel)

            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                state = False
        screen.fill((0, 0, 0))
        all_card.draw(screen)
        pygame.display.update()

    pygame.quit()


if __name__ == '__main__':
    main(screen)