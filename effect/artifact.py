from fullstats import FullStats
from effect.effect import Effect

class ArtifactSetEffect(Effect):
    def __init__(self):
        self.two_set_effect = FullStats()
        self.effect = Effect()
        
    def add_two_set_effect(self, stat: FullStats):
        self.two_set_effect = stat
        
    def add_four_set_effect(self, effect: Effect):
        self.effect = effect