import speech_recognition as sr

r = sr.Recognizer()


with harvard as source:
    r.adjust_for_ambient_noise(source, duration=0.5)
    audio1 = r.record(source, duration=4)
    
a = r.recognize_google('voice.mp3')