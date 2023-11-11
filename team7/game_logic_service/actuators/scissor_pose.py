from actuators.pose import Pose

class ScissorPose(Pose):
    def assume(self, motion):
        names = list()
        times = list()
        keys = list()

        names.append("LElbowRoll")
        times.append([0.36])
        keys.append([[-1.34216, [3, -0.133333, 0], [3, 0, 0]]])

        names.append("LElbowYaw")
        times.append([0.36])
        keys.append([[-1.5798, [3, -0.133333, 0], [3, 0, 0]]])

        names.append("LShoulderPitch")
        times.append([0.36])
        keys.append([[-0.106465, [3, -0.133333, 0], [3, 0, 0]]])

        names.append("LWristYaw")
        times.append([0.36])
        keys.append([[1.01404, [3, -0.133333, 0], [3, 0, 0]]])

        names.append("RElbowRoll")
        times.append([0.36])
        keys.append([[1.39277, [3, -0.133333, 0], [3, 0, 0]]])

        names.append("RElbowYaw")
        times.append([0.36])
        keys.append([[0.0383972, [3, -0.133333, 0], [3, 0, 0]]])

        names.append("RHand")
        times.append([0.36])
        keys.append([[0.98, [3, -0.133333, 0], [3, 0, 0]]])

        names.append("RShoulderPitch")
        times.append([0.36])
        keys.append([[-0.0296706, [3, -0.133333, 0], [3, 0, 0]]])

        names.append("RWristYaw")
        times.append([0.36])
        keys.append([[1.41721, [3, -0.133333, 0], [3, 0, 0]]])

        motion.angleInterpolationBezier(names, times, keys)

