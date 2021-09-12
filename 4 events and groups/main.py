import pygame
import colors
from balloon import *
SIZE = (800, 600)
pygame.init()
screen = pygame.display.set_mode(SIZE)
running = True
clock = pygame.time.Clock()
b = Balloon(300, 400)
balloons = pygame.sprite.Group()
balloons.add(b)
while (running):
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            for b in balloons:
                if (b.pierce(event.pos)):
                    break
            else:
                balloons.add(Balloon(event.pos[0], event.pos[1]))
        if event.type == pygame.QUIT:
            running = False
    screen.fill(colors.BLACK)
    balloons.draw(screen)
    balloons.update()
    pygame.display.flip()
    clock.tick()
pygame.quit()
