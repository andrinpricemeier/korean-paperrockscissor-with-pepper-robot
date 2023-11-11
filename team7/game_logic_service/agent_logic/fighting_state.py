from agent_logic.brain_constants import DIBI_CORPUS, DIBI_DIALOG, DIBI_CAMERA, DIBI_ACTIVEGAME, DIBI_BODY, DIBI_GAMEREGION, DIBI_POSEESTIMATION, DIBI_SPEAKER
from agent_logic.state import State
from actuators.dibi_pose import DibiPose, get_pose_name_by_index
from agent_logic.brain_constants import DIBI_ASYNCSERVICE
from agent_logic.farewell_state import FarewellState
from agent_logic.brain_constants import DIBI_OPPONENTNAME
from agent_logic.brain_constants import DIBI_MOODDETECTOR
import logging
from agent_logic.brain_constants import DIBI_LED

class FightingState(State):
    """The state in which the actual game takes place.
    """
    def __init__(self, state_machine, brain):
        self.state_machine = state_machine
        self.brain = brain

    def enter(self):
        logging.info("Starting fighting state.")
        corpus = self.brain.get_value(DIBI_CORPUS)
        dialog = self.brain.get_value(DIBI_DIALOG)
        speaker = self.brain.get_value(DIBI_SPEAKER)
        game = self.brain.get_value(DIBI_ACTIVEGAME)
        led = self.brain.get_value(DIBI_LED)
        game_region = self.brain.get_value(DIBI_GAMEREGION)
        async_service = self.brain.get_value(DIBI_ASYNCSERVICE)
        opponent_name = self.brain.get_value(DIBI_OPPONENTNAME)
        mood_detector = self.brain.get_value(DIBI_MOODDETECTOR)
        camera = self.brain.get_value(DIBI_CAMERA)
        if opponent_name is None:
            speaker.say("start_game")
        else:
            speaker.say_with_args("start_game_with_name", opponent_name)
        self.__inform_opponent_about_role(game, speaker)
        while self.__opponent_wants_to_play(dialog, corpus, game.rounds):
            # game_region.ensure_is_in_zone(2)

            # By animating our LEDs we give the opponent a hint on to when and for how long he has time to make a pose.
            async_service.future(led.activate_rasta)
            speaker.say_slowly("start_dibi_part_1")
            speaker.say_slowly("start_dibi_part_2")
            speaker.shout("start_dibi_part_3")

            if game.should_robot_lose_on_purpose():
                (robot_pose, opponent_pose) = self.__lose_on_purpose(camera)
            else:
                (robot_pose, opponent_pose) = self.__try_to_win(camera, async_service)

            game.evaluate_round(robot_pose, opponent_pose)
            self.__handle_game_result(game, speaker, opponent_pose, opponent_name)            
            opponent_mood = mood_detector.detect()
            game.record_opponent_mood(opponent_mood)
            self.__handle_role_switch(game, speaker)

        self.state_machine.transition(FarewellState(self.state_machine, self.brain))
        logging.info("Fighting state done.")

    def __inform_opponent_about_role(self, game, speaker):
        if game.opponent_is_leader():
            speaker.say("opponent_is_leader")
        else:
            speaker.say("opponent_is_follower")

    def __opponent_wants_to_play(self, dialog, corpus, rounds_played):
        if self.state_machine.is_done:
            return False
        if rounds_played == 0 or rounds_played % 3 != 0:
            return True
        play_again = dialog.ask("play_again_question",
                                    "play_again_accepted_reaction",
                                    "play_again_declined_reaction")
        return play_again is not None and play_again == 0

    def __handle_game_result(self, game, speaker, opponent_pose, opponent_name):
        if opponent_pose == DibiPose["UNKNOWN"]:
            speaker.say("pose_not_recognized")
            return

        # Say the recognized pose. This is mainly for verification purposes but useful nonetheless.
        speaker.say_with_args("opponent_picked_pose", get_pose_name_by_index(opponent_pose))
        if game.did_opponent_win_last_round():
            if opponent_name is None:
                speaker.say("congratulate")
            else:
                speaker.say_with_args("congratulate_with_name", opponent_name)
        else:
            if opponent_name is None:
                speaker.say("condole")
            else:
                speaker.say_with_args("condole_with_name", opponent_name)

    def __handle_role_switch(self, game, speaker):
        if game.did_role_switch_occur_last_round():
            if game.opponent_is_leader():
                speaker.say("role_switched_opponent_now_leader")
            else:
                speaker.say("role_switched_opponent_now_follower")

    def __try_to_win(self, camera, async_service):
        body = self.brain.get_value(DIBI_BODY)
        pose_estimation = self.brain.get_value(DIBI_POSEESTIMATION)
        game = self.brain.get_value(DIBI_ACTIVEGAME)
        # Take the image first before moving ourselves so that the image isn't blurry.
        opponent_image = camera.take_picture()
        # Pick a pose based on a prediction of the opponent's pose and his statistics.
        next_robot_pose = game.pick_winning_robot_pose()
        robot_pose_future = async_service.future(body.assume_pose, next_robot_pose)
        opponent_pose_future = async_service.future(pose_estimation.estimate, opponent_image)
        robot_pose_future.wait()
        opponent_pose_future.wait()
        return next_robot_pose, opponent_pose_future.value()

    def __lose_on_purpose(self, camera):
        body = self.brain.get_value(DIBI_BODY)
        pose_estimation = self.brain.get_value(DIBI_POSEESTIMATION)
        game = self.brain.get_value(DIBI_ACTIVEGAME)

        opponent_image = camera.take_picture()

        # Let the opponent pick a pose, but wait with picking one ourselves.
        opponent_pose = pose_estimation.estimate(opponent_image)

        # Now use the opponent's pose to pick a losing pose ourselves and act like nothing happened.
        next_robot_pose = game.pick_losing_robot_pose(opponent_pose)
        body.assume_pose(next_robot_pose)
        return next_robot_pose, opponent_pose