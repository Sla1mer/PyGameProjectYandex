import pygame, random
from load_img import load_image
from dict_cards_id import cards_ids
from button_class import Button
from particle_class import create_particles, all_parcticles
from play_sound import play_sound

all_new_card = pygame.sprite.Group()


class Card_Chest(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, size):
        super().__init__()
        self.open_animation = False
        self.sprites = []
        for i in range(1, 23):
            self.sprites.append(pygame.transform.scale(load_image(f'{i}.png'), (size)))
            self.sprites.append(pygame.transform.scale(load_image(f'{i}.png'), (size)))
            self.sprites.append(pygame.transform.scale(load_image(f'{i}.png'), (size)))
            self.sprites.append(pygame.transform.scale(load_image(f'{i}.png'), (size)))
            self.sprites.append(pygame.transform.scale(load_image(f'{i}.png'), (size)))
            self.sprites.append(pygame.transform.scale(load_image(f'{i}.png'), (size)))

        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x,pos_y]

    def open(self, size):
        self.open_animation = True
        self.size = size

    def update(self, speed):
        if self.open_animation:
            self.current_sprite += speed
            if int(self.current_sprite) >= len(self.sprites):
                self.current_sprite = 0
                self.open_animation = False
                new_deck(self.size)

        self.image = self.sprites[int(self.current_sprite)]


class Unlock_Card(pygame.sprite.Sprite):
    def __init__(self, card_id: tuple, pos: tuple, size: tuple):
        super().__init__(all_new_card)
        self.id = card_id
        self.pos = pos
        self.is_drawed = False
        self.card_size = size
        self.image = load_image(card_id[0])
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos


def get_random_deck():
    random_pick = set()
    while True:
        if len(random_pick) == 11:
            break
        random_pick.add(random.choice(list(cards_ids.keys())))
    return random_pick


def new_deck(size):
    for index, id in enumerate(get_random_deck()):
        card = cards_ids[id]
        all_new_card.add(Unlock_Card(card, (index * 200, 100), size))



def open_chest(screen, screen_size):
    bg = pygame.transform.scale(load_image('background.jpg'), (screen_size[0], screen_size[1]))
    mainClock = pygame.time.Clock()
    moving_sprites = pygame.sprite.Group()
    chest_size_x = screen_size[0] * 0.1
    chest_size_y = screen_size[0] * 0.1
    chest = Card_Chest(screen_size[0] // 2 - 2.1 * chest_size_x, screen_size[1] // 2 - chest_size_y * 0.8 , (chest_size_x, chest_size_y))
    moving_sprites.add(chest)
    card_size = (screen_size[0] // 14, screen_size[1] // 7)
    all_buttons = pygame.sprite.Group()
    all_buttons.add(Button(700, 800,
                           "print('ты лох')", 'button_start_game.png', (200, 100)))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if chest.rect.collidepoint(event.pos):
                    for i in all_new_card:
                        i.kill()
                    chest.open(card_size)
                for button in all_buttons:
                    if button.rect.collidepoint(event.pos):
                        # при нажатии на кнопку проигрываю звук, создаю партикл и ивалю ее функцию
                        play_sound('button_click.wav')
                        create_particles(pygame.mouse.get_pos())
                        eval(button.update())

        screen.blit(bg, (0, 0))
        moving_sprites.draw(screen)
        moving_sprites.update(1.5)
        all_new_card.draw(screen)
        all_buttons.draw(screen)
        all_parcticles.draw(screen)
        all_parcticles.update()
        mainClock.tick(60)
        pygame.display.flip()