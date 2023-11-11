import mediapipe as mp
import pandas as pd
import numpy as np
from estimation_model import EstimationModel
from knn_classification.full_body_pose_embedder import FullBodyPoseEmbedder
from knn_classification.pose_sample import PoseSample
from knn_classification.pose_classifier import PoseClassifier
import logging

class KNNClassifierModel(EstimationModel):
    """Classifies dibi game poses using a k-nearest neighbour algorithm."""
    def __init__(self, pose_samples_filepath):
        """Creates a new instance.

        Args:
            pose_samples_filepath (string): the path of the csv containing the pose samples including classes.
        """
        self.samples = self.__load_samples(pose_samples_filepath)

    def estimate(self, image, model_complexity, min_confidence):
        """Estimates and classifies a dibi pose.

        Args:
            image: the image to classify
            model_complexity (int): the complexity of the MediaPipe model to use. Acceptable values: 0, 1 and 2.
            min_confidence (float): the minimum confidence required for the estimated pose to be accepted.

        Returns:
            [(str, float)]: The estimated (pose_name, confidence).
        """
        pose_embedder = FullBodyPoseEmbedder()
        pose_classifier = PoseClassifier(
            pose_embedder=pose_embedder,
            pose_samples=self.samples,
            top_n_by_max_distance=300,
            top_n_by_mean_distance=100)        
        with mp.solutions.pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5, model_complexity=model_complexity) as pose:
            results = pose.process(image)
            if results.pose_landmarks is None:
                logging.info("No landmarks found.")
                return ("UNKNOWN", 0)
            # Extract the relevant coordinates
            # We don't consider the visibility coordinate 'v' as relevant.
            pose_landmarks = np.array([[lmk.x, lmk.y, lmk.z]
                                 for lmk in results.pose_landmarks.landmark], dtype=np.float32)
          
            # We only need a few joints for recognition.
            # We need more than the left and wrist because we have to normalize the size/translation.
            relevant_landmarks = [pose_landmarks[11], pose_landmarks[12], pose_landmarks[13], pose_landmarks[14], pose_landmarks[15], pose_landmarks[16], pose_landmarks[23], pose_landmarks[24]]
        
            pose_classification = pose_classifier(relevant_landmarks)
            
            predicted_class = None
            predicted_confidence = 0
            # We get the specified number of samples back that are closest to the opponent's pose.
            # We pick the one that has at least min_confidence samples.
            for key, value in pose_classification.items():
                if value >= (100 * min_confidence):
                    predicted_class = key
                    predicted_confidence = value / 100
                    break
            if predicted_class is None:
                return ("UNKNOWN", 0)
            else:
                # We used two different classes in the samples for both the left side scissor and right side scissor.
                if predicted_class == "Scissor1" or predicted_class == "Scissor2":
                    return ("SCISSOR", predicted_confidence)
                else:
                    return (predicted_class.upper(), predicted_confidence)

    def __load_samples(self, pose_samples_filepath):
        data = pd.read_csv(pose_samples_filepath, sep=";")
        samples = []
        pose_embedder = FullBodyPoseEmbedder()
        for index in data.index:
            entry = {}
            entry['classname'] = data['class'][index]
            entry['landmarks'] = [
                [data['x11'][index], data['y11'][index], data['z11'][index]],
                [data['x12'][index], data['y12'][index], data['z12'][index]],
                [data['x13'][index], data['y13'][index], data['z13'][index]],
                [data['x14'][index], data['y14'][index], data['z14'][index]],
                [data['x15'][index], data['y15'][index], data['z15'][index]],
                [data['x16'][index], data['y16'][index], data['z16'][index]],
                [data['x23'][index], data['y23'][index], data['z23'][index]],
                [data['x24'][index], data['y24'][index], data['z24'][index]]
            ]
            samples.append(PoseSample(
                    name=index,
                    landmarks=entry['landmarks'],
                    class_name=entry['classname'],
                    embedding=pose_embedder(entry['landmarks']),
                ))
        return samples