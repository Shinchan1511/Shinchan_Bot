import os
import pyttsx3
import datetime
import wikipedia
import webbrowser
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
engine.setProperty('rate', 150)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning sir!")

    elif hour >= 12 and hour < 18:
        speak("Good afternoon sir!")

    else:
        speak("Good Evening sir!")

    speak('I am Shinchan. How may i help you?')


def takecmd():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print("You said", query)

    except:
        engine.say("Can't recognize!. Say that again please...")
        return 'None'

    return query


if __name__ == "__main__":
    wishme()

    while True:
        query = takecmd().lower()

        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace('wikipedia', '')
            result = wikipedia.summary(query, sentences=1)
            speak('According to wikipedia')
            speak(result)

        elif 'open youtube' in query:
            webbrowser.open('www.youtube.com')

        elif 'open google' in query:
            webbrowser.open('www.google.co.in')

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codepath = "C:\\Program Files\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif 'exit' in query:
            speak("Thank u for using me. Have a nice day!.")
            exit()