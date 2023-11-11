from pepper import Robot, PepperConfiguration
from camera import Camera
from tablet import Tablet
import time

config = PepperConfiguration("Porter")
robot = Robot(config)
camera = Camera(robot)

# take a picture
remote_folder_path = "/home/nao/recordings/cameras/"
file_name = "my_picture.jpg"
camera.take_picture(remote_folder_path, file_name)

tablet = Tablet(robot)

try:
    tablet.show_image(remote_folder_path, file_name)
    time.sleep(5)
    tablet.hide_image()
    tablet.close()
except RuntimeError, e:
    print "error in showing image on tablet", e