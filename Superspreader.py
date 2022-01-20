import random

from Mask import Mask
from Virus import Virus
from settings import *


class Superspreader:
    def __init__(self):
        self.reduce_basis_frequency = 10
        self.virus_velocity = 7
        self.mask_velocity = 4;

    def produce_virus(self, game):
        # TODO:
        # later: + argument game_object_type -> check, which type and call constructor accordingly
        # later: vary size!
        game.virus_frequency = VIRUS_FREQUENCY_FRAMES_START - self.reduce_basis_frequency  # reset interval
        self.reduce_basis_frequency += 10 # reduce interval after each virus
        # TODO: startvelocity unter settings und direkt drauf zugreifen?
        if 40 < game.virus_frequency and game.virus_counter % (random.randint(1, 3)) == 0:
            #game.virus_frequency -= REDUCE_FRAMES_BETWEEN_VIRUS
            game.virus_frequency -= (random.randint(40, 50)) # set next interval to a random value between 30 and 40
            print("under 40!")
            #print("random change in r: " + str(game.virus_frequency))
            #print("Frequency: " + str(game.virus_frequency))
        if game.virus_frequency <= 40:  # frequency (frames between new viruses) should not be smaller than 40
            print("frequency reset")
            game.virus_frequency = 100  # frames to pass between the virus of this method call and the next
            # TODO: wenn die viren schneller sind, sollte der maximalabstand auch kleiner werden, sonst wartet man zu lang
            # vielleicht für jede geschwindigkeit einen eigenen max-abstand machen
            self.reduce_basis_frequency = 10
            self.virus_velocity += 3
            self.mask_velocity += 2  # masks are slower than viruses
            #velocity += 5
        # TODO: improve variation
        virus = Virus(self.virus_velocity)
        return virus

    def produce_mask(self, game):
        # Mask frequency is changed with each level
        # Todo: vary mask velocity?
        if game.level == 1:
            game.mask_frequency = MASK_FREQUENCY_FRAMES_START
        elif game.level > 1:
            game.mask_frequency = MASK_FREQUENCY_FRAMES_START + (100*(game.level-1))
        return Mask(self.mask_velocity + random.randint(0, 3))

