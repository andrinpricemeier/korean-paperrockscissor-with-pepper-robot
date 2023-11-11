
class Corpus:
    """Represents the entirety of the words and sentences spoken by the robot.
    """
    def __init__(self, dictionary, random_source):
        """Creates a new instance.

        Args:
            dictionary (dict[str]): The dictionary containing the actual sentences and words.
            random_source (RandomSource): an entity that has the ability of creating random numbers.
        """
        self.dictionary = dictionary
        self.random_source = random_source

    def lookup(self, entity_id):
        """Lookups an entry by its ids.

        Args:
            entity_id (str): the id of the entry in the dictionary.

        Returns:
            str: the resolved entry. If multiple entries are present, an entry is chosen at random.
        """
        if entity_id in self.dictionary:
            possible_entities = self.dictionary[entity_id]
            choice = self.random_source.randint(0, len(possible_entities) - 1)
            return possible_entities[choice]
        else:
            return entity_id

    def lookup_with_args(self, entity_id, *args):
        """Looks up an entry by its id and optional arguments.

        Args:
            entity_id (str): the id of the entry in the dictionary.

        Returns:
            str: the resolved entry. If multiple entries are present, an entry is chosen at random.
        """
        entity = self.lookup(entity_id)
        return entity.format(*args)
        
