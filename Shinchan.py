''' following libraries should be installed before running the code
    along with webdrivers of your webbrowsers
    
    you can find webdriver for your browser by seaching "<yourbrowsername> webdrivers download" '''


import os
import pyttsx3                              #pip install pyttsx3
import smtplib                              #pip install smtplib
import datetime     
import wikipedia                            #pip install wikipedia
import playsound                            #pip install playsound
import webbrowser                           #pip install webbrowser
import pywhatkit as kit                     #pip install pywhatkit
import speech_recognition as sr             #pip install speech_recognition
from googletrans import Translator          #pip install googletrans
from email.message import EmailMessage

translator = Translator()                   # initializing object for Translator() func
engine = pyttsx3.init('sapi5')              # initializing object for text to speech module
engine.setProperty('rate', 140)             # setting up rate (words per minute)
voices = engine.getProperty('voices')       # getting available voices in system 
engine.setProperty('voice', voices[0].id)   # setting up voice i.e. male/female


def speak(audio):                           # defining func for audio output
    engine.say(audio)                       # voice output
    engine.runAndWait()                     # delay


def wishme():                                   # defining wishme func which when started wishes the user acc to the real time                                               
    hour = int(datetime.datetime.now().hour)    # storing current value of hour in var
    if hour >= 0 and hour < 12:                 # comparing hour with diff time period to wish accordingly
        speak("Good morning sir!")

    elif hour >= 12 and hour < 18:
        speak("Good afternoon sir!")

    else:
        speak("Good Evening sir!")

    speak('I am Shinchan. How may i help you?')


def takecmd():                                  # defining func to take input as voice
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 0.5                 # waiting time before the a sentence meant to be completed
        audio = r.listen(source)

    try:                                        # recognizing the given input 
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print("You said", query)

    except:
        engine.say("Can't recognize!. Say that again please...")
        return 'None'

    return query


def mail(reciever):                             # defining mail func to send emails
    mails = {                                   # initializing dict to store recievers emails
        "name":"email id",
        "name":"email id",
        "name":"email id"
        }

    EMAIL = "your gamil id"                     # taking sender's email address
    PASSWORD = "password"                       # sender's login password

    msg = EmailMessage()

    if reciever in mails:                       # checking for the reciever in the mails dict
        RECIEVER = mails[reciever]

    else:
        speak("reciever don't found. Enter email address below")        # taking email manually if user not found
        RECIEVER = input("please enter reciever's address manually")
    #msg['Subject'] = 'Email using python'
    msg['From'] = EMAIL
    msg['To'] = RECIEVER

    speak("please tell the message to send")    # taking message as voice input to send
    message = takecmd()
    msg.set_content(message)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:               # sending email...
        smtp.login(EMAIL, PASSWORD)
        smtp.send_message(msg)

    speak("mail sent successfully")

def whatmsg(Reciever):                          # defining func to send whatsapp msgs
    contacts = {                                # using dict to store name and phone no. of the recievers
        "name": "phone no.",                    # more no. can be added with country code ex +91 for India
        "name": "phone no."
    }

    if Reciever in contacts:                    # checking reciever in contacts
        RECIEVER = contacts[Reciever]

    else:
        speak("reciever number not found")
        RECIEVER = str(input("please enter reciever's address manually"))

    speak("please tell the message to send")    # taking msg to send as voice input
    message = takecmd()

    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    lst = strTime.split(":")
    conlst = [int(i) for i in lst]
    if conlst[1] >= 0 and conlst[1] < 58:
        conlst[1] += 2
    
    elif conlst[1] > 58:
        conlst[0] += 2
        
    kit.sendwhatmsg(RECIEVER,message,conlst[0],conlst[1])       # sending msg
    speak("message sent successfully")

if __name__ == "__main__":
    wishme()

    while True:
        query = takecmd().lower()

        if 'wikipedia' in query:               # searching wikipedia for given query(must tell wikipedia before or after the query)
            speak('Searching wikipedia...')
            query = query.replace('wikipedia', '')
            result = wikipedia.summary(query, sentences=1)  # initializing the length of the result/sentences shown 
            speak('According to wikipedia')     # result of the query searched voice output  
            speak(result)

        elif 'send email' in query:                     # query to send email (speak 'send email' to activate this)
            speak("whom do you want to send email to")  # taking recievers name as voice input
            rc = takecmd().lower()
            mail(rc)

        elif 'send whatsapp message' in query:          # query to send whatsapp msgs (speak 'send whatsapp msg' to activate)
            speak("whom do you want to send message to")# taking recievers name as voice input
            rc = takecmd().lower()
            whatmsg(rc)

        elif ' open youtube' in query:                        # query to open youtube website
            webbrowser.open("www.youtube.com")

        elif 'google' in query:                         # query to search on google (speak 'google' before or after the query)
            query = query.replace('google', '')
            speak("Searching google...")
            kit.search(query)

        elif 'translate' in query:                      # query to translate given input into another lang
            query = query.replace('translate', '')
            ''' this queary translate hindi to english
                to change langs replace 'hi' to source lang and
                'en' to the lang in which you want to translate
                
                note: currently only hindi to english is available for voice output
                but u can get output in text form ''' 
            result = translator.translate(query, src = 'hi', dest = 'en')
            speak(result.text)
            print(result.text)

        elif 'time' in query:           # it tells the current time
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:      # query to open vs code
            codepath = "file path of vs code"
            os.startfile(codepath)

        ''' you can add as many as files, folders, apps to this
            just copy paste the above code and change the query and filepath'''

        elif 'poem' in query:
            ''' query to paly music 
             to play music replace 'poem' with 'play music' and 'Shinchan.mp3' to song name (if stored in same directory)
              or complete filepath of the song'''
            playsound.playsound("Shinchan.mp3")

        elif 'exit' in query:           # to exit the assistent
            speak("Thank u for using me. Have a nice day!.")
            exit()