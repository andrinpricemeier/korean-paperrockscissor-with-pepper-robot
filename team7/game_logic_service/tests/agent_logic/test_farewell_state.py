from agent_logic.state_machine import StateMachine
from agent_logic.blackboard import Blackboard
from agent_logic.brain_constants import DIBI_SPEAKER
from actuators.speaker import Speaker
from agent_logic.farewell_state import FarewellState
from agent_logic.brain_constants import DIBI_OPPONENTNAME

def test_wishes_farewell_without_name(mocker):
    state_machine = StateMachine()
    brain = Blackboard()
    speaker = Speaker()
    speaker_spy = mocker.spy(speaker, "say")
    brain.set_value(DIBI_SPEAKER, speaker)
    brain.set_value(DIBI_OPPONENTNAME, None)
    state = FarewellState(state_machine, brain)
    state.enter()
    speaker_spy.assert_called_with("farewell")

def test_wishes_farewell_with_name(mocker):
    state_machine = StateMachine()
    brain = Blackboard()
    speaker = Speaker()
    speaker_spy = mocker.spy(speaker, "say_with_args")
    brain.set_value(DIBI_SPEAKER, speaker)
    brain.set_value(DIBI_OPPONENTNAME, "any name")
    state = FarewellState(state_machine, brain)
    state.enter()
    speaker_spy.assert_called_with("farewell_with_name", "any name")

def test_concludes_game(mocker):
    state_machine = StateMachine()
    brain = Blackboard()
    speaker = Speaker()
    speaker_spy = mocker.spy(speaker, "say")
    brain.set_value(DIBI_SPEAKER, speaker)
    state = FarewellState(state_machine, brain)
    state.enter()
    assert state_machine.current_state is None