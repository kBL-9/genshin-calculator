from artifact.artifact import Artifact

HP = 0
ATK = 1
DEF = 2
EM = 3
ER = 4
DMG_BONUS = 5

class GobletOfEonothem(Artifact):
    def __init__(self, main_stat_type: int, bonus_type: int = 0, level: int = 20, rarity: int = 5):
        Artifact.__init__(self, level, rarity)
        self.type = "goblet"
        if level == 20 and rarity == 5:
            if main_stat_type == HP:
                self.add_hp(46.6, False)
            if main_stat_type == ATK:
                self.add_atk(46.6, False)
            if main_stat_type == DEF:
                self.add_def(58.3, False)
            if main_stat_type == EM:
                # wiki said so, the actual value is an int
                self.add_em(186.5, False)
            if main_stat_type == DMG_BONUS:
                self.add_dmg_bonus(46.6 if bonus_type != PHYSICAL_BONUS else 58.3)
        # add more code here to handle level and rarity