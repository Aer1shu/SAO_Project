from pyautogui import *
import keyboard
import pyautogui
import time
import random
import win32api, win32con

time.sleep(5.0)
im1 = pyautogui.screenshot (region = (1480, 188, 50, 600))
im1.save(r"./SS.png")
