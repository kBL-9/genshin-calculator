from effect.effect import Effect

class ChainEffect:
    def __init__(self, name: str):
        self.chain = list()
        self.name = name
        
    # duration in seconds
    def add_effect_to_chain(self, effect: Effect):
        self.chain.append(effect)
        return self

    def apply_effects(self, team: Team, enemy: Enemy, starting_time: int = 0):
        for effect in self.chain:
            effect.apply_effect(team, enemy, starting_time)
        
    def to_str(self, tabs = 0):
        result = "Chain \"{0}\" consists of following effects:\n".format(self.name)
        count = 0
        for effect in self.chain:
            result += "  " * tabs
            result += "Chain {0} for {1}s:\n{2}".format(count, effect.duration, effect.to_str(tabs + 1))
            count += 1
            
        return result
    
    def print(self, tabs = 0):
        print(self.to_str(tabs))
        