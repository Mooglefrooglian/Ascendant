import pygame
import tkMessageBox
from twisted.internet import reactor
#from pygame.locals import * # BAD MOOGLE NO WILDCARD IMPORTS
from variables import game
import messaging

def handle_events():
	#When focus is lost or gained, fire appropriate events
	if not(pygame.key.get_focused()):
		if game.graphics.lastFocused:
			game.graphics.lastFocused=False
			messaging.propagate("Focus-Lost")
	elif game.graphics.lastFocused==False:
		game.graphics.lastFocused=True
		messaging.propagate("Focus-Gained")
		
	pygame.event.pump()
	for event in pygame.event.get():
		r = event.type
		if r==pygame.locals.ACTIVEEVENT:
			n = str(r) + "-" + str(event.gain) + "-" + str(event.state)
		elif r==pygame.locals.KEYDOWN:
			n = str(r) + "-" + str(event.key)
		elif r==pygame.locals.KEYUP:
			n = str(r) + "-" + str(event.key)
		elif r==pygame.locals.MOUSEBUTTONUP:
			n = str(r) + "-" + str(event.button)
		elif r==pygame.locals.MOUSEBUTTONDOWN:
			n = str(r) + "-" + str(event.button)
		elif r==pygame.locals.QUIT:
			if tkMessageBox.askyesno("Quit", "Do you really want to quit?"):
				game.running=False
				n="QUIT"
			else:
				n=""
		else:
			n=str(r)
		messaging.propagate(n,[event])
