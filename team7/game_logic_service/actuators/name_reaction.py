import logging
class NameReaction():
    """Contains the reaction to certain names given to the opponent.
    """
    def __init__(self, speaker):
        self.speaker = speaker
        self.reactions = {}

    def add(self, name, reaction_id):
        """Adds a reaction mapping.

        Args:
            name (str): the opponent's name
            reaction_id (str): the id of the reaction looked up in the corpus.
        """
        self.reactions[name.lower()] = reaction_id

    def react(self, name):
        """Reacts to a chosen opponent's name. Does nothing if no mapping exists.

        Args:
            name (str): the opponent's name
        """
        if name.lower() in self.reactions:
            logging.info("Reacting to {0}".format(name))
            self.speaker.say(self.reactions[name.lower()])
        else:
            logging.info("No reaction for {0} found.".format(name))
