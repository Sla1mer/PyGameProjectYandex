import pyautogui
import pygame
from test_menu
width, height = pyautogui.size()
width = width // 4
height = height // 2
# Инициализация игрового поля
screen_size = (width, height)
pygame.init()
pygame.display.set_caption('Настройки')
d = pygame.display.set_mode(screen_size)
mainClock = pygame.time.Clock()


# Takes rectangle's size, position and a point. Returns true if that
# point is inside the rectangle and false if it isnt.
def pointInRectanlge(px, py, rw, rh, rx, ry):
    if px > rx and px < rx + rw:
        if py > ry and py < ry + rh:
            return True
    return False


# Blueprint to make sliders in the game
class Slider:
    def __init__(self, position: tuple, upperValue: int = 10, sliderWidth: int = 30,
                 text: str = "Editing features for simulation",
                 outlineSize: tuple = (300, 100)) -> None:
        self.position = position
        self.outlineSize = outlineSize
        self.text = text
        self.sliderWidth = sliderWidth
        self.upperValue = upperValue

    def getValue(self) -> float:
        return self.sliderWidth / (self.outlineSize[0] / self.upperValue)

    def render(self, display: pygame.display) -> None:
        pygame.draw.rect(display, (0, 0, 0), (self.position[0], self.position[1],
                                              self.outlineSize[0], self.outlineSize[1]), 3)

        pygame.draw.rect(display, (0, 0, 0), (self.position[0], self.position[1],
                                              self.sliderWidth, self.outlineSize[1] - 10))

        self.font = pygame.font.Font(pygame.font.get_default_font(), int((15 / 100) * self.outlineSize[1]))

        valueSurf = self.font.render(f"{self.text}: {round(self.getValue())}", True, (255, 0, 0))

        textx = self.position[0] + (self.outlineSize[0] / 2) - (valueSurf.get_rect().width / 2)
        texty = self.position[1] + (self.outlineSize[1] / 2) - (valueSurf.get_rect().height / 2)

        display.blit(valueSurf, (textx, texty))

    # allows users to change value of the slider by dragging it.
    def changeValue(self):
        # If mouse is pressed and mouse is inside the slider
        mousePos = pygame.mouse.get_pos()
        if pointInRectanlge(mousePos[0], mousePos[1]
                , self.outlineSize[0], self.outlineSize[1], self.position[0], self.position[1]):
            if pygame.mouse.get_pressed()[0]:
                # the size of the slider
                self.sliderWidth = mousePos[0] - self.position[0]

                # limit the size of the slider
                if self.sliderWidth < 1:
                    self.sliderWidth = 0
                if self.sliderWidth > self.outlineSize[0]:
                    self.sliderWidth = self.outlineSize[0]


slider = Slider((10, 10))
all_settings_button = pygame.sprite.Group()
all_settings_button.add()

def settings():
    while True:
        pygame.event.get()
        d.fill((255, 255, 255))

        slider.render(d)
        slider.changeValue()

        pygame.display.update()
        mainClock.tick(60)


settings()