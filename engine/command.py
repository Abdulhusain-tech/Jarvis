import pyttsx3


def speak(text):
	engine = pyttsx3.init('sapi5')
	voices = engine.getProperty('voices')
	print(voices)
	engine.setProperty('voice', voices[2].id)
	engine.setProperty('rate', 175)

	engine.say(text)
	engine.runAndWait()

speak("Hi Abdulhusain! How are you? I hope you are fine")