import time


class Dialog:

    def __init__(self, robot):
        self.__my_id = 123
        self.__al_dialog = robot.session.service("ALDialog")
        self.__al_tts = robot.ALTextToSpeech
        self.__al_dialog.setLanguage("English")
        self.__al_audio = robot.ALAudioDevice
        self.__al_dialog.openSession(self.__my_id)

    def say(self, text_to_say):
        self.__al_tts.say(text_to_say)

    def say_slowly(self, text_to_say):
        original_speed = self.__al_tts.getParameter("speed")
        self.__al_tts.setParameter("speed", 50)
        self.__al_tts.say(text_to_say)
        self.__al_tts.setParameter("speed", original_speed)

    def shout(self, text_to_say):
        original_volume = self.__al_audio.getOutputVolume()
        self.__al_audio.setOutputVolume(min(original_volume + 20, 100))
        original_pitch = self.__al_tts.getParameter("pitch")
        pitch = 80
        self.__al_tts.setParameter("pitch", pitch)
        self.__al_tts.say(text_to_say)
        self.__al_tts.setParameter("pitch", original_pitch)
        self.__al_audio.setOutputVolume(original_volume)

    def add_simple_reaction(self, topic_name, user_input, robot_output):
        topic_content = ('topic: ~' + topic_name + '()\n'
                         'language: enu\n'
                         'u:(' + user_input + ') ' + robot_output + '\n')
        self.__al_dialog.loadTopicContent(topic_content)

    def load_yes_no_question(self, topic_name, question, reaction_yes, reaction_no):
        topic_content = ('topic: ~' + topic_name + '()\n'
                         'language: enu\n'
                         'proposal: ' + question + '\n'
                         '   u1: (no) ' + reaction_no + ' $agree=0\n'
                         '   u1: (yes) ' + reaction_yes + ' $agree=1\n'
                         )
        self.__al_dialog.loadTopicContent(topic_content)

    def ask_yes_no_question(self, topic):
        self.__al_dialog.activateTopic(topic)
        self.__al_dialog.subscribe('myself')
        self.__al_dialog.setFocus(topic)  # focus on this topic (important for proposals)
        self.__al_dialog.forceOutput()  # start proposal sentence
        time.sleep(5)
        do_agree = self.__al_dialog.getUserData("agree", self.__my_id)
        self.__al_dialog.deactivateTopic(topic)
        return do_agree

    def start_topic(self, topic_name):
        self.__al_dialog.activateTopic(topic_name)
        self.__al_dialog.setFocus(topic_name)

    def stop_topic(self, topic_name):
        self.__al_dialog.deactivateTopic(topic_name)
        self.__al_dialog.unloadTopic(topic_name)

    def close_session(self):
        self.__al_dialog.closeSession()