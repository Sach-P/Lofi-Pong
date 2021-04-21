import pygame
import random
import math

from pygame.locals import(
    RLEACCEL,
    K_a,
    K_s,
    K_d,
    K_LEFT,
    K_RIGHT,
    K_DOWN,
    K_UP,
    K_ESCAPE,
    K_SPACE,
    KEYDOWN,
    QUIT,
)

f = open('timeBtwnBeats.txt', 'r')
FRAME_RATE = 60

start_delay = FRAME_RATE * float(f.readline())

class StartScreen(pygame.sprite.Sprite):
    def __init__(self):
        super(StartScreen, self).__init__()
        self.surf = pygame.image.load("StartScreen.png").convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.surf.get_rect(center=(SCREEN_WIDTH / 2 + 100, SCREEN_HEIGHT / 2 - 100))

class Table(pygame.sprite.Sprite):
    def __init__(self):
        super(Table, self).__init__()
        self.surf = pygame.Surface((400, 600))
        self.surf.fill((100, 150, 150))
        self.rect = self.surf.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))

class Net(pygame.sprite.Sprite):
    def __init__(self):
        super(Net, self).__init__()
        self.surf = pygame.image.load("Net.png").convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.surf.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.image.load("BluePaddleMid.png").convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.Lx = SCREEN_WIDTH / 2 - 150
        self.Mx = SCREEN_WIDTH / 2
        self.Rx = SCREEN_WIDTH / 2 + 150
        self.y = SCREEN_HEIGHT - 85
        self.rect = self.surf.get_rect(center=(self.Mx, self.y))

    def update(self, pressed_keys):
        if pressed_keys[K_a] or pressed_keys[K_LEFT]:
            self.rect = self.surf.get_rect(center=(self.Lx, self.y))
            self.surf = pygame.image.load("BluePaddleLeft.png").convert()
            self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        if pressed_keys[K_s] or pressed_keys[K_DOWN] or pressed_keys[K_UP]:
            self.rect = self.surf.get_rect(center=(self.Mx, self.y))
            self.surf = pygame.image.load("BluePaddleMid.png").convert()
            self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
            self.rect = self.surf.get_rect(center=(self.Rx, self.y))
            self.surf = pygame.image.load("BluePaddleRight.png").convert()
            self.surf.set_colorkey((0, 0, 0), RLEACCEL)

class Opponent(pygame.sprite.Sprite):
    def __init__(self):
        super(Opponent, self).__init__()
        self.surf = pygame.image.load("RedPaddleMid.png").convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.Lx = SCREEN_WIDTH / 2 - 150
        self.Mx = SCREEN_WIDTH / 2
        self.Rx = SCREEN_WIDTH / 2 + 150
        self.y = 85
        self.rect = self.surf.get_rect(center=(self.Mx, self.y))

    def update(self):
        if ball.endOfFile and ball.centerY < (SCREEN_HEIGHT / 2)  and ball.toY == ball.tY:
            self.rect = self.surf.get_rect(center=(ball.toX - 75, 85))
            if ball.toX == ball.Mx:
                self.surf = pygame.image.load("RedPaddleMid.png").convert()
                self.surf.set_colorkey((0, 0, 0), RLEACCEL)
            if ball.toX == ball.Lx:
                self.surf = pygame.image.load("RedPaddleLeft.png").convert()
                self.surf.set_colorkey((0, 0, 0), RLEACCEL)
            if ball.toX == ball.Rx:
                self.surf = pygame.image.load("RedPaddleRight.png").convert()
                self.surf.set_colorkey((0, 0, 0), RLEACCEL)

        elif ball.centerY < (SCREEN_HEIGHT / 2) and ball.toY == ball.tY:
            self.rect = self.surf.get_rect(center=(ball.toX, 85))
            if ball.toX == ball.Mx:
                self.surf = pygame.image.load("RedPaddleMid.png").convert()
                self.surf.set_colorkey((0, 0, 0), RLEACCEL)
            if ball.toX == ball.Lx:
                self.surf = pygame.image.load("RedPaddleLeft.png").convert()
                self.surf.set_colorkey((0, 0, 0), RLEACCEL)
            if ball.toX == ball.Rx:
                self.surf = pygame.image.load("RedPaddleRight.png").convert()
                self.surf.set_colorkey((0, 0, 0), RLEACCEL)

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super(Ball, self).__init__()
        self.surf = pygame.image.load("ball.png").convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.surf.get_rect(center=(SCREEN_WIDTH / 2, 100))

        self.bY = SCREEN_HEIGHT - 100
        self.tY = 100

        self.Lx = SCREEN_WIDTH / 2 - 150
        self.Mx = SCREEN_WIDTH / 2
        self.Rx = SCREEN_WIDTH / 2 + 150

        self.toY = 0
        self.toX = 0
        self.dx = 0
        self.dy = 0

        self.r = random.randint(1, 3)

        self.mult = 0
        self.endOfFile = False

        self.centerX, self.centerY = self.rect.center
      
    def update(self):

        self.centerX, self.centerY = self.rect.center

        self.simulate()

        if self.r == 1:
            self.toX = self.Lx
        elif self.r == 2:
            self.toX = self.Mx
        elif self.r == 3:
            self.toX = self.Rx
        
        if (self.toX - self.centerX != 0):
            self.dx = (self.toX - self.centerX) / abs(self.toY - self.centerY)

        self.rect.move_ip(self.dx * self.mult, self.dy * self.mult)  

    def simulate(self):

        opponent.update()
            
        if self.centerY <= self.tY and pygame.sprite.collide_rect(self, opponent):
            self.r = random.randint(1, 3)
            self.toY = self.bY
            next_line = f.readline()
            if next_line:
                self.mult = abs(self.toY - self.centerY) / (FRAME_RATE * float(next_line))
            else:
                self.endOfFile = True
            if (self.toY - self.centerY != 0):
                self.dy = 1
        
        elif self.centerY >= self.bY and pygame.sprite.collide_rect(self, player):
            self.r = random.randint(1, 3)
            self.toY = self.tY
            next_line = f.readline()
            if next_line:
                self.mult = abs(self.toY - self.centerY) / (FRAME_RATE * float(next_line))
            else:
                self.endOfFile = True
            if (self.toY - self.centerY != 0):
                self.dy = -1
  

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800

colorChangeBlue = 220
colorIncrementBlue = 2
colorChangeGreen = 5
colorIncrementGreen = 0
colorChangeRed = 5
colorIncrementRed = 0
t = 0

screenStart = pygame.display.set_mode([SCREEN_HEIGHT, SCREEN_WIDTH])

entities = pygame.sprite.Group()

table = Table()
entities.add(table)
player = Player()
entities.add(player)
opponent = Opponent()
entities.add(opponent)
ball = Ball()
entities.add(ball)
net = Net()
entities.add(net)

clock = pygame.time.Clock()

startScreen = StartScreen()

start = True
running = True
while start:
    for event in pygame.event.get():

        if event.type == KEYDOWN and event.key == K_ESCAPE:
                start = False
                running = False

        if event.type == KEYDOWN and event.key == K_SPACE:
                start = False

        if event.type == pygame.QUIT:
            start = False  
            running = False  
    screenStart.blit(startScreen.surf, startScreen.rect)
    pygame.display.flip()

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
while running:
    for event in pygame.event.get():

        if event.type == KEYDOWN and event.key == K_ESCAPE:
                running = False

                
        if event.type == pygame.QUIT:
            running = False

    screen.fill((colorChangeRed, colorChangeGreen, colorChangeBlue))

    if colorChangeBlue < 200 and colorChangeBlue >= 5:
        colorChangeBlue += colorIncrementBlue
    elif colorChangeBlue < 5:
        colorIncrementBlue = 0
        colorChangeBlue = 5
    else:
        colorIncrementBlue = -2
        colorChangeBlue += colorIncrementBlue
        colorIncrementGreen = 2

    if colorChangeGreen < 200 and colorChangeGreen >= 5:
        colorChangeGreen += colorIncrementGreen
    elif colorChangeGreen < 5:
        colorIncrementGreen = 0
        colorChangeGreen = 5
    else:
        colorIncrementGreen = -2
        colorChangeGreen += colorIncrementGreen
        colorIncrementRed = 2

    if colorChangeRed < 200 and colorChangeRed >= 5:
        colorChangeRed += colorIncrementRed
    elif colorChangeRed < 5:
        colorIncrementRed = 0
        colorChangeRed = 5
    else:
        colorIncrementRed = -2
        colorChangeRed += colorIncrementRed
        colorIncrementBlue = 2

    pressed_keys = pygame.key.get_pressed()

    player.update(pressed_keys)
    if start_delay == 0:
        ball.update()
    else:
        start_delay -= 1

    if ball.centerY < 0:
        print("You Win!")
        running = False

    elif ball.centerY > SCREEN_HEIGHT:
        print("You Lose :(")
        running = False

    for entity in entities:
        screen.blit(entity.surf, entity.rect)

    pygame.display.flip()

    clock.tick(FRAME_RATE)

f.close()
pygame.quit()