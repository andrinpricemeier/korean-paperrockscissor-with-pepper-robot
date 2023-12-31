#!/usr/bin/env python
# Class autogenerated from .\almotionrecorderproxy.h
# by Sammy Pfeiffer's <Sammy.Pfeiffer at student.uts.edu.au> generator
# You need an ALBroker running





class ALMotionRecorder(object):
    def __init__(self, session):
        self.session = session
        self.proxy = None

    def force_connect(self):
        self.proxy = self.session.service("ALMotionRecorder")

    def dataChanged(self, dataName, data, message):
        """Called by ALMemory when subcription data is updated. INTERNAL

        :param str dataName: Name of the subscribed data.
        :param AL::ALValue data: Value of the the subscribed data
        :param str message: The message give when subscribing.
        """
        if not self.proxy:
            self.proxy = self.session.service("ALMotionRecorder")
        return self.proxy.dataChanged(dataName, data, message)

    def ping(self):
        """Just a ping. Always returns true

        :returns bool: returns true
        """
        if not self.proxy:
            self.proxy = self.session.service("ALMotionRecorder")
        return self.proxy.ping()

    def startInteractiveRecording(self, jointsToRecord, nbPoses, extensionAllowed, mode):
        """Start recording the motion in an interactive mode

        :param std::vector<std::string> jointsToRecord: Names of joints that must be recorded
        :param int nbPoses: Default number of poses to record
        :param bool extensionAllowed: Set to true to ignore nbPoses and keep recording new poses as long as record is not manually stopped
        :param int mode: Indicates which interactive mode must be used. 1 : Use right bumper to enslave and left bumper to store the pose  (deprecated); 2 : Use chest button to store the pose
        """
        if not self.proxy:
            self.proxy = self.session.service("ALMotionRecorder")
        return self.proxy.startInteractiveRecording(jointsToRecord, nbPoses, extensionAllowed, mode)

    def startPeriodicRecording(self, jointsToRecord, nbPoses, extensionAllowed, timeStep, jointsToReplay, replayData):
        """Start recording the motion in a periodic mode

        :param std::vector<std::string> jointsToRecord: Names of joints that must be recorded
        :param int nbPoses: Default number of poses to record
        :param bool extensionAllowed: set to true to ignore nbPoses and keep recording new poses as long as record is not manually stopped
        :param float timeStep: Time in seconds to wait between two poses
        :param std::vector<std::string> jointsToReplay: Names of joints that must be replayed
        :param AL::ALValue replayData: An ALValue holding data for replayed joints. It holds two ALValues. The first one is an ALValue where each line corresponds to a joint, and column elements are times of control points The second one is also an ALValue where each line corresponds to a joint, but column elements are arrays containing [float angle, Handle1, Handle2] elements, where Handle is [int InterpolationType, float dAngle, float dTime] describing the handle offsets relative to the angle and time of the point. The first bezier param describes the handle that controls the curve preceding the point, the second describes the curve following the point.
        """
        if not self.proxy:
            self.proxy = self.session.service("ALMotionRecorder")
        return self.proxy.startPeriodicRecording(jointsToRecord, nbPoses, extensionAllowed, timeStep, jointsToReplay, replayData)

    def stopAndGetRecording(self):
        """Stop recording the motion and return data

        :returns AL::ALValue: Returns the recorded data as an ALValue: [[JointName1,[pos1, pos2, ...]], [JointName2,[pos1, pos2, ...]], ...]
        """
        if not self.proxy:
            self.proxy = self.session.service("ALMotionRecorder")
        return self.proxy.stopAndGetRecording()

    def version(self):
        """Returns the version of the module.

        :returns str: A string containing the version of the module.
        """
        if not self.proxy:
            self.proxy = self.session.service("ALMotionRecorder")
        return self.proxy.version()
