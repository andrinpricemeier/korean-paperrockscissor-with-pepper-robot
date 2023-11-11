from pepper import Robot, PepperConfiguration
import qi

# connect to a virtual robot
port = 54643  # start Choregraphe, go to Edit > Preferences > Virtual Robot to see port number
robot = Robot(PepperConfiguration("simulated_robot", "localhost", port))

# create proxy for text to speech and motion api
tts = robot.ALTextToSpeech
motion = robot.ALMotion

# let the robot talk and move in sequence
tts.say("i cannot move while i'm talking")
motion.moveTo(1, 0, 0)
tts.say("now i'm done")

# let the robot talk and move in parallel
qi.async(tts.say, "I'm starting to move now. Can you see how I can move and talk at the same time?")
future = qi.async(motion.moveTo, -1, 0, 0)
future.wait()
tts.say("ok, I'm done")