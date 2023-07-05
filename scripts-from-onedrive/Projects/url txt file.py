from urllib import request
from tkinter import Tk, StringVar, Label, CENTER

tk = Tk()
tk.attributes("-fullscreen", True)
string = StringVar()
Label(textvariable=string, font=(None, 100)).place(relx=0.5, rely=0.5, anchor=CENTER)

file = request.urlopen("https://raw.githubusercontent.com/dwyl/english-words/master/words.txt")
for line in file:
    decoded = line.decode("utf-8").split(" ")
    for word in decoded:
        string.set(word)
        tk.update()
