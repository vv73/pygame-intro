import pygame
import colors

def drawText(surface, color, text, where, font_name = "consolas", font_size = 16):
    font = pygame.font.SysFont(font_name, font_size)
    text = font.render(text, True, color)
    text_rect = text.get_rect()
    if type(where) is pygame.Rect:
        text_rect.center = where.center
    else:
        text_rect.topleft = where
    surface.blit(text, text_rect)
