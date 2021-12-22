import pygame
import os  # to define path to the images
from settings import *
from GameObject import GameObject  # from filename import className


class Virus(GameObject):  # (Vererbung)
    def __init__(self):  # runs whenever a new object of this type is made
        super().__init__()  # necessary, but why? from clear code tutorial https://www.youtube.com/watch?v=hDu8mcAlY4E
        self.image = pygame.transform.scale(pygame.image.load(os.path.join('assets', "virus.png")),
                                            (VIRUS_WIDTH, VIRUS_HEIGHT))  # resize image
        self.rect = pygame.Rect(810, 410, VIRUS_WIDTH, VIRUS_HEIGHT)  # position - shorter with surface.get_rect()
        self.VELOCITY_VIRUS = 5
        self.rotation_angle = 0

    def rotate(self, surface, angle):
        rotated_surface = pygame.transform.rotozoom(surface, angle, 1)
        rotated_rect = pygame.Rect(self.rect.x, self.rect.y, VIRUS_WIDTH, VIRUS_HEIGHT)
        return rotated_surface, rotated_rect
