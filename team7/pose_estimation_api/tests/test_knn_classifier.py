import os
import sys
import inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

import cv2
from knn_classification.knn_classifier_model import KNNClassifierModel

def estimate_pose(image_filepath, expected_pose):
    estimator = KNNClassifierModel("tests/models/pose_samples.csv")
    image = cv2.imread("tests/test_images/" + image_filepath)
    (pose, confidence) = estimator.estimate(image, 1, 0.8)
    assert pose == expected_pose

def test_estimates_rock_correctly():
    estimate_pose("test_image_rock.jpg", "ROCK")

def test_estimates_scissor_correctly():
    estimate_pose("test_image_scissor.jpg", "SCISSOR")

def test_estimates_paper_correctly():
    estimate_pose("test_image_paper.jpg", "PAPER")

def test_on_estimation_failure_returns_unknown():
    estimate_pose("test_image_unknown.jpg", "UNKNOWN")
