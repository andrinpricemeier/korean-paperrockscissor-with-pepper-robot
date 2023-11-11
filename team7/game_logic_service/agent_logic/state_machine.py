import logging

class StateMachine:
    """Represents the logic for running a state machine.
    """
    def __init__(self):
        self.current_state = None
        self.is_done = False

    def transition(self, state):
        self.current_state = state

    def run(self):
        try:
            while self.current_state is not None:
                state = self.current_state
                state.enter()
            logging.info("Stopping.")
        except KeyboardInterrupt:
            logging.warn("State machine was interrupted.")
        except Exception:
            logging.exception("Unexpected eception.")

