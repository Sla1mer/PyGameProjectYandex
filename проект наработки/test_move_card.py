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
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image('card.jpg')
        self.rect = self.image.get_rect()
        self.x = self.rect.x
        self.y = self.rect.y
        self.x1 = 100
        self.y1 = 100

    def update(self, *args):
        self.rect.x += args[0][0]
        self.rect.y += args[0][1]

    def check(self, x_pos, y_pos):
        if x_pos in range(self.rect.x, self.rect.x + self.rect[2]) and \
                y_pos in range(self.rect.y, self.rect.y + self.rect[3]):
            return True
        else:
            return False



def main(screen):
    pygame.display.set_caption('Перетаскивание')
    state = False
    first_card = Card()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if first_card.check(event.pos[0], event.pos[1]):
                    state = True

            if event.type == pygame.MOUSEMOTION:
                if state:
                    first_card.update(event.rel)

            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                state = False

        screen.fill((0, 0, 0))
        screen.blit(first_card.image, first_card.rect)
        pygame.display.update()

    pygame.quit()


if __name__ == '__main__':
    main(screen)