import random

from Mask import Mask
from Virus import Virus
from settings import *


class Superspreader:
    def __init__(self):
        self.reduce_basis_frequency = 10
        self.virus_velocity = 7
        self.mask_velocity = 6

    def produce_virus(self, size, game):
        # TODO:
        # later: + argument game_object_type -> check, which type and call constructor accordingly
        # later: vary size!
        game.virus_frequency = VIRUS_FREQUENCY_FRAMES_START - self.reduce_basis_frequency
        self.reduce_basis_frequency += 10
        #print("reduce basis frequency: " + str(self.reduce_basis_frequency))
        #print("reset frequency to: " + str(game.virus_frequency))
        # TODO: startvelocity unter settings und direkt drauf zugreifen?
        if 40 < game.virus_frequency and game.virus_counter % (random.randint(1, 3)) == 0:
            #game.virus_frequency -= REDUCE_FRAMES_BETWEEN_VIRUS
            game.virus_frequency -= (random.randint(30, 40))
            #print("random change in r: " + str(game.virus_frequency))
            #print("Frequency: " + str(game.virus_frequency))
        if game.virus_frequency <= 40:  # frequency (frames between new viruses) should not be smaller than 40
            game.virus_frequency = 100  # frames to pass between the virus of this method call and the next
            # TODO: wenn die viren schneller sind, sollte der maximalabstand auch kleiner werden, sonst wartet man zu lang
            # vielleicht für jede geschwindigkeit einen eigenen max-abstand machen
            self.reduce_basis_frequency = 10
            self.virus_velocity += 3
            self.mask_velocity += 2  # masks are slower than viruses
            if self.virus_velocity == 13:
                game.level = 1
                print("Level changed to 1!")
            #velocity += 5
        # TODO: improve variation
        virus = Virus(self.virus_velocity)
        return virus

    def produce_mask(self, game):
        game.mask_frequency = MASK_FREQUENCY_FRAMES_START
        #TODO: change mask frequency over time
        return Mask(self.mask_velocity)

