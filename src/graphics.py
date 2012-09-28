import pygame

class Graphics:
	window = None
	
	@staticmethod
	def init():
		pygame.init()
		Graphics.window = pygame.display.set_mode((640, 480))
		pygame.display.set_caption("Ascendant Alpha")
		Graphics.window.fill(pygame.Color(0, 0, 0)) #A splash screen should go here.
		pygame.display.update()
		
	@staticmethod
	def render():
		Graphics.window.fill(pygame.Color(0, 0, 0))
		pygame.display.update()
	