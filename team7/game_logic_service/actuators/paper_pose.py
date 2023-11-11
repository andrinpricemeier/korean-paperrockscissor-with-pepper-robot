from actuators.pose import Pose

class PaperPose(Pose):
    def assume(self, motion):
        names = list()
        times = list()
        keys = list()

        names.append("LElbowRoll")
        times.append([0.36])
        keys.append([[-1.56207, [3, -0.133333, 0], [3, 0, 0]]])

        names.append("LElbowYaw")
        times.append([0.36])
        keys.append([[-2.08567, [3, -0.133333, 0], [3, 0, 0]]])

        names.append("LHand")
        times.append([0.36])
        keys.append([[0.98, [3, -0.133333, 0], [3, 0, 0]]])

        names.append("LShoulderPitch")
        times.append([0.36])
        keys.append([[0.961676, [3, -0.133333, 0], [3, 0, 0]]])

        names.append("LShoulderRoll")
        times.append([0.36])
        keys.append([[0.287979, [3, -0.133333, 0], [3, 0, 0]]])

        names.append("LWristYaw")
        times.append([0.36])
        keys.append([[1.82387, [3, -0.133333, 0], [3, 0, 0]]])

        names.append("RElbowRoll")
        times.append([0.36])
        keys.append([[1.56207, [3, -0.133333, 0], [3, 0, 0]]])

        names.append("RElbowYaw")
        times.append([0.36])
        keys.append([[2.08567, [3, -0.133333, 0], [3, 0, 0]]])

        names.append("RHand")
        times.append([0.36])
        keys.append([[0.98, [3, -0.133333, 0], [3, 0, 0]]])

        names.append("RShoulderPitch")
        times.append([0.36])
        keys.append([[0.95644, [3, -0.133333, 0], [3, 0, 0]]])

        names.append("RShoulderRoll")
        times.append([0.36])
        keys.append([[-0.312414, [3, -0.133333, 0], [3, 0, 0]]])

        names.append("RWristYaw")
        times.append([0.36])
        keys.append([[-1.82387, [3, -0.133333, 0], [3, 0, 0]]])

        motion.angleInterpolationBezier(names, times, keys)
