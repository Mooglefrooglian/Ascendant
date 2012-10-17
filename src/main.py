#-------------------------------------------------------------------------------
#						Ascendant Alpha Source Code
#			By the illustrious Fel and the enigmatic Mooglefrooglian
#-------------------------------------------------------------------------------
import pygame
pygame.init() #needed for other code to not become sad

#Imports
import twisted
import time
from twisted.internet import reactor
#
from game import game
import graphics
import interface
import messaging

#-------------------------------------------------------------------------------
#Initialization
graphics.show_splash_screen()

clock=game.clock=pygame.time.Clock()
graphics.init()
interface.init()

time.sleep(2) #More loading goes in this area!



graphics.finalize()
#-------------------------------------------------------------------------------

while game.running:
	game.frame_time=game.clock.tick(60)
	#Handle user input
	interface.handle_events()
	#Deal with any timed events (MAYBE THIS SHOULD BE DEALT WITH IN THE REACTOR.ITERATE BIT?)
	messaging.pump_messaging()
	#Handle internet events (and eventually game logic)
	reactor.iterate()
	#Draw pretty things
	graphics.render()
#GAME OVER MAN, GAME OVER	


