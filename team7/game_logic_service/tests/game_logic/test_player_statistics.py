from game_logic.player_statistics import PlayerStatistics
from actuators.dibi_pose import DibiPose
from utils.static_random_source import StaticRandomSource

def test_record_works():
    statistics = PlayerStatistics(StaticRandomSource())
    statistics.record_pose(DibiPose["ROCK"])
    statistics.record_pose(DibiPose["ROCK"])
    statistics.record_pose(DibiPose["ROCK"])
    statistics.record_pose(DibiPose["SCISSOR"])
    statistics.record_pose(DibiPose["PAPER"])
    statistics.record_pose(DibiPose["PAPER"])
    assert statistics.get_poses_count(DibiPose["ROCK"]) == 3
    assert statistics.get_poses_count(DibiPose["SCISSOR"]) == 1
    assert statistics.get_poses_count(DibiPose["PAPER"]) == 2

def test_predict_next_pose():
    statistics = PlayerStatistics(StaticRandomSource())
    assert statistics.predict_next_pose() == DibiPose["PAPER"]