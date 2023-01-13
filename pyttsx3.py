import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice' , voices[0].id)
engine.say("enna ruzait enna kathe ")
engine.runAndWait()'''

'''from tkinter import *
import pyttsx3

root = Tk()

def fu():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say("testing    testing   testing ")
    engine.runAndWait()
    print("OK!")

b = Button(root,text="-- click me!--",command=fu).pack()

root.mainloop()'''

'''import pyttsx3
import datetime
import speech_recognition as sr             # as sr :- def use paane sr pooddu use pannelaam
                                            # (inthe module pakkenum enda ctrl+mouse click in speech... click pannenum

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say( audio )
    engine.runAndWait()

def wish_me():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am chitty!      my neik name is Riyaa!         i am  you'r assistan Sir.        Please tell me how may I help you")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1      #pesekkole 1 sollukku ideilaane idaiveelai
        audio = r.listen(source)

    try:
        print("Wait for few moments")
        query=r.recognize_google(audio,language='en-us')
        print("user said",query)

    except Exception as e:
        print(e)
        speak("say   that   again   please!")


if __name__ == "__main__":
    wish_me()
    takecommand()