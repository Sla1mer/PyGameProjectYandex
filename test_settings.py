import pygame
import sys
from button_class import Button
from load_img import load_image
from draw_text import draw_text
from play_sound import play_sound, change_volume, game_volume, get_volume
from particle_class import create_particles, all_parcticles

from Settings import set_volume, set_screen_mode

running = True


# меняю режим изображения
def change_window(screen_size, flag=False):
    global screen
    if flag:
        screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    else:
        screen = pygame.display.set_mode(screen_size)
    set_screen_mode(flag)


# костыль для выхода из настроек
def change_state():
    global running
    set_volume(get_volume())
    running = False


# функция настроек
def options(screen_size, screen):
    global running
    running = True
    # создаю все кнопочки, расчет их размеров так же на глаз
    bg = pygame.transform.scale(load_image('background.jpg'), (screen_size[0], screen_size[1]))
    mainClock = pygame.time.Clock()
    button_size = screen_size[0] // 7.2, screen_size[1] // 9
    button_pos_x = screen_size[0] // 2 - button_size[0] // 2
    button_pos_y = screen_size[1] // 9
    volume_ico_size = (screen_size[0] // 2 - 40, screen_size[1] // 2 - 2 * screen_size[1] * 0.1)
    all_settings_button = pygame.sprite.Group()
    all_settings_button.add(Button(button_pos_x, button_pos_y * 6, 'change_state()', 'button_go_back.png',
                                   button_size))

    all_settings_button.add(
        Button(volume_ico_size[0] - 25 - 40, volume_ico_size[1] + 25, 'change_volume(-0.1)', 'minus.png',
               (50, 50)))
    all_settings_button.add(
        Button(volume_ico_size[0] + 25 + 80, volume_ico_size[1] + 25, 'change_volume(0.1)',
               'plus.png', (50, 50)))
    all_settings_button.add(
        Button(button_pos_x, button_pos_y * 4, 'change_window(screen_size, True)', 'button_change_screen1.png',
               button_size))
    all_settings_button.add(
        Button(button_pos_x, button_pos_y * 5, 'change_window(screen_size)', 'button_change_screen2.png',
               button_size))
    volume_icon = pygame.transform.scale(load_image('volume.png'), (80, 80))

    while running:
        screen.blit(bg, (0, 0))
        screen.blit(volume_icon, volume_ico_size)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for button in all_settings_button:
                    if button.rect.collidepoint(event.pos):
                        eval(button.update())

                        play_sound('button_click.wav')

                        create_particles(pygame.mouse.get_pos())
        # надпись с громкостью

        draw_text(f'текущая громкость {round(get_volume() * 100)}%', screen_size[0] // 72, (255, 255, 255),
                  screen, screen_size[0] // 2 - button_size[0] // 2, button_pos_y * 2)

        all_settings_button.draw(screen)
        all_parcticles.draw(screen)
        all_parcticles.update()
        pygame.display.update()
        mainClock.tick(60)


