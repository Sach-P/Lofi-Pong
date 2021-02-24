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