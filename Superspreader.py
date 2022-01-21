import random

from Mask import Mask
from Virus import Virus
from settings import *


class Superspreader:
    def __init__(self):
        self.virus_velocity = VIRUS_BASIC_VELOCITY
        self.mask_velocity = MASK_BASIC_VELOCITY
        self.virus_rotate_by = ROTATEBY_VIRUS
        self.add = 0  # add to virus velocity and rotation

    def produce_virus(self, game):
        # later: + argument game_object_type -> check, which type and call constructor accordingly
        # later: vary size!

        # set upper bound for random frequency - workaround to avoid too small frequencies at higher levels
        if game.level < 5:
            max_frequency = VIRUS_FREQUENCY_FRAMES_START - game.level * 12
        else:
            max_frequency = 75

        # set next virus interval(frequency), velocity and rotation (rotation adjustment is optional)
        if game.level == 0:
            game.virus_frequency = random.randint(50,
                                                  max_frequency)
            self.virus_rotate_by = ROTATEBY_VIRUS
        elif game.level > 0:
            while True:  # workaround to prevent frequency to go under 30 (distance between viruses too narrow)
                game.virus_frequency = random.randint(30, max_frequency)
                if game.virus_frequency >= 30:
                    break
            if game.level < 5:  # randomly add to velocity  - workaround to prevent error when random range is reversed
                self.add = random.randint((game.level - 1), 3)
            else:
                self.add = random.randint(3, (game.level - 1))
            self.virus_velocity = VIRUS_BASIC_VELOCITY + self.add
            self.virus_rotate_by += self.add

        virus = Virus(self.virus_velocity, self.virus_rotate_by)
        game.virus_counter += 1
        return virus

    def produce_mask(self, game):
        if game.level == 1:
            game.mask_frequency = MASK_FREQUENCY_FRAMES_START
        elif game.level > 1:
            game.mask_frequency = MASK_FREQUENCY_FRAMES_START + (
                        100 * (game.level - 1))  # Mask frequency is changed with each level
        return Mask(self.mask_velocity + random.randint(0, 3)) # random mask veloci
