from tkinter import *
from tkinter import filedialog
from time import sleep
from playsound import playsound
from multiprocessing import Process
from pyautogui import click
import ntpath
import os


if __name__ == '__main__':
    window = Tk()
    window.geometry("520x222+500+200")
    window.attributes("-topmost", True)
    window.title("Soundboard")

    def change_default(num):
        click(9, 1051)  # start
        sleep(1.5)
        click(23, 944)  # settings
        sleep(4.5)
        click(232, 288)  # system
        sleep(2)
        click(55, 336)  # sounds
        sleep(1.5)
        click(576, 236)  # output
        sleep(1.5)
        if num == 0:
            click(572, 196)  # line
        else:
            click(572, 280)  # speakers
        sleep(1.5)
        click(1892, 10)  # exit
    
    #change_default(0)
    text = [StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar()]
    for x in range(len(text)):
        text[x].set("Select")
    
    select = [True, True, True, True, True, True, True, True]
    sounds = ["error.mp3", "error.mp3", "error.mp3", "error.mp3", "error.mp3", "error.mp3", "error.mp3", "error.mp3"]
    play = Process(target=print, args=("",))
    play.start()
    
    
    def search_for_file():
        tempdir = filedialog.askopenfilename(parent=window,
            initialdir='C:/James/Python/Projects/Soundboard/Sounds', title='Please select a file',
            filetypes=(("Audio Files", ".wav .mp3"), ("All Files", "*.*")))
        return tempdir
    

    def play_button(num):
        global play, sounds, select, text
        play.terminate()
        if select[num]:
            sounds[num] = search_for_file()
            if os.path.splitext(ntpath.basename(sounds[num]))[0] != "":
                text[num].set(os.path.splitext(ntpath.basename(sounds[num]))[0])
                select[num] = False
        else:
            play = Process(target=playsound, args=(sounds[num],))
            play.start()
    
    
    def wipe():
        global sounds, select, text
        select = [True, True, True, True, True, True, True, True]
        sounds = ["", "", "", "", "", "", "", ""]
        for z in range(len(text)):
            text[z].set("Select")
    
    
    button1 = Button(window, textvariable=text[0], height="4", width="15", command=lambda: play_button(0)).grid(row=0, column=0)
    button2 = Button(window, textvariable=text[1], height="4", width="15", command=lambda: play_button(1)).grid(row=0, column=1)
    button3 = Button(window, textvariable=text[2], height="4", width="15", command=lambda: play_button(2)).grid(row=0, column=2)
    button4 = Button(window, textvariable=text[3], height="4", width="15", command=lambda: play_button(3)).grid(row=0, column=3)
    button5 = Button(window, textvariable=text[4], height="4", width="15", command=lambda: play_button(4)).grid(row=1, column=0)
    button6 = Button(window, textvariable=text[5], height="4", width="15", command=lambda: play_button(5)).grid(row=1, column=1)
    button7 = Button(window, textvariable=text[6], height="4", width="15", command=lambda: play_button(6)).grid(row=1, column=2)
    button8 = Button(window, textvariable=text[7], height="4", width="15", command=lambda: play_button(7)).grid(row=1, column=3)
    wipe_button = Button(window, text="Wipe", height="1", width="65", command=wipe).place(x=0, y=190)
    window.mainloop()
    #change_default(1)
