import os
import sys
import inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
parent_parent_dir = os.path.dirname(parent_dir)
sys.path.insert(0, parent_parent_dir)

from actuators.dibi_pose import DibiPose
from game_logic.follower import Follower

def test_follower_won_returns_true():
    follower = Follower()
    assert follower.has_won(DibiPose["ROCK"], DibiPose["SCISSOR"])

def test_follower_lost_returns_false():
    follower = Follower()
    assert not follower.has_won(DibiPose["ROCK"], DibiPose["ROCK"])

def test_winning_poses_correctly():
    follower = Follower()
    rock_winners = follower.get_winning_poses(DibiPose["ROCK"])
    scissor_winners = follower.get_winning_poses(DibiPose["SCISSOR"])
    paper_winners = follower.get_winning_poses(DibiPose["PAPER"])
    assert rock_winners[0] == DibiPose["PAPER"] and rock_winners[1] == DibiPose["SCISSOR"]
    assert scissor_winners[0] == DibiPose["PAPER"] and scissor_winners[1] == DibiPose["ROCK"]
    assert paper_winners[0] == DibiPose["ROCK"] and paper_winners[1] == DibiPose["SCISSOR"]
