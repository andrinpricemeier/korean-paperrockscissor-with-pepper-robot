from flask import Flask, jsonify, request
import base64
import cv2
import base64
import base64
import io
from imageio import imread
from pose_estimation import PoseEstimation
import logging
import logging.config
import configparser
from knn_classification.knn_classifier_model import KNNClassifierModel


def init_logging():
    logging.config.fileConfig(fname="logger.conf")

def read_config():
    temp_config = configparser.ConfigParser()
    temp_config.read("api.conf")
    return temp_config

try:
    init_logging()
    config = read_config()
    pose_estimation = PoseEstimation(KNNClassifierModel(config["KNNClassifier"]["SamplesFilepath"]), float(config["KNNClassifier"]["MinConfidence"]))
    app = Flask(__name__)
except Exception as e:
    print(e)

@app.route("/poses/estimation", methods=['POST'])
def estimate_pose():
    try:
        logging.info("Received pose estimation request.")
        estimation_request = request.get_json()
        # read and decode the image
        base64_image = estimation_request['image']      
        img = imread(io.BytesIO(base64.b64decode(base64_image)))
        # estimate pose
        (pose, confidence) = pose_estimation.estimate(img)
        logging.info("Pose estimation done.")
        logging.info(f"pose: {pose} ({confidence})")
        return jsonify({ "estimated_pose": pose, "confidence": confidence, "error": None}), 200
    except Exception as e:
        logging.exception("Something went wrong.")
        return jsonify({ "estimated_pose": None, "confidence": None, "error": repr(e)}), 500