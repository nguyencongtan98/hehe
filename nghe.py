# import speech_recognition

# robot_ear = speech_recognition.Recognizer()
# with speech_recognition.Microphone() as mic:
# 	print("Robot: I'm Listening ... ")
# 	audio = robot_ear.listen(mic)
# try:
# 	you = robot_ear.recognize_google(audio, language="fr-FR")
# except:
# 	you = "loi"

# print(you) Tan NGuyen

import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
	print("Speak anithing ...")
	audio = r.listen(source)
	try:
		text = r.recognize_google(audio)
		print("You said: {}".format(text))
	except:
		print("Sorry")
