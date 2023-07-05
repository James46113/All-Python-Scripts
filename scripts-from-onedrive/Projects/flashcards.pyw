from tkinter import *
from random import choice

tk = Tk()
tk.geometry("200x100+600+250")
tk.resizable(False, False)
tk.attributes('-topmost', True)
tk.bind('<Escape>', lambda e: quit())
tk.bind('<Return>', lambda e: get_input())
tk.overrideredirect(True)

side = 0
correct = False
wrong = Label(text="Incorrect", fg="red")


def get_input():
    global correct, cat, side
    entry = entry_box.get()
    if entry == cat[1]:
        cat = choice(info_list)
        info.set(cat[0]+cat[1])
        question.set(cat[2])
        info_side()
        entry_box.delete(0, "end")
        side = 0
        wrong.place_forget()
    else:
        wrong.place(x=70, y=48)
        

def flip():
    global side
    if side == 0:
        question_side()
        side = 1
    else:
        info_side()
        side = 0
    wrong.place_forget()
    entry_box.delete(0, "end")


def info_side():
    entry_box.pack_forget()
    question_label.pack_forget()
    info_label.pack()


def question_side():
    info_label.pack_forget()
    question_label.pack()
    entry_box.pack()


# , ["A  is ", "a ", "What is a ?"]
info_list = [["A verb is ", "an action", "What is a verb?"], ["A noun is ", "a thing", "What is a noun?"]]

cat = choice(info_list)
info = StringVar()
info.set(cat[0] + cat[1])
question = StringVar()
question.set(cat[2])

while True:
    info_label = Label(textvariable=info, font=(None, 13))
    question_label = Label(textvariable=question, font=(None, 13))
    flip_button = Button(text="Flip", width=10, height=1, command=flip)
    check = Button(text="Check")
    entry_box = Entry()
    
    info_side()
    flip_button.place(x=60, y=70)
    tk.mainloop()
