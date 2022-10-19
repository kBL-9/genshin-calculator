from stats import Stats
from constants import INDENTATION

# assuming all artifacts are 5 star level 20
# can be extended to handle 3 and 4 star artifacts for beginners


class Artifact(Stats):
    def __init__(self, name: str, level: int = 20, rarity: int = 5):
        Stats.__init__(self, has_substat = True)
        self.name = name
        self.level = level
        self.rarity = rarity
        
    def to_str(self, tabs = 0):
        result = INDENTATION * tabs
        result += "Artifact: {0} - Level: {1} - Rarity: {2}\n{3}".format(
            self.name,
            self.level,
            self.rarity,
            Stats.to_str(self, tabs = 1)
        )
        return result
    
    def print(self, tabs = 0):
        print(self.to_str(tabs))