import pygame
import random
import math

from pygame.locals import(
    K_a,
    K_s,
    K_d,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

class Table(pygame.sprite.Sprite):
    def __init__(self):
        super(Table, self).__init__()
        self.surf = pygame.Surface((400, 600))
        self.surf.fill((100, 150, 150))
        self.rect = self.surf.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75, 35))
        self.surf.fill((255, 230, 255))
        self.rect = self.surf.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT - 50))

    def update(self, pressed_keys):
        if pressed_keys[K_a]:
            self.rect = self.surf.get_rect(center=(SCREEN_WIDTH / 2 - 200, SCREEN_HEIGHT - 50))
        if pressed_keys[K_s]:
            self.rect = self.surf.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT - 50))
        if pressed_keys[K_d]:
            self.rect = self.surf.get_rect(center=(SCREEN_WIDTH / 2 + 200, SCREEN_HEIGHT - 50))

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super(Ball, self).__init__()
        self.surf = pygame.Surface((20, 20))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect(center=(SCREEN_WIDTH / 2, 100))
        self.bY = SCREEN_HEIGHT - 100
        self.tY = 100

        self.Lx = SCREEN_WIDTH / 2 - 200
        self.Mx = SCREEN_WIDTH / 2
        self.Rx = SCREEN_WIDTH / 2 + 200

        self.toY = 0
        self.toX = 0
        self.dx = 0
        self.dy = 0
      

    def update(self):

        centerX, centerY = self.rect.center

        r = random.randint(1, 3)

        if r == 1:
            self.toX = self.Lx
        elif r == 2:
            self.toX = self.Mx
        elif r == 3:
            self.toX = self.Rx

        if centerY <= self.tY:
            self.toY = self.bY
            if (self.toX - centerX != 0):
                self.dx = (self.toX - centerX)/abs(self.toY - centerY)
            if (self.toY - centerY != 0):
                self.dy = 1
        
        elif centerY >= self.bY:
            self.toY = self.tY
            if (self.toX - centerX != 0):
                self.dx = (self.toX - centerX)/abs(self.toY - centerY)
            if (self.toY - centerY != 0):
                self.dy = -1




        self.rect.move_ip(self.dx * 10, self.dy * 10)   

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800


entities = pygame.sprite.Group()

table = Table()
entities.add(table)
player = Player()
entities.add(player)
ball = Ball()
entities.add(ball)



screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

clock = pygame.time.Clock()

running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():

        if event.type == KEYDOWN and event.key == K_ESCAPE:
                running = False

                
        if event.type == pygame.QUIT:
            running = False

    pressed_keys = pygame.key.get_pressed()

    screen.fill((0, 0, 0))

    player.update(pressed_keys)
    ball.update()

    for entity in entities:
        screen.blit(entity.surf, entity.rect)

    pygame.display.flip()

pygame.quit()