from tkinter import Tk, Label, Button, Entry, CENTER
from textwrap import fill

input_good = False
user_input = ""


def get_input(set: str):
    global user_input
    user_input = set


def ok_press(entry_box_value):
    global input_good, user_input
    if entry_box_value != "":
        input_good = True


def entry(prompt: str):
    global input_good, user_input
    
    tk = Tk()
    tk.attributes('-topmost', True)
    tk.title("Input")
    tk.resizable(0, 0)
    tk.bind("<Return>", lambda e: [ok_press(box.get()), tk.destroy()])
    x, y = 220, 115
    tk.geometry('{}x{}+{}+{}'.format(x, y, tk.winfo_screenwidth()//2-x//2, tk.winfo_screenheight()//2-y//2))
        
    prompt = fill(prompt, 30)
    Label(text=prompt).place(relx=0.5, y=30, anchor=CENTER)
    box = Entry()
    box.place(relx=0.5, y=65, anchor=CENTER)
    Button(text="Ok", width=10, command=lambda: [ok_press(box.get()), tk.destroy()]).place(relx=0.5, y=100, anchor=CENTER)
    
    tk.mainloop()
    if input_good:
        return user_input
    else:
        return "String not set"
