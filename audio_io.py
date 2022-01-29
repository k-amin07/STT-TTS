
import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()
voiceRate = 170
engine.setProperty('rate',voiceRate)
# voices = engine.getProperty('voices')
# [print(voice.id) for voice in voices]
engine.setProperty('voice', 'english+f4')

recognizer = sr.Recognizer()

while(1):
    try:
        with sr.Microphone() as input_source:
            recognizer.adjust_for_ambient_noise(input_source, duration=2) #0.2 works for earphones, because they dont pick up a lot of ambient noise. but for internal speakers, calibrate for 2 seconds
            print("Listening now...")
            audio_input = recognizer.listen(input_source)
            print("Converting speech to text...")
            audio_transcript = recognizer.recognize_google(audio_input)
            audio_transcript = audio_transcript.lower()
            print("Did you say " + audio_transcript)
            engine.say(audio_transcript)
            engine.runAndWait()
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
    except sr.UnknownValueError:
        print("unknown error occured")


# Working config for Arch:
## Family 17h HD Audio controller: Analog Stereo Duplex and probably Analog Surround 4.0 + Analog Stereo Input.
## UC02 (Earphones): Analog Stereo Output + Mono Input.
## Remove /etc/asound.conf

# python3 -m pip install pyttsx3
# python3 -m pip install SpeechRecognition