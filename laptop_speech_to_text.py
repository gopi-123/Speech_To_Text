
"""
Speak to laptop and it recognizes your speech and converts to text (displays text output on the screen)

#How to run
$ python laptop_speech_to_text.py


"""

import speech_recognition as sr

r = sr.Recognizer()
r.energy_threshold = 500
with sr.Microphone() as source:
    print("Speak Anything :")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("You said : {}".format(text))
    except:
        print("Sorry could not recognize what you said")
