from tkinter import *


def convert(event):
    if choice1.get() != choice2.get():
        amount = float(entry1.get('1.0', END))
        from_currency = rates[OPTIONS.index(choice1.get())]
        to_currency = rates[OPTIONS.index(choice2.get())]
        amount /= from_currency
        amount = round(amount * to_currency, 2)
        entry2.delete('1.0', "end")
        entry2.insert('1.0', amount)
    
    
def swap(event):
    ent1 = entry1.get('1.0', END)
    ent2 = entry2.get('1.0', END)
    entry1.delete('1.0', "end")
    entry2.delete('1.0', "end")
    entry1.insert('1.0', ent2)
    
    
    
OPTIONS = [
    "USD",
    "EUR",
    "YEN",
    "GBP"
]

rates = [1.32, 1.11, 137.9, 1]

tk = Tk()
x, y = 330, 270
tk.geometry('{}x{}+{}+{}'.format(x, y, tk.winfo_screenwidth()//2-x//2, tk.winfo_screenheight()//2-y//2))
choice1 = StringVar()
choice1.set(OPTIONS[3])
choice2 = StringVar()
choice2.set(OPTIONS[1])


entry1 = Text(width=5, height=1, font=(None, 30))
entry2 = Text(width=5, height=1, font=(None, 30))
om1 = OptionMenu(tk, choice1, *OPTIONS, command=convert)
om2 = OptionMenu(tk, choice2, *OPTIONS, command=convert)

swap_label = Label(text="⮀", font=(None, 30))
swap_label.bind("<Button-1>", swap)

entry1.place(x=60, rely=0.5, anchor=CENTER)
entry2.place(x=260, rely=0.5, anchor=CENTER)
swap_label.place(x=140, rely=0.4)
om1.place(x=60, rely=0.65, anchor=CENTER)
om2.place(x=260, rely=0.65, anchor=CENTER)

tk.mainloop()