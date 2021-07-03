#!/usr/bin/python
from pynput import keyboard
from pydub import AudioSegment
from pydub.playback import play
import threading
import random

song = AudioSegment.from_wav("1.wav")
song1 = AudioSegment.from_wav("119134__esperri__keyboard-key.wav")

class thread(threading.Thread):
    def __init__(self, thread_name, thread_ID):
        threading.Thread.__init__(self)
        self.thread_name = thread_name
        self.thread_ID = thread_ID

    def run(self):
        play(song)
        # self.join()
        

def on_press(key):    
    try:
        # print('Alphanumeric key pressed: {0} '.format(key.char))
        thread1 = thread("abc", int(random.randint(1000, 10000)))
        thread1.start()

    except AttributeError:
        print('special key pressed: {0}'.format(key))
        # play(song1)


def on_release(key):
    # print('Key released: {0}'.format(key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False


# Collect events until released
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
