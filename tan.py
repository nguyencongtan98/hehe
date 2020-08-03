print("tan")
you = "hello"

if you == "":
	robot_brain = "I can't hear you, try again"
elif you == "hello":
	robot_brain = "hello dung lai"
else:
	robot_brain = "I'm fine thank you"

print(robot_brain)

import pyttsx3


robot_mouth = pyttsx3.init()
robot_mouth.say(robot_brain)
robot_mouth.runAndWait()