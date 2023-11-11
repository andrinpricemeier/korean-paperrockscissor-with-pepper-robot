from pepper import Robot, PepperConfiguration
from dialog import Dialog

config = PepperConfiguration("Pale")
robot = Robot(config)
dialog = Dialog(robot)


topic_name = "topic_yes_no"
dialog.load_yes_no_question(topic_name, "hello human, are you ready to play a game", "great, let's start the game", "what a pity")
print "user's choice:  " + dialog.ask_yes_no_question(topic_name)
dialog.stop_topic(topic_name)

dialog.close_session()