import speech_recognition as sr
import os
import webbrowser
import datetime
import random
import pyttsx3

engine = pyttsx3.init()

def say(text):
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold=1
        audio = r.listen(source)
        try:
            query= r.recognize_google(audio, language='en-in')
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some error occurred. Sorry from Jarvis"

if __name__ == '__main__':
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        say("Good Morning")
    elif hour >= 12 and hour < 18:
        say("Good Afternoon")
    else:
        say("Good Evening")
    say("Hello I am Jarvis A.I")
    while True:
        print("Listening...")
        query = takeCommand().lower()
        sites=[["youtube", "https://www.youtube.com"], ["google", "https://www.google.com"], ["wikipedia", "https://www.wikipedia.com"]]
        for site in sites:
            if f"open {site[0]}" in query:
                say(f"Opening {site[0]}")
                webbrowser.open(site[1])

        '''
        Code to open music 
        elif "open music" in query:
        musicPath= " Path will come here"
        os.system(f"open {musicPath}")
        '''

        if "the time" in query:
            strfTime = datetime.datetime.now().strftime("%H:%M:%S")
            say(f"The time is {strfTime}")

        if "the date" in query:
            strfDate = datetime.datetime.now().strftime("%A, %d %B %Y")
            say(f"The date is {strfDate}")

        elif "open facetime" in query:
            os.system(f"open /System/Applications/FaceTime.app")