from artifact.artifact import Artifact

HP = 0
ATK = 1
DEF = 2
EM = 3
ER = 4

class SandsOfEon(Artifact):
    def __init__(self, main_stat_type: int, level: int = 20, rarity: int = 5):
        Artifact.__init__(self, level, rarity)
        self.type = "sands"
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
            if main_stat_type == ER:
                self.add_er(51.8, False)
        # add more code here to handle level and rarity