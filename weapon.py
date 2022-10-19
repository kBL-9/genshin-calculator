from fullstats import FullStats
from constants import DamageType
from effect.effect import Effect

ATK = 0
DEF = 1
HP = 2
EM = 3
ER = 4
CR = 5
CD = 6
PHYSICAL_BONUS = 7

class Weapon(FullStats):
    def __init__(self, base_atk: int, name: str, level: int = 90):
        self.add_atk(base_atk, is_base = True)
        self.effect = Effect()
        self.name = name
        self.level = level

    def print_basic_info(self):
        print("Weapon: {0} at level {1}".format(self.name, self.level))
     
    def add_secondary_stat(self, stat_type: int, stat_value: int):
        if secondary_stat_type == ATK:
            self.add_atk(secondary_stat_value)
        elif secondary_stat_type == DEF:
            self.add_def(secondary_stat_value)
        elif secondary_stat_type == HP:
            self.add_hp(secondary_stat_value)
        elif secondary_stat_type == EM:
            self.add_em(secondary_stat_value)
        elif secondary_stat_type == ER:
            self.add_er(secondary_stat_value)
        elif secondary_stat_type == CR:
            self.add_cr(secondary_stat_value)
        elif secondary_stat_type == CD:
            self.add_cd(secondary_stat_value)
        elif secondary_stat_type == PHYSICAL_BONUS:
            self.add_dmg_bonus(secondary_stat_value, DamageType.PHYSICAL)
            
        return self
        
    def add_weapon_effect(self, weapon_effect: Effect):
        self.effect = weapon_effect