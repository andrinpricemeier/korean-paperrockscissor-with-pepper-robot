import time


class Dialog:

    def __init__(self, robot):
        self.__al_tts = robot.ALTextToSpeech

    def say(self, text):
        self.__al_tts.say(text)

    def say_slowly(self, text):
        # to be implemented
        pass

    def shout(self, text):
        # to be implemented
        pass

    def add_simple_reaction(self, user_input, robot_output):
        # to be implemented
        pass

    def load_yes_no_question(self, question, reaction_yes, reaction_no):
        # to be implemented
        pass

    def ask_yes_no_question(self, topic):
        # to be implemented
        pass

    def start_topic(self, topic_name):
        # to be implemented
        pass

    def stop_topic(self, topic_name):
        # to be implemented
        pass

    def close_session(self):
        # to be implemented
        pass
