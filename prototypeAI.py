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

def rClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP)

# Function to find and click an image with a timeout
def find_and_click_image(image_path, confidence=0.83, timeout=10):
    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            location = pyautogui.locateOnScreen(image_path, grayscale=False, confidence=confidence)
            if location:
                click(1750, 953)
                return True
            time.sleep(0.001)
        except pyautogui.ImageNotFoundException:
            time.sleep(0.001)

    return False

# Main loop function
def main_loop():
    while not keyboard.is_pressed('q'):
        while True:
            if find_and_click_image('fish_start.png', confidence=0.80, timeout=10):
                print("Starting")
                click(1750, 953)
                time.sleep(0.001)
                return 1
                while 1:   
                    if pyautogui.pixel(1513, 689)[2] == 235:
                        print("Bait")
                        click(1750, 953)
                        return 2
                        while True:
                            if find_and_click_image('fish.png', confidence=0.80):
                                print('Reeling')
                        else:
                            return 2
                            break
                    
                break
            else:
                print("Fish start image not found within timeout. Exiting main loop.")
                click(1394, 183)
                break

# Exit loop function
def exit_loop():
            while True:
                if find_and_click_image('fish.png', confidence=0.80, timeout=7):
                    print('Reeling')
                else:
                    print("Restarting...")
                    click(1394, 183)
                    break

# Auto-loop at the beginning
while 2:
    main_loop()
    exit_loop()

