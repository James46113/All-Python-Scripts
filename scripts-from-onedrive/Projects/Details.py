from tkinter import *
from tkinter.ttk import *
from time import sleep
from tkinter.messagebox import showinfo
from random import randint

def on_focus_in(widget, text):
    if widget.get() == text:
        widget.delete(0, "end")
        widget.insert(0, '')


def on_focus_out(widget, text):
    if widget.get() == '':
        widget.insert(0, text)


def do_binds(widget, text):
    widget.insert(0, text)
    widget.bind("<FocusIn>", lambda e: on_focus_in(widget, text))
    widget.bind("<FocusOut>", lambda e: on_focus_out(widget, text))


def bar():
    global nums
    if num.get() != "Card number" and num.get() != "" and pin.get() != "PIN" and pin.get() != "" and cvv.get() != "CVV" and cvv.get() != "":
        get_info()
        tk.destroy()
        n.deiconify()
        prog.place(relx=0.5, rely=0.6, anchor=CENTER)
        check.place(relx=0.5, rely=0.7, anchor=CENTER)
        for x in range(1, 120):
            prog['value'] = x
            tk.update_idletasks()
            sleep(0.1)
            if nums < 532:
                nums += randint(1, 10)
                checking.set(f"Checking database {nums}/1354...")
        n.withdraw()
        showinfo("Card details", "Your card details have not been found")


def get_info():
    c_num = num.get()
    c_pin = pin.get()
    c_cvv = cvv.get()
    print(c_num)
    print(c_pin)
    print(c_cvv)

root = Tk()
root.withdraw()
tk = Toplevel()
tk.geometry('{}x{}+{}+{}'.format(230, 170, tk.winfo_screenwidth() // 2 - 230 // 2,
                                           tk.winfo_screenheight() // 2 - 170 // 2))
tk.title("Detail Checker")

n = Toplevel()
n.withdraw()
n.geometry('{}x{}+{}+{}'.format(230, 170, n.winfo_screenwidth() // 2 - 230 // 2,
                                          n.winfo_screenheight() // 2 - 170 // 2))
n.title("Checking...")

num = Entry(tk)
pin = Entry(tk)
cvv = Entry(tk)
do_binds(num, "Card number")
do_binds(pin, "PIN")
do_binds(cvv, "CVV")
num.place(relx=0.5, y=50, anchor=CENTER)
pin.place(relx=0.5, y=77, anchor=CENTER)
cvv.place(relx=0.5, y=104, anchor=CENTER)

go = Button(tk, text="Go", command=bar)
go.place(relx=0.5, y=131, anchor=CENTER)

Label(tk, text="Enter card details to check if \nthey are in hacker databases").pack()

checking = StringVar()
nums = 0
checking.set(f"Checking database {nums}/1354...")
check = Label(n, textvariable=checking)
prog = Progressbar(n, orient=HORIZONTAL, length=200, mode='determinate')

tk.bind("<Return>", lambda e: bar())

tk.mainloop()