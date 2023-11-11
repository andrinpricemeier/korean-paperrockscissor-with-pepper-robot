import logging

DibiPose = {
    "UNKNOWN": 0,
    "PAPER": 1,
    "ROCK": 2,
    "SCISSOR": 3
}

def get_pose_name_by_index(opponent_pose):
    for name, pose in DibiPose.items():
        if pose == opponent_pose:
            logging.info("Mapped {0} to {1}".format(opponent_pose, name))
            return name