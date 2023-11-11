from pepper import Robot, PepperConfiguration

from dialog_sol import Dialog
from speech_recognition import SpeechRecognition
import time


class Application(object):

    def __init__(self):
        config = PepperConfiguration("Amber")
        robot = Robot(config)
        self.__dialog = Dialog(robot)
        self.__start = False
        self.__stop = False
        vocabulary = ["let's start", "stop"]
        self.__speech_recognition = SpeechRecognition(robot, vocabulary, self.__speech_callback)

    def run(self):
        print "running programm"
        counter = 0
        while not self.__stop and counter < 15:
            print "iteration " + str(counter)
            if self.__start:
                self.__dialog.say("ok let's start")
                self.__start = False
                print "starting"
            time.sleep(1)
            counter += 1

        self.__dialog.say("ok i stop it now")
        self.__speech_recognition.unsubscribe()
        self.__dialog.close_session()

    def __speech_callback(self, value):
        print("recognized the following word:" + value[0] + " with accuracy: " + str(value[1]))
        if value[0] == "let's start":
            if value[1] > 0.35:
                print "received start signal"
                self.__start = True
        if value[0] == "stop":
            if value[1] > 0.35:
                print "received stop signal"
                self.__stop = True


app = Application()
app.run()