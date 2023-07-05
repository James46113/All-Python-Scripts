import socket
from tkinter import Tk, Button, LEFT, StringVar
from threading import Thread

hostname = socket.gethostname()
host = socket.gethostbyname(hostname)
port = 55555
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
print(f"IP: {server.getsockname()[0]}\nPORT: {server.getsockname()[1]}")
server.listen()


def handle(client):
    def check():
        while True:
            try:
                client.send("testing".encode("ascii"))
            except Exception:
                tk.destroy()
                break

    tk = Tk()
    tk.attributes('-topmost', True)
    #tk.overrideredirect(True)
    Button(tk, text="LEAVE", width=9, height=2, bg="#ff0000", command=lambda: client.send("LEAVE".encode("ascii"))).pack(side=LEFT)
    Button(tk, text="MUTE/UNMUTE", width=12, height=2, bg="#ff0000", command=lambda: client.send("MUTE".encode("ascii"))).pack(side=LEFT)
    Button(tk, text="START/STOP VIDEO", width=15, height=2, bg="#ff0000", command=lambda: client.send("VIDEO".encode("ascii"))).pack(side=LEFT)
    Button(tk, text="RAISE HAND", width=11, height=2, bg="#ff0000", command=lambda: client.send("HAND".encode("ascii"))).pack(side=LEFT)
    Button(tk, text="FULL SCREEN", width=11, height=2, bg="#ff0000", command=lambda: client.send("FULL".encode("ascii"))).pack(side=LEFT)
    Button(tk, text="SHOW CHAT", width=11, height=2, bg="#ff0000", command=lambda: client.send("CHAT".encode("ascii"))).pack(side=LEFT)
    tk.geometry("%dx%d+%d+%d" % (543, 20, -10, -35))
    t = Thread(target=check)
    t.start()
    tk.mainloop()


def receive():
    while True:
        client, address = server.accept()
        print(address)
        t = Thread(target=handle, args=(client,))
        t.start()


t = Thread(target=receive)
t.start()