class Dialog():
    """Abstract class for holding conversations with questions.
    """
    def ask_with_text(self, question_text, reaction_one_text, reaction_two_text):
        """Asks a question

        Args:
            question_text (str): the id of the question to lookup in the corpus.
            reaction_one_text (str): the first reaction (e.g. yes)
            reaction_two_text (str): the second reaction (e.g. no)
        """
        pass

    def ask(self, question_id, reaction_one_id, reaction_two_id):
        """Asks a question

        Args:
            question_id (str): the id of the question to lookup in the corpus.
            reaction_one_id (str): the first reaction (e.g. yes)
            reaction_two_id (str): the second reaction (e.g. no)
        """
        pass