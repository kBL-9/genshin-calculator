from constants import INDENTATION, DamageType

def add_bonus(stats_dict: dict, bonus_type: DamageType, value: float):
    if bonus_type == DamageType.PYRO:
        add_value_to_dict(stats_dict, "pyro", value)
    elif bonus_type == DamageType.HYDRO:
        add_value_to_dict(stats_dict, "hydro", value)
    elif bonus_type == DamageType.DENDRO:
        add_value_to_dict(stats_dict, "dendro", value)
    elif bonus_type == DamageType.ELECTRO:
        add_value_to_dict(stats_dict, "electro", value)
    elif bonus_type == DamageType.CRYO:
        add_value_to_dict(stats_dict, "cyro", value)
    elif bonus_type == DamageType.ANEMO:
        add_value_to_dict(stats_dict, "anemo", value)
    elif bonus_type == DamageType.GEO:
        add_value_to_dict(stats_dict, "geo", value)
    elif bonus_type == DamageType.PHYSICAL:
        add_value_to_dict(stats_dict, "physical", value)
    else:
        print("Wrong bonus type inputted")

def add_value_to_dict(stats_dict: dict, key: str, value: int):
    if key not in stats_dict:
        stats_dict[key] = value
        return
    
    stats_dict[key] += value

def sub_value_from_dict(stats_dict: dict, key: str, value: int):
    if key in stats_dict:
        stats_dict[key] = max(stats_dict[key] - value, 0)

def get_value_from_dict(stats_dict: dict, key: str):
    return stats_dict[key] if key in stats_dict else 0.0

class Stats:
    def __init__(self, has_substat: bool = False):
        self.stats = {
            "bonus": {},
        }
        
        self.print_stats = {
            "HP": lambda: self.stats["hp"] if "hp" in self.stats else "",
            "HP%": lambda: "{0}%".format(self.stats["hp%"] * 100) if "hp%" in self.stats else "",
            "ATK": lambda: self.stats["atk"] if "atk" in self.stats else "",
            "ATK%": lambda: "{0}%".format(self.stats["atk%"] * 100) if "atk%" in self.stats else "",
            "DEF": lambda: self.stats["def"] if "def" in self.stats else "",
            "DEF%": lambda: "{0}%".format(self.stats["def%"] * 100) if "def%" in self.stats else "",
            "Elemental Mastery": lambda: self.stats["em"] if "em" in self.stats else "",
            "Energy Recharge": lambda: "{0}%".format(self.stats["er"] * 100) if "er" in self.stats else "",
            "Crit Rate": lambda: "{0}%".format(self.stats["cr"] * 100) if "cr" in self.stats else "",
            "Crit Damage": lambda: "{0}%".format(self.stats["cd"] * 100) if "cd" in self.stats else "",
            "Pyro DMG Bonus": lambda: "{0}%".format(self.stats["bonus"]["pyro"] * 100) if "pyro" in self.stats["bonus"] else "",
            "Hydro DMG Bonus": lambda: "{0}%".format(self.stats["bonus"]["hydro"] * 100) if "hydro" in self.stats["bonus"] else "",
            "Anemo DMG Bonus": lambda: "{0}%".format(self.stats["bonus"]["anemo"] * 100) if "anemo" in self.stats["bonus"] else "",
            "Dendro DMG Bonus": lambda: "{0}%".format(self.stats["bonus"]["dendro"] * 100) if "dendro" in self.stats["bonus"] else "",
            "Geo DMG Bonus": lambda: "{0}%".format(self.stats["bonus"]["geo"] * 100) if "geo" in self.stats["bonus"] else "",
            "Electro DMG Bonus": lambda: "{0}%".format(self.stats["bonus"]["electro"] * 100) if "electro" in self.stats["bonus"] else "",
            "Cryo DMG Bonus": lambda: "{0}%".format(self.stats["bonus"]["cyro"] * 100) if "cyro" in self.stats["bonus"] else "",
            "Physical DMG Bonus": lambda: "{0}%".format(self.stats["bonus"]["physical"] * 100) if "physical" in self.stats["bonus"] else "",
            "Healing Bonus": lambda: "{0}%".format(self.stats["bonus"]["healing"] * 100) if "healing" in self.stats["bonus"] else "",
        }
        
        if not has_substat:
            self.stats["bonus"]["resist"] = {}
        
    def add_stats(stats):
        for (name, value) in stats.items():
            if name == "bonus":
                for (name, value) in stats["bonus"].items():
                    if name == "resist":
                        for (name, value) in stats["bonus"]["resist"].items():
                            add_value_to_dict(self.stats["bonus"]["resist"], name, value)
                        continue
                        
                    add_value_to_dict(self.stats["bonus"], name, value)
                continue
                
            add_value_to_dict(self.stats, name, value)
        return self
            
    def remove_stats(stats):
        for (name, value) in stats.items():
            if name == "bonus":
                for (name, value) in stats["bonus"].items():
                    if name == "resist":
                        for (name, value) in stats["bonus"]["resist"].items():
                            sub_value_from_dict(self.stats["bonus"]["resist"], name, value)
                        continue
                        
                    sub_value_from_dict(self.stats["bonus"], name, value)
                continue
                
            sub_value_from_dict(self.stats, name, value)            
        return self
            
    def add_hp(self, value: float, is_flat: bool = False):
        if is_flat:
            add_value_to_dict(self.stats, "hp", value)
        else:
            add_value_to_dict(self.stats, "hp%", value / 100)

        return self

    def add_atk(self, value: float, is_flat: bool = False):
        if is_flat:
            add_value_to_dict(self.stats, "atk", value)
        else:
            add_value_to_dict(self.stats, "atk%", value)

        return self
        
    def add_def(self, value: float, is_flat: bool = False):
        if is_flat:
            add_value_to_dict(self.stats, "def", value)
        else:
            add_value_to_dict(self.stats, "def%", value)

        return self
        
    def add_em(self, value: float):
        add_value_to_dict(self.stats, "em", value)
        return self
        
    def add_elemental_mastery(self, value: float):
        return self.add_em(value)
        
    def add_er(self, value: float):
        add_value_to_dict(self.stats, "er", value / 100)
        return self
        
    def add_energy_recharge(self, value: float):
        return self.add_er(value)
        
    def add_dmg_bonus(self, value: float, bonus_type: DamageType):
        add_bonus(self.stats["bonus"], bonus_type, value / 100)
        return self
        
    def add_cr(self, value: float):
        add_value_to_dict(self.stats, "cr", value / 100)
        return self
     
    def add_crit_rate(self, value: float):
        return self.add_cr(value)
        
    def add_cd(self, value: float):
        add_value_to_dict(self.stats, "cd", value / 100)
        return self
     
    def add_crit_dmg(self, value: float):
        return self.add_cd(value)
        
    def add_healing_bonus(self, value: float):
        add_value_to_dict(self.stats["bonus"], "healing", value / 100)
        
    def get_flat_hp(self): return get_value_from_dict(self.stats, "hp")
    def get_hp_percent(self): return get_value_from_dict(self.stats, "hp%")
    def get_flat_atk(self): return get_value_from_dict(self.stats, "atk")
    def get_atk_percent(self): return get_value_from_dict(self.stats, "atk%")
    def get_flat_def(self): return get_value_from_dict(self.stats, "def")
    def get_def_percent(self): return get_value_from_dict(self.stats, "def%")
    def get_em(self): return get_value_from_dict(self.stats, "em")
    def get_elemental_mastery(self): return get_value_from_dict(self.stats, "em")
    def get_er(self): return get_value_from_dict(self.stats, "er")
    def get_energy_recharge(self): return get_value_from_dict(self.stats, "er")
    def get_cr(self): return get_value_from_dict(self.stats, "cr")
    def get_crit_rate(self): return get_value_from_dict(self.stats, "cr")
    def get_cd(self): return get_value_from_dict(self.stats, "cd")
    def get_crit_damage(self): return get_value_from_dict(self.stats, "cd")
    def get_healing_bonus(self): return get_value_from_dict(self.stats["bonus"], "healing")
    def get_damage_bonus(self, damage_type: DamageType): return get_value_from_dict(self.stats["bonus"], damage_type.name.lower())
        
    def to_str(self, tabs = 0):
        result = ""
        for (stat_name, get_stat_value) in self.print_stats.items():
            value = get_stat_value()
            if len(value) != 0:
                result += "{0}{1}: {2}".format(INDENTATION * tabs, stat_name, value)
        
        return result
        
    def print(self, tabs: int = 0):
        print(self.to_str(tabs))