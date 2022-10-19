from fullstats import FullStats
from artifact.artifact import Artifact
from effect.artifact import ArtifactSetEffect
from basestats import BaseStats
from weapon import Weapon
from skill import Skill

# References:
# genshin-impact.fandom.com/wiki
# https://library.keqingmains.com/combat-mechanics/damage/damage-formula

class Character:
    # it is your responsibility to not include artifact stats to character base stat
    # if you are intending to add artifacts later on
    def __init__(self, name: str, level: int, base_stats: BaseStats):
        self.name = name
        self.level = level
        self.weapon = Weapon(name = "Basic", level = 1, base_atk = 23)
        self.base_stats = FullStats().add_stats(base_stats)
        self.artifact_set_effect = ArtifactSetEffect()
        self.skills = list()
        
    def add_artifact(self, artifact: Artifact):
        # not switch statement in python
        # added artifact will always override the last one
        old_artifact = None
        if artifact.type == "flower":
            old_artifact = self.flower_artifact
            self.flower_artifact = artifact
        elif artifact.type == "plume":
            old_artifact = self.plume_artifact
            self.plume_artifact = artifact
        elif artifact.type == "sands":
            old_artifact = self.sands_artifact
            self.sands_artifact = artifact
        elif artifact.type == "goblet":
            old_artifact = self.goblet_artifact
            self.goblet_artifact = artifact
        elif artifact.type == "circlet":
            old_artifact = self.circlet_artifact
            self.circlet_artifact = artifact
        else:
            print("Cannot identify the given artifact")
            return self
            
        # remove old stats and add new ones instead
        self.base_stats.remove_stats(old_artifact)
        self.base_stats.add_stats(artifact)
        return self
        
    def add_artifact_set_effect(self, set_effect: ArtifactSetEffect):
        self.base_stats.add_stats(set_effect.two_set_effect)
        self.artifact_set_effect = set_effect
        return self
        
    def add_weapon(weapon: Weapon):
        self.weapon = weapon
        return self
        
    def add_skill(skill: Skill):
        for char_skill in self.skills:
            if char_skill.type == skill.type or char_skill.name == skill.name:
                return self

        self.skills.append(skill)
        return self
        
    def add_info(self, name: str, level: int):
        self.name = name
        self.level = level
        return self
    
    def print_info(self, moreinfo = list(), more_info_fcn = None):
        print("------------------------------------------")
        print("Character: {0}. Level: {1}".format(name, level))
        
        for info in moreinfo:
            print(info)
            
        if more_info_fcn is not None:
            more_info_fcn()
            
        print("------------------------------------------")
    
    def calculate_raw_damage(self):
        damage = get_damage(self.base_stats, [self.weapon.effect, self.artifact_set_effect.effect])
        self.print_info([
            "Artifacts:\n\t- {0}\n\t- {1}\n\t- {2}\n\t- {3}\n\t- {4}".format(
                self.flower_artifact.get_info(),
                self.plume_artifact.get_info(),
                self.sands_artifact.get_info(),
                self.goblet_artifact.get_info(),
                self.circlet_artifact.get_info()
            ),
            "Raw damage: {0}".format(damage)
        ])
        
    def calculate_damage_with_effect(self):
        self.print_info()