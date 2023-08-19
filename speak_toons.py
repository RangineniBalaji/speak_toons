
from text_to_speech import text_to_speech
from pydub import AudioSegment
from playsound import playsound

f = text_to_speech()

class speak_toons(object):
    def __init__(self):
        filename = 'middle.wav'
        sound = AudioSegment.from_file(filename, format=filename[-3:])
        sound.export("out.wav", format="wav")
        playsound("out.wav")
if __name__ == '__main__':
    speak_toons()