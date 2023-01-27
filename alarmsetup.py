import datetime
import datefinder
import os
import pyttsx3
from playsound import playsound

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)
engine.setProperty('rate', 125)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("good morning")

    elif 12 <= hour < 18:
        speak("good afternoon")

    else:
        speak("good evening")

    speak("sir its time to get back to reality")
    day = datetime.datetime.now().strftime(" %a ")
    speak("today is " + day)
    time1 = datetime.datetime.now().strftime("%I;%M %p")
    speak(" and the time is" + time1)
    speak("Please tell me how may i help you.")
    playsound('C:\\Users\\User\\PycharmProjects\\practice\\ai sounds\\blip1.wav')


def alarm(text):
    dtime_alarm = datefinder.find_dates(text)
    for match in dtime_alarm:
        print(match)
    alarm_str = str(match)
    alarm_time = alarm_str[11:]
    alarm_hour = alarm_time[:-6]
    alarm_hour = int(alarm_hour)
    alarm_min = alarm_time[3:-3]
    alarm_min = int(alarm_min)

    while True:
        if alarm_hour == datetime.datetime.now().hour:
            if alarm_min == datetime.datetime.now().minute:
                alarm_path = 'C:\\Users\\User\\PycharmProjects\\practice\\alarm sound'
                alarm_sound = os.listdir(alarm_path)
                os.startfile(os.path.join(alarm_path, alarm_sound[0]))
                wishMe()
                break
            elif alarm_min < datetime.datetime.now().minute:
                break
