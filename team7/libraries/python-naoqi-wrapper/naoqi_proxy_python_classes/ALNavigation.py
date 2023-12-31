#!/usr/bin/env python
# Class autogenerated from .\alnavigationproxy.h
# by Sammy Pfeiffer's <Sammy.Pfeiffer at student.uts.edu.au> generator
# You need an ALBroker running





class ALNavigation(object):
    def __init__(self, session):
        self.session = session
        self.proxy = None

    def force_connect(self):
        self.proxy = self.session.service("ALNavigation")

    def findFreeZone(self, desiredRadius, maximumDisplacement):
        """Returns [errorCode, result radius[centerWorldMotionX, centerWorldMotionY]]

        :param float desiredRadius: The radius of the space we want in meters [m].
        :param float maximumDisplacement: The max distance we accept to move toreach the found place [m].
        :returns AL::ALValue: Returns [errorCode, result radius (m), [worldMotionToRobotCenterX (m), worldMotionToRobotCenterY (m)]]
        """
        if not self.proxy:
            self.proxy = self.session.service("ALNavigation")
        return self.proxy.findFreeZone(desiredRadius, maximumDisplacement)

    def getSecurityDistance(self):
        """Distance in meters fromwhich the robot should stop if there is an obstacle.

        :returns float: 
        """
        if not self.proxy:
            self.proxy = self.session.service("ALNavigation")
        return self.proxy.getSecurityDistance()

    def move(self, x, y, theta):
        """Makes the robot move at the given speed in S.I. units. This is a blocking call.

        :param float x: The speed along x axis [m.s-1].
        :param float y: The speed along y axis [m.s-1].
        :param float theta: The anglular speed around z axis [rad.s-1].
        """
        if not self.proxy:
            self.proxy = self.session.service("ALNavigation")
        return self.proxy.move(x, y, theta)

    def move2(self, x, y, theta, moveConfig):
        """Makes the robot move at the given speed in S.I. units. This is a blocking call.

        :param float x: The speed along x axis [m.s-1].
        :param float y: The speed along y axis [m.s-1].
        :param float theta: The anglular speed around z axis [rad.s-1].
        :param AL::ALValue moveConfig: An ALValue with custom move configuration.
        """
        if not self.proxy:
            self.proxy = self.session.service("ALNavigation")
        return self.proxy.move(x, y, theta, moveConfig)

    def moveAlong(self, trajectory):
        """.

        :param AL::ALValue trajectory: An ALValue describing a trajectory.
        :returns bool: 
        """
        if not self.proxy:
            self.proxy = self.session.service("ALNavigation")
        return self.proxy.moveAlong(trajectory)

    def moveTo(self, x, y, theta):
        """Makes the robot move at the given position.This is a blocking call.

        :param float x: The position along x axis [m].
        :param float y: The position along y axis [m].
        :param float theta: The angle around z axis [rad].
        """
        if not self.proxy:
            self.proxy = self.session.service("ALNavigation")
        return self.proxy.moveTo(x, y, theta)

    def moveTo2(self, x, y, theta, moveConfig):
        """Makes the robot move at the given position.This is a blocking call.

        :param float x: The position along x axis [m].
        :param float y: The position along y axis [m].
        :param float theta: The angle around z axis [rad].
        :param AL::ALValue moveConfig: An ALValue with custom move configuration.
        """
        if not self.proxy:
            self.proxy = self.session.service("ALNavigation")
        return self.proxy.moveTo(x, y, theta, moveConfig)

    def moveToward(self, x, y, theta):
        """Makes the robot move at the given speed in normalized speed fraction. This is a blocking call.

        :param float x: The speed along x axis [0.0-1.0].
        :param float y: The speed along y axis [0.0-1.0].
        :param float theta: The anglular speed around z axis [0.0-1.0].
        """
        if not self.proxy:
            self.proxy = self.session.service("ALNavigation")
        return self.proxy.moveToward(x, y, theta)

    def moveToward2(self, x, y, theta, moveConfig):
        """Makes the robot move at the given speed in normalized speed fraction. This is a blocking call.

        :param float x: The speed along x axis [0.0-1.0].
        :param float y: The speed along y axis [0.0-1.0].
        :param float theta: The anglular speed around z axis [0.0-1.0].
        :param AL::ALValue moveConfig: An ALValue with custom move configuration.
        """
        if not self.proxy:
            self.proxy = self.session.service("ALNavigation")
        return self.proxy.moveToward(x, y, theta, moveConfig)

    def navigateTo(self, x, y):
        """Makes the robot navigate to a relative metrical target pose2D expressed in FRAME_ROBOT. The robot computes a path to avoid obstacles.

        :param float x: The position along x axis [m].
        :param float y: The position along y axis [m].
        :returns bool: 
        """
        if not self.proxy:
            self.proxy = self.session.service("ALNavigation")
        return self.proxy.navigateTo(x, y)

    def navigateTo2(self, x, y, config):
        """Makes the robot navigate to a relative metrical target pose2D expressed in FRAME_ROBOT. The robot computes a path to avoid obstacles.

        :param float x: The position along x axis [m].
        :param float y: The position along y axis [m].
        :param AL::ALValue config: Configuration ALValue. For example, [["SpeedFactor", 0.5]] sets speedFactor to 0.5
        :returns bool: 
        """
        if not self.proxy:
            self.proxy = self.session.service("ALNavigation")
        return self.proxy.navigateTo(x, y, config)

    def navigateTo3(self, x, y, theta):
        """Makes the robot navigate to a relative metrical target pose2D expressed in FRAME_ROBOT. The robot computes a path to avoid obstacles.

        :param float x: The position along x axis [m].
        :param float y: The position along y axis [m].
        :param float theta: Orientation of the robot (rad).
        :returns bool: 
        """
        if not self.proxy:
            self.proxy = self.session.service("ALNavigation")
        return self.proxy.navigateTo(x, y, theta)

    def navigateTo4(self, x, y, theta, config):
        """Makes the robot navigate to a relative metrical target pose2D expressed in FRAME_ROBOT. The robot computes a path to avoid obstacles.

        :param float x: The position along x axis [m].
        :param float y: The position along y axis [m].
        :param float theta: Orientation of the robot (rad).
        :param AL::ALValue config: Configuration ALValue. For example, [["SpeedFactor", 0.5]] sets speedFactor to 0.5
        :returns bool: 
        """
        if not self.proxy:
            self.proxy = self.session.service("ALNavigation")
        return self.proxy.navigateTo(x, y, theta, config)

    def ping(self):
        """Just a ping. Always returns true

        :returns bool: returns true
        """
        if not self.proxy:
            self.proxy = self.session.service("ALNavigation")
        return self.proxy.ping()

    def setSecurityDistance(self, arg1):
        """Distance in meters fromwhich the robot should stop if there is an obstacle.

        :param float arg1: arg
        """
        if not self.proxy:
            self.proxy = self.session.service("ALNavigation")
        return self.proxy.setSecurityDistance(arg1)

    def startFreeZoneUpdate(self):
        """Starts a loop to update the mapping of the free space around the robot.
        """
        if not self.proxy:
            self.proxy = self.session.service("ALNavigation")
        return self.proxy.startFreeZoneUpdate()

    def stopAndComputeFreeZone(self, desiredRadius, maximumDisplacement):
        """Stops and returns free zone.

        :param float desiredRadius: The radius of the space we want in meters [m].
        :param float maximumDisplacement: The max distance we accept to move toreach the found place [m].
        :returns AL::ALValue: Returns [errorCode, result radius (m), [worldMotionToRobotCenterX (m), worldMotionToRobotCenterY (m)]]
        """
        if not self.proxy:
            self.proxy = self.session.service("ALNavigation")
        return self.proxy.stopAndComputeFreeZone(desiredRadius, maximumDisplacement)

    def stopNavigateTo(self):
        """Stops the navigateTo.
        """
        if not self.proxy:
            self.proxy = self.session.service("ALNavigation")
        return self.proxy.stopNavigateTo()

    def version(self):
        """Returns the version of the module.

        :returns str: A string containing the version of the module.
        """
        if not self.proxy:
            self.proxy = self.session.service("ALNavigation")
        return self.proxy.version()
