from tkinter import *

window = Tk()
window.geometry("600x342+500+200")
file1 = open("C:\\James\\Python\\Projects\\Notes_Project\\notes_1.txt", "r")
title1 = StringVar()
title1.set(file1.readline().strip())
first_line1 = ""


def read_title1():
    global file_title1
    global first_line1
    first_line1 = file_title1.get()
    
    
def open_notes1():
    notes_window = Tk()
    notes_window.geometry("600x342+500+200")
    file_tile1 = Entry(notes_window).place(x=230, y=0)
    get_title = Button(notes_window, text="change", command=read_title1).place(x=350, y=0)
    
    
    file1.writelines(first_line1)
    notes_window.mainloop()


notes_button = Button(textvariable=title1, height="5", width="15", command=open_notes1).grid(row=0, column=0)

window.mainloop()
