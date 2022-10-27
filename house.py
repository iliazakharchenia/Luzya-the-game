import pygame
import settings

class House(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('res/bg/house.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = settings.house_start_x
        self.rect.centery = settings.house_start_y
