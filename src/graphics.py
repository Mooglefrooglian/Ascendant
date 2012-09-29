import pygame

window = None

def init():
	global window
	
	pygame.init()
	window = pygame.display.set_mode((640, 480))
	pygame.display.set_caption("Ascendant Alpha")
	window.fill(pygame.Color(0, 0, 0)) #A splash screen should go here.
	pygame.display.update()
	
def render():
	window.fill(pygame.Color(0, 0, 0))
	pygame.display.update()

