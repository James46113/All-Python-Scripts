from tkinter import Tk, Button, Label, filedialog, StringVar, messagebox
from textwrap import fill
from tempfile import mkstemp


def leave():
    with open("Keybinds txt.txt", "w") as f:
        c = 0
        for s in start:
            if c == 0:
                f.write(s)
                c = 1
            else:
                f.write("\n"+s)

    tk.withdraw()
    messagebox.showinfo("Change Keybinds", "The changes will take\nplace after your PC restarts")
    tk.quit()
    tk.destroy()
    quit()


def change(ind):
    global names
    pat = str(filedialog.askopenfile(parent=tk, initialdir='C:\ProgramData\Microsoft\Windows\Start Menu\Programs', title='Please select a file')).split("'")[1]
    if pat != "":
        start[ind] = pat
        names[ind].set(fill(pat.split("/")[-1].split(".")[0], 16))


with open("Keybinds txt.txt", "r") as f:
    start = f.read().split("\n")

ICON = (b'\x00\x00\x01\x00\x01\x00\x10\x10\x00\x00\x01\x00\x08\x00h\x05\x00\x00'
        b'\x16\x00\x00\x00(\x00\x00\x00\x10\x00\x00\x00 \x00\x00\x00\x01\x00'
        b'\x08\x00\x00\x00\x00\x00@\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        b'\x00\x01\x00\x00\x00\x01') + b'\x00'*1282 + b'\xff'*64

_, ICON_PATH = mkstemp()
with open(ICON_PATH, 'wb') as icon_file:
    icon_file.write(ICON)


tk = Tk()
tk.title("Change Keybinds")
tk.iconbitmap(default=ICON_PATH)
tk.protocol("WM_DELETE_WINDOW", leave)

names = [StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar()]
c = 0
for path in start:
    names[c].set(fill(path.split("/")[-1].split(".")[0], 16))
    c += 1

L = Label(text="Select Button to Choose Keybind", font=(None, 13)).grid(row=0, column=0, columnspan=3)
B1 = Button(textvariable=names[0], width=14, height=4, command=lambda: change(0)).grid(row=1, column=0)
B2 = Button(textvariable=names[1], width=14, height=4, command=lambda: change(1)).grid(row=1, column=1)
B3 = Button(textvariable=names[2], width=14, height=4, command=lambda: change(2)).grid(row=1, column=2)
B4 = Button(textvariable=names[3], width=14, height=4, command=lambda: change(3)).grid(row=2, column=0)
B5 = Button(textvariable=names[4], width=14, height=4, command=lambda: change(4)).grid(row=2, column=1)
B6 = Button(textvariable=names[5], width=14, height=4, command=lambda: change(5)).grid(row=2, column=2)
B7 = Button(textvariable=names[6], width=14, height=4, command=lambda: change(6)).grid(row=3, column=0)
B8 = Button(textvariable=names[7], width=14, height=4, command=lambda: change(7)).grid(row=3, column=1)
B9 = Button(textvariable=names[8], width=14, height=4, command=lambda: change(8)).grid(row=3, column=2)
tk.mainloop()