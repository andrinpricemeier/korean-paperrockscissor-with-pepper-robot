from pepper import Robot, PepperConfiguration
from dialog import Dialog

config = PepperConfiguration("Amber")
robot = Robot(config)
dialog = Dialog(robot)

dialog.say("how are you today")
dialog.say_slowly("i am tired")
dialog.shout("what are you doing here?")

