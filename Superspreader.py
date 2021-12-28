from Virus import Virus


class Superspreader:
    def __init__(self):
        pass

    # TODO Ula: produce with arguments (initialize in virus): frequency, velocity
    def produce(self, frequency, velocity):
        # later: + argument game_object_type -> check, which type and call constructor accordingly
        virus = Virus(frequency, velocity)
        print(virus.VELOCITY_VIRUS)
        print(virus.FREQUENCY_VIRUS)
        return virus


