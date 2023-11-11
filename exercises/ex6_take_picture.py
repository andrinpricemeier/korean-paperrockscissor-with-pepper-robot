from pepper import Robot, PepperConfiguration
from camera import Camera
from file_transfer import FileTransfer

config = PepperConfiguration("Amber")
robot = Robot(config)
camera = Camera(robot)

# take a picture


# copy file to local path
