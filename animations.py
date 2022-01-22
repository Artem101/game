import pygame
from pygame.locals import *
import pyganim

pygame.init()
windowSurface = pygame.display.set_mode((1800, 1000), 0, 32)
pygame.display.set_caption('Pyganim Basic Demo')

boltAnim = pyganim.PygAnimation([('red_car.png', 100)])
boltAnim.play()


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

    windowSurface.fill((100, 50, 50))
    boltAnim.blit(windowSurface, (100, 50))
    pygame.display.update()
