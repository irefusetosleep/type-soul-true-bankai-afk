#hello penis breath

SOUL_REAPER = True

import subprocess
import time
import pydirectinput
import cv2
import pyautogui
import numpy as np
import random
import os

template = cv2.imread("Raid_Yes.png", cv2.IMREAD_COLOR)

_, w, h = template.shape[::-1]

script_dir = os.path.dirname(os.path.abspath(__file__))
exe_path = os.path.join(script_dir, 'Click.exe')

def search(): #this function seaches for the "Yes" button when called, returns x and y coords of location:wq
    try:
        location = pyautogui.locateCenterOnScreen("Raid_Yes.png", confidence=.5)
        if location is not None:
            return location
    except pyautogui.ImageNotFoundException:
        pass
    
    return (-69, -69)

click_sleep_time = 0.1
click_spam = 20

def click(x, y): #youll never guess what this function does
    print("MOVING MOUSE TO",x,y)

    pyautogui.moveTo(x, y + random.randint(1, 15))
    for i in range(1, click_sleep_time):
        subprocess.run([exe_path]) # SHOULD DO A FUCKING Click 
        time.sleep(click_sleep_time)

print("Starting the macro, tab into roblox.")
time.sleep(3)

time_since_moved = time.time()

time_to_move = 10 * 60 #10 minutes

while True:
    time.sleep(.3)

    if time.time() - time_since_moved > time_to_move:
        time_since_moved = time.time()
        for i in range(1,10):
            pydirectinput.press("Space") #built in anti-afk kick!
            time.sleep(0.1)

    x, y = search()

    if x != -69: #-69 means it didnt find it
        click(x, y)

        if SOUL_REAPER:
            time.sleep(91 - (click_spam * click_sleep_time)) #A raid takes 90 seconds to start
            for i in range(1,20):
                pydirectinput.press("m")
                time.sleep(.01)
            time.sleep(4)
            for i in range(1,20):
                pydirectinput.press("m")
                time.sleep(.01)
    else:
        print("Couldnt find yes button")
        


