from agent_logic.state_machine import StateMachine
from agent_logic.blackboard import Blackboard
from agent_logic.brain_constants import DIBI_SPEAKER
from agent_logic.init_state import InitState
from actuators.speaker import Speaker
from agent_logic.explanation_state import ExplanationState

def test_welcomes_opponent(mocker):
    state_machine = StateMachine()
    brain = Blackboard()
    speaker = Speaker()
    speaker_spy = mocker.spy(speaker, "say")
    brain.set_value(DIBI_SPEAKER, speaker)
    state = InitState(state_machine, brain)
    state.enter()
    speaker_spy.assert_called_with("welcome_to_game")

def test_changes_state_correctly(mocker):
    state_machine = StateMachine()
    brain = Blackboard()
    speaker = Speaker()
    speaker_spy = mocker.spy(speaker, "say")
    brain.set_value(DIBI_SPEAKER, speaker)
    state = InitState(state_machine, brain)
    state.enter()
    assert type(state_machine.current_state) is ExplanationState