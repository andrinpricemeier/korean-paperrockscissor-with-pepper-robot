from game_logic.game import Game
from game_logic.player import Player
from game_logic.leader import Leader
from game_logic.player_statistics import PlayerStatistics
from actuators.dibi_pose import DibiPose
from game_logic.follower import Follower
from utils.static_random_source import StaticRandomSource

def create_test_entities():
    robot_player = Player(StaticRandomSource(), Leader(), 0, PlayerStatistics(StaticRandomSource(), 0, 0, 0))
    opponent_player = Player(StaticRandomSource(), Follower(), 0, PlayerStatistics(StaticRandomSource(), 0, 0, 0))
    game = Game(StaticRandomSource(), robot_player, opponent_player, 3)
    return (game, robot_player, opponent_player)

def test_won_last_true_if_robot_wins():
    (game, robot_player, opponent_player) = create_test_entities()
    game.evaluate_round(DibiPose["ROCK"], DibiPose["ROCK"])
    assert game.robot_won_last

def test_won_last_false_if_opponent_wins():
    (game, robot_player, opponent_player) = create_test_entities()
    game.evaluate_round(DibiPose["ROCK"], DibiPose["SCISSOR"])
    assert not game.robot_won_last

def test_awards_point_correctly_if_robot_wins():
    (game, robot_player, opponent_player) = create_test_entities()
    game.evaluate_round(DibiPose["ROCK"], DibiPose["ROCK"])
    assert robot_player.total_points == 1
    assert opponent_player.total_points == 0

def test_awards_point_correctly_if_opponent_wins():
    (game, robot_player, opponent_player) = create_test_entities()
    game.evaluate_round(DibiPose["ROCK"], DibiPose["SCISSOR"])
    assert robot_player.total_points == 0
    assert opponent_player.total_points == 1

def test_role_switch():
    (game, robot_player, opponent_player) = create_test_entities()
    game.evaluate_round(DibiPose["ROCK"], DibiPose["ROCK"])
    game.evaluate_round(DibiPose["ROCK"], DibiPose["ROCK"])
    game.evaluate_round(DibiPose["ROCK"], DibiPose["ROCK"])
    assert game.roles_switched_last
    assert not robot_player.is_leader()
    assert opponent_player.is_leader()

def test_unknown_pose_awards_opponent_point():
    (game, robot_player, opponent_player) = create_test_entities()
    game.evaluate_round(DibiPose["ROCK"], DibiPose["UNKNOWN"])
    assert opponent_player.total_points == 1
    assert not game.robot_won_last

def test_opponent_is_leader():
    (game, robot_player, opponent_player) = create_test_entities()
    assert not game.opponent_is_leader()

def test_pick_winning_robot_pose():
    (game, robot_player, opponent_player) = create_test_entities()
    pose = game.pick_winning_robot_pose()
    assert pose == DibiPose["PAPER"]

def test_pick_losing_robot_pose():
    (game, robot_player, opponent_player) = create_test_entities()
    pose = game.pick_losing_robot_pose(DibiPose["PAPER"])
    assert pose == DibiPose["ROCK"]

def test_set_roles():
    (game, robot_player, opponent_player) = create_test_entities()
    game.set_roles(Follower(), Leader())
    assert game.opponent_is_leader()