import pygame
from graphics import Graphics
from interface import Interface

Graphics.init()

while True:
	Graphics.render()
	Interface.handle_events()
	pygame.time.Clock().tick(30)	#This is incredibly incorrect (the clock should be at the start of the loop)
									#but I don't know where to the time lapse. A new class?
	