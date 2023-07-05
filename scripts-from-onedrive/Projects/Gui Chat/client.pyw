import socket
import threading
from tkinter import *
import tkinter.scrolledtext
from tkinter import simpledialog
import os
from tkinter.colorchooser import askcolor
from tkinter.messagebox import showerror
import pyttsx3
from playsound import playsound

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
root = Tk()
root.withdraw()
root.iconbitmap(default="icon/cmd_icon.ico")
IP = simpledialog.askstring("IP", "Enter IP address", parent=root)  # "192.168.1.252"  # input("Enter IP: ")
nickname = simpledialog.askstring("Nickname", "Choose a nickname", parent=root)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client.connect((IP, 55555))
except:
    showerror("Error", "The server is not active, \ngot you have the wrong IP address")
    os._exit(0)

stop_thread = False


def receive():
    global text_box, in_focus, stop_thread, nickname
    while True:
        if stop_thread:
            break
        try:
            message = client.recv(1024).decode("ascii")
            if message == "NICK":
                client.send(nickname.encode("ascii"))
                msg = client.recv(1024).decode("ascii")
                print(msg)
                if msg == "TAKEN":
                    print("received taken")
                    try:
                        showerror("Taken", "Nickname taken", parent=root)
                    except Exception as e:
                        print(e)
                    os._exit(0)
            else:
                text_box.config(state="normal")
                text_box.insert(INSERT, message)
                text_box.config(state="disabled")
                text_box.see(END)
                if to_top:
                    tk.attributes('-topmost', 1)
                    tk.attributes('-topmost', 0)
                print(in_focus)
                if not in_focus:
                    print("voice:", voice_notif)
                    print("sound:", sound_notif)
                    if voice_notif:
                        if not message.startswith("Connected"):
                            index = 0
                            for ind, el in enumerate(message):
                                if el == ":":
                                    index = ind
                            print(index)
                            if message[:index] != nickname:
                                if index != 0:
                                    engine.say(f"You have a new message from {message[:index]}")
                                    engine.runAndWait()
                                    print("not 0")
                                else:
                                    print("is 0")
                                    engine.say(message)
                                    engine.runAndWait()

                    elif sound_notif:
                        playsound("sound\\ding.mp3")
                        print("played sound")

                    elif read_msg:
                        engine.say(message)
                        engine.runAndWait()

        except Exception as e:
            print(f"Error: {e}")
            print(f"An error occurred")
            client.close()
            stop_thread = True
            break


def write():
    while True:
        global stop_thread
        if stop_thread:
            break

        send_button.waitvar(wait)
        message = f"{nickname}: {msg_box.get('1.0', END)[:-1]}"
        wait.set(0)
        msg_box.delete('1.0', END)

        if message != "":
            try:
                if message[len(nickname)+2] == '/':
                    if str(message[len(nickname)+2:]).startswith('/exit'):
                        client.send("EXIT".encode("ascii"))
                        stop_thread = True
                        os._exit(0)

                    else:
                        print("Invalid Command!")
                else:
                    client.send(message.encode("ascii"))
            except Exception as e:
                showerror("Error", e)


def swap():
    global dark, colour
    if dark:
        tk.config(bg="#f8f4f4")
        text_box.config(bg="#ffffff", fg="#000000")
        msg_box.config(bg="#ffffff", fg="#000000")
        for button in buttons:
            button.config(bg="#f8f4f4", fg="#000000")
        dark = False
        colour.set("Light")

    else:
        tk.config(bg="#2b2b2b")
        text_box.config(bg="#333333", fg="#a9b7c6")  # #403c44
        msg_box.config(bg="#333333", fg="#a9b7c6")
        for button in buttons:
            button.config(bg="#2b2b2b", fg="#a9b7c6")
        dark = True
        colour.set("Dark")


def change_bg():
    global colour
    bg_colour = askcolor()[1]
    print(bg_colour)
    tk.config(bg=bg_colour)
    colour.set("Custom")


def change_msg_bg():
    global colour
    bg_colour = askcolor()[1]
    print(bg_colour)
    text_box.config(bg=bg_colour)
    msg_box.config(bg=bg_colour)
    colour.set("Custom")


def change_but_bg():
    global colour
    bg_colour = askcolor()[1]
    print(bg_colour)
    for button in buttons:
        button.config(bg=bg_colour)
    colour.set("Custom")


def change_but_fg():
    global colour
    fg_colour = askcolor()[1]
    print(fg_colour)
    for button in buttons:
        button.config(fg=fg_colour)
    colour.set("Custom")


def change_text_col():
    global colour
    txt_colour = askcolor()[1]
    print(txt_colour)
    msg_box.config(fg=txt_colour)
    text_box.config(fg=txt_colour)
    colour.set("Custom")


def in_focus_bool(args):
    global in_focus
    if in_focus:
        in_focus = False
    else:
        in_focus = True


def voice_notif_swap():
    global voice_notif, voice_notif_var, sound_notif, read_msg
    if voice_notif:
        voice_notif_var.set("Voice\nnotifications:\nOFF")
        voice_notif = False
    else:
        voice_notif_var.set("Voice\nnotifications:\nON")
        voice_notif = True
        if sound_notif:
            sound_notif_swap()
        if read_msg:
            read_msg_swap()


def sound_notif_swap():
    global sound_notif, sound_notif_var, voice_notif, read_msg
    if sound_notif:
        sound_notif_var.set("Sound\nnotifications:\nOFF")
        sound_notif = False
    else:
        sound_notif_var.set("Sound\nnotifications:\nON")
        sound_notif = True
        if voice_notif:
            voice_notif_swap()
        if read_msg:
            read_msg_swap()


def read_msg_swap():
    global read_msg, read_msg_var, sound_notif, voice_notif
    if read_msg:
        read_msg_var.set("Read\nmessages:\nOFF")
        read_msg = False
    else:
        read_msg_var.set("Read\nmessages:\nON")
        read_msg = True
        if sound_notif:
            sound_notif_swap()
        if voice_notif:
            voice_notif_swap()


def to_top_swap():
    global to_top, to_top_var
    if to_top:
        to_top_var.set("Jump to \ntop:\nOFF")
        to_top = False
    else:
        to_top_var.set("Jump to \ntop:\nON")
        to_top = True


dark = False
in_focus = False
buttons = []

tk = Toplevel()
tk.minsize(625, 500)
tk.resizable(False, False)
tk.title("TCP Chat")
tk.config(bg="#f8f4f4")
tk.iconbitmap("icon/cmd_icon.ico")
tk.protocol("WM_DELETE_WINDOW", lambda: os._exit(0))
tk.bind("<FocusIn>", in_focus_bool)
tk.bind("<FocusOut>", in_focus_bool)

colour = StringVar(tk)
colour.set("Light")
dark_light = Button(tk, textvariable=colour, width=10, height=2, command=swap)
dark_light.place(x=47, y=40, anchor=CENTER)
buttons.append(dark_light)

bg_colour_button = Button(tk, text="Bg colour", width=10, height=2, command=change_bg)
bg_colour_button.place(x=47, y=105, anchor=CENTER)
buttons.append(bg_colour_button)

msg_bg_colour = Button(tk, text="Msg bg", width=10, height=2, command=change_msg_bg)
msg_bg_colour.place(x=47, y=170, anchor=CENTER)
buttons.append(msg_bg_colour)

button_colour_button = Button(tk, text="Button bg", width=10, height=2, command=change_but_bg)
button_colour_button.place(x=47, y=235, anchor=CENTER)
buttons.append(button_colour_button)

button_fg_colour_button = Button(tk, text="Button text", width=10, height=2, command=change_but_fg)
button_fg_colour_button.place(x=47, y=300, anchor=CENTER)
buttons.append(button_fg_colour_button)

text_colour_button = Button(tk, text="Text colour", width=10, height=2, command=change_text_col)
text_colour_button.place(x=47, y=365, anchor=CENTER)
buttons.append(text_colour_button)

voice_notif = False
voice_notif_var = StringVar()
voice_notif_var.set("Voice\nnotifications:\nOFF")
voice_notification_button = Button(tk, textvariable=voice_notif_var, command=voice_notif_swap)
voice_notification_button.place(x=579, y=53, anchor=CENTER)
buttons.append(voice_notification_button)

sound_notif = False
sound_notif_var = StringVar()
sound_notif_var.set("Sound\nnotifications:\nOFF")
sound_notification_button = Button(tk, textvariable=sound_notif_var, command=sound_notif_swap)
sound_notification_button.place(x=579, y=153, anchor=CENTER)
buttons.append(sound_notification_button)

read_msg = False
read_msg_var = StringVar()
read_msg_var.set("Read\nmessages:\nOFF")
read_msg_button = Button(tk, textvariable=read_msg_var, width=10, command=read_msg_swap)
read_msg_button.place(x=579, y=253, anchor=CENTER)
buttons.append(read_msg_button)

to_top = False
to_top_var = StringVar()
to_top_var.set("Jump to \ntop:\nOFF")
to_top_button = Button(tk, textvariable=to_top_var, width=10, command=to_top_swap)
to_top_button.place(x=579, y=353, anchor=CENTER)
buttons.append(to_top_button)

text_box = tkinter.scrolledtext.ScrolledText(tk, width=60, fg="#000000", font=("Helvetica", 10), state='disabled')
text_box.pack(pady=10)

msg_box = Text(tk, width=45, height=2, font=("Helvetica", 10))
msg_box.place(relx=0.405, rely=0.9, anchor=CENTER)

wait = IntVar()
wait.set(0)
send_button = Button(tk, text="Send", width=10, height=2, command=lambda: wait.set(1))
send_button.place(relx=0.785, rely=0.9, anchor=CENTER)
buttons.append(send_button)

msg_box.bind("<Return>", lambda e: send_button.invoke())

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()

tk.mainloop()
