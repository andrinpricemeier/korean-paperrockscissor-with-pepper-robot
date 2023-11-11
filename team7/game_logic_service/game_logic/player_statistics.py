from actuators.dibi_pose import DibiPose


class PlayerStatistics():
    """Represents the statistics of how the player plays the game.
    The basic idea is that if the player chooses e.g. rock a lot, he will most likely choose rock
    a lot in the future as well.
    """
    def __init__(self, random_source, rock_count=0, paper_count=0, scissor_count=0):
        self.random_source = random_source
        self.statistics = {}
        self.statistics[DibiPose['PAPER']] = paper_count
        self.statistics[DibiPose['ROCK']] = rock_count
        self.statistics[DibiPose['SCISSOR']] = scissor_count

    def record_pose(self, pose):
        """Records the pose.

        Args:
            pose (DibiPose): the pose the player chose.
        """
        if pose == DibiPose["UNKNOWN"] or pose is None:
            return
        self.statistics[pose] = self.statistics[pose] + 1

    def get_poses_count(self, pose):
        """Get how many times the player chose the pose.

        Args:
            pose (DibiPose): the pose

        Returns:
            int: the amount of times the player has picked this pose
        """
        return self.statistics[pose]

    def predict_next_pose(self):
        """Picks the most likely next pose based on a weighted choice.
        The weights are the number of times each pose has been picked in the past.

        Returns:
            DibiPose: the most likely pose
        """
        choices = []
        for key in self.statistics:
            choices.append((key, self.statistics[key]))
        return self.random_source.weighted_choice(choices)
