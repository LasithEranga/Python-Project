import speech_recognition as s
import pyaudio
r = s.Recognizer()
mic  = s.Microphone()
with mic as source:
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
print(r.recognize_sphinx(audio))
