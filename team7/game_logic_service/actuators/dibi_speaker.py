from actuators.speaker import Speaker
import time
import logging

class DibiSpeaker(Speaker):
    def __init__(self, tts, animated_tts, memory, corpus, audio, slow_speaking_speed_in_percent, shouting_volume_increase_in_percent, shouting_pitch):
        self.tts = tts
        self.animated_tts = animated_tts
        self.memory = memory
        self.corpus = corpus
        self.audio = audio
        self.slow_speaking_speed_in_percent = slow_speaking_speed_in_percent
        self.shouting_volume_increase_in_percent = shouting_volume_increase_in_percent
        self.shouting_pitch = shouting_pitch

    def say(self, text_id):
        logging.info("Saying {0}".format(text_id))
        self.animated_tts.say(self.corpus.lookup(text_id))
        time.sleep(2)
        
    def say_with_args(self, text_id, *args):
        logging.info("Saying {0} with args".format(text_id))
        self.animated_tts.say(self.corpus.lookup_with_args(text_id, args))
        time.sleep(2)

    def say_slowly(self, text_id):
        logging.info("Saying {0} slowly".format(text_id))
        original_speed = self.tts.getParameter("speed")
        try:
            self.tts.setParameter("speed", self.slow_speaking_speed_in_percent)
            self.tts.say(self.corpus.lookup(text_id))
        finally:
            self.tts.setParameter("speed", original_speed)

    def shout(self, text_id):
        logging.info("Shouting {0}".format(text_id))
        original_volume = self.audio.getOutputVolume()
        original_pitch = self.tts.getParameter("pitch")
        try:
            self.audio.setOutputVolume(min(original_volume + self.shouting_volume_increase_in_percent, 100))
            pitch = self.shouting_pitch
            self.tts.setParameter("pitch", pitch)
            self.tts.say(self.corpus.lookup(text_id))
        finally:
            self.tts.setParameter("pitch", original_pitch)
            self.audio.setOutputVolume(original_volume)
