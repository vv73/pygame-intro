import pygame
import colors
import drawutils

class Balloon(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self._img = pygame.image.load("pics/balloon.png").convert_alpha()
        self.image = pygame.Surface(self._img.get_size(), pygame.SRCALPHA, 32)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
    def update(self):
        self.y -= 0.1
        self.rect.center = (self.x, self.y)
        self.image.fill((255, 255, 255, 0))
        self.image.blit(self._img, (0, 0))
        drawutils.drawText(self.image, colors.WHITE, f"H{600-int(self.y)}", (30, 100), font_size=32)

