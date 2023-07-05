import socket
try:
    import pyttsx3
except ImportError:
    import time
    import os
    os.system("pip install pyttsx3")
    time.sleep(60)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("192.168.1.252", 55555))  # 192.169.1.241
print("connected")
engine = pyttsx3.init()

while True:
    engine.say(client.recv(1024).decode("ascii"))
    engine.runAndWait()
