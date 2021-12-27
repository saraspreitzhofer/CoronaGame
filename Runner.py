import pygame
import os  # to define path to the images
from settings import *


class Runner(pygame.sprite.Sprite):  # Runner is a pygame Sprite object (Vererbung / Interface)
    def __init__(self):  # runs whenever a new object of this type is made
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(os.path.join('assets', "runner.png")),
                                            (RUNNER_WIDTH, RUNNER_HEIGHT))  # resize image
        self.rect = pygame.Rect(MARGIN, HEIGHT - MARGIN - RUNNER_HEIGHT, RUNNER_WIDTH, RUNNER_HEIGHT)
        self.VELOCITY_JUMP = 20
        self.jumping = False  # jetzt hier deklariert, damit ist der endlos jump gelöst

    def jump(self):
        self.rect.y -= self.VELOCITY_JUMP
        self.VELOCITY_JUMP -= 1
        if self.VELOCITY_JUMP < -20:
            self.jumping = False
            self.VELOCITY_JUMP = 20
