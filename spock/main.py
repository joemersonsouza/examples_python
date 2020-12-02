import speech_recognition as sr
import voicer_writer as reproducer
import voice_reader as speeker
from ispock import spock_response

def init():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
    return r

if __name__ == "__main__":
    time = 3 #int(input("time to listen: "))
    message = ""
    recognizer = init()
    reproducer.talk("who are you", "Hello, ")
    userName = speeker.listen(recognizer, time)
    while(not userName):
        userName = speeker.listen(recognizer, time)
    reproducer.talk("Wellcome ", userName)
    
    while(True):
        message = speeker.listen(recognizer, time)
        if(message):
            respose, tag = spock_response(message)
            reproducer.talk(respose, userName)
            print(str(tag))
            if(tag == "noanswer"):
                reproducer.talk("Todo google it", userName)
            if(message.find("goodbye") != -1 or message.find("bye") != -1):
                break