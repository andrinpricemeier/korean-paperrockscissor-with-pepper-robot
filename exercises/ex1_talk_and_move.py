from pepper import Robot, PepperConfiguration
import qi

# connect to a virtual robot
port = 59575  # start Choregraphe, go to Edit > Preferences > Virtual Robot to see port number
robot = Robot(PepperConfiguration("simulated_robot", "localhost", port))

# let the robot talk and move in sequence
tts = robot.ALTextToSpeech
motion = robot.ALMotion
tts.say("test")
motion.moveTo(1, 0, 0)
tts.say("done")

# let the robot talk and move in parallel
qi.async(tts.say, "test")
future = qi.async(motion.moveTo, -1, 0, 0)
future.wait()
tts.say("im done")