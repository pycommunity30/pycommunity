from pynput.mouse import Button, Controller
import pygame
pygame.init()
mouse = Controller()
RED = (255, 0, 0)
BLACK = (0, 0, 0)
xball = 400
yball = 250
WHITE = (255, 255, 255)
GREY = (200,200,200)
DARK_GREY = (100,100,100)
DARK_DARK_GREY = (50,50,50)
DARK_GREEN = (0,200,0)
DARK_RED = (200,0,0)
DARK_BLUE = (0,0,100)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
speed = 5
PURPLE = (130,0,130)
DARK_PURPLE = (100,0,100)
YELLOW = (255,255,0)
xchange = speed
ychange = speed
while True:

    
    xball = xball + xchange
    yball = yball + ychange
    y = mouse.position[1]
    pygame.init()
    windowsurface = pygame.display.set_mode((1000, 700), 0, 32)
    pygame.display.set_caption("pong")
    windowsurface.fill(BLACK)
    paddle = pygame.draw.rect(windowsurface, WHITE, (10, y - 140, 25, 140))
    ball = pygame.draw.rect(windowsurface, WHITE, (xball,yball,30,30))
    aipaddle = pygame.draw.rect(windowsurface, WHITE, (1000 - 32, yball - 75, 25, 140))
    pygame.display.update()
    if yball > 670 or yball == 0:
        ychange = 0 - ychange
    if ball.colliderect(paddle) or ball.colliderect(aipaddle):
        xchange = 0 - xchange
    if xball == 0:
        pygame.quit()
        break