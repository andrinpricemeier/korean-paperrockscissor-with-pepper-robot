from pepper import Robot, PepperConfiguration

from dialog import Dialog
from speech_recognition import SpeechRecognition
import time


class Application(object):

    def __init__(self):
        config = PepperConfiguration("Amber")
        robot = Robot(config)
        self.__start = False
        self.__stop = False
        vocabulary = ["let's start", "stop"]
        self.__speech_recognition = SpeechRecognition(robot, vocabulary, self.__speech_callback)

    def run(self):
        # to implement
        pass

    def __speech_callback(self, value):
        # to implement
        pass


app = Application()
app.run()