from agent_logic.state_machine import StateMachine
from agent_logic.blackboard import Blackboard
from agent_logic.brain_constants import DIBI_DIALOG, DIBI_SPEAKER
from agent_logic.explanation_state import ExplanationState
from actuators.speaker import Speaker
from actuators.dialog import Dialog
from agent_logic.learn_opponent_state import LearnOpponentState
from actuators.robot_body import RobotBody
from agent_logic.brain_constants import DIBI_BODY
from actuators.dibi_pose import DibiPose

class StubDialog(Dialog):
    def __init__(self, ask_return):
        self.ask_return = ask_return

    def ask(self, question_id, reaction_one_id, reaction_two_id):
        return self.ask_return

def test_asks_explanation(mocker):
    state_machine = StateMachine()
    brain = Blackboard()
    dialog = StubDialog(None)
    dialog_spy = mocker.spy(dialog, "ask")
    speaker = Speaker()
    speaker_spy = mocker.spy(speaker, "say")
    brain.set_value(DIBI_DIALOG, dialog)
    brain.set_value(DIBI_SPEAKER, speaker)
    state = ExplanationState(state_machine, brain)
    state.enter()   
    dialog_spy.assert_called_with("ask_explanation_required","ask_explanation_accepted_reaction", "ask_explanation_declined_reaction")

def test_doesnt_want_explanation_transitions_to_next_state(mocker):
    state_machine = StateMachine()
    brain = Blackboard()
    dialog = StubDialog(1)
    dialog_spy = mocker.spy(dialog, "ask")
    speaker = Speaker()
    speaker_spy = mocker.spy(speaker, "say")
    brain.set_value(DIBI_DIALOG, dialog)
    brain.set_value(DIBI_SPEAKER, speaker)
    brain.set_value(DIBI_BODY, RobotBody())
    state = ExplanationState(state_machine, brain)
    state.enter()
    assert type(state_machine.current_state) is LearnOpponentState

def test_explains(mocker):
    state_machine = StateMachine()
    brain = Blackboard()
    dialog = StubDialog(0)
    dialog_spy = mocker.spy(dialog, "ask")
    speaker = Speaker()
    speaker_spy = mocker.spy(speaker, "say")
    body = RobotBody()
    body_spy = mocker.spy(body, "assume_pose")
    brain.set_value(DIBI_DIALOG, dialog)
    brain.set_value(DIBI_SPEAKER, speaker)
    brain.set_value(DIBI_BODY, body)
    state = ExplanationState(state_machine, brain)
    state.enter()
    speaker_spy.assert_has_calls([mocker.call("explanation_introduction"), mocker.call("explanation_basics"), mocker.call("explanation_roles"), mocker.call("explanation_pose_scissor"), mocker.call("explanation_pose_paper"), mocker.call("explanation_pose_rock")])
    body_spy.assert_has_calls([mocker.call(DibiPose["SCISSOR"]), mocker.call(DibiPose["PAPER"]), mocker.call(DibiPose["ROCK"])])