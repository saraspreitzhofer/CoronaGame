import pygame.mixer
import os

pygame.mixer.init()  # for sounds

TITLE = "Corona Game"
TITLE_START = "Start Menu"
FPS = 60  # frames per second

WIDTH, HEIGHT = 900, 500
RUNNER_WIDTH, RUNNER_HEIGHT = 120, 120
VIRUS_WIDTH, VIRUS_HEIGHT = 50, 50
HEART_WIDTH, HEART_HEIGHT = 70, 70
BUTTON_WIDTH, BUTTON_HEIGHT = 270, 70
SMALL_BUTTON_WIDTH, SMALL_BUTTON_HEIGHT = 130, 60
RADIUS = 30

MARGIN = 15
WHITE = (255, 255, 255)
GREY = (200, 200, 200)
BLACK = (0, 0, 0)
TRANSPARENT = (0, 0, 0, 0)

ROTATEBY_VIRUS = 5

# virus frequency settings
FRAMES_BETWEEN_VIRUS_START = 140 # TODO: is reduced immediately. not very elegant.
REDUCE_FRAMES_BETWEEN_VIRUS = 20

# sounds
GAME_OVER_SOUND = pygame.mixer.Sound(os.path.join('assets', 'zapsplat_game_over.mp3'))
COLLISION_SOUND = pygame.mixer.Sound(os.path.join('assets', 'zapsplat_cough.mp3'))
JUMP_SOUND = pygame.mixer.Sound(os.path.join('assets', 'zapsplat_jump.mp3'))



