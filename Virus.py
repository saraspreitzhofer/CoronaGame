import pygame
import os  # to define path to the images
from settings import *
from GameObject import GameObject   # from filename import className


class Virus(GameObject):  # (Vererbung)
    def __init__(self):  # runs whenever a new object of this type is made
        self.image = pygame.transform.scale(pygame.image.load(os.path.join('assets', "virus.png")),
                                            (VIRUS_WIDTH, VIRUS_HEIGHT))  # resize image
        self.rect = pygame.Rect(810, 410, VIRUS_WIDTH, VIRUS_HEIGHT)
        self.VELOCITY_VIRUS = 5
