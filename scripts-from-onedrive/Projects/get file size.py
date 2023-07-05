from pathlib import Path
from tkinter import Tk, Label, CENTER, StringVar

root = Tk()
root.overrideredirect(True)
root.wm_attributes('-topmost', True)
root.geometry("200x100+1200+-40")
root.config(bg="red")
root.wm_attributes("-transparentcolor", "red")
gb = StringVar()
Label(textvariable=gb, width=15, bg="#5a5a5a", fg="#ffffff", font=(None, 13)).place(relx=0.5, rely=0.5, anchor=CENTER)
while True:
    gb.set(str(int(Path("C:\\Fibonacci Sequence\\fibonacci2.txt").stat().st_size)/1000000000) + " GB")
    root.update()
