from agent_logic.brain_constants import DIBI_BODY, DIBI_DIALOG, DIBI_SPEAKER
from agent_logic.state import State
from actuators.dibi_pose import DibiPose
from agent_logic.learn_opponent_state import LearnOpponentState
from agent_logic.farewell_state import FarewellState
import logging

class ExplanationState(State):    
    """The state in which the robot explains how the game is played.
    """
    def __init__(self, state_machine, brain):
        self.state_machine = state_machine
        self.brain = brain

    def enter(self):
        logging.info("Starting explanation state")
        dialog = self.brain.get_value(DIBI_DIALOG)
        wants_explanation = dialog.ask("ask_explanation_required", "ask_explanation_accepted_reaction", "ask_explanation_declined_reaction")
        if wants_explanation is not None and wants_explanation == 0:
            logging.info("Opponent wants explanation.")
            self.__explain()
        else:
            logging.info("Opponent doesn't want explanation.")
            self.state_machine.transition(LearnOpponentState(self.state_machine, self.brain))
        logging.info("Explanation state done.")

    def __explain(self):
        body = self.brain.get_value(DIBI_BODY)
        speaker = self.brain.get_value(DIBI_SPEAKER)
        dialog = self.brain.get_value(DIBI_DIALOG)
        while True:
            speaker.say("explanation_introduction")
            speaker.say("explanation_basics")
            speaker.say("explanation_roles")
            speaker.say("explanation_pose_scissor")
            body.assume_pose(DibiPose["SCISSOR"])
            speaker.say("explanation_pose_paper")
            body.assume_pose(DibiPose["PAPER"])
            speaker.say("explanation_pose_rock")
            body.assume_pose(DibiPose["ROCK"])
            understood = dialog.ask("ask_explanation_understood", "ask_explanation_understood_yes", "ask_explanation_understood_no")
            if understood is None or understood == 0:                
                if self.state_machine.is_done:
                    self.state_machine.transition(FarewellState(self.state_machine, self.brain))
                    break
                else:
                    logging.info("Opponent is satisifed with explanation or didn't answer.")
                    self.state_machine.transition(LearnOpponentState(self.state_machine, self.brain))
                    break
            else:
                logging.info("Opponent wants explanation to be repeated.")

