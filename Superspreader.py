from Virus import Virus
from settings import *


class Superspreader:
    def __init__(self):
        pass

    def produce_virus(self, velocity, size, game):
        # later: + argument game_object_type -> check, which type and call constructor accordingly
        # later: vary size!
        # TODO: startvelocity unter settings und direkt drauf zugreifen?
        if 40 < game.virus_frequency and game.virus_counter % 4 == 0:
            game.virus_frequency -= REDUCE_FRAMES_BETWEEN_VIRUS
            print("Frequency: " + str(game.virus_frequency))
        elif game.virus_frequency == 40:
            game.virus_frequency = 100
            velocity += 2
        # TODO: improve variation
        virus = Virus(velocity)
        return virus



