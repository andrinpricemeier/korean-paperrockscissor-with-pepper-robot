from agent_logic.state_machine import StateMachine
from agent_logic.blackboard import Blackboard
from agent_logic.brain_constants import DIBI_ACTIVEGAME, DIBI_DIALOG, DIBI_SPEAKER
from game_logic.game import Game
from game_logic.player import Player
from game_logic.leader import Leader
from game_logic.player_statistics import PlayerStatistics
from game_logic.follower import Follower
from agent_logic.ask_role_state import AskRoleState
from agent_logic.fighting_state import FightingState
from utils.static_random_source import StaticRandomSource
from actuators.speaker import Speaker
from actuators.dialog import Dialog

class StubDialog(Dialog):
    def __init__(self, ask_return):
        self.ask_return = ask_return

    def ask(self, question_id, reaction_one_id, reaction_two_id):
        return self.ask_return

def test_asks_for_role(mocker):
    state_machine = StateMachine()
    robot_player = Player(StaticRandomSource(), Leader(), 0, PlayerStatistics(StaticRandomSource(), 0, 0, 0))
    opponent_player = Player(StaticRandomSource(), Follower(), 0, PlayerStatistics(StaticRandomSource(), 0, 0, 0))
    game = Game(StaticRandomSource(), robot_player, opponent_player, 3)
    brain = Blackboard()
    dialog = StubDialog(None)
    dialog_spy = mocker.spy(dialog, "ask")
    speaker = Speaker()
    speaker_spy = mocker.spy(speaker, "say")
    brain.set_value(DIBI_ACTIVEGAME, game)
    brain.set_value(DIBI_DIALOG, dialog)
    brain.set_value(DIBI_SPEAKER, speaker)
    state = AskRoleState(state_machine, brain)
    state.enter()
    dialog_spy.assert_called_with("ask_what_role_do_you_want_start_with","ask_what_role_do_you_want_start_with_leader", "ask_what_role_do_you_want_start_with_follower")

def test_no_role_chosen(mocker):
    state_machine = StateMachine()
    robot_player = Player(StaticRandomSource(), Leader(), 0, PlayerStatistics(StaticRandomSource(), 0, 0, 0))
    opponent_player = Player(StaticRandomSource(), Follower(), 0, PlayerStatistics(StaticRandomSource(), 0, 0, 0))
    game = Game(StaticRandomSource(), robot_player, opponent_player, 3)
    brain = Blackboard()
    dialog = StubDialog(None)
    dialog_spy = mocker.spy(dialog, "ask")
    speaker = Speaker()
    speaker_spy = mocker.spy(speaker, "say")
    brain.set_value(DIBI_ACTIVEGAME, game)
    brain.set_value(DIBI_DIALOG, dialog)
    brain.set_value(DIBI_SPEAKER, speaker)
    state = AskRoleState(state_machine, brain)
    state.enter()
    speaker_spy.assert_called_with("ask_what_role_do_you_want_start_with_not_understood")

def test_leader_chosen(mocker):
    state_machine = StateMachine()
    robot_player = Player(StaticRandomSource(), Leader(), 0, PlayerStatistics(StaticRandomSource(), 0, 0, 0))
    opponent_player = Player(StaticRandomSource(), Follower(), 0, PlayerStatistics(StaticRandomSource(), 0, 0, 0))
    game = Game(StaticRandomSource(), robot_player, opponent_player, 3)
    brain = Blackboard()
    dialog = StubDialog(0)
    dialog_spy = mocker.spy(dialog, "ask")
    speaker = Speaker()
    speaker_spy = mocker.spy(speaker, "say")
    brain.set_value(DIBI_ACTIVEGAME, game)
    brain.set_value(DIBI_DIALOG, dialog)
    brain.set_value(DIBI_SPEAKER, speaker)
    state = AskRoleState(state_machine, brain)
    state.enter()
    assert game.opponent_is_leader()

def test_follower_chosen(mocker):
    state_machine = StateMachine()
    robot_player = Player(StaticRandomSource(), Leader(), 0, PlayerStatistics(StaticRandomSource(), 0, 0, 0))
    opponent_player = Player(StaticRandomSource(), Follower(), 0, PlayerStatistics(StaticRandomSource(), 0, 0, 0))
    game = Game(StaticRandomSource(), robot_player, opponent_player, 3)
    brain = Blackboard()
    dialog = StubDialog(1)
    dialog_spy = mocker.spy(dialog, "ask")
    speaker = Speaker()
    speaker_spy = mocker.spy(speaker, "say")
    brain.set_value(DIBI_ACTIVEGAME, game)
    brain.set_value(DIBI_DIALOG, dialog)
    brain.set_value(DIBI_SPEAKER, speaker)
    state = AskRoleState(state_machine, brain)
    state.enter()
    assert not game.opponent_is_leader()

def test_transitions_to_fighting_state(mocker):
    state_machine = StateMachine()
    robot_player = Player(StaticRandomSource(), Leader(), 0, PlayerStatistics(StaticRandomSource(), 0, 0, 0))
    opponent_player = Player(StaticRandomSource(), Follower(), 0, PlayerStatistics(StaticRandomSource(), 0, 0, 0))
    game = Game(StaticRandomSource(), robot_player, opponent_player, 3)
    brain = Blackboard()
    dialog = StubDialog(1)
    dialog_spy = mocker.spy(dialog, "ask")
    speaker = Speaker()
    speaker_spy = mocker.spy(speaker, "say")
    brain.set_value(DIBI_ACTIVEGAME, game)
    brain.set_value(DIBI_DIALOG, dialog)
    brain.set_value(DIBI_SPEAKER, speaker)
    state = AskRoleState(state_machine, brain)
    state.enter()
    assert type(state_machine.current_state) is FightingState