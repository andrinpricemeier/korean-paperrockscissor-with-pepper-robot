from agent_logic.ask_role_state import AskRoleState
from agent_logic.brain_constants import DIBI_CORPUS, DIBI_DIALOG, DIBI_FACEDETECTOR, DIBI_GAMEREGION, DIBI_NAMEREACTION, DIBI_OPPONENTNAME, DIBI_SPEAKER
from agent_logic.state import State
from agent_logic.farewell_state import FarewellState
import logging
class LearnOpponentState(State):
    """The state in which the robot gives the opponent a name and learns their name.
    """
    def __init__(self, state_machine, brain):
        self.state_machine = state_machine
        self.brain = brain

    def enter(self):
        logging.info("Starting learn opponent state")
        dialog = self.brain.get_value(DIBI_DIALOG)
        corpus = self.brain.get_value(DIBI_CORPUS)
        name_reaction = self.brain.get_value(DIBI_NAMEREACTION)       
        wants_name = dialog.ask("ask_if_opponent_wants_name", "ask_if_opponent_wants_name_yes", "ask_if_opponent_wants_name_no")
        logging.info(str(wants_name))
        if wants_name is not None and wants_name == 0:
            tries = 3
            while tries > 0:
                logging.info("Asking for name.")
                random_name = corpus.lookup("opponent_names")
                logging.info("Picked " + str(random_name))
                name_ok = dialog.ask_with_text(corpus.lookup_with_args("ask_name_opinion", random_name), corpus.lookup("ask_name_opinion_yes"), corpus.lookup("ask_name_opinion_no"))
                if name_ok is not None and name_ok == 0:
                    name_reaction.react(random_name)
                    self.brain.set_value(DIBI_OPPONENTNAME, random_name)
                    self.__learn_face(random_name)
                    break
                else:
                    tries -= 1
               
        if self.state_machine.is_done:
            self.state_machine.transition(FarewellState(self.state_machine, self.brain))
        else:
            self.state_machine.transition(AskRoleState(self.state_machine, self.brain))
        logging.info("Learn opponent state done.")

    def __learn_face(self, opponent_name):
        face_detector = self.brain.get_value(DIBI_FACEDETECTOR)
        speaker = self.brain.get_value(DIBI_SPEAKER)
        game_region = self.brain.get_value(DIBI_GAMEREGION)
        speaker.say("learn_face_come_closer")
        game_region.ensure_is_in_zone(1)
        success = face_detector.learn_face(opponent_name)
        name = face_detector.get_current_face_name()
        logging.info("Current face: {0}".format(name))
        if success:
            speaker.say("learn_face_success")
        else:
            speaker.say("learn_face_failure")


        

