import pygame
import os
from game import game
import messaging
import camera

class Drawable():
	def __init__(self,x,y,image,scale=1.0):
		self.x=x
		self.y=y
		self.image=image
		self.scale=scale
		self.width=scale*image.get_width()
		self.height=scale*image.get_height()

def show_splash_screen():
	pygame.font.init()
	pygame.init()
	os.environ['SDL_VIDEO_CENTERED'] = '1' #center the splashscreen
	window = game.graphics.window = pygame.display.set_mode((500, 500), pygame.NOFRAME)
	splash = pygame.transform.scale(pygame.image.load('resources/splash.png'), (500, 500))
	window.blit(splash, (0,0)) 
	window.blit(pygame.font.Font("resources/fonts/visitor.ttf", 9).render('Loading...', 1, (255,255,255)), (30,20))
	pygame.display.update() 
	
def init():
	game.graphics.camera=camera.Camera(0,0,game.graphics.resolution_x,game.graphics.resolution_y)
	game.graphics.camera.disableInput()
	game.graphics.drawables.append(Drawable(0,0,pygame.image.load("resources/splash.png")))
	#load sprites?
	
def finalize():
	window = game.graphics.window = pygame.display.set_mode((game.graphics.resolution_x, game.graphics.resolution_y))
	pygame.display.set_caption("Ascendant Alpha " + game.VERSION)
	
	window.fill(pygame.Color(0, 0, 0)) 
	pygame.display.update()
	game.graphics.base_ui.render()
	
def render():
	#Render game graphics!
	game.graphics.window.fill(pygame.Color(0, 0, 0))
	#Draw game world
	game.graphics.camera.update()
	#Render UI
	game.graphics.base_ui.render()
	#Call miscellaneous "every frame" functions
	messaging.propagate("new_frame")
	#Finalize this rendering of the game
	pygame.display.update()

