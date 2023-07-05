import socket
import threading
from tkinter import *
import tkinter.scrolledtext
from tkinter import simpledialog

HOST = "127.0.0.1"
PORT = 9090


class Client:
    def __init__(self, host, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))

        root = Tk()
        root.withdraw()

        self.nickname = simpledialog.askstring("Nickname", "Please choose a nickname", parent=root)

        self.gui_done = False
        self.running = True

        gui_thread = threading.Thread(target=self.gui_loop)
        receive_thread = threading.Thread(target=self.receive)

        gui_thread.start()
        receive_thread.start()

    def gui_loop(self):
        self.tk = Toplevel()
        self.tk.config(bg="Lightgrey")

        self.chat_label = Label(self.tk, text="Chat:", bg="Lightgrey", font=("Arial, 12"))
        self.chat_label.pack(padx=20, pady=5)

        self.text_area = tkinter.scrolledtext.ScrolledText(self.tk, state="disabled")
        self.text_area.pack(padx=20, pady=5)

        self.msg_label = Label(self.tk, text="Message:", bg="Lightgrey", font=("Arial, 12"))
        self.msg_label.pack(padx=20, pady=5)

        self.input_area = Text(self.tk, height=3)
        self.input_area.pack(padx=20, pady=5)

        self.send_button = Button(self.tk, text="Send", font=("Arial", 12), command=self.write)
        self.send_button.pack(padx=20, pady=5)

    def write(self):
        pass

    def receive(self):
        pass
