import pygame
import os  # to define path to the images
from settings import *
from GameObject import GameObject  # from filename import className


class Health1(GameObject):  # (Vererbung)
    def __init__(self):  # runs whenever a new object of this type is made
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(os.path.join('assets', "heart.png")),
                                              (HEART_WIDTH, HEART_HEIGHT))
        self.rect = pygame.Rect(MARGIN, MARGIN, HEART_WIDTH, HEART_HEIGHT)


class Health2(GameObject):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(os.path.join('assets', "heart.png")),
                                              (HEART_WIDTH, HEART_HEIGHT))
        self.rect = pygame.Rect(MARGIN * 2 + HEART_WIDTH, MARGIN, HEART_WIDTH, HEART_HEIGHT)


class Health3(GameObject):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(os.path.join('assets', "heart.png")),
                                              (HEART_WIDTH, HEART_HEIGHT))
        self.rect = pygame.Rect(MARGIN * 3 + HEART_WIDTH * 2, MARGIN, HEART_WIDTH, HEART_HEIGHT)