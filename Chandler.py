import pyttsx3
import datetime
from datetime import date
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import pyjokes
import pywhatkit
import alarmsetup
import requests
import sleepmode
from time import sleep
import wolframalpha
import datefinder
import ctypes
from playsound import playsound
import psutil
import listenmode
import json
import socket

REMOTE_SERVER = "1.1.1.1"

client = wolframalpha.Client("UV956G-KPX642YPRL")

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)
engine.setProperty('rate', 115)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def initializing():
    speak("initializing system and databases")
    os.startfile('D:\\testing python projects\\Chandler\\ai sounds\\ui sound.wav')
    speak("backing up the the configurations")
    speak("rendering main control center")
    speak("running deep tests and checking hard disks")
    speak("loading custom components")
    sat_num = ['1', '3', '6', '99', '54', '73', '33', '36', '61', '19', '616']
    speak("setting up connection to satellite number " + random.choice(sat_num))
    sleep(3)
    speak("system initializing completed")
    speak("Importing all packages and preferences from home interface. System's now fully operational and we are good "
          "to go.")
    os.system('TASKKILL /F /IM wmplayer.exe')


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("good morning")

    elif 12 <= hour < 18:
        speak("good afternoon")

    else:
        speak("good evening")

    speak("I am Chandler sir.")
    day = datetime.datetime.now().strftime(" %a ")
    speak("today is " + day)
    time1 = datetime.datetime.now().strftime("%I;%M %p")
    speak(" and the time is" + time1)
    speak("Please tell me how may i help you.")
    playsound('D:\\testing python projects\\Chandler\\ai sounds\\blip1.wav')


def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en')
        print("Luke said: ", query)

    except Exception as e:
        print(e)
        print("Please can you say that again?")
        speak("Please can you say that again")
        return "None"
    return query


def setAReminder(reminder_text):
    global match1
    dtime_reminder = datefinder.find_dates(reminder_text)
    for match1 in dtime_reminder:
        print(match1)
    reminder_str = str(match1)
    reminder_time = reminder_str[11:]
    reminder_hour = reminder_time[:-6]
    reminder_hour = int(reminder_hour)
    reminder_min = reminder_time[3:-3]
    reminder_min = int(reminder_min)

    while True:
        if reminder_hour == datetime.datetime.now().hour:
            if reminder_min == datetime.datetime.now().minute:
                alarm_path = 'D:\\testing python projects\\Chandler\\alarm sound'
                alarm_sound = os.listdir(alarm_path)
                os.startfile(os.path.join(alarm_path, alarm_sound[0]))
                speak("sir you told me to remind you of something")
                speak("here is it sir")
                speak(note_of_reminder)
                break
            elif reminder_min < datetime.datetime.now().minute:
                break


def ScreenOff():
    return ctypes.windll.user32.SendMessageW(65535, 274, 61808, 2)


def ScreenOn():
    return ctypes.windll.user32.SendMessageW(65535, 274, 61808, -1)


def cpu():
    cpu_usage = str(psutil.cpu_percent())
    used_ram = int(psutil.virtual_memory().used)
    ram_usage1 = str(used_ram / 1000000000)
    ram_usage2 = ram_usage1[:4]
    print("cpu is at " + cpu_usage + " %")
    speak("cpu is at " + cpu_usage + "%")
    print("ram is at " + ram_usage2 + " GB")
    speak("ram is at " + ram_usage2 + "GB")


def check_internet_connection():
    try:
        host = socket.gethostbyname(REMOTE_SERVER)
        s = socket.create_connection((host, 80), 2)
        s.close()
        speak("connected to the internet")
        return True
    except:
        speak("not connected to the internet")
        pass
    return False


api_dict = {
    "business": "http://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=c58dddab8c41466e8d9d69c4e5884d16",
    "entertainment": "http://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=c58dddab8c41466e8d9d69c4e5884d16",
    "health": "http://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=c58dddab8c41466e8d9d69c4e5884d16",
    "sports": "http://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=c58dddab8c41466e8d9d69c4e5884d16",
    "science": "http://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=c58dddab8c41466e8d9d69c4e5884d16",
    "technology": "http://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=c58dddab8c41466e8d9d69c4e5884d16"}

if __name__ == '__main__':
    initializing()
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia')
            print("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open google' in query:
            webbrowser.open_new_tab("google.com")

        elif 'play some music' in query or 'play another music' in query or 'play some more music' in query:
            speak("ok sir, surfing through your playlists")
            print("ok sir, surfing through your playlists...")
            sleep(1)
            speak("got it")
            speak("enjoy your music sir")
            speak("please feel free to call me if you need anything")
            music_file = 'F:\\LUKE\\songs'
            songs = os.listdir(music_file)
            random_song = random.choice(songs)
            print(songs)
            os.startfile(os.path.join(music_file, random_song))
            listenmode.listenmode()

        elif 'the time' in query:
            time = datetime.datetime.now().strftime("%I;%M %p")
            speak("sir, the time is" + time)

        elif 'rest' in query or 'quit' in query:
            speak("are you sure,sir")
            confirmation = takeCommand()
            if 'yes' in confirmation or 'yup' in confirmation or 'absolutely' in confirmation or 'yep' in confirmation:
                speak("Starting application shutdown sequence")
                speak("Closing all systems and saving it on a local server sir")
                speak("device disconnected successfully")
                playsound('C:\\Users\\User\\PycharmProjects\\practice\\ai sounds\\blip1.wav')
                quit()
            elif 'no' in confirmation or 'wait' in confirmation:
                speak("ok sir, i am still online")
                playsound('C:\\Users\\User\\PycharmProjects\\practice\\ai sounds\\blip2.wav')
            else:
                speak("ok sir, i am still online")
                playsound('C:\\Users\\User\\PycharmProjects\\practice\\ai sounds\\blip2.wav')

        elif 'are you listening' in query:
            speak("I am all ears, sir")

        elif 'chandler are you there' in query:
            speak("for you sir, always")

        elif 'open stackoverflow' in query:
            webbrowser.open_new_tab("stackoverflow.com")

        elif 'thanks chandler' in query or 'that was good' in query:
            response = ['At your service, sir', 'always ready for you sir', 'it was my pleasure', 'no problem sir',
                        'its okay sir']
            speak(random.choice(response))

        elif 'joke' in query or 'entertain me' in query:
            speak("i think i have something that might amuse you")
            speak(pyjokes.get_joke())

        elif 'open youtube' in query:
            speak("ok sir, what do you want to search youtube for")
            yt_query = takeCommand()
            speak("searching youtube")
            yt_video = yt_query.replace('search youtube for', '')
            pywhatkit.playonyt(yt_video)

        elif 'search google' in query or 'google search' in query:
            speak("ok sir what do you want to search for")
            google_search = takeCommand()
            speak("searching google")
            pywhatkit.search(google_search)

        elif 'say something about you' in query or 'give your introduction' in query or 'introduce yourself' in query or 'tell me something about you' in query:
            theme_path = 'F:\\New folder'
            theme_music = os.listdir(theme_path)
            os.startfile(os.path.join(theme_path, theme_music[0]))
            sleep(5)
            speak("Allow me to introduce myself. I am chandler, a virtual artificial intelligence and i am here to "
                  "assist you with all the tasks as best as i can. I am available 24 hours a day, 7 days a week.")

        elif 'find me a location' in query or 'help me locate' in query or 'open maps' in query:
            speak("please name your location sir")
            location = takeCommand()
            speak("searching google maps")
            speak("hold on i will show you where " + location + " is on the map. ")
            webbrowser.open_new_tab("https://www.google.nl/maps/place/" + location)

        elif 'take a note' in query or 'remember something for me' in query:
            speak("preparing to store data")
            speak("sir what do you need me to remember")
            remember_data = takeCommand()
            speak("saving data to a local server, sir")
            speak("data saved successfully")

        elif 'i told you to remember' in query or 'do i have any notes' in query or 'i tell you to remember' in query or 'i asked you to remember' in query or 'i ask you to remember' in query:
            speak("searching through the database sir, please wait")
            speak("you told me to remember about " + remember_data)

        elif 'alarm' in query:
            speak("ok sir, what time do you want me to set it up")
            alarm_time = takeCommand()
            speak("your alarm is being setup")
            print("your alarm is being setup...")
            speak("sir your alarm is up and running now")
            print("your alarm is up and running now...")
            alarmsetup.alarm(alarm_time)

        elif 'date' in query:
            speak("It is")
            speak(date.today())
            print(date.today())

        elif 'where am i' in query or 'what is my location' in query or 'find my location' in query:
            speak("wait sir, let me check")
            try:
                ipAdd = requests.get('http://api.ipify.org').text
                print(ipAdd)
                url = 'https://get.geojs.io/v1/ip/geo/' + ipAdd + '.json'
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()
                city = geo_data['city']
                country = geo_data['country']
                speak(f"sir i am not sure, i think we are in {city} city of {country}")
            except Exception:
                speak("sorry sir due to network issues i am not able to find our location")
                pass

        elif 'sleep mode' in query:
            speak("initializing sleep mode sequence")
            speak("backing up all data to the servers and saving ongoing instances")
            speak("chandler going into sleep mode sir")
            sleepmode.sleepmode()

        elif 'find out' in query or 'know about something' in query or 'activate alpha mode' in query:
            speak("alpha mode activated")
            playsound('C:\\Users\\User\\PycharmProjects\\practice\\ai sounds\\blip2.wav')
            speak("ok sir, what is it")
            task = takeCommand()
            speak("searching as per your request sir")
            speak("please wait")
            try:
                res = client.query(task)
                search_results = next(res.results).text
                speak("got it")
                speak(search_results)
                print(search_results)
            except:
                speak("sorry sir, due to some technical difficulties i am not able to perform the above task")
                pass

        elif 'reminder' in query:
            speak("absolutely sir, what time do you want me to set it up")
            time_of_reminder = takeCommand()
            speak("and what do you want me to remind you")
            note_of_reminder = takeCommand()
            speak("your reminder is being setup")
            print("your reminder is being setup...")
            speak("sir your reminder is up and running now")
            print("your reminder is up and running now...")
            setAReminder(time_of_reminder)

        elif 'open games folder' in query:
            os.startfile('C:\\Users\\User\\Desktop\\G')

        elif 'close firefox' in query:
            os.system('TASKKILL /F /IM firefox.exe')

        elif 'close brave' in query:
            os.system('TASKKILL /F /IM brave.exe')

        elif 'close vlc' in query:
            os.system('TASKKILL /F /IM vlc.exe')

        elif 'close media player' in query or 'close windows media player' in query:
            os.system('TASKKILL /F /IM wmplayer.exe')

        elif 'turn off the screen' in query or 'turn off screen' in query or 'turn the screen off' in query:
            ScreenOff()

        elif 'turn on the screen' in query or 'turn on screen' in query or 'turn the screen on' in query:
            ScreenOn()

        elif 'cpu usage' in query or 'cpu status' in query:
            cpu()

        elif 'stop listening' in query or 'stop hearing' in query:
            speak("listening mode disabled")
            playsound('C:\\Users\\User\\PycharmProjects\\practice\\ai sounds\\blip2.wav')
            listenmode.listenmode()

        elif 'tell me some news' in query or 'read the news' in query:
            speak("ok sir")
            content = None
            url = None
            print("what type of news do you want to hear?")
            speak("what type of news do you want to hear")
            speak("there is a variety of them")
            print("business, entertainment, health, sports, science and technology")
            speak("business, entertainment, health, sports, science and technology")
            field = takeCommand()
            for key, value in api_dict.items():
                if key.lower() in field.lower():
                    url = value
                    print("url found")
                    print(url)
                    break
                else:
                    url = True
            if url is True:
                print("url not found")

            news = requests.get(url).text
            news = json.loads(news)
            speak("here is the first news")
            news_num = 5
            for articles in news['articles']:
                if news_num > 0:
                    speak(str(articles['title']))
                    print("For more info visit: " + str(articles['url']))
                    speak(str(articles['description']))
                    news_num -= 1
            speak("these were the top headlines for today, thanks and have a good day sir")

        elif 'open headphone settings' in query:
            os.startfile('C:\\Program Files\\RedGear 7.1 GAMING HEADSET\\CPL\\FaceLift_x64.exe')

        elif 'close headphone settings' in query:
            os.system('TASKKILL /F /IM FaceLift_x64.exe')

        elif 'check internet connection' in query:
            speak("proceeding to check internet connection")
            check_internet_connection()

        elif 'check internet speed' in query:
            speak("proceeding to check internet speed")
            webbrowser.open_new_tab("https://fast.com/")

        elif 'open c folder' in query:
            os.startfile('C:')

        elif 'open d folder' in query:
            os.startfile('D:')

        elif 'open e folder' in query:
            os.startfile('E:')

        elif 'open f folder' in query:
            os.startfile('F:')

        elif 'close the folder' in query:
            os.system('TASKKILL /F /IM explorer.exe')
