class EstimationModel():
    """Represents a model for classification/estimation of poses.
    """
    def estimate(self, image, model_complexity, min_confidence=0.8):
        """Estimates and classifies a dibi pose.

        Args:
            image: the image to classify
            model_complexity (int): the complexity of the MediaPipe model to use. Acceptable values: 0, 1 and 2.
            min_confidence (float): the minimum confidence required for the estimated pose to be accepted.

        Returns:
            [(str, float)]: The estimated (pose_name, confidence).
        """
        pass