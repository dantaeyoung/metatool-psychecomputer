# run "pip install pygame" in terminal
# make sure you're in the same folder as this file!

from pygame import mixer
import time

mixer.init()
s = mixer.Sound('./bell.mp3')
s.play()
time.sleep(2)