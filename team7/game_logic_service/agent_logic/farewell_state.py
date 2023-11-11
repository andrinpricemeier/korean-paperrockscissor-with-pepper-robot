from agent_logic.brain_constants import DIBI_SPEAKER
from agent_logic.state import State
from agent_logic.brain_constants import DIBI_OPPONENTNAME
import logging

class FarewellState(State):
    """The state in which the robot says good bye and stops the game.
    """
    def __init__(self, state_machine, brain):
        self.state_machine = state_machine
        self.brain = brain

    def enter(self):
        logging.info("Starting farewell state.")
        speaker = self.brain.get_value(DIBI_SPEAKER)
        opponent_name = self.brain.get_value(DIBI_OPPONENTNAME)
        if opponent_name is None:
            speaker.say("farewell")
        else:
            speaker.say_with_args("farewell_with_name", opponent_name)
        self.state_machine.transition(None)
        logging.info("Farewell state done.")
        

