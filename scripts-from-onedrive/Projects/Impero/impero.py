from tkinter import Tk, Label, PhotoImage, CENTER


def no_op():
    pass


tk = Tk()
tk.attributes("-fullscreen", True)
tk.attributes("-topmost", True)
tk.protocol("WM_DELETE_WINDOW", no_op)
tk.bind("<Shift-1>", lambda e: quit())
tk.config(bg="#b4b4b4")
tk.config(cursor="None")
img = PhotoImage(file="Impero_logo.png")
Label(image=img, bd=0).place(relx=0.5, y=30, anchor=CENTER)

Label(text="This computer has been locked by an Impero Policy", font=(None, 20), fg="#ff0000", bg="#b5b5b5").place(relx=0.5, rely=0.5, anchor=CENTER)
tk.mainloop()
