from sensors.mood_detector import MoodDetector
import logging

class DibiMoodDetector(MoodDetector):
    def __init__(self, mood):
        self.mood = mood
        
    def detect(self):
        valence = self.mood.currentPersonState()["valence"]["value"]
        logging.info("Current valence. {0}".format(valence))
        mood = self.__valence_to_mood(valence)
        logging.info("Current mood: {0}".format(mood))
        return mood

    def __valence_to_mood(self, valence):
        # Safety margin.
        # We only consider positive/negative to simplify our "motivation" model
        if valence < -0.10:
            return "negative"
        else:
            return "positive"
