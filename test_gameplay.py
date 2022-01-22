import math

import os, platform
import random
import sys

from Settings import get_screen_mode
import pyautogui
import pygame

# Изображение не получится загрузить
# без предварительной инициализации pygame

width, height = pyautogui.size()
# Инициализация игрового поля
screen_size = (width, height)
clock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption('Крутая карточная игра')

if platform.system() == 'Windows':  # Windows
    from win32api import GetMonitorInfo, MonitorFromPoint
    monitor_info = GetMonitorInfo(MonitorFromPoint((0, 0)))
    monitor_area = monitor_info.get("Monitor")
    work_area = monitor_info.get("Work")

    if get_screen_mode():
        screen = pygame.display.set_mode((screen_size[0], screen_size[1] - (monitor_area[3] - work_area[3])), pygame.FULLSCREEN)
    else:
        screen = pygame.display.set_mode((screen_size[0], screen_size[1] - (monitor_area[3] - work_area[3])))
else:
    if get_screen_mode():
        screen = pygame.display.set_mode(screen_size, pygame.FULLSCREEN)
    else:
        screen = pygame.display.set_mode(screen_size)

parts_dict = {0: 'Твоя линия осадных карт', 1: 'Твоя линия дальников', 2: 'Твоя линия ближников',
              3: 'Линия противника ближников', 4: 'Линия противника дальников', 5: 'Линия противника осадных карт'}
cards_ids = {1000: ('swoarder1.png', 'Мечник', 2, 3)}
x_for_parts_coords, y_for_parts_coords = int(screen_size[0] / 3), screen_size[1] // 9
parts_coord = {0: (x_for_parts_coords, y_for_parts_coords), 1: (x_for_parts_coords, y_for_parts_coords * 2),
               2: (x_for_parts_coords, y_for_parts_coords * 3), 3: (x_for_parts_coords, y_for_parts_coords * 4),
               4: (x_for_parts_coords, y_for_parts_coords * 5), 5: (x_for_parts_coords, y_for_parts_coords * 6)}
board_lines_path_data = {0: ("board//line_siege.png", "board//line_siege_selected.png"),
                         1: ("board//line_distant.png", "board//line_distant_selected.png"),
                         2: ("board//line_swords.png", "board//line_swords_selected.png"),
                         5: ("board//line_siege.png", "board//line_siege_selected.png"),
                         4: ("board//line_distant.png", "board//line_distant_selected.png"),
                         3: ("board//line_swords.png", "board//line_swords_selected.png")}


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

    # image = load_image(cards_ids[card_id][0])

    def __init__(self, group, card_id):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite.
        # Это очень важно !!!
        super().__init__(group)
        self.image = load_image(cards_ids[card_id][0])

        self.image = pygame.transform.scale(self.image, (screen_size[0] // 2 // 12, screen_size[1] // 9))
        # self.image = pygame.transform.scale(self.image, (70, 96))
        self.rect = self.image.get_rect()
        self.rect.centerx, self.rect.centery = 1218, 633
        self.took = False
        self.card_id = card_id
        self.card_name = cards_ids[card_id][1]
        self.power = cards_ids[card_id][2]
        self.card_type = cards_ids[card_id][3]
        self.can_be_placed = True
        self.line = -1
        self.to_pos = (self.rect.centerx, self.rect.centery)

    def update_to_pos(self):
        self.to_pos = (self.rect.centerx, self.rect.centery)

    def get_cards(self):
        return

    # Движение к заданным координатам
    def directional_movement(self):
        if self.rect.centerx != self.to_pos[0] or self.rect.centery != self.to_pos[1]:
            x_target = self.to_pos[0] - self.rect.centerx
            y_target = self.to_pos[1] - self.rect.centery

            direction = math.atan2(y_target, x_target)

            distance = math.sqrt(x_target ** 2 + y_target ** 2)

            step = v / fps
            if distance < step:
                self.rect.centerx = self.to_pos[0]
                self.rect.centery = self.to_pos[1]
            else:
                self.rect.centery = self.rect.centery + math.sin(direction) * step
                self.rect.centerx = self.rect.centerx + math.cos(direction) * step

    def update(self, *args):
        if args:
            if self.rect.collidepoint(args[0]) and self.can_be_placed:
                for cardd in cards_group:
                    if self != cardd and cardd.took:
                        cardd.took = False
                        cardd.rect.y += 20
                        cardd.update_to_pos()
                self.took = True if not self.took else False
                if self.took:
                    self.rect.y -= 20
                    self.update_to_pos()
                else:
                    self.rect.y += 20
                    self.update_to_pos()
            else:
                if self.took:
                    part = list(filter(lambda x: x.get_part_type(args[0]) is not None, [part for part in all_parts]))
                    if part:
                        past = list(filter(lambda x: x.get_part_type(args[0]) is not None, [part for part in all_parts]))
                        part = part[0]
                        card_size_x, card_size_y = self.image.get_size()
                        len_cards_in_line = len(part.cards) * card_size_x
                        if part.get_part_type(args[0]) != self.card_type:
                            return
                        self.line = part.get_part_type(args[0])
                        self.took = False
                        self.can_be_placed = False
                        self.to_pos = part.rect.center

                        for my in my_part:
                            my.remove_card(self)

                        part.cards.append(self)
                        counter = 0

                        cards_len = len(part.cards)
                        left_cards = cards_len // 2
                        middle_cards = cards_len - cards_len // 2 - cards_len // 2
                        right_cards = cards_len // 2
                        cards_pos = []
                        if middle_cards == 1:
                            for i in range(1, left_cards + 1):
                                cards_pos.insert(-1, -card_size_x * i)
                            cards_pos.append(0)
                            for i in range(1, right_cards + 1):
                                cards_pos.append(card_size_x * i)
                        else:
                            temp = 0
                            for i in range(1, left_cards + 1):
                                cards_pos.insert(-1, -(card_size_x // 2) * i + temp)
                                temp += -(card_size_x // 2)
                            temp = 0
                            for i in range(1, right_cards + 1):
                                cards_pos.append((card_size_x // 2) * i + temp)
                                temp += (card_size_x // 2)
                        counter = 0
                        for card in part.cards:
                            card.to_pos = [part.rect.centerx + cards_pos[counter], part.rect.centery]
                            counter += 1
                        ball = list(filter(lambda x: x.if_part_type(self.line) is not None, [i for i in balls_stat]))[0]
                        ball.score += self.power
                        if 0 <= self.line <= 2:
                            ball = list(filter(lambda x: x.if_part_type(7) is not None, [ball for ball in balls_stat]))[0]
                            ball.score += self.power
                        elif 3 <= self.line <= 5:
                            ball = list(filter(lambda x: x.if_part_type(6) is not None, [ball for ball in balls_stat]))[0]
                            ball.score += self.power
                        # if len(part.cards) >= 1:
                        #     for card in part.cards:
                        #         card.to_pos = [card.to_pos[0] - 35, card.to_pos[1]]
                        #
                        # part.cards.append(self)
                        # self.to_pos = (part.rect.centerx + 35, part.rect.centery)

        self.directional_movement()


class Table(pygame.sprite.Sprite):
    image = load_image("board//background.png")

    def __init__(self, group):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite.
        # Это очень важно !!!
        super().__init__(group)
        self.image = Table.image
        self.image = pygame.transform.scale(self.image, screen_size)
        self.rect = self.image.get_rect()


class MyPartCards(pygame.sprite.Sprite):
    image_default = load_image("mypart.png")

    def __init__(self, group):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite.
        # Это очень важно !!!
        super().__init__(group)
        self.image = MyPartCards.image_default
        self.image = pygame.transform.scale(self.image, (screen_size[0] // 2, screen_size[1] // 9))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = (x_for_parts_coords, y_for_parts_coords * 7 + int(y_for_parts_coords * 0.5))
        self.my_cards = []

    def remove_card(self, card):
        self.my_cards.remove(card)
        card_size_x, card_size_y = card.image.get_size()

        cards_len = len(self.my_cards)
        left_cards = cards_len // 2
        middle_cards = cards_len - cards_len // 2 - cards_len // 2
        right_cards = cards_len // 2
        cards_pos = []
        if middle_cards == 1:
            for i in range(1, left_cards + 1):
                cards_pos.insert(-1, -card_size_x * i)
            cards_pos.append(0)
            for i in range(1, right_cards + 1):
                cards_pos.append(card_size_x * i)
        else:
            temp = 0
            for i in range(1, left_cards + 1):
                cards_pos.insert(-1, -(card_size_x // 2) * i + temp)
                temp += -(card_size_x // 2)
            temp = 0
            for i in range(1, right_cards + 1):
                cards_pos.append((card_size_x // 2) * i + temp)
                temp += (card_size_x // 2)
        counter = 0
        for card in self.my_cards:
            card.to_pos = [self.rect.centerx + cards_pos[counter], self.rect.centery]
            counter += 1

    def add_card(self, card):
        self.my_cards.append(card)
        card_size_x, card_size_y = card.image.get_size()

        cards_len = len(cards_group)
        left_cards = cards_len // 2
        middle_cards = cards_len - cards_len // 2 - cards_len // 2
        right_cards = cards_len // 2
        cards_pos = []
        if middle_cards == 1:
            for i in range(1, left_cards + 1):
                cards_pos.insert(-1, -card_size_x * i)
            cards_pos.append(0)
            for i in range(1, right_cards + 1):
                cards_pos.append(card_size_x * i)
        else:
            temp = 0
            for i in range(1, left_cards + 1):
                cards_pos.insert(-1, -(card_size_x // 2) * i + temp)
                temp += -(card_size_x // 2)
            temp = 0
            for i in range(1, right_cards + 1):
                cards_pos.append((card_size_x // 2) * i + temp)
                temp += (card_size_x // 2)
        counter = 0
        for card in self.my_cards:
            card.to_pos = [self.rect.centerx + cards_pos[counter], self.rect.centery]
            counter += 1


class Parts(pygame.sprite.Sprite):
    def __init__(self, group, part_type):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite.
        # Это очень важно !!!
        super().__init__(group)
        self.image_default = load_image(board_lines_path_data[part_type][0])
        self.image_selected = load_image(board_lines_path_data[part_type][1])
        self.image = self.image_default
        self.image = pygame.transform.scale(self.image, (screen_size[0] // 2, screen_size[1] // 9))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = parts_coord[part_type]
        self.part_type = part_type
        # if 0 <= part_type <= 2:
        self.cards = []

    def get_part_type(self, coords):
        if self.rect.collidepoint(coords):
            return self.part_type

    def if_part_type(self, part_type):
        if part_type == self.part_type:
            return self

    def update(self, *args):
        if args:
            if self.rect.collidepoint(args[0]):
                if self.image != self.image_selected:
                    self.image = self.image_selected
                    self.image = pygame.transform.scale(self.image, (screen_size[0] // 2, screen_size[1] // 9))
            else:
                if self.image != self.image_default:
                    self.image = self.image_default
                    self.image = pygame.transform.scale(self.image, (screen_size[0] // 2, screen_size[1] // 9))


class BallsCounters(pygame.sprite.Sprite):
    image_ball_blue = load_image("blue_ball.png")
    image_ball_yellow = load_image("yellow_ball.png")

    def __init__(self, group, part_type):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite.
        # Это очень важно !!!
        super().__init__(group)
        self.part_type = part_type
        if 0 <= part_type <= 2:
            part = list(filter(lambda x: x.if_part_type(part_type) is not None, [i for i in all_parts]))[0]
            self.image = BallsCounters.image_ball_yellow
            self.image = pygame.transform.scale(self.image, (part.rect.height // 2, part.rect.height // 2))
            self.rect = self.image.get_rect()
            self.rect.centerx, self.rect.centery = part.rect.topleft[0] - part.rect.topleft[0] // 27, part.rect.topleft[1] + part.rect.height // 2
        elif 3 <= part_type <= 5:
            part = list(filter(lambda x: x.if_part_type(part_type) is not None, [i for i in all_parts]))[0]
            self.image = BallsCounters.image_ball_blue
            self.image = pygame.transform.scale(self.image, (part.rect.height // 2, part.rect.height // 2))
            self.rect = self.image.get_rect()
            self.rect.centerx, self.rect.centery = part.rect.topleft[0] - part.rect.topleft[0] // 27, part.rect.topleft[1] + part.rect.height // 2
        elif part_type == 6:
            self.image = BallsCounters.image_ball_blue
            self.rect = self.image.get_rect()
            self.rect.centerx, self.rect.centery = (225, 233)
        elif part_type == 7:
            self.image = BallsCounters.image_ball_yellow
            self.rect = self.image.get_rect()
            self.rect.centerx, self.rect.centery = (225, 490)
        self.score = 0

    def if_part_type(self, part_type):
        if part_type == self.part_type:
            return self

    def draw_text(self):
        font = pygame.font.Font('our_font.otf', 35)
        text1 = font.render(str(self.score), False,
                            (219, 0, 223))
        return text1, (self.rect.centerx - (self.rect.centerx - self.rect.x) // 2.5, self.rect.y)

    # def update(self, *args):
    #     font = pygame.font.SysFont('Comic Sans MS', 30)
    #     text1 = font.render(str(self.score), False,
    #                       (154, 48, 48))
    #     screen.blit(text1, self.rect.center)

v = 1500
fps = 60
cards_group = pygame.sprite.Group()
board = pygame.sprite.Group()
my_part = pygame.sprite.Group()
all_parts = pygame.sprite.Group()
balls_stat = pygame.sprite.Group()


def play(screen, screen_size):
    # создадим группу, содержащую все спрайты
    global cards_group
    cards_group = pygame.sprite.Group()
    global board
    board = pygame.sprite.Group()
    global my_part
    my_part = pygame.sprite.Group()
    global all_parts
    all_parts = pygame.sprite.Group()
    global balls_stat
    balls_stat = pygame.sprite.Group()
    Card(cards_group, card_id=1000)
    Card(cards_group, card_id=1000)
    Card(cards_group, card_id=1000)
    Card(cards_group, card_id=1000)
    Card(cards_group, card_id=1000)
    Card(cards_group, card_id=1000)
    Card(cards_group, card_id=1000)
    Card(cards_group, card_id=1000)
    Card(cards_group, card_id=1000)
    Card(cards_group, card_id=1000)

    Table(board)

    MyPartCards(my_part)
    for my in my_part:
        for card in cards_group:
            my.add_card(card)

    Parts(all_parts, 0)
    Parts(all_parts, 1)
    Parts(all_parts, 2)
    Parts(all_parts, 3)
    Parts(all_parts, 4)
    Parts(all_parts, 5)

    BallsCounters(balls_stat, 0)
    BallsCounters(balls_stat, 1)
    BallsCounters(balls_stat, 2)
    BallsCounters(balls_stat, 3)
    BallsCounters(balls_stat, 4)
    BallsCounters(balls_stat, 5)
    BallsCounters(balls_stat, 6)
    BallsCounters(balls_stat, 7)

    running = True
    card_taked = False
    while running:

        clock.tick(fps)
        cards_group.update()
        balls_stat.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                cards_group.update(event.pos)
            if event.type == pygame.MOUSEMOTION:
                all_parts.update(event.pos)
        board.draw(screen)
        all_parts.draw(screen)
        my_part.draw(screen)
        balls_stat.draw(screen)
        for i in balls_stat:
            temp = i.draw_text()
            screen.blit(temp[0], temp[1])
        cards_group.draw(screen)
        pygame.display.flip()
