from game_logic.leader import Leader
from game_logic.follower import Follower
from actuators.dibi_pose import DibiPose
import logging

class Game():
    """Encapsulates the logic for the dibi game.
    """
    def __init__(self, random_source, robot_player, opponent_player, switch_after_points):
        self.random_source = random_source
        self.robot_player = robot_player
        self.opponent_player = opponent_player
        self.robot_won_last = False
        self.roles_switched_last = False
        self.rounds = 0
        self.switch_after_points = switch_after_points

    def evaluate_round(self, robot_pose, opponent_pose):
        """Evaluates, i.e. considers the effects of the poses chosen by the robot and opponent.

        Args:
            robot_pose (DibiPose): the robot's pose
            opponent_pose (DibiPose): the opponent's pose
        """
        self.robot_won_last = False
        self.roles_switched_last = False
        if opponent_pose == DibiPose["UNKNOWN"]:
            logging.info("Detected pose failed. Awarding point to opponent.")
            self.opponent_player.award_point()
            self.robot_won_last = False
        elif self.robot_player.has_won(robot_pose, opponent_pose):
            logging.info("Robot has won.")
            self.robot_player.award_point()
            self.robot_won_last = True
            self.robot_player.record_pose(robot_pose)
            self.opponent_player.record_pose(opponent_pose)
        else:
            logging.info("Opponent has won.")
            self.opponent_player.award_point()
            self.robot_won_last = False
            self.robot_player.record_pose(robot_pose)
            self.opponent_player.record_pose(opponent_pose)
        if self.robot_player.points == self.switch_after_points or self.opponent_player.points == self.switch_after_points:
            logging.info("Role switch necessary.")
            self.roles_switched_last = True
            self.__switch_roles()
        self.rounds += 1

    def record_opponent_mood(self, mood):
        """Records the opponent's mood for further analysis by the motivation submodule.

        Args:
            mood (str): one of: positive, neutral, negative or unknown.
        """
        self.opponent_player.record_impression(mood, not self.robot_won_last)

    def opponent_is_leader(self):
        """Checks whether the opponent is the leader.

        Returns:
            bool: True, if the opponent is the leader. 
        """
        return self.opponent_player.is_leader()

    def did_opponent_win_last_round(self):
        """Checks whether the opponent has won the last round.
        Can be used by the robot to react after a round.

        Returns:
            bool: True, if the opponent won last round.
        """
        return not self.robot_won_last

    def did_role_switch_occur_last_round(self):
        """Checks whether a role switch occurred.
        Can be used by the robot to notify the human of a role switch.

        Returns:
            bool: True, if a role switch occurred.
        """
        return self.roles_switched_last

    def should_robot_lose_on_purpose(self):
        """Determines whether the opponent's motivation is so low that
        the robot should lose on purpose.

        Returns:
            bool: True, if the robot should lose on purpose.
        """
        motivation = self.opponent_player.get_motivational_factor()
        logging.info("Calculated motivational factor of " + str(motivation))
        return motivation < 0.5

    def pick_winning_robot_pose(self):
        """Tries to pick a pose for the robot so that the robot wins.
        Uses the opponent's statistics for prediction.

        Returns:
            DibiPose: the potential winning pose
        """
        return self.robot_player.choose_next_winning_pose(self.opponent_player.predict_next_pose())

    def pick_losing_robot_pose(self, actual_opponent_pose):
        """Picks a pose for the robot that is guaranteed to give the opponent a win.

        Args:
            actual_opponent_pose (DibiPose): the actual pose the opponent picked.

        Returns:
            DibiPose: the pose
        """
        return self.robot_player.choose_next_losing_pose(actual_opponent_pose)

    def set_roles(self, robot_role, opponent_role):
        """Sets the roles for the players.

        Args:
            robot_role (GameRole): the robot's role
            opponent_role (GameRole): the opponent's role
        """
        self.robot_player.change_role(robot_role)
        self.opponent_player.change_role(opponent_role)

    def __switch_roles(self):
        if self.robot_player.is_leader():
            self.robot_player.change_role(Follower())
            self.opponent_player.change_role(Leader())
        else:
            self.robot_player.change_role(Leader())
            self.opponent_player.change_role(Follower())
