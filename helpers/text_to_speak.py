import pyttsx3

engine = pyttsx3.init()

def text_to_speak(text):
    engine.say(text)
    engine.runAndWait()