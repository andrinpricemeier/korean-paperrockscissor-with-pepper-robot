from actuators.dibi_pose import DibiPose
from actuators.scissor_pose import ScissorPose
from actuators.rock_pose import RockPose
from actuators.paper_pose import PaperPose
from actuators.robot_body import RobotBody
import time
import logging

class DibiBody(RobotBody):
    def __init__(self, motion, posture):
        self.motion = motion
        self.posture = posture
        
    def assume_pose(self, pose_type):
        logging.info("Assuming pose " + str(pose_type))
        pose = self.__pose_type_to_pose(pose_type)
        if pose is not None:
            pose.assume(self.motion)
            time.sleep(1)
            self.posture.goToPosture("Stand", 0.5)

    def __pose_type_to_pose(self, pose_type):
        if pose_type == DibiPose["PAPER"]:
            return PaperPose()
        elif pose_type == DibiPose["ROCK"]:
            return RockPose()
        elif pose_type == DibiPose["SCISSOR"]:
            return ScissorPose()
        return None
