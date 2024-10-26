import speech_recognition as sr
import pyttsx3
import pyjokes
import datetime
import pyaudio
import wikipedia as wiki
import pywhatkit as pymus


# Speech Recognition

recognizer = sr.Recognizer()

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

hello = "How can I help ya?"
goodbye = "See ya later!"
action = ""
engine.say(hello)
engine.runAndWait()

def google_api():
    try: 
        with sr.Microphone() as source:
            print("Listening...")
            audio = recognizer.listen(source)

        text = recognizer.recognize_google(audio)
        text = text.lower()
        print("recogonized text: *", text)
    except sr.UnknownValueError:
        print("I don't know what you're saying!")
        text = "Speech Error!"
 
    return text

def interactions():
    text = google_api()

    if "joke" in text:
        joke = pyjokes.get_jokes()
        engine.say(joke)
        engine.runAndWait()

    elif "date" in text:
            currentDate = datetime.datetime.now().strftime('%A %d %B %Y')
            engine.say("Today is:" + currentDate)
            engine.runAndWait()

    elif "who is" in text:
        user = text.replace("who is", "")
        wiki_sum = wiki.summary(user, sentences=2)
        engine.say(wiki_sum)
        engine.runAndWait()

    elif "play" in text:
        song = text.replace("play", "")
        engine.say("Playing" + song)
        pymus.playonyt(song)
        text = "quit"
    
    return text


while action != "quit":
    action = interactions()
else:
    engine.say(action)
    engine.runAndWait()

