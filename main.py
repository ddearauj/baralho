"""
Here we want to have a main function with some simple boiler plate stuff:
(that I always copy from other projects because I forget how to start)
"""
import pygame, sys
import settings as sett
# import asyncio # useful for uploading the game to itch.io online. Not sure if we will need it here
from board import Board

class Game:
	"""
	"""
	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode(sett.window_size)
		pygame.display.set_caption('Baralho!!')
		self.clock = pygame.time.Clock()
		self.board = Board()

	def run(self):
		while True:
			event_list = pygame.event.get()
			for event in event_list:
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
  
			dt = self.clock.tick(60) / 1000
			self.board.run(dt, event_list)
			pygame.display.update()

def main():
	game = Game()
	game.run()

if __name__ == '__main__':
    main()