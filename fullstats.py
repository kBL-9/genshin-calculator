from stats import Stats, add_value_to_dict, get_value_from_dict
from constants import DamageType

class FullStats(Stats):
    def __init__(self):
        Stats.__init__(self, is_substat = True)
        self.stats["bonus"]["resist"] = {}
        self.stats["reduction"] = { "resist": {} }
        self.stats["reduction"] = {}
        self.stats["ignore"] = {}
        self.print_stats = {
            ## Bonus
            "Pyro Resistance Bonus": lambda: "{0}%".format(self.get_resist_bonus(DamageType.PYRO) * 100),
            "Hydro Resistance Bonus": lambda: "{0}%".format(self.get_resist_bonus(DamageType.HYDRO) * 100),
            "Anemo Resistance Bonus": lambda: "{0}%".format(self.get_resist_bonus(DamageType.ANEMO) * 100),
            "Dendro Resistance Bonus": lambda: "{0}%".format(self.get_resist_bonus(DamageType.DENDRO) * 100),
            "Geo Resistance Bonus": lambda: "{0}%".format(self.get_resist_bonus(DamageType.GEO) * 100),
            "Electro Resistance Bonus": lambda: "{0}%".format(self.get_resist_bonus(DamageType.ELECTRO) * 100),
            "Cryo Resistance Bonus": lambda: "{0}%".format(self.get_resist_bonus(DamageType.CYRO) * 100),
            "Physical Resistance Bonus": lambda: "{0}%".format(self.get_resist_bonus(DamageType.PHYSICAL) * 100),
            ## Reduction
            "Pyro Resistance Reduction": lambda: "{0}%".format(self.get_resist_reduce(DamageType.PYRO) * 100),
            "Hydro Resistance Reduction": lambda: "{0}%".format(self.get_resist_reduce(DamageType.HYDRO) * 100),
            "Anemo Resistance Reduction": lambda: "{0}%".format(self.get_resist_reduce(DamageType.ANEMO) * 100),
            "Dendro Resistance Reduction": lambda: "{0}%".format(self.get_resist_reduce(DamageType.DENDRO) * 100),
            "Geo Resistance Reduction": lambda: "{0}%".format(self.get_resist_reduce(DamageType.GEO) * 100),
            "Electro Resistance Reduction": lambda: "{0}%".format(self.get_resist_reduce(DamageType.ELECTRO) * 100),
            "Cryo Resistance Reduction": lambda: "{0}%".format(self.get_resist_reduce(DamageType.CRYO) * 100),
            "Physical Resistance Reduction": lambda: "{0}%".format(self.get_resist_reduce(DamageType.PHYSICAL) * 100),
            "DEF Reduction": lambda: "{0}%".format(self.get_def_reduction() * 100),
            "DEF Ignore": lambda: "{0}%".format(self.get_def_ignore() * 100)
        }

    def add_resist_bonus(self, value: float, bonus_type: DamageType):
        add_bonus(self.stats["bonus"]["resist"], bonus_type, value / 100)
        return self
    
    def add_def_reduction(self, value: float):
        add_value_to_dict(self.stats["reduction"], "def", value / 100)
        return self
        
    def add_def_ignore(self, value: float):
        add_value_to_dict(self.stats["ignore"], "def", value / 100)
        return self
    
    def add_resist_reduce(self, value: float, resist_type: DamageType):
        add_bonus(self.stats["reduction"]["resist"], resist_type, value / 100)
        return self
        
    def add_flat_damage(self, value: float):
        add_value_to_dict(self.stats, "flat_damage", value)
        return self
        
    def get_resist_bonus(self, bonus_type: DamageType):
        return get_value_from_dict(self.stats["bonus"]["resist"], bonus_type.name.lower())
        
    def get_resist_reduction(self, reduce_type: DamageType):
        return get_value_from_dict(self.stats["reduction"]["resist"], reduce_type.name.lower())
        
    def get_def_reduction(self):
        return get_value_from_dict(self.stats["reduction"], "def")
        
    def get_def_ignore(self):
        return get_value_from_dict(self.stats["ignore"], "def")
        
    def get_flat_damage(self):
        return get_value_from_dict(self.stats, "flat_damage")
    