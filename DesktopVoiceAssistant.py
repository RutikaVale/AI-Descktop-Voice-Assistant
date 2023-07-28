import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')
print(voices[1].id)

engine.setProperty('voice', voices[2].id)

def speak (audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning sir!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon sir!")

    else:
        speak("good Evening sir! ")

    speak("I am Angel. please tell me how may I help you")


def takeCommand():
    #it takes microphone input from the user and return string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language= 'en-in')
        print(f"User Said: {query}\n") 


    except Exception as e:
        print(e) 
        speak(("Say that again please"))
        print("Say that again please...")
        return "None"   


    return query
     
def sendEmail(to, content): 
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('djsonu96.edu@gmail.com', 'failmylove9')
    server.sendmail('djsonu96.edu@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    #if 1:
        query = takeCommand().lower()
    
        #logic for executing takes based on query

        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace('wikipedia', "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'youtube' in query:
            webbrowser.open("https://www.youtube.com/")

        elif 'gmail' in query:
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")

        elif 'google' in query:
            webbrowser.open("https://www.google.co.in/?gws_rd=ssl")

        elif 'facebook' in query:
            webbrowser.open("https://www.facebook.com/")
        
        elif 'stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'weather' in query:
            webbrowser.open("https://www.google.com/search?q=weather&rlz=1C1CHBD_enIN937IN937&oq=weather&aqs=chrome..69i57j0i67i395i457j0i395i402l2j0i20i263i395j0i67i395j69i60l2.2950j1j7&sourceid=chrome&ie=UTF-8")

        elif 'music' in query:
            music_dir = 'E:\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'what is time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strtime)
            speak(f"Sir, the time is {strtime}")

        elif 'vs code' in query:
            codePath = "C:\\Program Files\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'notepad' in query:
            notePad = "%windir%\\system32\\notepad.exe"
            os.startfile(notePad)

        elif 'ms word' in query:
            pWord = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
            os.startfile(pWord)

        elif 'excel' in query:
            msExcel = "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
            os.startfile(msExcel)

        elif 'power point' in query:
            pP = "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
            os.startfile(pP)

        elif 'wordpad' in query:
            wordPad = "%ProgramFiles%\\Windows NT\\Accessories\\wordpad.exe"
            os.startfile(wordPad)

        elif 'chrome' in query:
            pChrome = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(pChrome)   

        elif 'opera' in query:
            pGX = "C:\\Users\\Sonu\\AppData\\Local\\Programs\\Opera GX\\launcher.exe"
            os.startfile(pGX)

        elif 'pycharm' in query:
            pyCharm = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.3.3\\bin\\pycharm64.exe"
            os.startfile(pyCharm)

        elif 'how are you' in query:
            speak("I am fine what about you")
            print('I am fine what about you')

        elif 'i am good' in query:
            speak("ok fine. how may I help you. what i do for you")

        elif 'what are you doing' in query:
            speak("now i am listening a songs")

        elif 'which type of songs' in query:
            speak('i am listening my favorite songs')

        elif 'can you play for me' in query:
            speak("yes sure, why not")
            music_dir = 'E:\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'email' in query:
            try:
                speak("what should i say ?")
                content = takeCommand()
                to = "djsonu96@gmail.com"
                sendEmail(to, content)
                speak("Email has been send!")
            except Exception as e:
                print(e)
                speak("sorry i am not able to send email")
                   


        elif 'shutdown my computer' in query:
            speak("do you want to switch off your computer")
            take = takeCommand().lower()
            
            
            if 'yes' in take:
                print("Shutting Down The Computer")
                speak("Shutdown your computer")
                os.system("shutdown /s /t 30")
                
            if 'no' in take:
                print("Thank you for confirmation")
                speak("Thank you for confirmation")

        elif 'restart my system' in query:
            speak("do you want to Restart your computer")
            take = takeCommand().lower()
            
            
            if 'yes' in take:
                print("Restart your Computer")
                speak("Restart your computer")
                os.system("shutdown /r /t 30")
                
            if 'no' in take:
                print("Thank you for confirmation")
                speak("Thank you for confirmation")


        elif ('stop') in query:
            exit()

        elif ('quit') in query:
            exit()

        elif ('exit') in query:
            exit()