from character import Character
from enemy import Enemy
from team import Team

class Effect:
    def __init__(self):
        self.duration = -1
        self.name = ""
        self.source = None
        self.callback = lambda: 0

    def set_name(self, name: str):
        self.name = name
        return self

    def set_effect_applicator(callback: Callable[[Character, Team, Enemy, int], int]):
        self.callback = callback
        return self

    def set_source(self, source: Character):
        self.source = source
        return self

    def apply_effect(
        self,
        team: Team,
        enemy: Enemy,
        starting_time: int = 0):
        self.callback(self.source, team, enemy, self.duration)
        return starting_time + max(0, self.duration)

    def to_str(self, tabs = 0):
        result = ""
        return result
        
    def print(self, tabs = 0):
        print(self.to_str(tabs))