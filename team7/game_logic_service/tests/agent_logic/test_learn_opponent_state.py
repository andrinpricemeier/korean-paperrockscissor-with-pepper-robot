from agent_logic.state_machine import StateMachine
from agent_logic.blackboard import Blackboard
from agent_logic.brain_constants import DIBI_SPEAKER
from actuators.speaker import Speaker
from agent_logic.brain_constants import DIBI_OPPONENTNAME
from agent_logic.learn_opponent_state import LearnOpponentState
from actuators.name_reaction import NameReaction
from agent_logic.brain_constants import DIBI_CORPUS, DIBI_DIALOG, DIBI_NAMEREACTION
from actuators.dialog import Dialog
from actuators.corpus import Corpus
from agent_logic.ask_role_state import AskRoleState
from agent_logic.brain_constants import DIBI_GAMEREGION
from agent_logic.brain_constants import DIBI_FACEDETECTOR
from sensors.face_detector import FaceDetector
from utils.static_random_source import StaticRandomSource
from actuators.dictionary import dictionary
from sensors.game_region import GameRegion

class StubDialog(Dialog):
    def __init__(self, *ask_return):
        self.ask_return = ask_return
        self.current_index = 0

    def ask_with_text(self, question_text, reaction_one_text, reaction_two_text):
        if self.current_index >= len(self.ask_return):
            self.current_index -= 1
        answer = self.ask_return[self.current_index]
        self.current_index += 1
        return answer

    def ask(self, question_id, reaction_one_id, reaction_two_id):
        if self.current_index >= len(self.ask_return):
            self.current_index -= 1
        answer = self.ask_return[self.current_index]
        self.current_index += 1
        return answer

def test_knows_opponent_transitions_to_next_state(mocker):
    state_machine = StateMachine()
    brain = Blackboard()
    speaker = Speaker()
    speaker_spy = mocker.spy(speaker, "say")
    brain.set_value(DIBI_SPEAKER, speaker)
    brain.set_value(DIBI_OPPONENTNAME, "anything")
    brain.set_value(DIBI_DIALOG, Dialog())
    brain.set_value(DIBI_CORPUS, Corpus(dictionary, StaticRandomSource()))
    brain.set_value(DIBI_NAMEREACTION, NameReaction(speaker))
    state = LearnOpponentState(state_machine, brain)
    state.enter()
    assert type(state_machine.current_state) is AskRoleState

def test_asks_for_name(mocker):
    state_machine = StateMachine()
    brain = Blackboard()
    dialog = StubDialog(0)
    dialog_spy = mocker.spy(dialog, "ask")
    speaker = Speaker()
    speaker_spy = mocker.spy(speaker, "say_with_args")
    brain.set_value(DIBI_SPEAKER, speaker)
    brain.set_value(DIBI_OPPONENTNAME, None)
    brain.set_value(DIBI_DIALOG, dialog)
    brain.set_value(DIBI_CORPUS, Corpus(dictionary, StaticRandomSource()))
    brain.set_value(DIBI_NAMEREACTION, NameReaction(speaker))
    brain.set_value(DIBI_GAMEREGION, GameRegion())
    brain.set_value(DIBI_FACEDETECTOR, FaceDetector())
    state = LearnOpponentState(state_machine, brain)
    state.enter()
    dialog_spy.assert_any_call("ask_if_opponent_wants_name", "ask_if_opponent_wants_name_yes", "ask_if_opponent_wants_name_no")

def test_doesnt_want_name_changes_state(mocker):
    state_machine = StateMachine()
    brain = Blackboard()
    dialog = StubDialog(1)
    dialog_spy = mocker.spy(dialog, "ask")
    speaker = Speaker()
    speaker_spy = mocker.spy(speaker, "say_with_args")
    brain.set_value(DIBI_SPEAKER, speaker)
    brain.set_value(DIBI_OPPONENTNAME, None)
    brain.set_value(DIBI_DIALOG, dialog)
    brain.set_value(DIBI_CORPUS, Corpus(dictionary, StaticRandomSource()))
    brain.set_value(DIBI_NAMEREACTION, NameReaction(speaker))
    brain.set_value(DIBI_GAMEREGION, GameRegion())
    brain.set_value(DIBI_FACEDETECTOR, FaceDetector())
    state = LearnOpponentState(state_machine, brain)
    state.enter()
    assert type(state_machine.current_state) is AskRoleState

def test_doesnt_like_name_changes_state(mocker):
    state_machine = StateMachine()
    brain = Blackboard()
    dialog = StubDialog(0, 1)
    dialog_spy = mocker.spy(dialog, "ask")
    speaker = Speaker()
    speaker_spy = mocker.spy(speaker, "say_with_args")
    brain.set_value(DIBI_SPEAKER, speaker)
    brain.set_value(DIBI_OPPONENTNAME, None)
    brain.set_value(DIBI_DIALOG, dialog)
    brain.set_value(DIBI_CORPUS, Corpus(dictionary, StaticRandomSource()))
    brain.set_value(DIBI_NAMEREACTION, NameReaction(speaker))
    brain.set_value(DIBI_GAMEREGION, GameRegion())
    brain.set_value(DIBI_FACEDETECTOR, FaceDetector())
    state = LearnOpponentState(state_machine, brain)
    state.enter()
    assert type(state_machine.current_state) is AskRoleState

def test_likes_name_reacts(mocker):
    state_machine = StateMachine()
    brain = Blackboard()
    dialog = StubDialog(0, 0)
    dialog_spy = mocker.spy(dialog, "ask")
    speaker = Speaker()
    corpus = Corpus(dictionary, StaticRandomSource())
    name = corpus.lookup("opponent_names")
    reaction = NameReaction(speaker)
    reaction.add(name, "opponent_names")
    reaction_spy = mocker.spy(reaction, "react")
    speaker_spy = mocker.spy(speaker, "say_with_args")
    brain.set_value(DIBI_SPEAKER, speaker)
    brain.set_value(DIBI_OPPONENTNAME, None)
    brain.set_value(DIBI_DIALOG, dialog)
    brain.set_value(DIBI_CORPUS, corpus)
    brain.set_value(DIBI_NAMEREACTION, reaction)
    brain.set_value(DIBI_GAMEREGION, GameRegion())
    brain.set_value(DIBI_FACEDETECTOR, FaceDetector())
    state = LearnOpponentState(state_machine, brain)
    state.enter()
    reaction_spy.assert_called_with(name)

def test_likes_name_saves_name(mocker):
    state_machine = StateMachine()
    brain = Blackboard()
    dialog = StubDialog(0, 0)
    dialog_spy = mocker.spy(dialog, "ask")
    speaker = Speaker()
    corpus = Corpus(dictionary, StaticRandomSource())
    name = corpus.lookup("opponent_names")
    reaction = NameReaction(speaker)
    reaction.add(name, "opponent_names")
    reaction_spy = mocker.spy(reaction, "react")
    speaker_spy = mocker.spy(speaker, "say_with_args")
    brain.set_value(DIBI_SPEAKER, speaker)
    brain.set_value(DIBI_OPPONENTNAME, None)
    brain.set_value(DIBI_DIALOG, dialog)
    brain.set_value(DIBI_CORPUS, corpus)
    brain.set_value(DIBI_NAMEREACTION, reaction)
    brain.set_value(DIBI_GAMEREGION, GameRegion())
    brain.set_value(DIBI_FACEDETECTOR, FaceDetector())
    state = LearnOpponentState(state_machine, brain)
    state.enter()
    assert brain.get_value(DIBI_OPPONENTNAME) == name

def test_learns_face_ensures_distance(mocker):
    state_machine = StateMachine()
    brain = Blackboard()
    dialog = StubDialog(0, 0)
    dialog_spy = mocker.spy(dialog, "ask")
    speaker = Speaker()
    corpus = Corpus(dictionary, StaticRandomSource())
    name = corpus.lookup("opponent_names")
    reaction = NameReaction(speaker)
    reaction.add(name, "opponent_names")
    reaction_spy = mocker.spy(reaction, "react")
    speaker_spy = mocker.spy(speaker, "say_with_args")
    game_region = GameRegion()
    game_region_spy = mocker.spy(game_region, "ensure_is_in_zone")
    brain.set_value(DIBI_SPEAKER, speaker)
    brain.set_value(DIBI_OPPONENTNAME, None)
    brain.set_value(DIBI_DIALOG, dialog)
    brain.set_value(DIBI_CORPUS, corpus)
    brain.set_value(DIBI_NAMEREACTION, reaction)
    brain.set_value(DIBI_GAMEREGION, game_region)
    brain.set_value(DIBI_FACEDETECTOR, FaceDetector())
    state = LearnOpponentState(state_machine, brain)
    state.enter()
    game_region_spy.assert_called_with(1)
    
def test_learns_face(mocker):
    state_machine = StateMachine()
    brain = Blackboard()
    dialog = StubDialog(0, 0)
    dialog_spy = mocker.spy(dialog, "ask")
    speaker = Speaker()
    corpus = Corpus(dictionary, StaticRandomSource())
    name = corpus.lookup("opponent_names")
    reaction = NameReaction(speaker)
    reaction.add(name, "opponent_names")
    reaction_spy = mocker.spy(reaction, "react")
    speaker_spy = mocker.spy(speaker, "say_with_args")
    game_region = GameRegion()
    game_region_spy = mocker.spy(game_region, "ensure_is_in_zone")
    face_detector = FaceDetector()
    face_detector_spy = mocker.spy(face_detector, "learn_face")
    brain.set_value(DIBI_SPEAKER, speaker)
    brain.set_value(DIBI_OPPONENTNAME, None)
    brain.set_value(DIBI_DIALOG, dialog)
    brain.set_value(DIBI_CORPUS, corpus)
    brain.set_value(DIBI_NAMEREACTION, reaction)
    brain.set_value(DIBI_GAMEREGION, game_region)
    brain.set_value(DIBI_FACEDETECTOR, face_detector)
    state = LearnOpponentState(state_machine, brain)
    state.enter()
    face_detector_spy.assert_called()