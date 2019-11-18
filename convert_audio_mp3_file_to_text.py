"""
Audio transcription works by a few steps:


input: .mp3 file
output: .wav file ++ text recognized ouput



How it works:
first converts mp3 to wav conversion,
loading the audio file,
feeding the audio file to a speech recongition system


"""


import speech_recognition as sr
from os import path
from pydub import AudioSegment

# convert mp3 file to wav                                    

mp3_filename = "test_1.mp3"
sound = AudioSegment.from_mp3(mp3_filename)
sound.export("transcript.wav", format="wav")


# transcribe audio file                                                         
AUDIO_FILE = "transcript.wav"

# use the audio file as the audio source                                        
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)  # read the entire audio file                  

        print("Transcription: " + r.recognize_google(audio))
