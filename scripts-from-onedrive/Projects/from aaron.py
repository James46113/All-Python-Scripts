from tkinter import *
import webbrowser

def openweb():
    webbrowser.open("https://youtu.be/dQw4w9WgXcQ")

tkWindow = Tk()
tkWindow.geometry("600x400")
tkWindow.title("Hello there")

usernameLabel = Label(tkWindow, text="Type here").grid(row=0, column=1)
usernameEntry = Entry(tkWindow).grid(row=0, column=2)

myButton = Button(tkWindow, text="Click me!", command=openweb).grid(row=0, column=3)

tkWindow.mainloop()