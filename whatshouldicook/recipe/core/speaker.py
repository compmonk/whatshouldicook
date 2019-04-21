import os
import sys

from gtts import gTTS
from settings import SOUNDS_DIR


def speak(statement):
    print(statement)
    tts = gTTS(text=statement, lang='en')
    tts.save(SOUNDS_DIR.child("output.mp3"))
    os.system("mpg321 -q {0}".format(SOUNDS_DIR.child("output.mp3")))


if __name__ == '__main__':
    if len(sys.argv) == 2:
        speak(sys.argv[1])
    else:
        speak("Hello")
