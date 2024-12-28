import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme(key):
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morining!")
    elif hour>=12 and hour<18:
        speak("good afternoon!")
    else:
        speak("good evening!")
    if key=='user':
        speak("i am Mystic. how may i help you")
    elif key=='admin':
        speak("hello sir tell me what to do")


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try :
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"User Said: {query}\n")

    except Exception as e:
        print(e)
        print("Say That Again...")
        return "none"
    return query


speak("Enter your acess key")
print("Enter Your Acess Key")
pwd = input()

if pwd =="wasd" or pwd == 'TrR' :
    if pwd == 'wasd' :
        print("Acess Granted As User")
        speak("Acess Granted As User")
        level = 'user'
        wishme('user')
    
    if pwd == 'TrR' :
        print("Acess Granted As Admin")
        speak("Acess Granted As Admin")
        level = 'admin'
        wishme('admin')

    while True:
        query =  takecommand().lower()

    #logics
        if 'wikipedia' in query:
            speak("searching wikipedia...")
            query = query.replace('wikipedia','')
            results = wikipedia.summary(query,sentences=2)
            speak('according to wikipedia')
            speak(results)
        
        elif 'introduce yourself' in query:
                if level == 'user':
                    speak("I Am Mystic & I Am An A.I Ask Me Anything")
                elif level == 'admin':
                    speak("Hello Sir This Is Mystic Your Friend")

        elif 'youtube' in query:
            if 'search' in query:
                query = query.replace('youtube search ','')
                yt = (f"https://www.youtube.com/results?search_query={query}")
                webbrowser.open(yt)

            else :    
                webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'play music' in query:
            music_dir = 'C:\\tm'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strtime}")
        
        elif 'open vs' in query:
            vspath = "C:\\tm\\Code.exe"
            os.startfile(vspath)

        elif 'open chrome' in query:
            chromepath = "C:\\tm\\chrome.exe"
            os.startfile(chromepath)

        elif 'open spotify' in query :
            spotifypath = "C:\\tm\\spotify.exe"
            os.startfile(spotifypath)

        #for addition

        elif '+' in query :
            ab=[]

            for a in query.split():
                if a.isdigit():
                    ab.append(int(a))

            y = 0

            for p in range(0,len(ab)):
                x = y + ab[p]
                y = x

            speak(y) 

        #for multiplication
        elif 'into' in query :
            ab=[]

            for a in query.split():
                if a.isdigit():
                    ab.append(int(a))

            y = 1

            for p in range(0,len(ab)):
                x = y * ab[p]
                y = x

            speak(y)

        #for division
        elif 'by' in query :
            ab=[]

            for a in query.split():
                if a.isdigit():
                    ab.append(int(a))

            y = ab[0]/ab[1]

            speak(y)

        #for Substraction
        elif '-' in query :
            ab=[]

            for a in query.split():
                if a.isdigit():
                    ab.append(int(a))

            y = ab[0]

            for p in range(1,len(ab)):
                x = y - ab[p]
                y = x

            speak(y)

        elif 'bad liar' in query :
            spath = 'https://open.spotify.com/track/2RSHsoi04658QL5xgQVov3?si=a4150a788b304d85'
            webbrowser.open(spath)

        elif 'runaway' in query :
            s2path = 'https://open.spotify.com/track/1v1oIWf2Xgh54kIWuKsDf6?si=59f1c4aa55b94c9c'
            webbrowser.open(s2path)
        
        elif 'write' in query :
            query = query.replace('write','')
            with open('text\\notes.txt','a') as f :
                f.write(query+'\n')

        elif 'zoom' in query :
            zoompath = 'C:\\Users\\91960\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe'
            os.startfile(zoompath)

        #end
        elif 'sleep' or 'stop' in query :
            break

        else :
            speak("say that again")

else :
    with open('text\\acess.txt','a') as f:
        f.write(f"Some One Tried To Acess With Key '{pwd}'\n")
    speak("Acess denied")
    print("Acess denied")