from fullstats import FullStats
from effect.effect import Effect

class WeaponEffect:
    def __init__(self):
        self.base_effect = FullStats()
        self.complementary_effect = Effect()
        
    def add_base_effect(stat: FullStats):
        self.base_effect = stat
        
    def add_complementary_effect(effect: Effect):
        self.complementary_effect = effect