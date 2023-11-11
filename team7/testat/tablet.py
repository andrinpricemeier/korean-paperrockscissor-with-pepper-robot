from pepper import Robot, PepperConfiguration


class Tablet:
    def __init__(self, robot):
        self.robot = robot

    def run_demo(self):
        tablet = robot.session.service("ALTabletService")
        tablet.loadApplication(".lastUploadedChoregrapheBehavior")
        # tablet.loadApplication("example_1_images")
        tablet.showWebview()

if __name__ == '__main__':
    config = PepperConfiguration("Pale")
    robot = Robot(config)
    if robot.ALAutonomousLife.getState() != "disabled":
        robot.ALAutonomousLife.setState("disabled")
    if robot.ALRobotPosture.getPosture() != "Stand":
        robot.ALRobotPosture.goToPosture("Stand", 0.5)
    tablet = Tablet(robot)
    tablet.run_demo()

