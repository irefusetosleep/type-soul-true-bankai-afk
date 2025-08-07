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
        print("Image not found, retrying")

    return (-69, -69)    
    
def click(x, y): #youll never guess what this function does
    print("Clicking yes")
    print("MOVING MOUSE TO",x,y)
    for i in range(1, 5):
        pyautogui.moveTo(x + random.randint(-15, 15), y)
        subprocess.run([exe_path]) # SHOULD DO A FUCKING CLICK
        time.sleep(.2)

print("Starting the macro, tab into roblox.")
time.sleep(3)

time_since_moved = time.time()

time_to_move = 10 * 60 #15 minutes

while True:
    time.sleep(.1)

    if time.time() - time_since_moved > time_to_move:
        pydirectinput.press("Space") #built in anti-afk kick!
        time_since_moved = time.time()

    x, y = search()

    if x != -69: #-69 means it didnt find it
        click(x, y)

        if SOUL_REAPER:
            time.sleep(90) #A raid takes 90 seconds to start
            pydirectinput.press("m")
            time.sleep(5)
            pydirectinput.press("m")
    else:
        print("Couldnt find yes button")
        


