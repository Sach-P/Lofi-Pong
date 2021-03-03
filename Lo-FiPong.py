import pygame
import random

from pygame.locals import (
	K_a,
	K_s,
	K_d,
	K_ESCAPE,
	QUIT,
	KEYDOWN,
)

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800
colorChangeBlue = 5
colorIncrementBlue = 2
colorChangeGreen = 5
colorIncrementGreen = 0
colorChangeRed = 5
colorIncrementRed = 0

#FIXME: add a player and enemy class

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		elif event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				running = False

	screen.fill((colorChangeRed, colorChangeGreen, colorChangeBlue))

	if colorChangeBlue < 220 and colorChangeBlue >= 5:
		colorChangeBlue += colorIncrementBlue
	elif colorChangeBlue < 5:
		colorIncrementBlue = 0
		colorChangeBlue = 5
	else:
		colorIncrementBlue = -2
		colorChangeBlue += colorIncrementBlue
		colorIncrementGreen = 2

	if colorChangeGreen < 220 and colorChangeGreen >= 5:
		colorChangeGreen += colorIncrementGreen
	elif colorChangeGreen < 5:
		colorIncrementGreen = 0
		colorChangeGreen = 5
	else:
		colorIncrementGreen = -2
		colorChangeGreen += colorIncrementGreen
		colorIncrementRed = 2

	if colorChangeRed < 220 and colorChangeRed >= 5:
		colorChangeRed += colorIncrementRed
	elif colorChangeRed < 5:
		colorIncrementRed = 0
		colorChangeRed = 5
	else:
		colorIncrementRed = -2
		colorChangeRed += colorIncrementRed
		colorIncrementBlue = 2

	pygame.display.flip()

	clock.tick(30)

pygame.quit()