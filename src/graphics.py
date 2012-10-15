import pygame
import os
import time
from variables import game

def initTitleScreen():
	os.environ['SDL_VIDEO_CENTERED'] = '1'
	window = game.graphics.window = pygame.display.set_mode((500, 500), pygame.NOFRAME)
	splash = pygame.transform.scale(pygame.image.load('resources/splash.png'), (500, 500))
	window.blit(splash, (0,0)) 
	window.blit(pygame.font.SysFont("Arial", 9).render('Loading...', 1, (255,255,255)), (30,20))
	pygame.display.update() 
	
	time.sleep(5) #loading should go here
	
	window = game.graphics.window = pygame.display.set_mode((1000, 1000))
	pygame.display.set_caption("Ascendant Alpha")
	window.fill(pygame.Color(0, 0, 0)) 
	pygame.display.update()
	
def render():
	game.graphics.window.fill(pygame.Color(0, 0, 0))
	pygame.display.update()

