import speech_recognition as sr

def listen(r, time):
    
    with sr.Microphone() as source:
        try:
            print("I'm listening...")
            data = r.record(source, duration=time)
            text = r.recognize_google(data,language='en')
            return text
        except:
            return None
    