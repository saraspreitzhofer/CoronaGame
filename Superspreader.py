from Virus import Virus


class Superspreader:
    def __init__(self):
        pass


    def produce_virus(self, frequency, velocity):
        # later: + argument game_object_type -> check, which type and call constructor accordingly
        virus = Virus(velocity)
        print(virus.VELOCITY_VIRUS)
        return virus


