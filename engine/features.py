from playsound import playsound
import eel
from engine.config import ASSISTANT_NAME
from engine.command import speak
import os
import pywhatkit as kit
import re


# playing assistant sound function

@eel.expose
def playAssistantSound():
	music_dir = "www\\assets\\audio\\start_sound.mp3"
	playsound(music_dir)


def openCommand(query):
	query = query.replace(ASSISTANT_NAME, "")
	query = query.replace("open", "")
	query.lower()

	if query!="":
		speak("opening "+query)
		os.system('start '+query)

	else:
		speak("not found")

def PlayYoutube(query):
    search_term = extract_yt_term(query)

    if search_term:
        speak("Playing " + search_term + " on YouTube")
        kit.playonyt(search_term)
    else:
        speak("Sorry, I could not find that video")

def extract_yt_term(command):
	pattern = r'play\s+(.*?)\s+on\s+youtube'
	match = re.search(pattern, command, re.IGNORECASE)
	return match.group(1) if match else None
