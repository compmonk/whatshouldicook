import speech_recognition as sr
import os

from .settings import SOUNDS_DIR


def listen(beep=True):
    r = sr.Recognizer()
    m = sr.Microphone()
    text = ""
    try:
        print("A moment of silence, please...")
        with m as source:
            r.adjust_for_ambient_noise(source)
        print("Set minimum energy threshold to {}".format(r.energy_threshold))
        if beep:
            os.system("mpg321 -q {0}".format(SOUNDS_DIR.child("list.mp3")))
            os.system("mpg321 -q {0}".format(SOUNDS_DIR.child("beep.mp3")))
        print("listening ...")
        with m as source:
            audio = r.listen(source)
        print("Got it! Now to recognize it...")
        try:
            # recognize speech using Google Speech Recognition
            text = r.recognize_google(audio)
            print(text)
            # # we need some special handling here to correctly print unicode characters to standard output
            # if str is bytes:  # this version of Python uses bytes for strings (Python 2)
            #     print(u"You said {}".format(value).encode("utf-8"))
            # else:  # this version of Python uses unicode for strings (Python 3+)
            #     print("You said {}".format(value))
        except sr.UnknownValueError:
            print("Oops! Didn't catch that")
        except sr.RequestError as e:
            print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
    except KeyboardInterrupt:
        pass
    return text


if __name__ == '__main__':
    print(listen())
