class RandomSource():
    """Represents a source of random numbers.
    We hide this functionality in a class to make code that uses random numbers testable and deterministic.
    """
    def randint(self, lower_inclusive, upper_incluse):
        """Generates a random number.

        Args:
            lower_inclusive (int): the lower bound
            upper_incluse (int): the upper bound
        """
        pass

    def weighted_choice(self, weighted_choices):
        """Returns an entry randomly, each choice being weighted.

        Args:
            weighted_choices ((choice, weight)): the weighted choices
        """
        pass