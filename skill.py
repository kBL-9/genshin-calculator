from effect.skill import SkillEffect
from constants import INDENTATION

class Skill:
    def __init__(self, name: str, level: int, skill_type: str):
        self.name = name
        self.level = level
        self.type = skill_type
        self.effect = Effect()
        self.multiplier = 1
        self.proc_duration = 0
        
    def set_skill_effect(self, effect: SkillEffect):
        self.effect = effect
        return self
        
    def set_multiplier(multiplier: float):
        self.multiplier = multiplier / 100
        return self
        
    def set_skill_proc_duration(self, duration: int):
        self.duration = duration
        return self
        
    def set_skill_tap(self):
        self.duration = -1
        return self
        
    def to_str(self, tabs = 0):
        result = "{0}Skill: {1} - Level {2} - {3}:\n{4}".format(
            INDENTATION * tabs,
            self.name,
            self.level,
            "Duration: {0}".format(self.duration) if self.duration != -1 else "Tapped",
            self.effect.to_str(tabs + 1)
        )
    
    def print(self, tabs = 0):
        print(self.to_str(tabs))