from pepper import Robot, PepperConfiguration

from camera import Camera
from file_transfer import FileTransfer

config = PepperConfiguration("Amber")
robot = Robot(config)
camera = Camera(robot)

# take a picture
remote_folder_path = "/home/nao/recordings/cameras/"
file_name = "my_picture.jpg"
camera.take_picture(remote_folder_path, file_name)

# copy file to local path
local = "C:\\work\\"+file_name
remote = remote_folder_path+file_name
file_transfer = FileTransfer(robot)
file_transfer.get(remote, local)
file_transfer.close()