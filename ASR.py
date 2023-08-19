
import pyaudio
import wave
import assemblyai as aai

from main_functions import *



class asr(object):
    def __init__(self):
        aai.settings.api_key = "1669637f8e0444419cf1d11bbc6f2013"
        transcriber = aai.Transcriber()
        transcript = transcriber.transcribe("test.wav")
        self.text = transcript.text
       
if __name__ == '__main__':
    asr()