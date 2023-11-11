from robot_led import RobotLED

class DibiLED(RobotLED):
    def __init__(self, led_service):
        self.led_service = led_service

    def activate_rasta(self, duration_in_seconds=5):
        self.led_service.rasta(duration_in_seconds)