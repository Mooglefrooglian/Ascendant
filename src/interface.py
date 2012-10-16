import pygame
from pygame import locals
import tkMessageBox
from twisted.internet import reactor
from game import game
import messaging

def handle_events():
	#When focus is lost or gained, fire appropriate events
	if not(pygame.key.get_focused()):
		if game.graphics.lastFocused:
			game.graphics.last_focused = False
			messaging.propagate("Focus-Lost")
	elif not game.graphics.last_focused:
		game.graphics.last_focused=True
		messaging.propagate("Focus-Gained")
		
	pygame.event.pump() #This line is NOT STRICTLY NECESSARY see http://www.pygame.org/docs/ref/event.html#pygame.event.pump
	messaging.pump_messaging()
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
				continue
		else:
			n=str(r)
		messaging.propagate(n,[event])
