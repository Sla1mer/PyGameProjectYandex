import pygame
from load_img import load_image


class Button(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos,  func, path, size=(200, 90)):
        super(Button, self).__init__()

        self.func = func
        self.image = pygame.transform.scale(load_image(path), (size))
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.x -= 10
        self.rect.y = y_pos

    def update(self):
        return self.func
