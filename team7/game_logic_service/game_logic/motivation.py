import pandas as pd
from datetime import datetime

class Motivation():
    """Represents the player's motivation to keep playing.
    The motivation is a combination of the mood of the player and how many times he has lost.
    """
    def __init__(self):
        self.moods = []
        self.outcomes = []
        self.happy = []
        self.dates = []

    def record_impression(self, mood, won_round):
        """Records the player's mood and whether he won.

        Args:
            mood (str): one of: positive, neutral, negative, unknown
            won_round (bool): True, if the player won the round
        """
        # We assume that the ALMood service is wrong a lot thus we only treat
        # definitely detected negative moods as negative.
        if mood == "negative":
            self.moods.append(0)
        else:
            self.moods.append(1)
        if won_round:
            self.outcomes.append(1)
        else:
            self.outcomes.append(0)
        # Used to calculate the cumulative maximum happiness.
        self.happy.append(1)
        # Needed by pandas.ewm
        self.dates.append(datetime.now())

    def calculate_motivational_factor(self):
        """Calculates the motivation of the player.
        This is in simple terms the ratio of the actual mood/progress to
        the maximum amount of happiness the player could achieve (always winning and always happy).

        Returns:
            float: the motivation of the player, from 0 to 1. 0 meaning the player will quit very soon, 1 meaning the player is very motivated and happy.
        """
        # Not enough data: assume everything is alright.
        if len(self.moods) <= 1:
            return 1
        df = pd.DataFrame({'moods': self.moods, 'outcomes': self.outcomes, 'dates': self.dates, 'happy': self.happy})
        # We give a lower weight to the mood because the opponent most likely doesn't react at all.
        df['cumulative motivation'] = 0.3*df['moods'] + 0.7*df['outcomes']
        # We use a very high alpha to punish older entries.
        # The opponent won't remember that he lost 10 rounds before.
        ewm = df.set_index('dates').ewm(alpha=0.9).mean()
        ewm = ewm.cumsum()
        ewm['motivation'] = ewm['cumulative motivation'] / ewm['happy']
        motivational_factor = ewm['motivation'].iloc[-1]
        return motivational_factor