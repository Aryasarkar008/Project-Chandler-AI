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


def listenmode():
    listen_call = takecommand()
    while True:
        if 'start listening' in listen_call or 'come back online' in listen_call or 'hey Chandler' in listen_call:
            Speak("listening mode enabled")
            playsound('C:\\Users\\User\\PycharmProjects\\practice\\ai sounds\\blip2.wav')
            break
        else:
            print("listening mode is disabled...")
            listenmode()
            break
