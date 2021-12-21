import pygame
import os  # to define path to the images
from settings import *
from Runner import Runner   # from filename import className
from Virus import Virus   # from filename import className


class Game:
    def __init__(self):  # initialize game window etc
        pygame.init()
        pygame.mixer.init()
        self.WIN = pygame.display.set_mode((WIDTH, HEIGHT))  # make new window of defined width & height
        pygame.display.set_caption(TITLE)  # window title
        self.clock = pygame.time.Clock()
        self.all_sprites = pygame.sprite.Group()  # creates new empty group for all sprites
        self.running = True
        self.playing = True
        self.jumping = False
        self.runner = Runner()
        self.virus = Virus()

        # self.runner = pygame.Rect(10, 370, RUNNER_WIDTH, RUNNER_HEIGHT)
        # self.RUNNER_IMAGE = pygame.image.load(os.path.join('assets', "runner.png"))
        # self.RUNNER = pygame.transform.scale(self.RUNNER_IMAGE, (RUNNER_WIDTH, RUNNER_HEIGHT))  # resize image
        # self.virus = pygame.Rect(810, 410, VIRUS_WIDTH, VIRUS_HEIGHT)
        # self.VIRUS_IMAGE = pygame.image.load(os.path.join('assets', "virus.png"))
        # self.VIRUS = pygame.transform.scale(self.VIRUS_IMAGE, (VIRUS_WIDTH, VIRUS_HEIGHT))  # resize image

    def new(self):  # start a new game
        self.run()

    def run(self):  # code that handles main game loop in pygame
        while self.playing:  # game loop: open & close the window
            self.clock.tick(FPS)  # controls speed of the while loop
            self.events()
            self.update()
            self.draw()

    def update(self):  # game loop - update
        # self.all_sprites.update()
        pygame.display.update()  # update changes

    def events(self):  # game loop - events
        for event in pygame.event.get():  # loop through list of all different events
            if event.type == pygame.QUIT:
                if self.playing:
                    self.playing = False  # end while loop if user quits game (press x)
                self.running = False
            # if self.jumping is False and event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            #    self.jumping = True
            # if self.jumping:
            #    self.jump()
        user_input = pygame.key.get_pressed()  # list of currently pressed key(s)
        if self.jumping is False and user_input[pygame.K_SPACE]:
            self.jumping = True
        if self.jumping:
            self.runner.jump()
            # pygame.time.delay(50)  # slows down everything!
        self.virus.rect.x -= self.virus.VELOCITY_VIRUS  # move image VELOCITY_VIRUS pixel to the left in each frame
        if self.runner.rect.colliderect(self.virus):  # detect collisions of two rectangles
            print("You are infected!")
            self.virus.image.fill(TRANSPARENT)  # make virus transparent after collision

    def draw(self):  # game loop - draw
        self.WIN.fill(WHITE)  # RGB color for the window background, defined as constant
        # coordinate system: (0,0) is top left
        self.WIN.blit(self.runner.image,
                      (self.runner.rect.x, self.runner.rect.y))  # draw surface (pictures, text, ...) on the screen
        self.WIN.blit(self.virus.image,
                      (self.virus.rect.x, self.virus.rect.y))
        # self.all_sprites.draw(self.WIN)

    def show_start_screen(self):  # game splash / start screen
        pass

    def show_go_screen(self):  # game over / continue
        pass