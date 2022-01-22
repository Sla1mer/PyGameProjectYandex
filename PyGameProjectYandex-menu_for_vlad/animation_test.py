import pygame, sys
from load_img import load_image


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

	def open(self):
		self.open_animation = True

	def update(self, speed):
		if self.open_animation == True:
			self.current_sprite += speed
			if int(self.current_sprite) >= len(self.sprites):
				self.current_sprite = 0
				self.open_animation = False

		self.image = self.sprites[int(self.current_sprite)]





def open_chest(screen, screen_size):
	bg = pygame.transform.scale(load_image('background.jpg'), (screen_size[0], screen_size[1]))
	mainClock = pygame.time.Clock()
	moving_sprites = pygame.sprite.Group()
	chest_size_x = screen_size[0] * 0.1
	chest_size_y = screen_size[0] * 0.1
	chest = Card_Chest(screen_size[0] // 2 + chest_size_x // 3, screen_size[1] - chest_size_y * 2.14, (chest_size_x, chest_size_y))
	moving_sprites.add(chest)
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
						chest.open()


		screen.blit(bg, (0, 0))
		moving_sprites.draw(screen)
		moving_sprites.update(1.5)
		mainClock.tick(60)
		pygame.display.flip()
