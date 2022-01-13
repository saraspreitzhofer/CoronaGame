import random

from Virus import Virus
from settings import *


class Superspreader:
    def __init__(self):
        self.reduce_basis_frequency = 10
        self.velocity = 7

    def produce_virus(self, size, game):
        # later: + argument game_object_type -> check, which type and call constructor accordingly
        # later: vary size!
        game.virus_frequency = FRAMES_BETWEEN_VIRUS_START - self.reduce_basis_frequency
        self.reduce_basis_frequency += 10
        print("reduce basis frequency: " + str(self.reduce_basis_frequency))
        print("reset frequency to: " + str(game.virus_frequency))
        # TODO: startvelocity unter settings und direkt drauf zugreifen?
        if 40 < game.virus_frequency and game.virus_counter % (random.randint(1, 3)) == 0:
            #game.virus_frequency -= REDUCE_FRAMES_BETWEEN_VIRUS
            game.virus_frequency -= (random.randint(30, 40))
            print("random change in r: " + str(game.virus_frequency))
            print("Frequency: " + str(game.virus_frequency))
        if game.virus_frequency <= 40:
            game.virus_frequency = FRAMES_BETWEEN_VIRUS_START
            self.reduce_basis_frequency = 10
            self.velocity += 3
            #velocity += 5
        # TODO: improve variation
        virus = Virus(self.velocity)
        return virus


