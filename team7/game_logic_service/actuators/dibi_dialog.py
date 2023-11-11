import time
import logging
from actuators.dialog import Dialog

class DibiDialog(Dialog):
    def __init__(self, dialog, corpus, memory):
        self.dialog = dialog
        self.corpus = corpus
        self.memory = memory

    def ask_with_text(self, question_text, reaction_one_text, reaction_two_text):
        logging.info("Asking {0} with reaction 1: {1} and reaction 2: {2}".format(question_text, reaction_one_text, reaction_two_text))
        id = 1
        self.dialog.openSession(id)
        topic = "question"
        topic_content = ('topic: ~' + topic + '()\n'
                        'language: enu\n'
                        'include: lexicon_enu.top\n'
                        'proposal: ' + question_text + '\n'
                        '   u1: ' + reaction_one_text + ' $answer=0\n'
                        '   u1: ' + reaction_two_text + ' $answer=1\n'
                        )
        self.dialog.loadTopicContent(topic_content)
        self.dialog.activateTopic(topic)
        self.dialog.setFocus(topic)
        self.dialog.subscribe('anything')
        self.dialog.forceOutput()
        logging.info("Waiting for answer...")
        time.sleep(3)
        answer = self.dialog.getUserData("answer", id)
        self.dialog.deactivateTopic(topic)
        self.dialog.unloadTopic(topic)
        self.dialog.closeSession()
        logging.info("Received answer: {0}".format(answer))
        if answer == '':
            logging.info("Returning none.")
            return None
        else:
            logging.info("Returning {0}".format(answer))
            return int(answer)

    def ask(self, question_id, reaction_one_id, reaction_two_id):
        return self.ask_with_text(self.corpus.lookup(question_id), self.corpus.lookup(reaction_one_id), self.corpus.lookup(reaction_two_id))