import pygame
import random

from pygame.locals import (
	K_A,
	K_S,
	K_D,
	K_ESCAPE,
	QUIT,
	KEYDOWN,
)

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800

#FIXME: add a player and enemy class

pygame.itit()

screen = pygame.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		elif event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				running = False

	screen.fill(0, 0, 0)

	pygame.display.flip()

pygame.quit()