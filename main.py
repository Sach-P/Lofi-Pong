import pygame
import random
import math

from pygame.locals import(
    K_a,
    K_s,
    K_d,
    K_LEFT,
    K_RIGHT,
    K_DOWN,
    K_UP,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# this file indicates the times between the beats of the song
f = open('timeBtwnBeats.txt', 'r')

FRAME_RATE = 60

# this is a daley for the first move from the first line of the txt file so the game doesn't start right away.
start_delay = FRAME_RATE * float(f.readline())

class Table(pygame.sprite.Sprite):
    def __init__(self):
        super(Table, self).__init__()
        self.surf = pygame.Surface((400, 600))
        self.surf.fill((100, 150, 150))
        self.rect = self.surf.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))

# the player (the bottom paddle) uses a combination of 3 keys to move to three different locations.
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75, 35))
        self.surf.fill((255, 230, 255))
        self.Lx = SCREEN_WIDTH / 2 - 150
        self.Mx = SCREEN_WIDTH / 2
        self.Rx = SCREEN_WIDTH / 2 + 150
        self.y = SCREEN_HEIGHT - 85
        self.rect = self.surf.get_rect(center=(self.Mx, self.y))

    def update(self, pressed_keys):
        if pressed_keys[K_a] or pressed_keys[K_LEFT]:
            self.rect = self.surf.get_rect(center=(self.Lx, self.y))
        if pressed_keys[K_s] or pressed_keys[K_DOWN] or pressed_keys[K_UP]:
            self.rect = self.surf.get_rect(center=(self.Mx, self.y))
        if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
            self.rect = self.surf.get_rect(center=(self.Rx, self.y))

# The opponent just moves to the balls x position until the last line of the file, where it just misses the ball so the player wins.
class Opponent(pygame.sprite.Sprite):
    def __init__(self):
        super(Opponent, self).__init__()
        self.surf = pygame.Surface((75, 35))
        self.surf.fill((255, 230, 255))
        self.Lx = SCREEN_WIDTH / 2 - 150
        self.Mx = SCREEN_WIDTH / 2
        self.Rx = SCREEN_WIDTH / 2 + 150
        self.y = 85
        self.rect = self.surf.get_rect(center=(self.Mx, self.y))

    def update(self):
        if ball.endOfFile and ball.centerY < (SCREEN_HEIGHT / 2)  and ball.toY == ball.tY:
            self.rect = self.surf.get_rect(center=(ball.toX - 75, 85))

        elif ball.centerY < (SCREEN_HEIGHT / 2) and ball.toY == ball.tY:
            self.rect = self.surf.get_rect(center=(ball.toX, 85))

# when the ball is hit by the player or opponent, it choses a random preset x position to move to and moves to the opposite side of the table
# in a given time read from the text file.
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super(Ball, self).__init__()
        self.surf = pygame.Surface((20, 20))
        self.surf.fill((255, 255, 255))
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

entities = pygame.sprite.Group()

table = Table()
entities.add(table)
player = Player()
entities.add(player)
ball = Ball()
entities.add(ball)
opponent = Opponent()
entities.add(opponent)

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():

        if event.type == KEYDOWN and event.key == K_ESCAPE:
                running = False

                
        if event.type == pygame.QUIT:
            running = False



    screen.fill((0, 0, 0))

    pressed_keys = pygame.key.get_pressed()

    player.update(pressed_keys)

    # ball only starts moving when the start delay is zero.
    if start_delay == 0:
        ball.update()
    else:
        start_delay -= 1

    # If the txt file has no more lines left, the song is over and the player wins.
    if ball.centerY < 0:
        print("You Win!")
        # TODO make this pop up a you win screen instead of closing the program.
        running = False

    # if the player misses the ball, the player loses
    elif ball.centerY > SCREEN_HEIGHT:
        print("You Lose :(")
        # TODO make this pop up a gameover screen instead of closing the program.
        running = False

    for entity in entities:
        screen.blit(entity.surf, entity.rect)

    pygame.display.flip()

    clock.tick(FRAME_RATE)

f.close()
pygame.quit()