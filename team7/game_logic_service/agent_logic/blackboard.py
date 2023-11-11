import logging
class Blackboard():
    """Represents state that can be stored and accessed by different parts of the agent.
    """
    def __init__(self):
        self.db = {}

    def set_value(self, key, value):
        self.db[key] = value

    def get_value(self, key):
        logging.debug("Retrieving key {0} from blackboard.".format(key))
        if key in self.db:
            return self.db[key]
        return None