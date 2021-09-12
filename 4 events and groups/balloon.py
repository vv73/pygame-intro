import pygame
import colors
import drawutils

class Balloon(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.state = "UP"
        self._img = pygame.image.load("pics/balloon.png").convert_alpha()
        self.image = pygame.Surface(self._img.get_size(), pygame.SRCALPHA, 32)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
    def update(self):
        if self.state == "UP":
            self.y -= 0.05
        else:
            self.y += 1
        if self.state == "BOOM":
            print(pygame.time.get_ticks() - self.boom_time)
        if self.state == "BOOM" and pygame.time.get_ticks() - self.boom_time > 100:
            self._img = pygame.image.load("pics/thread.png").convert_alpha()
            self.state = "THREAD"
        self.image.fill((255, 255, 255, 0))
        self.image.blit(self._img, (0, 0))
        drawutils.drawText(self.image, colors.BLACK, f"H {600-int(self.y)}",(20, 30), font_size=32)
        self.rect.center = (self.x, self.y)
    def pierce(self, pos):
        if self.state != "UP":
            return False
        if self.rect.collidepoint(pos):
            self._img = pygame.image.load("pics/boom.png").convert_alpha()
            self.state = "BOOM"
            self.boom_time = pygame.time.get_ticks()
            return True
        return False

