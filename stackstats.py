from fullstats import FullStats
from stats import Stats

class StackStats(FullStats):
    def __init__(self, has_substats: False):
        FullStats.__init__(self, has_substats)
        self.main_stack = []
        self.stack = []

    def append_stats(self, stats: Stats):
        self.stack.append(stats)
        return self

    def apply_stats(self):
        for stats in self.stack:
            self.add_stats(stats)
            self.main_stack.append(stats)
        self.stack = []

    def pop_stats(self):
        self.remove_stats(self.main_stack.pop())
        return self
