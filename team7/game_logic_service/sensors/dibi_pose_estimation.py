from sensors.pose_estimation import PoseEstimation

class DibiPoseEstimation(PoseEstimation):
    """Wrapper around the pose estimation API.
    """
    def __init__(self, api):
        self.api = api

    def estimate(self, image):
        """Estimate the pose based on the image.

        Args:
            image: the image with the pose to analyze

        Returns:
            str: the pose
        """
        return self.api.estimate(image)