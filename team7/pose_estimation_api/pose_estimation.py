import logging

class PoseEstimation():
    """Represents the main logic for classifying a pose.
    """
    def __init__(self, estimation_model, min_confidence):
        """Creates a new instance.

        Args:
            estimation_model (EstimationModel): the classifier to use
            min_confidence (float): the minimum confidence required for the pose to be accepted.
        """
        self.estimation_model = estimation_model
        self.min_confidence = min_confidence

    def estimate(self, image):
        """Estimates a pose

        Args:
            image: the image to classify

        Returns:
            (str, float): the estimated pose in format: (pose name, confidence)
        """
        try:
            # We first try the simpler MediaPipe model which is faster but less accurate to save time.
            # Only if it fails to detect the landmarks do we switch and try again.
            (pose, conf) = self.estimation_model.estimate(image, 1, self.min_confidence)
            if pose == "UNKNOWN":
                return self.estimation_model.estimate(image, 2, self.min_confidence)
            else:
                return (pose, conf)
        except Exception as e:
            logging.exception("Pose estimation failed.")
            return ("UNKNOWN", 0)
