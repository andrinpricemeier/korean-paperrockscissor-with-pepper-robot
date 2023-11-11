from agent_logic.brain_constants import DIBI_ACTIVEGAME, DIBI_DIALOG, DIBI_SPEAKER
from game_logic.follower import Follower
from game_logic.leader import Leader
from agent_logic.state import State
from agent_logic.fighting_state import FightingState
from agent_logic.farewell_state import FarewellState
import logging

class AskRoleState(State):
    """The state in which the robot asks what role the opponent wants to be.
    """
    def __init__(self, state_machine, brain):
        self.state_machine = state_machine
        self.brain = brain

    def enter(self):
        logging.info("Starting ask role state.")
        game = self.brain.get_value(DIBI_ACTIVEGAME)
        dialog = self.brain.get_value(DIBI_DIALOG)
        speaker = self.brain.get_value(DIBI_SPEAKER)
        chosen_role = dialog.ask("ask_what_role_do_you_want_start_with", "ask_what_role_do_you_want_start_with_leader", "ask_what_role_do_you_want_start_with_follower")
        if chosen_role is None:            
            logging.info("Opponent didn't specify what role to play.")
            # The role has been predefined at setup already, no need to do anything.
            speaker.say("ask_what_role_do_you_want_start_with_not_understood")
        elif chosen_role == 0:
            logging.info("Opponent wants to be leader.")
            game.set_roles(Follower(), Leader())
        else:
            logging.info("Opponent wants to be follower.")
            game.set_roles(Leader(), Follower())
        if self.state_machine.is_done:
            self.state_machine.transition(FarewellState(self.state_machine, self.brain))
        else:
            self.state_machine.transition(FightingState(self.state_machine, self.brain))
        logging.info("Ask role state done.")

