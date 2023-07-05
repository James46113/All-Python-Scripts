from pyautogui import click
from tkinter import Tk
from time import sleep
root = Tk()
sleep(10)
while True:
    sleep(2)
    click(int(root.winfo_pointerx()), int(root.winfo_pointery()), duration=0.5)
