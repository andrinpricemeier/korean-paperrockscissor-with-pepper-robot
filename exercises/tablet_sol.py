import qi
import os
import shutil


class Tablet:

    __pepper_path = "/opt/aldebaran/var/www/apps/"
    __path_from_tablet_to_pepper = "http://198.18.0.1/apps/"

    def __init__(self, robot, app_name = "my_app"):
        self.__al_tablet = robot.session.service("ALTabletService")
        self.__al_tablet.loadApplication(app_name)
        self.__app_name = app_name
        self.__create_directories()

    def __create_directories(self):
        if not os.path.exists(self.__pepper_path+self.__app_name):
            os.mkdir(self.__pepper_path+self.__app_name)
        if not os.path.exists(self.__pepper_path + self.__app_name+ "/html"):
            os.mkdir(self.__pepper_path+self.__app_name + "/html")

    def __remove_directories(self):
        shutil.rmtree(self.__pepper_path+self.__app_name)

    def close(self):
        self.__remove_directories()

    def show_image(self, path, file, async = True):
        shutil.copyfile(path+file, self.__pepper_path + self.__app_name+ "/html/" + file)
        if async:
            qi.async(self.__al_tablet.showImageNoCache, self.__path_from_tablet_to_pepper+self.__app_name+"/"+file)
        else:
            self.__al_tablet.showImageNoCache(self.__path_from_tablet_to_pepper+self.__app_name+"/"+file)

    def hide_image(self):
        self.__al_tablet.hideImage()