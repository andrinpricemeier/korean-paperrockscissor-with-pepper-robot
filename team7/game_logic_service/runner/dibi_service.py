from agent_logic.brain_constants import DIBI_NAMEREACTION, DIBI_ACTIVEGAME, DIBI_BODY, DIBI_CAMERA, DIBI_CORPUS, DIBI_DIALOG, DIBI_FACEDETECTOR, DIBI_GAMEREGION, DIBI_OPPONENTNAME, DIBI_POSEESTIMATION, DIBI_SPEAKER
from agent_logic.brain_constants import DIBI_ASYNCSERVICE
from agent_logic.brain_constants import DIBI_MOODDETECTOR
from actuators.dibi_led import DibiLED
from agent_logic.brain_constants import DIBI_LED
from sensors.dibi_mood_detector import DibiMoodDetector
from utils.qi_async_service import QiAsyncService
from sensors.dibi_face_detector import DibiFaceDetector
from actuators.name_reaction import NameReaction
from game_logic.player_statistics import PlayerStatistics
from sensors.pose_estimation_api import PoseEstimationAPI
from actuators.dibi_speaker import DibiSpeaker
from actuators.corpus import Corpus
from actuators.dibi_dialog import DibiDialog
from actuators.dibi_body import DibiBody
from sensors.dibi_camera import DibiCamera
from sensors.dibi_pose_estimation import DibiPoseEstimation
from agent_logic.blackboard import Blackboard
from agent_logic.agent import Agent
from game_logic.game import Game
from sensors.dibi_game_region import DibiGameRegion
from game_logic.player import Player
from game_logic.follower import Follower
from game_logic.leader import Leader
from utils.pseudo_random_source import PseudoRandomSource
import logging
from actuators.dictionary import dictionary

class DibiService:
    """Represents a NAOQi service that is called by the interactive activity.
    """
    def __init__(self, pepper, config):
        self.pepper = pepper
        self.config = config
        self.dialog = pepper.session.service("ALDialog")
        self.face_detection = self.pepper.ALFaceDetection

    def run(self):
        logging.info("DibiService called.")
        try:
            logging.info("Creating brain.")
            brain = self.create_brain()
            logging.info("Brain created.")
            agent = Agent(brain)
            agent.run()
        except Exception as e:
            logging.exception("Unexpected error.")
        self.__unsubscribe_everything()        
        logging.info("DibiService done.")

    def __unsubscribe_everything(self):
        # This is some ugly code, but to prevent memory leaks we try to unsubscribe from
        # any services that may still be running. If it fails we can't do anything anyway.
        # Interestingly enough, the "subscribe" methods seem to be idempotent, the unsubscribe methods however aren't.
        # If we don't do this the robot fails to exit our activity and must be rebooted.
        try:
            self.dialog.unsubscribe('anything')
        except Exception:
            pass
        try:
            self.face_detection.unsubscribe('Test_Face')
        except Exception:
            pass

    def create_brain(self):
        corpus = Corpus(dictionary, PseudoRandomSource())
        engagement_zone = self.pepper.session.service("ALEngagementZones")
        engagement_zone.setFirstLimitDistance(float(self.config["GameRegion"]["Zone1DistanceInMetres"]))
        engagement_zone.setSecondLimitDistance(float(self.config["GameRegion"]["Zone2DistanceInMetres"]))
        led_service = self.pepper.ALLeds
        led = DibiLED(led_service) 
        memory = self.pepper.ALMemory
        audio = self.pepper.ALAudioDevice
        speaker = DibiSpeaker(self.pepper.ALTextToSpeech, self.pepper.ALAnimatedSpeech, memory, corpus, audio, int(self.config["Dialog"]["SlowSpeakingSpeedInPercent"]), int(self.config["Dialog"]["ShoutingVolumeIncreaseInPercent"]), int(self.config["Dialog"]["ShoutingPitch"]))
        dialog_service = self.pepper.session.service("ALDialog")
        dialog_service.setLanguage("English")
        dialog = DibiDialog(dialog_service, corpus, memory)
        photo = self.pepper.ALPhotoCapture
        posture = self.pepper.ALRobotPosture
        camera = DibiCamera(photo, self.pepper, self.config["Camera"]["ImagesFolder"])
        estimation_api = PoseEstimationAPI(self.config["PoseEstimation"]["BaseURL"], self.config["PoseEstimation"]["EstimationEndpoint"])
        pose_estimation = DibiPoseEstimation(estimation_api)
        motion = self.pepper.ALMotion
        body = DibiBody(motion, posture)
        game_region = DibiGameRegion(memory, speaker)
        brain = Blackboard()
        face_detection = self.pepper.ALFaceDetection
        face_detector = DibiFaceDetector(face_detection, memory)
        opponent_name = face_detector.get_current_face_name()
        robot_player = Player(PseudoRandomSource(), Leader(), 0, PlayerStatistics(PseudoRandomSource(), 0, 0, 0))
        opponent_player = Player(PseudoRandomSource(), Follower(), 0, PlayerStatistics(PseudoRandomSource(), float(self.config["Game"]["InitialRockProb"]) * 100, float(self.config["Game"]["InitialPaperProb"]) * 100, float(self.config["Game"]["InitialScissorProb"]) * 100))
        name_reaction = NameReaction(speaker)
        name_reaction.add("Pepper", "opponent_name_reaction_pepper")
        name_reaction.add("Condiment", "opponent_name_reaction_condiment")
        name_reaction.add("Nao", "opponent_name_reaction_nao")
        name_reaction.add("Romeo", "opponent_name_reaction_romeo")
        mood_detector = DibiMoodDetector(self.pepper.session.service("ALMood"))
        brain.set_value(DIBI_LED, led)
        brain.set_value(DIBI_MOODDETECTOR, mood_detector)
        brain.set_value(DIBI_NAMEREACTION, name_reaction)
        brain.set_value(DIBI_SPEAKER, speaker)
        brain.set_value(DIBI_ASYNCSERVICE, QiAsyncService())
        brain.set_value(DIBI_CORPUS, corpus)
        brain.set_value(DIBI_DIALOG, dialog)
        brain.set_value(DIBI_CAMERA, camera)
        brain.set_value(DIBI_GAMEREGION, game_region)
        brain.set_value(DIBI_POSEESTIMATION, pose_estimation)
        brain.set_value(DIBI_BODY, body)
        brain.set_value(DIBI_FACEDETECTOR, face_detector)
        brain.set_value(DIBI_OPPONENTNAME, opponent_name)
        brain.set_value(DIBI_ACTIVEGAME, Game(PseudoRandomSource(), robot_player, opponent_player, int(self.config["Game"]["SwitchAfterPoints"])))
        return brain
