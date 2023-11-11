from game_logic.game import Game
from game_logic.player import Player
from game_logic.leader import Leader
from game_logic.player_statistics import PlayerStatistics
from actuators.dibi_pose import DibiPose
from game_logic.follower import Follower
from utils.static_random_source import StaticRandomSource

def test_change_role_works():
    player = Player(StaticRandomSource(), Leader(), 0, PlayerStatistics(StaticRandomSource()))
    player.award_point()
    player.change_role(Follower())
    assert not player.is_leader()

def test_change_role_resets_points():
    player = Player(StaticRandomSource(), Leader(), 0, PlayerStatistics(StaticRandomSource()))
    player.award_point()
    player.change_role(Follower())
    assert player.points == 0
    assert player.total_points == 1

def test_award_point_works():
    player = Player(StaticRandomSource(), Leader(), 0, PlayerStatistics(StaticRandomSource()))
    player.award_point()
    assert player.points == 1
    assert player.total_points == 1

def test_has_won_works():
    player = Player(StaticRandomSource(), Leader(), 0, PlayerStatistics(StaticRandomSource()))
    assert player.has_won(DibiPose["ROCK"], DibiPose["ROCK"])
    assert not player.has_won(DibiPose["ROCK"], DibiPose["SCISSOR"])

def test_record_pose_works():    
    player = Player(StaticRandomSource(), Leader(), 0, PlayerStatistics(StaticRandomSource()))
    player.record_pose(DibiPose["ROCK"])
    assert player.statistics.get_poses_count(DibiPose["ROCK"]) == 1

def test_choose_winning_pose_works():    
    player = Player(StaticRandomSource(), Leader(), 0, PlayerStatistics(StaticRandomSource()))
    pose = player.choose_next_winning_pose(DibiPose["ROCK"])
    assert pose == DibiPose["ROCK"]

def test_choose_winning_pose_handles_unknown_pose():    
    player = Player(StaticRandomSource(), Leader(), 0, PlayerStatistics(StaticRandomSource()))
    pose = player.choose_next_winning_pose(DibiPose["UNKNOWN"])
    assert pose == DibiPose["PAPER"]

def test_choose_losing_pose_works():    
    player = Player(StaticRandomSource(), Leader(), 0, PlayerStatistics(StaticRandomSource()))
    pose = player.choose_next_losing_pose(DibiPose["ROCK"])
    assert pose != DibiPose["ROCK"] and pose != DibiPose["UNKNOWN"]

def test_choose_losing_pose_handles_unknown():    
    player = Player(StaticRandomSource(), Leader(), 0, PlayerStatistics(StaticRandomSource()))
    pose = player.choose_next_losing_pose(DibiPose["ROCK"])
    assert pose != DibiPose["UNKNOWN"]
