from sensors.face_detector import FaceDetector
import logging
import time
from operator import itemgetter
class DibiFaceDetector(FaceDetector):
    def __init__(self, face_service, memory):
        self.face_service = face_service
        # Subscribing activates the face recognition, the result is written to FaceDetected in ALMemory.
        self.face_service.subscribe("Test_Face", 500, 0.0 )
        self.memory = memory

    def get_current_face_name(self):
        faces = self.__get_detected_faces()
        return self.__get_best_match_name(faces)

    def __get_best_match_name(self, faces):
        if len(faces) == 0:
            return None
        # Itemgetter uses the second element in the tuple, i.e. the score, to sort the list.
        sorted_faces = sorted(faces, key=itemgetter(1), reverse=True)
        best_match = sorted_faces[0]
        logging.info("Best matching face: {0} ({1}).".format(best_match[0], best_match[1]))
        return best_match[0]

    def __get_detected_faces(self):
        name_and_score = []
        for _ in range(0, 10):
            face = self.memory.getData("FaceDetected")
            if face and len(face) >= 2:
                for faceInfo in face[1]:
                    if faceInfo is None or len(faceInfo) < 2:
                        continue
                    faceExtraInfo = faceInfo[1]
                    # The last entry is "Time_Filtered_Reco_Info" and is a completely different structure, thus we skip it.
                    if len(faceExtraInfo) >= 3:
                        score = faceExtraInfo[1]
                        name = faceExtraInfo[2]
                        if name:
                            logging.info("num faces: {0}".format(len(face)))
                            logging.info("Retrieved face name: {0}".format(name))
                            name_and_score.append((name, score))
            if len(name_and_score) > 0:
                return name_and_score
            time.sleep(0.5)        
        logging.info("No face found.")
        return []

    def learn_face(self, person_name):
        logging.info("Learning face for {0}".format(person_name))
        return self.face_service.learnFace(person_name)