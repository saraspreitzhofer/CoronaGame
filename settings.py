import pygame.mixer
import os

pygame.mixer.init()  # for sounds

LEVEL_INTERVAL = 10  # number of viruses before next level
POINTS_MASK = 5  # number of points earned for each collected mask
PROTECTION_MASK = 100  # number of frames for protection after collecting a mask

TITLE = "Corona Game"
TITLE_START = "Start Menu"
FPS = 60  # frames per second

MARGIN = 15
WHITE = (255, 255, 255)
GREY = (200, 200, 200)
BLACK = (0, 0, 0)
TRANSPARENT = (0, 0, 0, 0)

# sizes and positions of objects
WIDTH, HEIGHT = 900, 500 # screen size
RUNNER_WIDTH, RUNNER_HEIGHT = 120, 120
VIRUS_WIDTH, VIRUS_HEIGHT = 50, 50
VIRUS_X, VIRUS_Y = (WIDTH - MARGIN - VIRUS_WIDTH), 460  # start position of virus
MASK_WIDTH, MASK_HEIGHT = 40, 40
MASK_X, MASK_Y = (WIDTH - MARGIN - MASK_WIDTH), 200 # start position of mask
HEART_WIDTH, HEART_HEIGHT = 70, 70

# buttons
BUTTON_WIDTH, BUTTON_HEIGHT = 270, 70
SMALL_BUTTON_WIDTH, SMALL_BUTTON_HEIGHT = 130, 60
#button positions
BUTTON1 = WIDTH / 2 - BUTTON_WIDTH / 2, 180, BUTTON_WIDTH, BUTTON_HEIGHT
BUTTON2 = WIDTH / 2 - BUTTON_WIDTH / 2, 180 + MARGIN + BUTTON_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT
BUTTON3 = WIDTH / 2 - BUTTON_WIDTH / 2, 180 + 2 * MARGIN + 2 * BUTTON_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT

RADIUS = 30  # TODO: Radius wofür? besser benennen

ROTATEBY_VIRUS = 4

# frequency settings
VIRUS_FREQUENCY_FRAMES_START = 140 #
MASK_FREQUENCY_FRAMES_START = 300
REDUCE_FRAMES_BETWEEN_VIRUS = 20
# velocity settings
VIRUS_BASIC_VELOCITY = 7
MASK_BASIC_VELOCITY = 4


# sounds
GAME_OVER_SOUND = pygame.mixer.Sound(os.path.join('assets', 'zapsplat_game_over.mp3'))
COLLISION_SOUND = pygame.mixer.Sound(os.path.join('assets', 'zapsplat_cough.mp3'))
JUMP_SOUND = pygame.mixer.Sound(os.path.join('assets', 'zapsplat_jump.mp3'))
MUSIC = pygame.mixer.Sound(os.path.join('assets', 'zapsplat_game_music.mp3'))



