from time import sleep
import speech_recognition as sr
import pyttsx3
from playsound import playsound

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)
engine.setProperty('rate', 130)


def Speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en')
        print("Luke said: ", query)

    except Exception as e:
        print(e)
        return "None"
    return query


def sleepmode():
    wakeup_call = takecommand()
    while True:
        if 'wake up' in wakeup_call:
            Speak("turning on the system and backing up data from server sir")
            Speak("it may take a few seconds")
            sleep(3)
            Speak("we are now good to go")
            playsound('C:\\Users\\User\\PycharmProjects\\practice\\ai sounds\\blip1.wav')
            break
        else:
            print("still in sleep mode sir")
            sleepmode()
            break
