from fullstats import FullStats

class Enemy:
	def __init__(self, name: str, level: int = 90, base_stats: FullStats):
        self.name = name
        self.level = level
        self.stats = base_stats