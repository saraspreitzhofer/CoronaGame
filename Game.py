import pygame
import os  # to define path to the images

from Superspreader import Superspreader
from settings import *
from Runner import Runner  # from filename import className
from Virus import Virus  # from filename import className
from Health import Health1, Health2, Health3


class Game:
    def __init__(self):  # initialize game window etc
        pygame.init()
        pygame.mixer.init()
        self.WIN = pygame.display.set_mode((WIDTH, HEIGHT))  # make new window of defined width & height
        pygame.display.set_caption(TITLE)  # window title
        self.clock = pygame.time.Clock()
        self.running = True
        self.playing = True
        # self.jumping = False  # ist jetzt in Klasse Runner
        self.all_sprites = pygame.sprite.Group()  # creates new empty group for all sprites

        # create runner and add it to sprites group
        self.runner = Runner()
        self.all_sprites.add(self.runner)

        # create viruses and add them to sprites group
        self.virus_frequency = 10
        self.superspreader = Superspreader()
        self.virus = self.superspreader.produce_virus(5) # TODO: temp - remove
        self.all_sprites.add(self.virus)  # add virus to sprites group

        # create hearts and add them to sprites group
        self.health1 = Health1()
        self.health2 = Health2()
        self.health3 = Health3()
        self.all_sprites.add(self.health1)
        self.all_sprites.add(self.health2)
        self.all_sprites.add(self.health3)

    def new(self):  # start a new game
        self.run()

    def run(self):  # code that handles main game loop in pygame
        while self.playing:  # game loop: open & close the window
            self.clock.tick(FPS)  # controls speed of the while loop
            self.events()
            self.update()
            self.draw()

    def update(self):  # game loop - update
        # TODO Ula: zaehlvariable für superspreader.produce(...)

        self.all_sprites.update()
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
        if self.runner.jumping is False and user_input[pygame.K_SPACE]:
            self.runner.jumping = True
        if self.runner.jumping:
            self.runner.jump()
            # pygame.time.delay(50)  # slows down everything!
        # rotate virus
        # self.virus.rotation_angle += ROTATEBY_VIRUS
        # pygame.time.delay(250)  # slows down everything!
        print("virus center: " + str(self.virus.rect.x) + ", " + str(self.virus.rect.y))
        # print("virus rotation angle: " + str(self.virus.rotation_angle))
        # self.virus.image, self.virus.rect = self.virus.roll_through_screen() #TODO: rotation doesn't work yet
        # detect collision
        # TODO Merve: improve collision
        if self.runner.rect.colliderect(self.virus):  # detect collisions of two rectangles
            print("You are infected!")
            self.virus.image.fill(TRANSPARENT)  # make virus transparent after collision TODO Merve: kill object

    def draw(self):  # game loop - draw
        self.WIN.fill(WHITE)  # RGB color for the window background, defined as constant
        # coordinate system: (0,0) is top left
        # uncommented because included in all_sprites group:
        # self.WIN.blit(self.runner.image,
        #              (self.runner.rect.x, self.runner.rect.y))  # draw surface (pictures, text, ...) on the screen
        # self.WIN.blit(self.virus.image,
        #              (self.virus.rect.x, self.virus.rect.y))
        self.all_sprites.draw(self.WIN)

    def show_start_screen(self):  # game splash / start screen
        pass

    def show_go_screen(self):  # game over / continue
        pass
