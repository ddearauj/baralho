import pygame
from card import Card
from player import Player

class Board:
	"""
	The board essentialy works as the level class.
	It controls most of the gameply dynamics
	"""
	def __init__(self):
		
        # get the display surface
		self.display_surface = pygame.display.get_surface()

		# sprite groups
		self.all_sprites = pygame.sprite.Group()
		self.player_group_sprite = pygame.sprite.Group()
		self.elapsed_time = 0

		self.player = Player(self.player_group_sprite)
		

	def run(self,dt,event_list):

		# Paint background
		self.display_surface.fill([95, 205, 228])

		self.player.update(event_list)


		# draw player hand
		self.player_group_sprite.draw(self.display_surface)
		self.player_group_sprite.update(dt)
	
		self.elapsed_time += (dt)