import pygame
import os  # to define path to the images
from settings import *
from GameObject import GameObject  # from filename import className


class Virus(GameObject):  # (Vererbung)
    # TODO: add params to constructor
    def __init__(self):  # runs whenever a new object of this type is made
        super().__init__()  # necessary, but why? from clear code tutorial https://www.youtube.com/watch?v=hDu8mcAlY4E
        self.image = pygame.transform.scale(pygame.image.load(os.path.join('assets', "virus.png")),
                                            (VIRUS_WIDTH, VIRUS_HEIGHT))  # resize image
        self.rect = pygame.Rect(WIDTH-MARGIN-VIRUS_WIDTH, HEIGHT-MARGIN-VIRUS_HEIGHT, VIRUS_WIDTH, VIRUS_HEIGHT)  # position - shorter with surface.get_rect()
        self.VELOCITY_VIRUS = 5
        self.FREQUENCY_VIRUS = 10  # noch ausprobieren, was passt
        self.rotation_angle = 0

    def roll_through_screen(self):
        # self.rect.x -= self.VELOCITY_VIRUS  # move image VELOCITY_VIRUS pixel to the left in each frame
        rotated_surface = pygame.transform.rotozoom(self.image, self.rotation_angle, 1)
        rotated_rect = self.image.get_rect(
            center=(self.rect.x, self.rect.y))  # pygame.Rect(self.rect.x, self.rect.y, VIRUS_WIDTH, VIRUS_HEIGHT)
        return rotated_surface, rotated_rect

    def update(self):
        print("update virus")
        self.rect.x -= self.VELOCITY_VIRUS  # move image VELOCITY_VIRUS pixel to the left in each frame
