import pygame
import time
import random
print("version 1.8")
health = 50
move = True
movex = 10
movey = 10
x3 = 10
y3 = 10
x2 = 20
y2 = 20
x = 500
y = 500
x4 = 10
y4 = 10
xgoto = 10
ygoto = 10
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (200,200,200)
DARK_GREY = (100,100,100)
DARK_DARK_GREY = (50,50,50)
DARK_GREEN = (0,200,0)
DARK_RED = (200,0,0)
DARK_BLUE = (0,0,100)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (130,0,130)
DARK_PURPLE = (100,0,100)
YELLOW = (255,255,0)
while True:
    pygame.init()
    windowsurface = pygame.display.set_mode((1000, 700), 0, 32)
    pygame.display.set_caption("chasing game")
    windowsurface.fill(DARK_DARK_GREY)
    pygame.draw.rect(windowsurface, GREY, (0, 0, 1000, 100))
    top = pygame.draw.rect(windowsurface, DARK_GREY, (0, 0, 1000, 40))
    pygame.display.update()
    player = pygame.draw.rect(windowsurface, GREEN, (x, y, 50, 50))
    pygame.draw.rect(windowsurface, DARK_GREEN, (x, y, 50, 20))

    if random.randint(0,20) == 1:
        move = False
        pygame.draw.rect(windowsurface, DARK_BLUE, (x2, y2, 50, 50))
        pygame.display.update()
        if random.randint(1,2) == 1:
            y2 = random.randint(y - 100 - 150, y + 100  + 150)
            x2 = random.randint(x - 150,x + 150)
        else:
            y2 = random.randint(y3 - 100 - 150, y3 + 100 + 150)
            x2 = random.randint(x3 - 150, x3 + 150)
        move = True
    chaser = pygame.draw.rect(windowsurface, RED, (x2, y2, 50, 50))
    pygame.draw.rect(windowsurface, DARK_RED, (x2, y2, 50, 20))
    pygame.draw.rect(windowsurface, RED, (x2 - 2, y2 - 15, 55, 4))
    chaserhealth = pygame.draw.rect(windowsurface, GREEN, (x2 - 2, y2 - 15, health, 4))
    pygame.display.update()
    if not health == 0:
        health = health - 0.1
    x3 = x3 + movex
    y3 = y3 + movey
    if health == 0:
        time.sleep(1)
        break
    pong_player = pygame.draw.rect(windowsurface, PURPLE, (x3, y3, 50, 50))
    pygame.draw.rect(windowsurface, DARK_PURPLE, (x3, y3, 50, 20))
    if pong_player.colliderect(top):
        movey = 10
    elif pong_player.colliderect(bottom):
        movey = -10
    elif pong_player.colliderect(left):
        movex = 10
    elif pong_player.colliderect(right):
        movex = -10
    if chaser.colliderect(pong_player):
        health = 50
    bottom = pygame.draw.rect(windowsurface, GREY, (0, 600, 1000, 100))
    pygame.draw.rect(windowsurface, DARK_GREY, (0, 600, 1000, 40))
    left = pygame.draw.rect(windowsurface, DARK_GREY, (0, 0, 40, 600))
    right = pygame.draw.rect(windowsurface, DARK_GREY, (965, 0, 40, 600))
    pygame.display.update()
    if player.colliderect(top):
        y += 10
    elif player.colliderect(bottom):
        y -= 10
    elif player.colliderect(left):
        x += 10
    elif player.colliderect(right):
        x -= 10
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                x = x - 10
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                x = x + 10
            if event.key == pygame.K_UP or event.key == ord('w'):
                y = y - 10
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                y = y + 10
            if event.key == ord('q'):
                pygame.quit()
                break
    if  not move == False:
        if x > x2:
            x2 = x2 + 5
            time.sleep(0.1)
        else:
            x2 = x2 - 5
            time.sleep(0.1)
        if y > y2:
            y2 = y2 + 5
            time.sleep(0.1)
        else:
            y2 = y2 - 5
            time.sleep(0.1)
    if player.colliderect(chaser) or player.colliderect(pong_player):
        time.sleep(1)
        break
