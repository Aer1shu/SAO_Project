import time
import keyboard
import pyautogui
import win32api
import win32con

# Function to simulate a mouse click
def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

# Function to simulate a right mouse click
def rClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP)

# Function to find and click an image with a timeout
def find_and_click_image(image_path, confidence=0.83, timeout=10):
    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            location = pyautogui.locateOnScreen(image_path, grayscale=True, confidence=confidence)
            if location:
                click(1750, 953)
                return True
            time.sleep(0.001)
        except pyautogui.ImageNotFoundException:
            time.sleep(0.001)

# Main loop function
def main_loop():
    while not keyboard.is_pressed('q'):
        # Starting
        if find_and_click_image('fish_start.png', timeout=20):
            print("Starting...")
            click(1750, 953)
            break
        else:
            print("Restarting...")
            click(1394, 183)
            break
        
def exit_loop():
    while True:
        if find_and_click_image('bait.png',confidence=0.90):
            print("Baiting...")
            click(1750, 953)
            break
        else:
            print("Bait Lost/Failed to Cast")
            break
        
    while True:
        if find_and_click_image('fish.png', confidence=0.80, timeout=7.5):
            print('Reeling...')
        else:
            print("Fishing Successful, Restarting...")
            click(1394, 183)
            break

# Auto-loop at the beginning
while True:
    main_loop()
    exit_loop()
