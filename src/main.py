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
#-------------------------------------------------------------------------------
#General game initialization
#Pygame specific
pygame.font.init()
pygame.init()
#
clock=game.clock.pygame.time.Clock()
#
graphics.initTitleScreen()
#-------------------------------------------------------------------------------
interface.mainTitleScreenLoop()

