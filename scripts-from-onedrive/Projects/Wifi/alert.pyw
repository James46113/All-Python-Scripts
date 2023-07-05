from tkinter import Tk, Label, Entry, StringVar, CENTER, TclError
from datetime import datetime
import smtplib, ssl
from time import sleep


def check(event):
    password = ""
    for num in [83, 97, 110, 100, 50, 48, 50, 48]:
        password += chr(num)
        
    if e.get() == password and event.keysym == "Return":
        tk.destroy()
    if event.keysym == "Escape":
        time_left = 0


now = datetime.now()

tk = Tk()
tk.geometry('{}x{}+{}+{}'.format(230, 130, tk.winfo_screenwidth()//2-230//2, tk.winfo_screenheight()//2-130//2))
tk.overrideredirect(True)
tk.config(bg="black")
tk.attributes('-topmost', True)
tk.bind("<KeyPress>", check)

time_left = 21

alert_var = StringVar()
alert_var.set(f"Alert will be sent in {time_left}s")
l = Label(tk, textvariable=alert_var, bg="black", fg="red", font=(None, 15))
l.place(relx=0.5, y=30, anchor=CENTER)
e = Entry(tk, bg="black", fg="white", show="*")
e.place(relx=0.5, y=70, anchor=CENTER)

while time_left > 0:
    sleep(0.95)
    time_left -= 1
    alert_var.set(f"Alert will be sent in {time_left}s")
    try:
        tk.update()
    except TclError:
        quit()

port = 465

context = ssl.create_default_context()
message = f"""\
Subject: Activity@{now.strftime("%H:%M:%S")}

Someone logged onto your laptop on the {now.strftime("%d/%m/%Y")} at {now.strftime("%H:%M:%S")}"""

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login("9.qk.c.2xmpu@gmail.com", "9.qk.c.2xmpu123")
    server.sendmail("9.qk.c.2xmpu@gmail.com", "jamescaroe@gmail.com", message)
    print("sent")

l.place_forget()
e.place_forget()
alert = Label(tk, text="Alert sent!", bg="black", fg="red", font=(None, 25))
alert.place(relx=0.5, rely=0.5, anchor=CENTER)
tk.update()

while True:
    alert.config(fg="black")
    alert.update()
    sleep(0.5)
    alert.config(fg="red")
    alert.update()
    sleep(0.5)
