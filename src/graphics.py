import pygame
import os
from game import game
import ui

def show_splash_screen():
	pygame.font.init()
	pygame.init()
	os.environ['SDL_VIDEO_CENTERED'] = '1'
	window = game.graphics.window = pygame.display.set_mode((500, 500), pygame.NOFRAME)
	splash = pygame.transform.scale(pygame.image.load('resources/splash.png'), (500, 500))
	window.blit(splash, (0,0)) 
	window.blit(pygame.font.SysFont("Arial", 9).render('Loading...', 1, (255,255,255)), (30,20))
	pygame.display.update() 
	
def init():
	ui.init()
	#load sprites?
	
def finalize():
	window = game.graphics.window = pygame.display.set_mode((1000, 1000))
	pygame.display.set_caption("Ascendant Alpha")
	
	window.fill(pygame.Color(0, 0, 0)) 
	pygame.display.update()
	game.graphics.base_ui.render()
	
def render():
	#Render game graphics!
	game.graphics.window.fill(pygame.Color(0, 0, 0))
	pygame.display.update()
	
	#Render UI
	game.graphics.base_ui.render()

