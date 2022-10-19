from artifact.artifact import Artifact

class PlumeOfDeath(Artifact):
    def __init__(self, level: int = 20, rarity: int = 5):
        Artifact.__init__(self, level, rarity)
        self.type = "plume"
        if level == 20 and rarity == 5:
            self.add_atk(311, True)
        # add more code here to handle level and rarity