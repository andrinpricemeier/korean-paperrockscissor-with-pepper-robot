from utils.random_source import RandomSource

class StaticRandomSource(RandomSource):
    """Represents a random source that is deterministic, i.e. that always returns the same for each call.
    """
    def randint(self, lower_inclusive, upper_incluse):
        return lower_inclusive

    def weighted_choice(self, weighted_choices):
        return weighted_choices[0][0]