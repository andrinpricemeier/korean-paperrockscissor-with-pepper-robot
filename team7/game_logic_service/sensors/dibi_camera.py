import vision_definitions
from utils.file_transfer import FileTransfer
from sensors.camera import Camera
import logging
class DibiCamera(Camera):
    __camera_id = vision_definitions.kTopCamera
    __resolution = vision_definitions.kVGA  # 640x480px
    __picture_format = "jpg"

    def __init__(self, photo, robot, images_folder):
        self.photo = photo
        self.robot = robot
        self.images_folder = images_folder
        self.__configure_camera(self.__camera_id, self.__resolution, self.__picture_format)

    def __configure_camera(self, camera_id, resolution, format):
        self.photo.setCameraID(camera_id)
        self.photo.setResolution(resolution)
        self.photo.setPictureFormat(format)

    def take_picture(self):
        logging.info("Taking picture.")
        remote_folder = "/home/nao/recordings/cameras/"
        image_filename = "temp_image.jpg"
        self.photo.takePicture(remote_folder, image_filename)
        # The picture is taken on the robot, our code is run on the laptop however.
        # That's why we have to download it first.
        file_transfer = FileTransfer(self.robot)
        file_transfer.get(remote_folder + image_filename, self.images_folder + image_filename)
        file_transfer.close()
        with open(self.images_folder + image_filename, "rb") as f:
            return f.read()
