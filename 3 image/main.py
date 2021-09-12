import pygame
import colors
from balloon import *
SIZE = (800, 600)
FPS = 60
pygame.init()
running = True
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
r = 10
b = Balloon(400, 500)
all_sprites = pygame.sprite.Group()
all_sprites.add(b)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(colors.BLACK)
    #pygame.draw.line(screen, colors.WHITE, (0, 0), (800, 600), 10)
    #pygame.draw.circle(screen, colors.RED, (400, 300), r, 0)
    #r += 1

    all_sprites.draw(screen)
    all_sprites.update()

    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()

