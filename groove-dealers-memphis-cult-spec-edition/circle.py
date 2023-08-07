import pyautogui
import math
import time
from pygame import mixer

mixer.init()
mixer.music.load('ez.mp3')

time.sleep(7)

# Radius
R = 200
# measuring screen size
(x, y) = pyautogui.size()
# locating center of the screen
(X, Y) = pyautogui.position(x / 2, y / 2)
# offsetting by radius
pyautogui.moveTo(X + R, Y)
mixer.music.play()
pyautogui.mouseDown(button='left')
for i in range(0, 361, 6):
    pyautogui.moveTo(X + R * math.cos(math.radians(i)), Y + R * math.sin(math.radians(i)))

while True:
    pass