"""
Audio transcription works by a few steps:

#### How to run:####

## You can run with wav input file 
python speech_recognize_audio_wav_to_text.py wav_test_1.wav 

or 
## or without wav input file 
python final_wav_to_text.py 


input as .wav audio file
output: as text
(Goal feeding the audio file to a speceh recongition system)


"""


import speech_recognition as sr
import sys;
r=sr.Recognizer();
r.energy_threshold = 500

if len(sys.argv)==2:
    filename = sys.argv[1];
    with sr.AudioFile(filename) as source:
        audio=r.listen(source);
else:
    with sr.Microphone() as source:
        print("Speak into microphone")
        audio=r.listen(source);

try:
    print(r.recognize_google(audio));
except Exception as e:
    pass
