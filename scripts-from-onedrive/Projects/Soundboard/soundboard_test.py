import ntpath
import tkinter as tk
from tkinter import filedialog

from playsound import playsound

go = True
sounds = []


def search_for_file():
    tempdir = filedialog.askopenfilename(parent=root,
        initialdir='C:/James/Python/Projects/Soundboard/Sounds', title='Please select a file')
    return tempdir


def play():
    global go, sounds
    if go:
        print("bye")
        the_sound = search_for_file()
        sounds.append(the_sound)
        # if os.path.splitext(ntpath.basename(sounds[1]))[0] != "":
        #    text2.set(os.path.splitext(ntpath.basename(sounds[1]))[0])
        go = False
    else:
        playsound(sounds[button_label_list[0][1]])
        print("hi")


def dump():
    global count, button_label_list, go
    go = True
    button_label_list.append([tk.Button(frame, text="play", command=lambda: play()), count])
    button_label_list[-1][0].grid(row=0, column=count)  # , sticky='nsew')
    frame.columnconfigure(count, weight=1)
    count += 1


root = tk.Tk()
count = 0
button_label_list = []
root.title("Hello")
root.rowconfigure(1, weight=1)
root.columnconfigure(2, weight=1)

frame = tk.Frame(root)
frame.rowconfigure(1, weight=1)
frame.grid(row=0, column=2, sticky='nsew', rowspan=2)

tk.Button(root, text="button", command=dump).grid(row=0, column=0)#, sticky='nsew')
tk.Button(root, text="Quit!", command=root.quit).grid(row=0, column=1)#, sticky='nsew')

root.mainloop()
