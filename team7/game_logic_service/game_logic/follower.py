from game_logic.game_role import GameRole
from actuators.dibi_pose import DibiPose
from game_logic.game_role_type import GameRoleType


class Follower(GameRole):
    """Represents a follower.
    """
    def __init__(self):
        self.role_type = GameRoleType["FOLLOWER"]

    def has_won(self, my_pose, opponent_pose):
        # The follower has won if he makes a different pose than the opponent.
        return my_pose != opponent_pose

    def get_winning_poses(self, predicted_opponent_pose):
        poses = []
        for pose in list(DibiPose.values()):
            if pose > 0 and pose != predicted_opponent_pose:
                poses.append(pose)
        return poses
