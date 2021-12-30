import pygame, sys
import os  # to define path to the images

from Superspreader import Superspreader
from settings import *
from Runner import Runner  # from filename import className
from Virus import Virus  # from filename import className
from Health import Health1, Health2, Health3
FPS = 60
FramePerSec =pygame.time.Clock()

class Game:
    def __init__(self):  # initialize game window etc
        self.game_over = None
        pygame.init()
        pygame.mixer.init()
        self.WIN = pygame.display.set_mode((WIDTH, HEIGHT))  # make new window of defined width & height
        pygame.display.set_caption(TITLE)  # window title
        self.clock = pygame.time.Clock()
        self.running = True
        self.playing = True
        # self.jumping = False  # ist jetzt in Klasse Runner
        self.all_sprites = pygame.sprite.Group()  # creates new empty group for all sprites
        self.virus_group = pygame.sprite.Group()

        # create runner and add it to sprites group
        self.runner = Runner()
        self.all_sprites.add(self.runner)

        # all about virus creation
        self.frame_counter = 0 # use for intervals when producing new virus
        self.virus_counter = 0 # TODO: maybe use later to increase virusproduction
        self.virus_frequency = 120
        self.superspreader = Superspreader()
        self.virus_first = None # first virus

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
        # virus sprite production depending on number of frames passed
        if self.frame_counter % self.virus_frequency == 0:
            virus = self.superspreader.produce_virus(7)  # produce virus with velocity 5
            self.all_sprites.add(virus)  # add virus to sprites group
            self.virus_group.add(virus)
            self.frame_counter = 0
            self.virus_counter += 1
        self.all_sprites.update()
        pygame.display.update()  # update changes
        self.frame_counter += 1 # necessary for virus sprite production

    def events(self): # game loop - events
        self.game_over = False
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
        # pygame.time.delay(400)  # slows down everything!
        # detect collision
        # TODO Merve: improve health decrease
        if pygame.sprite.spritecollide(self.runner, self.virus_group,
                                       True):  # self.runner.rect.colliderect(self.virus):  # detect collisions of two rectangles
            print("You are infected!")
            self.runner.numOfLives = -1
            if self.runner.numOfLives < 3:
                pygame.sprite.Sprite.kill(self.health3)
            elif self.runner.numOfLives < 2:
                pygame.sprite.Sprite.kill(self.health2)

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









class StartMenu:
    def __init__(self):  # initialize game window etc
        pygame.init()
        pygame.mixer.init()
        self.WIN = pygame.display.set_mode((WIDTH, HEIGHT))  # make new window of defined width & height
        pygame.display.set_caption(TITLE_START)  # window title
        self.running = True
        self.clock = pygame.time.Clock()
        self.font_small = pygame.font.Font(None, 60)
        self.font_big = pygame.font.Font(None, 100)
        self.click = False

    def draw_text(self, text, font, color, surface, x, y):
        text_obj = font.render(text, 1, color)
        text_rect = text_obj.get_rect()
        text_rect.topleft = (x, y)
        surface.blit(text_obj, text_rect)

    def display_main_menu(self):
        while self.running:
            self.WIN.fill(WHITE)
            mx, my = pygame.mouse.get_pos()
            start_button = pygame.Rect(280, 230, 150, 80)
            pygame.draw.rect(self.WIN, GREY, start_button)
            self.draw_text("Play", self.font_small, BLACK, self.WIN, 300, 250)
            self.draw_text("Corona Game", self.font_big, BLACK, self.WIN, 200, 100)

            if start_button.collidepoint((mx, my)):
                if self.click:
                    while g.running:
                        g.new()

            self.click = False
            pygame.display.update()
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.click = True


g = Game()
s = StartMenu()
while s.running:
    s.display_main_menu()