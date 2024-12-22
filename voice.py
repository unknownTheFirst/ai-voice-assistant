import pyttsx3

def speak(prompt):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 170)
    engine.say(prompt)
    engine.runAndWait()

