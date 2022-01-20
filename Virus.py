import pygame
import os  # to define path to the images
from settings import *
from GameObject import GameObject  # from filename import className


class Virus(GameObject):  # (Vererbung)
    def __init__(self, velocity, rotate_by):  # runs whenever a new object of this type is made
        super().__init__()  # necessary, but why? from clear code tutorial https://www.youtube.com/watch?v=hDu8mcAlY4E
        self.VELOCITY_VIRUS = velocity  # 5
        self.x = VIRUS_X  # center position on x-axis
        self.y = VIRUS_Y  # center position on y-axis
        self.rotation_angle = 0  # start point of rotation
        self.rotate_by = rotate_by  # increase rotation angle by this factor
        # image will be updated during rotation and original (necessary for rotation)
        self.image_original = pygame.transform.scale(pygame.image.load(os.path.join('assets', "virus.png")),
                                                     (VIRUS_WIDTH, VIRUS_HEIGHT))  # resize image
        self.image_original_rect = self.image_original.get_rect()
        self.image = self.image_original
        self.rect = self.image_original_rect # pygame.Rect(self.x, self.y, VIRUS_WIDTH, VIRUS_HEIGHT)  # position - shorter with surface.get_rect()

    def move(self):
        self.rotation_angle += ROTATEBY_VIRUS  # aktualisiert rotation angle von einzelnen virus sprites
        self.x -= self.VELOCITY_VIRUS  # move image VELOCITY_VIRUS pixel to the left in each frame
        rotated_surface = pygame.transform.rotozoom(self.image_original, self.rotation_angle, 1)
        rotated_rect = rotated_surface.get_rect(
            center=(self.x, VIRUS_Y))  # use freshly set new coordiates
        return rotated_surface, rotated_rect

    def update(self):
        self.image, self.rect = self.move()

