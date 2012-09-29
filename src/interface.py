import pygame
from pygame.locals import *
import sys

mouse_x = mouse_y = 0

def handle_events():
	for e in pygame.event.get():
		if e.type == QUIT:
			pygame.quit()
			sys.exit()
		elif e.type == MOUSEMOTION:
			mouse_x, mouse_y = e.pos
		elif e.type == MOUSEBUTTONUP:
			mouse_x, mouse_y = e.pos
			#e.button returns 1, 2, or 3 for l/m/r mouse clicks and 4 or 5 for scrolling up/down
		elif e.type == KEYDOWN:
			if e.key == K_ESCAPE:
				pygame.event.post(pygame.event.Event(QUIT))
