from game_logic.game_role import GameRole
from actuators.dibi_pose import DibiPose
from game_logic.game_role_type import GameRoleType

class Leader(GameRole):
    """The leader role.
    """
    def __init__(self):
        self.role_type = GameRoleType["LEADER"]

    def has_won(self, my_pose, opponent_pose):
        return my_pose == opponent_pose

    def get_winning_poses(self, predicted_opponent_pose):
        return [predicted_opponent_pose]