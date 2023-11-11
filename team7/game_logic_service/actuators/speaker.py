class Speaker:
    """Represents the speaker of the robot.
    """
    def say(self, text_id):
        """Says the text out loud, animated.

        Args:
            text_id (str): the id of the text to lookup and say in the corpus.
        """
        pass

    def say_with_args(self, text_id, *args):
        """Says the text including optional arguments.
        E.g. "Hello, {0}" where {0} is replaced with the first entry of *args.

        Args:
            text_id (str): the text id
        """
        pass

    def say_slowly(self, text_id):
        """Says a text slowly.

        Args:
            text_id (str): id of the text.
        """
        pass

    def shout(self, text_id):
        """Shouts the text.

        Args:
            text_id (str): the id of the text to say.
        """
        pass