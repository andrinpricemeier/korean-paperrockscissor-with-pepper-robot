from actuators.pose import Pose

class RockPose(Pose):
    def assume(self, motion):
        names = list()
        times = list()
        keys = list()

        names.append("LElbowRoll")
        times.append([0.36])
        keys.append([[-1.42768, [3, -0.133333, 0], [3, 0, 0]]])

        names.append("LElbowYaw")
        times.append([0.36])
        keys.append([[-0.660509, [3, -0.133333, 0], [3, 0, 0]]])

        names.append("LHand")
        times.append([0.36])
        keys.append([[0.98, [3, -0.133333, 0], [3, 0, 0]]])

        names.append("LShoulderPitch")
        times.append([0.36])
        keys.append([[0.198283, [3, -0.133333, 0], [3, 0, 0]]])

        names.append("LShoulderRoll")
        times.append([0.36])
        keys.append([[0.237065, [3, -0.133333, 0], [3, 0, 0]]])

        names.append("LWristYaw")
        times.append([0.36])
        keys.append([[-0.42237, [3, -0.133333, 0], [3, 0, 0]]])

        names.append("RElbowRoll")
        times.append([0.36])
        keys.append([[1.54462, [3, -0.133333, 0], [3, 0, 0]]])

        names.append("RElbowYaw")
        times.append([0.36])
        keys.append([[0.7662, [3, -0.133333, 0], [3, 0, 0]]])

        names.append("RHand")
        times.append([0.36])
        keys.append([[0.02, [3, -0.133333, 0], [3, 0, 0]]])

        names.append("RShoulderPitch")
        times.append([0.36])
        keys.append([[0.387463, [3, -0.133333, 0], [3, 0, 0]]])

        names.append("RShoulderRoll")
        times.append([0.36])
        keys.append([[-0.23911, [3, -0.133333, 0], [3, 0, 0]]])

        names.append("RWristYaw")
        times.append([0.36])
        keys.append([[-0.492183, [3, -0.133333, 0], [3, 0, 0]]])
        
        motion.angleInterpolationBezier(names, times, keys)

