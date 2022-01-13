import sys

import pygame
import os  # to define path to the images

from Mask import Mask
from PointsCounter import PointsCounter
from Superspreader import Superspreader
from settings import *
from Runner import Runner  # from filename import className
from Virus import Virus  # from filename import className
from Health import Health1, Health2, Health3

FPS = 60
FramePerSec = pygame.time.Clock()

class Game:
    def __init__(self):  # initialize game window etc
        self.game_over = None
        pygame.init()
        pygame.mixer.init()  # for sounds
        self.WIN = pygame.display.set_mode((WIDTH, HEIGHT))  # make new window of defined width & height
        pygame.display.set_caption(TITLE)  # window title
        self.clock = pygame.time.Clock()
        self.running = True
        self.playing = True
        self.pause = False
        self.click = False
        # self.jumping = False  # ist jetzt in Klasse Runner
        self.all_sprites = pygame.sprite.Group()  # creates new empty group for all sprites
        self.virus_group = pygame.sprite.Group()
        self.mask_group = pygame.sprite.Group()
        self.runner_group = pygame.sprite.Group()

        # create runner and add it to sprites group
        self.runner = None

        # all about virus creation
        self.superspreader = None # use to produce virus and mask sprites
        self.frame_counter = None  # use for intervals when producing new objects
        self.virus_counter = None  # used to measure player's progress TODO: brauchma den noch?
        self.virus_frequency = None
        self.mask_frequency = None


        # count collision -> virus
        self.collision_virus = 0

        # protection
        self.protected = False  # should be true for a certain period of time or frames after a mask has been collected

        # count points (virus reached the left screen border)
        self.points_counter = PointsCounter()
        self.all_sprites.add(self.points_counter)
        self.viruses_avoided = 0  # equivalent to points earned during the game

        # heats for health
        self.health1 = None
        self.health2 = None
        self.health3 = None

        # level TODO: oder stattdessen health-status benutzen?
        self.level = None

    def new(self):  # start a new game
        # create runner and add it to sprites group
        self.runner = Runner()
        self.all_sprites.add(self.runner)

        # initialize health
        # create hearts and add them to sprites group
        self.health1 = Health1()
        self.health2 = Health2()
        self.health3 = Health3()
        self.all_sprites.add(self.health1)
        self.all_sprites.add(self.health2)
        self.all_sprites.add(self.health3)

        # set counters to 0 (important when restarting the game)
        self.viruses_avoided = 0
        self.virus_counter = 0
        self.collision_virus = 0
        self.virus_frequency = 0
        self.mask_frequency = 0

        self.frame_counter = 0  # use for intervals when producing new
        self.superspreader = Superspreader()

        # level
        self.level = 0

        self.running = True
        self.playing = True

        # run the game
        self.run()

    def run(self):  # code that handles main game loop in pygame
        while self.playing:  # game loop: open & close the window
            self.clock.tick(FPS)  # controls speed of the while loop
            self.events()
            self.update()
            self.draw()

    def update(self):  # game loop - update
        # virus sprite production depending on number of frames passed
        if self.virus_frequency == 0:  #self.frame_counter % self.virus_frequency == 0:
            virus = self.superspreader.produce_virus(120, self)  # produce virus with velocity 7
            self.all_sprites.add(virus)  # add virus to sprites group
            self.virus_group.add(virus)
            self.virus_counter += 1
            # test masks TODO: improve intervals
            self.frame_counter = 0  # TODO: stattdessen einfach nur virusfrequency runterzählen und reagieren, wenn 0?

        if self.level > 0:
            if self.mask_frequency == 0: #self.level > 0 and self.virus_counter % 3 == 0:  # TODO: nicht fertig! besser: setz eigene mask frequency un dzähl die runter
                mask = self.superspreader.produce_mask(self)
                self.all_sprites.add(mask)
                self.mask_group.add(mask)
            self.mask_frequency -= 1  # TODO: experimentierstadium - lassen?
            # TODO: reset mask frequency in superspreader
            #runner

        self.all_sprites.update()
        pygame.display.update()  # update changes
        self.frame_counter += 1  # necessary for virus sprite production
        self.virus_frequency -= 1  # TODO: experimentierstadium - lassen?

    def events(self):  # game loop - events
        for event in pygame.event.get():  # loop through list of all different events
            if event.type == pygame.QUIT:
                if self.playing:  # TODO: necessary?
                    self.playing = False  # end while loop if user quits game (press x)
                self.running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.click = True
            # if self.jumping is False and event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            #    self.jumping = True
        user_input = pygame.key.get_pressed()  # list of currently pressed key(s)
        if self.runner.jumping is False and user_input[pygame.K_SPACE]:
            self.runner.jumping = True
            JUMP_SOUND.play()  # muss an diese Stelle, überall anders wird der Ton verzerrt
        if self.runner.jumping:
            self.runner.jump()
        # pygame.time.delay(400)  # slows down everything!
        # detect collision
        self.check_collision_with_mask()
        self.check_collision_with_virus()
        self.count_points()

    def check_collision_with_virus(self):  # improve health decrease & collision detection
        if pygame.sprite.spritecollide(self.runner, self.virus_group,
                                       True):  # self.runner.rect.colliderect(self.virus):  # detect collisions of two rectangles
            self.collision_virus += 1
            COLLISION_SOUND.play()
            print(self.collision_virus)
            if self.collision_virus == 1:
                pygame.sprite.Sprite.kill(self.health3)

                self.runner.sprites_running = []
                self.runner.sprites_running.append(pygame.transform.scale(
                    pygame.image.load(os.path.join('assets/Runner_infected', 'runner1_infected.png')), (RUNNER_WIDTH, RUNNER_HEIGHT)))
                self.runner.sprites_running.append(pygame.transform.scale(
                    pygame.image.load(os.path.join('assets/Runner_infected', 'runner2_infected.png')), (RUNNER_WIDTH, RUNNER_HEIGHT)))
                self.runner.sprites_running.append(pygame.transform.scale(
                    pygame.image.load(os.path.join('assets/Runner_infected', 'runner3_infected.png')), (RUNNER_WIDTH, RUNNER_HEIGHT)))
                self.runner.sprites_running.append(pygame.transform.scale(
                    pygame.image.load(os.path.join('assets/Runner_infected', 'runner3a_infected.png')), (RUNNER_WIDTH, RUNNER_HEIGHT)))
                self.runner.sprites_running.append(pygame.transform.scale(
                    pygame.image.load(os.path.join('assets/Runner_infected', 'runner4_infected.png')), (RUNNER_WIDTH, RUNNER_HEIGHT)))
                self.runner.sprites_running.append(pygame.transform.scale(
                    pygame.image.load(os.path.join('assets/Runner_infected', 'runner5_infected.png')), (RUNNER_WIDTH, RUNNER_HEIGHT)))
                self.runner.sprites_running.append(pygame.transform.scale(
                    pygame.image.load(os.path.join('assets/Runner_infected', 'runner6_infected.png')), (RUNNER_WIDTH, RUNNER_HEIGHT)))
                self.runner.sprites_running.append(pygame.transform.scale(
                    pygame.image.load(os.path.join('assets/Runner_infected', 'runner7_infected.png')), (RUNNER_WIDTH, RUNNER_HEIGHT)))
                self.runner.sprites_running.append(pygame.transform.scale(
                    pygame.image.load(os.path.join('assets/Runner_infected', 'runner8_infected.png')), (RUNNER_WIDTH, RUNNER_HEIGHT)))

            elif self.collision_virus == 2:
                pygame.sprite.Sprite.kill(self.health2)

            elif self.collision_virus == 3:  # display_game_over hier aufrufen
                pygame.sprite.Sprite.kill(self.health1)
                print("you are  dead ")
                self.end_game()  # for a clean end
                s.display_game_over()

    def check_collision_with_mask(self):
        if pygame.sprite.spritecollide(self.runner, self.mask_group, True):
            self.protected = True
            print("you are wearing a mask now")
            # todo: set timer and then set protection back to false

    def count_points(self):  # detect and kill escaped viruses with the help of points_counter sprite object
        if pygame.sprite.spritecollide(self.points_counter, self.virus_group, True):
            self.viruses_avoided += 1
            print("Viruses escaped: " + str(self.viruses_avoided))
            print("Viruses in group: " + str(self.virus_group))

    def end_game(self):  # kill all remaining game objects
        self.playing = False
        for thing in self.all_sprites:  # kills all sprites in the game ! all sprites have to be initialized again with new game!
            thing.kill()

    def draw(self):  # game loop - draw
        self.WIN.fill(WHITE)  # RGB color for the window background, defined as constant
        # coordinate system: (0,0) is top left

        # uncommented because included in all_sprites group:
        # self.WIN.blit(self.runner.image,
        #              (self.runner.rect.x, self.runner.rect.y))  # draw surface (pictures, text, ...) on the screen
        # self.WIN.blit(self.virus.image,
        #              (self.virus.rect.x, self.virus.rect.y))
        self.all_sprites.draw(self.WIN)
        # start and stop button
        mx, my = pygame.mouse.get_pos()
        stop_button = pygame.Rect(WIDTH - 2 * MARGIN - SMALL_BUTTON_WIDTH, MARGIN, SMALL_BUTTON_WIDTH,
                                  SMALL_BUTTON_HEIGHT)
        pause_button = pygame.Rect(WIDTH - 2 * MARGIN - SMALL_BUTTON_WIDTH, 2 * MARGIN + SMALL_BUTTON_HEIGHT,
                                   SMALL_BUTTON_WIDTH, SMALL_BUTTON_HEIGHT)
        pygame.draw.rect(self.WIN, GREY, stop_button)
        pygame.draw.rect(self.WIN, GREY, pause_button)
        Menu.draw_text(self, "stop", pygame.font.Font(None, 50), BLACK, self.WIN, WIDTH - MARGIN - SMALL_BUTTON_WIDTH,
                       2 * MARGIN)
        Menu.draw_text(self, "pause", pygame.font.Font(None, 50), BLACK, self.WIN, WIDTH - MARGIN - SMALL_BUTTON_WIDTH,
                       3 * MARGIN + SMALL_BUTTON_HEIGHT)

        if stop_button.collidepoint(mx, my):
            if self.click:
                self.click = False
                # self.playing = False  - moved to end_game()
                self.end_game()  # kills all virus objects produced so far
                s.display_main_menu()
        if pause_button.collidepoint(mx, my):
            if self.click:
                self.click = False
                self.pause = True
                while self.pause:
                    s.display_pause_screen()

        # display points during the game
        text = "Points: " + str(self.viruses_avoided)
        Menu.draw_text(self, text, pygame.font.Font(None, 50), BLACK, self.WIN, 400, 2 * MARGIN)

    # def show_start_screen(self):  # game splash / start screen
    #    pass

    # def show_go_screen(self):  # game over / continue
    #    pass


class Menu:
    def __init__(self):  # initialize game window etc
        pygame.init()
        pygame.mixer.init()
        self.WIN = pygame.display.set_mode((WIDTH, HEIGHT))  # make new window of defined width & height
        pygame.display.set_caption(TITLE_START)  # window title
        self.running = True
        self.clock = pygame.time.Clock()
        self.font_very_small = pygame.font.Font(None, 40)
        self.font_small = pygame.font.Font(None, 60)
        self.font_big = pygame.font.Font(None, 100)
        self.click = False

    def run(self):
        self.click = False
        pygame.display.update()
        self.clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.click = True

    def draw_text(self, text, font, color, surface, x, y):
        text_obj = font.render(text, 1, color)
        text_rect = text_obj.get_rect()
        text_rect.topleft = (x, y)
        surface.blit(text_obj, text_rect)

    def display_main_menu(self):
        while self.running:
            self.WIN.fill(WHITE)
            mx, my = pygame.mouse.get_pos()
            # create buttons
            start_button = pygame.Rect(BUTTON1)
            highscore_button = pygame.Rect(BUTTON2)
            quit_button = pygame.Rect(BUTTON3)
            # display rectangles
            pygame.draw.rect(self.WIN, GREY, start_button)
            pygame.draw.rect(self.WIN, GREY, highscore_button)
            pygame.draw.rect(self.WIN, GREY, quit_button)
            # create circle button
            help_button = pygame.draw.circle(self.WIN, GREY, (WIDTH - 2 * MARGIN - RADIUS, 2 * MARGIN + RADIUS),
                                             RADIUS)  # surface, color, center, radius
            # display text
            self.draw_text("Corona Game", self.font_big, BLACK, self.WIN, 220, 80)
            self.draw_text("Play", self.font_small, BLACK, self.WIN, WIDTH / 2 - BUTTON_WIDTH / 2 + 2 * MARGIN,
                           180 + MARGIN)
            self.draw_text("High Score", self.font_small, BLACK, self.WIN, WIDTH / 2 - BUTTON_WIDTH / 2 + 2 * MARGIN,
                           180 + 2 * MARGIN + BUTTON_HEIGHT)
            self.draw_text("Quit", self.font_small, BLACK, self.WIN, WIDTH / 2 - BUTTON_WIDTH / 2 + 2 * MARGIN,
                           180 + 3 * MARGIN + 2 * BUTTON_HEIGHT)
            self.draw_text("?", self.font_small, BLACK, self.WIN, help_button.x + MARGIN, help_button.y + MARGIN)
            # display pictures
            runner = pygame.transform.scale(pygame.image.load(os.path.join('assets/Runner', "runner3a.png")),
                                            (RUNNER_WIDTH * 1.5, RUNNER_HEIGHT * 1.5))
            small_virus = pygame.transform.scale(pygame.image.load(os.path.join('assets', "virus.png")),
                                                 (VIRUS_WIDTH, VIRUS_HEIGHT))
            big_virus = pygame.transform.scale(pygame.image.load(os.path.join('assets', "virus.png")),
                                               (VIRUS_WIDTH * 2, VIRUS_HEIGHT * 2))
            self.WIN.blit(runner, (WIDTH - 2 * MARGIN - RUNNER_WIDTH * 1.5,
                                   HEIGHT - 2 * MARGIN - RUNNER_HEIGHT * 1.5))  # draw surface (pictures, text, ...) on the screen
            self.WIN.blit(small_virus, (50, 350))
            self.WIN.blit(big_virus, (150, 200))

            if start_button.collidepoint((mx, my)):
                if self.click:
                    self.click = False  # reset to avoid zombie runner (continues running when dead if mouse stays in the same position)
                    while g.running:
                        g.new()
            if quit_button.collidepoint(mx, my):
                if self.click:
                    pygame.quit()
                    sys.exit()
            if highscore_button.collidepoint(mx, my):
                if self.click:
                    # TODO: display highscores
                    pass
            if help_button.collidepoint(mx, my):
                if self.click:
                    s.display_help_page()
            self.run()

    def display_help_page(self):
        while self.running:
            self.WIN.fill(WHITE)
            mx, my = pygame.mouse.get_pos()
            back_button = pygame.Rect(MARGIN, HEIGHT - MARGIN - BUTTON_HEIGHT, BUTTON_WIDTH * 0.75, BUTTON_HEIGHT)
            pygame.draw.rect(self.WIN, GREY, back_button)
            self.draw_text("<-- Back", self.font_small, BLACK, self.WIN, 2 * MARGIN, HEIGHT - BUTTON_HEIGHT)
            self.draw_text("Corona Game", self.font_big, BLACK, self.WIN, 220, 80)
            # jede Zeile in einen Befehl, falls jemand eine bessere Lösung hat bitte ändern
            self.draw_text("Anleitung Bla Bla alsdjf aslkd föalskd falsdk lasd fklasd asd",
                           self.font_very_small, BLACK, self.WIN, 2 * MARGIN, 180)
            self.draw_text("fj aölksdjf asklöd jfaöksldf jalskd föasldkf asdk fjasdklöf ",
                           self.font_very_small, BLACK, self.WIN, 2 * MARGIN, 230)
            self.draw_text("fj aölksdjf asklöd jfaöksldf jalskd föasldkf asdk fjasdklöf ",
                           self.font_very_small, BLACK, self.WIN, 2 * MARGIN, 280)
            self.draw_text("ycxjkv lykjsdflkwajerf klyxcnvpoid",
                           self.font_very_small, BLACK, self.WIN, 2 * MARGIN, 330)

            if back_button.collidepoint((mx, my)):
                if self.click:
                    self.click = False
                    s.display_main_menu()

            self.run()

    def display_pause_screen(self):
        while self.running:
            self.WIN.fill(WHITE)
            mx, my = pygame.mouse.get_pos()
            continue_button = pygame.Rect(WIDTH / 2 - BUTTON_WIDTH / 2, HEIGHT / 2 - BUTTON_HEIGHT / 2, BUTTON_WIDTH,
                                          BUTTON_HEIGHT)
            pygame.draw.rect(self.WIN, GREY, continue_button)
            self.draw_text("Continue", self.font_small, BLACK, self.WIN, WIDTH / 2 - BUTTON_WIDTH / 2 + 2 * MARGIN,
                           HEIGHT / 2 - BUTTON_HEIGHT / 2 + MARGIN)

            if continue_button.collidepoint((mx, my)):
                if self.click:
                    self.click = False
                    g.pause = False
                    break
            self.run()

    def display_game_over(self):
        print("len virus_group: " + str(len(g.virus_group)))
        GAME_OVER_SOUND.play()
        while self.running:
            # initialize text and buttons
            self.WIN.fill(WHITE)
            mx, my = pygame.mouse.get_pos()
            play_again_button = pygame.Rect(BUTTON1)  # TODO: positionen von verbessern
            main_menu_button = pygame.Rect(BUTTON2)
            quit_button = pygame.Rect(BUTTON3)
            pygame.draw.rect(self.WIN, GREY, play_again_button)
            pygame.draw.rect(self.WIN, GREY, main_menu_button)
            pygame.draw.rect(self.WIN, GREY, quit_button)
            self.draw_text("Ooops! You are dead :/", self.font_big, BLACK, self.WIN, 60, 40)
            self.draw_text("Play again", self.font_small, BLACK, self.WIN, play_again_button.x + MARGIN,
                           play_again_button.y + MARGIN)
            self.draw_text("Main Menu", self.font_small, BLACK, self.WIN, main_menu_button.x + MARGIN,
                           main_menu_button.y + MARGIN)
            self.draw_text("Quit", self.font_small, BLACK, self.WIN, quit_button.x + MARGIN, quit_button.y + MARGIN)

            self.draw_text("Viruses avoided: " + str(g.viruses_avoided), self.font_small, BLACK,
                           self.WIN, 250, 130)

            if play_again_button.collidepoint(mx, my):
                if self.click:
                    self.click = False  # reset to avoid zombie runner (continues running when dead if mouse stays in the same position)
                    g.new()  # run a new game

            if quit_button.collidepoint(mx, my):
                if self.click:
                    pygame.quit()
                    sys.exit()

            if main_menu_button.collidepoint(mx, my):
                if self.click:
                    self.click = False
                    self.display_main_menu()

            self.run()


g = Game()
s = Menu()
while s.running:
    s.display_main_menu()
