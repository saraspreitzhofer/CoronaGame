import pygame


class GameObject(pygame.sprite.Sprite):  # GameObject is a pygame Sprite object (Vererbung / Interface)
    def __init__(self):  # runs whenever a new object of this type is made
        pygame.sprite.Sprite.__init__(self)
