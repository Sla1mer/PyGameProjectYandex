from autho_and_reg import autho, reg
from load_img import load_image
import pygame
import sys
from pygame.locals import *
import random


# Инициализация игрового поля
screen_size = (1280, 720)
pygame.init()
pygame.display.set_caption('Крутая карточная игра')
screen = pygame.display.set_mode(screen_size)
mainClock = pygame.time.Clock()


# Функция отрисовывания эффектов, на вход принимает координаты где надо отрисовывать
def create_particles(position):
    # количество создаваемых частиц
    particle_count = 10
    # возможные скорости
    numbers = range(-5, 6)
    for _ in range(particle_count):
        Particle(position, random.choice(numbers), random.choice(numbers))


# функция отрисовки текста, принимает на вход текст, размер, цвет, поле на котором отрисовывает, и координаты x y
def draw_text(text, font_size, color, surface, x, y):
    font = pygame.font.Font('our_font.ttf', font_size)
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
    return textobj.get_width()


all_parcticles = pygame.sprite.Group()


class Particle(pygame.sprite.Sprite):
    # сгенерируем частицы разного размера
    fire = [load_image("star.png")]
    for scale in (5, 10, 20):
        fire.append(pygame.transform.scale(fire[0], (scale, scale)))

    def __init__(self, pos, dx, dy):
        super().__init__(all_parcticles)
        self.image = random.choice(self.fire)
        self.rect = self.image.get_rect()

        # у каждой частицы своя скорость — это вектор
        self.velocity = [dx, dy]
        # и свои координаты
        self.rect.x, self.rect.y = pos

        # гравитация будет одинаковой (значение константы)
        self.gravity = 0.5

    def update(self):
        # применяем гравитационный эффект:
        # движение с ускорением под действием гравитации
        self.velocity[1] += self.gravity
        # перемещаем частицу

        self.rect.x -= self.velocity[0]
        self.rect.y += self.velocity[1]
        # убиваем, если частица ушла за экран
        if not self.rect.colliderect(0, 0, screen_size[0], screen_size[1]):
            self.kill()


class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = (212, 175, 55)
        self.text = text
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False

        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    if draw_text(self.text, 20, (0, 170, 200), screen, self.rect.x + 5, self.rect.y + 5) + 10 < 400:
                        self.text += event.unicode
                    else:
                        draw_text(self.text, 20, (0, 170, 200), screen, self.rect.x + 5, self.rect.y + 5)

    def update(self):
        text_size = draw_text(self.text, 20, (0, 170, 200), screen, self.rect.x + 5, self.rect.y + 5) + 10
        self.rect.w = max(410, text_size)
        pygame.draw.rect(screen, self.color, self.rect, 2, 3)


    def give_text(self):
        return self.text


class Button(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos,  func, path, size=(200, 90)):
        super(Button, self).__init__()
        self.func = func
        self.image = pygame.transform.scale(load_image(path), (size))
        self.rect = self.image.get_rect()
        self.rect.x += x_pos
        self.rect.x -= 10
        self.rect.y += y_pos

    def update(self):
        eval(self.func)


# Создаю кнопки и поля ввода
password = InputBox(850, 550, 200, 50)
login = InputBox(850, 490, 200, 50)
input_boxes = [login, password]
all_buttons = pygame.sprite.Group()
all_buttons.add(Button(100, 200, "print('сделать')", 'button_start_game.png'))
all_buttons.add(Button(100, 300, "print('сделать')", 'button_change_deck.png'))
all_buttons.add(Button(100, 400, "print('сделать')", 'button_help.png'))
all_buttons.add(Button(100, 500, "print('сделать')", 'button_settings.png'))
all_buttons.add(Button(100, 600, "print('сделать')", 'button_stats.png'))
all_buttons.add(Button(850, 600, "autho(login.give_text(), password.give_text())", 'button_login.png'))
all_buttons.add(Button(1076, 600, "reg(login.give_text(), password.give_text())", 'button_reg.png'))



# Задний фон
bg = pygame.transform.scale(load_image('background.jpg'), (1280, 720))


# основной цикл программы
running = True


def main_menu():
    global running
    while running:
        # выход из игры
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                for button in all_buttons:
                    if button.rect.collidepoint(event.pos):
                        button.update()
                        create_particles(pygame.mouse.get_pos())

            for box in input_boxes:
                box.handle_event(event)

        # подгружаю задний фон
        screen.blit(bg, (0, 0))
        draw_text('Кардмастер', 100, (0, 170, 200), screen, 700, 50)

        all_buttons.draw(screen)

        for box in input_boxes:
            box.update()

        all_parcticles.draw(screen)
        all_parcticles.update()


        pygame.display.update()
        mainClock.tick(60)


if __name__ == '__main__':
    main_menu()
