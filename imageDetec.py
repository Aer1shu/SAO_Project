import pyautogui
import time
import keyboard
import random
import win32api, win32con

if keyboard.is_pressed('w') == False:
    res = pyautogui.locateOnScreen("bar.png")
    print(res)
    time.sleep(0.5)
