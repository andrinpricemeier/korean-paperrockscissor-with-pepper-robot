import random

from utils.random_source import RandomSource

class PseudoRandomSource(RandomSource):
    """Represents a source of pseudo random numbers.
    """
    def randint(self, lower_inclusive, upper_inclusive):
        return random.randint(lower_inclusive, upper_inclusive)

    def weighted_choice(self, weighted_choices):
        total = sum(w for c, w in weighted_choices)
        r = random.uniform(0, total)
        upto = 0
        for c, w in weighted_choices:
            if upto + w >= r:
                return c
            upto += w