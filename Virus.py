import pygame
import os  # to define path to the images
from settings import *
from GameObject import GameObject  # from filename import className


class Virus(GameObject):  # (Vererbung)
    def __init__(self, velocity):  # runs whenever a new object of this type is made
        super().__init__()  # necessary, but why? from clear code tutorial https://www.youtube.com/watch?v=hDu8mcAlY4E
        self.VELOCITY_VIRUS = velocity  # 5
        self.x = WIDTH - MARGIN - VIRUS_WIDTH  # center position on x-axis
        self.y = HEIGHT - MARGIN - VIRUS_HEIGHT  # center position on y-axis
        self.rotation_angle = 0
        self.image = pygame.transform.scale(pygame.image.load(os.path.join('assets', "virus.png")),
                                            (VIRUS_WIDTH, VIRUS_HEIGHT))  # resize image
        self.rect = pygame.Rect(self.x, self.y, VIRUS_WIDTH, VIRUS_HEIGHT)  # position - shorter with surface.get_rect()
        self.image_original = pygame.transform.scale(pygame.image.load(os.path.join('assets', "virus.png")),
                                            (VIRUS_WIDTH, VIRUS_HEIGHT))  # resize image
        self.image_original_rect = self.image_original.get_rect()  # set center?

    def roll_through_screen(self):
        # self.rect.x -= self.VELOCITY_VIRUS  # move image VELOCITY_VIRUS pixel to the left in each frame
        rotated_surface = pygame.transform.rotozoom(self.image_original, self.rotation_angle, 1)
        rotated_rect = rotated_surface.get_rect(
            center=(self.rect.x, 450))  # use freshly set new coordiates pygame.Rect(self.rect.x, self.rect.y, VIRUS_WIDTH, VIRUS_HEIGHT)
        return rotated_surface, rotated_rect

    def update(self):
        self.rotation_angle += ROTATEBY_VIRUS  # aktualisiert rotation angle von einzelnen virus sprites
        self.rect.x -= self.VELOCITY_VIRUS  # move image VELOCITY_VIRUS pixel to the left in each frame
        print("virus center before: " + str(self.rect.x) + ", " + str(self.rect.y))
        self.image, self.rect = self.roll_through_screen()
        print("virus center after: " + str(self.rect.x) + ", " + str(self.rect.y))


