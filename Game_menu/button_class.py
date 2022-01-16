import pygame
from load_img import load_image

all_buttons = pygame.sprite.Group()


# Класс кнопок при инициализации надо передать позицию, строку функционала которую она выполняет( с помощью eval), и размер автоматом стоит хрень какая-то
class Button(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos, func: str, path, size=(200, 100)):
        super().__init__(all_buttons)

        self.func = func
        self.image = pygame.transform.scale(load_image(path), (size))
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.x -= 10
        self.rect.y = y_pos

    # в коде просто выполняю eval() того что вернул метод апдейт
    def update(self):
        return self.func
