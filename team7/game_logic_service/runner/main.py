import configparser
import logging.config
from pepper import Robot, PepperConfiguration
from runner.dibi_service import DibiService
from os import path

def create_pepper(robot_config):
    if str(robot_config["Robot"]["UseVirtualRobot"]) == "True":
        return Robot(PepperConfiguration("simulated_robot", "localhost", int(robot_config["Robot"]["VirtualRobotPort"])))
    else:
        return Robot(PepperConfiguration(robot_config["Robot"]["RobotName"]))


def init_logging():
    logging.config.fileConfig(path.join(path.dirname(path.abspath(__file__)), 'logger.conf'))


def read_config():
    temp_config = configparser.ConfigParser()
    temp_config.read(path.join(path.dirname(path.abspath(__file__)), "dibi.conf"))
    return temp_config

if __name__ == '__main__':
    init_logging()
    config = read_config()
    pepper = create_pepper(config)
    service_id = None
    try:
        service = DibiService(pepper, config)
        service_id = pepper.session.registerService(config["Robot"]["ServiceName"], service)
        # Block the application until stop is called. Doesn't call start again if it was already called.
        # This obviates the need to use a while true loop.
        pepper.app.run()
    finally:
        logging.info("Deregistering.")
        if service_id:
            logging.info(service_id)
            pepper.session.unregisterService(service_id)


