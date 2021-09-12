import pygame
import colors

class Balloon(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.image = pygame.Surface((100, 100), pygame.SRCALPHA, 32)
        pygame.draw.line(self.image, colors.BLUE, (0, 0), (100, 100), 1)
        pygame.draw.line(self.image, colors.BLUE, (0, 100), (100, 0), 1)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
    def update(self):
        self.y -= 0.1
        self.rect.center = (self.x, self.y)
