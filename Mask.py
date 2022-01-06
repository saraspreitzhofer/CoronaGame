import pygame
import os  # to define path to the images
from settings import *
from GameObject import GameObject  # from filename import className


class Mask(GameObject):
    def __init__(self, velocity):  # runs whenever a new object of this type is made
        super().__init__()  # necessary, but why? from clear code tutorial https://www.youtube.com/watch?v=hDu8mcAlY4E
        self.VELOCITY_MASK = velocity  # 5
        self.x = WIDTH - MARGIN - MASK_WIDTH  # position on x-axis
        self.y = HEIGHT - MARGIN - MASK_HEIGHT - 200  # position on y-axis


        self.image = pygame.transform.scale(pygame.image.load(os.path.join('assets', "mask.png")),
                                            (MASK_WIDTH, MASK_HEIGHT))  # resize image
        self.rect = self.image.get_rect(topleft=(MASK_X, MASK_Y))

    def update(self):
        self.x -= self.VELOCITY_MASK  # move image VELOCITY_VIRUS pixel to the left in each frame


# <div>Icons made by <a href="https://www.flaticon.com/authors/mangsaabguru" title="mangsaabguru">mangsaabguru</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>
