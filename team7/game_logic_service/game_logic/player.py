from actuators.dibi_pose import DibiPose
from game_logic.game_role_type import GameRoleType
from game_logic.motivation import Motivation
import logging
class Player():
    """Represents a player in the game (either the robot or a human player)
    """
    def __init__(self, random_source, role, total_points, statistics):
        self.random_source = random_source
        self.role = role
        self.total_points = total_points
        self.points = 0
        self.statistics = statistics
        self.motivation = Motivation()

    def change_role(self, new_role):
        """Changes the role.

        Args:
            new_role (GameRole): the new role
        """
        self.role = new_role
        self.points = 0

    def award_point(self):
        """Awards a point, e.g. the player won a round.
        """
        self.total_points += 1
        self.points += 1

    def has_won(self, my_pose, opponent_pose):
        """Checks whether the player has won based on the given poses.

        Args:
            my_pose (DibiPose: the player's pose
            opponent_pose (DibiPose): the opponent's pose

        Returns:
            bool: True, if the player won
        """
        return self.role.has_won(my_pose, opponent_pose)

    def is_leader(self):
        """Checks whether the player is leader.

        Returns:
            bool: True, if the player is the leader
        """
        return self.role.role_type == GameRoleType["LEADER"]

    def record_pose(self, pose):
        """Records the pose for statistics.

        Args:
            pose (DibiPose): the pose
        """
        self.statistics.record_pose(pose)

    def record_impression(self, mood, won_round):
        """Records the player's impression for calculating the motivation later.

        Args:
            mood (str): the mood of the player after evaluating the round
            won_round (bool): True, if the player won
        """
        self.motivation.record_impression(mood, won_round)

    def get_motivational_factor(self):
        """Get this player's motivation.

        Returns:
            float: the motivation
        """
        return self.motivation.calculate_motivational_factor()

    def predict_next_pose(self):
        """Predicts this player's next pose

        Returns:
            DibiPose: the predicted pose
        """
        pose = self.statistics.predict_next_pose()
        logging.info("Predicted pose {0}".format(pose))
        return pose

    def choose_next_winning_pose(self, predicted_opponent_pose):
        """Chooses a pose that let's this player win.

        Args:
            predicted_opponent_pose (DibiPose): the most likely pose of the opponent

        Returns:
            DibiPose: the winning pose
        """
        if predicted_opponent_pose == DibiPose["UNKNOWN"]:
            return DibiPose["PAPER"]
        winning_poses = self.role.get_winning_poses(predicted_opponent_pose)
        choice = self.random_source.randint(0, len(winning_poses) - 1)
        return winning_poses[choice]

    def choose_next_losing_pose(self, actual_opponent_pose):
        """Chooses a pose that will let the player lose.

        Args:
            actual_opponent_pose (DibiPose): the actual pose the opponent chose.

        Returns:
            DibiPose: the losing pose
        """
        if actual_opponent_pose == DibiPose["UNKNOWN"]:
            return self.random_source.randint(1, 3)
        winning_poses = self.role.get_winning_poses(actual_opponent_pose)
        losing_poses = [pose for pose in [1, 2, 3] if pose not in winning_poses]
        if len(losing_poses) == 0:
            return self.random_source.randint(1, 3)
        choice = self.random_source.randint(0, len(losing_poses) - 1)
        return losing_poses[choice]