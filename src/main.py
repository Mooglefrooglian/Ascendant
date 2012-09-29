import pygame
import graphics
import interface

graphics.init()

while True:
	graphics.render()
	interface.handle_events()
	pygame.time.Clock().tick(30)	#This is incredibly incorrect (the clock should be at the start of the loop)
									#but I don't know where to the time lapse. A new class?
	