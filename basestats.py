from stats import Stats, get_value_from_dict

class BaseStats(Stats):
    def add_base_atk(self, value: float):
        self.stats["base_atk"] = self.print_stats["Base ATK"] = value
        
    def add_base_hp(self, value: float):
        self.stats["base_hp"] = self.print_stats["Base HP"] = value
        
    def add_base_def(self, value: float):
        self.stats["base_def"] = self.print_stats["Base DEF"] = value
        
    def add_ascension_atk(self, value: float):
        self.stats["base_atk"] = self.print_stats["Base ATK"] = self.stats["base_atk"] * value / 100
        
    def add_ascension_hp(self, value: float):
        self.stats["base_hp"] = self.print_stats["Base HP"] = self.stats["base_hp"] * value / 100
        
    def add_ascension_def(self, value: float):
        self.stats["base_def"] = self.print_stats["Base DEF"] = self.stats["base_def"] * value / 100
        
    def get_base_atk(self): return get_value_from_dict(self.stats, "base_atk")
    def get_base_hp(self): return get_value_from_dict(self.stats, "base_hp")
    def get_base_def(self): return get_value_from_dict(self.stats, "base_def")