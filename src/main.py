#-------------------------------------------------------------------------------
#						Ascendant Alpha Source Code
#			By the illustrious Fel and the enigmatic Mooglefrooglian
#-------------------------------------------------------------------------------
#Imports
import pygame
import twisted
from twisted.internet import reactor
#
from variables import game
import graphics
import interface
import messaging
#-------------------------------------------------------------------------------
#General game initialization
#Pygame specific
pygame.font.init()
pygame.init()
#
clock=game.clock=pygame.time.Clock()
#
graphics.initTitleScreen()
#-------------------------------------------------------------------------------

while game.running:
	game.frameTime=game.clock.tick(60)
	#Handle user input
	interface.handle_events()
	#Handle internet events (and eventually game logic)
	reactor.iterate()
	#Draw pretty things
	graphics.render()
#GAME OVER MAN, GAME OVER	


