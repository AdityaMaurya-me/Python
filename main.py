import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLib

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()


def processCommand(c):
    if "open google" in c.lower:
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower:
        webbrowser.open("https://youtube.com")
    elif "open pinterest" in c.lower:
        webbrowser.open("https://pinterest.com")
    elif c.lower.startswith("play"):
        song = c.lower().split(" ")[1]
        link =musicLib.music[song]
        webbrowser(link)

if __name__ == "__main__":
    speak("Initializing Jarvis...")
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source, timeout=5)

        print("recognizing...")
        try: 
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=5, phrase_time_limit=1)

            word = r.recognize_google(audio)
            if(command.lower() == "jarvis"):
                speak("Yes")
                with sr.Microphone() as source:
                    print("Listening...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)

        except Exception as e:
            print("Error: {0}".format(e))