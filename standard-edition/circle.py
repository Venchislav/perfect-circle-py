import pyautogui
import math
import time
time.sleep(7)

# Radius
R = 200
# measuring screen size
(x, y) = pyautogui.size()
# locating center of the screen
(X, Y) = pyautogui.position(x / 2, y / 2)
# offsetting by radius
pyautogui.moveTo(X + R, Y)
pyautogui.mouseDown(button='left')

for i in range(0, 361, 6):
    pyautogui.moveTo(X + R * math.cos(math.radians(i)), Y + R * math.sin(math.radians(i)))
