from agent_logic.state_machine import StateMachine
from agent_logic.blackboard import Blackboard
from agent_logic.brain_constants import DIBI_SPEAKER
from agent_logic.init_state import InitState
from actuators.speaker import Speaker
from agent_logic.explanation_state import ExplanationState
from game_logic.game import Game
from game_logic.player import Player
from game_logic.leader import Leader
from game_logic.player_statistics import PlayerStatistics
from actuators.dibi_pose import DibiPose
from game_logic.follower import Follower
from agent_logic.fighting_state import FightingState
from agent_logic.brain_constants import DIBI_ACTIVEGAME
from agent_logic.brain_constants import DIBI_GAMEREGION
from agent_logic.brain_constants import DIBI_ASYNCSERVICE
from agent_logic.brain_constants import DIBI_BODY
from agent_logic.brain_constants import DIBI_POSEESTIMATION
from agent_logic.brain_constants import DIBI_CAMERA
from agent_logic.brain_constants import DIBI_DIALOG
from agent_logic.brain_constants import DIBI_OPPONENTNAME
from agent_logic.brain_constants import DIBI_MOODDETECTOR
from agent_logic.brain_constants import DIBI_LED
from sensors.mood_detector import MoodDetector
from sensors.pose_estimation import PoseEstimation
from utils.static_random_source import StaticRandomSource
from sensors.game_region import GameRegion
from utils.async_service import AsyncService
from actuators.robot_body import RobotBody
from sensors.camera import Camera
from actuators.dialog import Dialog
from actuators.robot_led import RobotLED

class PseudoFuture():
    def wait(self):
        pass

    def value(self):
        return DibiPose["ROCK"]

class PseudoAsyncService(AsyncService):    
    def future(self, action, *args):
        return PseudoFuture()

def create_game_entities():
    robot_player = Player(StaticRandomSource(), Leader(), 0, PlayerStatistics(StaticRandomSource(), 0, 0, 0))
    opponent_player = Player(StaticRandomSource(), Follower(), 0, PlayerStatistics(StaticRandomSource(), 0, 0, 0))
    game = Game(StaticRandomSource(), robot_player, opponent_player, 3)
    return (game, robot_player, opponent_player)

def test_welcomes_opponent(mocker):
    state_machine = StateMachine()
    brain = Blackboard()
    speaker = Speaker()
    speaker_spy = mocker.spy(speaker, "say")
    brain.set_value(DIBI_SPEAKER, speaker)
    (game, robot_player, opponent_player) = create_game_entities()
    brain.set_value(DIBI_ACTIVEGAME, game)
    brain.set_value(DIBI_GAMEREGION, GameRegion())
    brain.set_value(DIBI_ASYNCSERVICE, PseudoAsyncService())
    brain.set_value(DIBI_BODY, RobotBody())
    brain.set_value(DIBI_POSEESTIMATION, PoseEstimation())
    brain.set_value(DIBI_CAMERA, Camera())
    brain.set_value(DIBI_DIALOG, Dialog())
    brain.set_value(DIBI_MOODDETECTOR, MoodDetector())
    brain.set_value(DIBI_LED, RobotLED())
    state = FightingState(state_machine, brain)
    state.enter()
    speaker_spy.assert_any_call("start_game")
    
def test_welcomes_opponent_with_name(mocker):
    state_machine = StateMachine()
    brain = Blackboard()
    speaker = Speaker()
    speaker_spy = mocker.spy(speaker, "say_with_args")
    brain.set_value(DIBI_SPEAKER, speaker)
    (game, robot_player, opponent_player) = create_game_entities()
    brain.set_value(DIBI_ACTIVEGAME, game)
    brain.set_value(DIBI_GAMEREGION, GameRegion())
    brain.set_value(DIBI_ASYNCSERVICE, PseudoAsyncService())
    brain.set_value(DIBI_BODY, RobotBody())
    brain.set_value(DIBI_POSEESTIMATION, PoseEstimation())
    brain.set_value(DIBI_CAMERA, Camera())
    brain.set_value(DIBI_DIALOG, Dialog())
    brain.set_value(DIBI_OPPONENTNAME, "anything")
    brain.set_value(DIBI_MOODDETECTOR, MoodDetector())
    brain.set_value(DIBI_LED, RobotLED())
    state = FightingState(state_machine, brain)
    state.enter()
    speaker_spy.assert_any_call("start_game_with_name", "anything")
    
def test_informs_about_role(mocker):
    state_machine = StateMachine()
    brain = Blackboard()
    speaker = Speaker()
    speaker_spy = mocker.spy(speaker, "say")
    brain.set_value(DIBI_SPEAKER, speaker)
    (game, robot_player, opponent_player) = create_game_entities()
    brain.set_value(DIBI_ACTIVEGAME, game)
    brain.set_value(DIBI_GAMEREGION, GameRegion())
    brain.set_value(DIBI_ASYNCSERVICE, PseudoAsyncService())
    brain.set_value(DIBI_BODY, RobotBody())
    brain.set_value(DIBI_POSEESTIMATION, PoseEstimation())
    brain.set_value(DIBI_CAMERA, Camera())
    brain.set_value(DIBI_DIALOG, Dialog())
    brain.set_value(DIBI_OPPONENTNAME, None)
    brain.set_value(DIBI_MOODDETECTOR, MoodDetector())
    brain.set_value(DIBI_LED, RobotLED())
    state = FightingState(state_machine, brain)
    state.enter()
    speaker_spy.assert_any_call("opponent_is_follower")
    
def test_ensures_distance(mocker):
    state_machine = StateMachine()
    brain = Blackboard()
    speaker = Speaker()
    speaker_spy = mocker.spy(speaker, "say")
    brain.set_value(DIBI_SPEAKER, speaker)
    (game, robot_player, opponent_player) = create_game_entities()
    game_region = GameRegion()
    game_region_spy = mocker.spy(game_region, "ensure_is_in_zone")
    brain.set_value(DIBI_ACTIVEGAME, game)
    brain.set_value(DIBI_GAMEREGION, game_region)
    brain.set_value(DIBI_ASYNCSERVICE, PseudoAsyncService())
    brain.set_value(DIBI_BODY, RobotBody())
    brain.set_value(DIBI_POSEESTIMATION, PoseEstimation())
    brain.set_value(DIBI_CAMERA, Camera())
    brain.set_value(DIBI_DIALOG, Dialog())
    brain.set_value(DIBI_OPPONENTNAME, None)
    brain.set_value(DIBI_MOODDETECTOR, MoodDetector())
    brain.set_value(DIBI_LED, RobotLED())
    state = FightingState(state_machine, brain)
    state.enter()
    game_region_spy.assert_called_with(2)