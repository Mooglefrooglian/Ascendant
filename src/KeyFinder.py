import pygame, sys
"""Run stand-alone. Allows you to find out what events correspond to what
code."""
pygame.init()
screen = pygame.display.set_mode((200,200))
clock = pygame.time.Clock() 
#pygame.event.set_blocked(pygame.MOUSEMOTION)
while True:
    clock.tick(5)
    for event in pygame.event.get():
        print(event)
