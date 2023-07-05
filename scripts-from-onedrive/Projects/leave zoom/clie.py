import socket
from pynput.keyboard import Controller, Key
from Modules.user import entry


c = Controller()
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((entry("IP address of server"), 55555))


while True:
    msg = client.recv(1024).decode("ascii")

    if msg == "LEAVE":
        c.press(Key.alt)
        c.press("q")
        c.release(Key.alt)
        c.release("q")

    elif msg == "MUTE":
        c.press(Key.alt)
        c.press("a")
        c.release(Key.alt)
        c.release("a")

    elif msg == "VIDEO":
        c.press(Key.alt)
        c.press("v")
        c.release(Key.alt)
        c.release("v")

    elif msg == "HAND":
        c.press(Key.alt)
        c.press("y")
        c.release(Key.alt)
        c.release("y")

    elif msg == "FULL":
        c.press(Key.alt)
        c.press("f")
        c.release(Key.alt)
        c.release("f")

    elif msg == "CHAT":
        c.press(Key.alt)
        c.press("h")
        c.release(Key.alt)
        c.release("h")
