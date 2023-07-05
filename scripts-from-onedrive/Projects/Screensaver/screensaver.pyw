from PIL import ImageTk
from tkinter import *
from random import choice
from datetime import datetime


def press():
    global not_pressed
    not_pressed = False


tk = Tk()
tk.attributes('-topmost', True)
tk.attributes('-fullscreen', True)
tk.bind('<KeyPress>', lambda e: press())
tk.configure(bg="black", cursor='none')

not_pressed = True
time = 5
x, y, xv, yv = 0, 0, 0.5, 0.5

images = [ImageTk.PhotoImage(file='screen-0.jpg'), ImageTk.PhotoImage(file='screen-1.jpg'),
          ImageTk.PhotoImage(file='screen-2.jpg'), ImageTk.PhotoImage(file='screen-3.jpg'),
          ImageTk.PhotoImage(file='screen-4.jpg')]

while True:
    go_again = True
    not_pressed = True
    while go_again:
        go_again = False
        now = datetime.now()
        start_time = int(now.strftime("%H%M%S"))
        time_elapsed = 0
        mouse_x = tk.winfo_pointerx()
        mouse_y = tk.winfo_pointery()
        while time_elapsed < time:
            now = datetime.now()
            time_elapsed = int(now.strftime("%H%M%S")) - start_time
            if mouse_x != tk.winfo_pointerx() and mouse_y != tk.winfo_pointery():
                go_again = True
                break
    try:
        dvd.destroy()
    except NameError:
        pass

    img = choice(images)
    dvd = Label(image=img, borderwidth=0, highlightthickness=0)
    tk.deiconify()
    
    while mouse_x == tk.winfo_pointerx() and mouse_y == tk.winfo_pointery() and not_pressed:
        dvd.destroy()
        dvd = Label(image=img, borderwidth=0, highlightthickness=0)
        
        y += yv
        x += xv
        
        if x > 1295 or x < -30:
            xv *= -1
            prev = img
            while img == prev:
                img = choice(images)
        
        if y > 690 or y < -25:
            yv *= -1
            prev = img
            while img == prev:
                img = choice(images)
        
        dvd.place_forget()
        dvd.place(x=x, y=y)
        tk.update()
    tk.withdraw()

