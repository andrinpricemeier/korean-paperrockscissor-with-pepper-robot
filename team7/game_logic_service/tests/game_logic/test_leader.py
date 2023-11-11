import os
import sys
import inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from actuators.dibi_pose import DibiPose
from game_logic.leader import Leader


def test_leader_won_returns_true():
    leader = Leader()
    assert leader.has_won(DibiPose["ROCK"], DibiPose["ROCK"])

def test_leader_lost_returns_false():
    leader = Leader()
    assert not leader.has_won(DibiPose["ROCK"], DibiPose["SCISSOR"])

def test_winning_poses_correctly():
    leader = Leader()
    rock_winners = leader.get_winning_poses(DibiPose["ROCK"])
    scissor_winners = leader.get_winning_poses(DibiPose["SCISSOR"])
    paper_winners = leader.get_winning_poses(DibiPose["PAPER"])
    assert rock_winners[0] == DibiPose["ROCK"]
    assert scissor_winners[0] == DibiPose["SCISSOR"]
    assert paper_winners[0] == DibiPose["PAPER"]
