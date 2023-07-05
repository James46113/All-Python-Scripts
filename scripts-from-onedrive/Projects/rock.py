from tkinter import *
from random import choice
from time import sleep

tk = Tk()
tk.geometry("240x150+800+400")
tk.title("Rock Paper Scissors")
tk.bind("<Return>", lambda e: guess(entry_box.get().strip().lower()))
tk.attributes('-topmost', True)

tk2 = Tk()
tk2.geometry("240x150+800+400")
tk2.title("Rock Paper Scissors")
tk2.bind("<Return>", lambda e: tk2.withdraw())
tk2.attributes('-topmost', True)
tk2.withdraw()


pos = ["rock", "paper", "scissors"]

u_win_label = Label(tk2, text="You win", font=(None, 20), fg="green")
c_win_label = Label(tk2, text="Computer wins", font=(None, 20), fg="green")
draw_label = Label(tk2, text="Draw", font=(None, 20))


u_score = IntVar()
u_score.set(0)
c_score = IntVar()
c_score.set(0)


Label(tk, text="You: ").place(x=0, y=-1)
Label(tk, text="Computer: ").place(x=165, y=-1)
u_score_label = Label(tk, textvariable=u_score)
u_score_label.place(x=26, y=0)
c_score_label = Label(tk, textvariable=c_score)
c_score_label.place(x=225, y=0)


def wipe():
    c_score.set(0)
    u_score.set(0)
    

def guess(u_guess):
    global u_score, c_score

    draw_label.place_forget()
    c_win_label.place_forget()
    u_win_label.place_forget()


    draw = False
    c_win = False
    u_win = False

    c_guess = choice(pos)
    
    if c_guess == "rock" and u_guess == "rock":
        draw = True
    elif c_guess == "paper" and u_guess == "paper":
        draw = True
    elif c_guess == "scissors" and u_guess == "scissors":
        draw = True

    if c_guess == "rock" and u_guess == "paper":
        u_win = True
    elif c_guess == "paper" and u_guess == "scissors":
        u_win = True
    elif c_guess == "scissors" and u_guess == "rock":
        u_win = True

    if c_guess == "paper" and u_guess == "rock":
        c_win = True
    elif c_guess == "scissors" and u_guess == "paper":
        c_win = True
    elif c_guess == "rock" and u_guess == "scissors":
        c_win = True
        
    if draw:
        tk2.deiconify()
        draw_label.place(x=85, y=50)
    if c_win:
        tk2.deiconify()
        temp = c_score.get()
        c_score.set(temp+1)
        c_win_label.place(x=22, y=50)
        c_score_label.update()
    if u_win:
        tk2.deiconify()
        temp = u_score.get()
        u_score.set(temp+1)
        u_win_label.place(x=70, y=50)
        u_score_label.update()
    entry_box.delete(0, "end")
    tk2.focus()

    
entry_box = Entry(tk)
entry_box.place(x=50, y=34)
entry_box.focus()

Button(text="Reset", command=wipe).place(x=100, y=100)


tk.mainloop()
