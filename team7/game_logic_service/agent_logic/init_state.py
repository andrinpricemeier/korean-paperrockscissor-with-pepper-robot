from agent_logic.brain_constants import DIBI_SPEAKER, DIBI_OPPONENTNAME
from agent_logic.state import State
from agent_logic.explanation_state import ExplanationState
from agent_logic.ask_role_state import AskRoleState
import logging
class InitState(State):
    """The state in which the robot introduces the game and controls what comes next.
    """
    def __init__(self, state_machine, brain):
        self.state_machine = state_machine
        self.brain = brain

    def enter(self):
        logging.info("Starting init state.")
        speaker = self.brain.get_value(DIBI_SPEAKER)
        opponent_name = self.brain.get_value(DIBI_OPPONENTNAME)
        if opponent_name is not None:
            speaker.say_with_args("welcome_player_with_name", opponent_name)
            # Skip explanation and learning opponent name and skip directly to role selection.
            self.state_machine.transition(AskRoleState(self.state_machine, self.brain))
        else:
            speaker.say("welcome_to_game")
            self.state_machine.transition(ExplanationState(self.state_machine, self.brain))
        logging.info("Init state done.")
        

