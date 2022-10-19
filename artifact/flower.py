from artifact.artifact import Artifact

class FlowerOfLife(Artifact):
    def __init__(self, level: int = 20, rarity: int = 5):
        Artifact.__init__(self, level, rarity)
        self.type = "flower"
        if level == 20 and rarity == 5:
            self.add_hp(4780, True)
        # add more code here to handle level and rarity
            