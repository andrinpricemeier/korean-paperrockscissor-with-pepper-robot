import requests
import json
import base64
import logging

from actuators.dibi_pose import DibiPose


class PoseEstimationAPI:
    """Represents the API for the pose estimation that is run separately.
    """
    def __init__(self, base_url, estimation_endpoint):
        self.base_url = base_url
        self.estimation_endpoint = estimation_endpoint

    def estimate(self, image):
        """Estiamtes the pose based on the image.

        Args:
            image: the image with a person making a pose

        Returns:
            DibiPose: the most likely pose
        """
        estimation_request = {"image": base64.b64encode(image).decode()}
        headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
        json_request = json.dumps(estimation_request)
        response = requests.post(self.base_url + self.estimation_endpoint, data=json_request, headers=headers)
        estimation_response = json.loads(response.content)
        if response.ok:
            logging.info("Estimated pose: " + estimation_response['estimated_pose'])
            return DibiPose[estimation_response['estimated_pose']]
        else:
            logging.error(estimation_response.error)
            return DibiPose["UNKNOWN"]

