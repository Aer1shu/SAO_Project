from pyautogui import *
import keyboard
import pyautogui
import time
import random
import win32api, win32con

pyautogui.useImageNotFoundException()

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event (win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    
while keyboard.is_pressed('p')== False:
    try:
        location1 = pyautogui.locateOnScreen('fish.png', confidence=0.80)
        print('image found')
        click (1772, 926)
        time.sleep(0.001)
                
    except pyautogui.ImageNotFoundException:
        time.sleep(0.001)
        
        #location2 = pyautogui.locateOnScreen('exit_button.png', confidence=90)
        #print('Fishing Success, Retrying...')
        #click (1393, 295)
        #time.sleep(3.0)
