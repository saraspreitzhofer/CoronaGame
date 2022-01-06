import pygame
from settings import *


class PointsCounter(pygame.sprite.Sprite):
    def __init__(self):  # runs whenever a new object of this type is made
        super().__init__()  # necessary, but why? from clear code tutorial https://www.youtube.com/watch?v=hDu8mcAlY4E
        # invisible counter object positioned at end of screen to detect virus that was not killed by collision with
        # runner
        self.image = pygame.Surface([1, VIRUS_HEIGHT]) #
        self.image.fill(WHITE)  # pointscounter should be invisible
        self.rect = self.image.get_rect(topleft=(0, VIRUS_Y))
