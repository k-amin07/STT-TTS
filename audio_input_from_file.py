import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()

r = sr.Recognizer()
hellow=sr.AudioFile('./audio.wav')
with hellow as source:
    audio = r.record(source)
MyText = r.recognize_google(audio)
print("Did you say: " + MyText)

engine.say(MyText)
engine.runAndWait()