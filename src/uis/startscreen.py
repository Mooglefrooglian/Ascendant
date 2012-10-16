from game import game
from ui import UI
import pygame

def init():
	game.graphics.uis['start_screen'] = StartScreenUI()
	
class StartScreenUI(UI):
	def __init__(self):
		super(StartScreenUI, self).__init__()
		self.events = [['2-13', self.enter_pushed]]
		#Set up font
		self.font = pygame.font.SysFont("Arial", 20) #NEEDS A TEXT CLASS
		self.color = (255, 255, 255) #white
	
	def enter_pushed(self, args):
		self.color = (255, 0, 0) #turn red when enter is pushed?
		
	def render(self):
		window = game.graphics.window #NEEDS A TEXT CLASS SO HARD
		window.blit(self.font.render('Play', 1, self.color), (20,20))
	
		super(StartScreenUI, self).render() #Renders children, not necessary I guess?