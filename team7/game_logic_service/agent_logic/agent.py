from agent_logic.state_machine import StateMachine
from agent_logic.init_state import InitState
from agent_logic.brain_constants import DIBI_GAMEREGION
import logging
import thread
import threading
import time

class Agent():
    """Represents a rational agent, in this case, one that can play the dibi game.
    """
    def __init__(self, brain):
        """Creates a new instance.

        Args:
            brain (Blackboard): represents the mind, the brain, of the agent, using the blackboard pattern.
        """
        self.brain = brain
        self.thread = threading.Thread(target=self.__start_watching)
        self.thread.daemon = True
        self.agent_is_running = False

    def run(self):
        """Awakens and starts the agent.
        """
        logging.info("Starting agent.")
        self.agent_is_running = True
        self.thread.start()        
        self.state_machine = StateMachine()
        self.state_machine.transition(InitState(self.state_machine, self.brain))
        self.state_machine.run()
        self.agent_is_running = False
        logging.info("Stopping agent. Waiting for watch thread to finish.")
        self.thread.join()
        logging.info("Stopped agent.")

    def __start_watching(self):
        logging.info("Starting zone watcher.")
        try:
            game_region = self.brain.get_value(DIBI_GAMEREGION)
            all_zones_empty = False
            while self.agent_is_running:
                if game_region.all_zones_empty():                
                    all_zones_empty = True
                    break
                time.sleep(5)
            if all_zones_empty:
                logging.warn("Opponent left. Stopping game.")
                self.state_machine.is_done = True
        except Exception as e:
            logging.exception("Unexpected error in watch thread.")
