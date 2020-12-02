import pyttsx3

def talk(speech, userName):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    speech = userName + ", " + speech
    engine.say(speech)
    engine.runAndWait()